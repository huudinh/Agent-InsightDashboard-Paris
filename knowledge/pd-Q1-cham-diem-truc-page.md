# pd-Q1 · ★★ CHẤM ĐIỂM TRỰC PAGE · 10 TIÊU CHÍ

> Sổ nhạy cảm nhất của repo. Nó tạo ra một con số gắn với **tên một con người**.
> ⛔ Chưa đọc hết §1 và §6 thì ⛔ không được chấm.

---

## 1. VÌ SAO AGENT NÀY CHẤM ĐIỂM SỐ CÒN `Agent-QC-Telesale` THÌ ⛔ KHÔNG

`Agent-QC-Telesale` cố tình **không** cho điểm số, vì cuộc gọi có nhóm *giọng & ngữ điệu* — nhóm chỉ chấm được khi có audio, mà bản ghi hay mất tiếng. Điểm số ở đó tạo cảm giác chính xác mà dữ liệu ⛔ không có.

Chat thì khác ở ba điểm:

```
① Bằng chứng ĐẦY ĐỦ — mọi chữ đều được lưu, ⛔ không có "mất tiếng".
② Mốc thời gian CHÍNH XÁC đến phút — SLA đo được, ⛔ không phải cảm nhận.
③ ⛔ Không nhóm nào phụ thuộc âm thanh — mọi tiêu chí đều đọc được từ văn bản.
```

Nhưng điểm số vẫn chỉ hợp lệ khi đi kèm **bốn rào an toàn ở §6**. ⛔ Bỏ một rào là sổ này thành **công cụ kỷ luật**, ⛔ không còn là công cụ kèm cặp.

⚠️ **Và một luật riêng của repo này:** điểm cá nhân ⛔ **không bao giờ đi vào đầu ra của luồng I** (`pd-F` §3). Luồng Q có quyền biết tên; luồng I ⛔ không.

---

## 2. CÁCH CHẤM — HAI TẦNG

```
TẦNG 1 · từng hội thoại : mỗi tiêu chí TC-1…TC-10 chấm ✓ / ✗ / — / ?
TẦNG 2 · từng nhân viên : quy ra điểm 0–10 khi đủ mẫu, rồi phân loại A/B/C/D
```

| Ký hiệu | Khi nào | Tính thế nào |
|---|---|---|
| `✓` **ĐẠT** | Có bằng chứng trong hội thoại | Tính 1 |
| `✗` **CHƯA ĐẠT** | Có bằng chứng là **không làm** hoặc **làm sai** | Tính 0 |
| `—` **KHÔNG ÁP DỤNG** | Tình huống ⛔ không phát sinh, **hoặc lỗi hệ** | ⛔ **Loại khỏi mẫu số**, ⛔ không tính là trượt |
| `?` **CHỜ ĐỐI CHIẾU** | ★ Cần dữ kiện **ngoài hội thoại** mới kết luận được | ⛔ Loại khỏi mẫu số, **in ra danh sách chờ** (§5) |

### Công thức

```
Điểm một hội thoại = (số ✓) ÷ (số ✓ + số ✗) × 10        ← thang 10 của P8 §6
Điểm một nhân viên = trung bình điểm các hội thoại của người đó trong kỳ
```

⚠️ `—` **⛔ không phải** `✗`. Gộp hai cái này là cách làm cho một nhân viên trông tệ chỉ vì khách của bạn ấy ⛔ không hỏi giá.

⚠️ `?` **⛔ không phải** `✗`. Đây là ký hiệu riêng của repo này, thêm vào vì ngành nha có nhiều dữ kiện **chưa được Paris cấp** (`pd-E` §7) — và ⛔ không có ký hiệu này thì mọi ô đó sẽ bị chấm `✗` oan.

---

## 3. ★ MƯỜI TIÊU CHÍ — ÁNH XẠ 1:1 VỚI `P8` §6

⚠️ **`P8` thắng khi mâu thuẫn.** `P8` sửa thì sổ này sửa theo.

> ⚠️ **Sửa một tiêu chí thì sửa ở BA chỗ CÙNG LÚC:** sổ này · `tools/tu_dien.json` (bộ từ khoá nhận diện) · `tools/pd.py` (hàm `cham_tc`). Thang điểm nằm nhiều chỗ mà lệch nhau thì ⛔ **không ai biết báo cáo đang chấm theo bản nào** — và lệch kiểu đó ⛔ không có cách nào phát hiện từ bên ngoài, vì mọi bảng vẫn khớp tổng.

| Mã | `P8` | Tiêu chí | Đạt khi | Trượt là lỗi gì |
|---|---|---|---|---|
| **`TC-1`** | ① | **Phản hồi ≤ 2 phút** | Chênh lệch dấu thời gian tin khách → tin NV đầu tiên ≤ 2'. ★ Chỉ trong **8h30–18h30**; ngoài giờ → `—` (§4) | Người, nếu trong giờ |
| **`TC-2`** | ② | **Gọi đúng tên dịch vụ/tình trạng** theo post khách bấm vào | Tin mở nhắc đúng dịch vụ. ⛔ Không hỏi chung *"cần tư vấn gì"* | Người |
| **`TC-3`** ★ | ③ | **Thu đủ 4 thông tin** | Tình trạng (**vị trí · bao lâu**) · đã điều trị ở đâu chưa · mong muốn · thời gian dự kiến | Người |
| **`TC-4`** ★ | ④ | **Tạo tin cậy bằng bằng chứng**, đúng rào cản khách mang | ≥1 bằng chứng **thật** (`pd-E` §2), ⛔ không chỉ tính từ | Người, hoặc **hệ** nếu bằng chứng chưa được cấp |
| **`TC-5`** | ⑤ | **Xin số có lý do có lợi cho khách** | *"để bác sĩ xem phim, báo lộ trình sát"*. ⛔ Không phải *"để gửi ưu đãi"* | Người |
| **`TC-6`** | ⑥ | **Xác thực số / Zalo** | Có hỏi lại số có Zalo không, hoặc xác nhận đúng số | Người |
| **`TC-7`** | ⑦ | **Phân loại HOT/WARM/COLD + nhóm giá trị `V`** | Có ghi chú phân loại, ⛔ không để trống | ★ Thường là **hệ** — xem §4 |
| **`TC-8`** | ⑧ | **Phiếu bàn giao đủ 13 trường** (`pd-E` §3) | Đủ 13 trường | ★ Thường là **hệ** — xem §4 |
| **`TC-9`** 🔴 | ⑨ | ⛔ **Không từ cấm · ⛔ không gắn *"chính hãng"* sai · ⛔ không chốt giá cứng** | ⛔ Không vi phạm | ★ **Cờ đỏ** — xem §7 |
| **`TC-10`** | ⑩ | **Nêu rõ bước tiếp theo** | **Ai gọi · số nào · lúc mấy giờ** | Người |

### Ba tiêu chí đáng nói riêng

★ **`TC-3` là tiêu chí của ngành nha.** Thẩm mỹ cần 2 thông tin; nha khoa cần 4, trong đó hai cái riêng: **vị trí răng & thời gian bị** và **đã điều trị ở đâu chưa**. ⛔ Thiếu hai mục này thì CSKH gọi điện phải hỏi lại khách từ đầu, và **⛔ không phát hiện được ca `V-01` làm lại** — ca mà cách tư vấn hoàn toàn khác.

★ **`TC-4` là tiêu chí trượt nhiều nhất, và cũng là tiêu chí dễ chấm sai nhất.** Phải tách hai loại trượt:
- **lỗi người** — bằng chứng **đã có trong tay** (đối tác hãng, giấy phép, công nghệ) mà vẫn trả lời bằng tính từ;
- **lỗi hệ** — bằng chứng **chưa được cấp** (số năm bảo hành, case có giấy đồng ý, bảng giá dòng sứ) → chấm `—` hoặc `?`.

★ **`TC-9` trượt thì ⛔ toàn hội thoại 0 điểm**, bất kể 9 tiêu chí kia. Đây là **rủi ro pháp lý, ⛔ không phải lỗi kỹ năng** (`P8` §6). Và nó luôn kèm một cờ đỏ (`pd-Q2`).

---

## 4. ★★ LỖI HỆ — BẢNG TRA, ⛔ ĐỪNG CHẤM `✗`

> ⚠️ Đây là rào hay bị quên nhất, và nó làm sai lệch điểm nhiều nhất.

| Tình huống | Ô | Chấm | Đẩy lên |
|---|---|---|---|
| Khách nhắn **sau 18h30 hoặc trước 8h30** | `TC-1` | `—` | ★ *"Khách nhắn ngoài giờ `n` lượt"* → **cân nhắc ca trực tối** |
| Khách hỏi giá dòng trụ/dòng sứ **chưa có trong bảng giá** | `TC-9`, `TC-4` | `?` | *"Chưa cấp bảng giá theo dòng"* |
| Khách hỏi **số năm bảo hành** | `TC-4` | `—` | *"Chưa cấp chính sách bảo hành theo dịch vụ"* |
| Khách xin **ảnh before–after** | `TC-4` | `—` | *"Chưa có danh sách case có giấy đồng ý"* |
| Khách tỉnh hỏi **All-On / ghép xương** | `TC-4` | `—` | *"Chưa có danh sách cơ sở đủ năng lực"* |
| ★ Bản xuất **⛔ không có phần ghi chú bàn giao** | `TC-8` | `—` | *"⚠ ⛔ không đo được `TC-8`"* — `P6` §5 |
| ★ Bản xuất **⛔ không có ô phân loại** | `TC-7` | `—` | *"⚠ ⛔ không đo được `TC-7`"* |
| Khách hỏi **bệnh nền / thuốc đang dùng / chống chỉ định** | `TC-4` | `—` | ⛔ Phải bác sĩ. Nhân viên **đúng** khi ⛔ không trả lời |

### ★ Hai ô `—` mặc định mà ⛔ đừng quên

> `TC-7` và `TC-8` chấm được **chỉ khi bản xuất có phần ghi chú của nhân viên**. Bản xuất chat thuần ⛔ **không có** hai thứ đó.
>
> ⛔ **Chấm `✗` cho `TC-7`/`TC-8` trên một bản xuất ⛔ không chứa ghi chú là cho 0 điểm oan cho cả khối.** Kiểm một lần ở đầu kỳ: bản xuất có ghi chú không? ⛔ Không có → cả hai ô là `—` cho **mọi** hội thoại, và ghi rõ ở đầu báo cáo *"kỳ này chấm trên 8 tiêu chí"*.

---

## 5. ★ Ô `?` — DANH SÁCH CHỜ ĐỐI CHIẾU

Ô `?` ⛔ không được để lại trong báo cáo mà ⛔ không giải quyết. Cuối `Q1`, in **danh sách chờ**:

```
DANH SÁCH CHỜ ĐỐI CHIẾU — n ô

① TC-9 · HT-019 · "bọc sứ Nacera 4 răng khoảng 24 triệu"
   → Hỏi: bảng giá hiện hành có dòng Nacera chưa, và con số có khớp?
   → Nếu CÓ và KHỚP     → TC-9 = ✓
   → Nếu CÓ và LỆCH     → TC-9 = ✗ + cờ đỏ CĐ-P5 (nói giá lệch bảng)
   → Nếu CHƯA CẤP       → TC-9 = — , vào "việc hệ thống"
   → Người đối chiếu: <Marketing/Kế toán — người giữ bảng giá>
```

★ **Mỗi ô `?` phải có: `HT-nnn` · nguyên văn · câu hỏi cần trả lời · ba nhánh kết luận · người đối chiếu.** ⛔ Không đủ năm thứ đó thì ô `?` thành ô bị bỏ quên, và kỳ sau ⛔ không ai nhớ.

⚠️ **Hai nhân viên báo hai giá khác nhau cho cùng dịch vụ trong cùng kỳ** → đó ⛔ **không phải ô `?`**, đó là **phát hiện phải đưa lên đầu báo cáo** (`P4` §4). Nó là lỗi hệ (chưa chốt giá) hoặc lỗi đào tạo, ⛔ không phải lỗi một người.

---

## 6. ★★ BỐN RÀO AN TOÀN — ⛔ BỎ MỘT CÁI LÀ SỔ NÀY VÔ HIỆU

```
① ĐIỂM ĐỂ KÈM CẶP, ⛔ KHÔNG ĐỂ KỶ LUẬT.
   Mọi bảng điểm phải mang đúng câu này ở chân bảng:
   "Điểm dùng để phân việc kèm cặp. Không phải căn cứ kỷ luật hay
    xếp hạng công khai."

② MỖI ĐIỂM TRỪ PHẢI CÓ BẰNG CHỨNG.
   Một ô ✗ ⛔ không gắn được HT-nnn + CẶP CÂU nguyên văn
   (câu khách + câu NV trả lời ngay sau) → đổi thành "—".
   ⛔ Không có bằng chứng thì ⛔ không có điểm trừ.

③ LỖI HỆ ⛔ KHÔNG TRỪ ĐIỂM NGƯỜI.
   Bảng tra ở §4. Chấm "—" hoặc "?", đẩy lên mục "việc hệ thống",
   ⛔ KHÔNG trừ nhân viên.

④ ⛔ KHÔNG XẾP HẠNG CÔNG KHAI TOÀN KHỐI.
   Dashboard QC hiện phân bố A/B/C/D và chỉ số cả đội.
   Tên + điểm cá nhân CHỈ xuất hiện trong sổ tay RIÊNG của người đó
   và bản của trưởng nhóm. ⛔ KHÔNG có bảng xếp hạng dán lên màn hình chung.
```

⚠️ **Rào ③ là rào hay bị quên nhất.** Ở ngành nha nó càng nặng, vì `pd-E` §5 đang có **sáu slot dữ kiện chưa được cấp** — nghĩa là một phần đáng kể các ô trượt `TC-4`/`TC-9` là **lỗi hệ**. Trừ điểm nhân viên vì chuyện đó là **chấm sai người**.

★ **Rào ⑤ của riêng repo này** (thêm vào, ⛔ không thay thế bốn rào trên):

```
⑤ ⛔ KHÔNG CHẤM BẰNG THỨ NHÂN VIÊN ⛔ KHÔNG BIẾT.
   Chân dung của kỳ (CD), hook, số ads ⛔ KHÔNG được đưa vào bảng chấm.
   Nhân viên trả lời khách TRƯỚC khi chân dung tồn tại.
   → pd-F §6, chiều ngược của tường ngăn.
```

---

## 7. PHÂN LOẠI A / B / C / D

| Loại | Điểm /10 | Nghĩa vận hành | Sổ tay nhận được |
|---|---|---|---|
| 🟢 **A** | **≥ 9,0** | Làm chuẩn. Dùng hội thoại của người này làm mẫu cho khối | **Mẫu lan toả** — 1 việc nâng cấp + 2 đoạn chat mẫu để chia sẻ |
| 🔵 **B** | **8,0 – 8,9** | ★ **Đạt chuẩn `P8`** (≥8/10), hụt 1–2 tiêu chí | Sửa đúng **một** tiêu chí yếu nhất |
| 🟡 **C** | **6,5 – 7,9** | Dưới chuẩn, cần kèm | **2 việc** + kịch bản mẫu + kèm cặp theo tuần |
| 🔴 **D** | **< 6,5** | Đang làm mất lead đều đặn | **1 việc duy nhất** + ngồi cùng trưởng nhóm đọc lại 5 hội thoại |

⚠️ **Một cờ đỏ trong kỳ → hội thoại đó 0 điểm** (`TC-9`, `P8` §6), và nhân viên ⛔ **không được xếp loại A** dù điểm trung bình cao.

### Điều kiện đủ mẫu — ⛔ không hạ ngưỡng

| Số HT của một nhân viên | Agent được làm gì |
|---|---|
| **< 5** | ⛔ Không chấm. Ghi `chưa đủ mẫu` |
| **5 – 9** | Chấm từng hội thoại, ⛔ **không cho điểm tổng, ⛔ không phân loại** |
| **≥ 10** | ✅ Điểm tổng + phân loại |
| **≥ 10 và liên tục 2 kỳ** | ✅ Vẽ xu hướng, so kỳ trước |

⚠️ Nhân viên có **ca trực lệch giờ** (ca tối) thì `TC-1` tính theo **khung giờ của ca đó**, ⛔ không dùng khung chung 8h30–18h30.

⚠️ **Mẫu bị lọc** (`pd-B` §6 câu ③) → ⛔ **không phân loại A/B/C/D**, chỉ chấm từng hội thoại. File đã bỏ hội thoại ngắn thì mọi nhân viên đều trông giỏi hơn thực tế.

---

## 8. ĐẦU RA CHUẨN CỦA LUỒNG Q

```
① PHÂN BỐ        : số người loại A/B/C/D + số người chưa đủ mẫu
② CHỈ SỐ ĐỘI     : % đạt từng tiêu chí TC-1…TC-10 — đây là thứ lên dashboard
③ BẢNG CÁ NHÂN   : tên · số HT · điểm · loại · tiêu chí yếu nhất · mạnh nhất
                   ⛔ CHỈ vào sổ tay riêng + bản trưởng nhóm
④ CỜ ĐỎ          : từng cờ · ai · HT-nnn · nguyên văn · người xử lý đích danh
⑤ VIỆC HỆ THỐNG  : các ô "—" do lỗi hệ, gom theo nguyên nhân (§4)
                   + số HT "chưa được chạm" (pd-B §7)
⑥ DANH SÁCH CHỜ  : các ô "?" (§5)
⑦ BA TIÊU CHÍ YẾU NHẤT CỦA KHỐI → thành nội dung đào tạo kỳ sau
```

★ **Ô ② là thứ duy nhất của luồng Q được lên dashboard công khai trong khối** — và nó ⛔ không có tên ai. Ô ③ ⛔ không lên dashboard.

---

## 9. TỰ KIỂM SỔ NÀY

- [ ] Mọi `✗` có `HT-nnn` + **cặp câu** nguyên văn chưa?
- [ ] ★ Có ô nào là **lỗi hệ** (§4) mà bị chấm `✗` không?
- [ ] ★ Bản xuất có ghi chú bàn giao không? ⛔ Không có mà vẫn chấm `✗` cho `TC-7`/`TC-8`?
- [ ] `—` và `?` có bị cộng vào **mẫu số** không?
- [ ] Mọi ô `?` có đủ **năm thứ** của §5 chưa?
- [ ] Người dưới 10 HT có bị phân loại không?
- [ ] Mẫu bị lọc mà vẫn phân loại A/B/C/D không?
- [ ] `TC-9` trượt: hội thoại đó có về **0 điểm** chưa, và có cờ đỏ kèm chưa?
- [ ] Câu *"Điểm dùng để kèm cặp…"* có ở chân **mọi** bảng điểm chưa?
- [ ] Có bảng xếp hạng cá nhân nào lọt ra ngoài sổ tay riêng không?
- [ ] ★ Có chân dung `CD` / hook / số ads nào lọt vào bảng chấm không? (rào ⑤ §6)
