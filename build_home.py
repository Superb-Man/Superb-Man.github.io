#!/usr/bin/env python3
"""Assemble index.html from independently editable HTML partials. No dependencies."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent
TEMPLATE = (ROOT / "index.template.html").read_text(encoding="utf-8")

def include(match):
    relative_path = match.group(1)
    target = (ROOT / relative_path).resolve()
    if not target.is_relative_to(ROOT):
        raise ValueError("Include must remain inside the project")
    return target.read_text(encoding="utf-8").rstrip()

output = re.sub(r"<!-- @include (partials/[a-z-]+\.html) -->", include, TEMPLATE)
(ROOT / "index.html").write_text(output + "\n", encoding="utf-8")
print("Generated index.html from partials")
