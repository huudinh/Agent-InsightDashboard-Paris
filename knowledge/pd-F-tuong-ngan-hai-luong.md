# pd-F · ★★ TƯỜNG NGĂN GIỮA HAI LUỒNG

> Sổ này là **lý do hai luồng phải tách**.
> Nó trả lời một câu: **cái gì được phép đi qua giữa hai luồng, và cái gì thì không.**
> ⛔ Chưa đọc hết §4 thì ⛔ không được xuất file nào.

---

## 1. HAI LUỒNG KHÁC NHAU Ở CHỖ NÀO — KHÔNG PHẢI Ở GIAO DIỆN

Nhiều người nghĩ tách luồng là chuyện chia tab cho dễ xem. Không phải. Hai luồng khác nhau ở **năm thứ cốt lõi**, và mỗi thứ đều kéo theo một hệ quả kỹ thuật:

| | **LUỒNG I · INSIGHT KHÁCH** | **LUỒNG Q · QC TRỰC PAGE** |
|---|---|---|
| **① Chủ thể câu kết luận** | *Khách* — "nhóm mất răng đang sợ tiêu xương" | *Một con người có tên* — "chị Linh trượt `TC-4`" |
| **② Người đọc** | Marketing · nội dung · ads | Trưởng nhóm trực page · chính người đó |
| **③ Ngưỡng đủ mẫu** | Theo **kỳ** (≥50 để phác chân dung) | Theo **người** (≥10 HT mới được phân loại) |
| **④ Dữ liệu nhạy cảm** | Lời khách — phải **ẩn danh khách** | Tên nhân viên — phải **che với người ngoài khối** |
| **⑤ Hệ quả khi sai** | Viết sai hook → mất một tuần nội dung | Chấm sai người → **mất một con người** |

### ★ Và một thứ thứ sáu, nặng hơn cả năm cái trên

**Cùng một bằng chứng, hai luồng đọc ra hai nghĩa trái nhau.**

Ví dụ thật, khuôn `MAU_Hoi-thoai` hội thoại số 2:

```
KH:  bọc sứ bao nhiêu tiền
NV:  Dạ chào anh, anh để lại số điện thoại em tư vấn chi tiết ạ
KH:  cứ nói giá đi đã
NV:  Dạ anh inbox lại giúp em nhé
```

| Luồng | Đọc ra | Việc phải làm |
|---|---|---|
| **I** | Khách vào từ post *"nụ cười mới chỉ sau 1 lần hẹn"* rồi hỏi giá ngay → **post hứa nhanh mà trang đích không có giá**. Đây là **phát hiện về nội dung** | Sửa post · thêm khung giá vào nội dung |
| **Q** | Nhân viên **xin số trước khi hỏi tình trạng** → trượt `TC-3`; **né giá hai lượt** → trượt `TC-9`? **Chưa chắc** — phải tra xem bảng giá có cấp cho dòng sứ đó chưa | Nếu **đã có giá** → lỗi người, vào sổ tay. Nếu **chưa cấp giá** → ⛔ **lỗi hệ, không trừ điểm**, đẩy lên "việc hệ thống" |

> ⚠️ **Gộp hai luồng vào một báo cáo là ép người đọc chọn một trong hai nghĩa.** Và trong thực tế họ luôn chọn nghĩa của luồng Q — vì nó có tên người, nghe cụ thể hơn. Kết quả: lỗi nội dung và lỗi hệ thống bị ghi thành lỗi nhân viên, kỳ nào cũng vậy, và không ai sửa post.

---

## 2. ⛔ VÌ SAO KHÔNG CÓ LỆNH `AUTO` CHẠY CẢ HAI LUỒNG

Một hệ gộp một luồng thì sẽ có lệnh `AUTO` chạy suốt từ đầu đến cuối ra một bộ đầu ra. Repo này **cố tình ⛔ không có lệnh đó.**

Ba lý do:

```
① AUTO sinh ra MỘT file. Một file thì tường ngăn không tồn tại.

② Hai luồng có hai cổng chặn khác nhau. AUTO phải dừng ở CỔNG 0 (của I)
   trong khi luồng Q đã sẵn sàng chạy xong — nghĩa là AUTO làm luồng Q
   phải CHỜ một cái duyệt KHÔNG LIÊN QUAN GÌ đến nó.

③ Hai luồng có hai người nhận khác nhau và hai nhịp khác nhau:
   insight đi theo nhịp kế hoạch nội dung (tuần/tháng),
   QC đi theo nhịp kèm cặp (tuần).
   Một lệnh ép hai nhịp thành một.
```

★ **Thay cho `AUTO`:** chạy `ĐỌC` một lần, rồi chạy `QC` và `INSIGHT` **độc lập, lúc nào cũng được, bao nhiêu lần cũng được**. Cả hai đều đọc lại từ `out/doc-hoi-thoai.json` nên ⛔ không bao giờ lệch số.

---

## 3. ★ BẢNG THẨM QUYỀN — CÁI GÌ ĐI QUA ĐƯỢC

Bảng dữ kiện gốc (`pd-C`) có đủ mọi cột. Mỗi luồng **chỉ được đọc cột của mình**.

| Cột trong bảng gốc | Luồng I | Luồng Q | Ghi chú |
|---|---|---|---|
| `ht` (mã hội thoại `HT-nnn`) | ✅ | ✅ | Khoá chung — thứ duy nhất **bắt buộc** có ở cả hai |
| `v_rang` (`V-01`…`V-11`) | ✅ | ✅ | |
| `nhom_gt` (`V1`/`V2`/`V3`) | ✅ | ✅ | |
| `l_code` (`L1.1`…`L6.7`) | ✅ | 🔶 | Q chỉ dùng để biết **rào cản khách mang** khi chấm `TC-4` |
| `giai_doan` (`S1`/`S2`/`S3`/`CS`) | ✅ | ⬜ | |
| `rao_can` (`SỢ`/`NGỜ`/`NGẠI`) | ✅ | 🔶 | Như `l_code` |
| `bitmask` · `do_nong` | ✅ | ✅ | Q cần để xét SLA theo độ nóng |
| `cau_hoi_ngam` | ✅ | ⬜ | |
| `trich_khach` (nguyên văn lời khách) | ✅ **đã ẩn danh** | 🔶 **chỉ trong sổ tay riêng** | ★ Xem §5 |
| `post_ads` (thẻ nguồn) | ✅ | ⬜ | |
| `nv` (**tên nhân viên**) | ⛔ **KHÔNG** | ✅ | ★ Luật cứng nhất của sổ này |
| `tc[1..10]` (10 ô chấm) | ⛔ **KHÔNG** | ✅ | |
| `diem` · `loai` (A/B/C/D) | ⛔ **KHÔNG** | ✅ | |
| `co_do` (cờ đỏ) | 🔶 **chỉ đếm tổng** | ✅ đầy đủ | ★ Xem §6 |
| `loi_he` (việc hệ thống) | ✅ | ✅ | **Cả hai** — xem §7 |

Ký hiệu: ✅ đọc được · 🔶 đọc được **có điều kiện** · ⬜ không cần · ⛔ **bị chặn**

### ★ Luật cứng nhất

> **Cột `nv` ⛔ KHÔNG BAO GIỜ đi vào bất cứ đầu ra nào của luồng I.**
> Không vào JSON, không vào HTML, không vào ghi chú, không vào ví dụ minh hoạ, không vào trích dẫn.

Nếu một phát hiện insight **chỉ giải thích được bằng cách chỉ ra ai làm**, thì đó ⛔ **không phải phát hiện insight** — nó là phát hiện QC đặt sai chỗ. Chuyển sang luồng Q.

**Cách viết đúng khi luồng I phải nói về chất lượng tư vấn:**

| ⛔ Sai (lọt tên) | ✅ Đúng (ở mức hiện tượng) |
|---|---|
| *"Chị Hà trả lời 'bọc sứ không đau và không hại gì' — sai"* | *"6/14 hội thoại nhóm `V-05` được trả lời bằng tính từ trấn an thay vì cơ chế mài răng (`HT-004`, `HT-019`, …). Khách hỏi lại lần hai rồi rơi."* |
| *"Linh né giá 3 lần"* | *"Nhóm `V-05` có 3/11 hội thoại né giá hoàn toàn. ⚠ Chưa rõ là lỗi người hay chưa cấp giá dòng sứ — đã đẩy sang luồng Q đối chiếu."* |

> ⚠️ Bản đúng **mạnh hơn** bản sai, không phải yếu hơn. *"6/14 hội thoại"* là một vấn đề nội dung có thể sửa bằng một tuyến bài. *"Chị Hà"* là một vấn đề của một người, và nó không nói gì về 13 hội thoại còn lại.

---

## 4. ★★ CỔNG T — KIỂM TƯỜNG NGĂN TRƯỚC KHI XUẤT

⛔ Không file nào được xuất ra trước khi chạy đủ **sáu câu kiểm** này. Mỗi câu phải trả lời được bằng *"đã kiểm, kết quả là…"*, ⛔ không phải *"chắc là ổn"*.

```
① TÊN NHÂN VIÊN
   Tìm mọi tên nhân viên (lấy từ cột `nv` của bảng gốc) trong file sắp xuất
   của luồng I. Tìm thấy dù một lần → ⛔ DỪNG, xoá, xuất lại.
   ⚠ Kiểm cả trong trích dẫn và trong tên file.

② THÔNG TIN KHÁCH
   Tám thứ của `pd-B` §3 (tên thật · SĐT · ảnh · email · địa chỉ ·
   link cá nhân · mã đơn · tên người nhà) — ⛔ không có ở file nào
   của CẢ HAI luồng, kể cả sổ tay riêng.

③ FILE INSIGHT CÓ ĐIỂM SỐ KHÔNG
   Mọi trường `diem`, `loai`, `tc*` trong JSON insight → ⛔ phải không tồn tại.
   ⚠ Không phải "để rỗng" — phải KHÔNG CÓ KHOÁ ĐÓ.

④ FILE QC CÓ LỜI KHÁCH DÀI KHÔNG
   Trích dẫn khách trong báo cáo QC chỉ được giữ ĐÚNG phần làm bằng chứng
   cho ô ✗ đang xét. ⛔ Không chép cả hội thoại.

⑤ NHÓM MỎNG
   Nhóm dưới 10 HT → đã ẩn tỷ lệ chưa? Nhân viên dưới 10 HT → đã bỏ
   phân loại chưa? Một `V-xx` chỉ có 1–2 HT có nhận ra được cá nhân không?

⑥ CÂU CHÂN BẢNG
   Mọi bảng điểm của luồng Q có đúng câu này ở chân chưa:
   "Điểm dùng để phân việc kèm cặp. Không phải căn cứ kỷ luật hay
    xếp hạng công khai."
```

⚠️ **Kiểm ① và ③ phải làm bằng máy, không bằng mắt.** `tools/pd.py` có hàm `kiem_tuong_ngan()` chạy đúng sáu câu trên và **từ chối ghi file** nếu trượt. Chạy tay thì ⛔ sẽ có kỳ quên.

---

## 5. TRÍCH DẪN LỜI KHÁCH — QUY TẮC KHÁC NHAU Ở HAI LUỒNG

Lời khách là thứ duy nhất **cả hai luồng đều cần** mà lại cần theo hai cách:

| | Luồng I dùng để | Luồng Q dùng để |
|---|---|---|
| **Mục đích** | Chứng minh *khách đang nghĩ gì* | Chứng minh *nhân viên đã bỏ sót điều gì* |
| **Độ dài** | Câu/cụm khách tự nói, giữ nguyên chữ của khách | **Cặp đôi**: câu khách + câu nhân viên trả lời ngay sau |
| **Số lượng** | Nhiều — mỗi chân dung ≥3 trích | Ít — mỗi ô `✗` đúng **một** cặp |
| **Ẩn danh** | ✅ bắt buộc | ✅ bắt buộc |
| **Đi tới ai** | Marketing | Chỉ người đó + trưởng nhóm |

★ **Luật cặp đôi của luồng Q:** một ô `✗` mà ⛔ không gắn được `HT-nnn` + **cặp câu nguyên văn** → đổi thành `—`. ⛔ **Không có bằng chứng thì không có điểm trừ.** (Rào ② của `pd-Q1` §6.)

⚠️ Và một luật dễ quên: **trích dẫn trong sổ tay riêng của người A ⛔ không được chứa lời của khách do người B phụ trách.** Sổ tay là tài liệu kèm cặp cá nhân, không phải bản tổng hợp cả khối.

---

## 6. CỜ ĐỎ — THỨ DUY NHẤT ĐI QUA ĐƯỢC TƯỜNG, NHƯNG CHỈ MỘT CHIỀU

Cờ đỏ pháp chế (`pd-Q2`) là rủi ro pháp lý, không chỉ là lỗi tư vấn. Nó **phải tới được Marketing** — vì nếu nhân viên nói *"răng sứ dùng trọn đời"* thì rất có thể post ads cũng đang viết thế.

**Cho nên cờ đỏ đi qua tường được, nhưng bị lọc:**

| Luồng Q nhận | Luồng I nhận |
|---|---|
| Mã cờ · **ai** · `HT-nnn` · **nguyên văn câu nói** · người xử lý đích danh | Mã cờ · **số lượt** · `HT-nnn` · **nhóm `V-xx` nào hay bị** |
| → để kèm cặp đúng người | → để kiểm xem **post ads và trang đích** có đang nói câu tương tự không |

★ **Ví dụ đúng, luồng I:**
> `CĐ-P1` (*cam kết kết quả / "an toàn 100%"*) — **4 lượt**, tập trung ở `V-05` bọc sứ (`HT-004`, `HT-019`, `HT-031`, `HT-052`). ⚠️ Rà lại nhóm post *"Bọc răng sứ có phải mài nhiều răng thật không"* — nếu nội dung post cũng trấn an bằng tính từ thì nhân viên đang **nhắc lại chữ của chính chúng ta**.

⛔ **Chiều ngược lại không có.** Luồng I ⛔ không gửi gì sang luồng Q. Chân dung, hook, số ads ⛔ không được đưa vào bảng chấm điểm — nhân viên ⛔ không được chấm bằng một thứ (chân dung của kỳ) mà họ không hề biết khi đang trả lời khách.

---

## 7. VIỆC HỆ THỐNG — Ô GIAO NHAU CHÍNH ĐÁNG

Ô `✗` do **lỗi hệ** ⛔ không trừ điểm người, và nó là thứ **cả hai luồng đều phải thấy**:

| Nhóm lỗi hệ | Luồng Q thấy gì | Luồng I thấy gì |
|---|---|---|
| **Chưa cấp bảng giá** dòng trụ / dòng sứ | Ô `TC-9` chấm `—`, không trừ ai | *"Khách hỏi giá ở `n` HT mà hệ chưa có số để trả lời"* → **thiếu nội dung giá** |
| **Chưa cấp số năm bảo hành** | Ô `—` | Khách hỏi bảo hành `n` lượt → **tuyến nội dung còn trống** |
| **Chưa có danh sách cơ sở làm All-On** | Ô `—` khi khách tỉnh hỏi | Khách `V-02` ở tỉnh `n` lượt → **định tuyến sai, mất ca đắt nhất** |
| **Ngoài giờ** (sau 18h30) | `TC-1` chấm `—` | Khách nhắn ngoài giờ `n` lượt → **cân nhắc ca trực tối** |
| **Chưa có case before–after có giấy đồng ý** | Ô `—` khi khách xin ảnh | Khách xin ảnh `n` lượt → **thiếu tài sản nội dung** |

> ★ **Đây là giá trị lớn nhất của việc tách luồng.** Ở một báo cáo gộp, năm dòng trên biến thành *"nhân viên né giá, không nêu bảo hành"* — và khối trực page bị đào tạo về một việc **không phải lỗi của họ**, kỳ này qua kỳ khác. Tách ra thì cùng một dữ kiện chỉ đúng vào **việc của hệ thống**, và nó xuất hiện ở **cả hai** báo cáo nên không ai bỏ qua được.

⚠️ Mục "việc hệ thống" ⛔ không được gộp vào mục "khuyến nghị". Nó phải là **mục riêng, có tên người chịu trách nhiệm cấp dữ kiện**, không phải gạch đầu dòng trong phần nhận xét.

---

## 8. BA CÁCH TƯỜNG NGĂN BỊ PHÁ TRONG THỰC TẾ

Ghi lại để nhận ra sớm:

```
① "CHO MỖI MỘT VÍ DỤ THÔI"
   Ai đó xin một ví dụ có tên người để báo cáo insight "sinh động hơn".
   → ⛔ Không. Dùng HT-nnn. Mã hội thoại đủ truy ngược cho người CÓ QUYỀN
     truy ngược, và vô nghĩa với người không có quyền. Đó chính là mục đích.

② "GỘP HAI FILE CHO DỄ GỬI"
   Ai đó ghép hai báo cáo thành một bản PDF để gửi họp.
   → ⛔ Không. Gửi hai file, hai người nhận. Nếu buổi họp cần cả hai thì
     người chủ trì đọc hai file — đó là việc của họ, không phải việc của agent.

③ "DASHBOARD CÓ Ô ĐĂNG NHẬP RỒI"
   Ai đó đề nghị một dashboard duy nhất, phân quyền bằng mật khẩu.
   → ⛔ Không trong bản này. Dashboard ở đây là file tĩnh, publish ra link;
     ai có link là mở được. Phân quyền bằng FILE, không bằng màn hình.
```

---

## 9. TỰ KIỂM SỔ NÀY

- [ ] Sáu câu của **CỔNG T** §4 đã chạy **bằng máy** chưa?
- [ ] File insight có **khoá** `nv` / `diem` / `loai` / `tc*` nào không? (phải là *không có khoá*, không phải *khoá rỗng*)
- [ ] Có phát hiện insight nào chỉ giải thích được bằng tên người không? → chuyển sang luồng Q
- [ ] Cờ đỏ sang luồng I đã **lọc hết tên người** chưa, và đã kèm **nhóm `V-xx`** để Marketing rà post chưa?
- [ ] Có gì từ luồng I (chân dung · hook · số ads) lọt vào bảng chấm điểm không?
- [ ] Mục **"việc hệ thống"** có mặt ở **cả hai** báo cáo chưa, và có **tên người chịu trách nhiệm cấp dữ kiện** chưa?
- [ ] Sổ tay của người A có chứa lời khách của người B không?
