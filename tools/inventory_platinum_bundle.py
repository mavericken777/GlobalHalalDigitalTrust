"""Inventory the user-held bundle without copying its licensed/source-derived bytes to Git."""
from __future__ import annotations
import hashlib,io,json,sys,zipfile
from pathlib import Path
import xml.etree.ElementTree as ET

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'master-standards-stack/source-bundle-holdings-2026-09-28.json'
def sha(b):return hashlib.sha256(b).hexdigest()
def main(source:Path):
 import fitz
 b=source.read_bytes(); z=zipfile.ZipFile(io.BytesIO(b)); assert z.testzip() is None
 infos=[x for x in z.infolist() if not x.is_dir()]
 assert len(infos)==len({x.filename for x in infos}), 'duplicate ZIP member names'
 assert all(not x.filename.startswith('/') and '..' not in Path(x.filename).parts for x in infos), 'unsafe member path'
 files=[]
 for item in infos:
  data=z.read(item);kind=Path(item.filename).suffix.lower();row={'path':item.filename,'bytes':len(data),'sha256':sha(data),'kind':kind}
  if kind=='.pdf':row['pdf_pages']=len(fitz.open(stream=data,filetype='pdf'))
  if kind=='.svg':ET.fromstring(data)
  files.append(row)
 assert sum(x['kind']=='.pdf' for x in files)==8
 assert sum(x['kind']=='.svg' for x in files)==30
 assert sum(x['kind']=='.png' for x in files)==30
 assert sum(x['kind']=='.html' for x in files)==0
 manifest={'artifact':OUT.name,'control_date':'2026-09-28','bundle':'Platinum_Tier_v2_Complete_Bundle.zip','bundle_sha256':sha(b),'integrity':'ZIP_CRC_PASS','declared_file_count_in_index':80,'actual_file_count':len(files),'missing_declared_html_sources':12,'classification':'SECONDARY_COMPILATION_SOURCE_HELD_NOT_NORMATIVE','repository_copy':False,'members':sorted(files,key=lambda x:x['path'])}
 OUT.write_text(json.dumps(manifest,indent=2,ensure_ascii=False)+'\n')
 print(json.dumps({'members':len(files),'pdfs':8,'svg':30,'png':30,'html':0,'sha256':sha(b)}))
if __name__=='__main__':main(Path(sys.argv[1]))
