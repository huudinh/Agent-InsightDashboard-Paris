#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
pd.py — Agent-InsightDashboard-Paris

MOT LAN DOC, HAI LUONG:

    hoi-thoai.md  --doc-->  out/doc-hoi-thoai.json   (bang du kien goc)
                                    |
                      +-------------+-------------+
                      |                           |
                 --insight-->                --qc-->
            out/bao-cao-insight.json     out/bao-cao-qc.json
            (ve KHACH, KHONG ten NV)     (ve NHAN VIEN)

TUONG NGAN (pd-F): khong file nao chua CA ten nhan vien LAN loi khach.
Ham kiem_tuong_ngan() chay 6 cau kiem va TU CHOI GHI FILE neu truot.
Do la ly do moi lan ghi JSON deu di qua ghi_json(), khong qua json.dump truc tiep.

Lenh:
    python tools/pd.py doc     du-lieu/hoi-thoai.md --ky "01-15/11"
    python tools/pd.py insight --ky "01-15/11"
    python tools/pd.py qc      --ky "01-15/11"
    python tools/pd.py ads     du-lieu/ads-facebook.csv --ky "01-15/11"
    python tools/pd.py kiem    out/bao-cao-insight.json
"""

import io
import os
import re
import sys
import json
import csv
import argparse
import unicodedata
from datetime import datetime

# Console Windows mac dinh cp1252 -> tieng Viet no. Ep UTF-8 truoc khi in.
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

GOC = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(GOC, "out")
SO_TAY = os.path.join(GOC, "so-tay")

with io.open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "tu_dien.json"),
             encoding="utf-8") as _f:
    TD = json.load(_f)


# ────────────────────────────────────────────────────────────────────
# 0 · TIEN ICH
# ────────────────────────────────────────────────────────────────────

def khong_dau(s):
    """Bo dau tieng Viet, ve chu thuong. Dung de khop tu khoa."""
    s = unicodedata.normalize("NFD", s or "")
    s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    return s.replace("đ", "d").replace("Đ", "D").lower()


_RE_CACHE = {}


def _re_tu(tu):
    """Tra ve (regex, co_dau) — regex khop tu khoa THEO RANH GIOI TU.

    Hai luat, ca hai deu ra tu loi THAT phat hien khi chay thu:

    ① ⛔ KHONG DUNG `in`. Tu khoa "hô" (V-04) bo dau thanh "ho", ma "ho" nam
       trong "hỏi", "hôm", "cho", "chỗ" -> V-04 NUOT 9/16 hoi thoai: cao voi,
       boc su, veneer, mat rang deu bi gan thanh "nieng".

    ② TU MOT AM TIET phai khop CO DAU. Bo dau thi "đau" (pain) va "đâu" (where)
       deu thanh "dau" -> "cao voi o ĐÂU a" bi cham thanh dau cap (V-06),
       keo theo nhom khach N4 va luat ghi de "toi thieu WARM".
       Tu tu hai am tiet tro len thi va cham gan nhu khong xay ra, nen van
       khop bo dau de chiu duoc viec khach go thieu dau.

    Ca hai deu la LOI IM LANG: moi bang van khop tong, bieu do van dep,
    ket luan sai hoan toan — dung loai ma pd-I1 §1 canh bao.
    """
    r = _RE_CACHE.get(tu)
    if r is None:
        goc = (tu or "").strip().lower()
        co_dau = len(goc.split()) == 1
        nen = goc if co_dau else khong_dau(goc)
        # "\\s+(?:\\d+\\s+)?" cho phep con so chen giua: "mat 2 rang", "boc 4 rang"
        than = r"\s+(?:\d+\s+)?".join(re.escape(x) for x in nen.split())
        r = (re.compile(r"(?<![0-9a-zà-ỹ])" + than + r"(?![0-9a-zà-ỹ])", re.U), co_dau)
        _RE_CACHE[tu] = r
    return r


def chua(text, tu_list):
    """Co cum nao trong tu_list xuat hien trong text? Tra ve cum dau tien."""
    t_kd, t_co = khong_dau(text), (text or "").lower()
    for tu in tu_list or []:
        rx, co_dau = _re_tu(tu)
        if rx.search(t_co if co_dau else t_kd):
            return tu
    return None


def tat_ca_cum(text, tu_list):
    t_kd, t_co = khong_dau(text), (text or "").lower()
    ra = []
    for tu in tu_list or []:
        rx, co_dau = _re_tu(tu)
        if rx.search(t_co if co_dau else t_kd):
            ra.append(tu)
    return ra


def cau_cua(text):
    """Tach text thanh tung cau — dung cho cac co do can xet TRONG CUNG MOT CAU."""
    return [c.strip() for c in re.split(r"[.!?;\n]+", text or "") if c.strip()]


def phut(ngay, gio):
    """'03/11' + '09:12' -> so phut tu dau nam (du de tru hai moc trong mot ky)."""
    try:
        d, m = int(ngay[:2]), int(ngay[3:5])
        h, p = int(gio[:2]), int(gio[3:5])
    except (ValueError, IndexError):
        return None
    return ((m * 31 + d) * 24 + h) * 60 + p


def trong_gio(gio):
    """pd-E §5 — gio lam 8h30-18h30. Ngoai khung -> TC-1 cham '—'."""
    try:
        h, p = int(gio[:2]), int(gio[3:5])
    except (ValueError, IndexError):
        return True
    gio_thap = h + p / 60.0
    return TD["gio_lam"]["mo"] <= gio_thap <= TD["gio_lam"]["dong"]


def nap_json(ten):
    p = os.path.join(OUT, ten)
    if not os.path.exists(p):
        return None
    with io.open(p, encoding="utf-8") as f:
        return json.load(f)


def bay_gio():
    return datetime.now().astimezone().replace(microsecond=0).isoformat()


# ────────────────────────────────────────────────────────────────────
# 1 · DOC FILE HOI THOAI  (khuon Paris, pd-B §2)
# ────────────────────────────────────────────────────────────────────

RE_DAU = re.compile(r"^##\s*(\d+)\s*\.\s*(.+?)\s*[—–-]\s*(\d{2}/\d{2})\s+(\d{2}:\d{2})\s*$")
RE_META = re.compile(r"^-\s*Ph[ụu]\s*tr[áa]ch\s*:\s*(.+?)\s*[·|]\s*C[óo]\s*S[ĐD]T\s*:\s*(C[óo]|Kh[ôo]ng)", re.I)
RE_TIN = re.compile(
    r"^-\s*\*\*\s*(\d{2}/\d{2})\s+(\d{2}:\d{2})\s+(KH|NV)\s*(?:\(([^)]*)\))?\s*:\s*\*\*\s*(.*)$")
RE_THE = re.compile(r"\[Th[ẻe]\s*:\s*Inbox t[ừu] qu[ảa]ng c[áa]o\s*([^\s–—-]+)\s*[–—-]\s*(.+?)\]", re.I)
RE_DINH_KEM = re.compile(r"\[(?:[ẢA]nh|T[ệe]p|Th[ẻe]\s*:[^\]]*)\]", re.I)
RE_GHI_CHU = re.compile(r"^-\s*Ghi ch[úu]\s*:", re.I)


def doc_file_hoi_thoai(path):
    """Tra ve (danh_sach_ht, co_ghi_chu_ban_giao)."""
    with io.open(path, encoding="utf-8") as f:
        dong = f.read().split("\n")

    ds, cur, co_ghi_chu = [], None, False
    for ln in dong:
        m = RE_DAU.match(ln)
        if m:
            if cur:
                ds.append(cur)
            cur = {"stt": int(m.group(1)), "ngay": m.group(3), "gio_mo": m.group(4),
                   "nv": "", "co_sdt": False, "tin": [], "ghi_chu": ""}
            continue
        if cur is None:
            continue
        m = RE_META.match(ln)
        if m:
            cur["nv"] = m.group(1).strip()
            cur["co_sdt"] = khong_dau(m.group(2)).startswith("co")
            continue
        if RE_GHI_CHU.match(ln):
            co_ghi_chu = True
            cur["ghi_chu"] = ln.split(":", 1)[1].strip()
            continue
        m = RE_TIN.match(ln)
        if m:
            noi_dung = m.group(5).strip()
            cur["tin"].append({
                "ngay": m.group(1), "gio": m.group(2),
                "ai": m.group(3).upper(),
                "nv": (m.group(4) or "").strip(),
                "noi_dung": noi_dung,
                # chu THAT khach go — bo [Anh]/[Tep]/[The:...] (pd-B §2)
                "chu_that": RE_DINH_KEM.sub(" ", noi_dung).strip(),
                "co_dinh_kem": bool(RE_DINH_KEM.search(noi_dung)),
            })
    if cur:
        ds.append(cur)

    for ht in ds:
        ht["ma"] = "HT-%03d" % ht["stt"]
        ht["kh"] = [t for t in ht["tin"] if t["ai"] == "KH"]
        # ★ [Thẻ:]/[Ảnh]/[Tệp] ⛔ KHONG phai chu khach go (pd-B §2) -> khong tinh
        # la mot luot khach. Dung kh_that cho: dem luot · cau hoi dau · moc TC-1.
        ht["kh_that"] = [t for t in ht["kh"] if t["chu_that"]]
        ht["nv_tin"] = [t for t in ht["tin"] if t["ai"] == "NV"]
        ht["loi_kh"] = " \n".join(t["chu_that"] for t in ht["kh"])
        ht["loi_nv"] = " \n".join(t["chu_that"] for t in ht["nv_tin"])
        the = None
        for t in ht["tin"]:
            the = RE_THE.search(t["noi_dung"])
            if the:
                break
        ht["post_ads"] = the.group(1).strip() if the else ""
        ht["loi_hua_post"] = the.group(2).strip() if the else ""
        if not ht["nv"] and ht["nv_tin"]:
            ht["nv"] = ht["nv_tin"][0]["nv"]
    return ds, co_ghi_chu


def ly_do_loai(ht):
    """pd-B §7 — ghi ro, ⛔ khong am tham bo."""
    if not ht["kh"] or not ht["loi_kh"].strip():
        return "khong-co-loi-khach"
    t = khong_dau(ht["loi_kh"])
    for cum in ["tuyen dung", "xin viec", "ban hang", "hop tac quang cao",
                "cho thue", "ban nha", "vay von"]:
        if cum in t:
            return "ngoai-pham-vi"
    if not ht["nv_tin"] and len(ht["kh_that"]) == 1:
        return "chua-duoc-cham"   # ★ phat hien, KHONG phai rac
    if not ht["nv_tin"]:
        return "chua-duoc-cham"
    return None


# ────────────────────────────────────────────────────────────────────
# 2 · GAN MA  (bo ma cua Paris-Agent-Factory — pd-A §3)
# ────────────────────────────────────────────────────────────────────

def gan_v_rang(loi_kh):
    """P4 §2 — xet THEO THU TU V-01 -> V-11, dung nhom dau tien thi lay."""
    for ma in TD["v_rang"]["_thu_tu"]:
        if ma.startswith("_"):
            continue
        if chua(loi_kh, TD["v_rang"][ma]["tu"]):
            return ma
    return "V-11"


def gan_nhom_gt(v_rang, loi_kh):
    gt = TD["v_rang"][v_rang]["gt"] or ""
    if chua(loi_kh, TD["nhom_gt"]["nang_len_v1"]["tu"]):
        return "V1"
    return gt or "V3"


def gan_tinh(loi_kh):
    """Tra ve (tinh, ngoai_7_tinh). pd-E §5."""
    for t in TD["tinh_co_so"]["ngoai_hay_gap"]:
        if chua(loi_kh, [t]):
            return t, True
    for t in TD["tinh_co_so"]["co"]:
        if chua(loi_kh, [t]):
            return t, False
    return "", None


def gan_l_code(ht, loi_kh, loi_nv):
    """P6 §2. Xet L6.x truoc, roi L4.1, roi L2.x, mac dinh L1.1."""
    ds_rao = []
    for ma in ["L6.7", "L6.5", "L6.3", "L6.4", "L6.6", "L6.2"]:
        if chua(loi_kh, TD["l_code"][ma]["tu"]):
            ds_rao.append(ma)

    tinh, ngoai = gan_tinh(loi_kh)
    # pd-E §5: NGOAI 7 tinh + noi xa -> L2.5. TRONG 7 tinh ma bao xa -> L6.4.
    if ngoai is True and chua(loi_kh, TD["l_code"]["L6.4"]["tu"] + ["xa", "o tinh"]):
        return "L2.5", ds_rao, tinh

    if ds_rao:
        return ds_rao[0], ds_rao, tinh

    if ht["co_sdt"] and gan_v_rang(loi_kh) != "V-11":
        return "L4.1", ds_rao, tinh
    if chua(loi_kh, TD["l_code"]["L2.4"]["tu"]):
        return "L2.4", ds_rao, tinh
    if ht["nv_tin"] and len(ht["kh"]) >= 2:
        return "L2.1", ds_rao, tinh
    if ht["nv_tin"]:
        return "L2.3", ds_rao, tinh
    return "L1.1", ds_rao, tinh


def gan_rao_can(ds_l6):
    """P2 §2 — quy moi L6.x ve SO / NGO / NGAI. Mot HT mang duoc 2-3 rao."""
    rao = []
    for ma in ds_l6:
        r = TD["l_code"].get(ma, {}).get("rao", "")
        for x in r.split("+"):
            x = x.strip()
            if x and x != "?" and x not in rao:
                rao.append(x)
    return rao


def gan_giai_doan(ht, v_rang, ds_l6, loi_kh):
    """P3 §1 — chi dung S1 · S2 · S3 · CS."""
    t = khong_dau(loi_kh)
    for cum in ["dang nieng", "da trong", "sieu nieng", "siet nieng", "tai kham",
                "da lam o paris", "cham soc sau", "da boc su roi"]:
        if cum in t:
            return "CS"
    if ds_l6:
        return "S3"
    if ht["kh"] and ht["kh"][0]["co_dinh_kem"]:
        return "S2"
    if v_rang == "V-11":
        return "S1"
    if chua(loi_kh, TD["tc"]["TC-3_thu_thong_tin"]["vi_tri_thoi_gian"]) or len(ht["kh"]) >= 3:
        return "S2"
    return "S1"


N6_TRE_CA_NHA = ["cho con", "cho bé", "con em", "bé nhà em", "cháu em", "con gái em",
                 "con trai em", "răng sữa", "cả nhà", "gia đình em", "gói gia đình",
                 "bé", "trẻ em", "niềng cho con"]


def gan_nhom_khach(v_rang, loi_kh, dau_gd):
    """P2 §3 — N1..N6. Xet HEP truoc (N5, N4, N6) roi moi den nhom rong.

    ⚠ N6 ⛔ KHONG phai "co nhac nguoi nha". Con nhan cho BO 68 tuoi mat ca ham
    thi benh nhan dung chan dung N1 ("45-70 tuoi, mat 1 rang den ca ham...
    nhac nguoi nha di cung" — P2 §3). N6 la TRE EM / CA NHA.
    Dau hieu nguoi thu ba van duoc giu rieng o cot `dau_gia_dinh`.
    """
    if v_rang == "V-01":
        return "N5"
    if v_rang == "V-06":
        return "N4"
    if v_rang == "V-10" or chua(loi_kh, N6_TRE_CA_NHA):
        return "N6"
    _ = dau_gd
    if v_rang in ("V-02", "V-03"):
        return "N1"
    if v_rang == "V-04":
        return "N3"
    if v_rang in ("V-05", "V-09"):
        return "N2"
    return ""


# ────────────────────────────────────────────────────────────────────
# 3 · DO NONG  (P8 §1 — bitmask 5 chu so + 3 luat ghi de)
# ────────────────────────────────────────────────────────────────────

def cham_bitmask(ht, v_rang, loi_kh):
    th = TD["tin_hieu_nong"]
    s1 = v_rang != "V-11"
    s2 = bool(chua(loi_kh, th["2_moc_thoi_gian"]))
    s3 = bool(chua(loi_kh, th["3_hoi_theo_ca_minh"]))
    s4 = any(t["co_dinh_kem"] for t in ht["kh"]) or bool(chua(loi_kh, th["4_gui_anh_mo_ta"]))
    s5 = bool(ht["co_sdt"])
    return [s1, s2, s3, s4, s5]


def gan_do_nong(bits, v_rang, loi_kh):
    """Tra ve (do_nong, do_nong_sao, ghi_de).

    do_nong_sao = cham lai KHONG ke tin hieu (1) — luat chong lap vong,
    pd-I2 §4. Dat >=3/4 trong (2)(3)(4)(5) thi la HOT*.
    """
    diem = sum(1 for b in bits if b)
    nong = "HOT" if diem >= 4 else ("WARM" if diem >= 2 else "COLD")

    gd = TD["ghi_de_nong"]
    ghi_de = ""
    if chua(loi_kh, gd["hot_da_dat_lich"]):
        nong, ghi_de = "HOT", "da dat lich / dang den"
    elif chua(loi_kh, gd["hot_da_co_phim"]):
        # ★ Luat de bo sot nhat va dat nhat: khach da qua giai doan chan doan.
        nong, ghi_de = "HOT", "da co phim / da kham noi khac"
    elif v_rang == "V-06" and nong == "COLD":
        nong, ghi_de = "WARM", "dau cap -> toi thieu WARM"

    diem_sao = sum(1 for b in bits[1:] if b)
    sao = "HOT*" if diem_sao >= 3 else ("WARM*" if diem_sao >= 2 else "COLD*")
    return nong, sao, ghi_de


# ────────────────────────────────────────────────────────────────────
# 4 · CO DO PHAP CHE  (pd-Q2 §2 — 11 co)
# ────────────────────────────────────────────────────────────────────

HA_THAP = ["khong tot", "re vi", "hang kem", "dung lam o", "hay loi", "te hon", "kem hon"]
RE_BAC_SI = re.compile(r"(?:b[áa]c s[ĩi]|bs|ts|th[ạa]c s[ĩi])\.?\s+"
                       r"((?:[A-ZĐÀÁÂÃÈÉÊÌÍÒÓÔÕÙÚĂĨŨƠƯĂẠ-ỹ][\wÀ-ỹ]*\s*){2,4})", re.U)


def mien_tru(ma, cau):
    """★ Cau mien tru — nhan vien NOI VE viec do de TU CHOI / HOAN theo dung quy trinh.

    Vi du that: "ve anh case thi em xin phep xac nhan lai danh sach anh duoc phep
    su dung roi gui chi, vi anh khach phai co su dong y cua ho" — day la lam DUNG,
    nhung cum "anh case" lai khop CD-P11.

    Gan co do cho nguoi LAM DUNG la loi te nhat ma repo nay co the sinh ra
    (pd-Q1 §6 rao ③). Nen moi lan bat co phai di qua ham nay.
    """
    mt = TD.get("mien_tru_co_do", {})
    return bool(chua(cau, mt.get("chung", [])) or chua(cau, mt.get(ma, [])))


def soat_co_do(loi_nv):
    """Tra ve list dict: {ma, nguyen_van}. Ba co bat bang LOGIC, khong bang tu khoa."""
    ra = []

    def gan(ma, cau):
        if not mien_tru(ma, cau):
            ra.append({"ma": ma, "nguyen_van": cau})

    for c in cau_cua(loi_nv):
        kd = khong_dau(c)

        # --- CD-P2: "chinh hang" ma KHONG co ten hang duoc duyet trong CUNG CAU
        if chua(c, TD["co_do"]["CĐ-P2"]["tu"]):
            if not chua(c, TD["hang_duyet"]["ten"]):
                gan("CĐ-P2", c)

        # --- CD-P6: ten sau "bac si" ma khong nam trong 3 bac si duoc duyet
        for m in RE_BAC_SI.finditer(c):
            ten = m.group(1).strip()
            if len(khong_dau(ten).split()) < 2:
                continue
            if not chua(ten, TD["bac_si_duyet"]["ten"]):
                gan("CĐ-P6", c)
                break
        else:
            if chua(c, TD["co_do"]["CĐ-P6"]["tu"]):
                gan("CĐ-P6", c)

        # --- CD-P9: ten doi thu + tu ha thap trong cung cau
        if chua(c, TD["doi_thu"]["ten"]) and chua(c, HA_THAP):
            gan("CĐ-P9", c)

        # --- cac co con lai: bat bang tu khoa
        for ma in ["CĐ-P1", "CĐ-P3", "CĐ-P4", "CĐ-P5", "CĐ-P7", "CĐ-P8", "CĐ-P10", "CĐ-P11"]:
            if chua(c, TD["co_do"][ma]["tu"]):
                gan(ma, c)

        if chua(c, TD["co_do"]["CĐ-P9"]["tu"]):
            gan("CĐ-P9", c)
        _ = kd

    # bo trung theo (ma, nguyen_van)
    thay, sach = set(), []
    for c in ra:
        k = (c["ma"], c["nguyen_van"])
        if k not in thay:
            thay.add(k)
            sach.append(c)
    return sach


# ────────────────────────────────────────────────────────────────────
# 5 · CHAM 10 TIEU CHI  (pd-Q1 §3 — anh xa 1:1 voi P8 §6)
# ────────────────────────────────────────────────────────────────────

XIN_SO = ["xin s[ốo]", "[đd]ể l[ạa]i s[ốo]", "cho em xin", "s[ốo] [đd]i[ệe]n tho[ạa]i",
          "s[ốo] c[óo] zalo", "xin zalo"]


def cham_tc(ht, v_rang, ds_l6, co_ghi_chu, co_do):
    """Tra ve (tc_dict, bang_chung_dict, ghi_chu_he_list).

    ✓ dat · ✗ chua dat · — khong ap dung HOAC loi he · ? cho doi chieu.
    pd-Q1 §2: — va ? LOAI KHOI MAU SO, ⛔ khong tinh la truot.
    """
    tc, bc, he = {}, {}, []
    loi_kh, loi_nv = ht["loi_kh"], ht["loi_nv"]
    tcd = TD["tc"]

    # ── TC-1 · phan hoi <= 2' (chi trong 8h30-18h30; ngoai gio -> '—')
    if not ht["nv_tin"]:
        tc["TC-1"] = "—"
        he.append("khong co luot NV nao")
    elif not trong_gio((ht["kh_that"][0]["gio"] if ht["kh_that"] else ht["gio_mo"])):
        tc["TC-1"] = "—"
        he.append("khach nhan ngoai gio 8h30-18h30")
    else:
        k0 = ht["kh_that"][0] if ht["kh_that"] else None
        t0 = phut(k0["ngay"], k0["gio"]) if k0 else None
        t1 = phut(ht["nv_tin"][0]["ngay"], ht["nv_tin"][0]["gio"])
        if t0 is None or t1 is None:
            tc["TC-1"] = "—"
        elif t1 < t0:
            # Dau thoi gian NV som hon khach -> ban xuat loi ngay, ⛔ khong cham oan
            tc["TC-1"] = "—"
            he.append("dau thoi gian loi: tin NV som hon tin khach")
        else:
            d = t1 - t0
            tc["TC-1"] = "✓" if d <= TD["gio_lam"]["sla_phut"] else "✗"
            if tc["TC-1"] == "✗":
                bc["TC-1"] = ["tin dau khach %s, NV tra loi %s — cham %d phut"
                              % (k0["gio"], ht["nv_tin"][0]["gio"], d)]

    # ── TC-2 · goi dung ten dich vu theo post khach bam vao
    if not ht["nv_tin"]:
        tc["TC-2"] = "—"
    else:
        mo = ht["nv_tin"][0]["chu_that"]
        goi_dung = False
        if v_rang != "V-11" and chua(mo, TD["v_rang"][v_rang]["tu"]):
            goi_dung = True
        if ht["loi_hua_post"] and chua(mo, ht["loi_hua_post"].split()[:6]):
            goi_dung = True
        tc["TC-2"] = "✓" if goi_dung else "✗"
        if not goi_dung:
            bc["TC-2"] = ["tin mo cua NV: " + mo[:160]]

    # ── TC-3 · thu du 4 thong tin  (P8 §6 (3) — nganh nha can 4, khong phai 2)
    if not ht["nv_tin"]:
        tc["TC-3"] = "—"
    else:
        # ★ "THU DU 4 thong tin" = thong tin THU DUOC, bat ke NV hoi hay khach tu noi.
        # Khop tren ca hai nua hoi thoai, neu khong se cham 0% oan cho ca khoi.
        ca_hai = loi_nv + "\n" + loi_kh
        thieu = [k for k, tu in tcd["TC-3_thu_thong_tin"].items()
                 if not k.startswith("_") and not chua(ca_hai, tu)]
        tc["TC-3"] = "✓" if not thieu else "✗"
        if thieu:
            bc["TC-3"] = ["thieu: " + ", ".join(thieu)]

    # ── TC-4 · tao tin cay bang BANG CHUNG THAT, dung rao can khach mang
    mien = TD["mien_tc"]
    hoi_slot = (chua(loi_kh, mien["hoi_bao_hanh"]) or chua(loi_kh, mien["xin_anh_case"])
                or chua(loi_kh, mien["hoi_benh_nen"]) or chua(loi_kh, mien["hoi_tra_gop"]))
    that = tat_ca_cum(loi_nv, tcd["TC-4_bang_chung"]["that"])
    if that:
        tc["TC-4"] = "✓"
        bc["TC-4"] = ["bang chung: " + ", ".join(that[:4])]
    elif hoi_slot:
        # ★ pd-Q1 §4 — LOI HE: he chua cap du kien thi ⛔ khong tru diem nguoi
        tc["TC-4"] = "—"
        he.append("khach hoi du kien he chua cap (%s)" % hoi_slot)
    elif ds_l6:
        tc["TC-4"] = "✗"
        tt = tat_ca_cum(loi_nv, tcd["TC-4_bang_chung"]["tinh_tu_tran_an"])
        bc["TC-4"] = ["khach mang rao %s; NV chi dung tinh tu: %s"
                      % (",".join(ds_l6), ", ".join(tt[:3]) or "(khong co bang chung nao)")]
    else:
        tc["TC-4"] = "—"

    # ── TC-5 · xin so co ly do CO LOI CHO KHACH
    co_xin = re.search("|".join(XIN_SO), khong_dau(loi_nv).replace("đ", "d"), re.I) \
        or chua(loi_nv, ["xin so", "de lai so", "cho em xin", "so co zalo"])
    if not co_xin:
        tc["TC-5"] = "—"
    elif chua(loi_nv, tcd["TC-5_ly_do_xin_so"]["co_loi_cho_khach"]):
        tc["TC-5"] = "✓"
    else:
        tc["TC-5"] = "✗"
        bc["TC-5"] = ["xin so khong co ly do co loi cho khach: "
                      + (chua(loi_nv, tcd["TC-5_ly_do_xin_so"]["khong_dat"]) or "")]

    # ── TC-6 · xac thuc so / Zalo  (chi xet khi co so)
    if not ht["co_sdt"]:
        tc["TC-6"] = "—"
    else:
        tc["TC-6"] = "✓" if chua(loi_nv, tcd["TC-6_xac_thuc_so"]) else "✗"

    # ── TC-7 · phan loai  &  TC-8 · phieu ban giao 13 truong
    # ★ pd-Q1 §4: ban xuat KHONG co ghi chu -> ca hai la '—' cho MOI hoi thoai.
    if not co_ghi_chu:
        tc["TC-7"] = tc["TC-8"] = "—"
        he.append("ban xuat khong co ghi chu ban giao -> TC-7, TC-8 khong do duoc")
    else:
        g = ht.get("ghi_chu", "")
        tc["TC-7"] = "✓" if chua(g, ["hot", "warm", "cold", "v1", "v2", "v3"]) else "✗"
        tc["TC-8"] = "✓" if len([x for x in g.split("·") if x.strip()]) >= 13 else "✗"

    # ── TC-9 · khong tu cam · khong "chinh hang" sai · khong chot gia cung
    if co_do:
        tc["TC-9"] = "✗"
        bc["TC-9"] = [c["ma"] + ": " + c["nguyen_van"][:160] for c in co_do[:2]]
    elif chua(loi_kh, TD["hoi_gia"]["tu"]):
        ne = chua(loi_nv, TD["ne_gia"]["cau_ne"])
        co_khung = re.search(r"\d[\d.,]*\s*(tri[ệe]u|tr\b|k\b|vn[đd])", khong_dau(loi_nv))
        if co_khung:
            # Neu gia gan voi dong tru/dong su -> can doi chieu bang gia (o '?')
            if chua(loi_kh + " " + loi_nv, ["dong su", "nacera", "zirconia", "cercon",
                                            "emax", "loai tru", "dong tru", "straumann"]):
                tc["TC-9"] = "?"
                bc["TC-9"] = ["NV neu gia gan dong tru/dong su — can doi chieu bang gia hien hanh"]
            else:
                tc["TC-9"] = "✓"
        elif ne:
            # ★ pd-E §6: gia DA CONG KHAI -> ne han la LOI NGUOI, khong phai loi he
            tc["TC-9"] = "✗"
            bc["TC-9"] = ["khach hoi gia; NV ne: " + ne + " (gia da cong khai tai /hoan-my-bang-gia...)"]
        else:
            tc["TC-9"] = "✗"
            bc["TC-9"] = ["khach hoi gia, NV khong neu khung gia va khong noi vi sao chua neu duoc"]
    else:
        tc["TC-9"] = "✓"

    # ── TC-10 · neu ro buoc tiep theo (ai goi · so nao · luc may gio)
    if not ht["co_sdt"]:
        tc["TC-10"] = "—"
    else:
        tc["TC-10"] = "✓" if chua(loi_nv, tcd["TC-10_buoc_tiep"]) else "✗"
        if tc["TC-10"] == "✗":
            bc["TC-10"] = ["co so nhung khong neu ai goi / luc may gio"]

    return tc, bc, sorted(set(he))


def diem_ht(tc):
    """pd-Q1 §2 — (so ✓) / (so ✓ + so ✗) x 10. '—' va '?' LOAI KHOI MAU SO."""
    v = sum(1 for x in tc.values() if x == "✓")
    x_ = sum(1 for x in tc.values() if x == "✗")
    if v + x_ == 0:
        return None
    return round(v / float(v + x_) * 10, 1)


# ────────────────────────────────────────────────────────────────────
# 6 · TUONG NGAN  (pd-F §4 — CONG T, 6 cau kiem)
# ────────────────────────────────────────────────────────────────────

CHAN_INSIGHT = ["nv", "tc", "diem", "loai", "bang_chung"]
CHAN_QC = ["chan_dung", "hook", "ma_tran", "ads"]
RE_SDT = re.compile(r"(?<!\d)(?:\+?84|0)(?:3|5|7|8|9)\d{8}(?!\d)")
RE_EMAIL = re.compile(r"[\w.+-]+@[\w-]+\.[\w.]+")


def _moi_khoa(o, duong=""):
    if isinstance(o, dict):
        for k, v in o.items():
            yield k, duong + "/" + str(k)
            for r in _moi_khoa(v, duong + "/" + str(k)):
                yield r
    elif isinstance(o, list):
        for i, v in enumerate(o):
            for r in _moi_khoa(v, duong + "[%d]" % i):
                yield r


def _moi_chuoi(o):
    if isinstance(o, str):
        yield o
    elif isinstance(o, dict):
        for v in o.values():
            for r in _moi_chuoi(v):
                yield r
    elif isinstance(o, list):
        for v in o:
            for r in _moi_chuoi(v):
                yield r


def kiem_tuong_ngan(data, luong, ten_nv=None):
    """Sau cau kiem cua CONG T. Tra ve list loi — rong la qua.

    ⚠ Chay BANG MAY, khong bang mat (pd-F §4). ghi_json() goi ham nay
    va TU CHOI GHI neu list khong rong.
    """
    loi = []
    chuoi = list(_moi_chuoi(data))

    # ① + ③ — khoa bi chan theo luong
    chan = CHAN_INSIGHT if luong == "insight" else CHAN_QC
    for k, duong in _moi_khoa(data):
        if k in chan:
            loi.append("[%s] khoa bi chan '%s' tai %s" % (luong, k, duong))

    # ① — ten nhan vien lot vao luong insight
    if luong == "insight" and ten_nv:
        for ten in ten_nv:
            if not ten.strip():
                continue
            for s in chuoi:
                if khong_dau(ten) in khong_dau(s):
                    loi.append("[insight] ten nhan vien '%s' lot vao: %s" % (ten, s[:90]))
                    break

    # ② — thong tin khach (8 thu cua pd-B §3)
    for s in chuoi:
        m = RE_SDT.search(s)
        if m:
            loi.append("[%s] so dien thoai khach: %s" % (luong, m.group(0)))
        m = RE_EMAIL.search(s)
        if m and "nhakhoaparis.vn" not in m.group(0):
            loi.append("[%s] email: %s" % (luong, m.group(0)))

    # ⑥ — cau chan bang cua luong Q
    if luong == "qc":
        if "kèm cặp" not in (data.get("chan_bang") or ""):
            loi.append("[qc] thieu cau chan bang 'Diem dung de phan viec kem cap...'")

    return loi


def ghi_json(ten, data, luong=None, ten_nv=None):
    """Moi lan ghi JSON di qua day. ⛔ Khong goi json.dump truc tiep o cho khac."""
    if luong:
        loi = kiem_tuong_ngan(data, luong, ten_nv)
        if loi:
            print("\n⛔ CONG T CHAN — ⛔ KHONG ghi file %s" % ten)
            for l in loi[:25]:
                print("   · " + l)
            if len(loi) > 25:
                print("   · … va %d loi nua" % (len(loi) - 25))
            print("\n→ Sua roi chay lai. Xem pd-F §4.")
            sys.exit(2)
    if not os.path.isdir(OUT):
        os.makedirs(OUT)
    p = os.path.join(OUT, ten)
    with io.open(p, "w", encoding="utf-8", newline="\n") as f:
        f.write(json.dumps(data, ensure_ascii=False, indent=2))
    print("→ %s" % os.path.relpath(p, GOC))
    return p


# ────────────────────────────────────────────────────────────────────
# 7 · LENH `doc`
# ────────────────────────────────────────────────────────────────────

def lenh_doc(args):
    ds, co_ghi_chu = doc_file_hoi_thoai(args.file)
    if not ds:
        print("⛔ Khong doc duoc hoi thoai nao. Kiem khuon file — pd-B §2.")
        sys.exit(1)

    hang, bo, ly_do = [], 0, {}
    for ht in ds:
        ld = ly_do_loai(ht)
        if ld:
            bo += 1
            ly_do[ld] = ly_do.get(ld, 0) + 1
            if ld != "chua-duoc-cham":
                continue

        loi_kh, loi_nv = ht["loi_kh"], ht["loi_nv"]
        v_rang = gan_v_rang(loi_kh)
        nhom_gt = gan_nhom_gt(v_rang, loi_kh)
        l_code, ds_l6, tinh = gan_l_code(ht, loi_kh, loi_nv)
        rao = gan_rao_can(ds_l6)
        dau_gd = bool(chua(loi_kh, TD["dau_gia_dinh"]["tu"]))
        bits = cham_bitmask(ht, v_rang, loi_kh)
        nong, sao, ghi_de = gan_do_nong(bits, v_rang, loi_kh)
        co_do = soat_co_do(loi_nv)
        tc, bc, he = cham_tc(ht, v_rang, ds_l6, co_ghi_chu, co_do)

        t0 = phut(ht["kh_that"][0]["ngay"], ht["kh_that"][0]["gio"]) if ht["kh_that"] else None
        t1 = phut(ht["nv_tin"][0]["ngay"], ht["nv_tin"][0]["gio"]) if ht["nv_tin"] else None

        hang.append({
            "ht": ht["ma"],
            "ngay": ht["ngay"], "gio_mo": ht["gio_mo"],
            "so_luot_kh": len(ht["kh_that"]), "so_luot_nv": len(ht["nv_tin"]),
            "co_sdt": ht["co_sdt"],
            "v_rang": v_rang, "nhom_gt": nhom_gt,
            "bitmask": "".join("1" if b else "0" for b in bits),
            "do_nong": nong, "do_nong_sao": sao, "ghi_de_nong": ghi_de,
            "co_do": [c["ma"] for c in co_do],
            "loi_he": he,
            "loai_khoi_mau": ld or "",

            "i": {
                "l_code": l_code, "ds_l6": ds_l6,
                "giai_doan": gan_giai_doan(ht, v_rang, ds_l6, loi_kh),
                "rao_can": rao,
                "nhom_khach": gan_nhom_khach(v_rang, loi_kh, dau_gd),
                "tinh": tinh,
                "post_ads": ht["post_ads"], "loi_hua_post": ht["loi_hua_post"],
                "cau_hoi_dau": (ht["kh_that"][0]["chu_that"][:200] if ht["kh_that"] else ""),
                "hoi_gia_tin_dau": bool(ht["kh_that"] and chua(ht["kh_that"][0]["chu_that"],
                                                               TD["hoi_gia"]["tu"])),
                "trich_khach": [t["chu_that"][:240] for t in ht["kh_that"][:4]],
                "dau_gia_dinh": dau_gd,
                "doi_thu_neu": tat_ca_cum(loi_kh, TD["doi_thu"]["ten"]),
                "cd": None,          # ⛔ null den khi anh duyet CONG 0 (pd-C §5)
            },

            "q": {
                "nv": ht["nv"],
                "phut_tra_loi_dau": (t1 - t0) if (t0 is not None and t1 is not None) else None,
                "trong_gio": trong_gio(ht["kh_that"][0]["gio"] if ht["kh_that"] else ht["gio_mo"]),
                "tc": tc,
                "bang_chung": bc,
                "co_do_chi_tiet": co_do,
                "ghi_chu_he": he,
            },
        })

    ds_nv = sorted({h["q"]["nv"] for h in hang if h["q"]["nv"]})
    canh_bao = []
    # pd-B §6 cau ③ — mau bi loc
    ngan = [h for h in hang if h["so_luot_kh"] <= 1]
    if hang and not ngan:
        canh_bao.append("⚠ Khong co HT nao duoi 2 luot khach — file co the DA BI LOC. "
                        "⛔ Khong dung de quyet ngan sach; ⛔ khong phan loai A/B/C/D.")
    if not co_ghi_chu:
        canh_bao.append("⚠ Ban xuat khong co ghi chu ban giao -> TC-7, TC-8 = '—' ca khoi. "
                        "Ky nay cham tren 8 tieu chi.")
    n_chua_cham = ly_do.get("chua-duoc-cham", 0)
    if n_chua_cham:
        canh_bao.append("⚠ %d HT khach nhan ma KHONG ai tra loi — lead mat trang, "
                        "vao muc 'viec he thong' (pd-B §7)." % n_chua_cham)

    data = {
        "schema": "doc-hoi-thoai-paris/1",
        "ky": args.ky,
        "tao_luc": bay_gio(),
        "nguon": os.path.basename(args.file),
        "co_ghi_chu_ban_giao": co_ghi_chu,
        "co_mau": {"doc": len(hang), "loai": bo, "ly_do_loai": ly_do},
        "canh_bao_mau": canh_bao,
        "nhan_vien": ds_nv,
        "ht": hang,
    }
    ghi_json("doc-hoi-thoai.json", data)

    print("\n── KIEM MAU (pd-B §6) ──")
    print("① Co mau      : %d doc · %d loai %s" % (len(hang), bo, ly_do or ""))
    print("② Khoang ngay : %s → %s" % (hang[0]["ngay"], hang[-1]["ngay"]))
    print("③ Mau bi loc? : %s" % ("⚠ CO DAU HIEU" if (hang and not ngan) else "khong"))
    print("④ Phan bo NV  :")
    for nv in ds_nv:
        n = sum(1 for h in hang if h["q"]["nv"] == nv)
        du = "✅ phan loai duoc" if n >= TD["nguong"]["nv_phan_loai"] else (
            "⛔ khong phan loai" if n >= TD["nguong"]["nv_khong_cham"] else "⛔ khong cham")
        print("   · %-22s %3d HT  %s" % (nv, n, du))
    for c in canh_bao:
        print("\n" + c)
    print("\n★ i.cd = null cho moi hang. Chay `insight` de phac hoa chan dung → CONG 0.")


# ────────────────────────────────────────────────────────────────────
# 8 · LENH `insight`  (luong I)
# ────────────────────────────────────────────────────────────────────

def _pc(n, m):
    return "%d%%" % round(n * 100.0 / m) if m else "—"


def _bang_truc(hang, lay, ten_map=None):
    """Mot dong cho moi gia tri. ★ LUON co cot hot_sao — luat chong lap vong."""
    nhom = {}
    for h in hang:
        k = lay(h)
        if not k:
            continue
        nhom.setdefault(k, []).append(h)
    ra = []
    for k, hs in sorted(nhom.items(), key=lambda x: -len(x[1])):
        n = len(hs)
        du = n >= TD["nguong"]["nhom_du"]
        ra.append({
            "ma": k,
            "ten": (ten_map or {}).get(k, ""),
            "n": n,
            # pd-D §5 quy tac ① — nhom duoi 10 HT thi AN TY LE
            "hot": _pc(sum(1 for h in hs if h["do_nong"] == "HOT"), n) if du else "⚠ chưa đủ mẫu",
            "hot_sao": _pc(sum(1 for h in hs if h["do_nong_sao"] == "HOT*"), n) if du else "⚠ chưa đủ mẫu",
            "co_sdt": _pc(sum(1 for h in hs if h["co_sdt"]), n) if du else "⚠ chưa đủ mẫu",
            "du_mau": du,
        })
    return ra


def lenh_insight(args):
    goc = nap_json("doc-hoi-thoai.json")
    if not goc:
        print("⛔ Chua co out/doc-hoi-thoai.json. Chay `doc` truoc.\n"
              "⛔ KHONG tu doc lai hoi thoai trong luong — pd-A §6.")
        sys.exit(1)

    hang = [h for h in goc["ht"] if not h["loai_khoi_mau"]]
    n = len(hang)
    ten_nv = goc.get("nhan_vien", [])

    # ── nguyen lieu phac hoa chan dung (pd-I1 §2) — in ra, CHUA gan
    cum = {}
    for h in hang:
        for t in h["i"]["trich_khach"]:
            for ma in ["L6.7", "L6.5", "L6.3", "L6.4", "L6.6", "L6.2"]:
                for tu in tat_ca_cum(t, TD["l_code"][ma]["tu"]):
                    cum[tu] = cum.get(tu, 0) + 1
    cum_top = sorted(cum.items(), key=lambda x: -x[1])[:14]

    hoi_gia_dau = sum(1 for h in hang if h["i"]["hoi_gia_tin_dau"])
    dau_gd = sum(1 for h in hang if h["i"]["dau_gia_dinh"])

    # ── rao can: DEM THEO LUOT (pd-I2 §3)
    luot = {}
    for h in hang:
        for r in h["i"]["rao_can"]:
            luot[r] = luot.get(r, 0) + 1
    tong_luot = sum(luot.values())

    # ── L6.7: neu ten hang / khong neu  (★ con so phai lam ngay)
    l67 = [h for h in hang if "L6.7" in h["i"]["ds_l6"]]
    l67_neu = sum(1 for h in l67 if h["q"]["tc"].get("TC-4") == "✓")

    # ── nhom N vang mat
    co_n = {h["i"]["nhom_khach"] for h in hang if h["i"]["nhom_khach"]}
    ten_n = {"N1": "Mất răng, trung–cao niên", "N2": "Thẩm mỹ răng 22–40",
             "N3": "Niềng răng", "N4": "Đau cấp", "N5": "Làm lại ca lỗi",
             "N6": "Gia đình & trẻ em"}
    vang = ["%s · %s — 0 HT" % (k, v) for k, v in ten_n.items() if k not in co_n]

    # ── post: loi hua ↔ cau hoi dau  (★ phan gia tri nhat, pd-I3 §5)
    post = {}
    for h in hang:
        p = h["i"]["post_ads"]
        if not p:
            continue
        d = post.setdefault(p, {"ma": p, "loi_hua": h["i"]["loi_hua_post"],
                                "n_ht": 0, "hoi_gia_dau": 0, "co_sdt": 0, "rao": {}})
        d["n_ht"] += 1
        d["hoi_gia_dau"] += 1 if h["i"]["hoi_gia_tin_dau"] else 0
        d["co_sdt"] += 1 if h["co_sdt"] else 0
        for r in h["i"]["rao_can"]:
            d["rao"][r] = d["rao"].get(r, 0) + 1
    for d in post.values():
        du = d["n_ht"] >= TD["nguong"]["nhom_du"]
        d["du_mau"] = du
        if not du:
            d["ghi_chu"] = "⚠ chưa đủ mẫu — ⛔ không xếp hạng, ⛔ không khuyến nghị"
        # khuon hinh (pd-I3 §5)
        if d["hoi_gia_dau"] * 2 >= d["n_ht"]:
            d["khuon"] = "hua-nhanh-khach-hoi-gia"
        elif d["rao"].get("NGỜ", 0) * 2 >= d["n_ht"]:
            d["khuon"] = "neu-hang-khach-van-ngo"
        else:
            d["khuon"] = "khop"

    # ── co do ĐÃ LỌC cho luong I (pd-F §6 — mot chieu, bo nguyen van + ten)
    co_do_tong = {}
    for h in hang:
        for ma in h["co_do"]:
            d = co_do_tong.setdefault(ma, {"ma": ma, "luot": 0, "ht": [], "v_rang": {}})
            d["luot"] += 1
            d["ht"].append(h["ht"])
            d["v_rang"][h["v_rang"]] = d["v_rang"].get(h["v_rang"], 0) + 1
    for d in co_do_tong.values():
        d["ten"] = TD["co_do"][d["ma"]]["ten"]
        d["v_rang_hay_gap"] = sorted(d["v_rang"], key=lambda k: -d["v_rang"][k])[:2]
        d.pop("v_rang")
        d["ht"] = d["ht"][:8]

    # ── viec he thong (pd-F §7 — xuat hien o CA HAI bao cao)
    he = {}
    for h in hang:
        for g in h["loi_he"]:
            he[g] = he.get(g, 0) + 1

    data = {
        "schema": "insight-dashboard-paris/1",
        "bo_cuc": "insight",
        "ky": args.ky,
        "thuong_hieu": "Nha khoa Paris",
        "tao_luc": bay_gio(),

        "the_so": [
            {"nhan": "Hội thoại đọc", "so": n, "phu": "%d bị loại" % goc["co_mau"]["loai"]},
            {"nhan": "% có SĐT", "so": _pc(sum(1 for h in hang if h["co_sdt"]), n),
             "phu": "%d/%d" % (sum(1 for h in hang if h["co_sdt"]), n)},
            {"nhan": "HOT", "so": _pc(sum(1 for h in hang if h["do_nong"] == "HOT"), n),
             "phu": "HOT* " + _pc(sum(1 for h in hang if h["do_nong_sao"] == "HOT*"), n)},
            {"nhan": "Chưa được chạm", "so": goc["co_mau"]["ly_do_loai"].get("chua-duoc-cham", 0),
             "canh_bao": True},
            {"nhan": "Ngoài 7 tỉnh (L2.5)", "so": sum(1 for h in hang if h["i"]["l_code"] == "L2.5"),
             "canh_bao": True},
        ],

        "truc": {
            "v_rang": _bang_truc(hang, lambda h: h["v_rang"],
                                 {k: TD["v_rang"][k]["ten"] for k in TD["v_rang"]["_thu_tu"]}),
            "nhom_gt": _bang_truc(hang, lambda h: h["nhom_gt"]),
            "giai_doan": _bang_truc(hang, lambda h: h["i"]["giai_doan"]),
            "l_code": _bang_truc(hang, lambda h: h["i"]["l_code"],
                                 {k: v.get("ten", "") for k, v in TD["l_code"].items()
                                  if isinstance(v, dict)}),
            "nhom_khach": _bang_truc(hang, lambda h: h["i"]["nhom_khach"], ten_n),
            "rao_can": [{"ma": k, "luot": v, "pc_luot": _pc(v, tong_luot)}
                        for k, v in sorted(luot.items(), key=lambda x: -x[1])],
        },
        "cach_dem_rao_can": ("Đếm theo LƯỢT rào cản: %d hội thoại → %d lượt. "
                             "Một hội thoại mang được 2–3 rào cản nên tổng cột lớn hơn "
                             "tổng hội thoại." % (n, tong_luot)),

        "nguyen_lieu_chan_dung": {
            "cum_chu_khach_tu_noi": [{"cum": k, "luot": v} for k, v in cum_top],
            "cau_hoi_dau": {"hoi_gia_ngay": hoi_gia_dau,
                            "neu_tinh_trang": n - hoi_gia_dau},
            "dau_hieu_nguoi_thu_ba": dau_gd,
        },
        "nhom_n_vang_mat": vang,

        "l6_7_ngo_vat_lieu": {
            "n": len(l67), "neu_ten_hang": l67_neu,
            "khong_neu": len(l67) - l67_neu,
            "doc_ra": ("%d hội thoại ngờ vật liệu — %d được nêu bằng chứng thật, "
                       "%d chỉ nhận câu trấn an chung. Con số cuối là NỘI DUNG PHẢI LÀM NGAY."
                       % (len(l67), l67_neu, len(l67) - l67_neu)),
        },

        "ads": {
            "co_so_lieu": bool(nap_json("doc-ads.json")),
            "post": sorted(post.values(), key=lambda d: -d["n_ht"]),
            "phe_u": {"inbox": n, "co_sdt": sum(1 for h in hang if h["co_sdt"]),
                      "ket_noi": None, "dat_lich": None, "den_kham": None},
            "canh_bao_phe_u": ("⚠ chưa đo được show-up — ⛔ KHÔNG lấy 'đặt lịch' "
                               "thay cho 'đến khám' (pd-I3 §1)"),
        },

        "doi_thu_bi_so_sanh": sorted(
            {t: sum(1 for h in hang if t in h["i"]["doi_thu_neu"])
             for h in hang for t in h["i"]["doi_thu_neu"]}.items(),
            key=lambda x: -x[1]),

        "co_do_tong": sorted(co_do_tong.values(), key=lambda d: -d["luot"]),
        "viec_he_thong": [{"nhom": k, "n_ht": v} for k, v in sorted(he.items(), key=lambda x: -x[1])],
        "slot_cho": [
            {"stt": 1, "ten": "Bảng giá theo dòng trụ / dòng sứ", "chan": "ô ? của TC-9 · CĐ-P5"},
            {"stt": 2, "ten": "Số năm bảo hành theo dịch vụ", "chan": "ô — của TC-4 · CĐ-P8"},
            {"stt": 3, "ten": "Case before–after có giấy đồng ý", "chan": "hook before–after đứng 🟠 · CĐ-P11"},
            {"stt": 4, "ten": "Cơ sở đủ năng lực All-On / ghép xương", "chan": "định tuyến khách tỉnh (V-02)"},
            {"stt": 5, "ten": "Số giấy xác nhận nội dung quảng cáo", "chan": "mọi hook y khoa đứng 🟠"},
            {"stt": 6, "ten": "Điều kiện & lãi suất trả góp", "chan": "ô — của TC-4 với rào L6.3"},
            {"stt": 7, "ten": "Mốc KPI (xin số · show-up · chốt phác đồ)", "chan": "⛔ không so được đạt/chưa"},
        ],

        "tu_kiem_4_rui_ro": {
            "mau_bi_loc": (goc["canh_bao_mau"][0] if goc["canh_bao_mau"] else "không thấy dấu hiệu"),
            "mau_nho": "%d/%d nhóm dưới 10 HT đã ẩn tỷ lệ" % (
                sum(1 for b in _bang_truc(hang, lambda h: h["v_rang"]) if not b["du_mau"]),
                len(_bang_truc(hang, lambda h: h["v_rang"]))),
            "lap_vong": "mọi bảng trục đều có cột hot_sao (chấm lại ⛔ không kể tín hiệu ①)",
            "lam_phat_hot": "⚠ ⛔ chưa đối chiếu được — chưa đo được show-up của nhóm HOT",
        },

        "cho_cong_0": True,
        "ghi_chu_cong_0": ("⛔ CHƯA gán chân dung. i.cd = null cho mọi hàng. "
                           "Agent phác họa 4–7 chân dung từ `nguyen_lieu_chan_dung` rồi "
                           "DỪNG chờ anh gõ DUYỆT CHÂN DUNG — pd-I1 §5."),
    }

    ghi_json("bao-cao-insight.json", data, luong="insight", ten_nv=ten_nv)

    print("\n── LUONG I · INSIGHT ──")
    print("Co mau      : %d HT" % n)
    print("Rao can     : %d luot / %d HT" % (tong_luot, n))
    print("L6.7        : %d HT ngo vat lieu — %d duoc neu bang chung that, %d chi nhan tran an"
          % (len(l67), l67_neu, len(l67) - l67_neu))
    print("Nhom N vang : %s" % (", ".join(vang) or "khong"))
    print("Post         : %d post co the nguon" % len(post))
    if vang:
        print("\n★ Nhom N vang mat la mot PHAT HIEN, khong phai o trong (pd-I1 §1).")
    print("\n★ CONG 0 — ⛔ CHUA gan chan dung. Phac hoa tu nguyen_lieu_chan_dung roi cho DUYET.")


# ────────────────────────────────────────────────────────────────────
# 9 · LENH `qc`  (luong Q)
# ────────────────────────────────────────────────────────────────────

CHAN_BANG = ("Điểm dùng để phân việc kèm cặp. Không phải căn cứ kỷ luật hay "
             "xếp hạng công khai.")

TEN_TC = {
    "TC-1": "Phản hồi ≤ 2 phút", "TC-2": "Gọi đúng tên dịch vụ / tình trạng",
    "TC-3": "Thu đủ 4 thông tin", "TC-4": "Tạo tin cậy bằng bằng chứng",
    "TC-5": "Xin số có lý do có lợi cho khách", "TC-6": "Xác thực số / Zalo",
    "TC-7": "Phân loại HOT/WARM/COLD + nhóm V", "TC-8": "Phiếu bàn giao đủ 13 trường",
    "TC-9": "⛔ Không từ cấm · không \"chính hãng\" sai · không chốt giá cứng",
    "TC-10": "Nêu rõ bước tiếp theo",
}


def lenh_qc(args):
    goc = nap_json("doc-hoi-thoai.json")
    if not goc:
        print("⛔ Chua co out/doc-hoi-thoai.json. Chay `doc` truoc.\n"
              "⛔ KHONG tu doc lai hoi thoai trong luong — pd-A §6.")
        sys.exit(1)

    # HT khong co NV thi khong cham duoc — nhung van dem (pd-B §7)
    hang = [h for h in goc["ht"] if h["q"]["nv"] and not h["loai_khoi_mau"]]
    mau_bi_loc = bool(goc["canh_bao_mau"]) and "BI LOC" in goc["canh_bao_mau"][0]

    # ── chi so doi: % dat tung TC, ⛔ chi tinh o ✓/✗
    chi_so = []
    for ma in ["TC-%d" % i for i in range(1, 11)]:
        v = sum(1 for h in hang if h["q"]["tc"].get(ma) == "✓")
        x = sum(1 for h in hang if h["q"]["tc"].get(ma) == "✗")
        mien = sum(1 for h in hang if h["q"]["tc"].get(ma) in ("—", "?"))
        ly_do = ""
        if mien:
            gom = {}
            for h in hang:
                if h["q"]["tc"].get(ma) in ("—", "?"):
                    for g in h["q"]["ghi_chu_he"]:
                        gom[g] = gom.get(g, 0) + 1
            ly_do = "; ".join(sorted(gom, key=lambda k: -gom[k])[:2])
        chi_so.append({"tc": ma, "ten": TEN_TC[ma],
                       "dat": _pc(v, v + x) if (v + x) else "⛔ không chấm được",
                       "n_cham": v + x, "n_mien": mien, "ly_do_mien": ly_do})

    # ── ca nhan (⛔ CHI ra so-tay, ⛔ khong len tab cong khai — pd-D §3)
    theo_nv = {}
    for h in hang:
        theo_nv.setdefault(h["q"]["nv"], []).append(h)

    ca_nhan, phan_bo = [], {"A": 0, "B": 0, "C": 0, "D": 0, "chua_du_mau": 0}
    for nv, hs in sorted(theo_nv.items()):
        diem_list = [d for d in (diem_ht(h["q"]["tc"]) for h in hs) if d is not None]
        # TC-9 truot -> hoi thoai 0 diem (P8 §6)
        diem_list = [0.0 if h["q"]["tc"].get("TC-9") == "✗" else d
                     for h, d in zip(hs, diem_list)] if diem_list else []
        n_ht = len(hs)
        yeu = manh = ""
        tl = {}
        for ma in TEN_TC:
            v = sum(1 for h in hs if h["q"]["tc"].get(ma) == "✓")
            x = sum(1 for h in hs if h["q"]["tc"].get(ma) == "✗")
            if v + x:
                tl[ma] = v / float(v + x)
        if tl:
            yeu = min(tl, key=lambda k: tl[k])
            manh = max(tl, key=lambda k: tl[k])

        rec = {"nv": nv, "n_ht": n_ht,
               "tc_yeu": yeu, "tc_manh": manh,
               "co_do": sorted({c for h in hs for c in h["co_do"]}),
               "o_loi_he": sum(1 for h in hs for x in h["q"]["tc"].values() if x == "—")}

        if n_ht < TD["nguong"]["nv_khong_cham"]:
            rec.update({"diem": None, "loai": "", "ghi_chu": "chưa đủ mẫu — ⛔ không chấm"})
            phan_bo["chua_du_mau"] += 1
        elif n_ht < TD["nguong"]["nv_phan_loai"] or mau_bi_loc:
            rec.update({"diem": None, "loai": "",
                        "ghi_chu": ("mẫu bị lọc — ⛔ không phân loại (pd-Q1 §7)" if mau_bi_loc
                                    else "5–9 HT — chấm từng hội thoại, ⛔ không phân loại")})
            phan_bo["chua_du_mau"] += 1
        else:
            d = round(sum(diem_list) / len(diem_list), 1) if diem_list else None
            pl = TD["phan_loai"]
            loai = "D"
            if d is not None:
                loai = "A" if d >= pl["A"] else "B" if d >= pl["B"] else "C" if d >= pl["C"] else "D"
            # ⚠ Mot co do trong ky -> ⛔ khong duoc xep loai A
            if loai == "A" and rec["co_do"]:
                loai = "B"
                rec["ghi_chu"] = "⚠ có cờ đỏ trong kỳ → ⛔ không xếp loại A (pd-Q1 §7)"
            rec.update({"diem": d, "loai": loai})
            phan_bo[loai] += 1
        ca_nhan.append(rec)

    # ── co do day du (luong Q duoc biet ten + nguyen van)
    co_do = []
    for h in hang:
        for c in h["q"]["co_do_chi_tiet"]:
            co_do.append({
                "ma": c["ma"], "ten": TD["co_do"][c["ma"]]["ten"],
                "ht": h["ht"], "nv": h["q"]["nv"],
                "nguyen_van": c["nguyen_van"],
                "v_rang": h["v_rang"],
                "goc": ("he-thong" if c["ma"] in ("CĐ-P8", "CĐ-P11") else "can-xac-dinh"),
                "nguoi_xu_ly": "⏸ chờ dữ kiện — trưởng nhóm trực page",
                "han": "⏸ chờ dữ kiện",
                "cau_dung": "⏸ chờ dữ kiện — ⛔ KHÔNG báo cờ mà không đưa câu đúng (pd-Q2 §4 ô ⑤)",
            })

    # ── o "?" cho doi chieu
    cho = []
    for h in hang:
        for ma, v in h["q"]["tc"].items():
            if v == "?":
                cho.append({
                    "tc": ma, "ht": h["ht"],
                    "nguyen_van": "; ".join(h["q"]["bang_chung"].get(ma, []))[:240],
                    "cau_hoi": "Bảng giá hiện hành có dòng này chưa, và con số có khớp?",
                    "nhanh": {"co_va_khop": "✓", "co_va_lech": "✗ + CĐ-P5", "chua_cap": "—"},
                    "nguoi_doi_chieu": "⏸ chờ dữ kiện — người giữ bảng giá",
                })

    # ── viec he thong, gom theo NGUYEN NHAN (⛔ khong theo nguoi)
    he = {}
    for h in hang:
        for g in h["q"]["ghi_chu_he"]:
            d = he.setdefault(g, {"nhom": g, "n_o": 0, "o": set()})
            d["n_o"] += 1
            for ma, v in h["q"]["tc"].items():
                if v in ("—", "?"):
                    d["o"].add(ma)
    viec_he = []
    for d in sorted(he.values(), key=lambda x: -x["n_o"]):
        viec_he.append({"nhom": d["nhom"], "n_o": d["n_o"], "o": sorted(d["o"]),
                        "ai_cap": "⏸ chờ dữ kiện",
                        "cap_roi_go_duoc": "⏸ chờ dữ kiện — ⛔ ô này là ô làm cho việc được làm (pd-Q3 §4)"})

    # ── 3 TC yeu nhat, SAU KHI loc bo cai la loi he
    cham_duoc = [c for c in chi_so if c["n_cham"] >= TD["nguong"]["nhom_du"]]
    xep = sorted(cham_duoc, key=lambda c: int(c["dat"].rstrip("%")) if c["dat"].endswith("%") else 999)
    yeu_nhat, loai_ra = [], []
    for c in xep:
        # loi he chiem phan lon o mien -> ⛔ khong dua vao dao tao (pd-Q3 §5)
        if c["n_mien"] > c["n_cham"]:
            loai_ra.append({"tc": c["tc"], "vi_sao": "phần lớn ô là lỗi hệ → ST-HT, ⛔ không đào tạo"})
        elif len(yeu_nhat) < 3:
            yeu_nhat.append(c["tc"])

    n_cham_duoc = sum(1 for c in chi_so if c["n_cham"] > 0)
    diem_khoi = [r["diem"] for r in ca_nhan if r["diem"] is not None]

    data = {
        "schema": "qc-trucpage-paris/1",
        "bo_cuc": "qc",
        "ky": args.ky,
        "tao_luc": bay_gio(),
        "chan_bang": CHAN_BANG,

        "the_so": [
            {"nhan": "Hội thoại chấm", "so": len(hang),
             "phu": "%d HT ⛔ không có NV" % (len(goc["ht"]) - len(hang))},
            {"nhan": "Số tiêu chí chấm được", "so": "%d/10" % n_cham_duoc,
             "phu": ", ".join(c["tc"] for c in chi_so if c["n_cham"] == 0) + " = — cả khối"
                    if n_cham_duoc < 10 else ""},
            {"nhan": "Điểm trung bình khối",
             "so": (round(sum(diem_khoi) / len(diem_khoi), 1) if diem_khoi else "⛔ chưa đủ mẫu"),
             "phu": "chuẩn P8 ≥ 8,0"},
            {"nhan": "Cờ đỏ", "so": len(co_do), "canh_bao": True},
            {"nhan": "Ô chờ đối chiếu", "so": len(cho), "canh_bao": True},
        ],

        "phan_bo": phan_bo,
        "chi_so_doi": chi_so,
        "ca_nhan": ca_nhan,
        "co_do": co_do,
        "cho_doi_chieu": cho,
        "viec_he_thong": viec_he,
        "chua_duoc_cham": {
            "n": goc["co_mau"]["ly_do_loai"].get("chua-duoc-cham", 0),
            "ht": [h["ht"] for h in goc["ht"] if h["loai_khoi_mau"] == "chua-duoc-cham"],
            "doc_ra": "Khách nhắn rồi ⛔ không ai trả lời — lead mất trắng. "
                      "⛔ KHÔNG chấm vào ai, nhưng phải có số (pd-B §7).",
        },
        "tc_yeu_nhat_khoi": yeu_nhat,
        "tc_loai_khoi_dao_tao": loai_ra,
        "canh_bao": goc["canh_bao_mau"],
    }

    ghi_json("bao-cao-qc.json", data, luong="qc")

    print("\n── LUONG Q · QC TRUC PAGE ──")
    print("Cham        : %d HT · %d nguoi" % (len(hang), len(theo_nv)))
    print("Tieu chi    : %d/10 cham duoc" % n_cham_duoc)
    print("Phan bo     : A=%d B=%d C=%d D=%d · chua du mau=%d"
          % (phan_bo["A"], phan_bo["B"], phan_bo["C"], phan_bo["D"], phan_bo["chua_du_mau"]))
    print("Co do       : %d" % len(co_do))
    print("O cho       : %d" % len(cho))
    print("\n── CHI SO DOI ──")
    for c in chi_so:
        print("  %-6s %-42s %7s  (cham %3d · mien %3d)"
              % (c["tc"], c["ten"][:42], c["dat"], c["n_cham"], c["n_mien"]))
    if mau_bi_loc:
        print("\n⚠ MAU BI LOC -> ⛔ KHONG phan loai A/B/C/D (pd-Q1 §7).")
    print("\n★ CONG 2 — soat %d co do truoc khi phat so tay (pd-Q2 §5)." % len(co_do))
    print("★ Bang ca nhan ⛔ KHONG len dashboard. Chi ra so-tay/ (pd-D §3).")


# ────────────────────────────────────────────────────────────────────
# 10 · LENH `ads`
# ────────────────────────────────────────────────────────────────────

def _so(x):
    try:
        return float(str(x).replace(",", "").replace(".", "").strip() or 0)
    except ValueError:
        return 0.0


def lenh_ads(args):
    with io.open(args.file, encoding="utf-8-sig") as f:
        rows = list(csv.DictReader(f))
    if not rows:
        print("⛔ File ads rong.")
        sys.exit(1)

    cot = {khong_dau(k): k for k in rows[0]}

    def lay(r, *ten):
        for t in ten:
            k = cot.get(khong_dau(t))
            if k:
                return r.get(k, "")
        return ""

    post = {}
    for r in rows:
        ma = (lay(r, "ma_post", "ten_quang_cao", "ma post", "post") or "").strip()
        if not ma:
            continue
        d = post.setdefault(ma, {"ma": ma, "chi": 0.0, "hien_thi": 0.0,
                                 "click": 0.0, "tin_nhan": 0.0, "tinh": set()})
        d["chi"] += _so(lay(r, "chi"))
        d["hien_thi"] += _so(lay(r, "hien_thi", "impressions"))
        d["click"] += _so(lay(r, "click"))
        d["tin_nhan"] += _so(lay(r, "tin_nhan", "inbox"))
        t = (lay(r, "co_so", "tinh") or "").strip()
        if t:
            d["tinh"].add(t)

    goc = nap_json("doc-hoi-thoai.json")
    ht_theo_post = {}
    if goc:
        for h in goc["ht"]:
            p = h["i"]["post_ads"]
            if p:
                ht_theo_post.setdefault(p, []).append(h)

    ra = []
    for d in post.values():
        hs = ht_theo_post.get(d["ma"], [])
        n_sdt = sum(1 for h in hs if h["co_sdt"])
        ra.append({
            "ma": d["ma"], "chi": round(d["chi"]), "tinh": sorted(d["tinh"]),
            "cpm": round(d["chi"] / d["hien_thi"] * 1000) if d["hien_thi"] else None,
            "ctr": ("%.2f%%" % (d["click"] / d["hien_thi"] * 100)) if d["hien_thi"] else None,
            "cpi": round(d["chi"] / d["tin_nhan"]) if d["tin_nhan"] else None,
            "n_ht_khop": len(hs),
            "cpl": round(d["chi"] / n_sdt) if n_sdt else None,
            "cp_dat_lich": None,   # ⏸ chua do duoc
            "cp_den_kham": None,   # ⏸ chua do duoc — ⛔ KHONG lay dat lich thay
            "du_mau": len(hs) >= TD["nguong"]["nhom_du"],
        })

    data = {
        "schema": "doc-ads-paris/1",
        "ky": args.ky,
        "tao_luc": bay_gio(),
        "nguon": os.path.basename(args.file),
        "post": sorted(ra, key=lambda d: -(d["chi"] or 0)),
        "canh_bao": [
            "⚠ cp_dat_lich và cp_den_kham = null — ⛔ KHÔNG lấy 'đặt lịch' thay cho "
            "'đến khám' (pd-I3 §1). Phễu nha khoa rò nặng nhất ở chính khe này.",
            "⚠ Mốc KPI chưa được Paris chốt → `⚠ chưa có mốc so sánh`. ⛔ Không tự đặt mốc.",
        ],
    }
    ghi_json("doc-ads.json", data)
    print("\nDoc %d post. ⛔ Post duoi 10 HT khop -> ⛔ khong xep hang (du_mau=false)." % len(ra))


# ────────────────────────────────────────────────────────────────────
# 11 · LENH `kiem`  (chay CONG T tay)
# ────────────────────────────────────────────────────────────────────

def lenh_kiem(args):
    with io.open(args.file, encoding="utf-8") as f:
        data = json.load(f)
    schema = data.get("schema", "")
    luong = "insight" if "insight" in schema else ("qc" if "qc" in schema else None)
    if not luong:
        print("⛔ ⛔ Khong nhan ra luong tu schema '%s'." % schema)
        sys.exit(1)
    goc = nap_json("doc-hoi-thoai.json")
    ten_nv = goc.get("nhan_vien", []) if goc else []
    loi = kiem_tuong_ngan(data, luong, ten_nv)
    print("CONG T · %s · luong %s" % (os.path.basename(args.file), luong))
    if not loi:
        print("✅ Qua 6 cau kiem tuong ngan.")
        return
    print("⛔ %d loi:" % len(loi))
    for l in loi:
        print("   · " + l)
    sys.exit(2)


# ────────────────────────────────────────────────────────────────────

def main():
    ap = argparse.ArgumentParser(description="Agent-InsightDashboard-Paris — mot lan doc, hai luong")
    sub = ap.add_subparsers(dest="lenh")

    p = sub.add_parser("doc", help="doc hoi thoai MOT LAN -> bang du kien goc")
    p.add_argument("file")
    p.add_argument("--ky", required=True)
    p.set_defaults(fn=lenh_doc)

    p = sub.add_parser("insight", help="luong I — ve KHACH")
    p.add_argument("--ky", required=True)
    p.set_defaults(fn=lenh_insight)

    p = sub.add_parser("qc", help="luong Q — ve NHAN VIEN")
    p.add_argument("--ky", required=True)
    p.set_defaults(fn=lenh_qc)

    p = sub.add_parser("ads", help="doc so quang cao")
    p.add_argument("file")
    p.add_argument("--ky", required=True)
    p.set_defaults(fn=lenh_ads)

    p = sub.add_parser("kiem", help="chay CONG T tay tren mot file JSON")
    p.add_argument("file")
    p.set_defaults(fn=lenh_kiem)

    a = ap.parse_args()
    if not getattr(a, "fn", None):
        ap.print_help()
        sys.exit(1)
    a.fn(a)


if __name__ == "__main__":
    main()
