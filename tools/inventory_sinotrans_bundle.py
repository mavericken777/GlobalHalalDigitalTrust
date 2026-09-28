"""Inventory a private Sinotrans playbook ZIP for provenance; never publish PDF bytes."""
from __future__ import annotations
from pathlib import Path
import hashlib,io,json,sys,zipfile
import xml.etree.ElementTree as ET
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'master-standards-stack/source-sinotrans-bundle-2026-09-28.json'
def digest(b):return hashlib.sha256(b).hexdigest()
def main(path):
 import fitz
 from PIL import Image
 b=path.read_bytes();z=zipfile.ZipFile(io.BytesIO(b));assert z.testzip() is None
 files=[i for i in z.infolist() if not i.is_dir()]
 assert len(files)==len({i.filename for i in files})==15
 assert all(not i.filename.startswith('/') and '..' not in Path(i.filename).parts for i in files)
 rows=[]
 for i in files:
  data=z.read(i);ext=Path(i.filename).suffix.lower();row={'path':i.filename,'bytes':len(data),'sha256':digest(data),'kind':ext}
  if ext=='.pdf':row['pdf_pages']=len(fitz.open(stream=data,filetype='pdf'))
  elif ext=='.svg':ET.fromstring(data)
  elif ext=='.png':
   with Image.open(io.BytesIO(data)) as im:im.verify()
  rows.append(row)
 assert [sum(x['kind']==kind for x in rows) for kind in ('.pdf','.svg','.png')]==[1,7,7]
 result={'artifact':OUT.name,'control_date':'2026-09-28','bundle':'MS2400_Sinotrans_Playbook_Bundle.zip','sha256':digest(b),'archive_integrity':'ZIP_CRC_PASS','ingestion_status':'BLOCKED_SOURCE_CONFLICT','repository_copy':False,'member_count':len(rows),'members':sorted(rows,key=lambda x:x['path'])}
 OUT.write_text(json.dumps(result,indent=2)+'\n')
 print(json.dumps({'count':len(rows),'pdf_pages':next(x['pdf_pages'] for x in rows if x['kind']=='.pdf'),'sha256':digest(b)}))
if __name__=='__main__':main(Path(sys.argv[1]))
