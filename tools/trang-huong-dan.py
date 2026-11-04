# -*- coding: utf-8 -*-
"""Sinh trang huong dan cai dat Insight Dashboard Paris.

Doc thang file trong repo nen moi nut Copy luon khop file nguon.
Khuon trang lay theo trang mau cua bo tai lieu huong dan agent;
bang mau + phong giu rieng cua Nha khoa Paris.
"""
import io, json, html, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "huong-dan.html")
REPO = u"https://github.com/huudinh/Agent-InsightDashboard-Paris"
ZIP = REPO + u"/archive/refs/heads/main.zip"
NL = chr(10)
TICK = chr(96) * 3

sys.path.insert(0, HERE)
from trang_css import CSS


def doc(p):
    return io.open(os.path.join(ROOT, p), encoding="utf-8").read()


def so(n):
    """12345 -> 12.345"""
    s = str(n)
    r = u""
    while len(s) > 3:
        r = u"." + s[-3:] + r
        s = s[:-3]
    return s + r


def khoi(txt):
    """Lay khoi ``` dau tien trong file prompt; khong co thi tra ca file."""
    i = txt.find(TICK)
    if i < 0:
        return txt.strip()
    i = txt.find(NL, i)
    j = txt.find(TICK, i)
    if i < 0 or j < 0:
        return txt.strip()
    return txt[i + 1:j].rstrip()


P = {}  # payload

# ─── the bo nao ──────────────────────────────────────────────
P[u"brain"] = doc(u"SYSTEM-PROMPT.md")
P[u"ngan"] = doc(u"SYSTEM-PROMPT-NGAN.md")
P[u"clone"] = u"git clone " + REPO + u".git"

# ─── ten / mo ta / cau mo dau ────────────────────────────────
P[u"m_ten"] = u"Insight Dashboard Paris"
P[u"m_mota"] = (
    u"Agent \u0111\u1ecdc h\u1ed9i tho\u1ea1i chat c\u1ee7a kh\u00e1ch Nha khoa Paris. "
    u"\u0110\u1ecdc \u0111\u00fang m\u1ed9t l\u1ea7n, r\u1ed3i t\u1eeb c\u00f9ng m\u1ed9t l\u1ea7n \u0111\u1ecdc sinh ra hai b\u1ed9 "
    u"\u0111\u1ea7u ra t\u00e1ch r\u1eddi nhau: lu\u1ed3ng I n\u00f3i v\u1ec1 kh\u00e1ch (ch\u00e2n dung c\u1ee7a k\u1ef3, r\u00e0o c\u1ea3n "
    u"S\u1ee2/NG\u1edc/NG\u1ea0I, c\u00e2u h\u1ecfi ng\u1ea7m, ma tr\u1eadn \u01b0u ti\u00ean, ng\u00e2n h\u00e0ng hook, s\u1ed1 ads) "
    u"v\u00e0 lu\u1ed3ng Q n\u00f3i v\u1ec1 ng\u01b0\u1eddi tr\u1ef1c page (10 ti\u00eau ch\u00ed TC, \u0111i\u1ec3m thang 10, 11 c\u1edd \u0111\u1ecf "
    u"ph\u00e1p ch\u1ebf, s\u1ed5 tay t\u1eebng ng\u01b0\u1ed1i). Gi\u1eefa hai lu\u1ed3ng c\u00f3 t\u01b0\u1eddng ng\u0103n: kh\u00f4ng file n\u00e0o "
    u"ch\u1ee9a c\u1ea3 t\u00ean nh\u00e2n vi\u00ean l\u1eabn l\u1eddi kh\u00e1ch. An to\u00e0n tr\u01b0\u1edbc b\u00e1n h\u00e0ng, "
    u"v\u00e0 b\u1ec7nh s\u1eed kh\u00e1ch l\u00e0 d\u1eef li\u1ec7u s\u1ee9c kho\u1ebb \u2014 ch\u1ec9 l\u01b0u nh\u00e3n."
)
P[u"m_st1"] = u"\u0110\u1eccC h\u1ed9i tho\u1ea1i k\u1ef3 01\u201315/11. \u0110\u00ednh k\u00e8m hoi-thoai.md + ads-facebook.csv."
P[u"m_st2"] = u"INSIGHT k\u1ef3 01\u201315/11. Ch\u1eb7ng 1 \u2014 ph\u00e1c h\u1ecda ch\u00e2n dung r\u1ed3i d\u1eebng \u1edf C\u1ed4NG 0."
P[u"m_st3"] = u"QC k\u1ef3 01\u201315/11. Ch\u1ea5m 10 ti\u00eau ch\u00ed r\u1ed3i d\u1eebng \u1edf C\u1ed4NG 2."

# ─── 19 file tri thuc ────────────────────────────────────────
NHOM_LOI = u"L\u00f5i \u2014 \u0111\u1ecdc m\u1ed9t l\u1ea7n"
NHOM_I = u"Lu\u1ed3ng I \u2014 v\u1ec1 kh\u00e1ch"
NHOM_Q = u"Lu\u1ed3ng Q \u2014 v\u1ec1 ng\u01b0\u1eddi tr\u1ef1c page"
NHOM_C = u"Chung"
NHOM_P = u"6 prompt \u2014 n\u1ea1p k\u00e8m \u0111\u1ec3 agent bi\u1ebft khu\u00f4n \u0111\u1ea7u ra"

FILES = [
 (NHOM_LOI, u"knowledge/pd-A-vai-tro-hai-luong.md", u"\u2605 l\u00f5i", 1,
  u"<b>Vai tr\u00f2 &amp; quy tr\u00ecnh</b> \u2014 hai lu\u1ed3ng \u00b7 b\u1ed1n c\u1ed5ng ch\u1eb7n \u00b7 b\u1ed9 m\u00e3 d\u00f9ng chung \u00b7 "
  u"\u2605 lu\u1eadt <b>m\u1ed9t quy\u1ebft \u0111\u1ecbnh \u2014 m\u1ed9t s\u1ed5</b>"),
 (NHOM_LOI, u"knowledge/pd-B-doc-dau-vao.md", u"", 0,
  u"<b>Khu\u00f4n \u0111\u1ea7u v\u00e0o</b> \u00b7 \u26d4 \u1ea9n danh 8 th\u1ee9 \u00b7 ki\u1ec3m m\u1eabu 4 c\u00e2u \u00b7 "
  u"\u2605\u2605 <b>d\u1eef li\u1ec7u s\u1ee9c kho\u1ebb</b> \u00a73b \u2014 Lu\u1eadt 91/2025/QH15"),
 (NHOM_LOI, u"knowledge/pd-C-bang-du-kien-goc.md", u"", 0,
  u"<b>B\u1ea3ng d\u1eef ki\u1ec7n g\u1ed1c</b> \u2014 lu\u1eadt m\u1ed9t l\u1ea7n \u0111\u1ecdc \u00b7 3 lu\u1eadt ghi \u0111\u00e8 \u0111\u1ed9 n\u00f3ng"),
 (NHOM_I, u"knowledge/pd-I1-chan-dung-cong-0.md", u"\u2605", 1,
  u"<b>Ch\u00e2n dung c\u1ee7a k\u1ef3</b> \u00b7 C\u1ed4NG 0 \u00b7 \u26d4 v\u00ec sao kh\u00f4ng d\u00f9ng <code>N1\u2026N6</code> l\u00e0m ch\u00e2n dung"),
 (NHOM_I, u"knowledge/pd-I2-dao-sau-insight.md", u"", 0,
  u"<b>C\u00e2u h\u1ecfi ng\u1ea7m</b> \u00b7 3 r\u00e0o c\u1ea3n S\u1ee2/NG\u1edc/NG\u1ea0I \u00b7 \u2605 lu\u1eadt ch\u1ed1ng l\u1eb7p v\u00f2ng <code>% HOT*</code>"),
 (NHOM_I, u"knowledge/pd-I3-ads-phe-u-nha-khoa.md", u"", 0,
  u"<b>Ph\u1ebfu nha khoa c\u00f3 b\u01b0\u1edbc \u201c\u0111\u1ebfn kh\u00e1m\u201d</b> \u00b7 \u2605 b\u1ea3ng <b>post h\u1ee9a g\u00ec \u2194 kh\u00e1ch h\u1ecfi g\u00ec</b>"),
 (NHOM_I, u"knowledge/pd-I4-ma-tran-hook.md", u"\u2605", 1,
  u"<b>Ma tr\u1eadn \u0111\u1ed9 n\u00f3ng \u00d7 V1/V2/V3</b> \u00b7 C\u1ed4NG 1 \u00b7 khu\u00f4n hook ba nh\u1ecbp \u00b7 c\u1edd ph\u00e1p ch\u1ebf"),
 (NHOM_Q, u"knowledge/pd-Q1-cham-diem-truc-page.md", u"\u2605\u2605 l\u00f5i", 1,
  u"<b>10 ti\u00eau ch\u00ed <code>TC-1\u2026TC-10</code></b> \u00b7 b\u1ea3ng tra l\u1ed7i h\u1ec7 \u00b7 "
  u"\u2605 <b>4 r\u00e0o an to\u00e0n</b> \u2014 b\u1ecf m\u1ed9t c\u00e1i l\u00e0 s\u1ed5 n\u00e0y th\u00e0nh c\u00f4ng c\u1ee5 k\u1ef7 lu\u1eadt"),
 (NHOM_Q, u"knowledge/pd-Q2-co-do-phap-che.md", u"", 0,
  u"<b>11 c\u1edd \u0111\u1ecf <code>C\u0110-P1\u2026C\u0110-P11</code></b> \u00b7 C\u1ed4NG 2 \u00b7 \u2605 c\u1ee5m <b>mi\u1ec5n tr\u1eeb</b> \u2014 "
  u"\u26d4 \u0111\u1eebng g\u1eafn c\u1edd cho ng\u01b0\u1eddi l\u00e0m \u0111\u00fang"),
 (NHOM_Q, u"knowledge/pd-Q3-so-tay-thuc-thi.md", u"", 0,
  u"<b>3 lo\u1ea1i s\u1ed5 tay</b> <code>ST-CN</code>/<code>ST-TN</code>/<code>ST-HT</code> \u00b7 "
  u"\u2605 ph\u1ea7n <b>\u201cvi\u1ec7c kh\u00f4ng ph\u1ea3i c\u1ee7a b\u1ea1n\u201d</b>"),
 (NHOM_C, u"knowledge/pd-D-dashboard-schema.md", u"", 0,
  u"<b>Hai schema \u00b7 hai file</b> \u00b7 ba quy t\u1eafc hi\u1ec3n th\u1ecb \u00b7 \u26d4 file QC kh\u00f4ng publish ra link"),
 (NHOM_C, u"knowledge/pd-E-module-paris.md", u"\u2605\u2605 l\u00f5i", 1,
  u"<b>Module th\u01b0\u01a1ng hi\u1ec7u Paris</b> \u2014 7 slot d\u1eef ki\u1ec7n ch\u01b0a c\u1ea5p \u00b7 "
  u"\u2605\u2605 <b>an to\u00e0n tr\u01b0\u1edbc b\u00e1n h\u00e0ng</b> \u00a73b \u00b7 \u0111\u1ed5i th\u01b0\u01a1ng hi\u1ec7u th\u00ec thay \u0111\u00fang s\u1ed5 n\u00e0y"),
 (NHOM_C, u"knowledge/pd-F-tuong-ngan-hai-luong.md", u"\u2605\u2605 l\u00f5i", 1,
  u"<b>T\u01b0\u1eddng ng\u0103n</b> \u2014 c\u00e1i g\u00ec \u0111i qua \u0111\u01b0\u1ee3c, c\u00e1i g\u00ec kh\u00f4ng \u00b7 C\u1ed4NG T \u00b7 "
  u"\u2605 c\u00e1ch vi\u1ebft \u0111\u00fang khi lu\u1ed3ng I ph\u1ea3i n\u00f3i v\u1ec1 ch\u1ea5t l\u01b0\u1ee3ng t\u01b0 v\u1ea5n"),
 (NHOM_P, u"prompts/prompt-doc.md", u"", 0,
  u"L\u1ec7nh <code>\u0110\u1eccC</code> \u2014 b\u01b0\u1edbc duy nh\u1ea5t \u0111\u1ecdc h\u1ed9i tho\u1ea1i"),
 (NHOM_P, u"prompts/prompt-insight.md", u"", 0,
  u"L\u1ec7nh <code>INSIGHT</code> \u2014 ch\u00e2n dung \u2192 C\u1ed4NG 0 \u2192 ma tr\u1eadn \u2192 C\u1ed4NG 1"),
 (NHOM_P, u"prompts/prompt-qc.md", u"", 0,
  u"L\u1ec7nh <code>QC</code> \u2014 10 ti\u00eau ch\u00ed \u00b7 11 c\u1edd \u0111\u1ecf \u2192 C\u1ed4NG 2"),
 (NHOM_P, u"prompts/prompt-so-tay.md", u"", 0,
  u"Sinh ba lo\u1ea1i s\u1ed5 tay \u2014 <code>ST-CN</code> s\u00e1u ph\u1ea7n"),
 (NHOM_P, u"prompts/prompt-hook.md", u"", 0,
  u"Ng\u00e2n h\u00e0ng hook \u2014 ch\u1ec9 d\u00f9ng sau khi ma tr\u1eadn \u0111\u00e3 duy\u1ec7t"),
 (NHOM_P, u"prompts/prompt-tuong-ngan.md", u"\u2605", 1,
  u"<code>C\u1ed4NG T</code> \u2014 s\u00e1u c\u00e2u ki\u1ec3m t\u01b0\u1eddng ng\u0103n tr\u01b0\u1edbc khi xu\u1ea5t file"),
]

for i, (nh, path, badge, hi, how) in enumerate(FILES):
    P[u"f%d" % (i + 1)] = doc(path)

# ─── prompt cards ────────────────────────────────────────────
G_LENH = u"lenh"
G_DOC = u"doc"
G_I = u"khach"
G_Q = u"nguoi"
G_T = u"tuong"

CARDS = [
 (G_LENH, u"\u0110\u1eccC \u2014 g\u00f5 m\u1ed9t c\u00e2u", u"chu\u1ea9n",
  u"\u0110\u1eccC h\u1ed9i tho\u1ea1i k\u1ef3 01\u201315/11." + NL +
  u"<\u0111\u00ednh k\u00e8m du-lieu/hoi-thoai.md>"),
 (G_LENH, u"\u0110\u1eccC \u2014 c\u00f3 b\u1ed1i c\u1ea3nh, t\u1ed1t h\u01a1n", u"\u2605 hay g\u1eb7p",
  u"\u0110\u1eccC h\u1ed9i tho\u1ea1i k\u1ef3 01\u201315/11." + NL + NL +
  u"\u0110\u00ednh k\u00e8m:" + NL +
  u" \u00b7 180 h\u1ed9i tho\u1ea1i inbox Facebook" + NL +
  u" \u00b7 s\u1ed1 ads Facebook c\u00f9ng k\u1ef3" + NL +
  u" \u00b7 b\u1ea3n xu\u1ea5t C\u00d3 ph\u1ea7n ghi ch\u00fa b\u00e0n giao" + NL + NL +
  u"In 4 c\u00e2u ki\u1ec3m m\u1eabu TR\u01af\u1edaC khi \u0111\u1ecdc, r\u1ed3i d\u1eebng cho t\u00f4i xem." + NL +
  u"\u26a0 N\u00f3i th\u1eadt n\u1ebfu m\u1eabu c\u00f3 d\u1ea5u hi\u1ec7u \u0110\u00c3 B\u1eca L\u1eccC."),
 (G_LENH, u"ADS \u2014 s\u1ed1 qu\u1ea3ng c\u00e1o c\u1ee7a k\u1ef3", u"",
  u"ADS k\u1ef3 01\u201315/11." + NL +
  u"<\u0111\u00ednh k\u00e8m du-lieu/ads-facebook.csv>" + NL + NL +
  u"\u26a0 Ph\u1ec5u PH\u1ea2I c\u00f3 c\u1ed9t \u201c\u0111\u1ebfn kh\u00e1m\u201d." + NL +
  u"\u26d4 KH\u00d4NG l\u1ea5y \u201c\u0111\u1eb7t l\u1ecbch\u201d thay cho \u201c\u0111\u1ebfn kh\u00e1m\u201d \u2014 ch\u01b0a \u0111o \u0111\u01b0\u1ee3c th\u00ec" + NL +
  u"  ghi \u201c\u26a0 ch\u01b0a \u0111o \u0111\u01b0\u1ee3c show-up\u201d v\u00e0 \u0111\u1ec3 tr\u1ed1ng."),
 (G_LENH, u"C\u1ed4NG 0 \u2014 duy\u1ec7t ch\u00e2n dung", u"sau ch\u1eb7ng 1",
  u"DUY\u1ec6T CH\u00c2N DUNG" + NL + NL +
  u"ho\u1eb7c:" + NL +
  u"S\u1eecA CD3 \u2014 t\u00e1ch ri\u00eang nh\u00f3m \u0111\u00e3 kh\u00e1m n\u01a1i kh\u00e1c v\u00e0 c\u00f3 b\u00e1o gi\u00e1" + NL +
  u"G\u1ed8P CD5 v\u00e0o CD2 \u2014 c\u00f9ng m\u1ed9t n\u1ed7i s\u1ee3" + NL +
  u"T\u00c1CH CD1 \u2014 l\u00e0m l\u1ea1i ca l\u1ed7i \u1edf n\u01a1i kh\u00e1c \u2260 l\u00e0m l\u1ea1i t\u1ea1i Paris"),
 (G_LENH, u"C\u1ed4NG 1 \u2014 duy\u1ec7t ma tr\u1eadn \u01b0u ti\u00ean", u"sau ch\u1eb7ng 2",
  u"DUY\u1ec6T" + NL + NL +
  u"ho\u1eb7c:" + NL +
  u"B\u1ece 4 \u2014 k\u1ef3 n\u00e0y kh\u1ed1i kh\u00f4ng l\u00e0m" + NL +
  u"CH\u1eC8 L\u00c0M 1, 2, 5" + NL +
  u"\u0110\u1ed4I TH\u1ee8 T\u1ef0 \u2014 \u0111\u01b0a vi\u1ec7c c\u1ee7a V1 l\u00ean tr\u01b0\u1edbc"),
 (G_LENH, u"C\u1ed4NG 2 \u2014 duy\u1ec7t ph\u00e1p ch\u1ebf", u"tr\u01b0\u1edbc khi ph\u00e1t s\u1ed5 tay",
  u"DUY\u1ec6T PH\u00c1P CH\u1ebe" + NL + NL +
  u"ho\u1eb7c:" + NL +
  u"\u0110\u00c3 G\u1ee0 C\u0110-P2, C\u0110-P8" + NL +
  u"CH\u1edc C\u0110-P11 \u2014 \u0111\u1ee3i danh s\u00e1ch \u1ea3nh c\u00f3 gi\u1ea5y \u0111\u1ed3ng \u00fd"),
 (G_DOC, u"prompts/prompt-doc.md", u"m\u1ed9t l\u1ea7n \u0111\u1ecdc", khoi(P[u"f14"])),
 (G_I, u"prompts/prompt-insight.md", u"\u2605 lu\u1ed3ng I", khoi(P[u"f15"])),
 (G_I, u"prompts/prompt-hook.md", u"sau C\u1ed4NG 1", khoi(P[u"f18"])),
 (G_Q, u"prompts/prompt-qc.md", u"\u2605 lu\u1ed3ng Q", khoi(P[u"f16"])),
 (G_Q, u"prompts/prompt-so-tay.md", u"sau C\u1ed4NG 2", khoi(P[u"f17"])),
 (G_T, u"prompts/prompt-tuong-ngan.md", u"\u2605\u2605 b\u1eaft bu\u1ed9c", khoi(P[u"f19"])),
]
for i, (g, t, k, body) in enumerate(CARDS):
    P[u"p%d" % (i + 1)] = body

# ─── khoi ma le ──────────────────────────────────────────────
P[u"cli"] = (
 u'python tools/pd.py doc     du-lieu/hoi-thoai.md --ky "01-15/11"' + NL +
 u'python tools/pd.py ads     du-lieu/ads-facebook.csv --ky "01-15/11"' + NL +
 u'python tools/pd.py insight --ky "01-15/11"' + NL +
 u'python tools/pd.py qc      --ky "01-15/11"' + NL +
 u'python tools/pd.py kiem    out/bao-cao-insight.json     # C\u1ed4NG T' + NL +
 u'python tools/gui-dashboard.py out/bao-cao-insight.json  # b\u1ea3n 1 file g\u1eedi \u0111\u01b0\u1ee3c')
P[u"thu"] = (
 u'python tools/pd.py doc     template/MAU_hoi-thoai.md --ky "03-16/11"' + NL +
 u'python tools/pd.py ads     template/MAU_ads-facebook.csv --ky "03-16/11"' + NL +
 u'python tools/pd.py insight --ky "03-16/11"' + NL +
 u'python tools/pd.py qc      --ky "03-16/11"')
P[u"du_cay"] = (
 u"du-lieu/" + NL +
 u"\u251c\u2500\u2500 hoi-thoai.md         \u2460 b\u1eaft bu\u1ed9c \u2014 khu\u00f4n \u1edf pd-B \u00a72" + NL +
 u"\u251c\u2500\u2500 ads-facebook.csv     \u2461 n\u00ean c\u00f3   \u2014 c\u1ed9t \u1edf pd-B \u00a75" + NL +
 u"\u2514\u2500\u2500 danh-sach-post.csv   \u2462 tu\u1ef3")
P[u"du_khuon"] = (
 u"## <STT>. <T\u00ean KH> \u2014 <DD/MM HH:MM>" + NL +
 u"- Ph\u1ee5 tr\u00e1ch: <t\u00ean NV> \u00b7 C\u00f3 S\u0110T: <C\u00f3|Kh\u00f4ng> \u00b7 S\u1ed1 tin: <n>" + NL +
 u"- **<DD/MM HH:MM> KH:** <n\u1ed9i dung kh\u00e1ch>" + NL +
 u"- **<DD/MM HH:MM> NV (<t\u00ean NV>):** <n\u1ed9i dung nh\u00e2n vi\u00ean>")
P[u"du_the"] = (
 u"- **03/11 09:12 KH:** [Th\u1ebb: Inbox t\u1eeb qu\u1ea3ng c\u00e1o QC_Implant_Straumann \u2013" + NL +
 u"  Tr\u1ed3ng r\u0103ng Implant tr\u1ee5 Straumann, \u0103n nhai nh\u01b0 r\u0103ng th\u1eadt]")
P[u"andanh"] = (
 u"t\u00ean th\u1eadt kh\u00e1ch \u00b7 s\u1ed1 \u0111i\u1ec7n tho\u1ea1i \u00b7 \u1ea3nh kh\u00e1ch \u00b7 email \u00b7 \u0111\u1ecba ch\u1ec9 nh\u00e0" + NL +
 u"link Facebook c\u00e1 nh\u00e2n \u00b7 m\u00e3 \u0111\u01a1n/h\u1ed3 s\u01a1 \u00b7 t\u00ean ng\u01b0\u1eddi nh\u00e0 kh\u00e1ch nh\u1eafc t\u1edbi")

# ════════════════════════════════════════════════════════════
# HTML
# ════════════════════════════════════════════════════════════
o = []
A = o.append

A(u'<!doctype html><html lang="vi"><head><meta charset="utf-8">')
A(u'<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">')
A(u'<title>Insight Dashboard Paris \u2014 c\u00e0i \u0111\u1eb7t</title>')
A(u'<link rel="preconnect" href="https://fonts.googleapis.com">')
A(u'<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>')
A(u'<link rel="stylesheet" href="https://fonts.googleapis.com/css2?'
  u'family=Be+Vietnam+Pro:wght@400;500;600;700;800&'
  u'family=Bricolage+Grotesque:opsz,wght@12..96,600;12..96,700;12..96,800&display=swap">')
A(u"<style>" + CSS + u"</style></head><body>")

# ─── header ──────────────────────────────────────────────────
A(u'''
<header class="top">
  <div class="wrap" style="padding-block:42px 36px">
    <p class="eyebrow">Nha khoa Paris \u00b7 nhakhoaparis.vn \u00b7 h\u01b0\u1edbng d\u1eabn c\u00e0i \u0111\u1eb7t &amp; prompt m\u1eabu</p>
    <h1>Insight Dashboard Paris</h1>
    <p class="lede">\u0110\u1ecdc h\u1ed9i tho\u1ea1i chat c\u1ee7a kh\u00e1ch \u0111\u01b0\u1ee3c nh\u1eadp v\u00e0o, \u0111\u1ecdc <b>\u0111\u00fang m\u1ed9t l\u1ea7n</b>,
      r\u1ed3i t\u1eeb c\u00f9ng m\u1ed9t l\u1ea7n \u0111\u1ecdc sinh ra <b>hai b\u1ed9 \u0111\u1ea7u ra t\u00e1ch r\u1eddi nhau</b>:
      m\u1ed9t b\u1ed9 n\u00f3i v\u1ec1 <b>kh\u00e1ch</b>, m\u1ed9t b\u1ed9 n\u00f3i v\u1ec1 <b>ng\u01b0\u1eddi tr\u1ef1c page</b>.</p>
    <p class="quick">G\u00f5 <b>\u0110\u1eccC</b> k\u00e8m file h\u1ed9i tho\u1ea1i &rarr; agent d\u1ef1ng b\u1ea3ng d\u1eef ki\u1ec7n g\u1ed1c.
      Sau \u0111\u00f3 <b>INSIGHT</b> v\u00e0 <b>QC</b> ch\u1ea1y <b>\u0111\u1ed9c l\u1eadp</b> \u2014 c\u1ea3 hai \u0111\u1ecdc l\u1ea1i t\u1eeb c\u00f9ng m\u1ed9t b\u1ea3ng
      n\u00ean \u26d4 kh\u00f4ng bao gi\u1edd l\u1ec7ch s\u1ed1.</p>
    <div class="chips"><span class="chip on">v1.1</span><span class="chip">13 s\u1ed5 tri th\u1ee9c</span><span class="chip">6 prompt</span><span class="chip">4 l\u1ec7nh</span><span class="chip">4 c\u1ed5ng ch\u1eb7n</span><span class="chip">10 c\u00e2u ki\u1ec3m</span><span class="chip">an to\u00e0n tr\u01b0\u1edbc b\u00e1n h\u00e0ng</span></div>
    <p class="dim" style="margin-top:18px">Lu\u1eadt t\u1ed1i th\u01b0\u1ee3ng: <b>kh\u00f4ng file n\u00e0o ch\u1ee9a c\u1ea3 t\u00ean nh\u00e2n vi\u00ean l\u1eabn l\u1eddi kh\u00e1ch</b>
      \u2014 v\u00e0 \u0111\u00f3 l\u00e0 l\u00fd do repo n\u00e0y t\u1ed3n t\u1ea1i \u00b7
      <a href="REPO" target="_blank" rel="noopener">repo tr\u00ean GitHub</a></p>
  </div>
</header>

<nav class="bar">
  <div class="wrap"><a href="#m1">1 &middot; C\u00e0i \u0111\u1eb7t</a><a href="#m2">2 &middot; B\u1ed1n l\u1ec7nh &amp; prompt</a><a href="#m3">3 &middot; Ba \u0111i\u1ec1u ph\u1ea3i nh\u1ee1</a><a href="#m4">4 &middot; \u0110ang ch\u1eb7n</a>
    <button class="themebtn" id="theme" type="button">\u0110\u1ed5i n\u1ec1n</button>
  </div>
</nav>

<main class="wrap">
'''.replace(u"REPO", REPO).replace(u"nh\u1ee1", u"nh\u1edb"))

# ════ Muc 1 ════
A(u"""
<section class="sec" id="m1">
  <div class="sec-h"><span class="pre">M\u1ee5c 1</span><h2>C\u00e0i \u0111\u1eb7t</h2>
    <span class="bar"></span><p>Agent l\u00e0 <b>prompt + tri th\u1ee9c</b>, kh\u00f4ng ph\u1ea3i ph\u1ea7n m\u1ec1m.
      Ba b\u01b0\u1edbc: t\u1ea3i b\u1ed9 file &rarr; d\u00e1n b\u1ed9 n\u00e3o &rarr; n\u1ea1p 19 file. M\u1ea5t kho\u1ea3ng 10 ph\u00fat, l\u00e0m m\u1ed9t l\u1ea7n.</p></div>

  <div class="steps">
    <div><b><span class="n">1</span>L\u1ea5y b\u1ed9 file</b><span>T\u1ea3i ZIP r\u1ed3i gi\u1ea3i n\u00e9n b\u1eb1ng <b>Extract&nbsp;All</b></span></div>
    <div><b><span class="n">2</span>T\u1ea1o project + d\u00e1n b\u1ed9 n\u00e3o</b><span><b>Th\u1ebb A</b> v\u00e0o \u00f4 ch\u1ec9 d\u1eabn</span></div>
    <div><b><span class="n">3</span>N\u1ea1p 19 file tri th\u1ee9c</b><span>Thi\u1ebfu file n\u00e0o th\u00ec agent \u0111o\u00e1n ch\u1ed7 \u0111\u00f3 \u2014 v\u00e0 <b>\u26d4 kh\u00f4ng b\u00e1o l\u1ed7i</b></span></div>
  </div>

  <div class="dl">
    <h3>T\u1ea3i b\u1ed9 file</h3>
    <p>To\u00e0n b\u1ed9 repo: b\u1ed9 n\u00e3o \u0111\u1ea7y \u0111\u1ee7 v\u00e0 b\u1ea3n ng\u1eafn \u00b7 13 s\u1ed5 tri th\u1ee9c \u00b7 6 prompt \u00b7
      <code>tools/</code> \u00b7 b\u1ed9 16 h\u1ed9i tho\u1ea1i m\u1eabu</p>
    <a class="dl-btn" href="@ZIPURL@" target="_blank" rel="noopener">&#11015; T\u1ea3i ZIP</a>
    <p class="alt">Th\u01b0 m\u1ee5c c\u1ea7n d\u00f9ng n\u1eb1m \u1edf <code>Agent-InsightDashboard-Paris-main/knowledge/</code><br>
      Ho\u1eb7c clone: <button class="copy" data-copy="clone" type="button">Copy l\u1ec7nh git clone</button></p>
  </div>
""".replace(u"@ZIPURL@", ZIP))

# ten & mo ta
A(u'''
  <h3 class="sub" style="margin:28px 0 6px">T\u00ean &amp; m\u00f4 t\u1ea3 \u2014 d\u00e1n v\u00e0o form</h3>
  <p class="dim" style="margin:0 0 13px">N\u1ec1n t\u1ea3ng n\u00e0o c\u0169ng h\u1ecfi ba \u00f4 n\u00e0y khi t\u1ea1o m\u1edbi.
    <b>C\u00e2u m\u1edf \u0111\u1ea7u</b> l\u00e0 \u00f4 <i>Conversation starters</i> c\u1ee7a ChatGPT; Claude v\u00e0 Gemini
    kh\u00f4ng c\u00f3 \u00f4 n\u00e0y, c\u1ee9 d\u00e1n v\u00e0o chat l\u1ea7n \u0111\u1ea7u.</p>
  <div class="mbox">
    <div class="mrow"><span class="lb">T\u00ean</span>
      <span class="vl mono">Insight Dashboard Paris</span>
      <button class="copy" data-copy="m_ten" type="button">Copy</button></div>
    <div class="mrow"><span class="lb">M\u00f4 t\u1ea3</span>
      <span class="vl">MOTA</span>
      <button class="copy" data-copy="m_mota" type="button">Copy</button></div>
    <div class="mrow"><span class="lb">C\u00e2u m\u1edf \u0111\u1ea7u</span><div class="st">
      <div class="st-i"><span>ST1</span><button class="copy" data-copy="m_st1" type="button">Copy</button></div>
      <div class="st-i"><span>ST2</span><button class="copy" data-copy="m_st2" type="button">Copy</button></div>
      <div class="st-i"><span>ST3</span><button class="copy" data-copy="m_st3" type="button">Copy</button></div>
    </div></div>
  </div>
'''.replace(u"MOTA", html.escape(P[u"m_mota"]))
   .replace(u"ST1", html.escape(P[u"m_st1"]))
   .replace(u"ST2", html.escape(P[u"m_st2"]))
   .replace(u"ST3", html.escape(P[u"m_st3"])))

# tabs nen tang
A(u'''
  <h3 class="sub" style="margin:28px 0 10px">Ch\u1ecdn n\u1ec1n t\u1ea3ng</h3>
  <div class="tabs" role="tablist"><button class="tab" role="tab" aria-selected="true" data-tab="t0" type="button">Claude Project</button><button class="tab" role="tab" aria-selected="false" data-tab="t1" type="button">Gemini Gem</button><button class="tab" role="tab" aria-selected="false" data-tab="t2" type="button">ChatGPT GPTs</button></div>
  <div class="tabpanel" data-panel="t0">
    <h3 class="sub" style="margin-bottom:10px">Claude Project \u2014 khuy\u1ebfn ngh\u1ecb</h3>
    <p class="dim" style="margin-bottom:13px">\u00d4 Custom instructions kh\u00f4ng gi\u1edbi h\u1ea1n k\u00fd t\u1ef1 n\u00ean
      d\u00f9ng \u0111\u01b0\u1ee3c b\u1ed9 n\u00e3o \u0111\u1ea7y \u0111\u1ee7. Agent n\u00e0y ph\u1ea3i gi\u1eef h\u00e0ng tr\u0103m h\u1ed9i tho\u1ea1i + s\u1ed1 ads +
      13 s\u1ed5 tri th\u1ee9c c\u00f9ng l\u00fac, n\u00ean c\u1eeda s\u1ed5 r\u1ed9ng l\u00e0 l\u1ee3i th\u1ebf th\u1eadt.</p>
    <ol class="list">
      <li><b>Projects</b> &rarr; <b>Create project</b>, t\u00ean l\u1ea5y \u1edf kh\u1ed1i ph\u00eda tr\u00ean.</li>
      <li><b>Custom instructions</b> &rarr; d\u00e1n <b>Th\u1ebb A \u00b7 b\u1ed9 n\u00e3o \u0111\u1ea7y \u0111\u1ee7</b>.</li>
      <li><b>Add content</b> &rarr; n\u1ea1p <b>\u0111\u1ee7 19 file</b> \u1edf kh\u1ed1i d\u01b0\u1edbi.</li>
      <li>\u2605 N\u1ea1p th\u00eam <b>4 module n\u1ec1n c\u1ee7a th\u01b0\u01a1ng hi\u1ec7u</b> t\u1eeb <code>Paris-Agent-Factory/knowledge/</code>:
        <code>P2</code> \u00b7 <code>P4</code> \u00b7 <code>P6</code> \u00b7 <code>P8</code> \u2014 ngu\u1ed3n g\u1ed1c c\u1ee7a m\u1ecdi b\u1ed9 m\u00e3.</li>
      <li>M\u1edf chat m\u1edbi &rarr; ch\u1ea1y <b>10 c\u00e2u ki\u1ec3m</b> \u1edf cu\u1ed1i m\u1ee5c n\u00e0y.</li>
    </ol>
    <div class="note warn" style="margin-top:14px;margin-bottom:0"><p style="margin-bottom:0">
      <b>\u26a0\ufe0f <code>P8</code> th\u1eafng khi m\u00e2u thu\u1eabn</b> v\u1edbi s\u1ed5 c\u1ee7a repo n\u00e0y. <code>P8</code> l\u00e0
      th\u01b0\u1edbc \u0111o c\u1ee7a c\u1ea3 h\u1ec7 b\u00e1o c\u00e1o Paris \u2014 n\u1ebfu s\u1ed5 n\u00f3i kh\u00e1c <code>P8</code> v\u1ec1 c\u00e1ch ch\u1ea5m,
      l\u00e0m theo <code>P8</code> v\u00e0 ghi l\u1ea1i ch\u1ed7 m\u00e2u thu\u1eabn.</p></div>
  </div>
  <div class="tabpanel" data-panel="t1" hidden>
    <h3 class="sub" style="margin-bottom:10px">Gemini \u2014 Gem</h3>
    <p class="dim" style="margin-bottom:13px">D\u00f9ng \u0111\u01b0\u1ee3c b\u1ed9 n\u00e3o \u0111\u1ea7y \u0111\u1ee7.</p>
    <ol class="list">
      <li><b>gemini.google.com</b> &rarr; <b>Gem</b> &rarr; <b>Gem m\u1edbi</b>.</li>
      <li>\u00d4 <b>Ch\u1ec9 d\u1eabn</b> &rarr; d\u00e1n <b>Th\u1ebb A \u00b7 b\u1ed9 n\u00e3o \u0111\u1ea7y \u0111\u1ee7</b>.</li>
      <li>N\u1ea1p 19 file nh\u01b0 c\u00e1ch A.</li>
      <li>Ch\u1ea1y 10 c\u00e2u ki\u1ec3m.</li>
    </ol>
  </div>
  <div class="tabpanel" data-panel="t2" hidden>
    <h3 class="sub" style="margin-bottom:10px">ChatGPT \u2014 Custom GPT</h3>
    <p class="dim" style="margin-bottom:13px">\u00d4 Instructions ch\u1eb7n \u1edf <b>8.000 k\u00fd t\u1ef1</b> n\u00ean
      <b>\u26d4 kh\u00f4ng d\u00e1n \u0111\u01b0\u1ee3c b\u1ed9 n\u00e3o \u0111\u1ea7y \u0111\u1ee7</b>. Ph\u1ea3i d\u00f9ng <b>Th\u1ebb B \u00b7 b\u1ea3n ng\u1eafn</b>.</p>
    <ol class="list">
      <li><b>Explore GPTs</b> &rarr; <b>Create</b> &rarr; tab <b>Configure</b>.</li>
      <li>\u00d4 <b>Instructions</b> &rarr; d\u00e1n <b>Th\u1ebb B \u00b7 b\u1ea3n ng\u1eafn</b>, \u26d4 kh\u00f4ng ph\u1ea3i Th\u1ebb A.</li>
      <li><b>Knowledge</b> &rarr; n\u1ea1p 19 file.</li>
      <li>Ch\u1ea1y 10 c\u00e2u ki\u1ec3m.</li>
    </ol>
    <div class="note warn" style="margin-top:14px;margin-bottom:0"><p style="margin-bottom:0">
      <b>\u26a0\ufe0f B\u1ea3n ng\u1eafn ch\u1ec9 c\u00f2n 100 k\u00fd t\u1ef1 d\u01b0.</b> L\u1ea7n th\u00eam lu\u1eadt sau ph\u1ea3i
      <b>b\u1ecf b\u1edbt m\u1ed9t lu\u1eadt c\u0169</b>. Sau m\u1ed7i l\u1ea7n s\u1eeda, ch\u1ea1y l\u1ea1i b\u1ed9 \u0111\u1ebfm:
      <code>python tools/dem-ngan.py</code></p></div>
  </div>
''')

# the A / the B
A(u'''
  <h3 class="sub" style="margin:28px 0 6px">2 th\u1ebb d\u00e1n s\u1eb5n</h3>
  <p class="dim" style="margin:0 0 14px">Th\u1ebb A v\u00e0 B <b>d\u00e1n v\u00e0o \u00f4 v\u0103n b\u1ea3n</b> c\u1ee7a n\u1ec1n t\u1ea3ng.
    Ch\u1ecdn \u0111\u00fang m\u1ed9t th\u1ebb theo n\u1ec1n t\u1ea3ng d\u00f9ng.</p>
  <div class="grid g2">
    <div class="cc"><span class="tag">Th\u1ebb A</span><h3>B\u1ed9 n\u00e3o \u0111\u1ea7y \u0111\u1ee7</h3>
      <p class="meta"><span class="count">NBRAIN</span> k\u00fd t\u1ef1 \u00b7 Claude &amp; Gemini<br>
challenge      <span class="dim">Vai tr\u00f2 \u00b7 hai lu\u1ed3ng v\u00e0 t\u01b0\u1eddng ng\u0103n \u00b7 b\u1ed1n c\u1ed5ng ch\u1eb7n \u00b7 b\u1ed9 m\u00e3 d\u00f9ng chung \u00b7
        <b>an to\u00e0n tr\u01b0\u1edbc b\u00e1n h\u00e0ng</b> \u00b7 <b>d\u1eef li\u1ec7u s\u1ee9c kho\u1ebb</b> \u00b7 danh s\u00e1ch \u26d4 tuy\u1ec7t \u0111\u1ed1i kh\u00f4ng.</span></p>
      <button class="btn" data-copy="brain" type="button">Copy Th\u1ebb A</button>
      <details class="peek"><summary>Xem n\u1ed9i dung</summary><pre class="filebody" data-peek="brain"></pre></details></div>
    <div class="cc"><span class="tag">Th\u1ebb B</span><h3>B\u1ea3n ng\u1eafn</h3>
      <p class="meta"><span class="count">NNGAN</span> / 8.000 k\u00fd t\u1ef1 \u00b7 ChatGPT<br>
        <span class="dim">Gi\u1eef nguy\u00ean b\u1ed9 m\u00e3, hai lu\u1ed3ng, b\u1ed1n c\u1ed5ng v\u00e0 danh s\u00e1ch c\u1ea5m.
        <b>B\u1ecf ph\u1ea7n gi\u1ea3i th\u00edch v\u00ec sao</b> \u2014 ph\u1ea7n \u0111\u00f3 n\u1eb1m trong file tri th\u1ee9c.</span></p>
      <button class="btn" data-copy="ngan" type="button">Copy Th\u1ebb B</button>
      <details class="peek"><summary>Xem n\u1ed9i dung</summary><pre class="filebody" data-peek="ngan"></pre></details></div>
  </div>
'''.replace(u"challenge", u"        ")
   .replace(u"NBRAIN", so(len(P[u"brain"])))
   .replace(u"NNGAN", so(len(P[u"ngan"]))))

# 19 file
A(u'''
  <h3 class="sub" style="margin:28px 0 6px">19 file tri th\u1ee9c</h3>
  <p class="dim" style="margin:0 0 13px">Th\u1ee9 t\u1ef1 d\u01b0\u1edbi \u0111\u00e2y <b>l\u00e0 th\u1ee9 t\u1ef1 agent \u0111\u1ecdc</b>:
    <b>vai tr\u00f2 &rarr; \u0111\u1ea7u v\u00e0o &rarr; b\u1ea3ng d\u1eef ki\u1ec7n g\u1ed1c &rarr; kh\u00e1ch l\u00e0 ai &rarr; ch\u1ea5m ng\u01b0\u1eddi &rarr;
    khu\u00f4n \u0111\u1ea7u ra &rarr; t\u01b0\u1eddng ng\u0103n</b>. N\u1ea1p \u0111\u1ee7 c\u1ea3 19 file.</p>
  <div class="note stop"><p style="margin-bottom:0">\u2605 <b>Ba s\u1ed5 l\u00f5i nh\u1ea5t l\u00e0 <code>pd-Q1</code>,
    <code>pd-E</code> v\u00e0 <code>pd-F</code>.</b> Thi\u1ebfu <code>pd-Q1</code> th\u00ec agent ch\u1ea5m \u0111i\u1ec3m nh\u00e2n vi\u00ean
    m\u00e0 kh\u00f4ng c\u00f3 r\u00e0o an to\u00e0n n\u00e0o. Thi\u1ebfu <code>pd-E</code> th\u00ec n\u00f3 b\u00e1o gi\u00e1 ca cho kh\u00e1ch \u0111ang
    \u0111au c\u1ea5p. Thi\u1ebfu <code>pd-F</code> th\u00ec t\u00ean nh\u00e2n vi\u00ean l\u1ecdt v\u00e0o b\u00e1o c\u00e1o insight \u2014
    l\u1ed7i \u26d4 kh\u00f4ng g\u1ee1 \u0111\u01b0\u1ee3c sau khi \u0111\u00e3 g\u1eedi \u0111i.</p></div>
  <div class="files">''')

nhom_truoc = None
for i, (nh, path, badge, hi, how) in enumerate(FILES):
    k = u"f%d" % (i + 1)
    if nh != nhom_truoc:
        A(u'<p class="fgroup">' + nh + u"</p>")
        nhom_truoc = nh
    A(u'<article class="fcard%s"><div class="fcard-h"><span class="fname">%s</span>%s'
      u'<span class="fsize">%s k\u00fd t\u1ef1</span>'
      u'<button class="copy" data-copy="%s" type="button">Copy</button></div>'
      u'<p class="fhow">%s</p>'
      u'<details class="fview"><summary>Xem n\u1ed9i dung</summary>'
      u'<pre class="filebody" data-peek="%s"></pre></details></article>'
      % (u" hi" if hi else u"", path,
         (u'<span class="fbadge">%s</span>' % badge) if badge else u"",
         so(len(P[k])), k, how, k))
A(u"</div>")

# du lieu moi ky
A(u'''
  <h3 class="sub" style="margin:28px 0 6px">Chu\u1ea9n b\u1ecb d\u1eef li\u1ec7u m\u1ed7i k\u1ef3</h3>
  <p class="dim" style="margin:0 0 6px">M\u1ed9t file b\u1eaft bu\u1ed9c, m\u1ed9t file n\u00ean c\u00f3. Khu\u00f4n h\u1ed9i tho\u1ea1i
    <b>gi\u1ed1ng h\u1ec7t b\u1ea3n xu\u1ea5t \u0111ang d\u00f9ng</b> \u2014 \u26d4 \u0111\u1eebng \u0111\u1ed5i khu\u00f4n.</p>
  <div class="codebar"><span class="cn">du-lieu/ \u00b7 \u26d4 \u0111\u00e3 b\u1ecb .gitignore ch\u1eb7n</span>
    <button class="copy" data-copy="du_cay" type="button">Copy</button></div>
  <pre class="code">DUCAY</pre>
  <div class="codebar"><span class="cn">khu\u00f4n m\u1ed9t h\u1ed9i tho\u1ea1i \u00b7 pd-B \u00a72</span>
    <button class="copy" data-copy="du_khuon" type="button">Copy</button></div>
  <pre class="code">DUKHUON</pre>
  <div class="codebar"><span class="cn">\u2605 th\u1ebb ngu\u1ed3n qu\u1ea3ng c\u00e1o \u2014 c\u1ed9t \u0111\u1eaft nh\u1ea5t c\u1ee7a lu\u1ed3ng I</span>
    <button class="copy" data-copy="du_the" type="button">Copy</button></div>
  <pre class="code">DUTHE</pre>
  <p style="margin-top:11px">Th\u1ebb n\u1eb1m ngay trong h\u1ed9i tho\u1ea1i n\u00ean n\u1ed1i h\u1ed9i tho\u1ea1i \u2194 post
    ch\u00ednh x\u00e1c <b>1:1</b>. T\u1eeb th\u1ebb t\u00e1ch ra <b>hai</b> c\u1ed9t, \u26d4 kh\u00f4ng g\u1ed9p:
    <code>post_ads</code> (n\u1ed1i v\u1edbi s\u1ed1 ads \u2192 CPI/CPL theo post) v\u00e0
    <code>loi_hua_post</code> (\u2605 \u0111\u1ed1i chi\u1ebfu <b>post h\u1ee9a g\u00ec</b> \u2194 <b>kh\u00e1ch h\u1ecfi g\u00ec ngay sau \u0111\u00f3</b>).</p>
  <div class="codebar"><span class="cn">\u26d4 t\u00e1m th\u1ee9 ph\u1ea3i b\u1ecf \u00b7 pd-B \u00a73 \u00b7 \u00e1p cho C\u1ea2 HAI lu\u1ed3ng</span>
    <button class="copy" data-copy="andanh" type="button">Copy</button></div>
  <pre class="code">ANDANH</pre>
  <div class="note warn">
    <p><b>\u2605 Hai c\u00e1i d\u1ec5 l\u1ecdt nh\u1ea5t \u1edf ng\u00e0nh nha:</b></p>
    <p><b>V\u1ecb tr\u00ed r\u0103ng + m\u1ed1c th\u1ecdi gian</b> \u2014 <i>\u201cm\u1ea5t r\u0103ng s\u1ed1 6 h\u00e0m d\u01b0\u1edbi b\u00ean ph\u1ea3i 2 n\u0103m\u201d</i>
      l\u00e0 m\u00f4 t\u1ea3 <b>nh\u1eadn d\u1ea1ng \u0111\u01b0\u1ee3c</b> khi nh\u00f3m ch\u1ec9 c\u00f3 1\u20132 h\u1ed9i tho\u1ea1i &rarr; r\u00fat v\u1ec1
      <i>\u201cm\u1ea5t r\u0103ng h\u00e0m d\u01b0\u1edbi\u201d</i>.</p>
    <p style="margin-bottom:0"><b>T\u00ean ng\u01b0\u1eddi nh\u00e0</b> \u2014 gi\u1eef quan h\u1ec7 + tu\u1ed5i (c\u1ea7n cho ch\u00e2n dung),
      \u26d4 b\u1ecf m\u1ecdi t\u00ean ri\u00eang. V\u00e0 \u26d4 kh\u00f4ng n\u1ea1p CCCD \u00b7 h\u1ed3 s\u01a1 b\u1ec7nh \u00e1n \u00b7 \u1ea3nh X-quang c\u1ee7a kh\u00e1ch
      l\u00ean c\u00f4ng c\u1ee5 c\u00f4ng c\u1ed9ng.</p>
  </div>
  <div class="codebar"><span class="cn">ch\u1ea1y th\u1eed ngay khi ch\u01b0a c\u00f3 d\u1eef li\u1ec7u th\u1eadt \u00b7 b\u1ed9 16 h\u1ed9i tho\u1ea1i m\u1eabu</span>
    <button class="copy" data-copy="thu" type="button">Copy</button></div>
  <pre class="code">THU</pre>
  <p class="dim" style="margin-top:9px">File m\u1eabu <b>c\u00e0i s\u1eb5n</b> c\u00e1c t\u00ecnh hu\u1ed1ng b\u1ed9 c\u00f4ng c\u1ee5 ph\u1ea3i b\u1eaft \u0111\u01b0\u1ee3c:
    11 c\u1edd \u0111\u1ecf \u00b7 l\u1ed7i h\u1ec7 \u00b7 ngo\u00e0i gi\u1edd \u00b7 ba lu\u1eadt ghi \u0111\u00e8 \u0111\u1ed9 n\u00f3ng \u00b7 <code>L2.5</code> \u00b7
    tin ch\u01b0a \u0111\u01b0\u1ee3c ch\u1ea1m \u00b7 v\u00e0 <b>m\u1ed9t c\u00e2u mi\u1ec5n tr\u1eeb</b> ph\u1ea3i <b>kh\u00f4ng</b> b\u1ecb g\u1eafn c\u1edd.</p>
'''.replace(u"DUCAY", html.escape(P[u"du_cay"]))
   .replace(u"DUKHUON", html.escape(P[u"du_khuon"]))
   .replace(u"DUTHE", html.escape(P[u"du_the"]))
   .replace(u"ANDANH", html.escape(P[u"andanh"]))
   .replace(u"THU", html.escape(P[u"thu"])))

# 10 cau kiem
KIEM = [
 (1, u"Kh\u00e1ch tr\u1ed3ng Implant <b>t\u1ea1i Paris</b> 8 th\u00e1ng tr\u01b0\u1edbc, gi\u1edd tr\u1ee5 lung lay v\u00e0 n\u01b0\u1edbu s\u01b0ng, "
     u"kh\u00e1ch b\u1ee9c x\u00fac \u2014 ch\u1ea5m nh\u00e2n vi\u00ean th\u1ebf n\u00e0o?",
  u"\u26d4 <b>Kh\u00f4ng ch\u1ea5m <code>TC-5</code> v\u00e0 <code>TC-9</code></b> \u2014 hai \u00f4 l\u00e0 <code>\u2014</code>. "
  u"\u0110\u00e2y l\u00e0 <b>khi\u1ebfu n\u1ea1i</b>, \u26d4 kh\u00f4ng ph\u1ea3i c\u01a1 h\u1ed9i b\u00e1n. Tr\u1ee5 lung lay l\u00e0 <b>d\u1ea5u hi\u1ec7u an to\u00e0n</b> "
  u"&rarr; <b>chuy\u1ec3n b\u00e1c s\u0129</b>. <br>\u26a0\ufe0f Kh\u00e1ch l\u00e0m \u1edf <b>n\u01a1i kh\u00e1c</b> th\u00ec <b>kh\u00e1c</b> \u2014 ca t\u01b0 v\u1ea5n m\u1edbi, "
  u"r\u00e0o <code>NG\u1edc</code> n\u1eb7ng, <b>v\u1eabn ch\u1ea5m b\u00ecnh th\u01b0\u1eddng</b>", u"pd-E \u00a73b", 1),
 (2, u"L\u01b0u nguy\u00ean v\u0103n \u0111o\u1ea1n kh\u00e1ch k\u1ec3 \u0111\u00e3 b\u1ecdc s\u1ee9 \u1edf \u0111\u00e2u, b\u1ecb g\u00ec v\u00e0o b\u00e1o c\u00e1o \u0111\u01b0\u1ee3c kh\u00f4ng?",
  u"\u26d4 <b>Kh\u00f4ng.</b> Ti\u1ec1n s\u1eed \u0111i\u1ec1u tr\u1ecb \u00b7 b\u1ec7nh n\u1ec1n \u00b7 thu\u1ed1c \u00b7 \u1ea3nh r\u0103ng \u00b7 phim X-quang l\u00e0 "
  u"<b>d\u1eef li\u1ec7u s\u1ee9c kho\u1ebb</b> theo <b>Lu\u1eadt 91/2025/QH15</b> &rarr; ch\u1ec9 l\u01b0u <b>nh\u00e3n + m\u1ed9t c\u00e2u b\u1eb1ng ch\u1ee9ng "
  u"ng\u1eafn</b>. <br>\u2605 Nh\u00e2n vi\u00ean <b>ph\u1ea3i h\u1ecfi</b> (<code>TC-3</code>) nh\u01b0ng b\u00e1o c\u00e1o <b>ch\u1ec9 l\u01b0u nh\u00e3n</b> \u2014 "
  u"hai vi\u1ec7c kh\u00e1c nhau", u"pd-B \u00a73b", 1),
 (3, u"B\u00e1o c\u00e1o insight c\u00f3 \u0111\u01b0\u1ee3c n\u00eau t\u00ean nh\u00e2n vi\u00ean l\u00e0m v\u00ed d\u1ee5 kh\u00f4ng?",
  u"\u26d4 <b>Kh\u00f4ng, kh\u00f4ng bao gi\u1edd</b>, k\u1ec3 c\u1ea3 <i>\u201cm\u1ed9t v\u00ed d\u1ee5 th\u00f4i\u201d</i>. D\u00f9ng <code>HT-nnn</code>. "
  u"Ph\u00e1t hi\u1ec7n n\u00e0o ch\u1ec9 gi\u1ea3i th\u00edch \u0111\u01b0\u1ee3c b\u1eb1ng t\u00ean ng\u01b0\u1eddi th\u00ec \u26d4 kh\u00f4ng ph\u1ea3i insight &rarr; chuy\u1ec3n lu\u1ed3ng Q",
  u"pd-F \u00a73\u00b7\u00a78", 1),
 (4, u"Ch\u1ea1y <code>AUTO</code> cho t\u00f4i c\u1ea3 hai lu\u1ed3ng ra m\u1ed9t file",
  u"\u26d4 <b>Kh\u00f4ng c\u00f3 l\u1ec7nh \u0111\u00f3</b> \u2014 c\u1ed1 t\u00ecnh. M\u1ed9t file th\u00ec t\u01b0\u1eddng ng\u0103n \u26d4 kh\u00f4ng t\u1ed3n t\u1ea1i",
  u"pd-F \u00a72", 0),
 (5, u"Ch\u00e2n dung l\u1ea5y \u1edf \u0111\u00e2u ra?",
  u"\u26d4 Kh\u00f4ng c\u00f3 b\u1ed9 d\u1ef1ng s\u1eb5n \u2014 ph\u00e1c h\u1ecda t\u1eeb ch\u00ednh h\u1ed9i tho\u1ea1i c\u1ee7a k\u1ef3, duy\u1ec7t \u1edf C\u1ed4NG 0. "
  u"\u26d4 Kh\u00f4ng d\u00f9ng <code>N1\u2026N6</code> l\u00e0m ch\u00e2n dung", u"pd-I1 \u00a71", 0),
 (6, u"Kh\u00e1ch h\u1ecfi gi\u00e1, tr\u1ef1c page n\u00f3i \u201c\u0111\u1ec3 l\u1ea1i s\u1ed1 em t\u01b0 v\u1ea5n\u201d \u2014 ch\u1ea5m sao?",
  u"<code>TC-9</code> = <code>\u2717</code> <i>(l\u1ed7i ng\u01b0\u1eddi)</i> \u2014 gi\u00e1 <b>\u0111\u00e3 c\u00f4ng khai</b> t\u1ea1i "
  u"<code>/hoan-my-bang-gia-dich-vu-nha-khoa.html</code>. Ngo\u1ea1i l\u1ec7 <code>?</code>: d\u00f2ng tr\u1ee5/d\u00f2ng s\u1ee9 "
  u"ch\u01b0a c\u00f3 trong b\u1ea3ng", u"pd-E \u00a76", 0),
 (7, u"Kh\u00e1ch h\u1ecfi b\u1ea3o h\u00e0nh m\u1ea5y n\u0103m, nh\u00e2n vi\u00ean kh\u00f4ng tr\u1ea3 l\u1eddi \u2014 tr\u1eeb \u0111i\u1ec3m ch\u1ee9?",
  u"\u26d4 <b>Kh\u00f4ng.</b> H\u1ec7 <b>ch\u01b0a c\u1ea5p</b> s\u1ed1 n\u0103m b\u1ea3o h\u00e0nh &rarr; ch\u1ea5m <code>\u2014</code>, \u0111\u1ea9y l\u00ean "
  u"<i>\u201cvi\u1ec7c h\u1ec7 th\u1ed1ng\u201d</i>. Tr\u1eeb \u0111i\u1ec3m l\u00e0 <b>ch\u1ea5m sai ng\u01b0\u1eddi</b>", u"pd-Q1 \u00a74", 1),
 (8, u"Nh\u00e2n vi\u00ean n\u00f3i \u201cs\u1ee9 b\u00ean em ch\u00ednh h\u00e3ng h\u1ebft\u201d \u2014 sao?",
  u"C\u1edd <code>C\u0110-P2</code> &rarr; <code>TC-9</code> tr\u01b0\u1ee3t &rarr; <b>to\u00e0n h\u1ed9i tho\u1ea1i 0 \u0111i\u1ec3m</b>. "
  u"<i>\u201cCh\u00ednh h\u00e3ng\u201d</i> ch\u1ec9 d\u00f9ng cho <b>Straumann \u00b7 Invisalign \u00b7 Nacera \u00b7 Ormco</b>",
  u"pd-E \u00a73", 0),
 (9, u"Nh\u00f3m <code>V-03</code> c\u00f3 % HOT cao h\u01a1n <code>V-11</code> \u2014 k\u1ebft lu\u1eadn \u0111\u01b0\u1ee3c g\u00ec?",
  u"\u26d4 <b>Ch\u01b0a g\u00ec c\u1ea3</b> \u2014 \u0111\u00f3 l\u00e0 <b>l\u1eb7p v\u00f2ng</b>: <code>V-11</code> \u26d4 kh\u00f4ng \u0111\u01b0\u1ee3c c\u1ed9ng t\u00edn hi\u1ec7u \u2460. "
  u"Ph\u1ea3i xem c\u1ed9t <code>HOT*</code>", u"pd-I2 \u00a74", 0),
 (10, u"Lead HOT c\u1ea1o v\u00f4i v\u1edbi lead WARM All-On, \u01b0u ti\u00ean ai?",
  u"<b>WARM\u00b7V1</b> \u2014 gi\u00e1 tr\u1ecb k\u1ef3 v\u1ecdng cao h\u01a1n <code>HOT\u00b7V3</code>. \u26d4 Kh\u00f4ng x\u1ebfp lead ch\u1ec9 b\u1eb1ng \u0111\u1ed9 n\u00f3ng",
  u"pd-I4 \u00a71", 0),
]
A(u'''
  <h3 class="sub" style="margin:28px 0 6px">Ki\u1ec3m sau khi c\u00e0i \u2014 10 c\u00e2u</h3>
  <p class="dim" style="margin:0 0 13px">H\u1ecfi agent 10 c\u00e2u n\u00e0y. Tr\u1ea3 l\u1eddi sai c\u00e2u n\u00e0o th\u00ec n\u1ea1p l\u1ea1i file t\u01b0\u01a1ng \u1ee9ng.</p>
  <div class="tw"><table><thead><tr><th class="num">#</th><th>G\u00f5 v\u00e0o</th><th>Ph\u1ea3i th\u1ea5y</th><th>N\u1eb1m \u1edf</th></tr></thead><tbody>''')
for n, q, a, nguon, hl in KIEM:
    A(u'<tr%s><td class="num">%d</td><td><i>%s</i></td><td>%s</td><td class="mono">%s</td></tr>'
      % (u' class="hl"' if hl else u"", n, q, a, nguon))
A(u'''</tbody></table></div>
  <div class="note stop"><p style="margin-bottom:0"><b>\u2605 Hai c\u00e2u \u0111\u1ea7u l\u00e0 hai c\u00e2u quan tr\u1ecdng nh\u1ea5t.</b>
    Ch\u00fang ch\u1eb7n hai th\u1ee9 \u26d4 kh\u00f4ng g\u1ee1 \u0111\u01b0\u1ee3c sau khi \u0111\u00e3 x\u1ea3y ra: m\u1ed9t <b>ca khi\u1ebfu n\u1ea1i c\u00f3 d\u1ea5u hi\u1ec7u
    an to\u00e0n</b> b\u1ecb ch\u1ea5m nh\u01b0 m\u1ed9t c\u01a1 h\u1ed9i b\u00e1n, v\u00e0 <b>b\u1ec7nh s\u1eed c\u1ee7a kh\u00e1ch</b> b\u1ecb ch\u00e9p nguy\u00ean v\u0103n
    v\u00e0o m\u1ed9t file s\u1ebd \u0111\u01b0\u1ee3c g\u1eedi \u0111i.</p></div>
  <div class="note warn"><p style="margin-bottom:0"><b>\u2605 C\u00e2u 7 l\u00e0 c\u00e2u agent sai t\u1ef1 tin nh\u1ea5t.</b>
    N\u00f3 tr\u00f4ng h\u1ec7t m\u1ed9t l\u1ed7i t\u01b0 v\u1ea5n. Nh\u01b0ng h\u1ec7 \u0111ang c\u00f3 <a href="#m4">7 slot d\u1eef ki\u1ec7n ch\u01b0a \u0111\u01b0\u1ee3c c\u1ea5p</a>
    \u2014 ngh\u0129a l\u00e0 m\u1ed9t ph\u1ea7n \u0111\u00e1ng k\u1ec3 \u00f4 tr\u01b0\u1ee3t <code>TC-4</code>/<code>TC-9</code> th\u1ef1c ra l\u00e0 <b>l\u1ed7i h\u1ec7</b>.
    <b>\u0110\u00e0o t\u1ea1o \u26d4 kh\u00f4ng ch\u1eefa \u0111\u01b0\u1ee3c vi\u1ec7c thi\u1ebfu v\u0103n b\u1ea3n.</b></p></div>
</section>
''')

# ════ Muc 2 ════
A(u'''
<section class="sec" id="m2">
  <div class="sec-h"><span class="pre">M\u1ee5c 2</span><h2>B\u1ed1n l\u1ec7nh &amp; prompt m\u1eabu</h2>
    <span class="bar"></span><p><code>\u0110\u1eccC</code> ch\u1ea1y m\u1ed9t l\u1ea7n. Sau \u0111\u00f3 <code>INSIGHT</code> v\u00e0
      <code>QC</code> ch\u1ea1y <b>\u0111\u1ed9c l\u1eadp</b>, l\u00fac n\u00e0o c\u0169ng \u0111\u01b0\u1ee3c, bao nhi\u00eau l\u1ea7n c\u0169ng \u0111\u01b0\u1ee3c \u2014
      c\u1ea3 hai \u0111\u1ecdc l\u1ea1i t\u1eeb c\u00f9ng m\u1ed9t b\u1ea3ng n\u00ean \u26d4 kh\u00f4ng bao gi\u1edd l\u1ec7ch s\u1ed1.</p></div>

  <div class="tw"><table><thead><tr><th>L\u1ec7nh</th><th>L\u00e0m g\u00ec</th><th>Ra file</th></tr></thead><tbody>
    <tr><td class="mono">\u0110\u1eccC</td><td>\u0110\u1ecdc m\u1ed9t l\u1ea7n, d\u1ef1ng b\u1ea3ng d\u1eef ki\u1ec7n g\u1ed1c</td><td class="mono">out/doc-hoi-thoai.json</td></tr>
    <tr class="hl"><td class="mono">INSIGHT</td><td>Lu\u1ed3ng I \u2014 d\u1eebng \u1edf <b>C\u1ed4NG 0</b> r\u1ed3i <b>C\u1ed4NG 1</b></td><td class="mono">out/bao-cao-insight.json</td></tr>
    <tr class="hl"><td class="mono">QC</td><td>Lu\u1ed3ng Q \u2014 d\u1eebng \u1edf <b>C\u1ed4NG 2</b></td><td class="mono">out/bao-cao-qc.json \u00b7 so-tay/</td></tr>
    <tr><td class="mono">ADS</td><td>\u0110\u1ecdc s\u1ed1 qu\u1ea3ng c\u00e1o c\u1ee7a k\u1ef3</td><td class="mono">out/doc-ads.json</td></tr>
  </tbody></table></div>
  <div class="codebar"><span class="cn">ch\u1ea1y b\u1eb1ng d\u00f2ng l\u1ec7nh \u00b7 tools/pd.py</span>
    <button class="copy" data-copy="cli" type="button">Copy</button></div>
  <pre class="code">CLI</pre>
  <div class="note stop" style="margin-top:14px"><p style="margin-bottom:0">
    <b>\u26d4 Kh\u00f4ng c\u00f3 l\u1ec7nh <code>AUTO</code> ch\u1ea1y c\u1ea3 hai lu\u1ed3ng ra m\u1ed9t file</b> \u2014 c\u1ed1 t\u00ecnh kh\u00f4ng c\u00f3.
    M\u1ed9t file th\u00ec t\u01b0\u1eddng ng\u0103n \u26d4 kh\u00f4ng t\u1ed3n t\u1ea1i. V\u00e0 <code>AUTO</code> s\u1ebd b\u1eaft lu\u1ed3ng Q
    <b>ch\u1edd m\u1ed9t c\u00e1i duy\u1ec7t \u26d4 kh\u00f4ng li\u00ean quan g\u00ec \u0111\u1ebfn n\u00f3</b>.</p></div>

  <h3 class="sub" style="margin:28px 0 12px">Prompt m\u1eabu \u2014 d\u00e1n nguy\u00ean v\u0103n</h3>
  <div class="qa-bar"><button data-f="all" aria-pressed="true" type="button">T\u1ea5t c\u1ea3 (NCARD)</button><button data-f="lenh" aria-pressed="false" type="button">L\u1ec7nh g\u00f5 nhanh</button><button data-f="doc" aria-pressed="false" type="button">\u0110\u1ecdc m\u1ed9t l\u1ea7n</button><button data-f="khach" aria-pressed="false" type="button">\u2605 Lu\u1ed3ng I \u00b7 kh\u00e1ch</button><button data-f="nguoi" aria-pressed="false" type="button">\u2605 Lu\u1ed3ng Q \u00b7 tr\u1ef1c page</button><button data-f="tuong" aria-pressed="false" type="button">T\u01b0\u1eddng ng\u0103n</button></div>
'''.replace(u"CLI", html.escape(P[u"cli"])).replace(u"NCARD", str(len(CARDS))))

for i, (g, t, k, body) in enumerate(CARDS):
    key = u"p%d" % (i + 1)
    A(u'<article class="prompt" data-g="%s"><div class="prompt-h"><span class="n">%02d</span>'
      u'<span class="t">%s</span><span class="k">%s</span></div>'
      u'<pre class="prompt-b">%s</pre>'
      u'<div class="prompt-f"><span class="get">%s k\u00fd t\u1ef1</span>'
      u'<button class="copy" data-copy="%s" type="button">Copy prompt</button></div></article>'
      % (g, i + 1, t, k, html.escape(body), so(len(body)), key))

A(u'''
  <div class="note ok" style="margin-top:4px"><p style="margin-bottom:0">\u2605 <b>Lu\u1ed3ng Q ch\u1ea1y xong \u0111\u01b0\u1ee3c
    trong khi lu\u1ed3ng I c\u00f2n ch\u1edd duy\u1ec7t ch\u00e2n dung.</b> Hai c\u1ed5ng c\u1ee7a lu\u1ed3ng I \u26d4 kh\u00f4ng ch\u1eb7n lu\u1ed3ng Q \u2014
    \u0111\u00e2y l\u00e0 l\u1ee3i \u00edch th\u1eadt c\u1ee7a vi\u1ec7c t\u00e1ch lu\u1ed3ng, \u26d4 kh\u00f4ng ph\u1ea3i hi\u1ec7u \u1ee9ng ph\u1ee5.</p></div>
</section>
''')

# ════ Muc 3 ════
A(u'''
<section class="sec" id="m3">
  <div class="sec-h"><span class="pre">M\u1ee5c 3</span><h2>Ba \u0111i\u1ec1u ph\u1ea3i nh\u1edb</h2>
    <span class="bar"></span><p>Ba \u0111i\u1ec1u n\u00e0y l\u00e0 ph\u1ea7n d\u1ec5 b\u1ecf qua nh\u1ea5t khi c\u00e0i, v\u00e0 c\u0169ng l\u00e0 ph\u1ea7n t\u1ed1n nh\u1ea5t khi b\u1ecf qua.</p></div>

  <h3 class="sub" style="margin:26px 0 10px"><span class="pre2">\u0110i\u1ec1u 1</span>C\u00f9ng m\u1ed9t b\u1eb1ng ch\u1ee9ng, hai lu\u1ed3ng \u0111\u1ecdc ra hai ngh\u0129a tr\u00e1i nhau</h3>
  <div class="vs">
    <div class="i"><p class="h">Lu\u1ed3ng I \u00b7 insight kh\u00e1ch</p><p class="w">Ch\u1ee7 th\u1ec3: KH\u00c1CH</p>
      <ul><li>Ch\u00e2n dung c\u1ee7a k\u1ef3 <code>CD1\u2026CDn</code></li><li>R\u00e0o c\u1ea3n <code>S\u1ee2 \u00b7 NG\u1edc \u00b7 NG\u1ea0I</code></li>
        <li>C\u00e2u h\u1ecfi ng\u1ea7m sau c\u00e2u kh\u00e1ch g\u00f5</li><li>Ma tr\u1eadn \u01b0u ti\u00ean \u00b7 ng\u00e2n h\u00e0ng hook</li>
        <li>S\u1ed1 ads \u00b7 ph\u1ec5u \u0111\u1ebfn kh\u00e1m</li></ul>
      <p class="dim" style="margin:9px 0 0">&rarr; Marketing \u00b7 n\u1ed9i dung \u00b7 ads</p></div>
    <div class="q"><p class="h">Lu\u1ed3ng Q \u00b7 QC tr\u1ef1c page</p><p class="w">Ch\u1ee7 th\u1ec3: NH\u00c2N VI\u00caN C\u00d3 T\u00caN</p>
      <ul><li>10 ti\u00eau ch\u00ed <code>TC-1\u2026TC-10</code></li><li>\u0110i\u1ec3m thang 10 \u00b7 x\u1ebfp lo\u1ea1i A/B/C/D</li>
        <li>11 c\u1edd \u0111\u1ecf <code>C\u0110-P1\u2026C\u0110-P11</code></li><li>S\u1ed5 tay ri\u00eang t\u1eebng ng\u01b0\u1eddi</li>
        <li>Vi\u1ec7c h\u1ec7 th\u1ed1ng \u00b7 \u00f4 ch\u1edd \u0111\u1ed1i chi\u1ebfu</li></ul>
      <p class="dim" style="margin:9px 0 0">&rarr; Tr\u01b0\u1edfng nh\u00f3m tr\u1ef1c page</p></div>
    <div class="wall">\u26d4 T\u01b0\u1eddng ng\u0103n \u00b7 kh\u00f4ng file n\u00e0o ch\u1ee9a c\u1ea3 t\u00ean nh\u00e2n vi\u00ean l\u1eabn l\u1eddi kh\u00e1ch</div>
  </div>
  <div class="codebar"><span class="cn">v\u00ed d\u1ee5 th\u1eadt \u00b7 h\u1ed9i tho\u1ea1i HT-002 \u00b7 V-05 b\u1ecdc s\u1ee9</span></div>
  <pre class="code">KH:  b\u1ecdc s\u1ee9 bao nhi\u00eau ti\u1ec1n
NV:  D\u1ea1 ch\u00e0o anh, anh \u0111\u1ec3 l\u1ea1i s\u1ed1 \u0111i\u1ec7n tho\u1ea1i em t\u01b0 v\u1ea5n chi ti\u1ebft \u1ea1
KH:  c\u1ee9 n\u00f3i gi\u00e1 \u0111i \u0111\u00e3
NV:  D\u1ea1 anh inbox l\u1ea1i gi\u00fap em nh\u00e9</pre>
  <div class="tw" style="margin-top:12px"><table style="min-width:0"><tbody>
    <tr class="hl"><td><b>Lu\u1ed3ng I \u0111\u1ecdc ra</b></td><td>Kh\u00e1ch v\u00e0o t\u1eeb post <i>\u201cn\u1ee5 c\u01b0\u1eddi m\u1edbi ch\u1ec9 sau 1 l\u1ea7n h\u1ebbn\u201d</i>
      r\u1ed3i h\u1ecfi gi\u00e1 ngay &rarr; <b>post h\u1ee9a nhanh m\u00e0 trang \u0111\u00edch \u26d4 kh\u00f4ng c\u00f3 gi\u00e1</b>.
      Ph\u00e1t hi\u1ec7n v\u1ec1 <b>n\u1ed9i dung</b> &rarr; s\u1eeda post, th\u00eam khung gi\u00e1</td></tr>
    <tr class="hl"><td><b>Lu\u1ed3ng Q \u0111\u1ecdc ra</b></td><td>Xin s\u1ed1 tr\u01b0\u1edbc khi h\u1ecfi t\u00ecnh tr\u1ea1ng &rarr; tr\u01b0\u1ee3t <code>TC-5</code>.
      N\u00e9 gi\u00e1 hai l\u01b0\u1ee3t &rarr; <code>TC-9</code>? <b>Ch\u01b0a ch\u1eafc</b> \u2014 ph\u1ea3i tra xem b\u1ea3ng gi\u00e1 \u0111\u00e3 c\u1ea5p cho
      d\u00f2ng s\u1ee9 \u0111\u00f3 ch\u01b0a. \u0110\u00e3 c\u00f3 gi\u00e1 &rarr; <b>l\u1ed7i ng\u01b0\u1eddi</b>; ch\u01b0a c\u1ea5p &rarr; \u26d4 <b>l\u1ed7i h\u1ec7, kh\u00f4ng tr\u1eeb \u0111i\u1ec3m</b></td></tr>
  </tbody></table></div>
  <div class="note stop"><p style="margin-bottom:0"><b>\u26a0\ufe0f G\u1ed9p hai lu\u1ed3ng l\u00e0 \u00e9p ng\u01b0\u1eddi \u0111\u1ecdc ch\u1ecdn m\u1ed9t
    trong hai ngh\u0129a.</b> V\u00e0 trong th\u1ef1c t\u1ebf h\u1ecd lu\u00f4n ch\u1ecdn ngh\u0129a c\u1ee7a lu\u1ed3ng Q \u2014 v\u00ec n\u00f3 c\u00f3 t\u00ean ng\u01b0\u1eddi,
    nghe c\u1ee5 th\u1ec3 h\u01a1n. K\u1ebft qu\u1ea3: l\u1ed7i n\u1ed9i dung v\u00e0 l\u1ed7i h\u1ec7 th\u1ed1ng b\u1ecb ghi th\u00e0nh l\u1ed7i nh\u00e2n vi\u00ean,
    k\u1ef3 n\u00e0o c\u0169ng v\u1eady, v\u00e0 \u26d4 kh\u00f4ng ai s\u1eeda post.</p></div>
  <div class="tw"><table style="min-width:0"><tbody>
    <tr><td><b>\u26d4 Sai \u2014 l\u1ecdt t\u00ean</b></td><td><i>\u201cCh\u1ecb H\u00e0 tr\u1ea3 l\u1eddi \u2018b\u1ecdc s\u1ee9 kh\u00f4ng \u0111au v\u00e0 kh\u00f4ng h\u1ea1i g\u00ec\u2019 \u2014 sai\u201d</i></td></tr>
    <tr class="hl"><td><b>\u2705 \u0110\u00fang \u2014 \u1edf m\u1ee9c hi\u1ec7n t\u01b0\u1ee3ng</b></td><td><i>\u201c6/14 h\u1ed9i tho\u1ea1i nh\u00f3m <code>V-05</code> \u0111\u01b0\u1ee3c tr\u1ea3 l\u1eddi
      b\u1eb1ng t\u00ednh t\u1eeb tr\u1ea5n an thay v\u00ec c\u01a1 ch\u1ebf m\u00e0i r\u0103ng (<code>HT-004</code>, <code>HT-019</code>\u2026).
      Kh\u00e1ch h\u1ecfi l\u1ea1i l\u1ea7n hai r\u1ed3i r\u01a1i.\u201d</i><br><span class="dim">B\u1ea3n \u0111\u00fang <b>m\u1ea1nh h\u01a1n</b> b\u1ea3n sai:
      m\u1ed9t v\u1ea5n \u0111\u1ec1 n\u1ed9i dung s\u1eeda \u0111\u01b0\u1ee3c b\u1eb1ng m\u1ed9t tuy\u1ebfn b\u00e0i, thay v\u00ec v\u1ea5n \u0111\u1ec1 c\u1ee7a m\u1ed9t ng\u01b0\u1eddi
      v\u00e0 \u26d4 kh\u00f4ng n\u00f3i g\u00ec v\u1ec1 13 h\u1ed9i tho\u1ea1i c\u00f2n l\u1ea1i.</span></td></tr>
  </tbody></table></div>

  <h3 class="sub" style="margin:26px 0 10px"><span class="pre2">\u0110i\u1ec1u 2</span>An to\u00e0n tr\u01b0\u1edbc b\u00e1n h\u00e0ng \u2014 \u0111\u1ee9ng tr\u00ean m\u1ecdi m\u1ee5c kh\u00e1c</h3>
  <div class="note stop"><p><b>D\u1ea5u hi\u1ec7u an to\u00e0n</b> <i>(\u0111au \u00b7 s\u01b0ng \u00b7 \u00e1p xe \u00b7 tr\u1ee5 lung lay \u00b7 bi\u1ebfn ch\u1ee9ng \u00b7
    b\u1ec7nh n\u1ec1n \u00b7 thu\u1ed1c \u00b7 mang thai)</i> &rarr; <b>chuy\u1ec3n b\u00e1c s\u0129</b>, \u26d4 kh\u00f4ng t\u01b0 v\u1ea5n b\u00e1n,
    \u26d4 kh\u00f4ng b\u00e1o gi\u00e1, \u26d4 kh\u00f4ng b\u00e1n th\u00eam.</p>
    <p style="margin-bottom:0">\u2605 V\u00e0 <code>V-01</code> <i>\u201cl\u00e0m l\u1ea1i ca l\u1ed7i\u201d</i> c\u00f3 <b>hai lo\u1ea1i \u26d4 kh\u00f4ng gi\u1ed1ng nhau</b>:
    l\u00e0m \u1edf <b>n\u01a1i kh\u00e1c</b> = ca t\u01b0 v\u1ea5n m\u1edbi <i>(ch\u1ea5m b\u00ecnh th\u01b0\u1eddng)</i>; l\u00e0m <b>t\u1ea1i Paris</b> =
    <b>khi\u1ebfu n\u1ea1i</b> &rarr; <code>TC-5</code> v\u00e0 <code>TC-9</code> ch\u1ea5m <code>\u2014</code>.</p></div>
  <div class="tw"><table style="min-width:0"><tbody>
    <tr class="hl"><td><b>\u26d4 Ch\u1ea5m nh\u00e2n vi\u00ean v\u00ec \u201ckh\u00f4ng xin \u0111\u01b0\u1ee3c s\u1ed1\u201d trong m\u1ed9t ca khi\u1ebfu n\u1ea1i</b></td>
      <td>l\u00e0 <b>ch\u1ea5m sai vi\u1ec7c</b>. Nh\u00e2n vi\u00ean <b>\u0110\u00daNG</b> khi \u26d4 kh\u00f4ng b\u00e1n</td></tr>
    <tr><td><b>D\u1eef li\u1ec7u s\u1ee9c kho\u1ebb</b> \u2014 Lu\u1eadt 91/2025/QH15</td>
      <td>Ti\u1ec1n s\u1eed \u0111i\u1ec1u tr\u1ecb \u00b7 b\u1ec7nh n\u1ec1n \u00b7 thu\u1ed1c \u00b7 \u1ea3nh r\u0103ng \u00b7 phim X-quang \u00b7 ch\u1ea9n \u0111o\u00e1n n\u01a1i kh\u00e1c
      &rarr; ch\u1ec9 l\u01b0u <b>nh\u00e3n + c\u00e2u b\u1eb1ng ch\u1ee9ng ng\u1eafn</b> \u00b7 gi\u1edbi h\u1ea1n ng\u01b0\u1eddi xem \u00b7 c\u1ea7n \u0111\u1ed3ng \u00fd x\u1ee9 l\u00fd.
      \u2605 Nh\u00e2n vi\u00ean <b>ph\u1ea3i h\u1ecfi</b>, b\u00e1o c\u00e1o <b>ch\u1ec9 l\u01b0u nh\u00e3n</b></td></tr>
    <tr><td><b>\u201cCh\u00ednh h\u00e3ng\u201d l\u00e0 tuy\u00ean b\u1ed1 ph\u00e1p l\u00fd</b></td>
      <td>Ch\u1ec9 4 h\u00e3ng: <b>Straumann \u00b7 Invisalign \u00b7 Nacera \u00b7 Ormco</b>.
      G\u1eafn sai &rarr; c\u1edd <code>C\u0110-P2</code>, <code>TC-9</code> tr\u01b0\u1ee3t &rarr; <b>to\u00e0n h\u1ed9i tho\u1ea1i 0 \u0111i\u1ec3m</b></td></tr>
    <tr><td><b>Ba b\u00e1c s\u0129 \u0111\u01b0\u1ee3c n\u00eau t\u00ean</b></td>
      <td>TS-BS. \u0110\u00e0m Ng\u1ecdc Tr\u00e2m \u00b7 BS. H\u1ed3 Hi\u1ec7p Anh Tu\u1ea5n \u00b7 BS.CKI Nguy\u1ec5n Ng\u1ecdc Linh.
      T\u00ean kh\u00e1c &rarr; <code>C\u0110-P6</code> + \u26a0 c\u1ea7n x\u00e1c minh t\u1eeb Paris</td></tr>
    <tr><td><b>Ph\u1ec5u d\u1eebng \u1edf \u201c\u0110\u1ebeN KH\u00c1M\u201d</b></td>
      <td>\u26d4 Kh\u00f4ng ph\u1ea3i doanh thu \u2014 quy\u1ebft \u0111\u1ecbnh ti\u1ec1n th\u1eadt x\u1ea3y ra <b>tr\u00ean gh\u1ebf kh\u00e1m</b>,
      \u26d4 kh\u00f4ng trong inbox. \u2605 CTA m\u1ea1nh nh\u1ea5t: m\u1eddi <b>\u0111i kh\u00e1m + ch\u1ee5p phim</b>,
      nh\u1ea5n <i>\u201cch\u01b0a ph\u1ea3i \u0111i\u1ec1u tr\u1ecb\u201d</i></td></tr>
  </tbody></table></div>

  <h3 class="sub" style="margin:26px 0 10px"><span class="pre2">\u0110i\u1ec1u 3</span>B\u1ed1n c\u1ed5ng ch\u1eb7n \u2014 agent ph\u1ea3i d\u1eebng, \u26d4 kh\u00f4ng \u0111\u01b0\u1ee3c t\u1ef1 ch\u1ea1y qua</h3>
  <div class="tw"><table><thead><tr><th>C\u1ed5ng</th><th>Ch\u1eb7n g\u00ec</th><th>V\u00ec sao</th></tr></thead><tbody>
    <tr><td><b>C\u1ed4NG 0</b><br><span class="dim">lu\u1ed3ng I</span></td>
      <td>\u26d4 Kh\u00f4ng g\u00e1n ch\u00e2n dung, kh\u00f4ng vi\u1ebft th\u1ebb insight khi <b>b\u1ea3n ph\u00e1c h\u1ecda ch\u01b0a \u0111\u01b0\u1ee3c duy\u1ec7t</b></td>
      <td>H\u1ec7 \u26d4 kh\u00f4ng c\u00f3 b\u1ed9 ch\u00e2n dung m\u1eb7c \u0111\u1ecbnh. Chia kh\u00e1ch sai th\u00ec m\u1ecdi b\u1ea3ng sau \u0111\u1ec1u sai theo,
        v\u00e0 \u26d4 kh\u00f4ng ai nh\u00ecn ra v\u00ec b\u1ea3ng n\u00e0o c\u0169ng kh\u1edbp t\u1ed5ng</td></tr>
    <tr><td><b>C\u1ed4NG 1</b><br><span class="dim">lu\u1ed3ng I</span></td>
      <td>\u26d4 Kh\u00f4ng vi\u1ebft hook khi <b>ma tr\u1eadn \u01b0u ti\u00ean ch\u01b0a \u0111\u01b0\u1ee3c duy\u1ec7t</b></td>
      <td>Vi\u1ebft 30 hook cho \u0111\u00fang t\u1ec7p m\u00e0 kh\u1ed1i \u26d4 kh\u00f4ng \u0111\u1ecbnh l\u00e0m l\u00e0 n\u00e9m \u0111i m\u1ed9t tu\u1ea7n</td></tr>
    <tr><td><b>C\u1ed4NG 2</b><br><span class="dim">lu\u1ed3ng Q</span></td>
      <td>\u26d4 Kh\u00f4ng ph\u00e1t s\u1ed5 tay, kh\u00f4ng \u0111\u0103ng hook khi c\u00f2n <b>c\u1edd \U0001F534 ch\u01b0a g\u1ee1</b></td>
      <td>M\u1ed9t c\u00e2u <i>\u201cr\u0103ng s\u1ee9 d\u00f9ng tr\u1ecdn \u0111\u1eddi\u201d</i> trong s\u1ed5 tay s\u1ebd \u0111\u01b0\u1ee3c 20 nh\u00e2n vi\u00ean nh\u1eafn l\u1ea1i
        <b>nguy\u00ean v\u0103n</b> cho 300 kh\u00e1ch</td></tr>
    <tr class="hl"><td><b>C\u1ed4NG T</b> \u2605<br><span class="dim">c\u1ea3 hai lu\u1ed3ng</span></td>
      <td>\u26d4 Kh\u00f4ng xu\u1ea5t file n\u00e0o khi ch\u01b0a qua <b>6 c\u00e2u ki\u1ec3m t\u01b0\u1eddng ng\u0103n</b> \u2014 ch\u1ea1y <b>b\u1eb1ng m\u00e1y</b></td>
      <td>C\u1ed5ng ri\u00eang c\u1ee7a repo n\u00e0y. H\u00e0m <code>kiem_tuong_ngan()</code> <b>t\u1eeb ch\u1ed1i ghi file</b> n\u1ebfu tr\u01b0\u1ee3t.
        Ch\u1ea1y tay th\u00ec \u26d4 <b>s\u1ebd c\u00f3 k\u1ef3 qu\u00ean</b></td></tr>
  </tbody></table></div>
  <div class="note ok"><p style="margin-bottom:0">\u1ede m\u1ed7i c\u1ed5ng agent <b>in ra th\u1ee9 c\u1ea7n duy\u1ec7t r\u1ed3i d\u1eebng</b>.
    N\u1ebfu n\u00f3 t\u1ef1 ch\u1ea1y qua, nh\u1eafc: <i>\u201cD\u1eebng \u1edf C\u1ed4NG 0, in b\u1ea3n ph\u00e1c h\u1ecda ch\u00e2n dung ra cho t\u00f4i duy\u1ec7t\u201d</i>.</p></div>
</section>
''')

# ════ Muc 4 ════
SLOT = [
 (u"\U0001F534", u"\u2460", u"B\u1ea3ng gi\u00e1 theo t\u1eebng <b>d\u00f2ng tr\u1ee5 / d\u00f2ng s\u1ee9</b>",
  u"\u00d4 <code>?</code> c\u1ee7a <code>TC-9</code> \u00b7 c\u1edd <code>C\u0110-P5</code>", u"Marketing / K\u1ebf to\u00e1n", 1),
 (u"\U0001F534", u"\u2461", u"<b>S\u1ed1 n\u0103m b\u1ea3o h\u00e0nh</b> theo d\u1ecbch v\u1ee5",
  u"\u00d4 <code>\u2014</code> c\u1ee7a <code>TC-4</code> \u00b7 \u2605 c\u1edd <code>C\u0110-P8</code>", u"Khoa Chuy\u00ean m\u00f4n", 1),
 (u"\U0001F534", u"\u2462", u"Danh s\u00e1ch <b>case before\u2013after c\u00f3 gi\u1ea5y \u0111\u1ed3ng \u00fd</b>",
  u"\u2605 C\u1edd <code>C\u0110-P11</code> \u00b7 m\u1ecdi hook before\u2013after \u0111\u1ee9ng \U0001F7E0", u"Marketing + Ph\u00e1p ch\u1ebf", 1),
 (u"\U0001F7E0", u"\u2463", u"C\u01a1 s\u1edf \u0111\u1ee7 n\u0103ng l\u1ef1c <b>All-On / gh\u00e9p x\u01b0\u01a1ng</b>",
  u"\u0110\u1ecbnh tuy\u1ebfn kh\u00e1ch t\u1ec9nh \u2014 <b>ca \u0111\u1eaft nh\u1ea5t</b> (<code>V-02</code>)", u"V\u1eadn h\u00e0nh", 0),
 (u"\U0001F7E0", u"\u2464", u"S\u1ed1 <b>gi\u1ea5y x\u00e1c nh\u1eadn n\u1ed9i dung qu\u1ea3ng c\u00e1o</b>",
  u"M\u1ecdi hook c\u00f3 ph\u00e1t ng\u00f4n y khoa \u0111\u1ee9ng \U0001F7E0", u"Ph\u00e1p ch\u1ebf", 0),
 (u"\U0001F7E0", u"\u2465", u"\u0110i\u1ec1u ki\u1ec7n &amp; <b>l\u00e3i su\u1ea5t tr\u1ea3 g\u00f3p</b>",
  u"\u00d4 <code>\u2014</code> c\u1ee7a <code>TC-4</code> v\u1edbi r\u00e0o <code>L6.3</code>", u"K\u1ebf to\u00e1n", 0),
 (u"\U0001F7E0", u"\u2466", u"<b>M\u1ed1c KPI</b> (xin s\u1ed1 \u00b7 show-up \u00b7 ch\u1ed1t ph\u00e1c \u0111\u1ed3)",
  u"\u26d4 Kh\u00f4ng so \u0111\u01b0\u1ee3c <i>\u201c\u0111\u1ea1t / ch\u01b0a \u0111\u1ea1t\u201d</i>", u"Paris", 0),
]
A(u'''
<section class="sec" id="m4">
  <div class="sec-h"><span class="pre">M\u1ee5c 4</span><h2>\u0110ang ch\u1eb7n</h2>
    <span class="bar"></span><p>Agent c\u00e0i xong l\u00e0 ch\u1ea1y \u0111\u01b0\u1ee3c ngay. Nh\u01b0ng c\u00f3 <b>b\u1ea3y slot ph\u1ea3i c\u00f3 ng\u01b0\u1eddi c\u1ea5p
      d\u1eef ki\u1ec7n</b> th\u00ec n\u00f3 m\u1edbi d\u00f9ng \u0111\u01b0\u1ee3c th\u1eadt \u2014 \u26d4 kh\u00f4ng ph\u1ea3i vi\u1ec7c c\u1ee7a agent.</p></div>
  <div class="tw"><table><thead><tr><th>M\u1ee9c</th><th class="num">#</th><th>Slot</th><th>Ch\u1eb7n g\u00ec</th><th>Ai c\u1ea5p</th></tr></thead><tbody>''')
for muc, n, slot, chan, ai, hl in SLOT:
    A(u'<tr%s><td>%s</td><td class="num">%s</td><td>%s</td><td>%s</td><td>%s</td></tr>'
      % (u' class="hl"' if hl else u"", muc, n, slot, chan, ai))
A(u'''</tbody></table></div>
  <div class="note stop"><p style="margin-bottom:0"><b>\u2605 Slot \u2461 v\u00e0 \u2462 l\u00e0 hai slot sinh c\u1edd \u0111\u1ecf.</b>
    Nh\u00e2n vi\u00ean b\u1ecb kh\u00e1ch h\u1ecfi m\u00e0 h\u1ec7 ch\u01b0a c\u1ea5p d\u1eef ki\u1ec7n th\u00ec ch\u1ec9 c\u00f3 hai \u0111\u01b0\u1eddng: <b>im</b>
    (tr\u01b0\u1ee3t <code>TC-4</code>) ho\u1eb7c <b>n\u00f3i m\u1ed9t con s\u1ed1 nghe \u0111\u01b0\u1ee3c</b> (c\u1edd <code>C\u0110-P8</code> /
    <code>C\u0110-P11</code>). C\u1ea3 hai \u0111\u1ec1u b\u1ecb tr\u1eeb. \u26d4 <b>\u0110\u00e0o t\u1ea1o \u26d4 kh\u00f4ng ch\u1eefa \u0111\u01b0\u1ee3c vi\u1ec7c n\u00e0y</b> \u2014
    c\u1ea5p hai slot \u0111\u00f3 th\u00ec c\u1edd t\u1ef1 h\u1ebft.</p></div>
  <div class="note warn"><p style="margin-bottom:0"><b>\u26a0\ufe0f M\u1ed1c KPI ch\u01b0a \u0111\u01b0\u1ee3c Paris ch\u1ed1t th\u00ec ghi
    <code>\u26a0 ch\u01b0a c\u00f3 m\u1ed1c so s\u00e1nh</code></b> \u2014 \u26d4 tuy\u1ec7t \u0111\u1ed1i kh\u00f4ng t\u1ef1 \u0111\u1eb7t m\u1ed1c r\u1ed3i k\u1ebft lu\u1eadn
    <i>\u201c\u0111\u1ea1t / kh\u00f4ng \u0111\u1ea1t\u201d</i>. N\u0103m m\u1ed1c c\u00f3 s\u1ed1 trong <code>P8</code> \u00a77 l\u00e0 <b>m\u1ed1c k\u1ebf th\u1eeba t\u1eeb
    h\u1ec7 CSKH t\u1eadp \u0111o\u00e0n, ch\u01b0a \u0111\u01b0\u1ee3c Paris x\u00e1c nh\u1eadn cho ng\u00e0nh nha</b>.</p></div>
  <div class="note"><p style="margin-bottom:0"><b>\u23f8 Slot ch\u1edd \u2265 3 k\u1ef3 &rarr; \u0111\u01b0a l\u00ean \u0110\u1ea6U b\u00e1o c\u00e1o</b>,
    \u26d4 kh\u00f4ng \u0111\u1ec3 trong ph\u1ee5 l\u1ee5c.</p></div>
</section>
</main>
''')

# ─── footer ──────────────────────────────────────────────────
A(u'''
<footer>
  <div class="wrap">
    <p><b>Insight Dashboard Paris</b> \u00b7 v1.1 \u00b7 Nha khoa Paris \u00b7 <code>nhakhoaparis.vn</code> \u2014
      trang n\u00e0y sinh th\u1eb3ng t\u1eeb n\u1ed9i dung repo, n\u00ean n\u00fat Copy lu\u00f4n kh\u1edbp file ngu\u1ed3n.</p>
    <p style="margin-bottom:0">Trang n\u00e0y l\u00e0 h\u01b0\u1edbng d\u1eabn c\u00e0i \u0111\u1eb7t. N\u00f3 \u26d4 <b>kh\u00f4ng ch\u1ee9a d\u1eef li\u1ec7u kh\u00e1ch</b>
      v\u00e0 \u26d4 <b>kh\u00f4ng ch\u1ee9a t\u00ean nh\u00e2n vi\u00ean</b> \u2014 c\u00f9ng lu\u1eadt v\u1edbi m\u1ecdi \u0111\u1ea7u ra c\u1ee7a h\u1ec7. \u00b7
      <a href="REPO" target="_blank" rel="noopener">repo tr\u00ean GitHub</a></p>
  </div>
</footer>

<div class="toast" id="toast" role="status" aria-live="polite"></div>
'''.replace(u"REPO", REPO))

# ─── payload + script ────────────────────────────────────────
js_payload = json.dumps(P, ensure_ascii=False)
js_payload = js_payload.replace(u"</", u"<" + chr(92) + u"/")
A(u'<script id="payload" type="application/json">' + js_payload + u"</script>")

A(u'''<script>
(function(){
  "use strict";
  var DATA = {};
  try { DATA = JSON.parse(document.getElementById("payload").textContent); } catch(e){}

  document.querySelectorAll("[data-peek]").forEach(function(pre){
    var t = DATA[pre.dataset.peek];
    if (t === undefined) return;
    pre.textContent = t.length > 2600
      ? t.slice(0, 2600) + NLNL + "\u2026 (c\u00f2n " + (t.length - 2600).toLocaleString("vi-VN") +
        " k\u00fd t\u1ef1 \u2014 b\u1ea5m Copy \u0111\u1ec3 l\u1ea5y \u0111\u1ee7)"
      : t;
  });

  var toast = document.getElementById("toast"), tid;
  function khoe(msg){
    toast.textContent = msg;
    toast.classList.add("on");
    clearTimeout(tid);
    tid = setTimeout(function(){ toast.classList.remove("on"); }, 1800);
  }

  document.addEventListener("click", function(ev){
    var b = ev.target.closest("[data-copy]");
    if (!b) return;
    var t = DATA[b.dataset.copy];
    if (t === undefined) return;
    var xong = function(){
      var cu = b.textContent;
      b.textContent = "\u2713 \u0110\u00e3 copy";
      b.classList.add("done");
      khoe("\u0110\u00e3 copy " + t.length.toLocaleString("vi-VN") + " k\u00fd t\u1ef1");
      setTimeout(function(){ b.textContent = cu; b.classList.remove("done"); }, 1800);
    };
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(t).then(xong, function(){
        khoe("Tr\u00ecnh duy\u1ec7t ch\u1eb7n copy \u2014 b\u1ea5m Xem n\u1ed9i dung r\u1ed3i copy tay");
      });
    } else {
      var ta = document.createElement("textarea");
      ta.value = t;
      ta.style.position = "fixed";
      ta.style.opacity = "0";
      document.body.appendChild(ta);
      ta.select();
      try { document.execCommand("copy"); xong(); }
      catch (err) { khoe("\u26d4 Kh\u00f4ng copy \u0111\u01b0\u1ee3c \u2014 b\u1ea5m Xem n\u1ed9i dung r\u1ed3i copy tay"); }
      document.body.removeChild(ta);
    }
  });

  document.querySelectorAll(".tab").forEach(function(b){
    b.addEventListener("click", function(){
      document.querySelectorAll(".tab").forEach(function(x){
        x.setAttribute("aria-selected", String(x === b));
      });
      document.querySelectorAll(".tabpanel").forEach(function(p){
        p.hidden = p.dataset.panel !== b.dataset.tab;
      });
    });
  });

  document.querySelectorAll(".qa-bar button").forEach(function(b){
    b.addEventListener("click", function(){
      var f = b.dataset.f;
      document.querySelectorAll(".qa-bar button").forEach(function(x){
        x.setAttribute("aria-pressed", String(x === b));
      });
      document.querySelectorAll(".prompt").forEach(function(p){
        p.hidden = (f !== "all" && p.dataset.g !== f);
      });
    });
  });

  var root = document.documentElement, nut = document.getElementById("theme");
  var khoa = "hd-theme-insightdashboard-paris";
  try { var luu = localStorage.getItem(khoa); if (luu) root.setAttribute("data-theme", luu); } catch(e){}
  nut.addEventListener("click", function(){
    var toi = root.getAttribute("data-theme") === "dark"
      || (!root.getAttribute("data-theme") && matchMedia("(prefers-color-scheme:dark)").matches);
    var moi = toi ? "light" : "dark";
    root.setAttribute("data-theme", moi);
    try { localStorage.setItem(khoa, moi); } catch(e){}
  });
})();
</script>
</body></html>
'''.replace(u"NLNL", u'String.fromCharCode(10) + String.fromCharCode(10) + '))

htm = NL.join(o)
io.open(OUT, "w", encoding="utf-8", newline="").write(htm)
print("viet", OUT)
print("kich thuoc:", len(htm.encode("utf-8")), "byte")
print("so khoa payload:", len(P))
