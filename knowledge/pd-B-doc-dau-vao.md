# pd-B · ĐỌC ĐẦU VÀO · ẨN DANH · KIỂM MẪU

> Sổ này nói: nhận file gì, khuôn nào, thiếu gì thì dừng, và **tám thứ phải bỏ trước khi ghi ra bất cứ đâu**.

---

## 1. BA DÒNG ĐẦU VÀO

| Dòng | File | Bắt buộc | Thiếu thì sao |
|---|---|---|---|
| ① | `du-lieu/hoi-thoai.md` | ✅ | ⛔ Dừng. Không có hội thoại thì không có gì để đọc |
| ② | `du-lieu/ads-facebook.csv` | 🔶 nên có | Luồng I **vẫn chạy** nhưng ⛔ không có mục số ads, mọi bảng ghi `⚠ chưa có số ads` |
| ③ | `du-lieu/danh-sach-post.csv` | ⬜ tuỳ | Thiếu thì nối hội thoại ↔ post **chỉ bằng thẻ trong hội thoại** (§2) |

⚠️ Thư mục `du-lieu/` **đã bị `.gitignore` chặn**. ⛔ Không commit dữ liệu khách.

---

## 2. DÒNG ① — KHUÔN HỘI THOẠI

Khuôn này **giống `Paris-Agent-Factory/doc/mau-du-lieu/MAU_Hoi-thoai.md`** — cùng một bản xuất, ⛔ không đổi khuôn:

```
## <STT>. <Tên KH> — <DD/MM HH:MM>
- Phụ trách: <tên NV> · Có SĐT: <Có|Không> · Số tin: <n>
- **<DD/MM HH:MM> KH:** <nội dung khách>
- **<DD/MM HH:MM> NV (<tên NV>):** <nội dung nhân viên>
```

| Trường | Bắt buộc | Dùng để | Luồng |
|---|---|---|---|
| Số thứ tự → `HT-nnn` | ✅ | Truy ngược — mọi hook, mọi ô `✗` phải chỉ về được `HT-nnn` | I · Q |
| Dấu thời gian **từng tin** | ✅ | `TC-1` phản hồi ≤2' · khung giờ · tốc độ | Q |
| `KH:` / `NV (<tên>):` | ✅ | Tách hai nửa hội thoại · gán nhân viên | I · Q |
| `Phụ trách` | ✅ | Gộp điểm theo người | **Q** |
| `Có SĐT` | ✅ | Chỉ số lõi `% có SĐT` · tín hiệu ⑤ | I · Q |
| `Số tin` | 🔶 | Kiểm xem bản xuất có bị cắt không | — |

### ★ Thẻ nguồn quảng cáo — lợi thế của bản xuất Paris

```
- **03/10 09:12 KH:** [Thẻ: Inbox từ quảng cáo QC_Implant_Straumann – Trồng răng Implant trụ Straumann, ăn nhai như răng thật]
```

> ★ **Thẻ nằm ngay trong hội thoại**, nên nối hội thoại ↔ post được chính xác **1:1**. ⛔ Không phải khớp bằng thời gian rồi đoán — cách đó sai nhiều.

Từ thẻ lấy ra hai thứ, ⛔ không gộp:

| Lấy ra | Ví dụ | Dùng để |
|---|---|---|
| `post_ads` — **mã post** | `QC_Implant_Straumann` | Nối với dòng ② để ra CPI/CPL theo post |
| `loi_hua_post` — **lời hứa của post** | *"ăn nhai như răng thật"* | ★ Đối chiếu **post hứa gì** ↔ **khách hỏi gì ngay sau đó** (`pd-I3` §5) |

★ **`loi_hua_post` là cột đắt nhất của luồng I.** Nó cho đọc được câu: *"post hứa `nụ cười mới chỉ sau 1 lần hẹn`, và 9/11 khách vào từ post đó hỏi giá ở tin đầu rồi rơi"* — một kết luận về **nội dung**, không về người.

### Ba thứ trong ngoặc vuông ⛔ KHÔNG phải chữ khách gõ

`[Ảnh]` · `[Tệp]` · `[Thẻ: …]`

⚠️ Chúng ⛔ không được tính vào độ dài tin khách, ⛔ không được trích dẫn như lời khách. Nhưng `[Ảnh]` **có** tính cho **tín hiệu ④** (gửi ảnh răng / phim) — xem `pd-I2` §4.

---

## 3. ⛔ TÁM THỨ PHẢI BỎ TRƯỚC KHI GHI RA BẤT CỨ ĐÂU

```
tên thật khách · số điện thoại · ảnh khách · email · địa chỉ nhà
link Facebook cá nhân · mã đơn/mã hồ sơ · tên người nhà khách nhắc tới
```

Trích dẫn trong mọi đầu ra phải ở dạng **đã ẩn danh**: chỉ còn `HT-nnn` + nội dung câu nói.

⚠️ Luật này áp cho **cả hai luồng**, kể cả **sổ tay riêng** của nhân viên. Sổ tay là tài liệu kèm cặp, ⛔ không phải bản lưu hồ sơ khách.

★ **Hai cái dễ lọt nhất ở ngành nha:**

| Dễ lọt | Vì sao | Xử thế nào |
|---|---|---|
| **Vị trí răng + mốc thời gian** | *"mất răng số 6 hàm dưới bên phải 2 năm"* là **mô tả nhận dạng được** khi nhóm chỉ có 1–2 HT | Nhóm dưới 10 HT → rút về *"mất răng hàm dưới"*, bỏ số răng và mốc năm |
| **Tên người nhà** | *"bố em 68 tuổi"*, *"vợ em cũng muốn làm"* | Giữ quan hệ + tuổi (**cần cho chân dung**), ⛔ bỏ mọi tên riêng |

⚠️ ⛔ **Không nạp CCCD · hồ sơ bệnh án · ảnh X-quang của khách lên công cụ công cộng** — kế thừa `np-rao-phap-ly`.

---

## 4. CÁC Ô TỰ SUY RA — ⛔ KHÔNG HỎI NGƯỜI DÙNG

Agent tự suy, ⛔ không được hỏi lại anh:

`v_rang` · `nhom_gt` · `l_code` · `giai_doan` · `rao_can` · `bitmask` · `do_nong` · `cau_hoi_ngam` · `post_ads` · `loi_hua_post` · `10 ô TC` · `co_do` · `loi_he`

### ⛔ Hai ô KHÔNG nằm trong danh sách này

| Ô | Vì sao không suy ra được |
|---|---|
| **`cd` — chân dung của kỳ** | Chân dung ⛔ không suy ra được từ một ô dữ liệu. Nó được **phác họa từ chữ của khách** rồi anh duyệt ở **CỔNG 0** (`pd-I1` §1–2). Trước khi duyệt, `cd` của mọi hội thoại để `null` |
| **`loi_nguoi_hay_loi_he`** cho ô `TC-9` giá | Phụ thuộc việc **bảng giá đã cấp cho dịch vụ đó chưa** — là dữ kiện **ngoài hội thoại**. Agent chấm `?` và in ra danh sách chờ đối chiếu (`pd-Q1` §5) |

---

## 5. DÒNG ② — SỐ QUẢNG CÁO FACEBOOK

Cột tối thiểu:

| Cột | Bắt buộc | Dùng để |
|---|---|---|
| `ngay` | ✅ | Khớp kỳ |
| `ma_post` / `ten_quang_cao` | ✅ | ★ Nối với `post_ads` của dòng ① |
| `chi` (VNĐ) | ✅ | Gốc của mọi chỉ số |
| `hien_thi` (impressions) | ✅ | CPM |
| `click` | 🔶 | CTR |
| `tin_nhan` (số inbox) | ✅ | CPI — chỉ số lõi |
| `dich_vu` | 🔶 | Cắt theo `V-xx` |
| `co_so` / `tinh` | 🔶 | ★ Cắt theo 7 tỉnh/thành — xem `pd-E` §3 |

Chuỗi chỉ số, tính theo đúng thứ tự này:

```
Chi → CPM → CTR → CPI → CPL → CP-ĐẶT-LỊCH → CP-ĐẾN-KHÁM
```

⚠️ **Hai mốc cuối là của ngành nha, ⛔ không bỏ:**
- `CPL` = chi ÷ số có SĐT
- `CP-ĐẶT-LỊCH` = chi ÷ số đặt lịch khám
- `CP-ĐẾN-KHÁM` = chi ÷ số **đến khám thật**

> ⛔ **Không được lấy "đặt lịch" thay cho "đến khám".** Dữ liệu không có cột đến khám → ghi `⚠ chưa đo được show-up` và **để trống**, ⛔ không suy ra. Ngành nha rò nặng nhất ở chính khe này (`P3` §3).

---

## 6. KIỂM MẪU — BỐN CÂU TRƯỚC KHI ĐỌC

Chạy trước `ĐỌC`, in kết quả ra đầu báo cáo:

```
① CỠ MẪU      : bao nhiêu HT · bao nhiêu bị loại · vì sao loại
② KHOẢNG NGÀY : ngày đầu → ngày cuối. Lệch với kỳ anh khai → hỏi lại
③ MẪU BỊ LỌC? : file có HT nào chỉ 1 lượt khách không?
                 ⛔ KHÔNG CÓ hội thoại ngắn là dấu hiệu file đã bị lọc
④ PHÂN BỐ NV  : mỗi nhân viên bao nhiêu HT → ai đủ 10 để phân loại
```

★ **Câu ③ là câu hay bị bỏ qua nhất.** Bản xuất chỉ gồm *"hội thoại dài"* hoặc *"hội thoại có số"* thì:

> Hội thoại dài = khách tương tác nhiều = **đã thiên về phía nóng**. Nó thổi phồng mọi post, và thổi **không đều nhau** → ghi cảnh báo, ⛔ **không dùng để quyết ngân sách**.

Và một hệ quả riêng cho luồng Q: file đã lọc bỏ hội thoại ngắn thì **mọi nhân viên đều trông giỏi hơn thực tế**, vì những hội thoại họ làm rơi sau một lượt đã bị loại khỏi mẫu. ⚠️ Trường hợp này ⛔ **không phân loại A/B/C/D**, chỉ chấm từng hội thoại.

---

## 7. HỘI THOẠI BỊ LOẠI — GHI RÕ, ⛔ KHÔNG ÂM THẦM BỎ

| Loại khỏi mẫu khi | Ghi nhãn |
|---|---|
| ⛔ Không có lượt nào của khách (chỉ tin tự động) | `loai: khong-co-loi-khach` |
| ⛔ Không có lượt nào của nhân viên **và** khách chỉ nhắn 1 lượt | `loai: chua-duoc-cham` → ★ đây là **con số phải báo riêng**, không phải rác |
| Spam · bán hàng · tuyển dụng · khách hỏi việc làm | `loai: ngoai-pham-vi` |
| Khách cũ hỏi lịch tái khám, ⛔ không có nhu cầu mới | `loai: cs-tai-kham` → vào mục `CS`, không vào phễu |

★ **Dòng `chua-duoc-cham` là một phát hiện, không phải mẫu bị loại.** Khách nhắn một câu rồi ⛔ không ai trả lời — đó là lead mất trắng. Nó ⛔ không được chấm vào điểm ai (không có gì để chấm), nhưng **phải có số và phải nằm ở đầu báo cáo QC** dưới mục *"việc hệ thống: tin chưa được chạm"*.

---

## 8. TỰ KIỂM SỔ NÀY

- [ ] Đã in **bốn câu kiểm mẫu** §6 ra đầu báo cáo chưa?
- [ ] Tám thứ của §3 đã bỏ hết chưa — kể cả trong **sổ tay riêng**?
- [ ] Nhóm dưới 10 HT: vị trí răng + mốc thời gian đã rút gọn chưa?
- [ ] `cd` của mọi hội thoại còn `null` trước CỔNG 0 chưa?
- [ ] Thẻ `[Thẻ: …]` đã tách thành **hai** cột `post_ads` và `loi_hua_post` chưa?
- [ ] Cột "đến khám" không có → đã ghi `⚠ chưa đo được show-up` và để **trống** chưa, hay đã lấy "đặt lịch" thay?
- [ ] Số HT `chua-duoc-cham` đã báo riêng chưa?
