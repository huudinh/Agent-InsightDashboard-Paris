# Agent · Insight Dashboard · Nha khoa Paris

> Đọc hội thoại chat của khách **Nha khoa Paris** (`nhakhoaparis.vn`) được nhập vào, đọc **đúng một lần**, rồi từ cùng một lần đọc sinh ra **hai bộ đầu ra tách rời nhau**: một bộ nói về **khách**, một bộ nói về **người trực page**.

`v1.0` · 31/10/2026 · ngành **nha khoa**

### 📘 [**Hướng dẫn cài đặt & prompt mẫu →**](https://claude.ai/artifact/B1qQBgUixjBjVwiiDwDTQJ)
*(9 mục · 3 tab nền tảng · 6 prompt dán nguyên văn · 19 nút Copy — dễ dùng hơn đọc repo)*
> ⚠️ Artifact đang **riêng tư**. Người khác chỉ mở được sau khi anh chia sẻ qua menu Share trên trang.

---

## ★ Hai luồng và tường ngăn

```
              du-lieu/hoi-thoai.md   (người dùng nhập vào)
                         │
                 ┌───────┴────────┐
                 │  ĐỌC MỘT LẦN   │   ← đọc đúng một lần, ⛔ không đọc lại
                 └───────┬────────┘
                         │
             out/doc-hoi-thoai.json   ← BẢNG DỮ KIỆN GỐC
                         │
        ┌────────────────┴────────────────┐
        │                                 │
   ╔════▼═══════════════╗         ╔═══════▼════════════╗
   ║  LUỒNG I           ║         ║  LUỒNG Q           ║
   ║  INSIGHT KHÁCH     ║         ║  QC TRỰC PAGE      ║
   ╠════════════════════╣         ╠════════════════════╣
   ║ Chủ thể: KHÁCH     ║         ║ Chủ thể: NHÂN VIÊN ║
   ║ • chân dung kỳ     ║         ║ • 10 tiêu chí TC   ║
   ║ • SỢ · NGỜ · NGẠI  ║         ║ • điểm + A/B/C/D   ║
   ║ • câu hỏi ngầm     ║         ║ • 11 cờ đỏ         ║
   ║ • ma trận · hook   ║         ║ • sổ tay từng người║
   ║ • số ads           ║         ║ • việc hệ thống    ║
   ╚════════┬═══════════╝         ╚═══════┬════════════╝
            │                             │
   bao-cao-insight.json          bao-cao-qc.json
            │                             │
      ▼ Marketing · nội dung       ▼ Trưởng nhóm trực page
            │                             │
   ═════════╧══════ TƯỜNG NGĂN ═══════════╧═════════
   ⛔ KHÔNG file nào chứa CẢ tên nhân viên LẪN lời khách
```

### Vì sao tách — ⛔ không phải để chia tab cho dễ xem

**Cùng một bằng chứng, hai luồng đọc ra hai nghĩa trái nhau.** Ví dụ thật, hội thoại `HT-002`:

```
KH:  bọc sứ bao nhiêu tiền
NV:  Dạ chào anh, anh để lại số điện thoại em tư vấn chi tiết ạ
KH:  cứ nói giá đi đã
NV:  Dạ anh inbox lại giúp em nhé
```

| Luồng | Đọc ra | Việc phải làm |
|---|---|---|
| **I** | Khách vào từ post *"nụ cười mới chỉ sau 1 lần hẹn"* rồi hỏi giá ngay → **post hứa nhanh mà trang đích ⛔ không có giá**. Phát hiện về **nội dung** | Sửa post · thêm khung giá |
| **Q** | Xin số trước khi hỏi tình trạng → trượt `TC-5`; né giá hai lượt → `TC-9`? **Chưa chắc** — phải tra xem bảng giá có cấp cho dòng sứ đó chưa | Đã có giá → **lỗi người**, vào sổ tay. Chưa cấp → ⛔ **lỗi hệ, không trừ điểm** |

> ⚠️ **Gộp hai luồng là ép người đọc chọn một trong hai nghĩa.** Và trong thực tế họ luôn chọn nghĩa của luồng Q — vì nó có tên người, nghe cụ thể hơn. Kết quả: lỗi nội dung và lỗi hệ thống bị ghi thành lỗi nhân viên, kỳ nào cũng vậy, và ⛔ không ai sửa post.

Luật đầy đủ ở [`knowledge/pd-F-tuong-ngan-hai-luong.md`](knowledge/pd-F-tuong-ngan-hai-luong.md).

---

## Bốn lệnh

| Lệnh | Làm gì | Ra |
|---|---|---|
| `ĐỌC` | Đọc một lần, dựng bảng dữ kiện gốc | `out/doc-hoi-thoai.json` |
| `INSIGHT` | Luồng I — dừng ở **CỔNG 0** rồi **CỔNG 1** | `out/bao-cao-insight.json` |
| `QC` | Luồng Q — dừng ở **CỔNG 2** | `out/bao-cao-qc.json` · `so-tay/` |
| `ADS` | Đọc số quảng cáo | `out/doc-ads.json` |

```bash
python tools/pd.py doc     du-lieu/hoi-thoai.md --ky "01-15/11"
python tools/pd.py insight --ky "01-15/11"
python tools/pd.py qc      --ky "01-15/11"
python tools/pd.py ads     du-lieu/ads-facebook.csv --ky "01-15/11"
python tools/pd.py kiem    out/bao-cao-insight.json     # CỔNG T
python tools/gui-dashboard.py out/bao-cao-insight.json  # bản 1 file gửi được
```

⛔ **Không có lệnh `AUTO` chạy cả hai luồng ra một file** — cố tình không có. Một file thì tường ngăn ⛔ không tồn tại.

★ **Luồng Q chạy xong được trong khi luồng I còn chờ anh duyệt chân dung.** Hai cổng của luồng I ⛔ không chặn luồng Q — đây là lợi ích thật của việc tách luồng, ⛔ không phải hiệu ứng phụ.

---

## Bốn cổng chặn

| Cổng | Chặn gì |
|---|---|
| **CỔNG 0** | ⛔ Không gán chân dung khi **bản phác họa chưa được duyệt**. Hệ ⛔ không có bộ chân dung mặc định |
| **CỔNG 1** | ⛔ Không viết hook khi **ma trận ưu tiên chưa được duyệt** |
| **CỔNG 2** | ⛔ Không phát sổ tay khi còn **cờ 🔴 chưa gỡ** |
| **CỔNG T** ★ | ⛔ Không xuất file khi chưa qua **6 câu kiểm tường ngăn** — chạy **bằng máy**, `pd.py` từ chối ghi file nếu trượt |

---

## 12 sổ tri thức

| Sổ | Nội dung |
|---|---|
| **Lõi — đọc một lần** | |
| [`pd-A`](knowledge/pd-A-vai-tro-hai-luong.md) | ★ Vai trò · hai luồng · quy trình · bốn cổng · bộ mã dùng chung |
| [`pd-B`](knowledge/pd-B-doc-dau-vao.md) | Khuôn đầu vào · ẩn danh 8 thứ · kiểm mẫu 4 câu |
| [`pd-C`](knowledge/pd-C-bang-du-kien-goc.md) | Bảng dữ kiện gốc · luật một lần đọc · 3 luật ghi đè độ nóng |
| **Luồng I — về khách** | |
| [`pd-I1`](knowledge/pd-I1-chan-dung-cong-0.md) | Chân dung của kỳ · CỔNG 0 · ⛔ vì sao không dùng `N1…N6` |
| [`pd-I2`](knowledge/pd-I2-dao-sau-insight.md) | Câu hỏi ngầm · 3 rào cản · ★ luật chống lặp vòng `% HOT*` |
| [`pd-I3`](knowledge/pd-I3-ads-phe-u-nha-khoa.md) | Phễu nha khoa có bước "đến khám" · ★ post hứa gì ↔ khách hỏi gì |
| [`pd-I4`](knowledge/pd-I4-ma-tran-hook.md) | Ma trận `độ nóng × V1/V2/V3` · CỔNG 1 · hook · cờ pháp chế |
| **Luồng Q — về nhân viên** | |
| [`pd-Q1`](knowledge/pd-Q1-cham-diem-truc-page.md) | ★★ 10 tiêu chí `TC` · bảng tra lỗi hệ · 4 rào an toàn |
| [`pd-Q2`](knowledge/pd-Q2-co-do-phap-che.md) | 11 cờ đỏ · CỔNG 2 · câu miễn trừ |
| [`pd-Q3`](knowledge/pd-Q3-so-tay-thuc-thi.md) | 3 loại sổ tay · ★ "việc không phải của bạn" |
| **Chung** | |
| [`pd-D`](knowledge/pd-D-dashboard-schema.md) | Hai schema · hai file · ba quy tắc hiển thị |
| [`pd-E`](knowledge/pd-E-module-paris.md) | Module thương hiệu Paris · ★ 7 slot dữ kiện chưa cấp |
| [`pd-F`](knowledge/pd-F-tuong-ngan-hai-luong.md) | ★★ **Tường ngăn** — cái gì đi qua được, cái gì không |

★ **Dựng agent cho thương hiệu nha khoa khác = thay `pd-E`**, ⛔ không sửa 11 sổ còn lại.

---

## ★ Bộ mã — ⛔ không đặt mã mới

Mọi mã dưới đây **đã tồn tại** trong [`Paris-Agent-Factory`](../Paris-Agent-Factory/). Agent này **tái dùng nguyên văn**:

| Bộ mã | Giá trị | Nguồn |
|---|---|---|
| Vấn đề răng | `V-01` … `V-11` | `P4` §2 |
| Nhóm giá trị | `V1` · `V2` · `V3` | `P4` §3 |
| Trạng thái vận hành | `L1.1` … `L6.7` | `P6` §2 |
| Giai đoạn | `S1` · `S2` · `S3` · `CS` | `P3` §1 |
| Rào cản chốt | `SỢ` · `NGỜ` · `NGẠI` | `P2` §2 |
| Nhóm khách | `N1` … `N6` | `P2` §3 |
| Độ nóng | `HOT`/`WARM`/`COLD` + bitmask 5 số | `P8` §1 |

Chỉ có ở repo này: `CD1…CDn` (chân dung **của kỳ**) · `TC-1…TC-10` (10 tiêu chí, ánh xạ 1:1 với `P8` §6) · `CĐ-P1…CĐ-P11` (cờ đỏ).

⚠️ ⛔ **Không gọi tiêu chí chấm là `N1…N6`** — `N` đã là nhóm khách.
⚠️ ⛔ **Không dùng `5A` / `O-01…O-12`** — ⛔ không phải bộ mã của hệ này. **`P8` thắng khi mâu thuẫn.**

---

## Sáu điều riêng của ngành nha

```
① BA TRỤC ⛔ KHÔNG GỘP: L-code · độ nóng · V1/V2/V3.
  ★ Một lead HOT·V3 (cạo vôi) ⛔ không bằng WARM·V1 (All-On).
  Gộp lại thì V3 đông và dễ chốt sẽ CHE MẤT việc V1 đang rò.
  V1 ⛔ không đánh giá bằng tốc độ chốt — nuôi tới 90 ngày.

② L6.7 NGỜ VẬT LIỆU — mã riêng ngành nha, ⛔ không gộp vào L6.2.
  Khách ⛔ KHÔNG tự kiểm được vật liệu trong miệng mình.
  ★ Nêu tên hãng CHƯA ĐỦ — phải cho thứ khách TỰ KIỂM được:
    tên dòng · mã trụ/phôi trên phiếu · được xem phiếu trước khi cấy.

③ "CHÍNH HÃNG" LÀ TUYÊN BỐ PHÁP LÝ, ⛔ không phải từ marketing.
  Chỉ 4 hãng: Straumann · Invisalign · Nacera · Ormco.
  Gắn sai → cờ CĐ-P2, TC-9 trượt → TOÀN HỘI THOẠI 0 ĐIỂM.

④ ⛔ KHÔNG hứa thời gian điều trị cứng · ⛔ không chẩn đoán qua ảnh ·
  ⛔ không chốt giá ca cụ thể · ⛔ không nêu bác sĩ ngoài 3 người được duyệt.

⑤ GIÁ ĐÃ CÔNG KHAI tại /hoan-my-bang-gia-dich-vu-nha-khoa.html
  → né giá hẳn là LỖI NGƯỜI. Nhưng giá dòng trụ/dòng sứ CHƯA CẤP → ô "?".

⑥ PHỄU DỪNG Ở "ĐẾN KHÁM", ⛔ không phải doanh thu.
  Quyết định tiền thật xảy ra TRÊN GHẾ KHÁM, ⛔ không trong inbox.
  ⛔ KHÔNG lấy "đặt lịch" thay cho "đến khám".
  ★ CTA mạnh nhất: mời ĐI KHÁM + CHỤP PHIM, nhấn "chưa phải điều trị".
```

---

## Cài đặt

📘 **Bản có nút Copy từng prompt:** <https://claude.ai/artifact/B1qQBgUixjBjVwiiDwDTQJ>

Hoặc xem [`doc/01-cai-dat.md`](doc/01-cai-dat.md). Ba cách: Claude Project · ChatGPT Custom GPT · Gemini Gem.

| Thẻ bộ não | Ký tự | Dùng cho |
|---|---|---|
| [`SYSTEM-PROMPT.md`](SYSTEM-PROMPT.md) | 9.070 | Claude Project · Gemini Gem |
| [`SYSTEM-PROMPT-NGAN.md`](SYSTEM-PROMPT-NGAN.md) | 7.062 | ChatGPT (ô Instructions giới hạn 8.000) |

```bash
python tools/dem-ngan.py   # kiểm bản ngắn còn trong giới hạn
```

---

## ⛔ Agent này không phải ai

| Việc | Của ai |
|---|---|
| Chấm **chất lượng cuộc gọi** (có audio) | `Agent-QC-Telesale` |
| Tối ưu **từ khoá & landing page** Google Ads | `Agent-AdsOptimize-NhaKhoaParis` |
| Sinh **bộ Excel R1–R6** theo khuôn tập đoàn | `Paris-Agent-Factory` |
| Viết **bài SEO** cho site | skill `seo-article-writer` |
| Trả lời khách · thao tác CRM | ⛔ Không agent nào — hệ này chỉ **đọc dữ liệu đã xảy ra** |
| Báo giá ca cụ thể | ⛔ Bác sĩ, sau khi khám và chụp phim |

⛔ **Không nạp lẫn tri thức của repo này với tri thức của một thương hiệu khác vào cùng một Project** — khác bộ mã, khác luật hiển thị giá, khác giờ làm.

---

## ⛔ Dữ liệu khách

`du-lieu/` · `data/` · `out/` · `dashboard/data/` · `so-tay/` **đã bị `.gitignore` chặn**. ⛔ Không commit dữ liệu khách.

⛔ Không nạp CCCD · hồ sơ bệnh án · ảnh X-quang của khách lên công cụ công cộng. 
