# pd-C · BẢNG DỮ KIỆN GỐC — MỘT LẦN ĐỌC

> Sổ này định nghĩa **thứ duy nhất mà cả hai luồng cùng đọc**: một bảng, một hàng cho một hội thoại, sinh ra ở `B2` và ⛔ không bao giờ sửa lại.

---

## 1. VÌ SAO PHẢI CÓ BẢNG NÀY

Nếu hai luồng mỗi luồng tự đọc hội thoại, sẽ xảy ra đúng ba chuyện:

```
① TỔNG LỆCH NHAU
   Báo cáo insight nói 119 HT, báo cáo QC nói 112 HT (vì QC bỏ HT không có NV).
   Không ai biết bên nào đúng, và cả hai đều mất uy tín.

② CÙNG MỘT HỘI THOẠI, HAI ĐỘ NÓNG
   Luồng I chấm HT-031 là WARM, luồng Q chấm HOT (vì xét SLA).
   Hai lần đọc độc lập thì ⛔ KHÔNG có cách nào bắt được sai lệch này.

③ KHÔNG NỐI ĐƯỢC HAI BÁO CÁO
   Câu hỏi "42 HT vướng NGỜ — có bao nhiêu được nhân viên nêu bằng chứng
   đối tác hãng?" ⛔ KHÔNG trả lời được, vì hai bên không chung khoá.
```

★ Bảng này là **khoá chung**. Hai luồng là **hai cách đọc một sự thật**, ⛔ không phải hai sự thật.

---

## 2. MỘT HÀNG — ĐẦY ĐỦ CÁC Ô

`out/doc-hoi-thoai.json`:

```json
{
  "schema": "doc-hoi-thoai-paris/1",
  "ky": "01-15/11",
  "tao_luc": "2026-11-16T09:12:00+07:00",
  "co_mau": { "doc": 119, "loai": 7, "ly_do_loai": { "ngoai-pham-vi": 4, "khong-co-loi-khach": 2, "cs-tai-kham": 1 } },
  "canh_bao_mau": ["⚠ Không có HT nào dưới 2 lượt khách — file có thể đã bị lọc"],
  "ht": [
    {
      "ht": "HT-001",

      "_": "─── Ô CHUNG · cả hai luồng ───",
      "ngay": "03/11", "gio_mo": "09:12",
      "so_luot_kh": 5, "so_luot_nv": 4,
      "co_sdt": true,
      "v_rang": "V-03", "nhom_gt": "V1",
      "bitmask": "10111", "do_nong": "HOT", "do_nong_sao": "HOT*",
      "co_do": ["CĐ-P4"],
      "loi_he": [],

      "_2": "─── Ô CỦA LUỒNG I ───",
      "i": {
        "l_code": "L4.1",
        "giai_doan": "S2",
        "rao_can": ["NGỜ"],
        "nhom_khach": "N1",
        "cau_hoi_ngam": ["Các anh có tráo vật liệu của tôi không"],
        "post_ads": "QC_Implant_Straumann",
        "loi_hua_post": "ăn nhai như răng thật",
        "trich_khach": ["trụ của mình là trụ gì ạ, có chính hãng không. em nghe nói nhiều nơi tráo trụ"],
        "dau_gia_dinh": false,
        "lam_o_dau": "noi-khac",
        "cd": null
      },

      "_3": "─── Ô CỦA LUỒNG Q ───",
      "q": {
        "nv": "Trần Thu",
        "phut_tra_loi_dau": 1,
        "trong_gio": true,
        "tc": {
          "TC-1": "✓", "TC-2": "✓", "TC-3": "✓", "TC-4": "✓", "TC-5": "✓",
          "TC-6": "✓", "TC-7": "—", "TC-8": "—", "TC-9": "✓", "TC-10": "✓"
        },
        "bang_chung": {
          "TC-4": ["KH: trụ của mình là trụ gì ạ, có chính hãng không",
                   "NV: Paris là đối tác của Straumann, mỗi trụ có mã riêng và phiếu bảo hành ghi rõ dòng trụ"]
        },
        "ghi_chu_he": []
      }
    }
  ]
}
```

### ★ Vì sao các ô được lồng vào `i` và `q`

> Không phải để cho gọn. Đây là **tường ngăn được cài vào chính cấu trúc dữ liệu**.

Khi xuất báo cáo, luồng I lấy `ht[].i` + các ô chung; luồng Q lấy `ht[].q` + các ô chung. Hàm sinh báo cáo ⛔ **không nhận cả object `ht[]`** — nó nhận đúng nhánh của mình. Nghĩa là **lọt tên nhân viên vào báo cáo insight là một lỗi phải cố tình mới làm được**, không phải lỗi quên.

⚠️ `co_do` nằm ở **ô chung**, không nằm trong `q` — vì cờ đỏ đi qua tường được (`pd-F` §6). Nhưng khi vào báo cáo insight nó **bị lọc còn mã + số lượt + `HT-nnn`**, ⛔ bỏ nguyên văn và ⛔ bỏ tên người.

---

## 3. BA Ô TRỌNG YẾU — CHẤM THẾ NÀO

### `v_rang` — 11 nhóm vấn đề răng

Xét **theo thứ tự ưu tiên từ `V-01` xuống `V-11`**, đúng nhóm đầu tiên thì lấy, ⛔ không xét tiếp. Bảng từ khoá đầy đủ ở `P4` §2.

★ Hai luật ghi đè, ⛔ không được bỏ:
- Khách nói **sửa lại ca cũ** → luôn `V-01`, kể cả có nêu dịch vụ gì. Vì cách tư vấn hoàn toàn khác.
- Khách vừa nói **mất răng** vừa nói **đau** → `V-03`, ghi chú *"kèm đau"*.

### ★★ Thứ tự kiểm **là một phần của luật**

```
Xét theo THỨ TỰ V-01 → V-11. Nhóm khớp ĐẦU TIÊN quyết định.
⛔ Không chấm điểm. ⛔ Không lấy nhóm trúng nhiều từ khoá nhất.

① Tiền sử can thiệp · ca đã làm hỏng     ← xét TRƯỚC  (V-01)
② Tình trạng răng · mục tiêu thẩm mỹ     ← xét SAU    (V-02…V-10)
```

> ⚠️ **Đảo thứ tự là xếp một ca sửa hỏng thành ca làm lần đầu** — rồi tư vấn sai, báo giá sai, và **mất một khách đã từng bị hỏng một lần**. Đây là nhóm ngờ nặng nhất của ngành nha (`N5`, `pd-I2` §3).

⛔ Thứ tự này để **nhận diện đúng**, ⛔ **không phải** thứ tự ưu tiên kinh doanh. Ưu tiên kinh doanh nằm ở `pd-I4` §1 và **chỉ tính từ dữ liệu**.

### ★ Một hội thoại hỏi NHIỀU dịch vụ

```
Chọn dịch vụ khách hỏi SÂU NHẤT (nhiều lượt nhất · có mô tả tình trạng).
Ghi các dịch vụ còn lại vào ô `dv_khac` để bán chéo.
⛔ KHÔNG tách thành hai hội thoại — tổng mẫu sẽ lệch, và cùng một
   người bị đếm hai lần trong mọi bảng.
```

★ Ngành nha rất hay gặp việc này: *"em muốn niềng, mà răng khôn có phải nhổ trước không, với cạo vôi luôn"* — ba dịch vụ, một người, một hội thoại. `pd-I3` §1 bảng cross-sell cho biết hướng tiếp theo tự nhiên.

### `nhom_gt` — V1 / V2 / V3

Suy từ `v_rang` + dịch vụ khách nêu. Bảng ở `P4` §3.

⚠️ **`nhom_gt` ⛔ không suy từ độ nóng, và ⛔ không suy từ số tiền khách nói.** Nó là **giá trị kỳ vọng của dịch vụ**, không phải mức sẵn sàng của khách. Một khách COLD hỏi All-On vẫn là `V1`.

### `bitmask` + `do_nong` — 5 tín hiệu

Bitmask 5 chữ số theo `P8` §1. `[10110]` = có ①③④, thiếu ②⑤.

> ⛔ **Không có bitmask thì không ai kiểm lại được điểm.** Mọi hàng phải có.

Ba luật ghi đè của ngành nha (`P8` §1), ⛔ không được bỏ:

```
① Đã đặt lịch khám, hoặc đang đến phòng khám        → HOT bất kể điểm
② Đã có phim X-quang, hoặc đã khám nơi khác và có
   phác đồ/báo giá rồi                              → HOT bất kể điểm
③ Đang đau cấp (V-06)                               → tối thiểu WARM
```

★ Luật ② là luật dễ bỏ sót nhất và đắt nhất: khách đã qua giai đoạn chẩn đoán, **chỉ còn chọn nơi làm** — lead nóng nhất của ngành nha, mà thang 5 tín hiệu thường chấm thấp oan cho họ.

### `do_nong_sao` — chấm lại không kể tín hiệu ①

⚠️ **Luật chống lặp vòng, bắt buộc.** Tín hiệu ① là *"nêu dịch vụ/tình trạng cụ thể"*. Mọi nhóm `V-01`…`V-10` **đã được cộng sẵn 1 điểm**, còn `V-11 chưa rõ` thì không. So `% HOT` giữa các nhóm `V` là so một thứ **đã được định nghĩa sẵn** → kết luận giả.

Nên mỗi hàng có **thêm** `do_nong_sao`: chấm lại chỉ bằng ②③④⑤, đạt **≥3/4** là `HOT*`.

★ Luật này áp cho **mọi** lần chia nhóm theo một thuộc tính vốn là tín hiệu chấm điểm — ⛔ không chỉ riêng tín hiệu ①. Chi tiết ở `pd-I2` §4.

---

## 4. LUẬT MỘT LẦN ĐỌC

```
① Một hội thoại được đọc và chấm ĐÚNG MỘT LẦN, ghi vào bảng này.
② Mọi bảng về sau (chân dung · ma trận · hook · điểm · sổ tay)
   ĐỌC LẠI TỪ BẢNG NÀY. ⛔ Không chấm lại.
③ Bảng này sau khi ghi là BẤT BIẾN trong kỳ.
   Cần sửa → sửa rồi CHẠY LẠI CẢ HAI LUỒNG, ⛔ không sửa một bên.
④ Ngoại lệ DUY NHẤT được ghi thêm sau: ô `i.cd`,
   điền sau khi anh duyệt CỔNG 0. ⛔ Không ô nào khác.
```

⚠️ **Luật ③ là luật hay bị phá nhất.** Khi anh chỉ ra một hội thoại bị đọc sai, phản xạ tự nhiên là sửa trong báo cáo đang mở. Làm thế thì báo cáo kia vẫn giữ số cũ, và **tường ngăn biến thành hai sự thật** — đúng cái mà `pd-F` §1 nói là mục đích của việc tách luồng chứ không phải hậu quả.

→ Đúng cách: sửa `out/doc-hoi-thoai.json`, chạy lại `INSIGHT` **và** `QC`, ghi vào `doc/CHANGELOG.md` dòng *"kỳ … sửa `HT-nnn`: … → chạy lại cả hai luồng"*.

---

## 5. ⛔ Ô `cd` TRƯỚC CỔNG 0

Mọi hàng có `i.cd = null` khi `ĐỌC` vừa chạy. ⛔ Không đoán, ⛔ không gán tạm, ⛔ không dùng `nhom_khach` (`N1`…`N6`) thay thế.

★ `nhom_khach` và `cd` là **hai thứ khác nhau**:

| | `nhom_khach` `N1…N6` | `cd` `CD1…CDn` |
|---|---|---|
| Từ đâu | **Biết trước** từ hồ sơ thương hiệu (`P2` §3) | **Phác họa từ chữ khách của chính kỳ này** |
| Suy ra được không | ✅ suy được từ `v_rang` + tuổi + dấu hiệu | ⛔ Không — phải đọc và phác họa |
| Có cần duyệt | ⛔ Không | ✅ **CỔNG 0** |
| Đổi theo kỳ | ⛔ Không | ✅ Có — `CD3` kỳ này ⛔ không phải `CD3` kỳ trước |

⚠️ Dùng `N1…N6` làm chân dung là lỗi **im lặng**: mọi bảng vẫn khớp tổng, trông vẫn đúng, nhưng báo cáo chỉ nói lại điều đã biết từ trước và ⛔ không phát hiện được gì mới của kỳ.

---

## 6. TỰ KIỂM SỔ NÀY

- [ ] Mọi hàng có `bitmask` chưa? Hàng nào thiếu là hàng ⛔ không kiểm lại được
- [ ] Mọi hàng có `do_nong_sao` chưa?
- [ ] Ba luật ghi đè độ nóng (§3) đã áp chưa — nhất là luật ② *đã có phim X-quang*?
- [ ] `v_rang` xét **theo thứ tự ưu tiên** chưa, hay lấy nhóm khớp nhiều từ khoá nhất?
- [ ] `nhom_gt` có bị suy từ độ nóng không?
- [ ] `i.cd` còn `null` hết chưa (trước CỔNG 0)?
- [ ] Các ô có **lồng đúng** vào `i` / `q` chưa, hay còn phẳng ở mức hội thoại?
- [ ] Nếu đã sửa một hàng: đã chạy lại **cả hai** luồng chưa?
