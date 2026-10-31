# pd-D · HAI SCHEMA DASHBOARD · HAI FILE

> ⚠️ **Repo này có HAI schema, ⛔ không phải một.** Tường ngăn (`pd-F`) được cài vào chính chỗ này: hai luồng ⛔ không dùng chung một file dữ liệu, nên ⛔ không có cách nào lọt từ bên này sang bên kia.

---

## 1. HAI SCHEMA

| Schema | File | Bố cục | Ai mở |
|---|---|---|---|
| `insight-dashboard-paris/1` | `dashboard/data/insight-<ky>.json` | `insight` | Marketing · nội dung · ads |
| `qc-trucpage-paris/1` | `dashboard/data/qc-<ky>.json` | `qc` | ⛔ **Chỉ** trưởng nhóm trực page |

⛔ **Hai schema ⛔ không tương thích với nhau, và ⛔ không tương thích với `insight-dashboard-kangnam/1` hay `insight-dashboard-knqt/1`.** Hai thư mục `data/` riêng là **không** đủ — phải hai **file** riêng, vì tường ngăn là tường giữa hai file.

⚠️ Trang `dashboard/index.html` **⛔ không bao giờ sửa**. Mỗi kỳ chỉ sinh thêm file JSON; trang tự đọc `bo_cuc` trong file rồi dựng đúng bộ tab.

---

## 2. SCHEMA `insight-dashboard-paris/1`

```json
{
  "schema": "insight-dashboard-paris/1",
  "bo_cuc": "insight",
  "ky": "01-15/11",
  "thuong_hieu": "Nha khoa Paris",
  "tao_luc": "2026-11-16T09:12:00+07:00",

  "the_so": [
    { "nhan": "Hội thoại đọc", "so": 119, "phu": "7 bị loại" },
    { "nhan": "% có SĐT", "so": "41%", "phu": "49/119" },
    { "nhan": "HOT", "so": "22%", "phu": "HOT* 14%" },
    { "nhan": "Chưa được chạm", "so": 6, "canh_bao": true },
    { "nhan": "Ngoài 7 tỉnh (L2.5)", "so": 11, "canh_bao": true }
  ],

  "truc": {
    "v_rang":  [{ "ma": "V-03", "ten": "Mất răng lẻ", "n": 28, "hot": "32%", "hot_sao": "18%", "gt": "V1" }],
    "nhom_gt": [{ "ma": "V1", "n": 51, "hot": "25%", "hot_sao": "16%" }],
    "giai_doan":[{ "ma": "S3", "n": 44, "hot": "30%", "hot_sao": "19%" }],
    "rao_can": [{ "ma": "NGỜ", "luot": 71, "l_code": ["L6.2", "L6.7"] }],
    "l_code":  [{ "ma": "L6.7", "ten": "Ngờ vật liệu", "n": 23, "neu_ten_hang": 9 }]
  },
  "cach_dem_rao_can": "Đếm theo lượt: 119 HT → 164 lượt. Một HT mang được 2–3 rào cản.",

  "chan_dung": [
    {
      "cd": "CD2", "ten": "Em làm ở chỗ khác rồi, giờ muốn sửa",
      "n": 14, "pc_mau": "12%", "gt": "V1-V2", "v_rang": "V-01",
      "hot": "21%", "hot_sao": "14%", "co_sdt": "36%",
      "ho_la_ai": "…", "insight": "…", "cau_hoi_ngam": ["…"],
      "rao_chu_dao": "NGỜ", "bang_chung_go": ["…"], "roi_o_dau": "S3",
      "lam_bang": ["HT-012", "HT-034", "HT-057"]
    }
  ],
  "cd0": { "n": 18, "pc_mau": "15%" },
  "nhom_n_vang_mat": ["N6 · gia đình & trẻ em — 0 HT"],

  "ads": {
    "co_so_lieu": true,
    "post": [{ "ma": "QC_Implant_Straumann", "loi_hua": "ăn nhai như răng thật",
               "chi": 0, "cpi": 0, "cpl": 0, "n_ht": 19,
               "cau_hoi_dau": { "hoi_gia": 3, "neu_tinh_trang": 14 }, "khuon": "khop" }],
    "phe_u": { "inbox": 119, "co_sdt": 49, "ket_noi": null, "dat_lich": null, "den_kham": null },
    "canh_bao_phe_u": "⚠ chưa đo được show-up — ⛔ không lấy đặt lịch thay"
  },

  "ma_tran": [{ "stt": 1, "viec": "…", "vi_sao": "23/119 HT", "nham": "CD2 · V1 · NGỜ",
                "chan": "L6.7", "ai_lam": "Marketing", "do_bang": "…" }],
  "cach_xep_ma_tran": "Xếp theo độ chặn; cùng mức thì V1 lên trước. ⚠ Chưa xếp theo giá trị kỳ vọng vì chưa đo được show-up.",

  "hook": [{ "ma": "HK-01", "cau": "Mất răng 2 năm rồi — giờ trồng còn kịp không?",
             "nham": "CD1 · V-03 · V1", "go_rao": "SỢ", "l_code": "L6.5",
             "chang": "S1", "bang_chung": ["…"], "lam_bang": ["HT-003"],
             "co_phap_che": "🟢", "ly_do_co": null }],
  "khe_con_trong": [{ "rao": "NGỜ · L6.7", "vi_sao": "⛔ Chưa cấp số năm bảo hành (slot ②)" }],

  "co_do_tong": [{ "ma": "CĐ-P2", "luot": 7, "v_rang_hay_gap": ["V-05"], "ht": ["HT-047"] }],
  "viec_he_thong": [{ "nhom": "Chưa cấp bảng giá theo dòng", "n_ht": 14, "ai_cap": "Marketing/Kế toán" }],
  "slot_cho": [{ "stt": 2, "ten": "Số năm bảo hành", "cho_may_ky": 3, "chan": "CĐ-P8" }],
  "tu_kiem_4_rui_ro": { "mau_bi_loc": "…", "mau_nho": "…", "lap_vong": "…", "lam_phat_hot": "…" }
}
```

### ⛔ Năm khoá ⛔ KHÔNG BAO GIỜ tồn tại trong file này

```
nv · tc · diem · loai · bang_chung
```

★ **⛔ Không phải "để rỗng" — phải KHÔNG CÓ KHOÁ.** Khoá rỗng là khoá sẽ có ngày được điền. `kiem_tuong_ngan()` của `tools/pd.py` kiểm đúng điều này và **từ chối ghi file** nếu thấy (`pd-F` §4 câu ③).

⚠️ `co_do_tong` **có** trong file insight, nhưng **đã lọc**: chỉ `mã` · `số lượt` · `HT-nnn` · `nhóm V-xx hay gặp`. ⛔ Không `nguyên văn`, ⛔ không `ai` (`pd-F` §6).

---

## 3. SCHEMA `qc-trucpage-paris/1`

```json
{
  "schema": "qc-trucpage-paris/1",
  "bo_cuc": "qc",
  "ky": "01-15/11",
  "tao_luc": "2026-11-16T09:40:00+07:00",
  "chan_bang": "Điểm dùng để phân việc kèm cặp. Không phải căn cứ kỷ luật hay xếp hạng công khai.",

  "the_so": [
    { "nhan": "Hội thoại chấm", "so": 112, "phu": "7 HT không có NV" },
    { "nhan": "Số tiêu chí chấm được", "so": "8/10", "phu": "TC-7, TC-8 = — cả khối" },
    { "nhan": "Điểm trung bình khối", "so": "7,4", "phu": "chuẩn P8 ≥ 8,0" },
    { "nhan": "Cờ đỏ", "so": 19, "canh_bao": true },
    { "nhan": "Ô chờ đối chiếu", "so": 23, "canh_bao": true }
  ],

  "phan_bo": { "A": 1, "B": 3, "C": 4, "D": 1, "chua_du_mau": 3 },

  "chi_so_doi": [
    { "tc": "TC-1", "ten": "Phản hồi ≤2'", "dat": "71%", "n_cham": 84, "n_mien": 28,
      "ly_do_mien": "ngoài giờ 8h30–18h30" },
    { "tc": "TC-4", "ten": "Tạo tin cậy bằng bằng chứng", "dat": "48%", "n_cham": 96, "n_mien": 16,
      "ly_do_mien": "chưa cấp bảo hành / case before–after" }
  ],

  "ca_nhan": [
    { "nv": "…", "n_ht": 23, "diem": 8.2, "loai": "B",
      "tc_yeu": "TC-4", "tc_manh": "TC-1", "co_do": [] }
  ],

  "co_do": [
    { "ma": "CĐ-P2", "ht": "HT-047", "nv": "…",
      "nguyen_van": "…", "ngu_canh": "khách hỏi phôi sứ (L6.7)",
      "sai_o_dau": "…", "cau_dung": "…",
      "nguoi_xu_ly": "…", "han": "2026-11-20",
      "goc": "noi-dung" }
  ],

  "cho_doi_chieu": [
    { "tc": "TC-9", "ht": "HT-019", "nguyen_van": "…",
      "cau_hoi": "Bảng giá có dòng Nacera chưa, con số có khớp?",
      "nhanh": { "co_khop": "✓", "co_lech": "✗ + CĐ-P5", "chua_cap": "—" },
      "nguoi_doi_chieu": "…" }
  ],

  "viec_he_thong": [
    { "nhom": "Chưa cấp số năm bảo hành", "n_o": 16, "o": ["TC-4"],
      "ai_cap": "Khoa Chuyên môn", "cap_roi_go_duoc": "16 ô TC-4 + 5 cờ CĐ-P8" }
  ],
  "chua_duoc_cham": { "n": 6, "ht": ["HT-061"] },
  "tc_yeu_nhat_khoi": ["TC-4", "TC-10", "TC-3"],
  "tc_loai_khoi_dao_tao": [{ "tc": "TC-4", "vi_sao": "phần lớn ô trượt là lỗi hệ → ST-HT" }]
}
```

### ⛔ Bốn khoá ⛔ KHÔNG BAO GIỜ tồn tại trong file này

```
chan_dung · hook · ma_tran · ads
```

★ Chiều ngược của tường ngăn (`pd-F` §6, rào ⑤ của `pd-Q1` §6): nhân viên ⛔ không được chấm bằng một thứ họ ⛔ không biết khi đang trả lời khách.

⚠️ Khoá `ca_nhan` **có trong file**, nhưng dashboard bố cục `qc` **⛔ không vẽ nó ra tab công khai** — nó chỉ xuất ra `so-tay/` (`pd-Q3`). File `qc-*.json` ⛔ không được publish ra link công khai.

---

## 4. BỐ CỤC TAB

### Bố cục `insight` — 6 tab

| Tab | Nội dung | Nguồn |
|---|---|---|
① **Tổng quan** | 5 thẻ số · 4 rủi ro tự kiểm | `the_so` · `tu_kiem_4_rui_ro`
② **Ba trục** | `V-xx` · `V1/V2/V3` · `S` · rào cản · `L-code` — ★ mọi bảng có cột `HOT*` | `truc`
③ **Chân dung** | Thẻ từng `CD` + `CD0` + nhóm `N` vắng mặt | `chan_dung`
④ **Quảng cáo** | Hiệu quả post · ★ bảng *"post hứa gì ↔ khách hỏi gì"* · phễu | `ads`
⑤ **Việc & hook** | Ma trận · ngân hàng hook theo chặng · ★ khe còn trống | `ma_tran` · `hook`
⑥ **Việc hệ thống** | Slot chờ · cờ đỏ **đã lọc** · tin chưa được chạm | `viec_he_thong` · `slot_cho`

### Bố cục `qc` — 5 tab

| Tab | Nội dung | Nguồn |
|---|---|---|
① **Tổng quan** | 5 thẻ số · phân bố A/B/C/D · ★ câu chân bảng | `the_so` · `phan_bo`
② **Chỉ số đội** | % đạt từng `TC-1…TC-10` + số ô miễn + lý do miễn | `chi_so_doi`
③ **Cờ đỏ** | Từng cờ đủ 6 ô · gốc nội dung / gốc hệ | `co_do`
④ **Chờ đối chiếu** | Từng ô `?` đủ 5 thứ | `cho_doi_chieu`
⑤ **Việc hệ thống** | Gom theo nguyên nhân · ★ cột *"cấp rồi gỡ được gì"* | `viec_he_thong`

⛔ **Bố cục `qc` ⛔ không có tab "bảng cá nhân".** Cố tình. Bảng cá nhân chỉ ra `so-tay/`.

---

## 5. BA QUY TẮC HIỂN THỊ

```
① NHÓM DƯỚI 10 HT → ẨN TỶ LỆ, chỉ hiện số đếm, gắn nhãn "⚠ chưa đủ mẫu".
   Trang tự làm, ⛔ không chờ người nhớ.

② MỌI BẢNG CHIA THEO V-xx / rào cản / S / CD → PHẢI CÓ CỘT HOT*.
   Thiếu cột đó thì trang hiện cảnh báo đỏ ngay trên bảng (pd-I2 §4).

③ Ô NÀO ⛔ KHÔNG CÓ DỮ LIỆU → chip "⏸ chờ dữ kiện" + tên slot.
   ⛔ KHÔNG hiện 0, ⛔ KHÔNG hiện "—" trơn, ⛔ KHÔNG bỏ trống.
   Lý do: 0 và "chưa đo" trông giống nhau trên biểu đồ, và
   người đọc luôn hiểu thành 0.
```

---

## 6. PUBLISH MỘT KỲ

★ **Bản một file gửi được:** nhúng file kỳ vào ô `<script type="application/json" id="pd-data">` của `dashboard/index.html` rồi publish file đó. Trang đọc khối nhúng **trước** `data/index.json`, nên bản một file ⛔ không cần máy chủ tĩnh. File kỳ **tự khai bố cục** qua trường `bo_cuc`.

⚠️ **Trước khi publish — ba câu:**

```
① File này là file nào? insight hay qc?
   → ⛔ File qc-*.json ⛔ KHÔNG publish ra link công khai. Chỉ gửi file,
     cho đúng trưởng nhóm.

② Đã chạy kiem_tuong_ngan() chưa? (pd-F §4, sáu câu)

③ Artifact mặc định RIÊNG TƯ. Chuyển sang "ai có link đều mở được"
   thì ⛔ ĐỪNG dán link vào repo public — kể cả file insight,
   vì nó chứa lời khách (đã ẩn danh) và kết luận nội bộ.
```

---

## 7. TỰ KIỂM SỔ NÀY

- [ ] File insight có khoá `nv` / `tc` / `diem` / `loai` / `bang_chung` không? (phải **không có khoá**)
- [ ] File qc có khoá `chan_dung` / `hook` / `ma_tran` / `ads` không?
- [ ] `co_do_tong` trong file insight đã **lọc hết** `nguyen_van` và `ai` chưa?
- [ ] Mọi bảng chia theo `V-xx` / rào cản / `S` / `CD` có cột `HOT*` chưa?
- [ ] Nhóm dưới 10 HT đã ẩn tỷ lệ chưa?
- [ ] Ô thiếu dữ liệu hiện **chip "⏸ chờ dữ kiện"** hay hiện `0`?
- [ ] Câu chân bảng có trong file qc chưa?
- [ ] Sắp publish: file đang publish là `insight` hay `qc`?
