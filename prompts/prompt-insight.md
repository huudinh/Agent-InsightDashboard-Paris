# Prompt · `INSIGHT` — luồng I, về KHÁCH

> Yêu cầu `ĐỌC` đã chạy. Luồng này đi qua **CỔNG 0** rồi **CỔNG 1**, dừng ở cả hai.
> ⛔ Tên nhân viên ⛔ không bao giờ xuất hiện trong bất cứ đầu ra nào của luồng này.

---

## Chặng 1 — dừng ở CỔNG 0

```
INSIGHT kỳ <KỲ>. Chặng 1.

Đọc lại từ out/doc-hoi-thoai.json. ⛔ KHÔNG đọc lại hội thoại.

① IN BỐN BẢNG NGUYÊN LIỆU (pd-I1 §2):
   ① cụm chữ khách tự nói — xuất hiện ≥3 lần, GIỮ NGUYÊN chữ khách gõ, kèm số lượt
   ② câu hỏi đầu tiên của khách — phân bố
   ③ phân bố ba trục: V-01…V-11 | V1/V2/V3 | S1/S2/S3/CS | SỢ/NGỜ/NGẠI
   ④ dấu hiệu người thứ ba — số HT có "bố/mẹ/con/vợ/chồng/cho người nhà"

② PHÁC HỌA 4–7 CHÂN DUNG. Mỗi thẻ đủ BẢY ô:
   mã · tên (★ LẤY TỪ CHỮ CỦA KHÁCH) · họ là ai · nỗi sợ thật ·
   dấu hiệu nhận ra · hệ số giá trị · ★ ≥3 HT-nnn + trích ẩn danh

③ IN dòng CD0 dự kiến + nhóm N nào VẮNG MẶT trong kỳ.

⛔ DỪNG. Chờ tôi gõ DUYỆT CHÂN DUNG / SỬA CD<n> … / GỘP … / TÁCH …

★ BỐN LUẬT PHÁC HỌA (pd-I1 §4):
① 4–7 chân dung. Ít hơn 4 là chia thô; nhiều hơn 7 thì nhóm nào cũng
  dưới ngưỡng mẫu.
② Mỗi chân dung ≥5 HT mới được viết thẻ insight. Dưới 5 → giữ trong bản
  phác họa, ghi "⚠ chưa đủ mẫu", ⛔ KHÔNG xoá.
③ ★ XẾP TỪ HẸP ĐẾN RỘNG khi gán. Chân dung rộng HÚT HẾT hội thoại của
  chân dung hẹp nếu gán rộng-trước. V-01 (làm lại ca lỗi) và V-11 (chưa rõ)
  là hai nhóm LUÔN bị hút — gán chúng TRƯỚC.
④ CD0 > 25% mẫu → bản phác họa CHƯA ĐỦ, phác lại.
  ⛔ Không nhét bừa vào chân dung gần nhất.

★ ⛔ KHÔNG dùng N1…N6 làm chân dung (pd-I1 §1).
  N1…N6 là nhóm khách BIẾT TRƯỚC từ hồ sơ thương hiệu.
  CD là chân dung PHÁC HỌA TỪ CHỮ KHÁCH CỦA CHÍNH KỲ NÀY.
  Dùng N thay CD là LỖI IM LẶNG: mọi bảng vẫn khớp tổng, biểu đồ vẫn đẹp,
  nhưng báo cáo chỉ nói lại điều đã biết và ⛔ không phát hiện gì mới.

★ Tên chân dung: ⛔ KHÔNG phải nhân khẩu học.
  ⛔ "Nữ 30–40 nội thành"  → đó là tệp quảng cáo
  ✅ "Em làm ở chỗ khác rồi, giờ muốn sửa"
```

---

## Chặng 2 — sau `DUYỆT CHÂN DUNG`, dừng ở CỔNG 1

```
Chặng 2.

④ GÁN cd cho từng HT, theo thứ tự HẸP → RỘNG. In dòng CD0 với số thật.

⑤ BẢNG CHÂN DUNG: CD · tên · n HT · % mẫu · V chủ đạo ·
   HOT · ★ HOT* · % có SĐT

⑥ THẺ INSIGHT từng CD ≥5 HT, đủ bảy ô (pd-I2 §1).
   ★ Ô "insight một câu" phải viết TỪ GÓC NHÌN KHÁCH, bắt đầu bằng "Tôi…".
     Đọc lên mà nghe như lời người bán thì ⛔ chưa phải insight.

⑦ MA TRẬN CD × RÀO CẢN. ★ Đếm theo LƯỢT, GHI CÁCH ĐẾM ở đầu bảng.
   ★ Phải có cột HOT* cạnh cột HOT.

⑧ L6.7 NGỜ VẬT LIỆU — dòng riêng, kèm con số:
   "n HT ngờ vật liệu — m được nêu bằng chứng thật, n−m chỉ nhận trấn an chung"
   ★ Con số n−m là NỘI DUNG PHẢI LÀM NGAY.

⑨ SỐ ADS (nếu có file): chuỗi Chi → CPM → CTR → CPI → CPL →
   CP-ĐẶT-LỊCH → CP-ĐẾN-KHÁM.
   ★ Bảng "POST HỨA GÌ ↔ KHÁCH HỎI GÌ NGAY SAU ĐÓ" — phần giá trị nhất.
   ⚠ Phễu PHẢI có cột "đến khám". ⛔ KHÔNG lấy "đặt lịch" thay.
     Không có → ghi "⚠ chưa đo được show-up", ĐỂ TRỐNG.

⑩ BA VẤN ĐỀ CỐT LÕI, xếp theo SỐ HT bị ảnh hưởng. Mỗi vấn đề đủ bốn phần:
   hiện tượng · bằng chứng (≥3 HT-nnn) · đọc ra gì · ★ AI SỬA
   ⚠ Ô "ai sửa" chỉ được là Marketing (nội dung) hoặc Hệ thống (cấp dữ kiện).
     ⛔ KHÔNG BAO GIỜ là tên nhân viên. Nếu câu trả lời tự nhiên là
     "trực page phải làm tốt hơn" thì vấn đề đó ⛔ không thuộc luồng I —
     chuyển sang luồng Q, hoặc viết lại ở mức hiện tượng.

⑪ MA TRẬN ƯU TIÊN — bảng việc, mỗi dòng bảy cột, kèm CÁCH XẾP.
   ★ Xếp theo ĐỘ CHẶN × GIÁ TRỊ (V1 > V2 > V3).
   ⛔ KHÔNG tự phát minh hệ số rồi nhân ra "điểm ưu tiên".
   ⚠ Chưa đo được show-up → xếp theo ĐỘ CHẶN THUẦN và NÓI RÕ.

⑫ MỤC VIỆC HỆ THỐNG — riêng, có tên người chịu trách nhiệm cấp dữ kiện.

⛔ DỪNG. Chờ tôi gõ DUYỆT / BỎ <n> / ĐỔI THỨ TỰ … / CHỈ LÀM <n>, <m>
```

---

## Chặng 3 — sau `DUYỆT`

Sinh ngân hàng hook theo `prompts/prompt-hook.md`.

---

## ★ Luật tường ngăn của luồng này

```
⛔ Tên nhân viên ⛔ KHÔNG vào JSON, HTML, ghi chú, ví dụ, trích dẫn.
⛔ ⛔ Không có khoá nv · tc · diem · loai · bang_chung trong file insight
   — phải KHÔNG CÓ KHOÁ, ⛔ không phải "để rỗng".
🔶 Cờ đỏ đi qua tường được nhưng BỊ LỌC: chỉ mã + số lượt + HT-nnn +
   nhóm V-xx hay gặp. ⛔ Không nguyên văn, ⛔ không tên người.
```

★ **Cách viết đúng khi phải nói về chất lượng tư vấn:**

| ⛔ Sai (lọt tên) | ✅ Đúng (ở mức hiện tượng) |
|---|---|
| *"Chị Hà trả lời 'bọc sứ không đau và không hại gì' — sai"* | *"6/14 HT nhóm `V-05` được trả lời bằng tính từ trấn an thay vì cơ chế mài răng (`HT-004`, `HT-019`…). Khách hỏi lại lần hai rồi rơi."* |

> Bản đúng **mạnh hơn** bản sai. *"6/14 HT"* là vấn đề nội dung sửa được bằng một tuyến bài. *"Chị Hà"* là vấn đề của một người, và ⛔ không nói gì về 13 HT còn lại.

---

```bash
python tools/pd.py insight --ky "01-15/11"
python tools/pd.py kiem out/bao-cao-insight.json   # CỔNG T
```
