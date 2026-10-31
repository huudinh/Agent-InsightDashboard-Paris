# pd-Q3 · SỔ TAY THỰC THI · VIỆC HỆ THỐNG

> Đầu ra cuối của luồng Q. Một bảng điểm ⛔ không sửa được gì; một sổ tay thì sửa được **một việc**.

---

## 1. BA LOẠI SỔ TAY — ⛔ KHÔNG TRỘN

| Sổ | Cho ai | Chứa gì | ⛔ Không chứa |
|---|---|---|---|
| **ST-CN** · cá nhân | Từng nhân viên | Điểm **của chính mình** · tiêu chí yếu nhất · việc phải làm · câu mẫu | ⛔ Điểm người khác · ⛔ tên người khác · ⛔ lời khách của người khác |
| **ST-TN** · trưởng nhóm | Trưởng nhóm trực page | Bảng cá nhân cả nhóm · phân bố A/B/C/D · cờ đỏ đích danh · ai kèm ai | ⛔ Lời khách dài · ⛔ chân dung · ⛔ hook |
| **ST-HT** · việc hệ thống | Người giữ dữ kiện (Marketing · Kế toán · Khoa chuyên môn) | Các ô `—`/`?` gom theo nguyên nhân · ai cấp · hạn | ⛔ Tên nhân viên · ⛔ điểm số |

★ **`ST-HT` ⛔ không chứa tên nhân viên** — đó là điểm khác với hai sổ kia, và là điểm hay bị làm sai. Việc hệ thống là việc của hệ thống; nhắc tên người vào đó biến nó thành lời buộc tội.

⚠️ `ST-HT` là sổ **duy nhất** của luồng Q được gửi cho người ngoài khối trực page. Nên nó phải qua kiểm tường ngăn chặt nhất (`pd-F` §4).

---

## 2. ★ MỘT `ST-CN` CÓ GÌ — SÁU PHẦN

```
① BẠN ĐANG Ở ĐÂU
   Điểm · loại · số HT trong kỳ · tiêu chí mạnh nhất · tiêu chí yếu nhất
   ⚠ ⛔ KHÔNG so với người khác. ⛔ KHÔNG nói "xếp thứ n/m".

② MỘT VIỆC (hoặc hai, nếu loại C)
   Đúng tiêu chí yếu nhất. Viết thành việc LÀM ĐƯỢC NGAY,
   ⛔ không phải lời khuyên.
   ⛔ "Cần tạo tin cậy tốt hơn"
   ✅ "Khi khách hỏi 'có chính hãng không', trả lời bằng BA THỨ
      KIỂM ĐƯỢC: tên hãng · mã trụ in trên phiếu · được xem phiếu
      trước khi cấy. ⛔ Đừng nói 'chị yên tâm'."

③ HAI ĐOẠN CHAT MẪU
   Một đoạn của chính bạn (câu bạn làm tốt) + một đoạn mẫu.
   ⚠ Đoạn "của chính bạn" phải là câu THẬT trong hội thoại của người đó.
     ⛔ Không có câu nào tốt → bỏ ô này, ⛔ ĐỪNG bịa.

④ BA CÂU ĐỪNG NÓI
   Lấy từ bảng từ cấm (pd-I4 §5), chỉ ba câu LIÊN QUAN đến
   nhóm dịch vụ người này hay gặp. ⛔ Không dán cả bảng.

⑤ ⛔ VIỆC KHÔNG PHẢI CỦA BẠN ★
   Các ô "—" lỗi hệ trong hội thoại của chính người này.
   Nói thẳng: "n ô trong kỳ của bạn là '—' vì hệ chưa cấp
   <bảng giá dòng sứ / số năm bảo hành / …>. Những ô đó
   ⛔ KHÔNG trừ điểm bạn, và ⛔ KHÔNG phải việc bạn phải sửa."

⑥ KỲ SAU NHÌN GÌ
   Đúng MỘT chỉ số. ⛔ Không phải "nâng điểm tổng".
```

★ **Phần ⑤ là phần quan trọng nhất của sổ tay này**, và là phần ⛔ không có trong sổ tay của `Agent-QC-Telesale`.

Lý do: ở ngành nha, `pd-E` §5 đang có **sáu slot dữ kiện chưa được cấp**. Nhân viên biết rõ là mình đang bị hỏi những câu mình ⛔ không có gì để trả lời. Một sổ tay ⛔ không nói ra điều đó thì **mất uy tín ngay từ trang đầu** — và khi đó bốn phần kia cũng ⛔ không được đọc.

⚠️ Phần ① ⛔ **không so sánh với người khác**, kể cả dạng *"điểm trung bình khối là 7,8"*. Rào ④ của `pd-Q1` §6.

---

## 3. SỔ TAY THEO LOẠI

| Loại | Số việc | Nhịp | Đặc biệt |
|---|---|---|---|
| 🟢 **A** | 1 việc **nâng cấp** | Tự chạy | ★ Thêm: **2 đoạn chat của người này để chia sẻ cho khối** — xin phép người đó trước |
| 🔵 **B** | 1 việc, đúng tiêu chí yếu nhất | Tự chạy, trưởng nhóm xem lại cuối kỳ | |
| 🟡 **C** | 2 việc | **Kèm cặp theo tuần** | Thêm kịch bản mẫu cho tình huống hay gặp nhất |
| 🔴 **D** | ★ **1 việc duy nhất** | Ngồi cùng trưởng nhóm đọc lại **5 hội thoại** | ⚠️ ⛔ Đừng đưa 3–4 việc. Người đang trượt nhiều nhóm ⛔ không làm được nhiều việc một lúc |

★ **Luật của loại A:** đoạn chat của người A chỉ được chia sẻ cho khối **sau khi xin phép chính người đó**. Lấy chat của ai ra làm mẫu mà ⛔ không hỏi là biến một việc khen thành một việc khó chịu.

---

## 4. ★ `ST-HT` — VIỆC HỆ THỐNG

Gom các ô `—` và `?` **theo nguyên nhân**, ⛔ không theo người, ⛔ không theo hội thoại.

| Nhóm lỗi hệ | Số ô | Ô nào | Ai cấp | Gỡ được gì |
|---|---|---|---|---|
| Chưa cấp **bảng giá theo dòng trụ / dòng sứ** | | `TC-9`, `TC-4` | Marketing / Kế toán | ★ Gỡ cả `CĐ-P5` lẫn phần lớn ô `?` |
| Chưa cấp **số năm bảo hành theo dịch vụ** | | `TC-4` | Khoa Chuyên môn | ★ Gỡ `CĐ-P8` |
| Chưa có **danh sách case before–after có giấy đồng ý** | | `TC-4` | Marketing + Pháp chế | ★ Gỡ `CĐ-P11` |
| Chưa có **danh sách cơ sở đủ năng lực All-On / ghép xương** | | `TC-4` | Vận hành | ★ Định tuyến khách tỉnh — ca đắt nhất |
| Chưa có **số giấy xác nhận nội dung quảng cáo** | | — | Pháp chế | Mở được hook 🟠 |
| **Bản xuất ⛔ không có ghi chú bàn giao** | | `TC-7`, `TC-8` | Vận hành / IT | ★ Mở được 2 tiêu chí đang `—` cho **cả khối** |
| **Khách nhắn ngoài giờ** (ngoài 8h30–18h30) | | `TC-1` | Vận hành | Cân nhắc ca trực tối |
| ★ **Tin khách chưa được chạm** (`pd-B` §7) | | — | Trưởng nhóm | Lead mất trắng, ⛔ không chấm được vào ai |

### Mỗi dòng phải có đủ bốn thứ

```
① SỐ Ô / SỐ HT bị ảnh hưởng — con số thật, ⛔ không "nhiều"
② Ô NÀO bị chấm "—" vì nó
③ AI CẤP — tên bộ phận, và nếu biết thì tên người
④ CẤP RỒI THÌ GỠ ĐƯỢC GÌ — ★ ô này là ô làm cho việc được làm
```

★ **Ô ④ là ô quyết định.** *"Chưa có số năm bảo hành"* nghe như một ghi chú. *"Cấp số năm bảo hành thì `n` cờ đỏ `CĐ-P8` tự hết và `m` ô `TC-4` chuyển từ `—` thành chấm được"* là một việc có giá.

⚠️ Dòng cuối — **tin khách chưa được chạm** — ⛔ không có ô nào để chấm, nên nó **chỉ xuất hiện được ở đây**. Bỏ `ST-HT` là mất luôn con số đó, và đó là con số lead mất trắng.

---

## 5. BA TIÊU CHÍ YẾU NHẤT CỦA KHỐI → NỘI DUNG ĐÀO TẠO

Lấy 3 tiêu chí `TC` có **% đạt thấp nhất toàn khối**, nhưng ⛔ **chỉ tính các ô `✓`/`✗`** — ⛔ không tính `—`/`?`.

⚠️ **Lọc trước khi xếp:** tiêu chí mà phần lớn ô trượt là **lỗi hệ** thì ⛔ **không được đưa vào nội dung đào tạo**. Nó thuộc `ST-HT`.

★ Cách kiểm nhanh: với mỗi tiêu chí yếu, hỏi *"nếu khối được đào tạo hoàn hảo về việc này thì tỷ lệ đạt có lên được không?"* — nếu câu trả lời là *"không, vì vẫn chưa có dữ kiện"* thì đó là việc hệ thống.

| Ví dụ tiêu chí yếu | Đào tạo chữa được? | Vào sổ nào |
|---|---|---|
| `TC-3` thu đủ 4 thông tin | ✅ Có | Đào tạo |
| `TC-5` xin số có lý do có lợi | ✅ Có | Đào tạo |
| `TC-10` nêu rõ bước tiếp theo | ✅ Có | Đào tạo |
| `TC-4` tạo tin cậy — trượt vì ⛔ không có số bảo hành | ⛔ Không | `ST-HT` |
| `TC-7`/`TC-8` — bản xuất ⛔ không có ghi chú | ⛔ Không | `ST-HT` |

---

## 6. NHẬT KÝ KỲ — `B4`

Ghi vào `doc/CHANGELOG.md`, bốn mục:

```
① VIỆC KỲ TRƯỚC: từng việc · đạt/chưa · số thật
② CỜ ĐỎ KỲ TRƯỚC: gỡ được mấy cái · cái nào quay lại
   ★ Cờ quay lại 2 kỳ liền → ⛔ KHÔNG phải lỗi nhân viên nữa.
     Hoặc gốc ở nội dung, hoặc gốc ở hệ. Ghi rõ.
③ SLOT DỮ KIỆN: slot nào được cấp trong kỳ · slot nào vẫn chờ, chờ mấy kỳ rồi
   ★ Slot chờ ≥3 kỳ → đưa lên ĐẦU báo cáo, ⛔ không để trong phụ lục
④ ĐIỀU HỌC ĐƯỢC VỀ CHÍNH BỘ CÔNG CỤ: tiêu chí nào chấm sai ·
   từ khoá nào nhận nhầm · luật nào thiếu
```

★ **Mục ④ ⛔ không được bỏ.** Bộ công cụ cũng sai, và nó sai theo cách im lặng. Kỳ nào cũng phải ghi lại ít nhất một điều học được về chính nó — ⛔ không có gì để ghi thường nghĩa là ⛔ chưa kiểm.

---

## 7. TỰ KIỂM SỔ NÀY

- [ ] `ST-CN` của người A có chứa tên / điểm / lời khách của người B không?
- [ ] ★ Phần ⑤ **"việc không phải của bạn"** có trong **mọi** `ST-CN` chưa?
- [ ] Phần ① có so sánh với người khác không — kể cả dạng *"trung bình khối là…"*?
- [ ] Ô ③ *"đoạn chat của chính bạn"*: có bị **bịa** không? ⛔ Không có câu tốt thì đã bỏ ô chưa?
- [ ] Loại D có bị đưa quá **một** việc không?
- [ ] Loại A: đã **xin phép** trước khi lấy chat làm mẫu cho khối chưa?
- [ ] `ST-HT` có lọt **tên nhân viên** nào không?
- [ ] Mỗi dòng `ST-HT` có đủ **bốn** thứ §4 chưa — nhất là ô ④ *"cấp rồi thì gỡ được gì"*?
- [ ] ★ Ba tiêu chí đào tạo: có tiêu chí nào thực ra là **lỗi hệ** bị đưa vào đào tạo không?
- [ ] Nhật ký kỳ có mục ④ **điều học được về bộ công cụ** chưa?
- [ ] Có cờ đỏ nào **quay lại 2 kỳ liền** mà vẫn ghi là lỗi nhân viên không?
