# 01 · Cài đặt

📘 **Bản có nút Copy từng prompt:** <https://claude.ai/artifact/B1qQBgUixjBjVwiiDwDTQJ>
*(9 mục · 6 prompt dán nguyên văn · 8 câu kiểm sau khi cài — dễ dùng hơn file này)*

Ba cách dùng agent này. Chọn một.

> ⚠️ Agent này dựng riêng cho **Nha khoa Paris** (`nhakhoaparis.vn`) — một thương hiệu độc lập, có bộ mã và luật riêng. ⛔ **Không nạp lẫn tri thức của repo này với tri thức của một thương hiệu khác vào cùng một Project** — khác bộ mã, khác luật hiển thị giá, khác giờ làm. Trộn vào là hai hệ mã cùng mô tả một thứ và ⛔ không ai biết bảng nào đúng.

---

## A · Claude Project *(khuyến nghị)*

1. Tạo Project mới, tên: **Insight Dashboard Paris**.
2. Dán toàn bộ [`SYSTEM-PROMPT.md`](../SYSTEM-PROMPT.md) vào ô **Custom instructions**.
3. Nạp vào **Knowledge**:
   - 12 file trong [`knowledge/`](../knowledge/)
   - 5 file trong [`prompts/`](../prompts/)
4. ★ Nạp thêm **4 module nền của thương hiệu** từ [`Paris-Agent-Factory/knowledge/`](../../Paris-Agent-Factory/knowledge/): `P2` · `P4` · `P6` · `P8`.
   Đây là nguồn gốc của mọi bộ mã. **`P8` thắng khi mâu thuẫn** với sổ của repo này.
5. Nạp file dữ liệu của kỳ khi chạy: hội thoại + số ads.

---

## B · ChatGPT Custom GPT

Ô **Instructions** giới hạn 8.000 ký tự → dán [`SYSTEM-PROMPT-NGAN.md`](../SYSTEM-PROMPT-NGAN.md) *(7.062 ký tự)*. Phần còn lại nạp vào **Knowledge** như cách A.

Sau mỗi lần sửa bản ngắn, chạy:

```bash
python tools/dem-ngan.py
```

---

## C · Gemini Gem

Ô **Chỉ dẫn**: dán [`SYSTEM-PROMPT.md`](../SYSTEM-PROMPT.md). Knowledge như cách A.

---

## Chuẩn bị dữ liệu mỗi kỳ

Tạo thư mục `du-lieu/` *(đã bị `.gitignore` chặn — ⛔ không commit dữ liệu khách)*:

```
du-lieu/
├── hoi-thoai.md         ① bắt buộc — khuôn ở pd-B §2
├── ads-facebook.csv     ② nên có   — cột ở pd-B §5
└── danh-sach-post.csv   ③ tuỳ
```

★ **Khuôn hội thoại giống hệt `Paris-Agent-Factory/doc/mau-du-lieu/MAU_Hoi-thoai.md`** — cùng một bản xuất, ⛔ đừng đổi khuôn:

```
## <STT>. <Tên KH> — <DD/MM HH:MM>
- Phụ trách: <tên NV> · Có SĐT: <Có|Không> · Số tin: <n>
- **<DD/MM HH:MM> KH:** <nội dung khách>
- **<DD/MM HH:MM> NV (<tên NV>):** <nội dung nhân viên>
```

### ★ Thẻ nguồn quảng cáo — lợi thế của bản xuất Paris

```
- **03/11 09:12 KH:** [Thẻ: Inbox từ quảng cáo QC_Implant_Straumann – Trồng răng Implant trụ Straumann, ăn nhai như răng thật]
```

> **Thẻ nằm ngay trong hội thoại**, nên nối hội thoại ↔ post chính xác **1:1** — ⛔ không phải khớp bằng thời gian rồi đoán. Và tách ra được **hai** cột: mã post (`post_ads`) và **lời hứa của post** (`loi_hua_post`).

★ `loi_hua_post` là cột đắt nhất của luồng I. Nó cho đọc được câu *"post hứa `nụ cười mới chỉ sau 1 lần hẹn`, và 9/11 khách vào từ post đó hỏi giá ở tin đầu rồi rơi"* — một kết luận về **nội dung**, ⛔ không về người.

### Chạy thử ngay khi chưa có dữ liệu thật

```bash
python tools/pd.py doc     template/MAU_hoi-thoai.md --ky "03-16/11"
python tools/pd.py ads     template/MAU_ads-facebook.csv --ky "03-16/11"
python tools/pd.py insight --ky "03-16/11"
python tools/pd.py qc      --ky "03-16/11"
```

★ File mẫu **cài sẵn** các tình huống bộ công cụ phải bắt được: 11 cờ đỏ · lỗi hệ · ngoài giờ · ba luật ghi đè độ nóng · `L2.5` · tin chưa được chạm · và **một câu miễn trừ** (nhân viên từ chối gửi ảnh chưa duyệt — ⛔ phải **không** bị gắn cờ). Sửa file thì ⛔ đừng bỏ các tình huống đó.

---

## Dashboard

Trang `dashboard/index.html` **⛔ không bao giờ sửa**. Mỗi kỳ chỉ sinh thêm file JSON trong `dashboard/data/`; trang tự đọc trường `bo_cuc` rồi dựng đúng bộ tab.

```bash
cd dashboard && python -m http.server 8080   # rồi mở http://localhost:8080
```

★ **Bản một file gửi được** *(⛔ không cần máy chủ tĩnh)*:

```bash
python tools/gui-dashboard.py out/bao-cao-insight.json
# → out/dashboard-insight-<ky>.html
```

| Schema | Bố cục | Ai mở |
|---|---|---|
| `insight-dashboard-paris/1` | `insight` — 6 tab | Marketing · nội dung · ads |
| `qc-trucpage-paris/1` | `qc` — 5 tab | ⛔ **Chỉ** trưởng nhóm trực page |

⚠️ **Hai schema ⛔ không tương thích với nhau**, và ⛔ không tương thích với schema của bất kỳ hệ dashboard nào khác. Hai thư mục `data/` riêng là **không** đủ — phải **hai file riêng**, vì tường ngăn là tường giữa hai file.

### ⚠️ Trước khi publish — ba câu

```
① File này là insight hay qc?
   → ⛔ File qc-*.json ⛔ KHÔNG publish ra link công khai.
     Nó có TÊN NHÂN VIÊN. Gửi file, cho đúng trưởng nhóm.
② Đã chạy CỔNG T chưa?
   python tools/pd.py kiem out/bao-cao-insight.json
③ Artifact mặc định RIÊNG TƯ. Chuyển sang "ai có link đều mở được" thì
   ⛔ đừng dán link vào repo public — kể cả bản insight, vì nó chứa lời
   khách (đã ẩn danh) và kết luận nội bộ.
```

⚠️ **Và kiểm thêm một thứ riêng của ngành nha:** mô tả *"mất răng số 6 hàm dưới bên phải 2 năm"* là **nhận dạng được** khi nhóm chỉ có 1–2 HT. Nhóm dưới 10 HT thì dashboard đã tự ẩn tỷ lệ, nhưng trước khi publish ra ngoài khối, soát lại các nhóm mỏng.

---

## Kiểm sau khi cài — 8 câu

Hỏi agent 8 câu; trả lời sai câu nào thì nạp lại file tương ứng.

| Câu hỏi | Phải trả lời đúng | Nằm ở |
|---|---|---|
| ★ *"Báo cáo insight có được nêu tên nhân viên làm ví dụ không?"* | ⛔ **Không, không bao giờ**, kể cả "một ví dụ thôi". Dùng `HT-nnn`. Phát hiện nào chỉ giải thích được bằng tên người thì ⛔ không phải insight → chuyển luồng Q | `pd-F` §3 · §8 |
| ★ *"Chạy `AUTO` cho tôi cả hai luồng ra một file"* | ⛔ **Không có lệnh đó** — cố tình. Một file thì tường ngăn ⛔ không tồn tại | `pd-F` §2 |
| *"Chân dung lấy ở đâu ra?"* | ⛔ Không có bộ dựng sẵn — phác họa từ chính hội thoại của kỳ, duyệt ở CỔNG 0. ⛔ Không dùng `N1…N6` làm chân dung | `pd-I1` §1 |
| ★ *"Khách hỏi giá, trực page nói 'để lại số em tư vấn' — chấm sao?"* | `TC-9` = `✗` *(lỗi người)* — giá **đã công khai** tại `/hoan-my-bang-gia-dich-vu-nha-khoa.html`. Ngoại lệ `?`: dòng trụ/dòng sứ chưa có trong bảng | `pd-E` §6 |
| ★ *"Khách hỏi bảo hành mấy năm, nhân viên không trả lời — trừ điểm chứ?"* | ⛔ **Không.** Hệ **chưa cấp** số năm bảo hành (slot ②) → chấm `—`, đẩy lên "việc hệ thống". Trừ điểm là **chấm sai người** | `pd-Q1` §4 · `pd-E` §7 |
| ★ *"Nhân viên nói 'sứ bên em chính hãng hết' — sao?"* | Cờ **`CĐ-P2`** → `TC-9` trượt → **toàn hội thoại 0 điểm**. *"Chính hãng"* chỉ dùng cho **Straumann · Invisalign · Nacera · Ormco** | `pd-E` §3 |
| ★ *"Nhóm `V-03` có `% HOT` cao hơn `V-11` — kết luận được gì?"* | ⛔ **Chưa gì cả** — đó là **lặp vòng**: `V-11` ⛔ không được cộng tín hiệu ①. Phải xem cột `HOT*`. Bỏ ① mà chênh lệch biến mất → nói thẳng *"⛔ không có bằng chứng"* | `pd-I2` §4 |
| *"Lead HOT cạo vôi với lead WARM All-On, ưu tiên ai?"* | **WARM·V1** — giá trị kỳ vọng cao hơn `HOT·V3`. ⛔ Không xếp lead chỉ bằng độ nóng | `pd-I4` §1 |

★ **Câu 5 là câu agent sai tự tin nhất.** Nó trông hệt một lỗi tư vấn, và `pd-E` §7 đang có **bảy slot dữ kiện chưa được cấp** — nghĩa là một phần đáng kể ô trượt `TC-4`/`TC-9` thực ra là **lỗi hệ**. Đào tạo ⛔ không chữa được việc thiếu văn bản.
