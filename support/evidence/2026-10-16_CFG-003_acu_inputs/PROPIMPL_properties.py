"""Validated, vectorized thermophysical-property models in SI units."""

from __future__ import annotations

from dataclasses import asdict, dataclass
from enum import Enum
from math import isfinite
from typing import Mapping, Protocol, Sequence

import numpy as np
from numpy.typing import ArrayLike, NDArray


class PropertyValidationError(ValueError):
    """Raised when a property definition is incomplete or physically invalid."""


class PropertyRangeError(ValueError):
    """Raised when evaluation is requested outside a declared valid range."""


class OutOfRangePolicy(str, Enum):
    """Explicit handling outside the property model's evidence range."""

    ERROR = "error"
    CLAMP = "clamp"
    LINEAR_EXTRAPOLATE = "linear_extrapolate"


@dataclass(frozen=True)
class PropertyProvenance:
    """Traceable source identity without a runtime dependency on that source."""

    source_id: str
    source_path: str
    source_revision: str
    evidence_status: str
    notes: str

    def __post_init__(self) -> None:
        for field_name in ("source_id", "source_path", "source_revision", "evidence_status"):
            if not getattr(self, field_name).strip():
                raise PropertyValidationError(f"provenance {field_name} must not be empty")


@dataclass(frozen=True)
class PropertyMetadata:
    """Units, applicability, and provenance shared by every property model."""

    property_name: str
    units: str
    valid_temperature_K: tuple[float, float]
    valid_pressure_Pa: tuple[float, float] | None
    out_of_range: OutOfRangePolicy
    provenance: PropertyProvenance

    def __post_init__(self) -> None:
        if not self.property_name or not self.units:
            raise PropertyValidationError("property_name and units must not be empty")
        _validate_range(self.valid_temperature_K, "valid_temperature_K", positive=True)
        if self.valid_pressure_Pa is not None:
            _validate_range(self.valid_pressure_Pa, "valid_pressure_Pa", positive=True)
        expected_units = {
            "density": "kg/m^3",
            "heat_capacity": "J/(kg*K)",
            "conductivity": "W/(m*K)",
            "viscosity": "Pa*s",
            "surface_tension": "N/m",
            "emissivity": "1",
        }
        expected = expected_units.get(self.property_name)
        if expected is not None and self.units != expected:
            raise PropertyValidationError(
                f"{self.property_name} units must be canonical SI units {expected!r}"
            )


class ScalarProperty(Protocol):
    """Temperature/pressure property contract used by fluids and solids."""

    metadata: PropertyMetadata

    def evaluate(
        self, temperature_K: ArrayLike, pressure_Pa: ArrayLike | None = None
    ) -> NDArray[np.float64]: ...


def _validate_range(values: tuple[float, float], name: str, *, positive: bool) -> None:
    low, high = values
    if not isfinite(low) or not isfinite(high) or low >= high:
        raise PropertyValidationError(f"{name} must be two finite increasing values")
    if positive and low <= 0.0:
        raise PropertyValidationError(f"{name} must be positive")


def _as_finite_array(value: ArrayLike, name: str) -> NDArray[np.float64]:
    array = np.asarray(value, dtype=float)
    if not np.all(np.isfinite(array)):
        raise PropertyValidationError(f"{name} must contain only finite values")
    return array


def _checked_inputs(
    metadata: PropertyMetadata,
    temperature_K: ArrayLike,
    pressure_Pa: ArrayLike | None,
) -> tuple[NDArray[np.float64], NDArray[np.float64] | None]:
    temperature = _as_finite_array(temperature_K, "temperature_K")
    if np.any(temperature <= 0.0):
        raise PropertyValidationError("temperature_K must be greater than 0 K")
    pressure = None if pressure_Pa is None else _as_finite_array(pressure_Pa, "pressure_Pa")
    if pressure is not None:
        try:
            temperature, pressure = np.broadcast_arrays(temperature, pressure)
        except ValueError as exc:
            raise PropertyValidationError(
                "temperature_K and pressure_Pa are not broadcast-compatible"
            ) from exc
        if np.any(pressure <= 0.0):
            raise PropertyValidationError("pressure_Pa must be positive")

    _enforce_or_transform_range(temperature, metadata.valid_temperature_K, metadata)
    if pressure is not None and metadata.valid_pressure_Pa is not None:
        _enforce_or_transform_range(pressure, metadata.valid_pressure_Pa, metadata)
    return temperature, pressure


def _enforce_or_transform_range(
    values: NDArray[np.float64], limits: tuple[float, float], metadata: PropertyMetadata
) -> None:
    if metadata.out_of_range is OutOfRangePolicy.ERROR:
        if np.any((values < limits[0]) | (values > limits[1])):
            raise PropertyRangeError(
                f"{metadata.property_name} input outside valid range {limits}"
            )


def _evaluation_temperature(
    temperature: NDArray[np.float64], metadata: PropertyMetadata
) -> NDArray[np.float64]:
    if metadata.out_of_range is OutOfRangePolicy.CLAMP:
        return np.clip(temperature, *metadata.valid_temperature_K)
    return temperature


@dataclass(frozen=True)
class ConstantProperty:
    """A positive constant over an explicitly bounded evidence range."""

    metadata: PropertyMetadata
    value: float

    def __post_init__(self) -> None:
        if not isfinite(self.value) or self.value <= 0.0:
            raise PropertyValidationError(f"{self.metadata.property_name} value must be positive")

    def evaluate(
        self, temperature_K: ArrayLike, pressure_Pa: ArrayLike | None = None
    ) -> NDArray[np.float64]:
        temperature, pressure = _checked_inputs(self.metadata, temperature_K, pressure_Pa)
        del pressure
        return np.full(temperature.shape, self.value, dtype=float)


@dataclass(frozen=True)
class PolynomialProperty:
    """Polynomial in kelvin with coefficients in ascending-power order."""

    metadata: PropertyMetadata
    coefficients: tuple[float, ...]

    def __post_init__(self) -> None:
        if not self.coefficients or not all(isfinite(value) for value in self.coefficients):
            raise PropertyValidationError("polynomial coefficients must be finite and nonempty")
        temperatures = np.linspace(*self.metadata.valid_temperature_K, 257)
        if np.any(self._evaluate_unchecked(temperatures) <= 0.0):
            raise PropertyValidationError(
                f"{self.metadata.property_name} polynomial is not positive over its valid range"
            )

    def _evaluate_unchecked(self, temperature_K: NDArray[np.float64]) -> NDArray[np.float64]:
        result = np.zeros_like(temperature_K, dtype=float)
        for coefficient in reversed(self.coefficients):
            result = result * temperature_K + coefficient
        return result

    def evaluate(
        self, temperature_K: ArrayLike, pressure_Pa: ArrayLike | None = None
    ) -> NDArray[np.float64]:
        temperature, _ = _checked_inputs(self.metadata, temperature_K, pressure_Pa)
        result = self._evaluate_unchecked(_evaluation_temperature(temperature, self.metadata))
        if np.any(result <= 0.0):
            raise PropertyValidationError(f"{self.metadata.property_name} evaluated nonpositive")
        return result


@dataclass(frozen=True)
class ExponentialInverseTemperatureProperty:
    """Property ``a*exp(b/T + c/T^2 + ...)`` with explicit Kelvin inputs."""

    metadata: PropertyMetadata
    coefficients: tuple[float, ...]

    def __post_init__(self) -> None:
        if len(self.coefficients) < 2 or not all(
            isfinite(value) for value in self.coefficients
        ):
            raise PropertyValidationError(
                "exponential inverse-temperature coefficients must contain finite a and b"
            )
        if self.coefficients[0] <= 0.0:
            raise PropertyValidationError(
                "exponential inverse-temperature scale must be positive"
            )
        temperatures = np.linspace(*self.metadata.valid_temperature_K, 257)
        values = self._evaluate_unchecked(temperatures)
        if not np.all(np.isfinite(values)) or np.any(values <= 0.0):
            raise PropertyValidationError(
                f"{self.metadata.property_name} exponential model is invalid over its range"
            )

    def _evaluate_unchecked(self, temperature_K: NDArray[np.float64]) -> NDArray[np.float64]:
        exponent = np.zeros_like(temperature_K, dtype=float)
        for inverse_power, coefficient in enumerate(self.coefficients[1:], start=1):
            exponent += coefficient / temperature_K**inverse_power
        return self.coefficients[0] * np.exp(exponent)

    def evaluate(
        self, temperature_K: ArrayLike, pressure_Pa: ArrayLike | None = None
    ) -> NDArray[np.float64]:
        temperature, _ = _checked_inputs(self.metadata, temperature_K, pressure_Pa)
        result = self._evaluate_unchecked(_evaluation_temperature(temperature, self.metadata))
        if not np.all(np.isfinite(result)) or np.any(result <= 0.0):
            raise PropertyValidationError(f"{self.metadata.property_name} evaluated invalid")
        return result

@dataclass(frozen=True)
class TabulatedProperty:
    """One-dimensional linear interpolation with explicit range behavior."""

    metadata: PropertyMetadata
    temperature_K: tuple[float, ...]
    values: tuple[float, ...]

    def __post_init__(self) -> None:
        temperatures = np.asarray(self.temperature_K, dtype=float)
        values = np.asarray(self.values, dtype=float)
        if temperatures.ndim != 1 or len(temperatures) < 2 or values.shape != temperatures.shape:
            raise PropertyValidationError("tabulated properties require equal 1-D arrays of length >= 2")
        if not np.all(np.isfinite(temperatures)) or not np.all(np.diff(temperatures) > 0.0):
            raise PropertyValidationError("tabulated temperatures must be finite and strictly increasing")
        if not np.all(np.isfinite(values)) or np.any(values <= 0.0):
            raise PropertyValidationError("tabulated property values must be finite and positive")
        declared = self.metadata.valid_temperature_K
        if declared[0] < temperatures[0] or declared[1] > temperatures[-1]:
            raise PropertyValidationError("declared valid range extends beyond tabulated temperatures")

    def evaluate(
        self, temperature_K: ArrayLike, pressure_Pa: ArrayLike | None = None
    ) -> NDArray[np.float64]:
        temperature, _ = _checked_inputs(self.metadata, temperature_K, pressure_Pa)
        query = _evaluation_temperature(temperature, self.metadata)
        result = np.interp(query, self.temperature_K, self.values)
        if self.metadata.out_of_range is OutOfRangePolicy.LINEAR_EXTRAPOLATE:
            low = query < self.temperature_K[0]
            high = query > self.temperature_K[-1]
            low_slope = (self.values[1] - self.values[0]) / (
                self.temperature_K[1] - self.temperature_K[0]
            )
            high_slope = (self.values[-1] - self.values[-2]) / (
                self.temperature_K[-1] - self.temperature_K[-2]
            )
            result = np.where(low, self.values[0] + low_slope * (query - self.temperature_K[0]), result)
            result = np.where(high, self.values[-1] + high_slope * (query - self.temperature_K[-1]), result)
        if np.any(result <= 0.0):
            raise PropertyValidationError(f"{self.metadata.property_name} evaluated nonpositive")
        return np.asarray(result, dtype=float)


@dataclass(frozen=True)
class MaterialProperties:
    """Named collection selected by facility configuration."""

    material_id: str
    material_kind: str
    revision: str
    calibration_eligible: bool
    properties: Mapping[str, ScalarProperty]

    def __post_init__(self) -> None:
        if self.material_kind not in {"fluid", "solid", "insulation"}:
            raise PropertyValidationError("material_kind must be fluid, solid, or insulation")
        required = {"density", "heat_capacity", "conductivity"}
        if self.material_kind == "fluid":
            required.add("viscosity")
        missing = sorted(required - self.properties.keys())
        if missing:
            raise PropertyValidationError(
                f"material {self.material_id!r} missing properties: {', '.join(missing)}"
            )

    def evaluate(
        self,
        property_name: str,
        temperature_K: ArrayLike,
        pressure_Pa: ArrayLike | None = None,
    ) -> NDArray[np.float64]:
        try:
            model = self.properties[property_name]
        except KeyError as exc:
            raise PropertyValidationError(
                f"material {self.material_id!r} has no property {property_name!r}"
            ) from exc
        return model.evaluate(temperature_K, pressure_Pa)

    def to_dict(self) -> dict[str, object]:
        """Expand model definitions and provenance for a resolved run bundle."""

        return {
            "material_id": self.material_id,
            "material_kind": self.material_kind,
            "revision": self.revision,
            "calibration_eligible": self.calibration_eligible,
            "properties": {
                name: property_to_dict(model) for name, model in self.properties.items()
            },
        }


def property_to_dict(model: ScalarProperty) -> dict[str, object]:
    """Serialize one property without losing coefficients or copied table values."""

    metadata = {
        "property_name": model.metadata.property_name,
        "units": model.metadata.units,
        "valid_temperature_K": list(model.metadata.valid_temperature_K),
        "valid_pressure_Pa": (
            None
            if model.metadata.valid_pressure_Pa is None
            else list(model.metadata.valid_pressure_Pa)
        ),
        "out_of_range": model.metadata.out_of_range.value,
        "provenance": asdict(model.metadata.provenance),
    }
    if isinstance(model, ConstantProperty):
        definition: dict[str, object] = {"model": "constant", "value": model.value}
    elif isinstance(model, PolynomialProperty):
        definition = {
            "model": "polynomial",
            "coefficients": list(model.coefficients),
            "coefficient_order": "ascending_power_of_temperature_K",
        }
    elif isinstance(model, ExponentialInverseTemperatureProperty):
        definition = {
            "model": "exponential_inverse_temperature",
            "coefficients": list(model.coefficients),
            "equation": "a*exp(b/T_K + c/T_K^2 + ...)",
        }
    elif isinstance(model, TabulatedProperty):
        definition = {
            "model": "tabulated_linear",
            "temperature_K": list(model.temperature_K),
            "values": list(model.values),
        }
    else:
        raise PropertyValidationError(f"cannot serialize property model {type(model).__name__}")
    return {**metadata, **definition}


def metadata_from_dict(
    property_name: str, value: Mapping[str, object], provenance: PropertyProvenance
) -> PropertyMetadata:
    """Build metadata from a validated YAML mapping."""

    required = {"units", "valid_temperature_K", "out_of_range"}
    missing = sorted(required - value.keys())
    if missing:
        raise PropertyValidationError(
            f"property {property_name!r} missing fields: {', '.join(missing)}"
        )
    temperature_range = _pair(value["valid_temperature_K"], "valid_temperature_K")
    pressure_value = value.get("valid_pressure_Pa")
    pressure_range = None if pressure_value is None else _pair(pressure_value, "valid_pressure_Pa")
    try:
        policy = OutOfRangePolicy(str(value["out_of_range"]))
    except ValueError as exc:
        raise PropertyValidationError(
            f"property {property_name!r} has unsupported out_of_range policy"
        ) from exc
    return PropertyMetadata(
        property_name=property_name,
        units=str(value["units"]),
        valid_temperature_K=temperature_range,
        valid_pressure_Pa=pressure_range,
        out_of_range=policy,
        provenance=provenance,
    )


def _pair(value: object, name: str) -> tuple[float, float]:
    if not isinstance(value, Sequence) or isinstance(value, (str, bytes)) or len(value) != 2:
        raise PropertyValidationError(f"{name} must contain exactly two values")
    return float(value[0]), float(value[1])
