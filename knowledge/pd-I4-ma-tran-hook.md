# pd-I4 · MA TRẬN ƯU TIÊN · CỔNG 1 · NGÂN HÀNG HOOK

> Đầu ra cuối của luồng I. Sổ này biến chân dung + insight thành **thứ tự việc phải làm** và **câu chữ dùng được ngay**.

---

## 1. ★ MA TRẬN ƯU TIÊN — ĐỘ NÓNG × NHÓM GIÁ TRỊ

> ⚠️ **Đây là điểm khác biệt quan trọng nhất giữa báo cáo nha khoa và báo cáo thẩm mỹ.**
> Dải giá dịch vụ nha khoa rộng gấp nhiều lần: một ca All-On và một ca cạo vôi ⛔ không thể xếp cùng mức ưu tiên dù cả hai đều `HOT`.

|  | **V1** · Implant · All-On · Invisalign · sứ toàn hàm | **V2** · sứ 1–6 răng · Veneer · mắc cài | **V3** · cạo vôi · tẩy trắng · trám · nhổ · trẻ em |
|---|---|---|---|
| **HOT** | 🔴 Ưu tiên tuyệt đối · người giỏi nhất · gọi ngay | 🟠 Gọi theo SLA | 🟡 Chốt lịch nhanh gọn, ⛔ **không dồn người giỏi nhất** |
| **WARM** | 🔴 ★ **Nuôi kỹ — giá trị kỳ vọng cao hơn `HOT·V3`** | 🟠 Nuôi theo nhịp | 🟡 Nhắn Zalo, mời khám định kỳ |
| **COLD** | 🟠 **Nuôi dài hạn, ⛔ không bỏ** · gửi nội dung giáo dục | 🟡 Nuôi theo nhịp chung | ⚪ Tệp remarketing |

### Ba câu phải nhớ khi viết khuyến nghị

```
① MỘT LEAD HOT CỦA CẠO VÔI ⛔ KHÔNG BẰNG MỘT LEAD WARM CỦA ALL-ON
   về giá trị kỳ vọng — nhưng vẫn đáng chăm, vì đó là cửa vào LTV.

② V1 ⛔ KHÔNG ĐƯỢC ĐÁNH GIÁ BẰNG TỐC ĐỘ CHỐT.
   Chu kỳ quyết định Implant/All-On/Invisalign tính bằng TUẦN–THÁNG,
   hay có người nhà tham gia. COLD ở V1 vẫn phải nuôi dài —
   đây là chỗ mất tiền nhiều nhất nếu bỏ.
   → L6.x · V1 nuôi tới 90 NGÀY, ⛔ không cắt ở 30 ngày (P6 §4).

③ V3 ĐO BẰNG TỶ LỆ ĐẾN KHÁM, ⛔ KHÔNG BẰNG DOANH THU CA ĐÓ.
   Mục tiêu của V3 là ĐẾN KHÁM và phát sinh dịch vụ tiếp theo.

→ Báo cáo nào xếp hạng lead CHỈ bằng độ nóng là báo cáo sai hướng
  cho ngành nha. Gộp V1/V2/V3 lại thì nhóm V3 (đông, dễ chốt)
  sẽ CHE MẤT việc V1 đang rò.
```

---

## 2. BẢNG VIỆC — XẾP THẾ NÀO

Mỗi việc một dòng, đủ bảy cột:

| Cột | Nội dung |
|---|---|
| `#` | Thứ tự ưu tiên |
| **Việc** | Một câu, động từ trước |
| **Vì sao** | ★ `n/m` HT + `HT-nnn` làm bằng |
| **Nhắm ai** | `CD` + `V1/V2/V3` + rào cản |
| **Chặn gì** | Rào cản nào được gỡ |
| **Ai làm** | Marketing / Hệ thống — ⛔ **không bao giờ là tên nhân viên** |
| **Đo bằng** | Chỉ số kỳ sau sẽ nhìn |

### Xếp theo gì

```
Mặc định: ĐỘ CHẶN × GIÁ TRỊ
  độ chặn = số HT bị rào cản đó chặn
  giá trị = V1 > V2 > V3

⚠ ⛔ KHÔNG tự phát minh hệ số rồi nhân ra "điểm ưu tiên".
   Một con số do agent bịa hệ số thì không ai kiểm lại được,
   và nó trông chính xác hơn dữ liệu thật rất nhiều.

★ Cách đúng: xếp theo ĐỘ CHẶN, rồi trong cùng mức độ chặn
   thì V1 lên trước. Và NÓI RÕ đã xếp theo cách đó.
```

⚠️ **Khi kỳ ⛔ không có dữ liệu tỷ lệ chốt** (chưa đo được show-up, chưa có số ads), thì ⛔ không xếp được theo giá trị kỳ vọng thật. Lúc đó xếp theo **độ chặn thuần**, và ghi thẳng: *"Kỳ này xếp theo **độ chặn**, ⛔ chưa xếp theo giá trị kỳ vọng vì chưa đo được show-up."*

---

## 3. ★ CỔNG 1 — DỪNG VÀ CHỜ

Ma trận xong → agent **in ra rồi dừng**. ⛔ Không viết hook.

```
① BẢNG VIỆC đã xếp (§2), kèm cách xếp
② BA VẤN ĐỀ CỐT LÕI (pd-I2 §5)
③ MỤC VIỆC HỆ THỐNG — riêng, có tên người chịu trách nhiệm cấp dữ kiện
④ Số việc dự kiến sinh hook cho (⛔ không phải tất cả)
```

| Anh gõ | Agent làm gì |
|---|---|
| `DUYỆT` | Chạy `I5` — sinh hook cho các việc đã duyệt |
| `BỎ <n>` | Bỏ việc đó khỏi bảng, in lại, **chờ tiếp** |
| `ĐỔI THỨ TỰ …` | Xếp lại, in lại, **chờ tiếp** |
| `CHỈ LÀM <n>, <m>` | Chỉ sinh hook cho hai việc đó |

> ⛔ **Viết 30 hook cho đúng tệp mà khối ⛔ không định làm là ném đi một tuần.** Đó là lý do duy nhất của cổng này.

---

## 4. NGÂN HÀNG HOOK — MỘT HOOK CÓ GÌ

| Ô | Yêu cầu |
|---|---|
| **Mã** | `HK-nn` |
| **Câu hook** | ★ 1–2 câu, **chữ của khách**, ⛔ không phải chữ marketing |
| **Nhắm** | `CD` + `V-xx` + `V1/V2/V3` |
| **Gỡ rào** | `SỢ`/`NGỜ`/`NGẠI` + `L6.x` |
| **Chặng** | `S1` / `S2` / `S3` — ★ hook cho `S3` khác hẳn hook cho `S1` |
| **Bằng chứng kèm** | Bằng chứng thật của Paris (`pd-E` §2) |
| **Làm bằng** | `HT-nnn` + trích ẩn danh — câu khách **thật sự đã gõ** |
| **Cờ pháp chế** | 🟢 sạch · 🟠 cần duyệt · 🔴 chặn (§5) |

### ★ Luật gốc của hook

> **Hook phải là câu khách đã tự nói, ⛔ không phải câu ta muốn khách nghe.**

Nguyên liệu là bảng ① của `pd-I1` §2 — cụm chữ khách tự nói, ≥3 lần. Hook ⛔ không có `HT-nnn` làm bằng thì ⛔ **không phải hook**, đó là ý tưởng.

| ⛔ Chưa phải hook | ✅ Hook |
|---|---|
| *"Trồng răng Implant công nghệ Pháp, an toàn tuyệt đối"* | *"Mất răng 2 năm rồi — giờ trồng còn kịp không?"* (×11 HT) |
| *"Bọc răng sứ thẩm mỹ cao cấp"* | *"Bọc sứ thì mài mất bao nhiêu răng thật của tôi?"* (×9 HT) |
| *"Niềng trong suốt hiện đại"* | *"Em làm ngân hàng, không muốn ai thấy em đang niềng"* (×6 HT) |
| *"Trụ Straumann chính hãng"* | *"Làm sao em biết trụ trong miệng em đúng là trụ đó?"* (×7 HT) |

★ Cột cuối của bảng trên là ví dụ của khuôn thứ tư ở `pd-I3` §5: khách ⛔ không cần nghe tên hãng to hơn, khách cần **cách tự kiểm**.

### Hook theo chặng — ⛔ đừng dùng lẫn

| Chặng | Hook làm gì | ⛔ Đừng |
|---|---|---|
| `S1` nhận biết | Gọi đúng tình trạng, gieo một câu hỏi họ đang có | ⛔ Đừng mời đặt lịch ngay |
| `S2` tìm hiểu | Giải thích **cơ chế**, nêu bằng chứng | ⛔ Đừng nói giá |
| `S3` cân nhắc & nỗi sợ ★ | **Gỡ đúng rào cản** rồi mới CTA | ⛔ Đừng đưa thêm thông tin mới |

> ★ **`S3` là điểm quyết định của ngành nha.** Phần lớn lead rơi ở đây, ⛔ không rơi ở `S1`. Số hook cho `S3` nên **nhiều nhất**, và mỗi hook phải chỉ rõ gỡ `L6.x` nào.

★ **CTA mạnh nhất của ngành nha** (`pd-I3` §1): mời **đi khám + chụp phim**, nhấn rõ *"chưa phải điều trị"*. Hook `S3` ⛔ không nên CTA bằng báo giá.

---

## 5. ★★ CỜ PHÁP CHẾ TRÊN HOOK

Mọi hook phải qua bảng này **trước khi vào ngân hàng**. Nguồn: `np-rao-phap-ly` + `pd-E` §4.

| Cờ | Nghĩa | Hook có gì |
|---|---|---|
| 🟢 **Sạch** | Đăng được | ⛔ Không từ cấm · ⛔ không số ⛔ không nguồn · ⛔ không claim y khoa |
| 🟠 **Cần duyệt** | Chờ người duyệt | Có phát ngôn y khoa · có số ca/% · có before–after · có nêu *"chính hãng"* |
| 🔴 **Chặn** | ⛔ Không đăng | Có từ cấm, hoặc gắn *"chính hãng"* sai, hoặc hứa thời gian điều trị cứng |

### Bảng từ CẤM → từ ĐÚNG

| ⛔ Cấm | ✅ Thay bằng |
|---|---|
| *khỏi 100%* · *chắc chắn thành công* | *tỷ lệ thành công cao khi đúng chỉ định và chăm sóc đúng*\* |
| *niềng không bao giờ đau* · *không đau* | *giảm cảm giác khó chịu nhờ công nghệ (Piezotome, lực nhẹ), bác sĩ theo dõi từng giai đoạn* |
| *không biến chứng* · *an toàn tuyệt đối* | *quy trình vô khuẩn theo Bộ Y tế, bác sĩ ĐH Y có chứng chỉ hành nghề* |
| *số 1* · *tốt nhất* · *duy nhất* · *hàng đầu* | (bỏ) hoặc nêu USP đo được: đối tác Straumann / Invisalign Black Diamond · GP `2032/HNO-GPHĐ/CL1` |
| *răng sứ dùng vĩnh viễn* · *trọn đời* | *độ bền theo khuyến cáo của hãng, có chế độ bảo hành* |
| *cam kết kết quả như hình* | *kết quả tuỳ tình trạng răng và cơ địa, bác sĩ đánh giá riêng*\* |
| *rẻ nhất thị trường* | *chi phí minh bạch, công khai tại bảng giá, có trả góp* |
| *nụ cười hoàn hảo 100%* | *nụ cười hài hoà với khuôn mặt, bác sĩ thiết kế theo từng ca*\* |
| ★ *"chính hãng"* cho vật liệu **ngoài 4 hãng** | ⛔ Bỏ chữ đó. Chỉ dùng cho **Straumann · Invisalign · Nacera · Ormco** |
| ★ *"niềng xong trong 12 tháng"* | *thời gian tuỳ tình trạng từng ca, bác sĩ xác định sau khi chụp phim và scan* |

\* Mọi con số và cam kết mức độ phải gắn `*` dẫn **"Hiệu quả phụ thuộc cơ địa mỗi người"**.

### ★ Hai cờ 🔴 riêng của ngành nha

```
① "CHÍNH HÃNG" LÀ TUYÊN BỐ PHÁP LÝ, ⛔ KHÔNG PHẢI TỪ MARKETING.
   Chỉ 4 hãng: Straumann · Invisalign · Nacera · Ormco.
   ⛔ Không suy diễn "đối tác hãng X" thành "mọi dịch vụ đều dùng hàng hãng X".
   Vật liệu khác / không rõ hãng → bỏ chữ đó, ghi ⚠ Cần xác minh từ Paris.

② ⛔ KHÔNG HỨA THỜI GIAN ĐIỀU TRỊ CỨNG.
   "Niềng xong trong 12 tháng", "3 ngày có răng mới" — thời gian phụ thuộc
   tình trạng từng ca. Đây là cờ 🔴, ⛔ không phải 🟠.
```

### Ba thứ nữa phải gắn 🟠

| Thứ | Vì sao |
|---|---|
| **Before–After** | Chỉ case **thật đã duyệt, có giấy đồng ý**. ⚠️ Google/Meta hạn chế nhiều định dạng before–after với ngành nha. Và `pd-E` §5: Paris **chưa cấp** danh sách case có giấy đồng ý → hiện tại ⛔ **mọi hook before–after là 🟠 chờ** |
| **Tên bác sĩ** | Chỉ **3 bác sĩ** trong `pd-E` §2. Tên khác → `⚠ Cần xác minh từ Paris` |
| **Mọi con số** | Số ca · % · năm kinh nghiệm — phải có nguồn thật. ⛔ Không nguồn → ⛔ không đăng |

⚠️ **Nội dung quảng cáo dịch vụ KCB cần giấy xác nhận nội dung quảng cáo.** Chưa có số giấy → gắn 🟠, ⛔ không bật chiến dịch. Số giấy hiện là `⚠ chờ cấp` (`pd-E` §5).

---

## 6. ⛔ MỘT THỨ HOOK ⛔ KHÔNG BAO GIỜ ĐƯỢC LÀM

```
⛔ KHÔNG nêu tên đối thủ để hạ thấp.
   (Elite Dental · Thùy Anh · Nha khoa Kim · Việt Pháp · I-Dent ·
    Lạc Việt Intech · Parkway)

★ Nhưng ĐẾM thì được và nên làm: khách nói "đang xem thêm vài nơi"
  (L6.2) — đếm xem có nêu tên đơn vị nào không, đối thủ nào bị so sánh
  nhiều nhất trong kỳ. Đây là số liệu cho báo cáo điều hành.

→ So sánh trong hook phải bằng BỘ TIÊU CHÍ KHÁCH QUAN:
  cơ sở được cấp phép · bác sĩ điều trị chính là ai · vật liệu hãng nào
  · chế độ bảo hành · tái khám.
```

★ Và một luật của ngành nha, cho nhóm `V-01` làm lại ca lỗi: **⛔ không chê nơi cũ**. Khách nhóm này ngờ rất nặng, và chê nơi cũ làm họ ngờ thêm — vì họ đã từng tin một nơi rồi. Hook cho `V-01` nhấn **đánh giá lại bằng phim X-quang**, ⛔ không nhấn *"chỗ kia làm sai"*.

---

## 7. ĐẦU RA CHUẨN CỦA `I5`

```
① NGÂN HÀNG HOOK: bảng đầy đủ, xếp theo CHẶNG rồi theo RÀO CẢN
② PHÂN BỐ CỜ: bao nhiêu 🟢 / 🟠 / 🔴 — và 🔴 vì sao
③ MỤC 🟠 CHỜ DUYỆT: ai duyệt, chờ dữ kiện gì
④ TUYẾN NỘI DUNG: nhóm hook thành 3–5 tuyến, mỗi tuyến một câu mục tiêu
⑤ ⚠ KHE CÒN TRỐNG: rào cản nào ⛔ CHƯA có hook nào gỡ được,
   và vì sao — thường vì ⛔ CHƯA CÓ BẰNG CHỨNG (việc hệ thống)
```

★ **Ô ⑤ quan trọng hơn ô ①.** Một ngân hàng 30 hook mà bỏ trống rào cản chặn nhiều nhất thì ⛔ không bằng 12 hook phủ đúng. Và khe trống thường ⛔ không phải vì thiếu ý tưởng — mà vì **hệ chưa cấp bằng chứng** (số năm bảo hành, case có giấy đồng ý, bảng giá dòng sứ). Nói rõ điều đó.

---

## 8. TỰ KIỂM SỔ NÀY

- [ ] Ma trận có **cả hai trục** `độ nóng × V1/V2/V3` chưa, hay chỉ xếp theo độ nóng?
- [ ] Có hệ số nào do agent **tự phát minh** để nhân ra "điểm ưu tiên" không?
- [ ] Cột *"ai làm"* có chỗ nào ghi tên nhân viên không?
- [ ] Có dừng **thật** ở CỔNG 1 không, hay đã viết hook rồi mới xin duyệt?
- [ ] Mọi hook có `HT-nnn` làm bằng chưa? Hook nào ⛔ không có → đó là ý tưởng, chuyển mục
- [ ] Hook có dùng **chữ của khách** không, hay chữ marketing?
- [ ] Số hook cho `S3` có nhiều nhất không?
- [ ] ★ Mọi hook đã qua **bảng từ cấm** §5 chưa? Có hook nào gắn *"chính hãng"* cho vật liệu ngoài 4 hãng?
- [ ] Có hook nào hứa **thời gian điều trị cứng** không?
- [ ] Hook before–after: đã gắn 🟠 chưa (vì chưa có danh sách case có giấy đồng ý)?
- [ ] Hook nhóm `V-01` có chê nơi cũ không?
- [ ] ★ Mục ⑤ **khe còn trống** có chưa?
