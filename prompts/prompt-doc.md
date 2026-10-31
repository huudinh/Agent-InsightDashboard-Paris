# Prompt · `ĐỌC` — một lần đọc, dựng bảng dữ kiện gốc

> Dán prompt này kèm file hội thoại. Đây là **bước duy nhất đọc hội thoại**. Hai luồng sau đó đọc lại từ kết quả của bước này.

---

```
ĐỌC hội thoại kỳ <KỲ>.

Làm đúng thứ tự:

① KIỂM MẪU — in ra TRƯỚC khi đọc (pd-B §6):
   ① cỡ mẫu: bao nhiêu HT · bao nhiêu bị loại · vì sao loại
   ② khoảng ngày: ngày đầu → ngày cuối
   ③ mẫu bị lọc? — file có HT nào chỉ 1 lượt khách không?
      ⛔ KHÔNG CÓ hội thoại ngắn là dấu hiệu file ĐÃ BỊ LỌC
   ④ phân bố nhân viên: ai bao nhiêu HT, ai đủ 10 để phân loại

② ĐỌC TỪNG HỘI THOẠI — ĐÚNG MỘT LẦN. Mỗi HT ghi ra một hàng đủ các ô:

   Ô CHUNG   : ht · ngày · giờ · số lượt KH/NV · có SĐT
               v_rang (V-01…V-11) · nhom_gt (V1/V2/V3)
               bitmask 5 chữ số · do_nong · do_nong_sao
               co_do · loi_he
   Ô LUỒNG I : l_code (L1.1…L6.7) · giai_doan (S1/S2/S3/CS)
               rao_can (SỢ/NGỜ/NGẠI) · nhom_khach (N1…N6)
               cau_hoi_ngam · post_ads · loi_hua_post
               trich_khach (ĐÃ ẨN DANH) · dau_gia_dinh · cd = null
   Ô LUỒNG Q : nv · phut_tra_loi_dau · trong_gio
               tc (TC-1…TC-10: ✓/✗/—/?) · bang_chung · ghi_chu_he

③ IN RA kết quả kiểm mẫu + phân bố ba trục. ⛔ DỪNG tại đây.

★ BA LUẬT CỦA BƯỚC NÀY:
① v_rang xét THEO THỨ TỰ V-01 → V-11, đúng nhóm đầu tiên thì lấy,
  ⛔ không xét tiếp. ⛔ Không lấy nhóm khớp nhiều từ khoá nhất.
② Mọi hàng PHẢI có bitmask. ⛔ Không có bitmask thì ⛔ không ai kiểm lại
  được điểm. Và mọi hàng PHẢI có do_nong_sao (chấm lại ⛔ không kể tín hiệu ①).
③ cd = null cho MỌI hàng. ⛔ Không gán chân dung ở bước này.
  ⛔ Không dùng nhom_khach (N1…N6) thay cho chân dung.

★ BA LUẬT GHI ĐÈ ĐỘ NÓNG — ⛔ đừng bỏ (P8 §1):
① đã đặt lịch khám / đang đến phòng khám  → HOT bất kể điểm
② đã có phim X-quang, hoặc đã khám nơi khác và có phác đồ/báo giá
                                          → HOT bất kể điểm
③ đang đau cấp (V-06)                     → tối thiểu WARM
⚠ Luật ② là luật dễ bỏ sót và đắt nhất: khách đã qua giai đoạn chẩn đoán,
  chỉ còn CHỌN NƠI LÀM — lead nóng nhất của ngành nha.

★ ẨN DANH — bỏ 8 thứ trước khi ghi ra bất cứ đâu (pd-B §3):
tên thật khách · SĐT · ảnh · email · địa chỉ nhà · link cá nhân ·
mã đơn/hồ sơ · tên người nhà.
⚠ Hai cái dễ lọt ở ngành nha:
  · vị trí răng + mốc thời gian ("mất răng số 6 hàm dưới bên phải 2 năm")
    → nhóm dưới 10 HT thì rút về "mất răng hàm dưới"
  · tên người nhà → giữ quan hệ + tuổi, ⛔ bỏ tên

★ HỘI THOẠI BỊ LOẠI — ghi rõ, ⛔ không âm thầm bỏ (pd-B §7):
khong-co-loi-khach · chua-duoc-cham · ngoai-pham-vi · cs-tai-kham
⚠ "chua-duoc-cham" là một PHÁT HIỆN, ⛔ không phải mẫu rác: khách nhắn
  rồi ⛔ không ai trả lời = lead mất trắng. Phải có số, ở đầu báo cáo QC.
```

---

## Chạy bằng công cụ

```bash
python tools/pd.py doc du-lieu/hoi-thoai.md --ky "01-15/11"
```

Ra `out/doc-hoi-thoai.json`. Sau đó `INSIGHT` và `QC` **đọc lại từ file này**, chạy độc lập, lúc nào cũng được.

⚠️ Sửa một hàng trong bảng gốc → **chạy lại CẢ HAI luồng**, ⛔ không sửa một bên (`pd-C` §4).
