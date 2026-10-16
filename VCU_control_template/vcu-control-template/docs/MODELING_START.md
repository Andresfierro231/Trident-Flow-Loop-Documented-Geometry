# Computational team: choose inputs both teams can trace

Start with **Requirements**, filtered to Modeling or Shared. Each row states the purpose, proposed owner, applicability, source, current evidence and open question. “Needs review” does not mean a choice is approved.

## 1. Define the intended comparison

Record the configuration/run, predicted quantities, relevant accuracy and model version. State whether the use is 1-D, CFD/conjugate heat transfer, or both. Separate fluid temperatures, wall temperatures, sensor response and effective fitted zone temperatures.

## 2. Complete one property-selection form

Open **Form material**. The supplied insulation equation is only a reported candidate. Before selecting it, record:

- The material/product and evidence that it is installed on the relevant component.
- The exact source, edition, page/table/equation and coefficients or data.
- Input/output units, temperature convention and composition basis.
- The property’s valid temperature, pressure, composition and phase domain; the actual intended use range belongs beside it.
- Source uncertainty, fitting error, interpolation and outside-domain behavior.
- Why this source is appropriate, alternatives considered, and independent check values.
- The implementation/version, reviewer, approved scope and effective configuration.

Repeat the record for each needed property. Fluid density, heat capacity, enthalpy, viscosity, conductivity and expansion behavior may be needed; solids require the properties used by the actual storage and conduction model. Surface and contact properties need their own evidence or explicit assumptions.

**A correlation’s validity range is not an operating limit.** VCU Prop-30, air and water need explicit circuit and run assignments. The draft Prop-30 campaign does not qualify the other fluids. Keep intrinsic properties separate from fitted effective conductances or thermal capacities.

## 3. Agree on physical and mathematical boundaries

For TLEP/BREP, first obtain the installed connectivity, valve states, tank level, vent/pressure and thermal contact evidence. Then specify the model cut plane and mass/pressure/thermal conditions for each model. No throughflow alone does not establish an adiabatic branch.

For electrical heating, define where real electrical power is measured, which elements are energized, the spatial source and how external losses and heater/structure storage enter the energy balance. Keep controller commands, electrical input and heat delivered to the modeled volume distinct. Do not reuse secondary-fluid heater duty formulas without adaptation.

For cooling, identify coolant inlet/outlet, measurement planes, fluid properties, flow and feedback history. Explain the selected boundary condition and its uncertainty. State gravity, pressure reference, flow regime, closures, contact assumptions and numerical settings for the intended use.

## 4. Separate calibration from validation

Use the phase request IDs to agree on the data return. Freeze property, sensor-map and model versions before blind comparisons. A case reassigned to fitting cannot independently validate the revised model. Preserve accepted intervals, exclusions, covariance assumptions, conservation checks, resolution sensitivity and applicability limits.

## 5. Record the decision separately

Keep the evidence type unchanged when a reviewer accepts a choice. In **Requirements**, use **Selected choice**, **Decision scope / rationale**, **Reviewer / date** and **Effective configuration** for the decision. Then update **Review state**. Preserve any conflicting evidence and identify the reason for the selection.

The maintainer transfers accepted inputs into the applicable baseline tables. Filling the material form does not silently activate its equation in a model or the Materials sheet.
