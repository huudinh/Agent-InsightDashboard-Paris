# Prompt · `QC` — luồng Q, về NGƯỜI TRỰC PAGE

> Yêu cầu `ĐỌC` đã chạy. Luồng này dừng ở **CỔNG 2**.
> ★ Luồng này chạy xong được **trong khi** luồng I còn đang chờ duyệt chân dung — hai cổng của luồng I ⛔ không chặn luồng này.

---

```
QC kỳ <KỲ>.

Đọc lại từ out/doc-hoi-thoai.json. ⛔ KHÔNG đọc lại hội thoại.
⛔ KHÔNG dùng chân dung / hook / số ads — nhân viên trả lời khách TRƯỚC
   khi chân dung tồn tại (rào ⑤ của pd-Q1 §6).

① KIỂM MỘT LẦN Ở ĐẦU KỲ:
   Bản xuất có PHẦN GHI CHÚ BÀN GIAO không?
   ⛔ Không có → TC-7 và TC-8 là "—" cho MỌI hội thoại, và ghi rõ ở đầu
     báo cáo: "kỳ này chấm trên 8 tiêu chí".
   ⚠ Chấm ✗ cho TC-7/TC-8 trên bản xuất không chứa ghi chú là cho 0 điểm
     oan cho CẢ KHỐI.

② QUY 10 Ô TC THÀNH ĐIỂM:
   Điểm một HT = (số ✓) ÷ (số ✓ + số ✗) × 10
   Điểm một người = trung bình điểm các HT của người đó
   ⚠ "—" và "?" LOẠI KHỎI MẪU SỐ. ⛔ Không tính là trượt.
   ⚠ TC-9 trượt → HT đó 0 điểm, bất kể 9 tiêu chí kia (P8 §6).

③ PHÂN LOẠI: A ≥9,0 · B 8,0–8,9 (đạt chuẩn P8) · C 6,5–7,9 · D <6,5
   ⛔ <5 HT: không chấm. 5–9 HT: chấm từng HT, KHÔNG phân loại.
   ⛔ Mẫu bị lọc → KHÔNG phân loại A/B/C/D, chỉ chấm từng HT.
   ⚠ Một cờ đỏ trong kỳ → ⛔ không được xếp loại A dù điểm cao.

④ SOÁT 11 CỜ ĐỎ. Mỗi cờ đủ SÁU Ô (pd-Q2 §4):
   ① nguyên văn · ② ai · ③ ngữ cảnh · ④ sai ở đâu ·
   ⑤ ★ CÂU ĐÚNG · ⑥ người xử lý đích danh + hạn
   ⚠ Ô ⑤ ⛔ không được bỏ. Báo cờ mà không đưa câu đúng thì nhân viên sẽ
     tự tìm cách nói khác, và thường là một câu sai khác.
   ★ Với MỖI cờ, hỏi thêm một câu: "nhân viên tự nghĩ ra, hay đang NHẮC LẠI
     chữ của post ads / tài liệu đào tạo?" — nếu là cái thứ hai thì GỐC LỖI
     Ở NỘI DUNG, gửi sang luồng I.

⑤ DANH SÁCH Ô "?" — mỗi ô đủ NĂM thứ (pd-Q1 §5):
   HT-nnn · nguyên văn · câu hỏi cần trả lời · ba nhánh kết luận ·
   người đối chiếu

⑥ VIỆC HỆ THỐNG — gom theo NGUYÊN NHÂN, ⛔ không theo người.
   Mỗi dòng đủ bốn thứ: số ô · ô nào · ai cấp ·
   ★ "cấp rồi thì gỡ được gì"
   + số HT "chưa được chạm" (⛔ không chấm được vào ai, nhưng PHẢI có số)

⑦ BA TIÊU CHÍ YẾU NHẤT CỦA KHỐI → nội dung đào tạo kỳ sau.
   ⚠ LỌC TRƯỚC KHI XẾP: tiêu chí mà phần lớn ô trượt là LỖI HỆ thì
     ⛔ KHÔNG được đưa vào đào tạo — nó thuộc ST-HT.
   ★ Cách kiểm: "nếu khối được đào tạo hoàn hảo về việc này thì tỷ lệ đạt
     có lên được không?" Nếu "không, vì vẫn chưa có dữ kiện" → việc hệ thống.

⛔ DỪNG ở CỔNG 2. Chờ tôi gõ DUYỆT PHÁP CHẾ / ĐÃ GỠ <mã> … / CHỜ <mã>
```

---

## ★ BẢNG TRA LỖI HỆ — ⛔ đừng chấm `✗` (`pd-Q1` §4)

| Tình huống | Ô | Chấm | Đẩy lên |
|---|---|---|---|
| Khách nhắn **ngoài 8h30–18h30** | `TC-1` | `—` | *"khách nhắn ngoài giờ n lượt"* → ca trực tối |
| Hỏi giá **dòng trụ/dòng sứ chưa có trong bảng giá** | `TC-9`, `TC-4` | `?` | chưa cấp bảng giá theo dòng |
| Hỏi **số năm bảo hành** | `TC-4` | `—` | chưa cấp chính sách bảo hành |
| Xin **ảnh before–after** | `TC-4` | `—` | chưa có case có giấy đồng ý |
| Khách tỉnh hỏi **All-On / ghép xương** | `TC-4` | `—` | chưa có danh sách cơ sở đủ năng lực |
| Bản xuất **không có ghi chú bàn giao** | `TC-7`, `TC-8` | `—` | ⛔ không đo được |
| Hỏi **bệnh nền / thuốc / chống chỉ định** | `TC-4` | `—` | ⛔ Phải bác sĩ. Nhân viên **đúng** khi không trả lời |

⚠️ **Rào ③ là rào hay bị quên nhất.** `pd-E` §7 đang có **bảy slot dữ kiện chưa được cấp** — nghĩa là một phần đáng kể ô trượt `TC-4`/`TC-9` là **lỗi hệ**. Trừ điểm nhân viên vì chuyện đó là **chấm sai người**.

---

## ★ CÂU MIỄN TRỪ — ⛔ đừng gắn cờ cho người làm ĐÚNG

Nếu câu có cụm **từ chối / hoãn / dẫn khách theo đúng quy trình** thì ⛔ **không gắn cờ**, dù có từ khoá khớp:

> *"về ảnh case thì em **xin phép xác nhận lại** danh sách ảnh được phép sử dụng rồi gửi chị, vì ảnh khách **phải có sự đồng ý** của họ"*

Câu trên khớp từ khoá `CĐ-P11` nhưng là **làm đúng**. Cụm miễn trừ: *xin phép xác nhận lại · chưa dám nói · phải có sự đồng ý · được phép sử dụng · bác sĩ xác định sau · tuỳ tình trạng · phải khám mới · em không dám*.

> ★ **Gắn cờ đỏ cho người làm đúng là lỗi tệ nhất mà repo này có thể sinh ra.** `tools/pd.py` có hàm `mien_tru()` chạy đúng việc này.

---

## ★ BỐN RÀO AN TOÀN — ⛔ bỏ một là sổ này vô hiệu

```
① Điểm để KÈM CẶP, ⛔ không để kỷ luật. Mọi bảng điểm mang đúng câu này
   ở chân bảng: "Điểm dùng để phân việc kèm cặp. Không phải căn cứ
   kỷ luật hay xếp hạng công khai."
② Mỗi ✗ phải có HT-nnn + CẶP CÂU nguyên văn (câu khách + câu NV trả lời
   ngay sau). ⛔ Không có bằng chứng thì đổi thành "—".
③ Lỗi hệ ⛔ không trừ điểm người.
④ ⛔ KHÔNG xếp hạng công khai. Tên + điểm cá nhân CHỈ trong sổ tay riêng
   của người đó và bản trưởng nhóm.
⑤ ⛔ KHÔNG chấm bằng thứ nhân viên không biết (chân dung · hook · ads).
```

⛔ **Và ⛔ không có bảng "ai nhiều cờ nhất".** Người nhận hội thoại khó (`V-01` làm lại ca lỗi, `V-02` All-On) tự nhiên gặp nhiều tình huống chạm ranh hơn. Nếu phải so, so theo **số cờ / số hội thoại** và nói rõ nhóm `V-xx` người đó phụ trách.

---

```bash
python tools/pd.py qc --ky "01-15/11"
python tools/pd.py kiem out/bao-cao-qc.json   # CỔNG T
```
