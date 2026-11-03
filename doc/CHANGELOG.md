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

---

## v1.0.1 — 02/11/2026

- **Bỏ mọi định vị chéo thương hiệu.** Nha khoa Paris là thương hiệu độc lập — repo ⛔ không còn trình bày nó như "bản nha khoa" của công cụ một thương hiệu khác. Sửa 15 chỗ trong 11 file; cảnh báo kỹ thuật (⛔ không nạp lẫn tri thức hai thương hiệu, ⛔ không dùng `5A`/`O-01…O-12`, schema ⛔ không tương thích) **giữ nguyên giá trị**, chỉ viết lại ở mức chung. Đối chiếu ở mức **ngành** (phễu nha khoa có thêm bước đến khám; dải giá rộng hơn) thì giữ — đó là tri thức của chính Paris trong `P3` §3 và `P4` §3.
- **Thêm trang hướng dẫn cài đặt & prompt mẫu:** <https://claude.ai/artifact/B1qQBgUixjBjVwiiDwDTQJ> — 9 mục, 3 tab nền tảng, 6 prompt dán nguyên văn, 19 nút Copy. Hai luồng được **mã màu** (xanh = luồng I, vàng = luồng Q) chạy suốt trang để tường ngăn đọc được bằng mắt. ⚠️ Artifact đang **riêng tư**.
- **Sửa số ký tự đã lệch** trong `README.md` và `doc/01-cai-dat.md` sau lần sửa trên: `SYSTEM-PROMPT.md` 9.076 → **9.070**, bản ngắn 7.058 → **7.062** (vẫn trong giới hạn 8.000 của ChatGPT).

---

## v1.1 — 03/11/2026 · port tri thức từ hệ cùng họ

Hệ `InsightDashboard` của một thương hiệu khác trong tập đoàn vừa sửa sâu phần tri thức. Kỳ này **port phần phương pháp sang Paris**, ⛔ không port nội dung.

### ⛔ Cái ⛔ KHÔNG port — và vì sao

Ba sổ mới của hệ kia là **bản nhập nguyên văn bộ `KF-60` / `KF-62` / `KF-64` của khối Sale** thương hiệu đó: bảng điểm lead, danh mục chân dung, ngưỡng chọn tệp. Đó là **nội dung của một ngành khác và một khối Sale khác** — và **hệ Paris ⛔ chưa có bộ `KF` nào tương đương**. Bê sang là dán bảng điểm của ngành khác lên khách nha khoa.

★ Paris đã có thước đo riêng: `P8` §1 (5 tín hiệu) · `P8` §4 (SLA) · `P4` §3 (`V1/V2/V3`). **`P8` thắng khi mâu thuẫn** — ⛔ không đẻ thang thứ hai.

### ✅ Mười ba điểm đã port — toàn bộ là **phương pháp**

| # | Port gì | Vào đâu |
|---|---|---|
| ① | ★★ **Dữ liệu sức khoẻ** — tiền sử · bệnh nền · thuốc · ảnh · phim là dữ liệu sức khoẻ theo **Luật 91/2025/QH15**: chỉ lưu **nhãn + câu bằng chứng ngắn**, giới hạn người xem, cần đồng ý xử lý | `pd-B` §3b **(mới)** |
| ② | ★★ **An toàn trước bán hàng** — dấu hiệu an toàn → chuyển bác sĩ, ⛔ không tư vấn bán. Và `V-01` có **hai loại**: làm ở **nơi khác** = ca tư vấn mới; làm **tại Paris** = **khiếu nại**, ⛔ không phải cơ hội bán → `TC-5`/`TC-9` chấm `—` | `pd-E` §3b **(mới)** |
| ③ | ★★ **Ba nhãn cho một hội thoại** — chân dung (*khách là ai*) × `L-code`/rào cản (*đang vướng gì*) × độ nóng. ⛔ Không chân dung nào tên là một trở ngại | `pd-I1` §1c **(mới)** |
| ④ | ★★ **Phác họa theo kỳ là CHẾ ĐỘ TẠM** — cố định là đích. Ghi rõ cái mất (`CD3` tháng 10 ≠ `CD3` tháng 11) và **ba điều kiện để nghỉ CỔNG 0** | `pd-I1` §1 *(viết lại)* |
| ⑤ | ★★ **Ưu tiên chân dung chỉ tính từ dữ liệu** — độ nóng trung bình + tỷ lệ đến khám thật. Ngưỡng ≥30 HT **và** ≥5 lượt đến khám. ★ Ưu tiên đổi ngân sách/nội dung/đào tạo, ⛔ **KHÔNG đổi SLA khách** | `pd-I4` §2b **(mới)** |
| ⑥ | ★★ **Một quyết định — một sổ.** Hai công thức cho một quyết định thì **chắc chắn lệch nhau** mà vẫn khớp tổng. Bảng ranh giới 9 quyết định + 3 cặp hay bị trộn | `pd-A` §3b **(mới)** |
| ⑦ | **Luật nghỉ một mục** — `⛔ ĐÃ NGHỈ <ngày> — thay bằng <X>`, ⛔ không xoá, ⛔ không chạy song song. Và: đổi luật thì **ghi luôn cái mất** | `pd-A` §3b |
| ⑧ | **Năm cổng ổn định** của bộ chân dung + ★ chẩn đoán khi trượt cổng `CD0`: đo độ dài chữ khách trước. ⛔ **Thêm từ khoá khi khách chưa nói gì là ÉP DỮ LIỆU** | `pd-I1` §5b **(mới)** |
| ⑨ | **Thứ tự kiểm là một phần của luật** — ⚠️ đảo thứ tự là xếp ca sửa hỏng thành ca làm lần đầu, rồi mất một khách **đã từng bị hỏng một lần** | `pd-C` §3 |
| ⑩ | **Một hội thoại hỏi nhiều dịch vụ** — lấy dịch vụ hỏi **sâu nhất**, ghi phần còn lại để bán chéo, ⛔ không tách thành hai hội thoại | `pd-C` §3 |
| ⑪ | **Khuôn ba nhịp** của câu gửi khách: *điều khách sợ bằng chữ khách → điều mình làm khác → bằng chứng*. Và **trạng thái duyệt gắn trên từng câu**, ⛔ không theo cả tuyến | `pd-I4` §4 · `pd-Q3` §2 |
| ⑫ | **Luật sổ nhập từ ngoài** — giữ nguyên văn để đối chiếu · ⛔ repo không tự đặt thêm · thiếu thì **báo lại để bổ sung bản sau** · `⚠ Cần xác minh` chặn **cả câu thoại**, ⛔ không chỉ con số | `pd-E` đầu sổ |
| ⑬ | **Sửa một tiêu chí thì sửa BA chỗ cùng lúc** — sổ · `tu_dien.json` · `pd.py`. Lệch nhau thì ⛔ không ai biết chấm theo bản nào | `pd-Q1` §3 |

### Đã cài vào công cụ, ⛔ không chỉ viết vào sổ

Theo đúng luật ⑬ vừa thêm:

- `tools/tu_dien.json`: thêm khối `lam_o_dau` *(tai_paris · noi_khac · phan_nan)* và `an_toan_truoc_ban`; mở rộng `V-01` *(trụ bị lung lay · bị hở · sứ bị rơi · mão bị bung…)*.
- `tools/pd.py`: thêm `gan_lam_o_dau()` · `co_dau_hieu_an_toan()` · `dang_phan_nan()`; `cham_tc()` miễn `TC-5`/`TC-9` ở luồng ⛔ không-phải-bán; bảng gốc thêm ô `i.lam_o_dau` và `dau_hieu_an_toan`.
- `template/MAU_hoi-thoai.md`: thêm `HT-017` — ca **trồng Implant tại Paris, trụ lung lay, khách bức xúc**. Nó phải ra `V-01` · `tai-paris` · `TC-5`=`—` · `TC-9`=`—`.

★ **Một lỗi thiết kế bắt được khi chạy thử:** bản đầu khoá `gan_lam_o_dau()` sau `v_rang == "V-01"`. `HT-017` khi đó ra `V-03` *(bộ từ khoá `V-01` chưa có "trụ bị lung lay")* nên ô `lam_o_dau` trống, và **một ca khiếu nại bị chấm như một cơ hội bán**. → Bỏ khoá: *"làm ở đâu"* là dữ kiện **độc lập**. ⛔ **Một lỗ hổng của bộ từ khoá ⛔ không được biến thành một ca khiếu nại chấm sai.**

### Hai chỗ số liệu lệch sẵn có — sửa luôn

- `pd-E` §7 tiêu đề ghi *"SÁU SLOT"* nhưng bảng có **bảy** dòng → sửa thành **BẢY**.
- `pd-Q3` §2 và `pd-Q1` §2 trỏ sang *"`pd-E` §5"* và *"sáu slot"* → sửa thành **`pd-E` §7** và **bảy slot**.

### Đã kiểm

```
✅ python tools/dem-ngan.py   → bản ngắn 7.900 / 8.000  ⚠️ chỉ còn 100 ký tự dư
✅ doc · insight · qc · ads   → chạy sạch trên 17 HT mẫu
✅ CỔNG T                     → qua 6 câu, cả hai file
✅ HT-017 → V-01 · tai-paris · TC-5 = — · TC-9 = —
           ghi chú hệ: "khong phai luong ban (khieu nai tai Paris)"
✅ HT-006 (đau cấp) · HT-011 (tiểu đường) → TC-5 = — theo luật an toàn
✅ HT-007 (bọc sứ ở chỗ khác) → noi-khac, VẪN chấm bình thường
```

### ⚠️ Việc còn mở

- **Thư viện chân dung nha khoa ⛔ chưa có.** CỔNG 0 vẫn chạy, và chế độ phác họa theo kỳ vẫn mang đúng cái mất đã ghi ở `pd-I1` §1: ⛔ không so được giữa các kỳ, ⛔ không bàn giao được cho Sale.
- **Bản ngắn chỉ còn 100 ký tự dư.** Lần thêm luật sau phải bỏ bớt một luật cũ, hoặc chuyển hẳn sang bản đầy đủ.
