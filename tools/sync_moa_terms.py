"""Synchronize the shared proposed-terms block across the MoA draft set."""
from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[1]
SIGNING_PATH = 'CHINA_TRIP_2026/signing-register.json'
START, END = '<!-- COMMON_TERMS_START -->', '<!-- COMMON_TERMS_END -->'


def sync_terms(root=ROOT):
    source = (root / 'CHINA_TRIP_2026/MOA_TEMPLATES/COMMON_TERMS.md').read_text(encoding='utf-8')
    assert source.count(START) == source.count(END) == 1
    block = START + source.split(START, 1)[1].split(END, 1)[0] + END
    register = json.loads((root / SIGNING_PATH).read_text(encoding='utf-8'))
    for item in register['instruments']:
        path = root / item['path']
        content = path.read_text(encoding='utf-8')
        assert content.count(START) == content.count(END) == 1, f"shared terms markers invalid: {item['id']}"
        path.write_text(re.sub(re.escape(START) + '.*?' + re.escape(END), lambda _: block, content, flags=re.S), encoding='utf-8')


if __name__ == '__main__':
    sync_terms()
    print('Shared proposed MoA terms synchronized.')
