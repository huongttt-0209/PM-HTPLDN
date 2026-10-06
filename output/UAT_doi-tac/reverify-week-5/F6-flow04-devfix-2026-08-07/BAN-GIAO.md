# Bàn giao — lô F6 FLOW 04 (4 case dev báo đã fix) · 07/08/2026

**Quy trình áp dụng:** [`flows/04-verify-bug-dev-fix-khong-ho-so.md`](../../../../flows/04-verify-bug-dev-fix-khong-ho-so.md)
**Nguồn chuẩn chấm duy nhất:** `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/` (đúng đường dẫn prompt cấp)
**Bảng ghi kết quả:** spreadsheet `1OKBN2otlmdZ44THkmhtsn-_63M2Boh7zQwearwjYR3s`, tab **`bug`** (gid 1714340219)
**Môi trường đo:** `https://18.143.165.120.nip.io` (env **nội bộ**), tài khoản **`cbnv_tw_04`** theo prompt

---

## 1. Kết quả 4 case

| Dòng | Mã TC | Verdict | Ô "Trạng thái dev fix" | Vì sao |
|---:|---|---|---|---|
| **65** | `DGKQHTVV_02` | 🟡 **Cần BA** | `BA confirm` | 3/6 vế đo được **đều đạt**; 3 vế còn lại đặc tả **chưa quy định** (bộ nhãn + bố cục nhóm Đánh giá · có thêm 2 trường Người/Ngày đánh giá không · tiêu chí "không tràn, không bẻ vỡ" cho vùng nhóm chi tiết · số chữ số thập phân của điểm tổng) |
| **68** | `DGKQHTVV_04` | ✅ **Pass** | `Test done` | 2/2 vế `MATCH` đạt. Bộ điểm phân biệt **4-8-9 → 7** loại trừ mọi công thức sai; không có ô nhập điểm tổng ⇒ đúng "tự động tính" |
| **285** | `QLNDTVVCG_19` | ✅ **Pass** | `Test done` | **5/5 vế `MATCH` đều đạt.** Env đã sẵn hồ sơ `TVCS-QLND19-UAT` kèm 2 đánh giá ⇒ thoát được kịch bản "Chưa chốt" |
| **288** | `QLNDTVVCG_38` | 🟡 **Cần BA** | `BA confirm` | **4/4 vế `MATCH` (C1–C4) đều đạt — web hiện tại ĐÚNG kỳ vọng đối tác**, triệu chứng *"Phân công hàng loạt chưa được hỗ trợ"* **không còn tái hiện**. Còn 1 vế `GAP` (C5 — chọn một chuyên gia chung hay riêng từng hồ sơ) đặc tả im lặng |

**Cả 4 ô đã ghi lên Drive và đã đọc lại xác nhận.** Ô `Kết quả verify` (cột T) của cả 4 dòng đều đã có nội dung
đầy đủ; **4 ô chỉ đọc `Trạng thái` · `Kết quả thực tế` · `TKM phản hồi lần 1` · `DEV phản hồi lần 1` KHÔNG bị
đụng tới** (chốt chặn `--expect` của công cụ ghi chỉ cho phép sửa đúng 2 cột R và T).

### 1.1 Điểm cần người điều phối đọc kỹ — dòng 288

Prompt giả định *"SRS chỉ quy định phân công từng bản ghi và không hề có hàng loạt"*. **Giả định đó KHÔNG đúng.**
`srs-fr-12-tv-chuyen-sau.md:1127` quy định rõ nút `[Phân công CG hàng loạt]` cho bản ghi `TIEP_NHAN`, và yêu cầu
này **có từ bản v3** (`srs-v3/srs-fr-12:886`). Đúng lúc đó, hộp thoại từ chối trong ảnh của đối tác lại **viện dẫn
chính `srs-fr-12`** để biện minh cho việc không hỗ trợ. Nếu web còn hiện hộp thoại đó thì đã là **Reopen**, không
phải chuyện BA. Thực đo trên env nội bộ: **đã làm đúng đặc tả**, nên chỉ còn vế câu chữ C5 chờ BA.

---

## 2. Lỗi mới phát sinh

| Mã TC | Dòng sheet | Mức | Nội dung |
|---|---:|---|---|
| `QLNDTVVCG_QA01` | **376** (thêm mới, cuối bảng) | Câu chữ hiển thị | Nhãn trạng thái màn danh sách Tư vấn chuyên sâu lệch bảng nhãn đặc tả `srs-fr-12:1130–1140`: `PHAN_CONG` hiện **"Phân công"** (đặc tả **"Đã phân công"**, `:1135`) · `HUY` hiện **"Hủy"** (đặc tả **"Đã hủy"**, `:1140`). `TIEP_NHAN` và `DA_DUYET` thì khớp |

Đã điền đúng bộ ô prompt yêu cầu: `Mã TC` · `Tên chức năng` · `Mô tả` · `Các bước thực hiện` · `Kết quả mong đợi` ·
`Kết quả thực tế` · `Trạng thái = Fail` · `Dopai = bug` · `Ảnh/vieo 1 = link Drive xem được`. Đã đọc lại khớp 9 ô.

**Phát lộ hợp lệ**, không phải mở rộng phạm vi: vế C4 của dòng 288 **buộc** phải đọc lại nhãn trạng thái của từng
hồ sơ sau khi phân công. Chỉ khẳng định 2 trạng thái đã trực tiếp nhìn thấy; **không đi rà nốt 5 trạng thái còn lại**
(Flow 04 cấm mở rộng case để điều tra).

**Ứng viên lỗi khác:** không có. Không gặp mã lỗi 4xx/5xx, không phải đi vòng ở bất kỳ bước nào trong 4 case.

---

## 3. Dữ liệu đã thay đổi trên môi trường — bắt buộc đọc trước khi chạy lại

| Case | Bản ghi | Thay đổi | Còn dùng lại được? |
|---|---|---|---|
| Dòng 65 | — | **Không đổi gì** (chỉ đọc) | — |
| Dòng 68 | `VV-QAW7-DG01` | `HOAN_THANH` → `DA_DANH_GIA`; thêm 1 đánh giá của cán bộ (4-8-9, nhận xét `QA-DGKQ-20260807-0220`) | ❌ **Đã tiêu** — hệ thống chặn đánh giá lần hai cùng loại người. Dự phòng: `VV-QAW7-TRALOI-UBND`, `VV-QAW7-TV-MANGLUOI`, `VV-QA-001`…`VV-QA-007` |
| Dòng 285 | — | **Không đổi gì** (chỉ đọc) | — |
| Dòng 288 | `TVCS-QLND38-UAT-01` + `TVCS-QLND38-UAT-02` | `TIEP_NHAN` → `PHAN_CONG`, gán CG `Chuyên gia UAT QLNDTVVCG 38`, `version 1 → 2`, ghi chú `QA-QLND38-20260807-0240` | ❌ **Đã tiêu** — không còn ở `TIEP_NHAN`. Dự phòng cùng lĩnh vực Thương mại: `TVCS-20260805-0003`, `TVCS-20260805-0001`, `TVCS-20260803-0003`, `TVCS-20260725-0008/0007/0001`, `TVCS-20260721-0001`, `TVCS-TNND01-UAT`, `TVCS-20260806-0003` |

**Không đụng dữ liệu của đối tác** ở bất kỳ case nào — mọi bản ghi bị thay đổi đều là dữ liệu UAT dựng riêng cho
chính case đó.

---

## 4. 🔴 Bản dựng — verdict của 4 case KHÔNG cùng một bó mã

Env deploy **5 lần** trong 12 tiếng, **2 lần rơi vào giữa phiên đo**:

| Case | Bó mã FE đã đo | `last-modified` |
|---|---|---|
| Dòng 65, 68 | `index-DsMHK7Dp.js` | `06 Aug 2026 18:51:25 GMT` (07/08 01:51 giờ VN) |
| Dòng 285, 288 | `index-D4Buvu4S.js` | `06 Aug 2026 19:23:01 GMT` (07/08 02:23 giờ VN) |

Chi tiết + mốc thời gian đầy đủ: [`BAN-DUNG.md`](BAN-DUNG.md).

⚠️ **Chuỗi phiên bản ở chân sidebar KHÔNG dùng được làm vân tay.** Đọc `HTPLDN · V1.0.9` ở **cả ba** bó mã
`index-B2W2Krcs.js` · `index-DsMHK7Dp.js` · `index-D4Buvu4S.js`. Hồ sơ lô F3 cùng ngày
(`F3-devfix-2026-08-07/TIEN-DO.md:169`, `do/CNDSMLTVV_01.md:16`) ghi `index-B2W2Krcs.js` ứng với `V1.0.10` —
**lệch với đo lại**. **Không tự sửa hồ sơ lô F3**, để người điều phối chốt. Kể từ nay dùng **tên bó mã +
`last-modified`**.

---

## 5. Giới hạn hiệu lực chung

1. **Đo trên env nội bộ, đối tác đo trên env nghiệm thu `htpldn-uat.ospgroup.vn`** với bản dựng cũ hơn (ảnh dòng 288
   cho thấy chân sidebar `V1.0` và tên các thẻ phân loại khác hẳn). Mọi verdict chỉ có hiệu lực cho **env + bó mã
   đã ghi**.
2. **Không có ảnh "lỗi cũ" do chính bên kiểm thử phía này chụp** ở cả 4 case ⇒ theo ca biên Flow 04, chỉ kết luận
   được **hiện trạng đúng/sai so với đặc tả**, **không** kết luận được "bản sửa có tác dụng".
3. Chỉ dòng 288 có ảnh bằng chứng của đối tác (`partner-evidence/QLNDTVVCG_38.jpg`); 3 case còn lại phiếu không khai
   tệp nào ⇒ tiền đề phải tự dựng, đã khai rõ trong từng hồ sơ đo.

---

## 6. Việc còn lại cho người điều phối

1. **Gửi BA 2 câu hỏi** — dòng 65 (4 mục a-d) và dòng 288 (một chuyên gia chung hay riêng từng hồ sơ; xử lý ra sao
   khi các hồ sơ chọn thuộc lĩnh vực khác nhau). Nguyên văn ở `do/DGKQHTVV_02.md` và `do/QLNDTVVCG_38.md §8`.
2. **Chuyển dev dòng 376** (`QLNDTVVCG_QA01`) — sửa 2 nhãn trạng thái.
3. **Chốt chênh lệch chuỗi phiên bản** giữa lô F6 và lô F3 (§4).
4. Nếu cần đo lại dòng 68 hoặc 288 → dùng bản ghi dự phòng ở §3, **không** dùng lại bản ghi đã tiêu.

---

## 7. Hồ sơ trong thư mục này

| Thư mục | Nội dung |
|---|---|
| `chuan/` | Chuẩn chấm đã khóa **trước khi mở màn** (Giai đoạn A) — 4 tệp, có `BUG SCOPE LOCK` từng vế `Cn` |
| `do/` | Hồ sơ đo (Giai đoạn B) — 4 tệp, gồm verdict · số liệu thô · đối chứng độc lập · bẫy đã tránh · giới hạn |
| `note/` | Đúng chữ đã ghi vào ô `Kết quả verify` của 4 dòng |
| `audit/` | Bản đồ 26 cột tab `bug` + giá trị **cũ** của 4 ô trước khi ghi (cả 4 ô `Kết quả verify` đều **trống**) |
| `image/` | 10 ảnh bằng chứng, **đã tải lên Drive lấy link xem được** (`tools/evidence_drive_links_f6devfix.json`) |
| `partner-evidence/` | `QLNDTVVCG_38.jpg` — ảnh gốc của đối tác |
| `bug-moi/` | Bộ ô đã ghi cho dòng lỗi mới `QLNDTVVCG_QA01` |
| `BAN-DUNG.md` | Vân tay bản dựng theo từng mốc deploy |

**Ô sheet chỉ chứa link Drive xem được, không chứa đường dẫn tệp trên máy** — đường dẫn nội bộ trong ô sheet coi
như không có bằng chứng.
