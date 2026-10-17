# Instruments

What this site's sensors **are**, as distinct from what its channels are
called. The channel map next door says a channel is in `degC`; this says the
channel comes from a `SCAIN-062U-12` thermocouple on a 16-bit acquisition
module at the cooler heater.

The shape follows [ADR-028](https://github.com/UT-Computational-NE/neutron-os/blob/main/docs/adrs/adr-028-a-site-declares-its-instruments.md),
which takes it from INL's DeepLynx: an `[instrument_class]` is a class of
hardware and an `[[instrument]]` is one installed unit of it, with the
channels that unit feeds attached to it. A deployment running DeepLynx can
sync against this; nothing here depends on DeepLynx being installed.

## Files

| File | What it is |
|---|---|
| `instruments.toml` | The declaration the platform reads |
| `sources/ACU-STNCL-sensors.xlsx` | The site's own sensor list, as received |
| `sensors.csv` | The same three sheets, flattened, so it is diffable and greppable |

`instruments.toml` is transcribed from the workbook. Where the two disagree,
the workbook is right and the transcription is a bug.

## What it declares

Twenty instrument classes and forty-eight installed units, covering sixty-one
of the map's one hundred and nineteen channels.

**A property nobody wrote down is absent.** It is not zero and it is not
guessed. Two cases are worth calling out because the temptation is real:

- The mass flow controller is an `MC-1SLPM` and the pressure controller is a
  `PCD-15PSID`. Those almost certainly mean a one standard-litre-per-minute
  and a fifteen-PSI-differential full scale. No unit is declared for either,
  because a model number is a string a vendor chose and reading units out of
  it is right until the day it is not. They are questions for the site.
- The air velocity channels have no unit for the same reason.

## What the document settled

**The 16-bit module explains the values we were serving as temperatures.**
The workbook says every thermocouple measurement goes through an
AutomationDirect P1-04THM, 16-bit, roughly 200 ms. That is declared here as
`bits = 16` on the module, and every thermocouple inherits it by naming the
module as its reader. One line reaches twenty-four channels.

It is declared as the module's **width**, not as a list of fault values. The
values 65535, 3276.75 and 655.35 that appear in the data are what a 16-bit
word and its fixed-point scalings look like, which is a strong inference and
still an inference. Turning the width into a quarantine rule is the
platform's job and it must be labelled as inferred when it does it.

**The pressure transmitters have a range and an accuracy.** 0 to 50 psia, and
0.25 **percent of span** — recorded as `uncertainty_pct_of_span`, never as
`uncertainty`, because a relative accuracy stored where an absolute one is
expected is wrong by a factor of the span.

**Salt temperature and surface temperature are different measurements.** The
workbook distinguishes them per thermocouple in its location column, for
example "Exp Tank Downpipe" against "Exp Tank Downpipe Salt Temp". That
distinction is carried into `placement` here, and it is what a `role` on those
channels should be derived from rather than from the tag.

## What it found

**Eight instruments are installed and send us nothing.**

| Instrument | What it is |
|---|---|
| `RADAR0` | Vega VEGAPULS 6S level radar on the exp tank |
| `FLOW1` | Sporian Thermaflow 700 flow meter |
| `VFD1` | WEG CFW500 driving the cooler fan |
| `ODISI-7100` | LUNA fibre, marked "not yet implemented" in the source |
| `TC-ETH1.1` | Thermocouple on the exp tank band heater |
| `TC-MH1.1`, `.2`, `.3` | Three thermocouples, no location recorded |

A flat channel map cannot represent an instrument we receive nothing from, so
this was unrepresentable rather than merely unnoticed.

`TC-ETH1.1` and the PV `NCDT1:HEAT:TC-ET1_1` may be one instrument spelled two
ways. They are **not** joined here. A name that looks like a typo is sometimes
two real instruments, and this site already has a second one: `TC-EP2_1` is a
PV with no row in the sensor list at all.

**Fifty-eight mapped channels have no instrument behind them**, in two groups:

- **Thirty-nine heater channels.** Thirteen band heaters, each with
  `OutputPower`, `SetPoint` and `Time`. The workbook lists the thermocouples
  that watch the heaters and never lists the heaters themselves.
- **Nineteen gas controller channels** under `FC1`, `PC1` and `MFC1`. The
  workbook names `FC31` and `PC11`. These look like earlier names for the same
  two Alicat devices, which would make them history under a former tag rather
  than four devices. Not merged, for the same reason as above.

## Adding to this file

State what is written down somewhere. If the only evidence is a model number
or a habit, it belongs in a question to the site, not here. A wrong value in
this file is invisible downstream; an absent one is not.
