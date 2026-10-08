"""Fail on missing relative Markdown link targets in tracked repository files."""
from pathlib import Path
import re, subprocess, sys
from urllib.parse import unquote, urlsplit
ROOT=Path(__file__).resolve().parents[1]
LINK=re.compile(r'(?<!!)\[[^\]]*\]\(([^)]+)\)')
def main():
    names=subprocess.check_output(['git','ls-files','-z'],cwd=ROOT).decode().split('\0')
    deleted=set(subprocess.check_output(['git','ls-files','--deleted','-z'],cwd=ROOT).decode().split('\0'))
    missing=[];checked=0
    for name in filter(lambda x:x.endswith('.md'),names):
        if name in deleted:continue
        source=ROOT/name
        if not source.is_file():
            missing.append(f'{name}: tracked file missing')
            continue
        for lineno,line in enumerate(source.read_text(errors='replace').splitlines(),1):
            for match in LINK.finditer(line):
                raw=match.group(1).split(' ')[0].strip('<>')
                parsed=urlsplit(raw)
                if parsed.scheme or parsed.netloc or not parsed.path or parsed.path.startswith('/'):
                    continue
                checked+=1
                if not (source.parent/unquote(parsed.path)).exists():
                    missing.append(f'{name}:{lineno}: {raw}')
    for problem in missing:print(problem,file=sys.stderr)
    print(f'Checked {checked} relative Markdown links in tracked files; missing: {len(missing)}')
    return 1 if missing else 0
if __name__=='__main__':raise SystemExit(main())
