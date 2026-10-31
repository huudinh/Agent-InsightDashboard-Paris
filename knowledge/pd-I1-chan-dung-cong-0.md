# pd-I1 · CHÂN DUNG CỦA KỲ · CỔNG 0

> ⛔ **Hệ này không có bộ chân dung mặc định.** Chân dung được phác họa từ chữ của khách trong chính kỳ đang chạy, rồi **anh duyệt**. Sổ này nói cách phác họa và cách dừng lại chờ.

---

## 1. ⛔ VÌ SAO KHÔNG DÙNG `N1…N6` LÀM CHÂN DUNG

`P2` §3 đã có sáu nhóm khách: `N1` mất răng trung–cao niên · `N2` thẩm mỹ 22–40 · `N3` niềng · `N4` đau cấp · `N5` làm lại ca lỗi · `N6` gia đình & trẻ em.

**Sáu nhóm đó đúng, và sổ này dùng chúng** — nhưng dùng làm **lưới kiểm**, ⛔ không làm chân dung.

| | `N1…N6` — nhóm khách | `CD1…CDn` — chân dung của kỳ |
|---|---|---|
| Nguồn | Hồ sơ thương hiệu, **biết trước khi đọc** | **Chữ khách của chính kỳ này** |
| Trả lời câu | *"Ngành nha có những loại khách nào"* | *"Kỳ này ai đang nhắn vào page, và họ đang nghĩ gì"* |
| Đổi theo kỳ | ⛔ Không | ✅ Có |
| Cần duyệt | ⛔ Không | ✅ **CỔNG 0** |

> ⚠️ **Dùng `N1…N6` làm chân dung là lỗi im lặng.** Mọi bảng vẫn khớp tổng, biểu đồ vẫn đẹp, nhưng báo cáo chỉ nói lại điều đã biết từ trước. Nó ⛔ không phát hiện được gì mới — mà phát hiện cái mới chính là việc duy nhất của luồng I.

★ **Cách dùng `N1…N6` cho đúng:** sau khi phác họa `CD`, đối chiếu xem có nhóm `N` nào **không xuất hiện** trong kỳ. Nhóm vắng mặt là một phát hiện: *"`N6` gia đình & trẻ em — 0 hội thoại trong kỳ, dù đây là cửa vào LTV mạnh nhất. ⚠️ Kỳ này ⛔ không có post nào nhắm nhóm này."*

---

## 2. NGUYÊN LIỆU PHÁC HỌA — IN RA TRƯỚC KHI PHÁC

Trước khi viết chân dung nào, in **bốn bảng nguyên liệu** này. Chúng là bằng chứng cho bản phác họa, và là thứ anh soi khi duyệt:

```
① CỤM CHỮ KHÁCH TỰ NÓI
   Cụm xuất hiện ≥3 lần, giữ nguyên chữ khách gõ, kèm số lượt.
   Ví dụ: "sợ mài răng thật" ×11 · "có chính hãng không" ×9
          "bố em / mẹ em" ×7 · "làm ở chỗ khác rồi" ×6

② CÂU HỎI ĐẦU TIÊN CỦA KHÁCH — phân bố
   Hỏi giá ngay ×41 · nêu tình trạng ×38 · hỏi địa chỉ ×12 · hỏi bác sĩ ×9

③ PHÂN BỐ TRỤC
   V-01…V-11 × | V1/V2/V3 × | S1/S2/S3/CS × | SỢ/NGỜ/NGẠI ×

④ DẤU HIỆU NGƯỜI THỨ BA
   Số HT có "bố/mẹ/con/vợ/chồng/cho người nhà" → ★ cột `dau_gia_dinh`
```

★ **Bảng ④ là bảng riêng của ngành nha.** Người quyết định thường ⛔ không phải người nhắn: con nhắn cho bố mất răng, mẹ nhắn cho con niềng. Hội thoại nhóm này **thường bị chấm COLD** vì người nhắn không tự đặt lịch được — mà đó lại là tệp LTV cao nhất của Paris (`P2` §3, `N6`).

---

## 3. MỘT THẺ CHÂN DUNG CÓ GÌ

Mỗi chân dung **bắt buộc** đủ bảy ô. Thiếu ô nào thì ⛔ chưa phác xong:

| Ô | Yêu cầu | ⛔ Sai thường gặp |
|---|---|---|
| **Mã** | `CD1`…`CDn` | — |
| **Tên** | ★ **Lấy từ chữ của khách**, không phải từ nhân khẩu học | ⛔ *"Nữ 30–40 nội thành"* — đó là tệp quảng cáo, không phải chân dung |
| **Họ là ai** | 2–3 câu: hoàn cảnh, vì sao nhắn **bây giờ** | ⛔ Mô tả dịch vụ họ hỏi thay vì mô tả họ |
| **Nỗi sợ thật** | Câu hỏi ngầm, ⛔ không phải câu khách gõ (`pd-I2` §2) | ⛔ *"Sợ đắt"* — quá chung, dùng được cho mọi chân dung |
| **Dấu hiệu nhận ra** | 2–4 dấu hiệu **đọc được từ hội thoại** | ⛔ Dấu hiệu phải suy đoán thêm mới thấy |
| **Hệ số giá trị** | `V1`/`V2`/`V3` chủ đạo của nhóm | ⛔ Trộn V1 và V3 trong một chân dung |
| **Làm bằng** | ★ **≥3 `HT-nnn` + trích dẫn ẩn danh** | ⛔ Không có `HT` → ⛔ không phải chân dung, là giả thuyết |

### Mẫu một thẻ

> **`CD2` · "Em làm ở chỗ khác rồi, giờ muốn sửa"**
> **Họ là ai:** đã bọc sứ hoặc niềng ở nơi khác, kết quả không như mong đợi — sứ lệch, cộm, hoặc niềng dở dang rồi phòng khám cũ đóng. Nhắn bây giờ vì đã chịu đựng đủ lâu và vừa mất niềm tin vào một nơi.
> **Nỗi sợ thật:** *"Lần này có mất thêm răng thật nữa không, và các anh có nói thật với tôi không"* — ⛔ không phải sợ giá.
> **Dấu hiệu:** kể lại nơi cũ nhưng ⛔ không nêu tên · hỏi *"có sửa được không"* trước khi hỏi giá · hỏi rất kỹ về bác sĩ nào làm · thường gửi ảnh ngay tin đầu.
> **Hệ số giá trị:** `V1`–`V2`, `v_rang` = `V-01`.
> **Làm bằng:** `HT-012` *"em bọc 4 răng ở chỗ khác bị cộm, giờ sửa lại có phải mài thêm không"* · `HT-034` · `HT-057` · `HT-081`.

---

## 4. BỐN LUẬT PHÁC HỌA

```
① SỐ CHÂN DUNG: 4–7. Ít hơn 4 là chia thô, nhiều hơn 7 thì nhóm nào
   cũng dưới ngưỡng mẫu và không kết luận được gì.

② MỖI CHÂN DUNG ≥ 5 HT mới được viết thẻ insight (pd-I2 §1).
   Dưới 5 → giữ trong bản phác họa, ghi "⚠ chưa đủ mẫu", KHÔNG xoá.

③ XẾP TỪ HẸP ĐẾN RỘNG khi gán.
   ⚠ Luật này ra từ một lỗi thật: chân dung rộng ("quan tâm thẩm mỹ răng")
   HÚT HẾT hội thoại của chân dung hẹp ("sửa ca lỗi") nếu gán theo
   thứ tự rộng-trước. Gán hẹp trước, rộng nhận phần còn lại.

④ CD0 — HỘI THOẠI KHÔNG VÀO CHÂN DUNG NÀO.
   Luôn có dòng CD0 với số thật. CD0 > 25% mẫu → ⛔ bản phác họa CHƯA ĐỦ,
   phác lại, ⛔ không nhét bừa vào chân dung gần nhất.
```

★ **Luật ③ nói lại cho rõ:** `V-01` (làm lại ca lỗi) và `V-11` (chưa rõ) là hai nhóm **luôn** bị hút. Gán chúng trước.

---

## 5. ★ CỔNG 0 — DỪNG VÀ CHỜ

Phác xong, agent **in ra rồi dừng**. ⛔ Không chạy tiếp.

Bản in ra CỔNG 0 gồm đúng bốn phần:

```
① CỠ MẪU đã đọc / bỏ, vì sao bỏ
② BỐN BẢNG NGUYÊN LIỆU (§2)
③ BẢN PHÁC HỌA 4–7 CHÂN DUNG, mỗi cái đủ bảy ô (§3)
④ DÒNG CD0 dự kiến + ba nhóm N nào vắng mặt trong kỳ (§1)
```

Anh trả lời bằng một trong:

| Anh gõ | Agent làm gì |
|---|---|
| `DUYỆT CHÂN DUNG` | Gán `cd` cho từng HT, chạy tiếp `I2` |
| `SỬA CD<n> <điều chỉnh>` | Sửa đúng thẻ đó, in lại, **chờ tiếp** |
| `GỘP CD<a> CD<b>` | Gộp, in lại dòng CD0 mới, **chờ tiếp** |
| `TÁCH CD<n> theo <tiêu chí>` | Tách, in lại, **chờ tiếp** |

⛔ **Agent không tự duyệt thay anh.** ⛔ Không có trường hợp *"mẫu rõ ràng nên tôi gán luôn"*.

⚠️ **Và ⛔ không được lách CỔNG 0 bằng cách gọi nó tên khác** — ví dụ in ra "bảng phân nhóm khách sơ bộ" rồi dùng luôn. Bất cứ thứ gì chia khách thành nhóm **của kỳ này** rồi làm nền cho bảng khác đều là chân dung, và đều phải qua CỔNG 0.

---

## 6. SAU KHI DUYỆT — GÁN & THẺ INSIGHT

```
① GÁN: điền i.cd cho từng HT, theo thứ tự HẸP → RỘNG (luật ③ §4)
② DÒNG CD0: số thật, % mẫu
③ BẢNG CHÂN DUNG: CD · tên · n HT · % mẫu · V chủ đạo
                   · HOT/WARM/COLD · HOT* · % có SĐT
④ MA TRẬN CD × RÀO CẢN: hàng CD, cột SỢ/NGỜ/NGẠI
   ⚠ Một HT mang nhiều rào cản → ĐẾM THEO LƯỢT, ghi rõ cách đếm
     ở đầu bảng, nếu không người đọc cộng ra số lớn hơn tổng HT
     và nghĩ bảng sai
⑤ THẺ INSIGHT từng CD ≥5 HT (pd-I2 §1)
```

★ **Bảng ④ phải có thêm cột `HOT*`** cạnh cột `HOT` — vì chia theo rào cản là chia theo một thuộc tính liên quan tới tín hiệu chấm điểm. Xem `pd-I2` §4.

---

## 7. TỰ KIỂM SỔ NÀY

- [ ] Bốn bảng nguyên liệu §2 đã in **trước** bản phác họa chưa?
- [ ] Mỗi thẻ đủ **bảy** ô chưa? Có thẻ nào thiếu `HT-nnn` làm bằng không?
- [ ] Tên chân dung lấy từ **chữ khách** hay từ nhân khẩu học?
- [ ] "Nỗi sợ thật" của các chân dung có **khác nhau** không, hay đều là *"sợ đắt / sợ đau"*?
- [ ] Gán theo thứ tự **hẹp → rộng** chưa? `V-01` và `V-11` có bị hút không?
- [ ] `CD0` có số thật chưa, và có vượt 25% không?
- [ ] Có dừng **thật** ở CỔNG 0 không, hay đã gán rồi mới in ra xin duyệt?
- [ ] Ma trận `CD × rào cản` có ghi **cách đếm** ở đầu bảng chưa?
- [ ] Đã nói nhóm `N` nào **vắng mặt** trong kỳ chưa?
