# BA confirmation needed — Báo cáo thống kê (nhóm FR-IX) · Xuất PDF/Excel — 2026-08-03

> **File này để làm gì:** gom các testcase mà QA **không tự chốt verdict được** vì SRS tự mâu thuẫn, kèm đầy đủ đối chiếu SRS + evidence UI để BA quyết nhanh. KHÔNG dùng file này thay bug-report.

| | |
|---|---|
| **Đợt** | Re-verify vòng 2 UAT đối tác (54 case dev báo đã fix) |
| **Ngày** | 2026-08-03 |
| **Môi trường** | https://htpldn-uat.ospgroup.vn — build **HTPLDN V1.0.4** |
| **Tài khoản test** | `cbnv_tw` (vai trò `CB_NV_TW`, phạm vi Toàn quốc) |
| **Số phiếu chờ BA** | **21** (sheet `UAT_TGPL Doanh Nghiệp-tuần 3`) |
| **Số phiếu bị ảnh hưởng gián tiếp** | **17** phiếu xuất Excel đang để `Pass` (xem câu hỏi 3) |
| **Đã ghi vào sheet** | `Verify 2` = `BA confirm` cho cả 21 phiếu; **không** đụng `Trạng thái dev fix 2` |
| **Hồ sơ mâu thuẫn gốc** | `tasks/srs-contradictions.md` → **SRS-C-010** (Open) |

**Quy tắc citation:** mọi số dòng dưới đây đã mở file kiểm trực tiếp trên bản chuẩn `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/`.

---

## 21 phiếu chờ BA (cùng 1 vấn đề) — Tệp PDF của Báo cáo thống kê có phải theo khung văn bản hành chính TT 17/2025 không

**Bối cảnh testcase**

- Sheet `UAT_TGPL Doanh Nghiệp-tuần 3`, 21 dòng:

  | Mã TC | Dòng | Báo cáo | Mã TC | Dòng | Báo cáo |
  |---|---|---|---|---|---|
  | `SLHDVM_07` | 192 | Số lượng hỏi đáp/vướng mắc PL | `VVTLHDN_06` | 247 | Vụ việc theo loại hình DN |
  | `VVDTN_07` | 197 | Vụ việc đã tiếp nhận | `VVTTGCT_06` | 249 | Vụ việc theo thời gian chi tiết |
  | `VVDHT_07` | 204 | Vụ việc đang hỗ trợ | `CPHTCT_07` | 251 | Chi phí chi trả hỗ trợ |
  | `VVDHTHT_07` | 210 | Vụ việc đã hoàn thành | `CPCTHTTDVQL_07` | 254 | Chi phí theo đơn vị |
  | `VVTTG_06` | 217 | Vụ việc theo thời gian | `CPCTHTTLHDN_07` | 258 | Chi phí theo loại hình DN |
  | `CLDTBDDDR_07` | 223 | Lớp đào tạo đang diễn ra | `CPCTHTTTG_06` | 261 | Chi phí theo thời gian |
  | `LDTBDDDR_07` | 228 | Lớp đào tạo đã diễn ra | `SLCTHT_07` | 265 | Số lượng chương trình hỗ trợ |
  | `CGTVPL_07` | 231 | Số lượng CG/TVV | `CTTDVQL_05` | 269 | Chương trình theo đơn vị |
  | `DGHQHTPL_07` | 234 | Đánh giá hiệu quả HTPL | `CTTLV_06` | 274 | Chương trình theo lĩnh vực |
  | `VVTDVQL_07` | 240 | Vụ việc theo đơn vị quản lý | `CTTTG_05` | 276 | Chương trình theo thời gian |
  | `VVTLV_06` | 244 | Vụ việc theo lĩnh vực | | | |

- Nội dung kiểm tra: `CB_NV_TW` vào **Báo cáo thống kê** → chọn loại báo cáo → Kỳ = Năm 2026 → Đơn vị = Toàn quốc → **[Xem báo cáo]** → **[Xuất PDF]** → chọn A4 / Dọc → **[Xuất file]**.
- Expected trong file UAT (câu chữ chung của 21 phiếu): *"Tạo tệp PDF theo mẫu Thông tư 17/2025/TT-BTP — A4, Times New Roman 13, có header; tự tải về máy"*; một số phiếu ghi thêm quy ước tên tệp và hỗ trợ ký số.
- Actual đối tác ghi (retest 31/07): *"Hệ thống hiển thị thông báo Forbidden"*.

**Kết quả verify UI hiện tại**

- Verify lại **03/08/2026** qua Chrome DevTools MCP (thao tác thật trên giao diện, không gọi API trực tiếp), tài khoản `cbnv_tw`.
- **Lỗi "Forbidden" đã hết** ở cả 21 phiếu: `POST /api/v1/bao-cao/export` trả **200**, `content-type: application/pdf`, tệp tự tải về máy. Bộ quan sát DOM (cài trước khi bấm, không lọc trùng) chỉ bắt được thông báo *"Đang tạo file..."*, không có thông báo lỗi nào.
- Nội dung tệp đã mở đọc để kiểm (không chỉ kiểm tệp tạo được):
  - Khổ giấy **A4** (595 × 842 pt) ✔
  - Phông **Tinos Regular/Bold** — bộ metric tương đương Times New Roman ✔
  - Đầu tệp có đủ 4 mục: **tên báo cáo · Kỳ báo cáo · Đơn vị · Ngày tạo** ✔
  - Số liệu trong tệp **khớp số liệu trên màn hình** ✔ (vd `SLHDVM_07`: Tổng 61 · Đã trả lời 20 · Chờ 41 · 32.8% · Lao động 21 · Thuế 10)
  - **Không có quốc hiệu / tên cơ quan ban hành ở đầu trang** ✘
  - **Không có ngày ký / chức danh người ký ở cuối trang** ✘
  - Tên tệp dạng `bao-cao-<slug>-YYYY-MM-DD.pdf` (vd `bao-cao-hoi-dap-2026-08-03.pdf`)
- **Đối chiếu nội bộ:** báo cáo theo mẫu TT 17/2025 thật (Đánh giá hiệu quả → tab Báo cáo → Xuất DOCX/XLSX) **đã có đủ** quốc hiệu, tiêu ngữ, dòng *"(Theo mẫu Thông tư số 17/2025/TT-BTP)"*, mục I→V và bảng ký. Tức hệ thống **có** dựng được khung TT 17/2025, nhưng cố ý chỉ áp cho báo cáo đó — không áp cho nhóm IX.
- Evidence: `evidence/SLHDVM_07-bao-cao-hoi-dap.pdf` · `evidence/CGTVPL_07-bao-cao-so-luong-cg-tvv.pdf` (2 tệp PDF thật lấy từ hệ thống ngày 03/08/2026).

**Điểm mâu thuẫn trong SRS v3.5**

1. **Nguồn A — FR-IX buộc PDF "theo Thông tư 17/2025":**
   - `srs-fr-11-bao-cao.md:86` — *"Nếu xuất PDF: tạo file .pdf giữ nguyên định dạng trình bày theo Thông tư 17/2025 (khổ A4, font Times New Roman cỡ 13)"*
   - `srs-fr-11-bao-cao.md:124` — Tiêu chí chấp nhận: *"tải file .pdf theo format TT17/2025"*
   - `srs-fr-11-bao-cao.md:1052-1053` — SCR, nút Xuất Excel/Xuất PDF *"→ xuất theo format TT17/2025"*

2. **Nguồn B — "format chung theo TT 17/2025" bao gồm cả khung hành chính, và bảng mapping gán khung đó cho toàn bộ nhóm IX:**
   - `srs-v3.5.md:6669` — heading *"**Format chung theo TT 17/2025:**"*
   - `srs-v3.5.md:6672` — *"Header: Quốc hiệu + Tên cơ quan ban hành"*
   - `srs-v3.5.md:6673` — *"Footer: Ngày ký + Chức danh người ký + Con dấu (nếu in chính thức)"*
   - `srs-v3.5.md:6666-6667` — bảng D.2.4 chỉ liệt kê **Mẫu 21a / 21b**, nhưng cột "FR tham chiếu" lại gán cả hai cho **`FR-IX-01~23 (TPL-REPORT-FULL)`** — tức kéo toàn bộ 23 chức năng báo cáo nhóm IX vào khung này.

3. **Nguồn C — mô tả riêng phần đầu tệp của nhóm IX lại chỉ có 4 mục, không có quốc hiệu/khối ký:**
   - `srs-fr-11-bao-cao.md:1092` — *"Export XLSX/PDF chèn tiêu đề BC + thông tin kỳ + đơn vị + ngày tạo vào header file"*

4. **Hai điểm hai nguồn thống nhất là KHÔNG có trong đặc tả nhóm IX:**
   - Quy ước đặt tên tệp `BaoCaoXxx_{YYYYMMDD_HHmm}` — chỉ FR-II-01 có (`HoiDap_{YYYYMMDD_HHmm}.xlsx`); FR-XIII lại dùng kiểu chữ thường gạch nối (`kho-cau-hoi-{YYYYMMDD-HHmm}.xlsx`).
   - "Hỗ trợ ký số điện tử" — chỉ FR-III-20 (Đào tạo) yêu cầu.

5. **Chính đặc tả cũng đang tự cảnh báo:** CHANGELOG v3→v4 (đổi Word → PDF) ghi *"Cần Cán bộ phụ trách xác nhận Thông tư 17/2025 có thực sự yêu cầu PDF hay chấp nhận Word — đoạn trích dẫn về Mẫu 21a/21b cũng chưa được tra cứu lại"*. Lưu ý D.2.3 (Export format) khai định dạng xuất của Mẫu 21a/21b là **Excel (.xlsx) + Word (.docx)**, **không có PDF**.

**Câu hỏi cần BA xác nhận**

1. **Tệp PDF của màn Báo cáo thống kê (nhóm FR-IX) có phải trình bày theo khung văn bản hành chính TT 17/2025 không** — tức có quốc hiệu + tên cơ quan ở đầu trang và ngày ký + chức danh người ký ở cuối trang? Hay chỉ cần 4 mục header theo `srs-fr-11-bao-cao.md:1092`?
   1. **Hướng 1 — theo Nguồn B (có bắt buộc):** tệp PDF phải có quốc hiệu, tên cơ quan, ngày ký, chức danh người ký. ⇒ phần mềm hiện **thiếu**, là lỗi thật.
   2. **Hướng 2 — theo Nguồn C (không bắt buộc):** tệp PDF chỉ cần A4 + Times New Roman 13 + 4 mục header. ⇒ phần mềm hiện **đã đúng**.
2. Tùy câu 1, đặc tả cần dọn lại cho hết mâu thuẫn:
   - Nếu **Hướng 1**: khối D.2.4 cần ghi rõ áp cho cả nhóm IX, và D.2.3 cần bổ sung PDF vào danh mục định dạng xuất.
   - Nếu **Hướng 2**: nên bỏ cụm *"theo Thông tư 17/2025"* ở `srs-fr-11-bao-cao.md:86` / `:124` / `:1052-1053`, vì cụm này đang kéo theo cả khung hành chính ngoài ý định.
3. **Quy ước đặt tên tệp xuất của nhóm IX (áp cho cả .xlsx lẫn .pdf)** — chọn kiểu `BaoCaoXxx_{YYYYMMDD_HHmm}` (như đối tác kỳ vọng, giống FR-II-01), hay kiểu chữ-thường-gạch-nối (như FR-XIII và như phần mềm đang làm), hay xác nhận **không quy định**?
   > ⚠️ Câu này xin BA trả lời **kể cả khi câu 1 chốt là "không bắt buộc"**, vì nó quyết định **17 phiếu xuất Excel đang để `Pass`** có phải mở lại hay không.
4. **Báo cáo nhóm IX có cần hỗ trợ ký số điện tử không?** (Hiện chỉ FR-III-20 Đào tạo yêu cầu.)

**Đề xuất QA tạm thời**

- **Chưa chuyển 21 phiếu này cho Dev** cho tới khi BA chốt nguồn đúng — chấm Pass thì bỏ qua chỗ lệch, chấm Reopen thì đẩy cho dev một yêu cầu chưa chắc có trong đặc tả.
- Verdict tạm cho cả 21 phiếu: **`BA confirm`** (đã ghi `Verify 2` trên sheet).
- **QA nghiêng về Hướng 2 (không bắt buộc khung hành chính)**, vì chính CHANGELOG mô tả nhóm IX là *"báo cáo phục vụ cán bộ và lãnh đạo trong nội bộ cơ quan, khác báo cáo định kỳ gửi cấp trên thuộc nhóm FR-15"* — tức báo cáo nghiệp vụ nội bộ, không phải văn bản trình ký. Khung TT 17/2025 giữ nguyên cho Mẫu 21a/21b và báo cáo Đánh giá hiệu quả.
- **Nếu BA chốt Hướng 1:** 21 phiếu chuyển `Reopen`, owner **Dev BE** (bổ sung quốc hiệu + khối ký vào bản dựng PDF của nhóm IX).
- **Nếu BA chốt Hướng 2:** 21 phiếu chuyển `Pass`, đồng thời QA đề nghị **cập nhật lại câu chữ "Kết quả mong đợi"** của 21 phiếu UAT cho khớp đặc tả.
- **Nếu BA chốt câu 3 theo hướng "có quy ước tên tệp":** thêm **17 phiếu xuất Excel** đang `Pass` phải mở lại (CLDTBDDDR_06, LDTBDDDR_06, CGTVPL_06, DGHQHTPL_06, CLDTBDPL_06, VVTDVQL_06, VVTLV_05, VVTLHDN_05, VVTTGCT_05, CPHTCT_06, CPCTHTTDVQL_06, CPCTHTTLHDN_06, CPCTHTTTG_05, SLCTHT_06, CTTDVQL_04, CTTLV_05, CTTTG_04).

---

## Ô điền cho BA

| Câu hỏi | Quyết định của BA | Ngày chốt | Người chốt |
|---|---|---|---|
| 1. PDF nhóm IX có theo khung hành chính TT 17/2025? | | | |
| 2. Dọn câu chữ đặc tả theo hướng nào? | | | |
| 3. Quy ước đặt tên tệp xuất nhóm IX? | | | |
| 4. Nhóm IX có cần ký số điện tử? | | | |

> Sau khi BA điền bảng trên, QA sẽ cập nhật `Verify 2` cho 21 phiếu (và 17 phiếu Excel nếu câu 3 đổi), đồng thời đóng mục **SRS-C-010** trong `tasks/srs-contradictions.md`.
