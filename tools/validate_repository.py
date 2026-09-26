"""Validate tracked structured artifacts and the October readiness invariants.

Run from any directory: python tools/validate_repository.py
This checks structure, never authority, reservations or production readiness.
"""
from pathlib import Path
import gzip
import hashlib
import sys
import json
import subprocess
import xml.etree.ElementTree as ET
from datetime import date

ROOT = Path(__file__).resolve().parents[1]


def validate():
    files = subprocess.check_output(['git', 'ls-files', '-z'], cwd=ROOT).decode().split('\0')
    quarantine = json.loads((ROOT / '00_EXECUTIVE_COMMAND/artifact-quarantine-2026-09-26.json').read_text())['items']
    known = {x['path']: x for x in quarantine}
    for name, item in known.items():
        assert hashlib.sha256((ROOT / name).read_bytes()).hexdigest() == item['sha256'], f'quarantine changed: {name}; review before clearing'
    counts = {'json': 0, 'gzip_json': 0, 'svg': 0}
    for name in filter(None, files):
        path = ROOT / name
        if name in known:
            continue
        if name.endswith('.json'):
            json.loads(path.read_text()); counts['json'] += 1
        elif name.endswith('.json.gz'):
            json.loads(gzip.decompress(path.read_bytes())); counts['gzip_json'] += 1
        elif name.endswith('.svg'):
            ET.parse(path); counts['svg'] += 1
    manifest_dir = ROOT / 'master-standards-stack/verified-2026-09-17'
    manifest = json.loads((manifest_dir / 'MANIFEST.json').read_text())
    for name in manifest['files']:
        assert (manifest_dir / name).is_file(), f'missing baseline file {name}'
    gates = json.loads((ROOT / '00_EXECUTIVE_COMMAND/october-2026-readiness.json').read_text())
    dates = gates['dates']
    days = (date.fromisoformat(dates['end']) - date.fromisoformat(dates['start'])).days
    assert days + 1 == dates['days'] == 8 and days == dates['nights'] == 7
    people = gates['travellers']
    assert people['malaysia'] + people['hong_kong'] == people['total'] == 12
    ids = [g['id'] for g in gates['gates']]
    assert len(ids) == len(set(ids)), 'duplicate gate ID'
    for gate in gates['gates']:
        date.fromisoformat(gate['target_date'])
        assert gate['proposed_owner'] and gate['closure_evidence_required']
        assert gate['status'] in {'OPEN', 'CLOSED'}
        if gate['status'] == 'CLOSED':
            assert gate['evidence_reference'], 'cannot close without evidence'
    if any(g['status'] == 'OPEN' and g['domain'] == 'mission' for g in gates['gates']):
        assert gates['status'] == 'NOT_TRAVEL_READY'
    print(json.dumps({'structural_checks': 'PASS_WITH_QUARANTINE', 'artifacts': counts, 'mission_gates': len(ids),
                      'mission_status': gates['status'], 'authority_verified': False, 'quarantined_files': list(known)}))


if __name__ == '__main__':
    validate()
    if '--strict' in sys.argv:
        quarantine = json.loads((ROOT / '00_EXECUTIVE_COMMAND/artifact-quarantine-2026-09-26.json').read_text())
        if quarantine['items']:
            raise SystemExit('BLOCKED: quarantined source artifacts remain')
