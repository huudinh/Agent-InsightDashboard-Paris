# CHANGELOG

## v1.0 — 31/10/2026 · bản đầu

Dựng `Agent-InsightDashboard-Paris` cho **Nha khoa Paris** (`nhakhoaparis.vn`) — một thương hiệu độc lập, có bộ mã và luật riêng.

### Mười quyết định thiết kế của bản này

| | Quyết định | Vì sao |
|---|---|---|
| ① | ★ **Hai luồng** có tường ngăn, **một lần đọc** chung | Cùng một bằng chứng, hai luồng đọc ra hai nghĩa trái nhau. Gộp lại thì lỗi nội dung và lỗi hệ thống bị ghi thành lỗi nhân viên |
| ② | `ĐỌC` → `INSIGHT` / `QC` **độc lập**. ⛔ ⛔ Không có `AUTO` | Một file thì tường ngăn ⛔ không tồn tại. Và luồng Q ⛔ không phải chờ một cái duyệt ⛔ không liên quan đến nó |
| ③ | Phễu `S1/S2/S3/CS`, ★ dừng ở **đến khám** | Quyết định tiền thật xảy ra **trên ghế khám**, ⛔ không trong inbox. Chỉ số trực page dừng ở show-up |
| ④ | Rào cản `L1.1…L6.7` + `SỢ·NGỜ·NGẠI` | Tái dùng nguyên văn của `Paris-Agent-Factory` — ⛔ không đặt mã trùng nghĩa |
| ⑤ | ★ Thêm **trục giá trị `V1/V2/V3`** | Dải giá nha khoa rộng gấp nhiều lần: một ca All-On và một ca cạo vôi ⛔ không thể cùng mức ưu tiên dù cả hai đều `HOT` |
| ⑥ | Tiêu chí `TC-1…TC-10`, **thang 10** | `P8` §6 là thước đo của cả hệ báo cáo Paris — **`P8` thắng** khi mâu thuẫn |
| ⑦ | **11 cờ đỏ** `CĐ-P1…CĐ-P11`, 4 cờ riêng ngành nha | *"Chính hãng"* là tuyên bố pháp lý; hứa thời gian điều trị cứng; chẩn đoán qua ảnh; chốt giá ca |
| ⑧ | Giờ làm **8h30–18h30** | Giờ thật của Paris (`pd-E` §5) — ngoài khung thì `TC-1` chấm `—`, ⛔ không trừ ai |
| ⑨ | Giá **đã công khai** → né giá là **lỗi người** | Bảng giá niêm yết tại `/hoan-my-bang-gia-dich-vu-nha-khoa.html`, khách tra được trước khi nhắn |
| ⑩ | **Bốn cổng** — thêm **CỔNG T** kiểm tường ngăn **bằng máy** | Chạy tay thì ⛔ sẽ có kỳ quên. Lọt tên nhân viên vào báo cáo insight là lỗi ⛔ không gỡ được sau khi đã gửi đi |

### Bộ mã — tái dùng, ⛔ không đặt mới

`V-01…V-11` · `V1/V2/V3` · `L1.1…L6.7` · `S1/S2/S3/CS` · `SỢ/NGỜ/NGẠI` · `N1…N6` · bitmask 5 tín hiệu — tất cả lấy nguyên văn từ `Paris-Agent-Factory` (`P2`·`P3`·`P4`·`P6`·`P8`).

⚠️ Hai bộ mã phải mới: `CD1…CDn` (chân dung **của kỳ**, vì `N1…N6` là nhóm biết trước) và `TC-1…TC-10` (vì `P8` §6 ghi `①…⑩` mà cần mã gọi được thành chữ, và ⛔ không được gọi là `N` — `N` đã là nhóm khách).

---

### ★ Năm lỗi của chính bộ công cụ, phát hiện khi chạy thử 16 hội thoại mẫu

> Ghi lại đầy đủ vì cả năm đều là **lỗi im lặng**: mọi bảng vẫn khớp tổng, biểu đồ vẫn đẹp, kết luận sai hoàn toàn.

**① Khớp từ khoá bằng `in` trên chữ bỏ dấu → `V-04` nuốt 9/16 hội thoại.**
Từ khoá `"hô"` (V-04) bỏ dấu thành `"ho"`, mà `"ho"` nằm trong `"hỏi"`, `"hôm"`, `"cho"`, `"chỗ"`. Cạo vôi, bọc sứ, veneer, mất răng đều bị gán thành *"niềng"*. Thử `"cho em hỏi giá"` → `V-04`.
→ Sửa: khớp **theo ranh giới từ** bằng regex, ⛔ không dùng `in`.

**② Từ một âm tiết phải khớp CÓ DẤU — `"đau"` vs `"đâu"`.**
Bỏ dấu thì cả hai thành `"dau"`, nên *"cạo vôi ở **đâu** ạ"* bị chấm thành **đau cấp** `V-06`, kéo theo nhóm khách `N4` và luật ghi đè *"tối thiểu WARM"*.
→ Sửa: từ **một âm tiết** khớp có dấu; từ **hai âm tiết trở lên** vẫn khớp bỏ dấu (va chạm gần như không xảy ra, và chịu được việc khách gõ thiếu dấu).

**③ Dòng `[Thẻ: …]` bị đếm là một lượt khách.**
`pd-B` §2 nói rõ thẻ ⛔ không phải chữ khách gõ. Hệ quả ba cái: `so_luot_kh` lệch 1 → kiểm *"mẫu bị lọc"* báo động giả; `cau_hoi_dau` rỗng; `TC-1` lấy mốc thời gian của **dòng thẻ** thay vì của câu khách thật.
→ Sửa: tách `kh_that` (lượt khách có chữ thật) dùng cho đếm · câu hỏi đầu · mốc `TC-1`.

**④ `TC-3` chấm 0% trên cả 15 hội thoại.**
Hai nguyên nhân: bộ từ khoá quá hẹp, **và** đọc sai tiêu chí. `P8` §6 ③ là *"**thu đủ** 4 thông tin"* — thông tin **thu được**, bất kể nhân viên hỏi hay khách tự nói.
→ Sửa: khớp trên **cả hai nửa** hội thoại, mở rộng 4 nhóm từ khoá. Còn 27% — con số thật.

**⑤ ★ Cờ đỏ gắn cho người làm ĐÚNG.**
`HT-014` bị gắn `CĐ-P11` vì câu *"về ảnh case thì em xin phép xác nhận lại danh sách ảnh được phép sử dụng rồi gửi chị, vì ảnh khách phải có sự đồng ý của họ"* — nhân viên **từ chối gửi ảnh chưa duyệt**, đúng quy trình, nhưng cụm *"ảnh case"* khớp từ khoá.
→ Sửa: thêm khối `mien_tru_co_do` và hàm `mien_tru()`; **mọi** lần bắt cờ phải đi qua nó. Cờ từ 11 xuống **10, tất cả đều thật**.

> ⚠️ **Lỗi ⑤ là lỗi tệ nhất mà repo này có thể sinh ra** — đúng cái mà `pd-Q1` §6 rào ③ cảnh báo. Một cờ đỏ gắn sai tên không gỡ được sau khi đã gửi đi.

### Hai chỗ đọc sai tri thức, cũng sửa trong lần chạy đó

- **`V-04` mặc định `V1`** → `P4` §3 ghi *"V1 (Invisalign) / V2 (mắc cài)"*, nên mặc định phải là **`V2`**, chỉ nâng lên `V1` khi có Invisalign/trong suốt. Một ca veneer ⛔ không phải `V1`.
- **`N6` gán cho mọi hội thoại có nhắc người nhà** → con nhắn cho **bố 68 tuổi mất cả hàm** thì bệnh nhân đúng chân dung **`N1`** (*"45–70 tuổi, mất 1 răng đến cả hàm… nhắc người nhà đi cùng"*, `P2` §3). `N6` là **trẻ em / cả nhà**. Dấu hiệu người thứ ba vẫn giữ riêng ở cột `dau_gia_dinh`.

---

### Đã kiểm

```
✅ python tools/dem-ngan.py              → bản ngắn 7.058 / 8.000 ký tự
✅ python tools/pd.py doc · insight · qc · ads  → chạy sạch trên 16 HT mẫu
✅ python tools/pd.py kiem (CỔNG T)      → qua 6 câu, cả hai file
✅ Thử PHÁ tường ngăn: cài tên "Nguyễn Hà" vào file insight
   → CỔNG T chặn, exit 2, ⛔ từ chối ghi file
✅ 16/16 hội thoại mẫu gán đúng V-xx · V1/V2/V3 · L-code · N · độ nóng
✅ 10/10 cờ đỏ đều thật, ⛔ không còn cờ nào gắn cho người làm đúng
```

### ⏸ Còn chờ Paris cấp — 7 slot

| # | Slot | Chặn gì |
|---|---|---|
| ① | Bảng giá theo dòng trụ / dòng sứ | ô `?` của `TC-9` · cờ `CĐ-P5` |
| ② | Chính sách bảo hành theo dịch vụ (số năm) | ô `—` của `TC-4` · ★ cờ `CĐ-P8` |
| ③ | Danh sách case before–after có giấy đồng ý | ★ cờ `CĐ-P11` · mọi hook before–after đứng 🟠 |
| ④ | Cơ sở đủ năng lực All-On / ghép xương | định tuyến khách tỉnh — **ca đắt nhất** |
| ⑤ | Số giấy xác nhận nội dung quảng cáo | mọi hook có phát ngôn y khoa đứng 🟠 |
| ⑥ | Điều kiện & lãi suất trả góp | ô `—` của `TC-4` với rào `L6.3` |
| ⑦ | Mốc KPI (xin số · show-up · chốt phác đồ) | ⛔ không so được *"đạt / chưa đạt"* |

★ Slot ② và ③ là hai slot **sinh cờ đỏ**: nhân viên bị khách hỏi mà hệ chưa cấp dữ kiện thì chỉ có hai đường — im (trượt `TC-4`) hoặc nói một con số nghe được (cờ đỏ). ⛔ **Đào tạo ⛔ không chữa được việc này.**

⚠️ **Slot chờ ≥3 kỳ → đưa lên đầu báo cáo**, ⛔ không để trong phụ lục.

### ⏸ Chưa làm

- Chưa chạy trên **dữ liệu thật** — mọi con số trong lần kiểm là của 16 hội thoại **mô phỏng**.
- `so-tay/` chưa có bộ sinh tự động (`ST-CN` · `ST-TN` · `ST-HT` hiện viết tay theo `prompts/prompt-so-tay.md`).
- Chưa có `goi/GOP-tri-thuc.md` (bản gộp cho nền tảng giới hạn số file).
- Phễu `ket_noi` · `dat_lich` · `den_kham` = `null` — ⛔ **chưa đo được show-up**, và ⛔ không lấy *"đặt lịch"* thay.
