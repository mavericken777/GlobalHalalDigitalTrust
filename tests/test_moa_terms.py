import importlib.util
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('sync_moa_terms', ROOT / 'tools/sync_moa_terms.py')
sync = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sync)


class SharedMoATerms(unittest.TestCase):
    def test_draft_terms_match_the_shared_source(self):
        source = (ROOT / 'CHINA_TRIP_2026/MOA_TEMPLATES/COMMON_TERMS.md').read_text(encoding='utf-8')
        start, end = sync.START, sync.END
        expected = start + source.split(start, 1)[1].split(end, 1)[0] + end
        register = json.loads((ROOT / sync.SIGNING_PATH).read_text(encoding='utf-8'))
        for item in register['instruments']:
            content = (ROOT / item['path']).read_text(encoding='utf-8')
            self.assertIn(expected, content, item['id'])


if __name__ == '__main__':
    unittest.main()
