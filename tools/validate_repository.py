"""Validate active repository structure and machine-readable project artifacts.

Historical source snapshots are not required project inputs. This validator checks only current files and formats.
"""
from pathlib import Path
import json
import subprocess
import sys
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]

def validate():
    files = subprocess.check_output(["git", "ls-files", "-z"], cwd=ROOT).decode().split("\0")
    counts = {"json": 0, "svg": 0}
    missing = []
    for name in filter(None, files):
        path = ROOT / name
        if not path.is_file():
            missing.append(name)
            continue
        if name.endswith(".json"):
            json.loads(path.read_text(encoding="utf-8"))
            counts["json"] += 1
        elif name.endswith(".svg"):
            ET.parse(path)
            counts["svg"] += 1
    if missing:
        raise AssertionError("tracked paths missing from working tree: " + ", ".join(missing))
    register = ROOT / "master-standards-stack/iq300-all-jakim-ms/01_MASTER_STANDARDS_REGISTER.md"
    assert register.is_file(), "current standards register is missing"
    print(json.dumps({"structure": "PASS", "artifacts": counts, "current_register": register.relative_to(ROOT).as_posix()}))

if __name__ == "__main__":
    validate()
