#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Đếm ký tự SYSTEM-PROMPT-NGAN.md — ô Instructions của ChatGPT giới hạn 8.000."""
import io, os, sys

# Console Windows mac dinh cp1252 -> tieng Viet no. Ep UTF-8 truoc khi in.
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

GIOI_HAN = 8000
goc = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def dem(ten):
    p = os.path.join(goc, ten)
    with io.open(p, encoding="utf-8") as f:
        s = f.read()
    return len(s), s.count("\n") + 1

n, d = dem("SYSTEM-PROMPT-NGAN.md")
N, D = dem("SYSTEM-PROMPT.md")

print("SYSTEM-PROMPT.md      : {:>6,} ký tự · {} dòng".format(N, D))
print("SYSTEM-PROMPT-NGAN.md : {:>6,} ký tự · {} dòng".format(n, d))
print("-" * 46)
if n <= GIOI_HAN:
    print("OK — còn {:,} ký tự trong giới hạn {:,}".format(GIOI_HAN - n, GIOI_HAN))
    sys.exit(0)
print("VUOT {:,} ky tu so voi gioi han {:,}".format(n - GIOI_HAN, GIOI_HAN))
sys.exit(1)
