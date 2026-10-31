#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Nhung mot file ky vao dashboard/index.html -> ban MOT FILE gui duoc.

Trang doc khoi <script id="pd-data"> TRUOC data/index.json, nen ban nhung
⛔ khong can may chu tinh (pd-D §6).

    python tools/gui-dashboard.py out/bao-cao-insight.json
    -> out/dashboard-insight-<ky>.html

⚠ File qc-* ⛔ KHONG publish ra link cong khai. Script nhac lai dieu do.
"""
import io
import os
import re
import sys
import json

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

GOC = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

if len(sys.argv) < 2:
    print(__doc__)
    sys.exit(1)

nguon = sys.argv[1]
with io.open(nguon, encoding="utf-8") as f:
    data = json.load(f)

trang = os.path.join(GOC, "dashboard", "index.html")
with io.open(trang, encoding="utf-8") as f:
    html = f.read()

# </script> trong du lieu se dong som the <script> -> phai cat chuoi
js = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
moi, n = re.subn(r'(<script type="application/json" id="pd-data">).*?(</script>)',
                 lambda m: m.group(1) + js + m.group(2), html, count=1, flags=re.S)
if not n:
    print("⛔ ⛔ Khong tim thay o <script id=\"pd-data\"> trong dashboard/index.html")
    sys.exit(1)

bo_cuc = data.get("bo_cuc", "insight")
ky = re.sub(r"[^0-9A-Za-z]+", "-", data.get("ky", "ky")).strip("-")
ra = os.path.join(GOC, "out", "dashboard-%s-%s.html" % (bo_cuc, ky))
with io.open(ra, "w", encoding="utf-8", newline="\n") as f:
    f.write(moi)

print("→ %s  (%.0f KB)" % (os.path.relpath(ra, GOC), os.path.getsize(ra) / 1024.0))
if bo_cuc == "qc":
    print("\n⚠ Day la ban LUONG Q — co ten nhan vien.")
    print("⛔ KHONG publish ra link cong khai. Gui file, cho dung truong nhom (pd-D §6).")
else:
    print("\n⚠ Ban nay chua loi khach (da an danh) va ket luan noi bo.")
    print("Artifact mac dinh RIENG TU — chuyen sang \"ai co link deu mo duoc\" thi")
    print("⛔ dung dan link vao repo public.")
