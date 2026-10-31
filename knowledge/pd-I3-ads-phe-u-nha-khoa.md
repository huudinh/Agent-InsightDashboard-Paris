# pd-I3 · SỐ QUẢNG CÁO · PHỄU NHA KHOA · NỐI POST ↔ HỘI THOẠI

> Sổ này nối hai nguồn: **chữ của khách** và **số của quảng cáo**. Nó trả lời câu *"nội dung nào kéo về tệp rẻ mà ⛔ không ra số, và nội dung nào hứa điều ta ⛔ không đỡ được"*.

---

## 1. ★ PHỄU NHA KHOA CÓ MỘT BƯỚC THẨM MỸ ⛔ KHÔNG CÓ

Phễu thẩm mỹ: `inbox → có SĐT → kết nối → booking → thực hiện`

**Phễu nha khoa:**

```
inbox → có SĐT → kết nối (gọi được) → đặt lịch khám
      → ★ ĐẾN KHÁM (show-up) ← bước rò nhiều nhất, và là MỐC CUỐI của trực page
      → chốt phác đồ → điều trị (nhiều buổi) → tái khám
```

### Hai điều ⛔ không được quên khi đọc số

```
① "ĐẶT LỊCH KHÁM" ≠ "CHỐT ĐIỀU TRỊ".
   Khách đến khám, chụp phim, nghe bác sĩ rồi mới quyết.
   Quyết định tiền thật xảy ra TRÊN GHẾ KHÁM, không xảy ra trong inbox.
   → Chỉ số của trực page DỪNG Ở "ĐẾN KHÁM", ⛔ không phải doanh thu.

② MỜI ĐI KHÁM DỄ HƠN MỜI ĐIỀU TRỊ RẤT NHIỀU.
   Khám + chụp X-quang/scan là bước có GIÁ TRỊ THẬT với khách
   (biết mình đang bị gì), ⛔ chưa phải điều trị, ⛔ chưa phải trả tiền lớn.
   → Đây là CTA tự nhiên và mạnh nhất của ngành nha.
   → Hội thoại nào ⛔ không dùng CTA này mà nhảy thẳng vào báo giá
     là tư vấn sai nhịp — và nó cũng là một phát hiện về NỘI DUNG:
     post có mời đi khám, hay post chỉ mời hỏi giá?
```

⚠️ **Phễu trong báo cáo bắt buộc có cột "đến khám".** ⛔ Không có cột đó trong dữ liệu → ghi `⚠ chưa đo được show-up` và **để trống**. ⛔ **Không được lấy "đặt lịch" thay cho "đến khám"** — đó là chỗ ngành nha rò nặng nhất, và lấy số này thay số kia là che đúng cái khe cần nhìn.

---

## 2. CHUỖI CHỈ SỐ — ĐỌC THEO ĐÚNG THỨ TỰ

```
Chi → CPM → CTR → CPI → CPL → CP-ĐẶT-LỊCH → CP-ĐẾN-KHÁM
```

| Chỉ số | Công thức | Đọc ra gì |
|---|---|---|
| `CPM` | chi ÷ hiển thị × 1000 | Giá mua mắt. Tăng → **cạnh tranh/tệp**, ⛔ không phải nội dung |
| `CTR` | click ÷ hiển thị | Hình + câu đầu có kéo được không |
| `CPI` | chi ÷ số inbox | Giá một người chịu nhắn |
| `CPL` | chi ÷ số có SĐT | ★ Chỉ số lõi của trực page |
| `CP-ĐẶT-LỊCH` | chi ÷ số đặt lịch | |
| `CP-ĐẾN-KHÁM` | chi ÷ số đến khám | ★ Chỉ số **thật** của kỳ |

### ★ Luật chẩn đoán: `CPL` tăng thì đi từ gốc lên, ⛔ đừng đoán

```
CPL tăng
 ├─ CPM tăng?        → ⛔ KHÔNG PHẢI vấn đề nội dung.
 │                     Nói thẳng câu đó. Kiểm cạnh tranh / tệp / mùa.
 ├─ CTR giảm?        → Hình + câu đầu. Việc của Marketing.
 ├─ CPI ổn, CPL tăng → ★ Khách vẫn nhắn, nhưng KHÔNG CHO SỐ.
 │                     → đây là khe giữa luồng I và luồng Q:
 │                       • nội dung hứa sai kỳ vọng  → luồng I
 │                       • cách xin số               → luồng Q
 │                     ⛔ KHÔNG tự chọn một trong hai. Nói CẢ HAI
 │                       khả năng và chỉ ra cách phân biệt (§5).
 └─ CPL ổn, CP-ĐẾN-KHÁM tăng
                     → ⛔ KHÔNG phải việc của trực page nữa.
                       Khe gọi điện / đặt lịch / nhắc hẹn → CSKH
```

⚠️ Mốc KPI chưa được Paris chốt → ghi `⚠ chưa có mốc so sánh`. ⛔ **Không tự đặt mốc.** Năm mốc có số ở `P8` §7 là **mốc kế thừa từ hệ CSKH tập đoàn, chưa xác nhận cho ngành nha** — mọi lần so vào phải ghi rõ.

---

## 3. NỐI POST ↔ HỘI THOẠI

Nối bằng `post_ads` lấy từ thẻ trong hội thoại (`pd-B` §2), ⛔ không khớp bằng thời gian.

| Bảng | Hàng | Cột |
|---|---|---|
| **Hiệu quả post** | `post_ads` | chi · CPI · số HT · % có SĐT · CPL · `V-xx` chủ đạo · `V1/V2/V3` |
| **Post × chân dung** | `post_ads` | `CD1`…`CDn` + `CD0` |
| **Post × rào cản** | `post_ads` | SỢ · NGỜ · NGẠI |

★ **Bảng "Post × rào cản" là bảng đắt nhất.** Nó trả lời: *"post nào kéo về khách đã sẵn lòng tin, post nào kéo về khách ngờ nặng"* — và từ đó biết **nên sửa post hay nên cấp bằng chứng cho trực page**.

⚠️ Post dưới 10 HT → ghi `⚠ chưa đủ mẫu`, ⛔ không xếp hạng, ⛔ không khuyến nghị tắt/mở.

---

## 4. ⛔ KHI ⛔ KHÔNG CÓ SỐ ADS

Luồng I **vẫn chạy**. Nhưng:

```
⛔ KHÔNG viết CPI/CPL/CPM nào — kể cả "khoảng", kể cả "ước"
⛔ KHÔNG xếp hạng post theo hiệu quả
✅ VẪN xếp được post theo SỐ HỘI THOẠI và CHẤT hội thoại
   (% có SĐT · rào cản · chân dung) — đây là số đếm được
   từ chính hội thoại, ⛔ không cần file ads
✅ VẪN đọc được "post hứa gì ↔ khách hỏi gì" (§5) — ★ phần giá trị nhất
```

★ Nói rõ ở đầu mục: *"Kỳ này ⛔ chưa có file số ads. Mục này đọc **chất** của tệp từng post, ⛔ không đọc **giá** của tệp."*

---

## 5. ★★ POST HỨA GÌ ↔ KHÁCH HỎI GÌ NGAY SAU ĐÓ

Đây là phần **chỉ repo này làm được**, vì bản xuất của Paris mang sẵn `loi_hua_post` trong thẻ.

**Cách làm:** với mỗi post, đặt cạnh nhau hai thứ:

```
① LỜI HỨA của post   ← loi_hua_post
② CÂU HỎI ĐẦU TIÊN của khách vào từ post đó — phân bố
```

### Bốn khuôn hình hay gặp

| Khuôn | Dấu hiệu | Đọc ra | Ai sửa |
|---|---|---|---|
| **Khớp** | Post hứa *"ăn nhai như răng thật"* → khách hỏi *"tuổi này còn trồng được không"* | ✅ Post kéo đúng người, đúng tầng | — |
| **Hứa nhanh, khách hỏi giá** | Post *"nụ cười mới chỉ sau 1 lần hẹn"* → `9/11` khách hỏi giá ở tin đầu | 🔴 Post tạo kỳ vọng **nhanh + rẻ**, nhưng trang đích ⛔ không có khung giá | **Marketing** |
| **Hứa an toàn, khách ngờ nặng** | Post *"không đau, an toàn"* → khách hỏi *"có mài răng thật không"* | 🟠 Post **nói trước** nỗi sợ nên khách **mang nỗi sợ vào** hội thoại | Marketing — đổi sang nói **cơ chế** |
| **Nêu hãng, khách vẫn ngờ** | Post *"trụ Straumann"* → khách vẫn hỏi *"có chính hãng không, có bị tráo không"* | ★ Nêu tên hãng **chưa đủ** — khách cần **cách tự kiểm** (mã trụ, phiếu bảo hành) | Marketing + cấp bằng chứng cho trực page |

★ **Khuôn thứ tư là phát hiện quý nhất của ngành nha.** Nó nói rằng rào cản `L6.7` ⛔ không gỡ được bằng cách **nói tên hãng to hơn**, mà gỡ bằng cách cho khách **thứ tự kiểm tra được**. Đây là một tuyến nội dung, không phải một câu thoại.

### ★ Và đây là cách phân biệt hai khả năng ở §2

Khi `CPI` ổn mà `CPL` tăng, dùng chính bảng này:

| Nếu thấy | Thì nguyên nhân nằm ở | Chuyển cho |
|---|---|---|
| Câu hỏi đầu của khách **lệch hẳn** lời hứa post | **Nội dung** — post kéo sai kỳ vọng | Luồng I → Marketing |
| Câu hỏi đầu **khớp** lời hứa post, nhưng khách vẫn ⛔ không cho số | **Cách xin số** | ★ Luồng Q (`TC-5`) |

⚠️ ⛔ **Không tự chọn một trong hai rồi viết như thể đã biết chắc.** In cả hai số ra, để người đọc thấy khe nằm ở đâu.

---

## 6. CẮT THEO TỈNH — ĐẶC THÙ 7 CƠ SỞ

Nếu dòng ② có cột `co_so`/`tinh`:

| Cắt | Đọc ra |
|---|---|
| Chi theo tỉnh × số HT theo tỉnh | Tỉnh nào đang chi nhiều mà ⛔ không ra inbox |
| HT **ngoài 7 tỉnh/thành** (`L2.5`) | ★ Chi cho vùng ⛔ không có cơ sở |
| HT `V-02`/`V-03` (All-On, Implant) ở tỉnh | ★ Ca đắt nhất ở xa — ⛔ hệ chưa có danh sách cơ sở làm được (`pd-E` §5) |

★ **Dòng `L2.5` phải có số.** Chi tiền kéo khách ở tỉnh ⛔ không có cơ sở là tiền mất ngay từ đầu, ⛔ không phải lỗi tư vấn. Và nó là thứ ⛔ không ai thấy nếu ⛔ không cắt theo tỉnh.

⚠️ Khách **trong** 7 tỉnh/thành mà bảo xa → `L6.4`, **còn cửa**. ⛔ Không xếp vào `L2.5`. Phân biệt ở `pd-E` §3.

---

## 7. TỰ KIỂM SỔ NÀY

- [ ] Phễu có cột **"đến khám"** chưa? Có lấy "đặt lịch" thay không?
- [ ] `CPL` tăng: đã đi **từ `CPM` lên** chưa, hay kết luận ngay là lỗi nội dung?
- [ ] `CPI` ổn mà `CPL` tăng: đã in **cả hai** khả năng và cách phân biệt (§5) chưa?
- [ ] ⛔ Không có file ads: có con số `CPI`/`CPL` nào bị viết ra không?
- [ ] Bảng **"post hứa gì ↔ khách hỏi gì"** có chưa? Đây là phần giá trị nhất, ⛔ đừng bỏ
- [ ] Post dưới 10 HT có bị xếp hạng không?
- [ ] Dòng `L2.5` (ngoài 7 tỉnh/thành) có số chưa?
- [ ] Mốc KPI: có mốc nào tự đặt không? Mốc kế thừa đã ghi rõ **chưa được Paris xác nhận** chưa?
