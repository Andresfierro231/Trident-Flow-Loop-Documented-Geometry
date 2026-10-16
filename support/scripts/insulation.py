"""Resolve recorded insulation coverage without inferring installed boundaries or resistance."""
import math

# Stable IDs are model-interface keys. These do not imply physical flow direction.
REGIONS = (
    ('INS-01', 'Upcomer', 'upcomer', 'Full segment'),
    ('INS-02', 'Top-left corner', 'upper_left_bend', 'Full schematic corner'),
    ('INS-03', 'Pre-cooler', 'cooler', 'Segment start to Complete jacket start'),
    ('INS-04', 'Cooler', 'cooler', 'Complete jacket start to Complete jacket end'),
    ('INS-05', 'Post-cooler', 'cooler', 'Complete jacket end to segment end'),
    ('INS-06', 'Top-right corner', 'upper_right_bend', 'Full schematic corner'),
    ('INS-07', 'Downcomer', 'downcomer', 'Full segment'),
    ('INS-08', 'Bottom-right corner', 'lower_right_bend', 'Full schematic corner'),
    ('INS-09', 'Heater', 'heater', 'Full segment'),
    ('INS-10', 'Bottom-left corner', 'lower_left_bend', 'Full schematic corner'),
)
HEADERS = ('Region ID', 'Region', 'Boundary reference', 'Coverage', 'Material ID',
           'Thickness mm', 'Evidence type', 'Evidence file / location', 'Notes')
COVERAGE = ('Unknown', 'Insulated', 'Bare')
EVIDENCE_TYPES = ('Unknown', 'CAD-derived', 'Installed measurement', 'Reported', 'Modeling assumption')


def default_rows():
    return [dict(zip(HEADERS, (rid, name, boundary, 'Unknown', None, None, 'Unknown', None,
                              'Identify the insulated surface, especially jacket exterior versus pipe.' if rid == 'INS-04' else None)))
            for rid, name, segment, boundary in REGIONS]


def resolve_regions(tables, segments, notes):
    present = 'Insulation regions' in tables
    rows = tables.get('Insulation regions', default_rows())
    ids = [r.get('Region ID') for r in rows]
    expected = {r[0] for r in REGIONS}
    if len(ids) != len(set(ids)):
        raise ValueError('Insulation regions: duplicate Region ID.')
    if set(ids) != expected:
        raise ValueError('Insulation regions: retain all ten Region IDs INS-01 through INS-10.')
    if not present:
        notes.append('Insulation regions worksheet absent: all coverage is Unknown; no insulation is inferred from legacy thickness fields.')
    indexed = {r['Region ID']: r for r in rows}
    materials = {r['Material ID'] for r in tables['Materials']}
    jackets = [r for r in tables['Thermal spans'] if r.get('Feature') == 'Complete jacket']
    if len(jackets) > 1:
        raise ValueError('Insulation regions: Complete jacket is ambiguous; retain one boundary reference.')
    jacket = jackets[0] if jackets else None
    top = segments.get('cooler')
    if top is None or top['Kind'] != 'straight':
        raise ValueError('Insulation regions: the cooler must be a named straight segment.')
    length = top['axial_length_mm']
    boundaries = None
    if jacket:
        if jacket.get('Role') != 'Jacket envelope' or jacket.get('Segment') != 'cooler':
            raise ValueError('Insulation regions: Complete jacket must be the cooler Jacket envelope.')
        a, b = jacket.get('Start mm'), jacket.get('End mm')
        if a is not None and b is not None:
            # solve() has already checked ordering, range, and endpoint identity.
            boundaries = (float(a), float(b)) if jacket['From endpoint'] == top['Start'] else (length - float(b), length - float(a))
    if boundaries is None:
        notes.append('Insulation regions INS-03 through INS-05: jacket boundaries unresolved; top-region overlays omitted.')
    result = []
    for rid, name, segment_name, boundary in REGIONS:
        row = indexed[rid]
        if any(key not in row for key in HEADERS):
            raise ValueError(f'Insulation regions / {rid}: keep the row-5 column headers unchanged.')
        if row['Region'] != name or row['Boundary reference'] != boundary:
            raise ValueError(f'{rid}: Region and Boundary reference identify fixed regions; restore their reference text.')
        coverage = row.get('Coverage')
        if coverage not in COVERAGE:
            raise ValueError(f'{rid}: Coverage must be Unknown, Insulated or Bare; use Unknown rather than a blank.')
        material = row.get('Material ID') or None
        if material and material not in materials:
            raise ValueError(f'{rid}: Material ID {material} is not in Materials.')
        thickness = row.get('Thickness mm')
        if thickness in (None, ''):
            thickness = None
        else:
            try:
                thickness = float(thickness)
            except (ValueError, TypeError):
                raise ValueError(f'{rid}: Thickness mm must be a number without unit text.') from None
            if not math.isfinite(thickness) or thickness < 0:
                raise ValueError(f'{rid}: Thickness mm must be finite and nonnegative.')
            if coverage == 'Insulated' and thickness == 0:
                raise ValueError(f'{rid}: an entered insulated thickness must be positive.')
            if coverage == 'Bare' and thickness > 0:
                raise ValueError(f'{rid}: Bare coverage contradicts positive insulation thickness.')
        if coverage == 'Bare' and material:
            raise ValueError(f'{rid}: clear insulation Material ID when coverage is Bare.')
        evidence_type = row.get('Evidence type')
        if evidence_type not in EVIDENCE_TYPES:
            raise ValueError(f'{rid}: choose a listed Evidence type.')
        evidence = row.get('Evidence file / location') or None
        if coverage != 'Unknown' and (evidence_type == 'Unknown' or not evidence):
            notes.append(f'{rid}: {coverage} is recorded without complete supporting evidence; installed coverage is not verified.')
        seg = segments.get(segment_name)
        if seg is None:
            raise ValueError(f'{rid}: missing geometry segment {segment_name}.')
        straight = seg['Kind'] == 'straight'
        start_station = 0.0 if straight else None
        end_station = seg['axial_length_mm'] if straight else None
        basis = str(seg.get('Status') or 'Unknown')
        source = seg.get('Source')
        resolved = True
        if rid in ('INS-03', 'INS-04', 'INS-05'):
            basis = str(jacket.get('Status') or 'Unknown') if jacket else 'Unknown'
            basis += '; mechanical jacket envelope; provisional insulation partition'
            source = jacket.get('Source') if jacket else None
            if boundaries is None:
                start_station = end_station = None
                resolved = False
            else:
                j0, j1 = boundaries
                start_station, end_station = {'INS-03': (0.0, j0), 'INS-04': (j0, j1), 'INS-05': (j1, length)}[rid]
        if straight and resolved:
            a, b = seg['start_xyz_mm'], seg['end_xyz_mm']
            start = tuple(a[k] + start_station / seg['axial_length_mm'] * (b[k] - a[k]) for k in range(3))
            end = tuple(a[k] + end_station / seg['axial_length_mm'] * (b[k] - a[k]) for k in range(3))
        elif resolved:
            start, end = seg['start_xyz_mm'], seg['end_xyz_mm']
        else:
            start = end = None
        legacy = seg.get('Insulation mm')
        if legacy is not None:
            if coverage == 'Bare' and float(legacy) > 0:
                notes.append(f'{rid}: Bare coverage conflicts with legacy Geometry Insulation mm; the regional record is authoritative.')
            elif coverage == 'Unknown' or thickness is None:
                notes.append(f'{rid}: legacy Geometry insulation thickness is not used to infer regional coverage or thickness.')
            elif not math.isclose(float(legacy), thickness, abs_tol=1e-9):
                notes.append(f'{rid}: regional thickness conflicts with legacy Geometry Insulation mm; the regional record is authoritative.')
        result.append(dict(region_id=rid, name=name, coverage=coverage, segment=segment_name,
                           segment_start_endpoint=seg['Start'], segment_end_endpoint=seg['End'],
                           geometry_kind='straight' if straight else 'schematic_corner',
                           geometry_qualification=seg.get('Notes'),
                           boundary_reference=boundary, boundary_basis=basis, boundary_source=source,
                           extent_resolved=resolved, start_station_mm=start_station, end_station_mm=end_station,
                           start_xyz_mm=start, end_xyz_mm=end,
                           length_mm=(end_station - start_station) if straight and resolved else None,
                           material_id=material, thickness_mm=thickness, evidence_type=evidence_type,
                           evidence_file_location=evidence, notes=row.get('Notes')))
    return result


def export_regions(tables, model, digest):
    return dict(schema_version=1, facility=model['settings']['Facility'],
                configuration_id=model['settings']['Configuration ID'],
                effective_date=model['settings'].get('Effective date'), input_sha256=digest,
                coverage_record_present='Insulation regions' in tables,
                coordinate_frame=dict(origin=model['settings']['Origin'], units='mm',
                                      x='drawing right', y='drawing up', z='out of drawing'),
                station_convention='Millimetres along the parent straight segment from its Start endpoint; pre/post denote drawing traversal, not measured flow direction.',
                qualifications=['Coverage is a recorded state, not a release approval.',
                                'Band width is illustrative, not insulation thickness.',
                                'Jacket-derived top partitions are provisional; they do not establish active cooling.',
                                'Corner path lengths are unknown. No resistance or boundary-condition calculation is performed.'],
                regions=model['insulation_regions'])


def insulation_diagram(model, Drawing):
    points = model['points']
    xmin, xmax = min(p[0] for p in points.values()), max(p[0] for p in points.values())
    ymin, ymax = min(p[1] for p in points.values()), max(p[1] for p in points.values())
    scale = min(660 / (xmax - xmin), 760 / (ymax - ymin))
    def screen(p):
        return (370 + (p[0] - xmin) * scale, 390 + (ymax - p[1]) * scale)
    fig = Drawing('INSULATION COVERAGE', model['settings']['Configuration ID'] + ' | recorded regional coverage')
    for x, title, color, width, dash, opacity in (
            (80, 'Insulated', '#287FA3', 30, False, .28),
            (480, 'Bare', '#263D4B', 4, False, 1),
            (820, 'Unknown (?)', '#7B8992', 22, True, .35)):
        fig.line((x, 185), (x + 70, 185), color, width, dash, opacity)
        fig.text(x + 90, 192, title, 23)
    for region in model['insulation_regions']:
        if not region['extent_resolved']:
            continue
        start, end = screen(region['start_xyz_mm']), screen(region['end_xyz_mm'])
        if region['coverage'] == 'Insulated':
            fig.line(start, end, '#287FA3', 36, opacity=.28)
        elif region['coverage'] == 'Unknown':
            fig.line(start, end, '#7B8992', 22, True, .35)
    # Centerlines remain readable above the transparent coverage layer.
    for seg in model['segments'].values():
        fig.line(screen(seg['start_xyz_mm']), screen(seg['end_xyz_mm']), width=3, dash=seg['Kind'] == 'bend')
    placements = ((75, 700, 'start'), (75, 340, 'start'), (300, 260, 'middle'),
                  (700, 260, 'middle'), (1090, 260, 'middle'), (1110, 440, 'start'),
                  (1110, 790, 'start'), (1110, 1150, 'start'), (700, 1260, 'middle'),
                  (75, 1150, 'start'))
    for region, (x, y, anchor) in zip(model['insulation_regions'], placements):
        if region['extent_resolved']:
            a, b = screen(region['start_xyz_mm']), screen(region['end_xyz_mm'])
            middle = ((a[0] + b[0]) / 2, (a[1] + b[1]) / 2)
            leader = (x + 185 if anchor == 'start' and x < 300 else x - 10 if anchor == 'start' else x, y + 58)
            fig.line(middle, leader, '#98A7B1', 1)
        fig.text(x, y, region['region_id'] + ' / ' + region['name'], 20, anchor=anchor, bold=True)
        state = region['coverage'] + (' (?)' if region['coverage'] == 'Unknown' else '')
        if not region['extent_resolved']:
            state += ' / extent unresolved'
        fig.text(x, y + 28, state, 19, '#576976', anchor)
        if region['geometry_kind'] == 'schematic_corner':
            fig.text(x, y + 51, 'Schematic corner', 16, '#576976', anchor)
    top_regions = [r for r in model['insulation_regions'] if r['region_id'] in ('INS-03', 'INS-04')]
    for region in top_regions:
        if region['extent_resolved']:
            fig.circle(*screen(region['end_xyz_mm']), r=5)
    fig.text(70, 1370, 'Coverage bands are illustrative; their width does not represent physical thickness.', 18)
    fig.text(70, 1403, 'Top regions use provisional jacket boundaries. Pre/post follow the drawing traversal.', 18)
    fig.text(70, 1436, 'Corner connectors are schematic; no elbow length or thermal resistance is inferred.', 18)
    return fig
