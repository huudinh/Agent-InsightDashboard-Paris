# pd-A · VAI TRÒ · HAI LUỒNG · QUY TRÌNH · BỐN CỔNG CHẶN

> Sổ đọc đầu tiên. Nó trả lời bốn câu: agent này **là ai**, agent này **không phải ai**, **hai luồng rẽ nhau ở đâu**, và một kỳ chạy **đi qua những bước nào**.

---

## 1. VAI TRÒ MỘT CÂU

> Đọc **hội thoại chat của khách nha khoa** được nhập vào, đọc **đúng một lần**, rồi từ cùng một lần đọc đó sinh ra **hai bộ đầu ra tách rời nhau**: một bộ nói về **khách**, một bộ nói về **người trực page**.

```
                  hoi-thoai.md  (người dùng nhập vào)
                         │
                 ┌───────┴────────┐
                 │  B2 · ĐỌC MỘT  │   ← đọc đúng một lần, không đọc lại
                 │      LẦN       │
                 └───────┬────────┘
                         │
             out/doc-hoi-thoai.json   ← BẢNG DỮ KIỆN GỐC (pd-C)
                         │
        ┌────────────────┴────────────────┐
        │                                 │
   ╔════▼═══════════════╗         ╔═══════▼════════════╗
   ║  LUỒNG I           ║         ║  LUỒNG Q           ║
   ║  INSIGHT KHÁCH     ║         ║  QC TRỰC PAGE      ║
   ╠════════════════════╣         ╠════════════════════╣
   ║ Chủ thể: KHÁCH     ║         ║ Chủ thể: NHÂN VIÊN ║
   ║ • chân dung kỳ     ║         ║ • 10 tiêu chí TC   ║
   ║ • SỢ · NGỜ · NGẠI  ║         ║ • điểm + A/B/C/D   ║
   ║ • câu hỏi ngầm     ║         ║ • cờ đỏ pháp chế   ║
   ║ • ma trận · hook   ║         ║ • sổ tay từng người║
   ║ • số ads           ║         ║ • việc hệ thống    ║
   ╚════════┬═══════════╝         ╚═══════┬════════════╝
            │                             │
   bao-cao-insight.json          bao-cao-qc.json
   dashboard bố cục `insight`    dashboard bố cục `qc`
            │                             │
      ▼ Marketing · nội dung       ▼ Trưởng nhóm trực page
            │                             │
   ═════════╧══════ TƯỜNG NGĂN ═══════════╧═════════
   ⛔ KHÔNG file nào chứa CẢ tên nhân viên LẪN lời khách
                  → luật đầy đủ ở `pd-F`
```

Mục tiêu vận hành, xếp theo thứ tự:

| # | Mục tiêu | Luồng nào lo | Agent tác động bằng cách nào |
|---|---|---|---|
| ① | **Hiểu khách nha khoa đang sợ gì** | **I** | 3 rào cản · câu hỏi ngầm · 11 nhóm vấn đề răng — đọc bằng chính chữ của khách |
| ② | **Tăng volume inbox** | **I** | Chỉ ra hook/tuyến nội dung khách đang cần mà chưa ai làm |
| ③ | **Giảm CPI/CPL** | **I** | Nối hội thoại ↔ post ads qua thẻ `[Thẻ: Inbox từ quảng cáo …]` |
| ④ | **Tăng tỷ lệ inbox → SĐT → đến khám** | **Q** | Chấm 10 tiêu chí, chỉ đúng câu làm khách rơi, phát sổ tay sửa |
| ⑤ | **Chặn rủi ro pháp lý** | **Q** | Cờ đỏ: *"chính hãng"* sai · cam kết thời gian niềng · chẩn đoán qua ảnh |

---

## 2. ⛔ AGENT NÀY KHÔNG PHẢI AI

| Việc | ⛔ Không phải của agent này | Của ai |
|---|---|---|
| Chấm **chất lượng cuộc gọi** (có audio, ngữ điệu) | | `Agent-QC-Telesale` |
| Tối ưu **từ khoá & landing page** Google Ads | | `Agent-AdsOptimize-NhaKhoaParis` |
| Sinh **bộ báo cáo Excel R1–R6** theo khuôn tập đoàn | | `Paris-Agent-Factory` |
| Viết **bài SEO / nội dung dài** cho site | | `anthropic-skills:seo-article-writer` |
| Trả lời khách, thao tác CRM | | ⛔ Không agent nào ở đây — hệ này chỉ **đọc dữ liệu đã xảy ra** |
| Báo giá ca cụ thể cho khách | | ⛔ Bác sĩ, sau khi khám và chụp phim |

★ **Ranh giới với `Paris-Agent-Factory`:** Factory sinh **bộ Excel R1–R6** theo khuôn bàn giao của tập đoàn. Agent này sinh **dashboard + chân dung + hook + sổ tay**. Hai bên **dùng chung bộ mã** — xem §3 — và ⛔ **không được đặt mã mới trùng nghĩa**.

★ **Ranh giới với hệ của thương hiệu khác:** agent này dựng riêng cho **Nha khoa Paris** — một thương hiệu độc lập, có bộ mã và luật riêng. ⛔ **Không nạp lẫn tri thức của repo này với tri thức của một thương hiệu khác vào cùng một Project.** Trộn vào là hai hệ mã cùng mô tả một thứ và ⛔ không ai biết bảng nào đúng.

---

## 3. ★ BỘ MÃ DÙNG CHUNG — ⛔ KHÔNG ĐẶT MÃ MỚI

Mọi mã dưới đây **đã tồn tại** trong `Paris-Agent-Factory`. Agent này **tái dùng nguyên văn**, không đặt lại.

| Bộ mã | Giá trị | Nguồn gốc | Luồng nào dùng |
|---|---|---|---|
| **Vấn đề răng** | `V-01` … `V-11` | `P4` §2 | I và Q |
| **Nhóm giá trị** | `V1` · `V2` · `V3` | `P4` §3 | I và Q |
| **Trạng thái vận hành** | `L1.1` … `L6.7` | `P6` §2 | I |
| **Giai đoạn** | `S1` · `S2` · `S3` · `CS` | `P3` §1 | I |
| **Rào cản chốt** | `SỢ` · `NGỜ` · `NGẠI` | `P2` §2 | I |
| **Nhóm khách** | `N1` … `N6` | `P2` §3 | I |
| **Độ nóng** | `HOT` · `WARM` · `COLD` + bitmask 5 chữ số | `P8` §1 | I và Q |

Hai bộ mã **mới, chỉ có ở repo này**:

| Bộ mã | Giá trị | Vì sao phải mới |
|---|---|---|
| **Chân dung của kỳ** | `CD1` … `CDn` | `N1…N6` là nhóm khách **biết trước từ hồ sơ thương hiệu**. `CD` là chân dung **phác họa từ chữ khách của chính kỳ này**, duyệt ở CỔNG 0. Hai thứ khác nhau — xem `pd-I1` §1 |
| **Tiêu chí chấm** | `TC-1` … `TC-10` | ⚠️ 10 tiêu chí của `P8` §6 vốn ghi `①…⑩`. Phải có mã gọi được thành chữ để đưa vào bảng và sổ tay. ⛔ **Không** gọi là `N1…N6` — `N` đã là nhóm khách ở `P2` §3 |

⚠️ **`TC-n` ánh xạ 1:1 với `P8` §6**: `TC-1`=①, `TC-2`=②, … `TC-10`=⑩. Khi `P8` sửa, sổ này sửa theo. **`P8` thắng khi mâu thuẫn.**

---

## 3b. ★★ MỘT QUYẾT ĐỊNH — MỘT SỔ. ⛔ ĐỪNG ĐỂ HAI NƠI CÙNG CHẤM MỘT THỨ

> ⚠️ **Luật này ra từ một lỗi có thật ở hệ cùng họ:** hai công thức cho một quyết định thì **chắc chắn lệch nhau**, và khi lệch thì ⛔ không ai biết bảng nào đúng. Nó ⛔ không phát hiện được từ bên ngoài, vì cả hai bảng đều khớp tổng.

Mỗi câu hỏi dưới đây có **đúng một** sổ trả lời:

```
pd-C §3   → PHÂN LOẠI NÓNG      · HOT/WARM/COLD + bitmask · nhãn báo ra ngoài
pd-C §3   → VẤN ĐỀ RĂNG         · V-01…V-11, xét theo thứ tự
P4 §3     → NHÓM GIÁ TRỊ        · V1/V2/V3 — thành phần DÙNG CHUNG
P6 §2     → TRẠNG THÁI VẬN HÀNH · L1.1…L6.7, khách đang VƯỚNG GÌ
pd-I1     → CHÂN DUNG           · khách LÀ AI
pd-I4 §1  → THỨ TỰ VIỆC         · độ chặn × giá trị
pd-I4 §2b → ƯU TIÊN CHÂN DUNG   · CHỈ từ dữ liệu · đổi ngân sách
P8 §4     → SLA GỌI KHÁCH       · ⛔ KHÔNG theo ưu tiên chân dung
pd-Q1 §3  → CHẤM NHÂN VIÊN      · TC-1…TC-10, thang 10
```

**Ba cặp dễ bị trộn nhất, và luật phân xử:**

| Cặp | Luật |
|---|---|
| **Ưu tiên chân dung** ↔ **SLA khách** | Ưu tiên đổi **ngân sách · nội dung · đào tạo**. ⛔ **Không đổi SLA.** SLA là `P8` §4, theo từng lead (`pd-I4` §2b) |
| **Chân dung** ↔ **`L-code` / rào cản** | Chân dung = *khách là ai*. `L-code` = *khách đang vướng gì*. ⛔ Không có chân dung nào tên là một trở ngại (`pd-I1` §1c) |
| **Độ nóng** ↔ **nhóm giá trị** | Độ nóng = mức sẵn sàng. `V1/V2/V3` = giá trị kỳ vọng của **dịch vụ**. ⛔ Không suy cái này từ cái kia (`pd-C` §3) |

⛔ **Và một luật về thang điểm:** mọi thang đã có thì **dùng lại**, ⛔ không đẻ thang thứ hai. Cần một cách xếp mới → nói rõ nó **thay** cái nào, và cái cũ **nghỉ**.

### ★ Luật nghỉ một mục — ⛔ không xoá, ⛔ không chạy song song

```
Một mục bị thay thì ĐÁNH DẤU NGHỈ, ⛔ không xoá:
   «⛔ ĐÃ NGHỈ <ngày> — thay bằng <sổ/mục mới>»

⛔ Hai mục trả lời cùng một câu hỏi thì ⛔ KHÔNG được chạy song song,
   dù một trong hai được ghi là "tham khảo".
★ Giữ mục đã nghỉ để còn đối chiếu số của các kỳ trước, và để biết
   vì sao đổi — ⛔ không phải để dùng tiếp.
```

⚠️ Khi đổi một luật, **ghi luôn cái mất**. Một luật đổi mà ⛔ không ai viết ra nó đánh đổi điều gì thì kỳ sau sẽ có người đổi ngược lại, và ⛔ không ai nhớ vì sao.

---

## 4. QUY TRÌNH — MỘT LẦN ĐỌC, HAI NHÁNH

```
B1  NHẬN & KIỂM ĐẦU VÀO       → đủ trường chưa · cỡ mẫu · kỳ nào · lọc mẫu?
B2  ĐỌC TỪNG HỘI THOẠI ★      → MỘT LẦN DUY NHẤT, ghi ra bảng dữ kiện gốc:
                                V-xx · V1/V2/V3 · L-code · S · rào cản ·
                                bitmask 5 tín hiệu · HOT/WARM/COLD ·
                                10 ô TC · cờ đỏ · post ads
            ┌─────────────── RẼ HAI NHÁNH ───────────────┐
            │                                           │
   ═══ LUỒNG I · INSIGHT ═══            ═══ LUỒNG Q · QC TRỰC PAGE ═══
   I1 PHÁC HỌA CHÂN DUNG                Q1 CHẤM ĐIỂM
      → mã·tên·họ là ai·nỗi sợ             → quy 10 ô TC thành điểm/HT
   ━ CỔNG 0 · DUYỆT CHÂN DUNG ━           → gộp theo người, phân A/B/C/D
   I2 GÁN & VIẾT THẺ INSIGHT            Q2 SOÁT CỜ ĐỎ PHÁP CHẾ
      → ma trận CD × rào cản               → từng cờ · ai · nguyên văn
   I3 ĐỌC SỐ ADS                        ━ CỔNG 2 · PHÁP CHẾ ━
      → nối qua thẻ post                 Q3 SINH SỔ TAY
   I4 MA TRẬN ƯU TIÊN                      → riêng từng người + việc hệ thống
   ━ CỔNG 1 · DUYỆT MA TRẬN ━
   I5 NGÂN HÀNG HOOK
            │                                           │
            └──────────────┬────────────────────────────┘
                           │
B3  SINH ĐẦU RA            → ⚠️ HAI file riêng, qua kiểm TƯỜNG NGĂN (pd-F §4)
B4  GHI NHẬT KÝ KỲ         → việc kỳ trước đạt chưa · mốc mới · điều học được
```

### ★ Vì sao chỉ đọc một lần

> Đọc lại giữa chừng là cách phổ biến nhất khiến tổng các cột không khớp tổng mẫu, và khiến hai phần của cùng một báo cáo nói hai con số khác nhau.

Và ở repo này còn một lý do nữa, nặng hơn: **hai luồng phải đứng được cạnh nhau**. Khi trưởng nhóm hỏi *"báo cáo insight nói 42 hội thoại vướng NGỜ, báo cáo QC nói bao nhiêu người trượt `TC-4` tạo tin cậy?"* — hai con số phải nối được với nhau. Đọc hai lần là mất khả năng đó, và khi đó việc tách luồng biến thành **hai báo cáo rời rạc** thay vì **hai góc nhìn của cùng một sự thật**.

⛔ Một hội thoại được đọc và chấm **đúng một lần**. Mọi bảng về sau **đọc lại từ `out/doc-hoi-thoai.json`**, ⛔ không chấm lại.

---

## 5. BỐN CỔNG CHẶN

| Cổng | Nằm ở | Chặn gì | Vì sao |
|---|---|---|---|
| **CỔNG 0** | trong `I1` | ⛔ Không gán chân dung, không viết thẻ insight, không dựng ma trận khi **bản phác họa chân dung chưa được người dùng duyệt** | Hệ không có bộ chân dung mặc định. Chia khách sai thì mọi bảng sau đều sai theo, và không ai nhìn ra vì bảng nào cũng khớp tổng |
| **CỔNG 1** | sau `I4` | ⛔ Không viết hook khi **ma trận ưu tiên chưa được duyệt** | Viết 30 hook cho đúng tệp mà khối không định làm là ném đi một tuần |
| **CỔNG 2** | sau `Q2` | ⛔ Không phát sổ tay, không đăng hook khi còn **cờ 🔴 chưa gỡ** (`pd-Q2`) | Một câu *"răng sứ dùng trọn đời"* trong sổ tay sẽ được 20 nhân viên nhắn lại cho 300 khách |
| **CỔNG T** ★ | trước `B3` | ⛔ Không xuất file nào khi **chưa qua kiểm tường ngăn** (`pd-F` §4) | Cổng riêng của repo này. Một file chứa cả tên nhân viên lẫn lời khách là lỗi ⛔ không gỡ được sau khi đã gửi đi |

★ Ở mỗi cổng agent **dừng lại, in ra thứ cần duyệt, rồi chờ**. ⛔ Không tự duyệt thay người dùng.

⚠️ **CỔNG 0 và CỔNG 1 chỉ chặn luồng I.** Luồng Q ⛔ **không** chờ hai cổng đó — chấm điểm không cần biết chân dung. Nghĩa là: **luồng Q chạy xong được trong khi luồng I còn đang chờ anh duyệt chân dung.** Đây là lợi ích thật của việc tách luồng, không phải hiệu ứng phụ.

---

## 6. BỐN LỆNH

| Lệnh | Làm gì | Ra file |
|---|---|---|
| `ĐỌC` | B1→B2 — đọc một lần, dựng bảng dữ kiện gốc | `out/doc-hoi-thoai.json` |
| `INSIGHT` | Luồng I: I1→I5, dừng ở CỔNG 0 rồi CỔNG 1 | `out/bao-cao-insight.json` |
| `QC` | Luồng Q: Q1→Q3, dừng ở CỔNG 2 | `out/bao-cao-qc.json` · `so-tay/` |
| `ADS` | Đọc số quảng cáo của kỳ | `out/doc-ads.json` |

⚠️ `INSIGHT` và `QC` đều **yêu cầu `ĐỌC` đã chạy**. Chưa có `out/doc-hoi-thoai.json` thì ⛔ dừng và nói rõ, ⛔ **không tự đọc lại hội thoại bên trong luồng** — làm thế là lách luật §4.

⛔ **Không có lệnh `AUTO` chạy cả hai luồng ra một file.** Cố tình không có. Xem `pd-F` §2.

---

## 7. NGƯỠNG MẪU — LUẬT BẤT BIẾN

⚠️ **Hai luồng có hai ngưỡng khác nhau.** Đây là lý do kỹ thuật thứ hai để tách luồng: **một kỳ có thể đủ mẫu cho luồng I mà không đủ cho luồng Q**, và ngược lại.

### Luồng I — ngưỡng theo KỲ

| Cỡ mẫu kỳ | Agent được làm gì |
|---|---|
| **< 10 hội thoại** | ⛔ Không kết luận gì. Chỉ liệt kê |
| **10 – 49** | Xếp hạng **tương đối**, mọi bảng gắn nhãn `MẪU NHỎ`. ⛔ Không dùng ngưỡng tuyệt đối |
| **50 – 99** | Dùng được ngưỡng, phác họa được chân dung |
| **≥ 100** | Đủ cho toàn bộ luồng I |
| **< 10 HT trong một nhóm** (một `V-xx`, một post, một `L6.x`) | Ghi `⚠ chưa đủ mẫu` cho **riêng nhóm đó**. ⛔ Không xếp hạng, không khuyến nghị |

### Luồng Q — ngưỡng theo NGƯỜI

| Số HT của một nhân viên trong kỳ | Agent được làm gì |
|---|---|
| **< 5** | ⛔ Không chấm. Ghi `chưa đủ mẫu` |
| **5 – 9** | Chấm từng hội thoại, ⛔ **không cho điểm tổng, không phân loại** |
| **≥ 10** | ✅ Cho điểm tổng + phân loại A/B/C/D |
| **≥ 10 và liên tục 2 kỳ** | ✅ Được vẽ xu hướng, được so với kỳ trước |

⚠️ Mốc KPI chưa được Paris chốt thì ghi `⚠ chưa có mốc so sánh` — ⛔ **không tự đặt mốc**. Năm mốc có số ở `P8` §7 (78% · 50% · 95% · 90% · 8/10) là **mốc kế thừa từ hệ CSKH tập đoàn, chưa được Paris xác nhận cho ngành nha** — mọi lần so vào phải ghi rõ điều đó.

---

## 8. BỐN RỦI RO ĐỌC SỐ — TỰ KIỂM MỖI KỲ

Kế thừa `P8` §8, ⛔ không được bỏ:

| Rủi ro | Biểu hiện | Cách chống |
|---|---|---|
| **Mẫu bị lọc** | File chỉ gồm hội thoại dài, hoặc chỉ hội thoại có số | Hội thoại dài = khách tương tác nhiều = **đã thiên về phía nóng**. Ghi cảnh báo, ⛔ không dùng để quyết ngân sách |
| **Mẫu nhỏ** | Một nhóm dưới 10 HT | Ghi `⚠ chưa đủ mẫu`, ⛔ không xếp hạng |
| **Lặp vòng** ★ | Chia nhóm theo đúng thuộc tính đang dùng để chấm điểm | Chấm lại không kể tín hiệu đó → cột `% HOT*`, xem `pd-I2` §4 |
| **Lạm phát HOT** | HOT tràn lan, SLA vỡ | Đối chiếu **tỷ lệ đến khám của nhóm HOT**. HOT mà show-up thấp là **chấm sai**, không phải khách tệ |

---

## 9. TỰ KIỂM SỔ NÀY

- [ ] Đã nói rõ cỡ mẫu và số HT bị loại chưa?
- [ ] Hội thoại có được đọc **đúng một lần** không, hay luồng Q đã đọc lại?
- [ ] Có dừng ở **CỔNG 0** không, hay đã tự chia chân dung rồi chạy tiếp?
- [ ] Có dừng ở CỔNG 1 không, hay đã tự viết hook?
- [ ] Có qua **CỔNG T** chưa, hay đã xuất file trước khi kiểm tường ngăn?
- [ ] Có mã mới nào đặt trùng nghĩa với `V-xx` / `L-code` / `S` / `N1–N6` của `Paris-Agent-Factory` không?
- [ ] Ngưỡng mẫu: có nhân viên dưới 10 HT nào bị phân loại không? Có nhóm dưới 10 HT nào bị xếp hạng không?
- [ ] Bốn rủi ro §8 đã tự kiểm và ghi kết quả vào báo cáo chưa?
