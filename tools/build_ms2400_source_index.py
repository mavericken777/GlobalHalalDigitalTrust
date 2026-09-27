"""Build a non-normative locator index from user-held MS 2400 PDFs.

Source PDFs are intentionally kept outside this public repository. The output
contains clause numbers and PDF-page locators only, never standard wording.
Version 1.0; control date 2026-09-27; [SOURCE-LOCKED] for licensed text.
"""
from __future__ import annotations
import argparse
import gzip
import hashlib
import io
import json
from pathlib import Path
import re
import tarfile

ROOT = Path(__file__).resolve().parents[1]
DEST = ROOT / 'master-standards-stack/iq300-full-matrix/source-index-2026-09-27'
EXPECTED = {
    1: ('MS2400-1_2019.pdf', '1e5c635cbb434465f4deb43ffb0ae7a52040210eab46a517593390443bc4d7a2', 42, 192),
    2: ('MS2400-2_2019.pdf', 'd6369596a188446a5916e0d7d946d56e2a0bdcf6675d01d1a9e1cff204ff6720', 43, 206),
    3: ('MS2400-3_2019.pdf', '8e757fa1821edb7a246dbf3146d8e44533c4d32badf5c214b9ab7d32b1c61058', 48, 230),
}
HEADING = re.compile(r'(?m)^\s*([4-8](?:\.\d+){1,5})\s+(?=[A-Za-z])')

def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

def encode(obj) -> bytes:
    return (json.dumps(obj, ensure_ascii=False, indent=2) + '\n').encode()

def build(source_dir: Path):
    try:
        import fitz
    except ImportError as exc:
        raise SystemExit('PyMuPDF is required to build the local source indexes') from exc
    DEST.mkdir(parents=True, exist_ok=True)
    content = {}
    sources = []
    for part, (filename, sha, pages, expected) in EXPECTED.items():
        pdf = source_dir / filename
        blob = pdf.read_bytes()
        assert digest(blob) == sha, f'unknown/revised input PDF: {filename}'
        doc = fitz.open(stream=blob, filetype='pdf')
        assert len(doc) == pages
        found = {}
        for pdf_page, page in enumerate(doc, 1):
            if pdf_page <= 8:
                continue  # front matter and contents are not operative section headings
            for match in HEADING.finditer(page.get_text()):
                clause = match.group(1)
                found.setdefault(clause, []).append(pdf_page)
        assert len(found) == expected, f'clause count drift: part {part} {len(found)} != {expected}'
        filename_out = f'MS2400-{part}_2019_CLAUSE_LOCATORS.json'
        obj = {
            'artifact': filename_out, 'version': '1.0', 'control_date': '2026-09-27',
            'source': filename, 'source_sha256': sha, 'source_pdf_pages': pages,
            'edition': f'MS 2400-{part}:2019',
            'classification': 'LOCATORS_ONLY_NO_NORMATIVE_TEXT',
            'extraction': 'numbered headings in PDF body, sections 4-8; PDF pages 1-based',
            'count': len(found),
            'locators': [
                {'clause': key, 'pdf_page': found[key][0], 'pdf_pages': sorted(set(found[key]))}
                for key in sorted(found, key=lambda x: tuple(map(int, x.split('.'))))
            ],
        }
        data = encode(obj)
        content[filename_out] = data
        sources.append({
            'name': filename, 'sha256': sha, 'pages': pages,
            'locator_count': len(found), 'locator_file': filename_out,
            'locator_sha256': digest(data), 'permission_to_redistribute': 'NOT_ESTABLISHED',
            'duplicate_identifiers': {key: value for key, value in found.items() if len(value) > 1},
        })
    manifest = {
        'artifact': 'SOURCE_INDEX_MANIFEST.json', 'version': '1.0', 'control_date': '2026-09-27',
        'scope': 'Three source-held 2019 editions; no normative clause text or automatic control rules',
        'sources': sources, 'total_locators': sum(x['locator_count'] for x in sources),
        'historical_object_count': 613,
        'history_note': 'The 187/201/225 control-object set omitted five deeply nested visible headings in each standard. It is not the full locator inventory.',
        'license_boundary': 'Original supplied PDFs are single-user licensed to third parties; copying/networking prohibited on their covers. They are excluded from this public package.',
        'archive': 'IQ300_MS2400_SOURCE_INDEX_2026-09-27.tar.gz',
        'archive_scope': 'Manifest and three clause/page locator JSON files only; not a replacement for proprietary source text or historical control mappings.',
    }
    content['SOURCE_INDEX_MANIFEST.json'] = encode(manifest)
    for filename, data in content.items():
        (DEST / filename).write_bytes(data)
    archive = DEST / manifest['archive']
    with archive.open('wb') as stream:
        with gzip.GzipFile(filename='', mode='wb', fileobj=stream, mtime=0) as zipped:
            with tarfile.open(mode='w', fileobj=zipped) as tar:
                for filename, data in sorted(content.items()):
                    info = tarfile.TarInfo(filename)
                    info.size = len(data)
                    info.mtime = 0
                    info.uid = info.gid = 0
                    info.uname = info.gname = ''
                    info.mode = 0o644
                    tar.addfile(info, io.BytesIO(data))
    print(json.dumps({'locators': manifest['total_locators'], 'archive_sha256': digest(archive.read_bytes()), 'index_dir': str(DEST)}))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('source_dir', type=Path, help='private local directory with the three source-held PDF copies')
    build(parser.parse_args().source_dir)
