#!/usr/bin/env python3
"""Generate AHTE/JAKIM/JSM process-flow SVG infographics from STANDARDS_FLOW_SPEC.json."""
from pathlib import Path
import json, html, re, textwrap

ROOT = Path(__file__).resolve().parents[1]
SPEC = ROOT / "master-standards-stack" / "process-flow-infographics" / "STANDARDS_FLOW_SPEC.json"
OUT = ROOT / "master-standards-stack" / "process-flow-infographics"
W,H=1800,1200

def esc(s): return html.escape(str(s))
def txt(x,y,s,size=20,weight=600,anchor="start",fill="#0f172a"):
    return f'<text x="{x}" y="{y}" font-family="Inter,Arial,sans-serif" font-size="{size}" font-weight="{weight}" text-anchor="{anchor}" fill="{fill}">{esc(s)}</text>'
def wrap(s,w): return textwrap.wrap(s,width=w,break_long_words=False)

def one_flow(item):
    num=item["flow"]; ms=item["standard"]; title=item["title"]; steps=item["steps"]
    p=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',
       '<rect width="1800" height="1200" fill="#f1f5f9"/>',
       '<rect x="40" y="32" width="1720" height="120" rx="28" fill="#0f172a"/>',
       txt(85,82,"AMANAH HALAL TRUST ECOSYSTEM",28,800,fill="#ffffff"),
       txt(85,120,f"{ms}  •  {title}",32,800,fill="#ffffff"),
       txt(1690,82,f"PROCESS FLOW {num}",18,700,"end","#cbd5e1"),
       txt(1690,110,"Implementation view",16,500,"end","#cbd5e1"),
       '<rect x="40" y="176" width="1720" height="930" rx="28" fill="#ffffff" stroke="#e2e8f0"/>',
       txt(78,220,"END-TO-END DIGITAL ASSURANCE FLOW",22,800),
       txt(78,250,"Scope → provenance → control → evidence → assessment → authority gate → trusted release",16,500,fill="#475569")]
    y0=285; boxw=1540; boxh=83; x=130; gap=24
    for i,step in enumerate(steps):
        y=y0+i*(boxh+gap)
        p += [f'<rect x="{x}" y="{y}" width="{boxw}" height="{boxh}" rx="18" fill="#'+('ffffff' if i%2==0 else 'f8fafc')+'" stroke="#cbd5e1" stroke-width="2"/>',
              f'<circle cx="{x+44}" cy="{y+41}" r="26" fill="#0f172a"/>',
              txt(x+44,y+48,str(i+1),18,800,"middle","#ffffff")]
        lines=wrap(step,105)[:2]
        for j,line in enumerate(lines): p.append(txt(x+88,y+34+j*22,line,20,650))
        if i<7:
            p += [f'<line x1="{x+boxw/2}" y1="{y+boxh}" x2="{x+boxw/2}" y2="{y+boxh+gap-7}" stroke="#64748b" stroke-width="4"/>',
                  f'<polygon points="{x+boxw/2-8},{y+boxh+gap-12} {x+boxw/2+8},{y+boxh+gap-12} {x+boxw/2},{y+boxh+gap}" fill="#64748b"/>']
    p += ['<rect x="82" y="1018" width="500" height="58" rx="15" fill="#ecfeff" stroke="#99f6e4"/>',
          txt(105,1055,"AHTE bindings: requirement • HCP • evidence • audit test",15,650),
          '<rect x="600" y="1018" width="500" height="58" rx="15" fill="#f8fafc" stroke="#cbd5e1"/>',
          txt(625,1055,"Authority gate + controlled release",15,650),
          '<rect x="1118" y="1018" width="600" height="58" rx="15" fill="#f8fafc" stroke="#cbd5e1"/>',
          txt(1140,1055,"Digital events + traceability preserve every state transition",15,650),
          '</svg>']
    return "\n".join(p)

def master(items):
    Wm,Hm=2200,1850
    p=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{Wm}" height="{Hm}" viewBox="0 0 {Wm} {Hm}">',
       f'<rect width="{Wm}" height="{Hm}" fill="#f1f5f9"/>',
       '<rect x="40" y="30" width="2120" height="125" rx="28" fill="#0f172a"/>',
       txt(80,78,"AMANAH HALAL TRUST ECOSYSTEM",32,800,fill="#ffffff"),
       txt(80,120,"JAKIM/JSM HALAL STANDARDS — COMPLETE PROCESS-FLOW INFOGRAPHIC ATLAS",27,800,fill="#ffffff"),
       txt(2115,78,"17 STANDARD FLOWS",17,700,"end","#cbd5e1"),
       txt(2115,108,"AHTE implementation view",15,500,"end","#cbd5e1"),
       '<rect x="40" y="180" width="2120" height="1600" rx="28" fill="#ffffff" stroke="#e2e8f0"/>',
       txt(75,225,"COMMON AHTE CONTROL SPINE",22,800),
       txt(75,252,"Authority → scope → requirement → HCP → evidence → assessment → corrective action → re-verification → authority gate → trust state",16,500,fill="#475569")]
    spine=["Authority","Scope","Requirement","HCP / Risk","Evidence","Audit","CAR / Re-verify","Authority gate","Trust / Release"]
    sx=75; sy=275; sbw=215; gap=12
    for i,st in enumerate(spine):
        x=sx+i*(sbw+gap)
        p += [f'<rect x="{x}" y="{sy}" width="{sbw}" height="55" rx="14" fill="#f8fafc" stroke="#cbd5e1"/>',txt(x+sbw/2,sy+35,st,14,700,"middle")]
        if i<8:
            p += [f'<line x1="{x+sbw}" y1="{sy+27}" x2="{x+sbw+gap-2}" y2="{sy+27}" stroke="#64748b" stroke-width="2"/>',
                  f'<polygon points="{x+sbw+gap-10},{sy+20} {x+sbw+gap-10},{sy+34} {x+sbw+gap},{sy+27}" fill="#64748b"/>']
    panel_w=670; panel_h=205; gx=25; gy=18; px0=75; py0=360
    for i,item in enumerate(items):
        r=i//3; c=i%3; x=px0+c*(panel_w+gx); y=py0+r*(panel_h+gy)
        p += [f'<rect x="{x}" y="{y}" width="{panel_w}" height="{panel_h}" rx="18" fill="#ffffff" stroke="#cbd5e1" stroke-width="2"/>',
              f'<rect x="{x}" y="{y}" width="68" height="48" rx="14" fill="#0f172a"/>',
              txt(x+34,y+31,item["flow"],16,800,"middle","#ffffff"),
              txt(x+86,y+26,item["standard"],18,800),
              txt(x+86,y+49,item["title"][:60],13,600,fill="#475569")]
        mini_w=147; mini_h=55; mg=8; mx=x+16; my=y+66
        for j,step in enumerate(item["steps"]):
            rr=j//4; cc=j%4; xx=mx+cc*(mini_w+mg); yy=my+rr*(mini_h+mg)
            p += [f'<rect x="{xx}" y="{yy}" width="{mini_w}" height="{mini_h}" rx="10" fill="#f8fafc" stroke="#e2e8f0"/>']
            lines=wrap(step,20)[:2]
            p.append(txt(xx+8,yy+19,f"{j+1}. {lines[0] if lines else step}",11,650))
            if len(lines)>1: p.append(txt(xx+8,yy+35,lines[1],10,500,fill="#334155"))
        p.append(txt(x+panel_w-16,y+191,f'AHTE FLOW {item["flow"]}',10,700,"end","#64748b"))
    fy=360+5*(panel_h+gy); fx=75
    p += [f'<rect x="{fx}" y="{fy}" width="{3*panel_w+2*gx}" height="{panel_h}" rx="18" fill="#f8fafc" stroke="#cbd5e1"/>',
          txt(fx+22,fy+34,"AHTE VISUAL DOCTRINE",18,800),
          txt(fx+22,fy+64,"The flow converts applicable standards into digital controls, HCPs, evidence, audit tests and traceable authority-gated outcomes.",14,550,fill="#334155"),
          txt(fx+22,fy+101,"Analytical execution",14,800),
          txt(fx+22,fy+127,"Laboratory, AI and operational outputs are bound to the evidence, audit and authority workflow.",13,550,fill="#334155"),
          txt(fx+22,fy+165,"Traceability",14,800),
          txt(fx+22,fy+191,"Events, provenance and state transitions are preserved across the AHTE trust graph.",13,550,fill="#334155"),
          '<rect x="75" y="1740" width="2050" height="16" rx="8" fill="#e2e8f0"/>',
          '<rect x="75" y="1740" width="1600" height="16" rx="8" fill="#0f172a"/>',
          txt(90,1810,"Implementation-oriented paraphrase; no copyrighted normative standard text is reproduced.",17,650),
          '</svg>']
    return "\n".join(p)

def main():
    items=json.loads(SPEC.read_text(encoding="utf-8"))
    OUT.mkdir(parents=True, exist_ok=True)
    for item in items:
        safe=re.sub(r"[^A-Za-z0-9]+","_",item["standard"])
        (OUT/f'{item["flow"]}_{safe}_PROCESS_FLOW.svg').write_text(one_flow(item),encoding="utf-8")
    (OUT/"00_AHTE_MASTER_JAKIM_MS_PROCESS_FLOW.svg").write_text(master(items),encoding="utf-8")
    print(f"generated {len(items)+1} SVG files")

if __name__=="__main__": main()
