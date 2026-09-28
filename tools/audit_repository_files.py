"""Create a point-in-time file inventory; this is not a normative or production audit."""
from pathlib import Path
import csv,gzip,hashlib,io,json,subprocess,tarfile,xml.etree.ElementTree as ET
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'docs/repository-inventory-2026-09-28.json'
def main():
 names=[x for x in subprocess.check_output(['git','ls-files','-z'],cwd=ROOT).decode().split('\0') if x and x!=str(OUT.relative_to(ROOT))]
 rows=[];checks={}
 for name in names:
  p=ROOT/name
  assert p.is_file(),f'missing tracked file: {name}'
  b=p.read_bytes();kind='.tar.gz' if name.endswith('.tar.gz') else '.json.gz' if name.endswith('.json.gz') else p.suffix.lower() or '(none)'
  row={'path':name,'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'kind':kind}
  if kind=='.json':json.loads(b)
  elif kind=='.json.gz':json.loads(gzip.decompress(b))
  elif kind=='.svg':ET.fromstring(b)
  elif kind=='.py':compile(b,name,'exec')
  elif kind in {'.yml','.yaml'}:
   try:import yaml
   except ImportError:pass  # CI does not require PyYAML for the core repository checks
   else:yaml.safe_load(b)
  elif kind=='.tar.gz':
   with tarfile.open(fileobj=io.BytesIO(b),mode='r:gz') as t:row['archive_members']=len(t.getmembers())
  elif kind=='.csv':row['data_rows']=max(0,len(list(csv.reader(io.StringIO(b.decode('utf-8-sig')))))-1)
  checks[kind]=checks.get(kind,0)+1
  rows.append(row)
 manifest={'artifact':OUT.name,'control_date':'2026-09-28','basis':'tracked worktree after source-retirement and issue-1 fixes; inventory file excluded to avoid self-hash recursion','base_commit':subprocess.check_output(['git','rev-parse','origin/main'],cwd=ROOT).decode().strip(),'file_count':len(rows),'by_kind':checks,'scope':'identity and format checks only; no full semantic review of each file, external evidence or production assurance','files':rows}
 OUT.write_text(json.dumps(manifest,indent=2)+'\n')
 print(json.dumps({'file_count':len(rows),'by_kind':checks}))
if __name__=='__main__':main()
