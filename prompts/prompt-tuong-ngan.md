# Prompt · CỔNG T — kiểm tường ngăn trước khi xuất

> ⛔ Không file nào được xuất ra trước khi chạy đủ **sáu câu kiểm** này.
> Mỗi câu phải trả lời được bằng *"đã kiểm, kết quả là…"*, ⛔ không phải *"chắc là ổn"*.

---

```
CỔNG T — kiểm tường ngăn cho <tên file>.

① TÊN NHÂN VIÊN
   Tìm MỌI tên nhân viên (lấy từ cột nv của bảng gốc) trong file sắp xuất
   của luồng I. Tìm thấy dù một lần → ⛔ DỪNG, xoá, xuất lại.
   ⚠ Kiểm cả trong trích dẫn và trong TÊN FILE.

② THÔNG TIN KHÁCH
   Tám thứ của pd-B §3 (tên thật · SĐT · ảnh · email · địa chỉ ·
   link cá nhân · mã đơn · tên người nhà) — ⛔ không có ở file nào của
   CẢ HAI luồng, kể cả sổ tay riêng.

③ FILE INSIGHT CÓ ĐIỂM SỐ KHÔNG
   Khoá nv · tc · diem · loai · bang_chung trong JSON insight
   → ⛔ PHẢI KHÔNG TỒN TẠI.
   ⚠ ⛔ Không phải "để rỗng" — phải KHÔNG CÓ KHOÁ ĐÓ.
     Khoá rỗng là khoá sẽ có ngày được điền.

④ FILE QC CÓ LỜI KHÁCH DÀI KHÔNG
   Trích dẫn khách trong báo cáo QC chỉ được giữ ĐÚNG phần làm bằng chứng
   cho ô ✗ đang xét. ⛔ Không chép cả hội thoại.
   Và khoá chan_dung · hook · ma_tran · ads → ⛔ PHẢI KHÔNG TỒN TẠI.

⑤ NHÓM MỎNG
   Nhóm dưới 10 HT → đã ẩn tỷ lệ chưa?
   Nhân viên dưới 10 HT → đã bỏ phân loại chưa?
   Một V-xx chỉ có 1–2 HT có nhận ra được cá nhân không?
   ⚠ "mất răng số 6 hàm dưới bên phải 2 năm" là mô tả NHẬN DẠNG ĐƯỢC khi
     nhóm chỉ có 1–2 HT → rút về "mất răng hàm dưới".

⑥ CÂU CHÂN BẢNG
   Mọi bảng điểm của luồng Q có đúng câu này ở chân chưa:
   "Điểm dùng để phân việc kèm cặp. Không phải căn cứ kỷ luật hay
    xếp hạng công khai."
```

---

## ⚠️ Câu ① và ③ phải chạy BẰNG MÁY

```bash
python tools/pd.py kiem out/bao-cao-insight.json
python tools/pd.py kiem out/bao-cao-qc.json
```

Hàm `kiem_tuong_ngan()` chạy đúng sáu câu trên và **từ chối ghi file** nếu trượt — nên mọi lần ghi JSON đều đi qua `ghi_json()`, ⛔ không gọi `json.dump` trực tiếp ở chỗ khác.

> Chạy tay thì ⛔ **sẽ có kỳ quên**. Và lọt tên nhân viên vào báo cáo insight là lỗi ⛔ không gỡ được sau khi đã gửi đi.

---

## ★ Ba cách tường ngăn bị phá trong thực tế

```
① "CHO MỖI MỘT VÍ DỤ THÔI"
   Ai đó xin một ví dụ có tên người để báo cáo insight "sinh động hơn".
   → ⛔ Không. Dùng HT-nnn. Mã hội thoại đủ truy ngược cho người CÓ QUYỀN
     truy ngược, và vô nghĩa với người không có quyền. Đó chính là mục đích.

② "GỘP HAI FILE CHO DỄ GỬI"
   Ai đó ghép hai báo cáo thành một bản PDF để gửi họp.
   → ⛔ Không. Gửi hai file, hai người nhận. Buổi họp cần cả hai thì người
     chủ trì đọc hai file — đó là việc của họ, ⛔ không phải việc của agent.

③ "DASHBOARD CÓ Ô ĐĂNG NHẬP RỒI"
   Ai đó đề nghị một dashboard duy nhất, phân quyền bằng mật khẩu.
   → ⛔ Không trong bản này. Dashboard ở đây là file tĩnh, publish ra link;
     ai có link là mở được. Phân quyền bằng FILE, ⛔ không bằng màn hình.
```

---

## Trước khi publish — ba câu

```
① File này là file nào? insight hay qc?
   → ⛔ File qc-*.json ⛔ KHÔNG publish ra link công khai.
     Chỉ gửi file, cho đúng trưởng nhóm.
② Đã chạy kiem_tuong_ngan() chưa?
③ Artifact mặc định RIÊNG TƯ. Chuyển sang "ai có link đều mở được" thì
   ⛔ ĐỪNG dán link vào repo public — kể cả file insight, vì nó chứa lời
   khách (đã ẩn danh) và kết luận nội bộ.
```
