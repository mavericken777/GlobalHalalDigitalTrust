"""Validate trip/document controls; render the board without asserting real-world readiness.

Version 1.1, 2026-10-01. Existing executed instruments are outside this tool's scope.
"""
from pathlib import Path
import argparse
import json
import re

ROOT = Path(__file__).resolve().parents[1]
READY_PATH = '00_EXECUTIVE_COMMAND/october-2026-readiness.json'
SIGNING_PATH = 'CHINA_TRIP_2026/signing-register.json'
START, END = '<!-- COMMON_TERMS_START -->', '<!-- COMMON_TERMS_END -->'
CANONICAL = 'Authority → Standard / Instrument → Clause / Requirement → Applicability → Control → HCP / SCCP → Evidence → Audit Test → Finding → Corrective Action → Re-verification → Authority Gate → Trust State → Operational Release'

def load(path, root=ROOT):
    return json.loads((root / path).read_text())

def derive_status(data):
    gates = data['gates']
    expected = {**{f'T{i:02}':'travel' for i in range(1,14)}, **{f'S{i:02}':'signing' for i in range(1,6)}, 'D01':'demonstration', 'D02':'communications', 'G01':'travel', 'G02':'travel', 'G03':'signing', **{f'P{i:02}':'production' for i in range(1,5)}}
    ids = [g['id'] for g in gates]
    assert len(ids) == len(set(ids)) and set(ids) == set(expected), 'missing/duplicate/unknown readiness gate'
    for gate in gates:
        assert gate['workstream'] == expected[gate['id']], 'gate reassignment needs controlled validator revision'
        assert gate['status'] in {'OPEN', 'CLOSED'}
        if gate['status'] == 'CLOSED':
            assert isinstance(gate.get('evidence_reference'),str) and gate['evidence_reference'].strip(), 'closure requires evidence'
    def all_closed(stream):
        selected = [g for g in gates if g['workstream'] == stream]
        return bool(selected) and all(g['status'] == 'CLOSED' for g in selected)
    return {'status': 'TRAVEL_READY' if all_closed('travel') else 'NOT_TRAVEL_READY',
            'signing_status': 'SIGNING_READY' if all_closed('signing') else 'NOT_SIGNING_READY',
            'demo_status': 'REHEARSAL_RECORDED' if all_closed('demonstration') else 'REHEARSAL_PENDING',
            'production_status': 'PRODUCTION_GATES_RECORDED_CLOSED' if all_closed('production') else 'NOT_PRODUCTION_READY'}

def board(data):
    derived=derive_status(data)
    text='\n'+' · '.join(f'**{k}: `{v}`**' for k,v in derived.items())+'\n\n'
    text+='| Gate | Workstream | Action | Proposed accountable owner | Due | Status |\n|---|---|---|---|---|---|\n'
    for g in data['gates']:
        values=[g['id'],g['workstream'],g['action'],g['proposed_owner'],g['target_date'],g['status']]
        text+='| '+' | '.join(v.replace('|','/') for v in values)+' |\n'
    return text+'\n'

def common_block(root=ROOT):
    text=(root/'CHINA_TRIP_2026/MOA_TEMPLATES/COMMON_TERMS.md').read_text()
    return START+text.split(START,1)[1].split(END,1)[0]+END

def render(root=ROOT):
    data=load(READY_PATH,root)
    data.update(derive_status(data))
    (root/READY_PATH).write_text(json.dumps(data,indent=2,ensure_ascii=False)+'\n')
    path=root/'CHINA_TRIP_2026/EXECUTION_BOARD.md'
    text=path.read_text()
    text=re.sub(r'(?s)(<!-- READINESS_START -->).*?(<!-- READINESS_END -->)',lambda m:m[1]+board(data)+m[2],text)
    path.write_text(text)

def sync_terms(root=ROOT):
    block=common_block(root)
    for item in load(SIGNING_PATH,root)['instruments']:
        path=root/item['path']
        text=path.read_text()
        assert text.count(START)==text.count(END)==1
        path.write_text(re.sub(re.escape(START)+'.*?'+re.escape(END),lambda _:block,text,flags=re.S))

def _capture(pattern, content, label):
    match = re.search(pattern, content, flags=re.M)
    assert match, f'missing controlled headline field: {label}'
    return match.group(1)

def documented_readiness(path, content):
    """Parse the explicitly labelled controlled readiness fields, never substrings.

    Public documents may legitimately mention operator-reported states alongside the
    controlled register state. Validation therefore extracts the labelled field and
    compares the complete token, so TRAVEL_READY cannot satisfy NOT_TRAVEL_READY (or
    vice versa) merely because one token is a substring of the other.
    """
    if path == 'README.md':
        match = re.search(
            r'\[readiness register\]\([^)]+\) records travel as `([^`]+)` and signing as `([^`]+)`\.',
            content,
            flags=re.M,
        )
        assert match, f'missing controlled headline fields: {path}'
        return {'status': match.group(1), 'signing_status': match.group(2)}
    if path == 'STATUS.md':
        return {
            'status': _capture(r'^\| Travel \|.*?controlled register `([^`]+)` \|', content, f'{path}:travel'),
            'signing_status': _capture(r'^\| Signing \| `([^`]+)` \|', content, f'{path}:signing'),
        }
    if path == 'CHINA_TRIP_2026/00_READ_THIS_FIRST.md':
        return {
            'status': _capture(r'^\| Travel \|.*?controlled register `([^`]+)`.*?\|$', content, f'{path}:travel'),
            'signing_status': _capture(r'^\| Signing \| `([^`]+)`.*?\|$', content, f'{path}:signing'),
        }
    raise AssertionError(f'unregistered readiness headline document: {path}')

def validate(root=ROOT):
    data=load(READY_PATH,root)
    assert all(data.get(k)==v for k,v in derive_status(data).items()), 'stale derived readiness; run --render'
    rendered=(root/'CHINA_TRIP_2026/EXECUTION_BOARD.md').read_text().split('<!-- READINESS_START -->',1)[1].split('<!-- READINESS_END -->',1)[0]
    assert rendered==board(data), 'execution board stale; run --render'
    for path in ['README.md','00_EXECUTIVE_COMMAND/README.md','AGENTS.md']:
        assert CANONICAL in (root/path).read_text(), f'canonical path drift: {path}'
    for status_file in ['README.md', 'STATUS.md', 'CHINA_TRIP_2026/00_READ_THIS_FIRST.md']:
        content=(root/status_file).read_text()
        documented=documented_readiness(status_file, content)
        for key in ['status', 'signing_status']:
            assert documented[key] == data[key], f'stale headline status: {status_file}:{key} expected {data[key]} got {documented[key]}'
    instruments=load(SIGNING_PATH,root)['instruments']
    assert len({i['id'] for i in instruments})==len(instruments)
    assert len({i['path'] for i in instruments})==len(instruments), 'competing scopes share one signing draft'
    original={i['id']:i for i in instruments if i['id'].startswith('M')}
    assert set(original)=={f'M{i}' for i in []} or set(original)=={f'M{i:02}' for i in range(1,7)}
    block=common_block(root)
    for i in instruments:
        content=(root/i['path']).read_text()
        assert block in content, f'common terms drift: {i["id"]}'
        assert i['status'] in {'DRAFT','APPROVED_FOR_SIGNATURE','EXECUTED','DEFERRED'}
        if i['status'] in {'APPROVED_FOR_SIGNATURE','EXECUTED'}:
            assert i.get('execution_evidence'), 'signing approval requires controlled evidence reference'
        if i['id'] in {'M01','M02','M05','M06'}:
            assert 'phc' in i['parties'] and 'PERAK HALAL CORPORATION SDN BHD' in content and 'For PHC:' in content, f'PHC missing: {i["id"]}'
    assert 'AGRICULTURAL_DEVELOPMENT' in original['M04']['path'], 'M04 agricultural scope lost'
    partners=load('00_EXECUTIVE_COMMAND/partner-registry.json',root)['partners']
    assert len({p['id'] for p in partners})==len(partners)
    assert 'china-food-security-lab' in {p['id'] for p in partners}, 'legacy lab identity removed'
    for partner in partners:
        for key in ['contractual_status','canonical_path_position','evidence_class','authority_boundary','open_gates','integration_points','repository_path']:
            assert partner.get(key), f'missing partner control {partner["id"]}: {key}'
        assert partner['path']==partner['repository_path'] and (root/partner['path']).is_dir()
    # Validate only active trip links; historical documents retain their own lineage.
    for path in (root/'CHINA_TRIP_2026').rglob('*.md'):
        for target in re.findall(r'\]\(([^)]+)\)',path.read_text()):
            if '://' in target or target.startswith('#'):
                continue
            assert (path.parent/target.split('#')[0]).exists(), f'broken link: {path}: {target}'
    return {'trip_controls':'PASS','active_drafts':len(instruments),**derive_status(data)}

if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--render',action='store_true')
    parser.add_argument('--sync-terms',action='store_true')
    args=parser.parse_args()
    if args.sync_terms: sync_terms()
    if args.render: render()
    print(json.dumps(validate()))
