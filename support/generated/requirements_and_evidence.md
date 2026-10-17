# VCU requirements and evidence register

Generated from `VCU_inputs.xlsx`. Edit the workbook and regenerate. Draft; no release approval is implied.

Evidence type and review state are independent. All proposed owners require team confirmation.

## Requirements

### C01

**Package:** Configuration


**Field:** Facility and configuration ID


**Purpose:** Tie measurements to one physical setup.


**Responsible team:** Experimental team


**Applicability:** VCU; every configuration and affected run


**Requirement source:** P0


**Requirement locator:** Section 3 Method, document facility configuration


**Current evidence:** VCU; prototype ID VCU-REV9-DRAFT-001


**Evidence type:** Reported


**Evidence source:** USER / current workbook


**Evidence locator:** Facility selection; Start sheet


**Review state:** Needs review


**Unresolved question:** Which installed configuration and effective date does this identify?


**Selected choice:** Unknown


**Decision scope / rationale:** Unknown


**Reviewer / date:** Unknown


**Effective configuration:** Unknown


### C02

**Package:** Configuration


**Field:** Effective date and change history


**Purpose:** Explain what changed between datasets.


**Responsible team:** Experimental team


**Applicability:** VCU; every configuration and affected run


**Requirement source:** P0; DESIGN


**Requirement locator:** Campaign execution conventions; proposed revision log


**Current evidence:** 2026-10-16 / VCU-REV9-DRAFT-002: PTC-X removed from active sensor and calibration records at the repository owner's request. Documentation change only; no physical removal or installed-hardware verification is asserted. 2026-10-16 / VCU-REV9-DRAFT-003: added ten insulation coverage regions and the diagram; all coverage Unknown pending evidence.


**Evidence type:** Reported


**Evidence source:** USER


**Evidence locator:** Start effective date and change summary; previous record saved at support/checkpoints/2026-10-16_VCU-REV9-DRAFT-002/. Owner-approved insulation feature plan in the Codex session, 2026-10-16; installed coverage remains unconfirmed.


**Review state:** Needs review


**Unresolved question:** Record effective date, author, changed item, reason, previous/new evidence, affected runs and whether recalibration or model revalidation is needed.


**Selected choice:** Unknown


**Decision scope / rationale:** Unknown


**Reviewer / date:** Unknown


**Effective configuration:** Unknown


### C03

**Package:** Shared


**Field:** Reviewer, date and approved use


**Purpose:** Record an actual release decision separately from evidence type.


**Responsible team:** Facility lead / package reviewer


**Applicability:** VCU; every configuration and affected run


**Requirement source:** P0


**Requirement locator:** Approval record and Section 3 Disposition


**Current evidence:** Unknown


**Evidence type:** Unknown


**Evidence source:** None supplied


**Evidence locator:** Not available


**Review state:** Needs information


**Unresolved question:** Who may release the package, and for which experiment/model use?


**Selected choice:** Unknown


**Decision scope / rationale:** Unknown


**Reviewer / date:** Unknown


**Effective configuration:** Unknown


### C04

**Package:** Shared


**Field:** Source revision and file hash


**Purpose:** Make the geometry baseline reproducible.


**Responsible team:** Experimental + computational


**Applicability:** VCU; 1-D and CFD / CHT


**Requirement source:** R9


**Requirement locator:** Sheet 8 source identity


**Current evidence:** Rev9 is user-selected best current geometry for new work; existing solver/results remain versioned Rev8.


**Evidence type:** Reported


**Evidence source:** VSEL; WORK


**Evidence locator:** See cited Sources locators and Current knowledge / Native channels; CFG-002 evidence bundle


**Review state:** Needs review


**Unresolved question:** Confirm installed configuration and dates; no physical release implied.


**Selected choice:** Rev9 for new configuration documentation; no historical run migration


**Decision scope / rationale:** Transferred documented working understanding; provisional use only; no installed or package release approval.


**Reviewer / date:** Unknown


**Effective configuration:** VCU-REV9-DRAFT-007


### C05

**Package:** Configuration


**Field:** Coordinate datum and axes


**Purpose:** Give every location the same reference.


**Responsible team:** Experimental + computational


**Applicability:** VCU; 1-D and CFD / CHT


**Requirement source:** R9


**Requirement locator:** Sheets 1 and 7


**Current evidence:** B origin; x right; y up; n normal; B-C-D-E-F-G-H-A-B


**Evidence type:** CAD-derived


**Evidence source:** R9


**Evidence locator:** Sheets 1, 7


**Review state:** Needs review


**Unresolved question:** Identify these points on a dated hardware photo.


**Selected choice:** Unknown


**Decision scope / rationale:** Unknown


**Reviewer / date:** Unknown


**Effective configuration:** Unknown


### C06

**Package:** Configuration


**Field:** Segment endpoints and straight length


**Purpose:** Define the length being measured.


**Responsible team:** Experimental team


**Applicability:** VCU; 1-D and CFD / CHT


**Requirement source:** P0; SEG


**Requirement locator:** Method geometry map; segment rows


**Current evidence:** Upcomer B-C 1219.200 mm; other spans in SEG


**Evidence type:** CAD-derived


**Evidence source:** SEG


**Evidence locator:** upcomer row: reference_length_mm and length_basis


**Review state:** Needs review


**Unresolved question:** Measure axis-end span; do not substitute virtual-corner length.


**Selected choice:** Unknown


**Decision scope / rationale:** Unknown


**Reviewer / date:** Unknown


**Effective configuration:** Unknown


### C07

**Package:** Configuration


**Field:** Installed inclination and gravity direction


**Purpose:** Determine elevation changes and buoyancy orientation.


**Responsible team:** Experimental team


**Applicability:** VCU; 1-D and CFD / CHT


**Requirement source:** P0; R9


**Requirement locator:** Method geometry map; sheets 1-2


**Current evidence:** Geometry-derived inclined axes about 10.8 deg; working local gravity (0,-1,0). Installed gravity survey absent.


**Evidence type:** Modeling assumption


**Evidence source:** VSEL; WORK


**Evidence locator:** See cited Sources locators and Current knowledge / Native channels; CFG-002 evidence bundle


**Review state:** Needs review


**Unresolved question:** Installed tilt/gravity and uncertainty still need survey.


**Selected choice:** Use current local drawing frame and geometry-derived inclination provisionally


**Decision scope / rationale:** Transferred documented working understanding; provisional use only; no installed or package release approval.


**Reviewer / date:** Unknown


**Effective configuration:** VCU-REV9-DRAFT-007


### C08

**Package:** Configuration


**Field:** Bend geometry and length basis


**Purpose:** Avoid replacing a chord with an arc.


**Responsible team:** Experimental + computational


**Applicability:** VCU; 1-D and CFD / CHT


**Requirement source:** SEG


**Requirement locator:** Bend rows and length_basis


**Current evidence:** Three torus arcs; G-H recovered spine qualified; exact joined path unresolved


**Evidence type:** CAD-derived


**Evidence source:** SEG; R9


**Evidence locator:** Bend rows; sheet 2


**Review state:** Needs review


**Unresolved question:** How will the physical bend be measured and represented?


**Selected choice:** Unknown


**Decision scope / rationale:** Unknown


**Reviewer / date:** Unknown


**Effective configuration:** Unknown


### C09

**Package:** Configuration


**Field:** Pipe inside diameter


**Purpose:** Set fluid area, inventory and hydraulic dimension.


**Responsible team:** Experimental team


**Applicability:** VCU; 1-D and CFD / CHT


**Requirement source:** P0; DIA


**Requirement locator:** Geometry map; Main swept loop


**Current evidence:** CAD main bore absent. GEO-008 retains 26.64 mm rounded nominal ID for provisional main piping; not a CAD-extracted bore or installed measurement. Local spool bores differ.


**Evidence type:** Reported


**Evidence source:** DIA; VSEL


**Evidence locator:** Main swept loop; GEO-008 main nominal ID; CAD dimensions tab


**Review state:** Needs review


**Unresolved question:** Confirm actual bore/specification and local restrictions; keep CAD null.


**Selected choice:** Unknown


**Decision scope / rationale:** Unknown


**Reviewer / date:** Unknown


**Effective configuration:** Unknown


### C10

**Package:** Configuration


**Field:** Pipe outside diameter


**Purpose:** Set wall and external thermal geometry.


**Responsible team:** Experimental team


**Applicability:** VCU; 1-D and CFD / CHT


**Requirement source:** DIA


**Requirement locator:** Main swept loop row


**Current evidence:** 33.401 mm CAD OD


**Evidence type:** CAD-derived


**Evidence source:** DIA


**Evidence locator:** Main swept loop / outer_diameter_mm


**Review state:** Needs review


**Unresolved question:** Confirm installed OD and measurement uncertainty.


**Selected choice:** Unknown


**Decision scope / rationale:** Unknown


**Reviewer / date:** Unknown


**Effective configuration:** Unknown


### C11

**Package:** Configuration


**Field:** Pipe material grade and certificate


**Purpose:** Identify the solid whose properties will be used.


**Responsible team:** Experimental team


**Applicability:** VCU; 1-D and CFD / CHT


**Requirement source:** P0; MAT


**Requirement locator:** Geometry map; VCU Piping


**Current evidence:** 316L, nominal 1-inch schedule 40 reported


**Evidence type:** Reported


**Evidence source:** MAT


**Evidence locator:** VCU Piping lines 23-27


**Review state:** Needs review


**Unresolved question:** Provide purchase/specification or material certificate.


**Selected choice:** Unknown


**Decision scope / rationale:** Unknown


**Reviewer / date:** Unknown


**Effective configuration:** Unknown


### C12

**Package:** Configuration


**Field:** Dimension uncertainty and method


**Purpose:** Propagate measurement uncertainty without using CAD print precision.


**Responsible team:** Experimental team


**Applicability:** VCU; 1-D and CFD / CHT


**Requirement source:** P0; DESIGN


**Requirement locator:** Measurement uncertainties; proposed geometry uncertainty field


**Current evidence:** Unknown


**Evidence type:** Unknown


**Evidence source:** None supplied


**Evidence locator:** Not available


**Review state:** Needs information


**Unresolved question:** Record method, instrument, repeatability and uncertainty units for each dimension.


**Selected choice:** Unknown


**Decision scope / rationale:** Unknown


**Reviewer / date:** Unknown


**Effective configuration:** Unknown


### C13

**Package:** Configuration


**Field:** Insulation product and layer order


**Purpose:** Identify the actual thermal stack.


**Responsible team:** Experimental team


**Applicability:** VCU; 1-D and CFD / CHT


**Requirement source:** P0; MAT


**Requirement locator:** Geometry map; VCU insulation


**Current evidence:** Ordinary main piping (upcomer/downcomer and four corners): fiberglass MAIN-INS; heater: calcium-aluminum-silicate HEATER-INS strip only, no additional fiberglass.


**Evidence type:** Reported


**Evidence source:** VREG; VTOP


**Evidence locator:** VREG regional YAML and ADR-0025/0026; VTOP corner/LF-01 correction; user reaffirmation 2026-10-16


**Review state:** Needs review


**Unresolved question:** Which product and layers are installed on this exact segment?


**Selected choice:** Unknown


**Decision scope / rationale:** Unknown


**Reviewer / date:** Unknown


**Effective configuration:** Unknown


### C14

**Package:** Configuration


**Field:** Insulation thickness by section


**Purpose:** Set the thermal resistance geometry.


**Responsible team:** Experimental team


**Applicability:** VCU; 1-D and CFD / CHT


**Requirement source:** P0; MAT


**Requirement locator:** Geometry map; VCU insulation


**Current evidence:** Reported estimates: ordinary insulated regions 50.8 mm (2 in); heater strip 6.35 mm (1/4 in). Not installed thickness measurements.


**Evidence type:** Reported


**Evidence source:** VREG; VTOP


**Evidence locator:** VREG regional YAML and ADR-0025/0026; VTOP corner/LF-01 correction; user reaffirmation 2026-10-16


**Review state:** Needs review


**Unresolved question:** Measure each layer; do not apply either value everywhere.


**Selected choice:** Unknown


**Decision scope / rationale:** Unknown


**Reviewer / date:** Unknown


**Effective configuration:** Unknown


### C15

**Package:** Configuration


**Field:** Coverage start/end, gaps and condition


**Purpose:** Capture uninsulated heat-loss paths.


**Responsible team:** Experimental team


**Applicability:** VCU; 1-D and CFD / CHT


**Requirement source:** P0


**Requirement locator:** Method: facility and fluid configuration; geometry map


**Current evidence:** Reported coverage known for all ten regions: upcomer/downcomer, four corners and heater insulated; pre-cooler/jacket/post-cooler D-E bare. LF-01 covered. Exact local contacts and transitions remain open.


**Evidence type:** Reported


**Evidence source:** VREG; VTOP


**Evidence locator:** VREG regional YAML and ADR-0025/0026; VTOP corner/LF-01 correction; user reaffirmation 2026-10-16


**Review state:** Needs review


**Unresolved question:** Supply evidence and request review.


**Selected choice:** Unknown


**Decision scope / rationale:** Unknown


**Reviewer / date:** Unknown


**Effective configuration:** Unknown


### C16

**Package:** Shared


**Field:** Insulation contact and support details


**Purpose:** Represent contact resistance and support heat paths.


**Responsible team:** Experimental + computational


**Applicability:** VCU; 1-D and CFD / CHT


**Requirement source:** P0; HEAT


**Requirement locator:** Geometry map; VCU Insulation


**Current evidence:** Perfect thermal contact is a user-directed model assumption (VINS), not a surveyed contact condition. Actual supports, gaps and layers remain open.


**Evidence type:** Modeling assumption


**Evidence source:** VINS


**Evidence locator:** insulation.yaml contact


**Review state:** Needs review


**Unresolved question:** Is there evidence of contact, compression, gaps or support conduction?


**Selected choice:** Unknown


**Decision scope / rationale:** Unknown


**Reviewer / date:** Unknown


**Effective configuration:** Unknown


### C17

**Package:** Configuration


**Field:** Dated overview and detail photos


**Purpose:** Make the configuration recognizable and auditable.


**Responsible team:** Experimental team


**Applicability:** VCU; every configuration and affected run


**Requirement source:** USER; DESIGN


**Requirement locator:** Requested form-like geometry package


**Current evidence:** Supplied images are illustrations; not a dated installed survey


**Evidence type:** Reported


**Evidence source:** USER


**Evidence locator:** Supplied VCU image captions


**Review state:** Needs review


**Unresolved question:** Attach photos showing endpoints, insulation and sensors with scale.


**Selected choice:** Unknown


**Decision scope / rationale:** Unknown


**Reviewer / date:** Unknown


**Effective configuration:** Unknown


### C18

**Package:** Configuration


**Field:** Fluid identity and circuit assignment


**Purpose:** Avoid confusing working fluid, coolant and room air.


**Responsible team:** Experimental team


**Applicability:** VCU; every configuration and affected run


**Requirement source:** USER; P0


**Requirement locator:** Fluid scope; facility/fluid configuration


**Current evidence:** VCU options Prop-30/air/water; primary fill selected per run. Jacket water reported; ambient air role distinct.


**Evidence type:** Reported


**Evidence source:** USER; FLUIDCFG; XWALK; WORK


**Evidence locator:** See cited Sources locators and Current knowledge / Native channels; CFG-002 evidence bundle


**Review state:** Needs review


**Unresolved question:** Confirm fluid/batch in each acquisition; ambient filename alone is insufficient.


**Selected choice:** Run-specific primary fill; reported water jacket coolant


**Decision scope / rationale:** Transferred documented working understanding; provisional use only; no installed or package release approval.


**Reviewer / date:** Unknown


**Effective configuration:** VCU-REV9-DRAFT-007


### C19

**Package:** Configuration


**Field:** Composition and concentration basis


**Purpose:** Select the correct property family.


**Responsible team:** Experimental team


**Applicability:** VCU mixtures


**Requirement source:** P0


**Requirement locator:** Method fluid configuration


**Current evidence:** Prop-30: 30% propylene glycol by mass reported


**Evidence type:** Reported


**Evidence source:** MAT; PG


**Evidence locator:** MAT lines 19-21; PG 30 wt% note


**Review state:** Needs review


**Unresolved question:** Identify formulation, preparation and concentration verification.


**Selected choice:** Unknown


**Decision scope / rationale:** Unknown


**Reviewer / date:** Unknown


**Effective configuration:** Unknown


### C20

**Package:** Configuration


**Field:** Batch, fill inventory and condition


**Purpose:** Reproduce thermal capacity and hydraulic state.


**Responsible team:** Experimental team


**Applicability:** VCU; every configuration and affected run


**Requirement source:** P0; P2


**Requirement locator:** P0 fluid configuration; P2 fill record


**Current evidence:** Unknown


**Evidence type:** Unknown


**Evidence source:** None supplied


**Evidence locator:** Not available


**Review state:** Needs information


**Unresolved question:** Record batch, fill date, mass/level, contamination and trapped-gas evidence.


**Selected choice:** Unknown


**Decision scope / rationale:** Unknown


**Reviewer / date:** Unknown


**Effective configuration:** Unknown


### C21

**Package:** Configuration


**Field:** Sensor hardware ID and type


**Purpose:** Identify the installed instrument independently of a CAD label.


**Responsible team:** Experimental team


**Applicability:** VCU; every configuration and affected run


**Requirement source:** P0; SNS


**Requirement locator:** Instrumentation documentation; sensor rows


**Current evidence:** Active geometry: 12 STC, 4 main PTC, 4 LF and 2 JTC = 22 references; 20 main-loop references. Original extraction has 23 including excluded PTC-X. Native core inventory has 20 channels incl. Amb/Tank; LF is not mapped.


**Evidence type:** Reported


**Evidence source:** VSEL; WORK; XWALK


**Evidence locator:** See cited Sources locators and Current knowledge / Native channels; CFG-002 evidence bundle


**Review state:** Needs review


**Unresolved question:** Installed inventory, serials and fiber channels still need evidence.


**Selected choice:** Exclude PTC-X from active register; preserve original reference


**Decision scope / rationale:** Transferred documented working understanding; provisional use only; no installed or package release approval.


**Reviewer / date:** Unknown


**Effective configuration:** VCU-REV9-DRAFT-007


### C22

**Package:** Configuration


**Field:** Sensor model and serial number


**Purpose:** Connect the device to its calibration evidence.


**Responsible team:** Experimental team


**Applicability:** VCU; every configuration and affected run


**Requirement source:** P0


**Requirement locator:** Method instrumentation documentation


**Current evidence:** Unknown


**Evidence type:** Unknown


**Evidence source:** None supplied


**Evidence locator:** Not available


**Review state:** Needs information


**Unresolved question:** Supply evidence and request review.


**Selected choice:** Unknown


**Decision scope / rationale:** Unknown


**Reviewer / date:** Unknown


**Effective configuration:** Unknown


### C23

**Package:** Configuration


**Field:** DAQ channel crosswalk


**Purpose:** Connect a physical sensor to the recorded signal.


**Responsible team:** Experimental team


**Applicability:** VCU; every configuration and affected run


**Requirement source:** P0


**Requirement locator:** Method instrumentation documentation


**Current evidence:** User-selected STC1-12/PTC1-4 matching Rev9 references; JTC-B=PTC5 inlet and JTC-A=PTC6 outlet. Amb/Tank native names have no accepted XYZ.


**Evidence type:** Reported


**Evidence source:** VSEL; WORK; XWALK


**Evidence locator:** See cited Sources locators and Current knowledge / Native channels; CFG-002 evidence bundle


**Review state:** Needs review


**Unresolved question:** Verify cable/DAQ identity and historical run applicability; do not map by name alone.


**Selected choice:** Use Native channels working register; LF remains unbound


**Decision scope / rationale:** Transferred documented working understanding; provisional use only; no installed or package release approval.


**Reviewer / date:** Unknown


**Effective configuration:** VCU-REV9-DRAFT-007


### C24

**Package:** Configuration


**Field:** Sensor segment, endpoint and axial distance


**Purpose:** Locate the sensor without scaling an image.


**Responsible team:** Experimental team


**Applicability:** VCU; 1-D and CFD / CHT


**Requirement source:** SNS


**Requirement locator:** nearest_endpoint, nearest_distance_mm


**Current evidence:** Rev9 axial references preserved; STC5 is B+942.186081 mm, PTC4 H+63.716137 mm. User selects these for new work.


**Evidence type:** CAD-derived


**Evidence source:** VSEL; WORK


**Evidence locator:** See cited Sources locators and Current knowledge / Native channels; CFG-002 evidence bundle


**Review state:** Needs review


**Unresolved question:** Survey actual sensing/contact point and historical installation dates.


**Selected choice:** Use Rev9 axial references; physical sensing tips remain unknown


**Decision scope / rationale:** Transferred documented working understanding; provisional use only; no installed or package release approval.


**Reviewer / date:** Unknown


**Effective configuration:** VCU-REV9-DRAFT-007


### C25

**Package:** Configuration


**Field:** Circumferential angle and zero reference


**Purpose:** Locate a sensor around the pipe circumference.


**Responsible team:** Experimental team


**Applicability:** VCU; 1-D and CFD / CHT


**Requirement source:** USER; DESIGN


**Requirement locator:** Circumference clarification; coordinate guide


**Current evidence:** Convention proposed: projected top; vertical pipe uses drawing +x


**Evidence type:** Modeling assumption


**Evidence source:** DESIGN


**Evidence locator:** Coordinate convention


**Review state:** Needs review


**Unresolved question:** Confirm convention; measure angle. No sensor angles have been supplied.


**Selected choice:** Unknown


**Decision scope / rationale:** Unknown


**Reviewer / date:** Unknown


**Effective configuration:** Unknown


### C26

**Package:** Configuration


**Field:** Radius, insertion depth and sensing extent


**Purpose:** Distinguish mount, sheath, junction and fiber active region.


**Responsible team:** Experimental team


**Applicability:** VCU; 1-D and CFD / CHT


**Requirement source:** P0; SNS


**Requirement locator:** Installed coupling; reference_basis


**Current evidence:** CAD does not define verified TC junctions or optical sensing extents


**Evidence type:** CAD-derived


**Evidence source:** SNS; R9


**Evidence locator:** reference_basis; sheets 5-6


**Review state:** Needs review


**Unresolved question:** Record physical junction or fiber extent; a mount centroid is not a tip.


**Selected choice:** Unknown


**Decision scope / rationale:** Unknown


**Reviewer / date:** Unknown


**Effective configuration:** Unknown


### C27

**Package:** Configuration


**Field:** Attachment and thermal coupling


**Purpose:** Interpret what temperature a sensor measures.


**Responsible team:** Experimental team


**Applicability:** VCU; 1-D and CFD / CHT


**Requirement source:** P0


**Requirement locator:** Method instrumentation documentation


**Current evidence:** All STCs contact bare pipe locally per user; insulated parent regions remain per CURRENT. LF-01 locally covered. Actual attachment details unknown.


**Evidence type:** Reported


**Evidence source:** VSEL; VTOP; CURRENT


**Evidence locator:** See cited Sources locators and Current knowledge / Native channels; CFG-002 evidence bundle


**Review state:** Needs review


**Unresolved question:** Attachment, window width, junction footprint, response and local contact resistance unknown.


**Selected choice:** Bare local STC contact; do not infer whole parent leg bare


**Decision scope / rationale:** Transferred documented working understanding; provisional use only; no installed or package release approval.


**Reviewer / date:** Unknown


**Effective configuration:** VCU-REV9-DRAFT-007


### C28

**Package:** Configuration


**Field:** Calibration date, certificate and validity


**Purpose:** Establish calibration provenance.


**Responsible team:** Experimental team


**Applicability:** VCU; every configuration and affected run


**Requirement source:** P0; DESIGN


**Requirement locator:** Method instrumentation documentation; proposed maintenance/validity extension


**Current evidence:** Plan mentions a prior five-temperature bath; date/certificate not supplied


**Evidence type:** Reported


**Evidence source:** P0


**Evidence locator:** Section 2 apparatus, channel table


**Review state:** Needs review


**Unresolved question:** Provide instrument-specific date, certificate, traceability, next-due or recheck trigger, and validity at the run date.


**Selected choice:** Unknown


**Decision scope / rationale:** Unknown


**Reviewer / date:** Unknown


**Effective configuration:** Unknown


### C29

**Package:** Configuration


**Field:** Calibration range and correction


**Purpose:** Apply corrections only where supported.


**Responsible team:** Experimental team


**Applicability:** VCU; every configuration and affected run


**Requirement source:** P0


**Requirement locator:** Method instrumentation documentation


**Current evidence:** Unknown


**Evidence type:** Unknown


**Evidence source:** None supplied


**Evidence locator:** Not available


**Review state:** Needs information


**Unresolved question:** Supply calibration points, applied correction and residuals with units.


**Selected choice:** Unknown


**Decision scope / rationale:** Unknown


**Reviewer / date:** Unknown


**Effective configuration:** Unknown


### C30

**Package:** Shared


**Field:** Measurement uncertainty and coverage


**Purpose:** Combine uncertainties on a consistent basis.


**Responsible team:** Experimental + computational


**Applicability:** VCU; 1-D and CFD / CHT


**Requirement source:** P0; P1


**Requirement locator:** Instrumentation documentation; Data Acceptance and Uncertainty


**Current evidence:** Unknown


**Evidence type:** Unknown


**Evidence source:** None supplied


**Evidence locator:** Not available


**Review state:** Needs information


**Unresolved question:** State standard/expanded uncertainty, coverage factor, confidence and shared error sources.


**Selected choice:** Unknown


**Decision scope / rationale:** Unknown


**Reviewer / date:** Unknown


**Effective configuration:** Unknown


### C31

**Package:** Configuration


**Field:** Sampling, scaling, filtering and response


**Purpose:** Reproduce recorded signals and temporal response.


**Responsible team:** Experimental team


**Applicability:** VCU; every configuration and affected run


**Requirement source:** P0


**Requirement locator:** Instrumentation documentation and logging


**Current evidence:** Approximately 30 Hz native sampling documented for Sep2/4 only. Filtering/scaling and lag remain run-specific and unqualified.


**Evidence type:** Reported


**Evidence source:** DIAG; FOLLOW


**Evidence locator:** See cited Sources locators and Current knowledge / Native channels; CFG-002 evidence bundle


**Review state:** Needs review


**Unresolved question:** Need instrument response, scaling/filtering and status-code evidence.


**Selected choice:** Use native timebase and per-run metadata; no universal sample-rate assignment


**Decision scope / rationale:** Transferred documented working understanding; provisional use only; no installed or package release approval.


**Reviewer / date:** Unknown


**Effective configuration:** VCU-REV9-DRAFT-007


### C32

**Package:** Configuration


**Field:** Clock synchronization and common-event check


**Purpose:** Align measurements, commands and events.


**Responsible team:** Experimental team


**Applicability:** VCU; every configuration and affected run


**Requirement source:** P0


**Requirement locator:** Method logging and time synchronization


**Current evidence:** Unknown


**Evidence type:** Unknown


**Evidence source:** None supplied


**Evidence locator:** Not available


**Review state:** Needs information


**Unresolved question:** Supply evidence and request review.


**Selected choice:** Unknown


**Decision scope / rationale:** Unknown


**Reviewer / date:** Unknown


**Effective configuration:** Unknown


### C33

**Package:** Shared


**Field:** Mandatory / alternate / diagnostic role


**Purpose:** Define usable channels before selecting results.


**Responsible team:** Experimental + computational


**Applicability:** VCU Prop-30 draft campaign; requalify other fluids


**Requirement source:** P0; P1


**Requirement locator:** P0 acceptance-channel matrix; P1 TC-Luna comparison


**Current evidence:** Main-loop observations STC1-12/PTC1-4; jacket PTC5/6; Amb/Tank auxiliary; LF geometric only. No blanket mandatory-channel acceptance rule selected.


**Evidence type:** Reported


**Evidence source:** WORK; XWALK


**Evidence locator:** See cited Sources locators and Current knowledge / Native channels; CFG-002 evidence bundle


**Review state:** Needs review


**Unresolved question:** Preapprove mandatory/alternate roles for each intended use.


**Selected choice:** Working roles in Native channels


**Decision scope / rationale:** Transferred documented working understanding; provisional use only; no installed or package release approval.


**Reviewer / date:** Unknown


**Effective configuration:** VCU-REV9-DRAFT-007


### C34

**Package:** Configuration


**Field:** Heater element identity and active spans


**Purpose:** Map where electrical heat is generated.


**Responsible team:** Experimental team


**Applicability:** VCU; 1-D and CFD / CHT


**Requirement source:** P0; HEAT; R9


**Requirement locator:** Geometry map; heater note; sheet 4


**Current evidence:** Electrical heater footprint remains unverified. GEO-008 assumes full projected H-A span 0-1346.496215 mm for modeling only; mechanical clamps do not establish active heating.


**Evidence type:** Modeling assumption


**Evidence source:** HEAT; VSEL


**Evidence locator:** GEO-008 lower-leg assumption; original Active heater baseline remains null


**Review state:** Needs review


**Unresolved question:** Survey each energized element; clamp edges and reported total coverage are not active boundaries.


**Selected choice:** Unknown


**Decision scope / rationale:** Unknown


**Reviewer / date:** Unknown


**Effective configuration:** Unknown


### C35

**Package:** Configuration


**Field:** Heater supply and circuit diagram


**Purpose:** Establish the electrical measurement boundary.


**Responsible team:** Experimental team


**Applicability:** VCU; 1-D and CFD / CHT


**Requirement source:** USER; HEAT


**Requirement locator:** Requested power/circuit schematic; heater note


**Current evidence:** Shared voltage source is described as in theory


**Evidence type:** Reported


**Evidence source:** HEAT


**Evidence locator:** Line 19


**Review state:** Needs review


**Unresolved question:** Provide rated elements, wiring, series/parallel layout, switching and measurement points.


**Selected choice:** Unknown


**Decision scope / rationale:** Unknown


**Reviewer / date:** Unknown


**Effective configuration:** Unknown


### C36

**Package:** Shared


**Field:** Measured heater power and uncertainty


**Purpose:** Distinguish input power, controller command and heat entering the loop.


**Responsible team:** Experimental + computational


**Applicability:** VCU; 1-D and CFD / CHT


**Requirement source:** P0; P3; DESIGN


**Requirement locator:** Secondary duty; electrical-heater adaptation


**Current evidence:** Unknown


**Evidence type:** Unknown


**Evidence source:** None supplied


**Evidence locator:** Not available


**Review state:** Needs information


**Unresolved question:** Provide time-resolved real electrical power, meter/waveform basis, losses and storage accounting.


**Selected choice:** Unknown


**Decision scope / rationale:** Unknown


**Reviewer / date:** Unknown


**Effective configuration:** Unknown


### C37

**Package:** Configuration


**Field:** Heater control and monitor signals


**Purpose:** Explain controller actions and protect measurement interpretation.


**Responsible team:** Experimental team


**Applicability:** VCU; every configuration and affected run


**Requirement source:** P0


**Requirement locator:** Method logging; approved operating limits


**Current evidence:** Unknown


**Evidence type:** Unknown


**Evidence source:** None supplied


**Evidence locator:** Not available


**Review state:** Needs information


**Unresolved question:** Record feedback sensor, setpoint, output, on/off state, alarms and wiring reference.


**Selected choice:** Unknown


**Decision scope / rationale:** Unknown


**Reviewer / date:** Unknown


**Effective configuration:** Unknown


### C38

**Package:** Configuration


**Field:** Cooler jacket and active cooling boundaries


**Purpose:** Separate mechanical geometry from effective heat transfer.


**Responsible team:** Experimental team


**Applicability:** VCU; 1-D and CFD / CHT


**Requirement source:** R9


**Requirement locator:** Sheet 3


**Current evidence:** Shell 1017.5875 mm; complete jacket 1030.2875 mm


**Evidence type:** CAD-derived


**Evidence source:** R9


**Evidence locator:** Sheet 3; J-IN/J-OUT


**Review state:** Needs review


**Unresolved question:** Measure active span and preserve shell versus complete-envelope definitions.


**Selected choice:** Unknown


**Decision scope / rationale:** Unknown


**Reviewer / date:** Unknown


**Effective configuration:** Unknown


### C39

**Package:** Configuration


**Field:** Coolant routing and measurement planes


**Purpose:** Bound the measured cooler energy balance.


**Responsible team:** Experimental team


**Applicability:** VCU; 1-D and CFD / CHT


**Requirement source:** P0


**Requirement locator:** Method secondary-side energy-balance boundaries


**Current evidence:** Working jacket inlet JTC-B/PTC5, outlet JTC-A/PTC6; detailed internal routing and wetted sensing planes unverified.


**Evidence type:** Reported


**Evidence source:** VSEL; WORK


**Evidence locator:** See cited Sources locators and Current knowledge / Native channels; CFG-002 evidence bundle


**Review state:** Needs review


**Unresolved question:** Confirm run-specific hoses, bypasses and physical sensing planes.


**Selected choice:** JTC-B/PTC5 inlet; JTC-A/PTC6 outlet


**Decision scope / rationale:** Transferred documented working understanding; provisional use only; no installed or package release approval.


**Reviewer / date:** Unknown


**Effective configuration:** VCU-REV9-DRAFT-007


### C40

**Package:** Configuration


**Field:** Coolant flow and inlet/outlet measurements


**Purpose:** Compute duty with calibrated signals and correct coolant properties.


**Responsible team:** Experimental team


**Applicability:** VCU; 1-D and CFD / CHT


**Requirement source:** P0


**Requirement locator:** Secondary-side boundaries


**Current evidence:** PTC5/6 provide working inlet/outlet temperatures; coolant flow calibration and physical planes are unknown.


**Evidence type:** Reported


**Evidence source:** VSEL; WORK; FOLLOW


**Evidence locator:** See cited Sources locators and Current knowledge / Native channels; CFG-002 evidence bundle


**Review state:** Needs review


**Unresolved question:** Obtain measured coolant flow, units, calibration, properties and timing.


**Selected choice:** Use temperature roles provisionally; do not invent flow or measured duty


**Decision scope / rationale:** Transferred documented working understanding; provisional use only; no installed or package release approval.


**Reviewer / date:** Unknown


**Effective configuration:** VCU-REV9-DRAFT-007


### C41

**Package:** Configuration


**Field:** Cooler feedback and setpoint history


**Purpose:** Distinguish an imposed model condition from actual control behavior.


**Responsible team:** Experimental team


**Applicability:** VCU; every configuration and affected run


**Requirement source:** P0


**Requirement locator:** Method logging and time synchronization


**Current evidence:** Chiller on/off contributes to hot-plateau oscillations per user. CAL-004 finds provisional temperature associations, not control causality.


**Evidence type:** Reported


**Evidence source:** OPCYCLE; FOLLOW


**Evidence locator:** See cited Sources locators and Current knowledge / Native channels; CFG-002 evidence bundle


**Review state:** Needs review


**Unresolved question:** Need controller sensor, setpoint/deadband, switching and exact intervals.


**Selected choice:** Treat oscillatory plateaus as potentially cyclic operation


**Decision scope / rationale:** Transferred documented working understanding; provisional use only; no installed or package release approval.


**Reviewer / date:** Unknown


**Effective configuration:** VCU-REV9-DRAFT-007


### C42

**Package:** Configuration


**Field:** TLEP/BREP connections and termination


**Purpose:** Locate branch interfaces and attached hardware.


**Responsible team:** Experimental team


**Applicability:** VCU; 1-D and CFD / CHT


**Requirement source:** R9


**Requirement locator:** Sheet 4


**Current evidence:** Each modeled exit tube is 469.900 mm; IN/OUT means near/far, not flow direction


**Evidence type:** CAD-derived


**Evidence source:** R9


**Evidence locator:** Sheet 4 endpoints and connection qualifications


**Review state:** Needs review


**Unresolved question:** Confirm valve/tank connectivity, actual cut plane and installed branch geometry.


**Selected choice:** Unknown


**Decision scope / rationale:** Unknown


**Reviewer / date:** Unknown


**Effective configuration:** Unknown


### C43

**Package:** Configuration


**Field:** Tank level, vent/pressure and valve states


**Purpose:** Define hydraulic and thermal branch conditions.


**Responsible team:** Experimental team


**Applicability:** VCU; every configuration and affected run


**Requirement source:** P0


**Requirement locator:** Method document facility/fluid configuration


**Current evidence:** Unknown


**Evidence type:** Unknown


**Evidence source:** None supplied


**Evidence locator:** Not available


**Review state:** Needs information


**Unresolved question:** Record fill level, gas/vent pressure, valve/bypass state and changes during the run.


**Selected choice:** Unknown


**Decision scope / rationale:** Unknown


**Reviewer / date:** Unknown


**Effective configuration:** Unknown


### C44

**Package:** Configuration


**Field:** Ambient temperature/RH and outer-surface locations


**Purpose:** Resolve room gradients and condensation conditions.


**Responsible team:** Experimental team


**Applicability:** VCU Prop-30 draft campaign; requalify other fluids


**Requirement source:** P0


**Requirement locator:** Method environmental and condensation measurements


**Current evidence:** Amb is a native ambient reference with unaccepted coordinates; room RH/two-station installation unverified. Bare STC contact does not establish an exposed ambient-surface measurement.


**Evidence type:** Reported


**Evidence source:** XWALK; VSEL; FOLLOW


**Evidence locator:** See cited Sources locators and Current knowledge / Native channels; CFG-002 evidence bundle


**Review state:** Needs review


**Unresolved question:** Identify room sensor placement and actual exposed surface channels.


**Selected choice:** Retain Amb role without inventing XYZ or RH channels


**Decision scope / rationale:** Transferred documented working understanding; provisional use only; no installed or package release approval.


**Reviewer / date:** Unknown


**Effective configuration:** VCU-REV9-DRAFT-007


### C45

**Package:** Configuration


**Field:** Operating limits and alarm/interlock basis


**Purpose:** Reference facility-approved limits for this setup.


**Responsible team:** Facility lead / package reviewer


**Applicability:** VCU; every configuration and affected run


**Requirement source:** P0


**Requirement locator:** Method approved operating limits


**Current evidence:** Unknown


**Evidence type:** Unknown


**Evidence source:** None supplied


**Evidence locator:** Not available


**Review state:** Needs information


**Unresolved question:** Provide approved limits and source; do not infer them from property-fit ranges.


**Selected choice:** Unknown


**Decision scope / rationale:** Unknown


**Reviewer / date:** Unknown


**Effective configuration:** Unknown


### C46

**Package:** Configuration


**Field:** Run ID, raw files and event log


**Purpose:** Tie data, changes and analysis intervals to the configuration.


**Responsible team:** Experimental team


**Applicability:** VCU; every configuration and affected run


**Requirement source:** P0; P4


**Requirement locator:** Campaign execution conventions; Phase 4 records


**Current evidence:** VCU inventory: 23 native sources, 22 readable; 19 CSVs are supplementary, not independent experiments. July29 unreadable; preserve hashes and run/event records.


**Evidence type:** Reported


**Evidence source:** DIAG; TRIAGE; FOLLOW


**Evidence locator:** See cited Sources locators and Current knowledge / Native channels; CFG-002 evidence bundle


**Review state:** Needs review


**Unresolved question:** No universal experiment/fluid assignment; July15 ambient-named file may be liquid continuation.


**Selected choice:** Use source/run hashes and run-specific event logs


**Decision scope / rationale:** Transferred documented working understanding; provisional use only; no installed or package release approval.


**Reviewer / date:** Unknown


**Effective configuration:** VCU-REV9-DRAFT-007


### M01

**Package:** Modeling


**Field:** Intended use and prediction targets


**Purpose:** Define what comparison would be useful.


**Responsible team:** Computational team


**Applicability:** VCU; 1-D and CFD / CHT


**Requirement source:** USER; MODEL


**Requirement locator:** Both models; four model stages


**Current evidence:** Unknown


**Evidence type:** Unknown


**Evidence source:** None supplied


**Evidence locator:** Not available


**Review state:** Needs information


**Unresolved question:** Identify outputs, required accuracy and excluded uses for each model.


**Selected choice:** Unknown


**Decision scope / rationale:** Unknown


**Reviewer / date:** Unknown


**Effective configuration:** Unknown


### M02

**Package:** Modeling


**Field:** Model/software/input revision


**Purpose:** Reproduce an analysis with the same inputs.


**Responsible team:** Computational team


**Applicability:** VCU; 1-D and CFD / CHT


**Requirement source:** MODEL; P2


**Requirement locator:** Run outputs; model freeze


**Current evidence:** This documentation uses WORK v3 / regional v7 / material v3. Historical numerical studies keep original Rev8/insulation-v5 inputs.


**Evidence type:** Reported


**Evidence source:** WORK; CURRENT; FOLLOW


**Evidence locator:** See cited Sources locators and Current knowledge / Native channels; CFG-002 evidence bundle


**Review state:** Needs review


**Unresolved question:** Record actual solver/input/property versions separately in every run.


**Selected choice:** VCU-REV9-DRAFT-007 for current documentation only


**Decision scope / rationale:** Transferred documented working understanding; provisional use only; no installed or package release approval.


**Reviewer / date:** Unknown


**Effective configuration:** VCU-REV9-DRAFT-007


### M03

**Package:** Modeling


**Field:** Model domain and geometry simplifications


**Purpose:** Make excluded branches and healed geometry visible.


**Responsible team:** Computational team


**Applicability:** VCU; 1-D and CFD / CHT


**Requirement source:** R9; MODEL


**Requirement locator:** Sheet 8 qualifications; model stages


**Current evidence:** Rev9 selected as provisional working geometry; main nominal ID 26.64 mm is separate from CAD null. H-A projected union is not an exact connected centerline; G-H reconstructed spline remains qualified.


**Evidence type:** Modeling assumption


**Evidence source:** VSEL; SEG


**Evidence locator:** GEO-008 Why H-A has a qualification; Geometry notes; CAD dimensions tab


**Review state:** Needs review


**Unresolved question:** Which simplifications are accepted and what sensitivity supports them?


**Selected choice:** Unknown


**Decision scope / rationale:** Unknown


**Reviewer / date:** Unknown


**Effective configuration:** Unknown


### M04

**Package:** Modeling


**Field:** 1-D cell and CFD region mapping


**Purpose:** Compare the right model quantity with each sensor.


**Responsible team:** Experimental + computational


**Applicability:** VCU; 1-D and CFD / CHT


**Requirement source:** P0


**Requirement locator:** Method geometry/model map


**Current evidence:** STCs observe outside wall locally on bare pipe; PTC1-4 treated as centerline fluid; JTC/PTC5/6 are jacket boundaries, not main-loop nodes.


**Evidence type:** Modeling assumption


**Evidence source:** VSEL; WORK; XWALK


**Evidence locator:** See cited Sources locators and Current knowledge / Native channels; CFG-002 evidence bundle


**Review state:** Needs review


**Unresolved question:** Actual junction depths, response, finite footprints and mesh interpolation unknown.


**Selected choice:** Working observation operators in Calibration and Native channels


**Decision scope / rationale:** Transferred documented working understanding; provisional use only; no installed or package release approval.


**Reviewer / date:** Unknown


**Effective configuration:** VCU-REV9-DRAFT-007


### M05

**Package:** Modeling


**Field:** Flow mode and governing equations


**Purpose:** Identify zero-flow, prescribed-flow or buoyancy-coupled assumptions.


**Responsible team:** Computational team


**Applicability:** VCU; 1-D and CFD / CHT


**Requirement source:** MODEL


**Requirement locator:** The four physical-model stages


**Current evidence:** M0-M3 and a separate reduced-zone model are described


**Evidence type:** Reported


**Evidence source:** MODEL


**Evidence locator:** Stage table and reduced-zone paragraph


**Review state:** Needs review


**Unresolved question:** Select governing equations, gravity/pressure reference, compressibility or Boussinesq approximation, and laminar/turbulent treatment with validity; identify any effective-zone assumptions.


**Selected choice:** Unknown


**Decision scope / rationale:** Unknown


**Reviewer / date:** Unknown


**Effective configuration:** Unknown


### M06

**Package:** Modeling


**Field:** Storage, conjugate heat transfer and contact model


**Purpose:** Represent fluid, wall, insulation and interface physics.


**Responsible team:** Computational team


**Applicability:** VCU; 1-D and CFD / CHT


**Requirement source:** MODEL; P2


**Requirement locator:** Model stages; reduced-zone thermal model


**Current evidence:** Perfect insulation contact is a user-directed modeling assumption; local bare STCs and distinct fiberglass/ceramic regions retained.


**Evidence type:** Modeling assumption


**Evidence source:** VINS; VSEL; CURRENT; ASSUME


**Evidence locator:** See cited Sources locators and Current knowledge / Native channels; CFG-002 evidence bundle


**Review state:** Needs review


**Unresolved question:** Model-specific storage, axial paths and contact sensitivity require review.


**Selected choice:** Keep separate fluid/wall/insulation paths and declared contact assumption


**Decision scope / rationale:** Transferred documented working understanding; provisional use only; no installed or package release approval.


**Reviewer / date:** Unknown


**Effective configuration:** VCU-REV9-DRAFT-007


### M07

**Package:** Modeling


**Field:** TLEP/BREP mathematical boundary conditions


**Purpose:** Translate documented branch hardware into equations.


**Responsible team:** Computational team


**Applicability:** VCU; 1-D and CFD / CHT


**Requirement source:** USER; P0


**Requirement locator:** Exit-pipe alignment request; configuration record


**Current evidence:** Shared default omits BREP (ASM-020) and retains TLEP with experiment-specific temperature/pressure (ASM-021). No installed VCU boundary values are known.


**Evidence type:** Modeling assumption


**Evidence source:** ASSUME


**Evidence locator:** See cited Sources locators and Current knowledge / Native channels; CFG-002 evidence bundle


**Review state:** Needs review


**Unresolved question:** Select exact VCU termination planes and measured states before use; no-throughflow is not adiabatic.


**Selected choice:** Provisional model-domain defaults only


**Decision scope / rationale:** Transferred documented working understanding; provisional use only; no installed or package release approval.


**Reviewer / date:** Unknown


**Effective configuration:** VCU-REV9-DRAFT-007


### M08

**Package:** Modeling


**Field:** Heater source distribution and power balance


**Purpose:** Refer electrical measurements to the modeled control volume.


**Responsible team:** Experimental + computational


**Applicability:** VCU; 1-D and CFD / CHT


**Requirement source:** P0; P3; DESIGN


**Requirement locator:** Duty definitions; VCU electrical adaptation


**Current evidence:** GEO-008 assumes uniform extent over H-A projected span 1346.496215 mm. Real electrical power, spatial distribution, efficiency and heater/structure storage remain unresolved.


**Evidence type:** Modeling assumption


**Evidence source:** VSEL; HEAT


**Evidence locator:** GEO-008 lower-leg modeling assumption; Thermal spans keeps installed footprint unknown


**Review state:** Needs review


**Unresolved question:** Specify spatial source, meter boundary, external losses and storage without double counting.


**Selected choice:** Unknown


**Decision scope / rationale:** Unknown


**Reviewer / date:** Unknown


**Effective configuration:** Unknown


### M09

**Package:** Modeling


**Field:** Cooler mathematical boundary and feedback


**Purpose:** Match model inputs to measured coolant/control conditions.


**Responsible team:** Experimental + computational


**Applicability:** VCU; 1-D and CFD / CHT


**Requirement source:** P0; MODEL


**Requirement locator:** Secondary boundaries; cooler forms


**Current evidence:** Working PTC5 inlet/PTC6 outlet; measured cooler forcing varies; user reports chiller cycling. Coefficient/flow and active-span choices unresolved.


**Evidence type:** Reported


**Evidence source:** VSEL; WORK; OPCYCLE; FOLLOW


**Evidence locator:** See cited Sources locators and Current knowledge / Native channels; CFG-002 evidence bundle


**Review state:** Needs review


**Unresolved question:** Need flow, routing, controller logs and qualified boundary/model choice.


**Selected choice:** Run-specific cooler input; compare cyclic mean/amplitude separately


**Decision scope / rationale:** Transferred documented working understanding; provisional use only; no installed or package release approval.


**Reviewer / date:** Unknown


**Effective configuration:** VCU-REV9-DRAFT-007


### M10

**Package:** Modeling


**Field:** External convection and radiation model


**Purpose:** Represent exchange with room and surfaces.


**Responsible team:** Computational team


**Applicability:** VCU; 1-D and CFD / CHT


**Requirement source:** P2; MODEL


**Requirement locator:** Reduced-zone heat loss; thermal network


**Current evidence:** Reported insulated regions and bare D-E are known; jacket heat exchange is with water where present. Ambient coupling/emissivity unresolved.


**Evidence type:** Reported


**Evidence source:** CURRENT; VSEL; WORK


**Evidence locator:** See cited Sources locators and Current knowledge / Native channels; CFG-002 evidence bundle


**Review state:** Needs review


**Unresolved question:** Select qualified correlations, surface states, supports and ambient assignment.


**Selected choice:** Separate room-air loss from coolant exchange


**Decision scope / rationale:** Transferred documented working understanding; provisional use only; no installed or package release approval.


**Reviewer / date:** Unknown


**Effective configuration:** VCU-REV9-DRAFT-007


### M11

**Package:** Modeling


**Field:** Hydraulic friction and local losses


**Purpose:** Compute resistance and uncertainty consistently.


**Responsible team:** Computational team


**Applicability:** VCU; 1-D and CFD / CHT


**Requirement source:** MODEL; DESIGN


**Requirement locator:** M3 momentum model; proposed closure record


**Current evidence:** Unknown


**Evidence type:** Unknown


**Evidence source:** None supplied


**Evidence locator:** Not available


**Review state:** Needs information


**Unresolved question:** Record roughness, K values, correlation versions, reference diameters and regime limits.


**Selected choice:** Unknown


**Decision scope / rationale:** Unknown


**Reviewer / date:** Unknown


**Effective configuration:** Unknown


### M12

**Package:** Shared


**Field:** Material/product-to-property link


**Purpose:** Use properties for the actual material or fluid.


**Responsible team:** Experimental + computational


**Applicability:** VCU; 1-D and CFD / CHT


**Requirement source:** P0


**Requirement locator:** Definitions: fixed property reference


**Current evidence:** Reported 316L pipe, fiberglass candidate and calcium-aluminum-silicate strip; VMAT explicitly marks all three calibration-ineligible and unverified against installed products. Fluid formulation remains unresolved.


**Evidence type:** Reported


**Evidence source:** VMAT; MAT


**Evidence locator:** VMAT materials.*.provenance and calibration_eligible; Materials tab


**Review state:** Needs review


**Unresolved question:** Confirm installed identity; list needed fluid density/cp/enthalpy/viscosity/k/expansion and solid density/cp/k by model, plus relevant surface/contact properties.


**Selected choice:** Unknown


**Decision scope / rationale:** Unknown


**Reviewer / date:** Unknown


**Effective configuration:** Unknown


### M13

**Package:** Modeling


**Field:** Property source and exact equation/table


**Purpose:** Make every numerical property reproducible.


**Responsible team:** Computational team


**Applicability:** VCU; 1-D and CFD / CHT


**Requirement source:** P0


**Requirement locator:** Definitions and Conventions


**Current evidence:** Nine explicit solid rho/cp/k functions transcribed from VMAT v3. Original derivations and installed-product source data remain unverified. No fluid functions imported.


**Evidence type:** Reported


**Evidence source:** VMAT


**Evidence locator:** vcu_candidate_materials_v3.yaml materials.*.properties; Materials equations


**Review state:** Needs review


**Unresolved question:** Retain original publication/product table and exact coefficients, edition and locator.


**Selected choice:** Unknown


**Decision scope / rationale:** Unknown


**Reviewer / date:** Unknown


**Effective configuration:** Unknown


### M14

**Package:** Modeling


**Field:** Input/output units and concentration basis


**Purpose:** Prevent temperature and mixture-basis conversion errors.


**Responsible team:** Computational team


**Applicability:** VCU; 1-D and CFD / CHT


**Requirement source:** P0


**Requirement locator:** Definitions: property reference


**Current evidence:** All imported solid functions take T in K; rho kg/m^3, cp J/(kg*K), k W/(m*K). Prop-30 mass fraction 0.30 is reported; formulation verification pending.


**Evidence type:** Reported


**Evidence source:** VMAT; PG


**Evidence locator:** VMAT properties units/coefficient_order; Fluids tab


**Review state:** Needs review


**Unresolved question:** Record K versus deg C, pressure units, mass/volume fraction and output units for each function.


**Selected choice:** Unknown


**Decision scope / rationale:** Unknown


**Reviewer / date:** Unknown


**Effective configuration:** Unknown


### M15

**Package:** Modeling


**Field:** Applicability domain


**Purpose:** Prevent unsupported extrapolation across fluids or regimes.


**Responsible team:** Computational team


**Applicability:** VCU; 1-D and CFD / CHT


**Requirement source:** P0; P2


**Requirement locator:** Property reference; temperature/condensation applicability


**Current evidence:** User-authorized working intervals: pipe 278.15-813 K; fiberglass 278.15-533 K; heater strip 278.15-1089 K. ADR-0033 extends all nine functions to 5 C; extrapolation is not product validation or an operating limit.


**Evidence type:** Modeling assumption


**Evidence source:** VMAT; V5C


**Evidence locator:** VMAT valid_temperature_K; ADR-0033 Decision and authority


**Review state:** Needs review


**Unresolved question:** Verify property-specific T/p/composition/phase domain from original sources.


**Selected choice:** Unknown


**Decision scope / rationale:** Unknown


**Reviewer / date:** Unknown


**Effective configuration:** Unknown


### M16

**Package:** Modeling


**Field:** Interpolation and out-of-range behavior


**Purpose:** Make tables and correlations behave consistently.


**Responsible team:** Computational team


**Applicability:** VCU; 1-D and CFD / CHT


**Requirement source:** DESIGN


**Requirement locator:** Proposed implementation control


**Current evidence:** VMAT polynomial functions use ascending powers of T in K; density/cp constants as specified; all nine functions specify out_of_range: error. No fluid interpolation policy supplied.


**Evidence type:** Reported


**Evidence source:** VMAT


**Evidence locator:** VMAT materials.*.properties model/coefficient_order/out_of_range


**Review state:** Needs review


**Unresolved question:** Specify interpolation; reject/flag extrapolation explicitly rather than silently clipping.


**Selected choice:** Unknown


**Decision scope / rationale:** Unknown


**Reviewer / date:** Unknown


**Effective configuration:** Unknown


### M17

**Package:** Modeling


**Field:** Property uncertainty and fit residuals


**Purpose:** Separate source uncertainty from fitting accuracy.


**Responsible team:** Computational team


**Applicability:** VCU; 1-D and CFD / CHT


**Requirement source:** P0; P1


**Requirement locator:** Property reference; uncertainty propagation


**Current evidence:** Unknown


**Evidence type:** Unknown


**Evidence source:** None supplied


**Evidence locator:** Not available


**Review state:** Needs information


**Unresolved question:** Quantify source, composition, fit and implementation uncertainty separately.


**Selected choice:** Unknown


**Decision scope / rationale:** Unknown


**Reviewer / date:** Unknown


**Effective configuration:** Unknown


### M18

**Package:** Modeling


**Field:** Selection rationale and alternatives


**Purpose:** Explain why both teams use this property model.


**Responsible team:** Experimental + computational


**Applicability:** VCU; 1-D and CFD / CHT


**Requirement source:** USER


**Requirement locator:** Requested material-property justification


**Current evidence:** Candidate working functions supplied by user; ADR-0033 authorizes low-temperature extrapolation. Reported independent pipe comparison has no retained comparison table; package transfer does not establish independent validation.


**Evidence type:** Reported


**Evidence source:** VMAT; V5C


**Evidence locator:** VMAT provenance; ADR-0033 Evidence and limits


**Review state:** Needs review


**Unresolved question:** Compare candidate sources and explain selection or any deliberate mixed-source set.


**Selected choice:** Unknown


**Decision scope / rationale:** Unknown


**Reviewer / date:** Unknown


**Effective configuration:** Unknown


### M19

**Package:** Modeling


**Field:** Implementation reference checks


**Purpose:** Check equation transcription and thermodynamic consistency.


**Responsible team:** Computational team


**Applicability:** VCU; 1-D and CFD / CHT


**Requirement source:** DESIGN


**Requirement locator:** Proposed shared property tests


**Current evidence:** Unknown


**Evidence type:** Unknown


**Evidence source:** None supplied


**Evidence locator:** Not available


**Review state:** Needs information


**Unresolved question:** Store reference values; check cp/enthalpy and density/expansion consistency where used.


**Selected choice:** Unknown


**Decision scope / rationale:** Unknown


**Reviewer / date:** Unknown


**Effective configuration:** Unknown


### M20

**Package:** Modeling


**Field:** Initial temperature, flow and inventory state


**Purpose:** Initialize transient models from evidence.


**Responsible team:** Experimental + computational


**Applicability:** VCU Prop-30 draft campaign; requalify other fluids


**Requirement source:** P2


**Requirement locator:** Method initial condition; Required Outputs


**Current evidence:** Unknown


**Evidence type:** Unknown


**Evidence source:** None supplied


**Evidence locator:** Not available


**Review state:** Needs information


**Unresolved question:** Record fluid/wall distribution, initial flow, fill history and unresolved state uncertainty.


**Selected choice:** Unknown


**Decision scope / rationale:** Unknown


**Reviewer / date:** Unknown


**Effective configuration:** Unknown


### M21

**Package:** Modeling


**Field:** Observation averaging and sensor response


**Purpose:** Compare like quantities rather than convenient nodes.


**Responsible team:** Computational team


**Applicability:** VCU; 1-D and CFD / CHT


**Requirement source:** P0; P2


**Requirement locator:** Model map; effective initial states


**Current evidence:** STC wall and assumed PTC centerline operators are explicit. Distributed optical extent and sensor lag unknown; reduced-zone states need their own averaging rule.


**Evidence type:** Modeling assumption


**Evidence source:** XWALK; VSEL; WORK


**Evidence locator:** See cited Sources locators and Current knowledge / Native channels; CFG-002 evidence bundle


**Review state:** Needs review


**Unresolved question:** Qualify lag/spatial/time averaging and noncoincident comparisons.


**Selected choice:** Do not equate effective-zone temperature with fluid or wall automatically


**Decision scope / rationale:** Transferred documented working understanding; provisional use only; no installed or package release approval.


**Reviewer / date:** Unknown


**Effective configuration:** VCU-REV9-DRAFT-007


### M22

**Package:** Modeling


**Field:** Steady-state class and acceptance limits


**Purpose:** Fix data-quality criteria before selecting windows.


**Responsible team:** Experimental + computational


**Applicability:** VCU Prop-30 draft campaign; requalify other fluids


**Requirement source:** P1


**Requirement locator:** Section 2 Data Acceptance and Uncertainty


**Current evidence:** Sep2/4 are provisional ambient baseline candidates; stable mean cyclic operation differs from instantaneous equilibrium. No accepted comparison tolerances established.


**Evidence type:** Reported


**Evidence source:** DIAG; FOLLOW; OPCYCLE


**Evidence locator:** See cited Sources locators and Current knowledge / Native channels; CFG-002 evidence bundle


**Review state:** Needs review


**Unresolved question:** Approve intended-use tolerances and qualify run-specific intervals.


**Selected choice:** Keep exploratory classifications separate from accepted steady-state limits


**Decision scope / rationale:** Transferred documented working understanding; provisional use only; no installed or package release approval.


**Reviewer / date:** Unknown


**Effective configuration:** VCU-REV9-DRAFT-007


### M23

**Package:** Modeling


**Field:** Accepted interval and target-attainment result


**Purpose:** Keep constancy separate from reaching the requested target.


**Responsible team:** Experimental + computational


**Applicability:** VCU Prop-30 draft campaign; requalify other fluids


**Requirement source:** P4


**Requirement locator:** Method establishing/recording a state


**Current evidence:** Unknown


**Evidence type:** Unknown


**Evidence source:** None supplied


**Evidence locator:** Not available


**Review state:** Needs information


**Unresolved question:** Record acceptance time, confirmed span, reporting interval and target-band result separately.


**Selected choice:** Unknown


**Decision scope / rationale:** Unknown


**Reviewer / date:** Unknown


**Effective configuration:** Unknown


### M24

**Package:** Modeling


**Field:** Covariance and autocorrelation method


**Purpose:** Report uncertainty using independent information.


**Responsible team:** Computational team


**Applicability:** VCU Prop-30 draft campaign; requalify other fluids


**Requirement source:** P1


**Requirement locator:** Required Outputs: correlation structure and uncertainty


**Current evidence:** Slow correlated variation persists after averaging; ten-second block means are not independent. CAL-004 temporal-block analyses address serial dependence; Type B calibration unknown.


**Evidence type:** Reported


**Evidence source:** DIAG; FOLLOW


**Evidence locator:** See cited Sources locators and Current knowledge / Native channels; CFG-002 evidence bundle


**Review state:** Needs review


**Unresolved question:** No universal validated block length, intrinsic noise floor or absolute accuracy supplied.


**Selected choice:** Use temporal correlation and joint-channel covariance; report block sensitivity


**Decision scope / rationale:** Transferred documented working understanding; provisional use only; no installed or package release approval.


**Reviewer / date:** Unknown


**Effective configuration:** VCU-REV9-DRAFT-007


### M25

**Package:** Modeling


**Field:** Calibration/withheld split and model freeze


**Purpose:** Keep validation independent of parameter fitting.


**Responsible team:** Computational team


**Applicability:** VCU Prop-30 draft campaign; requalify other fluids


**Requirement source:** P2; P3; P4


**Requirement locator:** P2 runs/freeze; P3 blind validation; P4 applicability case


**Current evidence:** Existing acquisitions have working calibration roles, not independent validation; no blind Rev9 split established. Historical model/configurations remain frozen to their own inputs.


**Evidence type:** Reported


**Evidence source:** FOLLOW; WORK


**Evidence locator:** See cited Sources locators and Current knowledge / Native channels; CFG-002 evidence bundle


**Review state:** Needs review


**Unresolved question:** Finalize scientific calibration/validation roles; empirical interval holdout is not facility validation.


**Selected choice:** Declare held-out intervals/runs and model freeze before scoring


**Decision scope / rationale:** Transferred documented working understanding; provisional use only; no installed or package release approval.


**Reviewer / date:** Unknown


**Effective configuration:** VCU-REV9-DRAFT-007


### M26

**Package:** Modeling


**Field:** Parameter identifiability and sensitivities


**Purpose:** Avoid fitting unsupported model complexity.


**Responsible team:** Computational team


**Applicability:** VCU Prop-30 draft campaign; requalify other fluids


**Requirement source:** P2


**Requirement locator:** Required Outputs steps 5-7


**Current evidence:** Passive relaxation constrains time constants and parameter ratios; absolute conductance/capacitance scales need a fixed or measured-power anchor.


**Evidence type:** Modeling assumption


**Evidence source:** MODEL; FOLLOW


**Evidence locator:** See cited Sources locators and Current knowledge / Native channels; CFG-002 evidence bundle


**Review state:** Needs review


**Unresolved question:** No validated all-layer parameter identification or fitted properties imported.


**Selected choice:** Require identifiability and boundary/initial-state sensitivity before interpreting fitted material constants


**Decision scope / rationale:** Transferred documented working understanding; provisional use only; no installed or package release approval.


**Reviewer / date:** Unknown


**Effective configuration:** VCU-REV9-DRAFT-007


### M27

**Package:** Modeling


**Field:** Settling time and supported domain


**Purpose:** Use a supported operational settling value.


**Responsible team:** Computational team


**Applicability:** VCU Prop-30 draft campaign; requalify other fluids


**Requirement source:** P2


**Requirement locator:** Slowest loop time constant; Required Outputs


**Current evidence:** Response/settling estimates are conditional on boundary, interval and model. Oscillating hot plateaus need cycle metrics rather than assumed instantaneous settling.


**Evidence type:** Reported


**Evidence source:** FOLLOW; OPCYCLE


**Evidence locator:** See cited Sources locators and Current knowledge / Native channels; CFG-002 evidence bundle


**Review state:** Needs review


**Unresolved question:** Qualify confidence, start-time, boundary variability and supported domain.


**Selected choice:** No universal settling time selected


**Decision scope / rationale:** Transferred documented working understanding; provisional use only; no installed or package release approval.


**Reviewer / date:** Unknown


**Effective configuration:** VCU-REV9-DRAFT-007


### M28

**Package:** Modeling


**Field:** Mass/energy conservation and solution convergence


**Purpose:** Check that the numerical solution is credible.


**Responsible team:** Computational team


**Applicability:** VCU; 1-D and CFD / CHT


**Requirement source:** MODEL; DESIGN


**Requirement locator:** Heat ledger; proposed verification record


**Current evidence:** Unknown


**Evidence type:** Unknown


**Evidence source:** None supplied


**Evidence locator:** Not available


**Review state:** Needs information


**Unresolved question:** Define residual/closure criteria and failure handling for each solver.


**Selected choice:** Unknown


**Decision scope / rationale:** Unknown


**Reviewer / date:** Unknown


**Effective configuration:** Unknown


### M29

**Package:** Modeling


**Field:** Spatial/time resolution sensitivity


**Purpose:** Separate discretization error from experimental discrepancy.


**Responsible team:** Computational team


**Applicability:** VCU; 1-D and CFD / CHT


**Requirement source:** DESIGN


**Requirement locator:** Proposed 1-D and CFD verification field


**Current evidence:** Unknown


**Evidence type:** Unknown


**Evidence source:** None supplied


**Evidence locator:** Not available


**Review state:** Needs information


**Unresolved question:** Report mesh/cell/time refinement and tolerance sensitivity relevant to predictions.


**Selected choice:** Unknown


**Decision scope / rationale:** Unknown


**Reviewer / date:** Unknown


**Effective configuration:** Unknown


### M30

**Package:** Modeling


**Field:** Flow inference and conditioning gates


**Purpose:** Avoid reporting flow from unresolved enthalpy differences.


**Responsible team:** Computational team


**Applicability:** VCU Prop-30 draft campaign; requalify other fluids


**Requirement source:** P4


**Requirement locator:** Section 2 Primary-flow and Reynolds-number inference


**Current evidence:** Unknown


**Evidence type:** Unknown


**Evidence source:** None supplied


**Evidence locator:** Not available


**Review state:** Needs information


**Unresolved question:** Use validated loss corrections, covariance-aware consistency and defined uncertainty gates.


**Selected choice:** Unknown


**Decision scope / rationale:** Unknown


**Reviewer / date:** Unknown


**Effective configuration:** Unknown


### M31

**Package:** Modeling


**Field:** Validation metrics, discrepancy and applicability


**Purpose:** Bound what has actually been demonstrated.


**Responsible team:** Experimental + computational


**Applicability:** VCU; 1-D and CFD / CHT


**Requirement source:** P2; P3; P4


**Requirement locator:** Validation and disposition sections


**Current evidence:** Historical forward/boundary studies remain conditional; neither successful computation nor an empirical holdout validates the Rev9 facility model.


**Evidence type:** Reported


**Evidence source:** FOLLOW; WORK


**Evidence locator:** See cited Sources locators and Current knowledge / Native channels; CFG-002 evidence bundle


**Review state:** Needs review


**Unresolved question:** No validated facility accuracy or release criterion supplied.


**Selected choice:** Retain conservation/uncertainty checks and predeclared unseen assessment


**Decision scope / rationale:** Transferred documented working understanding; provisional use only; no installed or package release approval.


**Reviewer / date:** Unknown


**Effective configuration:** VCU-REV9-DRAFT-007


### M32

**Package:** Modeling


**Field:** Repeatability and path-dependence criteria


**Purpose:** Distinguish significant history effects from measurement scatter.


**Responsible team:** Experimental + computational


**Applicability:** VCU Prop-30 draft campaign; requalify other fluids


**Requirement source:** P4


**Requirement locator:** Method central-state repeat; Required Outputs


**Current evidence:** Unknown


**Evidence type:** Unknown


**Evidence source:** None supplied


**Evidence locator:** Not available


**Review state:** Needs information


**Unresolved question:** Preapprove response set, equivalence limits and practical-significance threshold.


**Selected choice:** Unknown


**Decision scope / rationale:** Unknown


**Reviewer / date:** Unknown


**Effective configuration:** Unknown


## Phase requests

### P0-01

**Phase:** 0


**Request:** Identify the physical setup


**Experimental-team action:** Photograph the whole VCU loop; name the revision, date and changed components.


**Return this evidence:** Configuration ID, change list and labeled photos


**Review partner:** Facility lead / package reviewer


**Field IDs:** C01-C17


**Source locator:** P0 Section 3 Method: configuration and geometry


**VCU adaptation / caution:** No electrical-specific adaptation identified.


**Completion check:** Evidence supplied and reviewed; open limitations recorded.


### P0-02

**Phase:** 0


**Request:** Trace every channel


**Experimental-team action:** Match each installed sensor to its cable/DAQ channel and actual sensing point.


**Return this evidence:** Channel crosswalk, position survey, calibration certificates and uncertainties


**Review partner:** Experimental + computational


**Field IDs:** C21-C33; M04


**Source locator:** P0 Method: instrumentation


**VCU adaptation / caution:** PTC-X omitted from the active register by owner request, 2026-10-16. Verify remaining installed sensor identities; do not assume CAD IDs are DAQ channels or TC/Luna co-location.


**Completion check:** Evidence supplied and reviewed; open limitations recorded.


### P0-03

**Phase:** 0


**Request:** Document heater and cooler measurement boundaries


**Experimental-team action:** Supply the actual circuit/plumbing and feedback sketches, meter positions and logged signals.


**Return this evidence:** Electrical wiring/power record; coolant routing, flow and temperature planes


**Review partner:** Experimental + computational


**Field IDs:** C34-C41; M08-M09


**Source locator:** P0 Section 2 duties; Section 3 secondary-side boundaries


**VCU adaptation / caution:** Replace heater secondary-fluid duty with an approved electrical control-volume balance.


**Completion check:** Evidence supplied and reviewed; open limitations recorded.


### P0-04

**Phase:** 0


**Request:** Document fluid, branches and operating limits


**Experimental-team action:** Identify each circuit fluid, batch, fill level, valves, vent/pressure and approved limits.


**Return this evidence:** Fluid/inventory record, branch state sheet and limit references


**Review partner:** Facility lead / package reviewer


**Field IDs:** C18-C20; C42-C45; M07


**Source locator:** P0 Method: facility/fluid configuration and operating limits


**VCU adaptation / caution:** Draft Prop-30 limits do not automatically apply to air or water experiments.


**Completion check:** Evidence supplied and reviewed; open limitations recorded.


### P0-05

**Phase:** 0


**Request:** Demonstrate logging and synchronization


**Experimental-team action:** Provide a checkout record showing required signals and a common timed event.


**Return this evidence:** Raw checkout file, channel units/rates, clock offsets and event log


**Review partner:** Experimental + computational


**Field IDs:** C31-C33; C44; C46


**Source locator:** P0 Method: environment, synchronization and coordinated checkout


**VCU adaptation / caution:** Confirm two room T/RH stations and exposed cold-surface measurements; dew-point rule remains draft.


**Completion check:** Evidence supplied and reviewed; open limitations recorded.


### P1-01

**Phase:** 1


**Request:** Supply a qualified ambient baseline


**Experimental-team action:** Under the approved procedure, record the passive baseline and room/control history.


**Return this evidence:** At least 6 h after ambient equilibrium plus a relevant HVAC cycle, as requested by draft


**Review partner:** Experimental + computational


**Field IDs:** C44; C46; M22-M24


**Source locator:** P1 Section 3 Method, Record the baseline


**VCU adaptation / caution:** Verify electrical heater input and residual cooler duty are inactive; command OFF alone is insufficient.


**Completion check:** Evidence supplied and reviewed; open limitations recorded.


### P1-02

**Phase:** 1


**Request:** Explain channel quality and substitutions


**Experimental-team action:** Identify bad channels; provide real TC/Luna pairs and note spatial offsets.


**Return this evidence:** Quality/exclusion list, pairing map, noise/drift/covariance summary


**Review partner:** Experimental + computational


**Field IDs:** C23-C33; M21; M24


**Source locator:** P1 Section 3 Required Outputs


**VCU adaptation / caution:** P0 says not all locations are co-located; P1 wording needs a usable-pair rule.


**Completion check:** Evidence supplied and reviewed; open limitations recorded.


### P1-03

**Phase:** 1


**Request:** Agree on measurable acceptance criteria


**Experimental-team action:** Review whether proposed limits can be resolved by the baseline measurements.


**Return this evidence:** Approved channel roles, block/window rules and resolution evidence


**Review partner:** Computational team


**Field IDs:** C33; M22-M24


**Source locator:** P1 Section 2 and Section 3 Required Outputs


**VCU adaptation / caution:** Illustrative targets are not approved VCU limits; improve measurement/window before relaxing intent.


**Completion check:** Evidence supplied and reviewed; open limitations recorded.


### P2-01

**Phase:** 2


**Request:** Agree on the conditioning procedure


**Experimental-team action:** Confirm how VCU is filled, circulated, isolated and judged near-isothermal.


**Return this evidence:** Reviewed procedure, fill/inventory/valve history and initial temperature map


**Review partner:** Experimental + computational


**Field IDs:** C20; C43; M20


**Source locator:** P2 Section 3 Method and Required Outputs step 1


**VCU adaptation / caution:** Resolve continuous in-loop recirculation versus tank-uniformity-before-each-fill wording.


**Completion check:** Evidence supplied and reviewed; open limitations recorded.


### P2-02

**Phase:** 2


**Request:** Preserve warm and cold relaxation records


**Experimental-team action:** Provide full conditioning, shutdown and relaxation histories with room/event data.


**Return this evidence:** Two warm and two cold runs requested by draft; calibration/withheld roles assigned in advance


**Review partner:** Experimental + computational


**Field IDs:** C46; M20; M25


**Source locator:** P2 Section 3 Run IDs and Method


**VCU adaptation / caution:** Draft target offsets/durations are provisional; establish VCU operating and condensation limits first.


**Completion check:** Evidence supplied and reviewed; open limitations recorded.


### P2-03

**Phase:** 2


**Request:** Demonstrate the passive boundary


**Experimental-team action:** Show actual electrical input and residual cooler/attached-hardware heat exchange after shutdown.


**Return this evidence:** Residual-duty evidence, isolation timing and initial-state uncertainty


**Review partner:** Experimental + computational


**Field IDs:** C36; C40; M06; M08; M20


**Source locator:** P2 Method initial condition and Required Outputs qualification


**VCU adaptation / caution:** Include heater stored heat; zero electrical input does not prove zero thermal release.


**Completion check:** Evidence supplied and reviewed; open limitations recorded.


### P2-04

**Phase:** 2


**Request:** Review the fitted model before later tests


**Experimental-team action:** Confirm the sensor-to-zone map and explain structured residuals with experimental context.


**Return this evidence:** Frozen model/property/mapping versions, withheld comparisons, parameter uncertainty and settling bound


**Review partner:** Computational team


**Field IDs:** M21; M25-M27


**Source locator:** P2 Section 3 Required Outputs / Disposition


**VCU adaptation / caution:** Computational team owns fits; experimental team supplies physical-state evidence.


**Completion check:** Evidence supplied and reviewed; open limitations recorded.


### P3-01

**Phase:** 3


**Request:** Provide low-duty accepted-state records


**Experimental-team action:** Return heater-only and cooler-only histories, inactive-system evidence and accepted intervals.


**Return this evidence:** HTR-LOW-01 / CLR-LOW-01 records, ambient exchange and uncertainty inputs


**Review partner:** Experimental + computational


**Field IDs:** C36; C40; C44; M22-M24


**Source locator:** P3 Section 3 Method / Required Outputs


**VCU adaptation / caution:** Adapt whole-loop energy accounting to measured electrical input and explicit losses/storage.


**Completion check:** Evidence supplied and reviewed; open limitations recorded.


### P3-02

**Phase:** 3


**Request:** Keep blind comparisons independent


**Experimental-team action:** Review discrepancies before any fitted parameter is changed.


**Return this evidence:** Dated blind comparison, residuals, condensation class and disposition


**Review partner:** Computational team


**Field IDs:** M25; M31


**Source locator:** P3 Section 2 Blind validation; Section 3 Disposition


**VCU adaptation / caution:** A run reassigned to calibration cannot validate the revised model; obtain new independent cases.


**Completion check:** Evidence supplied and reviewed; open limitations recorded.


### P4-01

**Phase:** 4


**Request:** Agree on attainable target bands


**Experimental-team action:** Confirm instrumentation and controls can resolve the proposed mean-temperature and duty targets.


**Return this evidence:** Approved target coordinates/bands and actual achieved conditions


**Review partner:** Experimental + computational


**Field IDs:** C36; C41; M22-M23


**Source locator:** P4 Section 3 Method: select matrix coordinates


**VCU adaptation / caution:** Replace heater-duty coordinate with agreed electrical/net-thermal definition consistently.


**Completion check:** Evidence supplied and reviewed; open limitations recorded.


### P4-02

**Phase:** 4


**Request:** Return complete matrix and transition histories


**Experimental-team action:** Preserve OP-A/B/C/D/E and B-R records, approach paths, events and failed attempts.


**Return this evidence:** Five unique states plus repeat; accepted spans, reporting intervals and transition times


**Review partner:** Experimental + computational


**Field IDs:** C46; M23; M32


**Source locator:** P4 Section 3 Run IDs / Required Outputs


**VCU adaptation / caution:** State constancy and target attainment are separate checks; no retroactive threshold relaxation.


**Completion check:** Evidence supplied and reviewed; open limitations recorded.


### P4-03

**Phase:** 4


**Request:** Qualify inference and applicability


**Experimental-team action:** Provide usable exchanger-temperature differences and uncertainty inputs; identify a withheld applicability state.


**Return this evidence:** Flow/Reynolds conditioning evidence, independent estimates and applicability comparison


**Review partner:** Computational team


**Field IDs:** M15; M25; M30-M31


**Source locator:** P4 Section 2 flow inference; Section 3 Required Outputs


**VCU adaptation / caution:** Heater-side inference needs the electrical adaptation; no quantitative inference from unresolved heat balance.


**Completion check:** Evidence supplied and reviewed; open limitations recorded.


## Review issues

### I01

**Kind:** Hardware / plan mismatch


**Source and locator:** P0 Section 2 duties; P3 energy balance versus HEAT VCU Heater


**What conflicts / is missing:** Plans use heater secondary enthalpy flow; VCU notes report electrical mat/band heaters.


**Suggested owner:** Experimental + computational


**Resolution needed:** Define electrical measurement boundary, real power, heater/structure storage and external losses; revise Phase 0-4 references.


**Affected fields:** C34-C37; M08; M30


### I02

**Kind:** Internal procedure inconsistency


**Source and locator:** P2 Section 3 Method vs Required Outputs step 1


**What conflicts / is missing:** In-loop recirculation is specified, but qualification still refers to tank uniformity before each fill.


**Suggested owner:** Plan author + experimental lead


**Resolution needed:** Choose the actual conditioning method and align initial-condition, timing and acceptance wording.


**Affected fields:** C20; M20


### I03

**Kind:** Conditional measurement assumption


**Source and locator:** P0 apparatus/channel table vs P1 Required Outputs TC-Luna comparison


**What conflicts / is missing:** P0 states not all sensors are co-located; P1 requests each TC compared with its co-located Luna measurement.


**Suggested owner:** Instrumentation + computational


**Resolution needed:** Identify actual pairs and offsets; define how non-coincident pairs may be used.


**Affected fields:** C24-C27; C33; M21


### I04

**Kind:** Conflicting sensor evidence


**Source and locator:** R9 sheets 5-6; SNOTE VCU Rev9 PTCX note


**What conflicts / is missing:** Historical CAD extraction includes PTC-X; the supplied note calls PTCX a fluke. PTC-X was removed from the active sensor/calibration records by owner request, 2026-10-16. Installed hardware identity is unverified.


**Suggested owner:** Experimental instrumentation


**Resolution needed:** Retain the original CAD/source evidence. Confirm whether the excluded reference corresponds to installed hardware before using it in any run or model mapping.


**Affected fields:** C21; C23


### I05

**Kind:** Unqualified geometry interpretation


**Source and locator:** R9 sheets 2-4 and SEG


**What conflicts / is missing:** Heater pieces overlap/offset; lower-right bend is reconstructed; clamp spans are mechanical only.


**Suggested owner:** Experimental geometry + computational


**Resolution needed:** Survey geometry; document any model healing and active heater boundaries separately.


**Affected fields:** C06-C08; C34; M03


### I06

**Kind:** Cross-facility / revision contamination


**Source and locator:** SNOTE VCU sections; supplied VCU illustration captions


**What conflicts / is missing:** Some VCU note links target ACU or Rev8; supplied VCU overview illustrations identify Rev8.


**Suggested owner:** Package maintainer


**Resolution needed:** Keep references for context only; use Rev9 rows as CAD candidate and new installed evidence for verification.


**Affected fields:** C04; C23


### I07

**Kind:** Applicability gap


**Source and locator:** P0 Purpose/Required scope; USER fluid clarification


**What conflicts / is missing:** Draft campaign is Prop-30-specific; user also lists air/water VCU experiments.


**Suggested owner:** Facility lead + computational


**Resolution needed:** Keep plan thresholds and fluid correlations scoped to the documented fluid/circuit and requalify other uses.


**Affected fields:** C18-C19; C45; M15


### I08

**Kind:** Approval status missing


**Source and locator:** P0-P4 title/status and approval records


**What conflicts / is missing:** Documents are marked draft; no Nick-approved requirement status is established here.


**Suggested owner:** Facility lead / plan author


**Resolution needed:** Confirm approved revision and record which requirements remain proposed.


**Affected fields:** C03; M22


### I09

**Kind:** Property-source qualification gap


**Source and locator:** MAT lines 35-40; STEEL lines 3-21; PG figures


**What conflicts / is missing:** Notes contain candidate fits/mixed-source choices; original validity and uncertainty are not yet verified.


**Suggested owner:** Computational materials + experimental


**Resolution needed:** Check original sources and installed identity before approving equations; keep source domain separate from operating limits.


**Affected fields:** M12-M19


### I10

**Kind:** Historical applicability


**Source and locator:** VSEL; WORK; FOLLOW; DAQISS; OPCYCLE


**What conflicts / is missing:** STC5 changed location; Rev9 working map and historical Rev8 records have no installation date crosswalk.


**Suggested owner:** Experimental + computational


**Resolution needed:** Provide dated sensor/geometry applicability per run; retain original model versions.


**Affected fields:** C04; C23-C24; C46; M02


### I11

**Kind:** Data validity and calibration


**Source and locator:** VSEL; WORK; FOLLOW; DAQISS; OPCYCLE


**What conflicts / is missing:** June12 nonphysical readings; Type B accuracy and status/scaling unqualified; slow temporal covariance matters.


**Suggested owner:** Experimental + computational


**Resolution needed:** Resolve DAQ status; version masks and correlation-aware uncertainty; retain raw.


**Affected fields:** C28-C32; M22-M24


### I12

**Kind:** Boundary-control qualification


**Source and locator:** VSEL; WORK; FOLLOW; DAQISS; OPCYCLE


**What conflicts / is missing:** Chiller contribution reported; internal jacket route, flow, controller identity and switching logs absent.


**Suggested owner:** Experimental + computational


**Resolution needed:** Confirm PTC5/6 run-specific planes and controller/flow logs before causal or duty claims.


**Affected fields:** C39-C41; M09; M27


## Sources

### R9

**File / record:** VCU_Rev9_CAD_Engineering_Drawings.pdf


**Revision / context:** 2026-10-08; VCU-R9-E01


**Locator guide:** Sheets 1-8


**Qualification:** VCU CAD candidate. Printed precision is not tolerance; geometry is not installed verification.


### SEG

**File / record:** VCU_Rev9_Segments.csv


**Revision / context:** Companion Rev9 structured package


**Locator guide:** Rows keyed by segment; length_basis, dx_mm, dy_mm, centerline_length_mm


**Qualification:** Preserve blanks, projected spans and qualified spline lengths.


### SNS

**File / record:** VCU_Rev9_Sensor_Stations.csv


**Revision / context:** Companion Rev9 structured package


**Locator guide:** Rows keyed by sensor_id; reference_basis, nearest_endpoint, nearest_distance_mm


**Qualification:** Geometric references, not verified sensing tips or DAQ names.


### DIA

**File / record:** VCU_Rev9_Diameters.csv


**Revision / context:** Companion Rev9 structured package


**Locator guide:** Rows keyed by item


**Qualification:** Main swept-loop bore is absent; local spool bores are not loop-wide IDs.


### MAT

**File / record:** 1.2 Main Material Props.md


**Revision / context:** Supplied notes; VCU section cites 2026-09-16 report


**Locator guide:** VCU section only; lines 17-44


**Qualification:** Reported materials/composition and proposed insulation fit; original sources not verified.


### PG

**File / record:** 1.2.1 Prop 30 ThermoPhys Props.md


**Revision / context:** Supplied notes


**Locator guide:** 30 wt% heading and linked property figures


**Qualification:** Property-source leads; do not transfer image/table values without source and units.


### STEEL

**File / record:** 1.2.2 Steel Pipe Properties.md


**Revision / context:** Supplied notes


**Locator guide:** Lines 3-21; Suggested you use


**Qualification:** Mixed candidate correlations. A range beside MOOSE items does not qualify the whole selection.


### HEAT

**File / record:** 1.1.0 Heaters and coolers.md


**Revision / context:** Supplied notes; 2026-10-07 reported heater message


**Locator guide:** VCU / Insulation / Heater; lines 5-23


**Qualification:** Electrical mat/band heaters reported. Wiring, active boundaries and net duty unverified.


### SNOTE

**File / record:** 1.1.2 Sensors.md


**Revision / context:** Supplied notes


**Locator guide:** VCU / Rev9; PTCX note


**Qualification:** PTCX called a fluke; some links in this section point to ACU/Rev8. Keep conflict visible.


### MODEL

**File / record:** 0.0 Intro to Model.md


**Revision / context:** Supplied model overview


**Locator guide:** The four physical-model stages; reduced-zone paragraph


**Qualification:** Supports proposed model scope; not verification that any facility run is validated.


### P0

**File / record:** STNCL_Phase0_System_Checkout.tex


**Revision / context:** Revision 0.1; 2026-08-17; draft


**Locator guide:** Section 2 Technical Basis; Section 3 Method / Required Outputs


**Qualification:** Draft requirements for facility-specific completion; approval not supplied.


### P1

**File / record:** STNCL_Phase1_Ambient_Equilibrium_Baseline.tex


**Revision / context:** Revision 0.1; draft


**Locator guide:** Section 2 Data Acceptance and Uncertainty; Section 3 Method / Required Outputs


**Qualification:** Prop-30 plan; thresholds and noise examples are not universal operating limits.


### P2

**File / record:** STNCL_Phase2_Thermal_Relaxation_Tests.tex


**Revision / context:** Revision 0.1; draft


**Locator guide:** Section 2 Thermal Model and Heat Loss; Section 3 Method / Required Outputs


**Qualification:** Prop-30 plan; conditioning and tank qualification wording need reconciliation.


### P3

**File / record:** STNCL_Phase3_Low_Duty_Steady_Heat_Loss_Tests.tex


**Revision / context:** Revision 0.1; draft


**Locator guide:** Section 2 Blind validation; Section 3 Method / Required Outputs / Disposition


**Qualification:** Heater-side duty definition requires electrical adaptation for VCU.


### P4

**File / record:** STNCL_Phase4_Initial_Test_Matrix_and_Transition_Characterization.tex


**Revision / context:** Revision 0.1; draft


**Locator guide:** Section 2 Primary-flow inference; Section 3 Method / Required Outputs


**Qualification:** Five unique states plus repeat; applicability and uncertainty gates are draft requirements.


### USER

**File / record:** User decisions in this chat


**Revision / context:** 2026-10-15


**Locator guide:** Editable forms; VCU fluid scope; both models; circumferential sensor position


**Qualification:** VCU Prop-30/air/water; circuit and run assignment still required. ACU excluded.


### DESIGN

**File / record:** Proposed package design


**Revision / context:** 2026-10-15


**Locator guide:** This requirements register and coordinate convention


**Qualification:** Assistant-proposed documentation field/convention, not an approved physical fact.


### VMAT

**File / record:** support/evidence/2026-10-16_CFG-001_vcu_references/vcu_candidate_materials_v3.yaml


**Revision / context:** 2026-10-07 v3


**Locator guide:** materials.*.properties; provenance


**Qualification:** Nine user-supplied solid-property candidates; not product verified; calibration-ineligible. Coverage wording in older provenance is superseded by VSEL.


### V5C

**File / record:** support/evidence/2026-10-16_CFG-001_vcu_references/ADR-0033-vcu-solid-properties-5c.md


**Revision / context:** 2026-10-07 accepted working-range decision


**Locator guide:** Decision and authority; Evidence and limits


**Qualification:** User authorizes working extrapolation to 5 C, not source/product validation or an operating limit.


### VSEL

**File / record:** support/evidence/2026-10-16_CFG-001_vcu_references/2026-10-14_GEO-008_rev9_working_selection.md


**Revision / context:** 2026-10-14 provisional working selection


**Locator guide:** User direction and interpretation; Why H-A has a qualification


**Qualification:** Dated working geometry/installation choices; historical run dates, tips and electrical footprint unresolved.


### VINS

**File / record:** support/evidence/2026-10-16_CFG-001_vcu_references/insulation.yaml


**Revision / context:** v5 2026-10-07, amended by VSEL for Rev9


**Locator guide:** coverage; contact; regions


**Qualification:** Historical regional v5. Current coverage is VREG/CURRENT and WORK v3; all STC contacts bare per VSEL. Preserve v5 as provenance only.


### VTOP

**File / record:** support/evidence/2026-10-16_GEO-009_covered_top_corners/USER_CLARIFICATION.md


**Revision / context:** Direct user clarification 2026-10-16; model regional v6 / Rev9 working v2


**Locator guide:** Whole C-D / E-F corners; LF-01 local exposure


**Qualification:** Reported by user; no independent survey, optical extent, covered extent or historical run dates supplied.


### VREG

**File / record:** support/evidence/2026-10-16_GEO-010_regional_insulation_sync/README.md


**Revision / context:** GEO-010 2026-10-16; regional v7 / working v3


**Locator guide:** region_assignments.json; insulation.yaml; ADR-0025/0026; USER_CONFIRMATION.md


**Qualification:** Reported coverage and approximate thickness estimates; product/fit validation, installed surveys and historical applicability remain separate.


### WORK

**File / record:** support/evidence/2026-10-16_CFG-002_vcu_current_understanding/WORK_rev9_working_selection_v3.json


**Revision / context:** Rev9 working selection v3; GEO-010 2026-10-16


**Locator guide:** sensors, heater, jacket, insulation; historical_run_applicability


**Qualification:** Working choices; not installed survey, calibration or historical run migration.


### XWALK

**File / record:** support/evidence/2026-10-16_CFG-002_vcu_current_understanding/XWALK_2026-10-05_VCU_WORKING_SENSOR_CROSSWALK.md


**Revision / context:** 2026-10-05 historical Rev8 crosswalk


**Locator guide:** Working measurement operators and native channel roles


**Qualification:** Use radial operators/native roles only; Rev8 stations, old insulation and unpaired JTC wording superseded by VSEL/VREG/WORK.


### DIAG

**File / record:** support/evidence/2026-10-16_CFG-002_vcu_current_understanding/DIAG_README.md


**Revision / context:** CAL-003 2026-10-08


**Locator guide:** Quality issues; ambient correlation; chiller operator report


**Qualification:** Installed-system diagnostics, not sensor accuracy; compact ten-second blocks remain correlated. CAL-004 follow-up supersedes initial masks/method limitations.


### FOLLOW

**File / record:** support/evidence/2026-10-16_CFG-002_vcu_current_understanding/FOLLOW_README.md


**Revision / context:** CAL-004 2026-10-08 follow-up


**Locator guide:** Native validity; temporal uncertainty; heated associations; forward comparisons


**Qualification:** Conditional historical Rev8/insulation-v5 analysis. Numerical correlations do not prove controller causality or validate Rev9.


### DAQISS

**File / record:** support/evidence/2026-10-16_CFG-002_vcu_current_understanding/DAQISS_EXPERIMENTAL_TEAM_CLARIFICATION.md


**Revision / context:** 2026-10-08 source-linked clarification draft


**Locator guide:** June12 source hash and channel invalid counts; June17/23 events


**Qualification:** Draft for user to send; not sent and not answered.


### OPCYCLE

**File / record:** support/evidence/2026-10-16_CFG-002_vcu_current_understanding/OPCYCLE_operator_update.json


**Revision / context:** Direct user report 2026-10-08


**Locator guide:** statements and unknown


**Qualification:** Chiller on/off contributes to hot-plateau oscillation; exact intervals/control logs unknown.


### TRIAGE

**File / record:** support/evidence/2026-10-16_CFG-002_vcu_current_understanding/TRIAGE_README.md


**Revision / context:** CAL-003 2026-10-07


**Locator guide:** July15 identity/clock limits; July29 source


**Qualification:** Short ambient-named July15 file may be same liquid experiment; not independently established air run.


### FLUIDCFG

**File / record:** support/evidence/2026-10-16_CFG-002_vcu_current_understanding/FLUIDCFG_fluid.yaml


**Revision / context:** Provisional identity configuration


**Locator guide:** identity, unresolved, runtime_property_selection


**Qualification:** Prop-30 identity candidate; no selected numerical fluid property model. Later USER reports 30% mass basis.


### ASSUME

**File / record:** support/evidence/2026-10-16_CFG-002_vcu_current_understanding/ASSUME_ASSUMPTIONS.md


**Revision / context:** Snapshot read 2026-10-16


**Locator guide:** ASM-020/021/022/023/026/027; later VSEL/VREG overrides


**Qualification:** Shared model defaults are modeling choices, not observed VCU valve states. Historical heater lengths/contact/ranges superseded by later dated decisions.


### CURRENT

**File / record:** support/evidence/2026-10-16_CFG-002_vcu_current_understanding/CURRENT_INSULATION_CURRENT.md


**Revision / context:** GEO-010 2026-10-16


**Locator guide:** Regional assignment table and qualifications


**Qualification:** Current reported coverage; estimated thickness; not product confirmation.


## Native channels

### STC2

**Reference / domain:** STC-02 / main_loop


**Working role / operator:** Outside pipe surface; local bare contact


**Basis / source:** VSEL; WORK; XWALK


**Limits / next evidence:** Working binding, 2026-10-14. CAD reference is not sensing junction; calibration and historical applicability unknown.


### STC3

**Reference / domain:** STC-03 / main_loop


**Working role / operator:** Outside pipe surface; local bare contact


**Basis / source:** VSEL; WORK; XWALK


**Limits / next evidence:** Working binding, 2026-10-14. CAD reference is not sensing junction; calibration and historical applicability unknown.


### STC4

**Reference / domain:** STC-04 / main_loop


**Working role / operator:** Outside pipe surface; local bare contact


**Basis / source:** VSEL; WORK; XWALK


**Limits / next evidence:** Working binding, 2026-10-14. CAD reference is not sensing junction; calibration and historical applicability unknown.


### STC5

**Reference / domain:** STC-05 / main_loop


**Working role / operator:** Outside pipe surface; local bare contact


**Basis / source:** VSEL; WORK; XWALK


**Limits / next evidence:** Working binding, 2026-10-14. CAD reference is not sensing junction; calibration and historical applicability unknown.


### STC6

**Reference / domain:** STC-06 / main_loop


**Working role / operator:** Outside pipe surface; local bare contact


**Basis / source:** VSEL; WORK; XWALK


**Limits / next evidence:** Working binding, 2026-10-14. CAD reference is not sensing junction; calibration and historical applicability unknown.


### PTC1

**Reference / domain:** PTC-01 / main_loop


**Working role / operator:** Primary fluid; centerline observation assumed


**Basis / source:** VSEL; WORK; XWALK / ASM-023


**Limits / next evidence:** Working binding, 2026-10-14. CAD reference is not sensing junction; calibration and historical applicability unknown.


### STC7

**Reference / domain:** STC-07 / main_loop


**Working role / operator:** Outside pipe surface; local bare contact


**Basis / source:** VSEL; WORK; XWALK


**Limits / next evidence:** Working binding, 2026-10-14. CAD reference is not sensing junction; calibration and historical applicability unknown.


### PTC3

**Reference / domain:** PTC-03 / main_loop


**Working role / operator:** Primary fluid; centerline observation assumed


**Basis / source:** VSEL; WORK; XWALK / ASM-023


**Limits / next evidence:** Working binding, 2026-10-14. CAD reference is not sensing junction; calibration and historical applicability unknown.


### STC8

**Reference / domain:** STC-08 / main_loop


**Working role / operator:** Outside pipe surface; local bare contact


**Basis / source:** VSEL; WORK; XWALK


**Limits / next evidence:** Working binding, 2026-10-14. CAD reference is not sensing junction; calibration and historical applicability unknown.


### STC9

**Reference / domain:** STC-09 / main_loop


**Working role / operator:** Outside pipe surface; local bare contact


**Basis / source:** VSEL; WORK; XWALK


**Limits / next evidence:** Working binding, 2026-10-14. CAD reference is not sensing junction; calibration and historical applicability unknown.


### STC10

**Reference / domain:** STC-10 / main_loop


**Working role / operator:** Outside pipe surface; local bare contact


**Basis / source:** VSEL; WORK; XWALK


**Limits / next evidence:** Working binding, 2026-10-14. CAD reference is not sensing junction; calibration and historical applicability unknown.


### STC11

**Reference / domain:** STC-11 / main_loop


**Working role / operator:** Outside pipe surface; local bare contact


**Basis / source:** VSEL; WORK; XWALK


**Limits / next evidence:** Working binding, 2026-10-14. CAD reference is not sensing junction; calibration and historical applicability unknown.


### PTC4

**Reference / domain:** PTC-04 / main_loop


**Working role / operator:** Primary fluid; centerline observation assumed


**Basis / source:** VSEL; WORK; XWALK / ASM-023


**Limits / next evidence:** Working binding, 2026-10-14. CAD reference is not sensing junction; calibration and historical applicability unknown.


### STC12

**Reference / domain:** STC-12 / main_loop


**Working role / operator:** Outside pipe surface; local bare contact


**Basis / source:** VSEL; WORK; XWALK


**Limits / next evidence:** Working binding, 2026-10-14. CAD reference is not sensing junction; calibration and historical applicability unknown.


### PTC2

**Reference / domain:** PTC-02 / main_loop


**Working role / operator:** Primary fluid; centerline observation assumed


**Basis / source:** VSEL; WORK; XWALK / ASM-023


**Limits / next evidence:** Working binding, 2026-10-14. CAD reference is not sensing junction; calibration and historical applicability unknown.


### STC1

**Reference / domain:** STC-01 / main_loop


**Working role / operator:** Outside pipe surface; local bare contact


**Basis / source:** VSEL; WORK; XWALK


**Limits / next evidence:** Working binding, 2026-10-14. CAD reference is not sensing junction; calibration and historical applicability unknown.


### PTC6

**Reference / domain:** JTC-A / jacket_port


**Working role / operator:** jacket outlet


**Basis / source:** VSEL; WORK; XWALK


**Limits / next evidence:** Working binding, 2026-10-14. CAD reference is not sensing junction; calibration and historical applicability unknown.


### PTC5

**Reference / domain:** JTC-B / jacket_port


**Working role / operator:** jacket inlet


**Basis / source:** VSEL; WORK; XWALK


**Limits / next evidence:** Working binding, 2026-10-14. CAD reference is not sensing junction; calibration and historical applicability unknown.


### Amb

**Reference / domain:** No accepted XYZ / auxiliary


**Working role / operator:** Room ambient temperature reference


**Basis / source:** XWALK; FOLLOW


**Limits / next evidence:** Native name and candidate role; exact sensor placement, medium, calibration and run-specific use need confirmation.


### Tank

**Reference / domain:** No accepted XYZ / auxiliary


**Working role / operator:** Tank / secondary-boundary temperature reference


**Basis / source:** XWALK; FOLLOW


**Limits / next evidence:** Native name and candidate role; exact sensor placement, medium, calibration and run-specific use need confirmation.


## Current knowledge

### K01

**Topic:** Facility and configuration


**Current understanding:** VCU only; Rev9 documentation DRAFT-007. Current geometry working v3, insulation v7, solid materials v3.


**Basis / source:** WORK; CURRENT; VMAT


**Limits / next evidence:** Draft, not an installed release or model-ready input; ACU evidence does not qualify VCU.


### K02

**Topic:** Coordinates and lengths


**Current understanding:** B origin; x=B_CAD_Z-CAD_Z, y=CAD_Y-B_CAD_Y, n=CAD_X-B_CAD_X. Traverse B-C-D-E-F-G-H-A-B.


**Basis / source:** VSEL; WORK; Geometry


**Limits / next evidence:** A-H are axis endpoints, not virtual corners; lengths/projected spans and bend arcs have different bases.


### K03

**Topic:** Gravity and inclination


**Current understanding:** Working gravity (0,-1,0); straight inclined axes about 10.8 deg; heater chord about 10.79355 deg.


**Basis / source:** VSEL; WORK


**Limits / next evidence:** Installed gravity survey absent; keep n and do not conflate circumferential angle with inclination.


### K04

**Topic:** Heater and lower-right geometry


**Current understanding:** H-A projected union 1346.4962148518246 mm; pieces overlap 7.202344894878479 mm and are offset 0.1515510905213091 mm. G-H is reconstructed spine.


**Basis / source:** VSEL; WORK; CAD dimensions


**Limits / next evidence:** No exact connected hydraulic centerline or silent healing.


### K05

**Topic:** Pipe dimensions


**Current understanding:** Main OD 33.401 mm CAD-derived. Working main ID 26.64 mm rounded nominal, separate from unknown CAD bore; component-specific bores in CAD dimensions.


**Basis / source:** VSEL; DIA; Model choices


**Limits / next evidence:** Main Geometry ID remains blank; do not fill from local spools.


### K06

**Topic:** Insulation


**Current understanding:** Six ordinary-pipe regions fiberglass about 50.8 mm; straight heater ceramic strip only about 6.35 mm; three straight D-E regions bare. Both upper corners insulated; LF-01 locally covered.


**Basis / source:** CURRENT; VREG; VTOP


**Limits / next evidence:** Reported thickness estimates, not measured; local transition/contact surveys and product identity unknown.


### K07

**Topic:** STC contacts


**Current understanding:** All 12 STCs contact bare pipe locally, including on insulated parent regions.


**Basis / source:** VSEL; WORK


**Limits / next evidence:** Do not turn local bare contact into whole-leg bare coverage. Footprints/windows/attachment response unknown.


### K08

**Topic:** Main sensor map


**Current understanding:** 16 working numbered STC/PTC mappings populated in Sensors; STC5 B+942.186081 mm, PTC4 H+63.716137 mm.


**Basis / source:** VSEL; WORK


**Limits / next evidence:** Current working binding; physical tips, serials and historical change dates unknown.


### K09

**Topic:** Jacket map


**Current understanding:** JTC-B = PTC5 inlet; JTC-A = PTC6 outlet. Port reference positions in WORK; no main-loop station invented.


**Basis / source:** VSEL; WORK; Native channels


**Limits / next evidence:** Internal flow routing and actual wetted measurement planes unverified.


### K10

**Topic:** Sensor inventory and exclusions


**Current understanding:** 22 active geometric references: 12 STC + 4 main PTC + 4 LF + 2 JTC; 20 on main loop. Original 23 includes excluded PTC-X. Native core register has 20 channels incl. Amb/Tank.


**Basis / source:** WORK; XWALK; Review issues I04


**Limits / next evidence:** PTC-X excluded from active records, not asserted physically removed. LF mounts are not fiber active extents/channels.


### K11

**Topic:** Observation operators


**Current understanding:** STC outside-wall surface; PTC1-4 centerline primary fluid is a working assumption. Amb/Tank lack accepted XYZ.


**Basis / source:** XWALK; ASSUME ASM-023; VSEL


**Limits / next evidence:** CAD references remain pipe points/mounts, never certified sensing junctions. Angles/radii remain blank.


### K12

**Topic:** Calibration and DAQ


**Current understanding:** Instrument certificates, corrections, Type B uncertainties, coverage factors and response are unknown. Sep2/4 native sampling about 30 Hz, scoped to those runs.


**Basis / source:** DIAG; FOLLOW; Calibration


**Limits / next evidence:** Do not invent calibrations from noise statistics or assign one rate/clock/filter globally.


### K13

**Topic:** Heater source


**Current understanding:** Electrical mat/band heaters reported; modeling extent full projected H-A. Real energized boundaries/power/efficiency/spatial split remain unknown.


**Basis / source:** HEAT; VSEL; WORK


**Limits / next evidence:** Measured Active heater span remains blank; voltage is not watts; clamp positions are mechanical only.


### K14

**Topic:** Cooler geometry and boundaries


**Current understanding:** Shell 1017.5875 mm; complete jacket 1030.2875 mm; envelope starts D+127.56180941009107 mm. Bare pipe under jacket exchanges with coolant.


**Basis / source:** WORK; CAD dimensions; CURRENT


**Limits / next evidence:** Active cooling extent, coolant flow and contact/routing unresolved; envelope is not automatically active area.


### K15

**Topic:** Cooler cycling


**Current understanding:** User reports on/off chiller contributes to heated-plateau oscillation; conditional CAL-004 associations exist.


**Basis / source:** OPCYCLE; FOLLOW


**Limits / next evidence:** No universal period/causality; need controller/switching logs. Separate settled cycle mean from instantaneous equilibrium.


### K16

**Topic:** Fluids


**Current understanding:** VCU options Prop-30 (reported 30% PG by mass), air, water; reported jacket water; primary fill/circuit must be matched to run.


**Basis / source:** USER; PG; FLUIDCFG; XWALK


**Limits / next evidence:** Product/formulation/batch/property functions and operating limits unverified; air has both ambient and possible primary roles.


### K17

**Topic:** Solid properties


**Current understanding:** Nine candidate rho/cp/k functions already in Materials: pipe, fiberglass, heater ceramic. T in K; explicit SI outputs; out-of-range error.


**Basis / source:** VMAT; V5C


**Limits / next evidence:** Working domains pipe 278.15-813 K, fiberglass 278.15-533 K, strip 278.15-1089 K. 5 C extension authorized; not validated, calibration-eligible or operating limits.


### K18

**Topic:** Topology and branches


**Current understanding:** Each CAD exit tube 469.9 mm; top-exit/tank junction geometry does not certify hydraulics. Shared defaults omit BREP and retain TLEP with per-experiment temperature/pressure.


**Basis / source:** CAD dimensions; ASSUME ASM-020/021


**Limits / next evidence:** Installed valves, vents, fill level and actual boundaries unknown. No-throughflow is not adiabatic.


### K19

**Topic:** Model and property selection


**Current understanding:** Physics model and effective reduced-zone model have separate observation/identification contracts; no fluid property model or facility closures approved here.


**Basis / source:** MODEL; FLUIDCFG; Model choices


**Limits / next evidence:** No fitted constants imported or solver migration activated; property candidates calibration-ineligible.


### K20

**Topic:** Historical applicability


**Current understanding:** STC5 changed location; no change dates/run ranges. Earlier solver and diagnostic runs retain Rev8 and original insulation/material selections.


**Basis / source:** VSEL; WORK; FOLLOW


**Limits / next evidence:** Never relabel historical results Rev9 or retroactively relocate sensors without run-specific evidence.


### K21

**Topic:** Experiment inventory


**Current understanding:** 23 native TDMS sources, 22 readable; 19 supplementary CSVs are not independent experiments. July29 waveform unreadable. Sep2/4 provisional ambient candidates.


**Basis / source:** DIAG; TRIAGE


**Limits / next evidence:** Shape labels are exploratory, not evidence of heater commands/fluid identity or accepted steady intervals.


### K22

**Topic:** Known data-quality failures


**Current understanding:** June12 STC6/PTC2/PTC3 include nonphysical Celsius readings. Retain raw, quarantine affected channel intervals and propagate versioned masks; retain unaffected channels.


**Basis / source:** DAQISS; FOLLOW


**Limits / next evidence:** Cause/status/scaling unresolved. June17 auxiliary heater temperatures need separate screens; June17/23 transitions need event interpretation.


### K23

**Topic:** Noise and uncertainty


**Current understanding:** Slow correlated temperature motion persists with averaging; compact ten-second block results are not valid independent-block accuracy bars. CAL-004 explores temporal correlation/covariance.


**Basis / source:** DIAG; FOLLOW


**Limits / next evidence:** No universal noise floor, absolute accuracy, optimal averaging or validated block length established; Type B absent.


### K24

**Topic:** Run identity and events


**Current understanding:** Short July15 ambient-named acquisition may be same liquid experiment; clocks and media need confirmation. Chiller, heater and jolt events require run-specific logs.


**Basis / source:** TRIAGE; FOLLOW


**Limits / next evidence:** Do not call it an independent air-only test from filename or fit material constants without boundary/validity qualification.


### K25

**Topic:** Identification and validation


**Current understanding:** Relaxation gives time constants/parameter ratios without an absolute power or fixed-capacitance anchor. Existing fits/holdouts are conditional studies, not facility validation.


**Basis / source:** MODEL; FOLLOW


**Limits / next evidence:** Approve intended-use tolerances, identifiability, calibration/withheld split and frozen model before accuracy claims.


### K26

**Topic:** Remaining experimental returns


**Current understanding:** Need installed surveys and dated photos, sensor identities/depths, calibration/DAQ status, real heater power/wiring, coolant flow/route/control, fluid batch, boundary states and historical dates.


**Basis / source:** Requirements; Review issues; Phase requests


**Limits / next evidence:** Plans P0-P4 remain draft; records do not authorize operation or establish Nick approval.

