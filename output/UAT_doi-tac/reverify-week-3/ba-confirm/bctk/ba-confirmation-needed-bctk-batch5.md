# BA confirmation needed — BCTK Batch 5 (BUTTON: nút "In báo cáo" không hiển thị) — 2026-07-21

> **File này để làm gì:** gom 6 testcase batch 5 mà QA verify xong nhưng cần BA phản hồi đối tác. Cả 6 cùng 1 gốc: đối tác kỳ vọng có nút "In báo cáo" trên màn Báo cáo thống kê, nhưng SRS SCR-IX-01 KHÔNG quy định nút này (chỉ spec 4 nút). App hiện đúng SRS → bất đồng về **đặc tả**, không phải bug → BA chốt có bổ sung chức năng In không.

> **Quy tắc citation:** SRS v3.5 = `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md`. Mọi khẳng định dẫn số dòng thực đã mở file kiểm.

> **Tài khoản verify:** `cbnv_tw_02` (CB Nghiệp vụ - Trung ương #02, CB_NV_TW, phạm vi Toàn quốc). Kỳ báo cáo = Năm 2026, đơn vị = Toàn quốc; cả 6 báo cáo đều có dữ liệu thực khi Xem báo cáo.

---

## SLHDVM_08 · VVDTN_08 · VVDHT_08 · VVDHTHT_08 · VVTTG_07 · CLDTBDDDR_08 — Đối tác kỳ vọng nút "In báo cáo" mà SRS không quy định (cụm 6 case cùng gốc)

**Bối cảnh testcase**

- 6 dòng Excel / mã TC:
  - Dòng 193 · `SLHDVM_08` — BC Số lượng hỏi đáp/vướng mắc pháp luật (FR-IX-01 / UC124).
  - Dòng 198 · `VVDTN_08` — BC Vụ việc đã tiếp nhận (FR-IX-02 / UC125).
  - Dòng 205 · `VVDHT_08` — BC Vụ việc đang hỗ trợ (FR-IX-03 / UC126).
  - Dòng 211 · `VVDHTHT_08` — BC Vụ việc đã hoàn thành (FR-IX-04 / UC127).
  - Dòng 218 · `VVTTG_07` — BC Vụ việc theo thời gian (FR-IX-05 / UC128).
  - Dòng 224 · `CLDTBDDDR_08` — BC Lớp đào tạo đang diễn ra (FR-IX-06 / UC129).
- Nội dung kiểm tra: Cán bộ nghiệp vụ mở màn Báo cáo thống kê (SCR-IX-01), tìm chức năng "In báo cáo".
- Expected trong file UAT (đối tác): có nút "In báo cáo" → mở xem trước + hộp thoại in của trình duyệt.
- Actual đối tác ghi: "Màn hình không hiển thị nút chức năng" (không tìm thấy nút In báo cáo).

**Đối chiếu SRS v3.5**

- SCR-IX-01 §Thành phần màn hình (bảng toolbar/action-bar) chỉ quy định **4 nút** trên màn Báo cáo thống kê:
  - Nút **Làm mới** (toolbar).
  - Nút **Xem báo cáo** (action-bar, primary).
  - Nút **Xuất Excel (.xlsx)** (action-bar, hiện sau khi Xem báo cáo).
  - Nút **Xuất PDF (.pdf)** (action-bar, hiện sau khi Xem báo cáo).
- SRS **KHÔNG có** component "In báo cáo" / nút In ở bất kỳ dòng nào của SCR-IX-01. Vậy app hiện (không có nút In) đúng SRS hiện tại.
- **Điểm quan trọng cho BA:** trên UI, khi bấm **Xuất PDF**, hệ thống mở hộp thoại tiêu đề **"Tùy chọn in báo cáo PDF"** — cho chọn Khổ giấy (A4 / A3 / Letter) + Hướng giấy (Dọc / Ngang) → tạo file PDF in được. Tức bản chất "in báo cáo" mà đối tác cần **đã được đáp ứng qua nút Xuất PDF** (tạo PDF theo tùy chọn in, người dùng in từ file PDF).

**Citation**

- `srs-v3.5/srs-fr-11-bao-cao.md:1042` (toolbar — Tiêu đề trang + Nút Làm mới)
- `srs-v3.5/srs-fr-11-bao-cao.md:1047-1049` (action-bar — Xem báo cáo / Xuất Excel / Xuất PDF; KHÔNG có nút In)
- `srs-v3.5/srs-fr-11-bao-cao.md:1037-1054` (toàn bảng §Thành phần màn hình SCR-IX-01 — không có component In báo cáo)

**Kết quả verify UI hiện tại**

- Verify ngày 21/07/2026 qua Chrome DevTools MCP, tài khoản `cbnv_tw_02` (CB Nghiệp vụ - Trung ương, Toàn quốc), kỳ Năm 2026.
- Với mỗi loại báo cáo: chọn loại BC → Kỳ Năm → Xem báo cáo (ra dữ liệu) → liệt kê toàn bộ nút toolbar bằng `evaluate_script` + chụp full-res. **Cả 6 báo cáo đều chỉ có 4 nút: Làm mới, Xem báo cáo, Xuất Excel, Xuất PDF** (+ nút toggle "Ẩn biểu đồ"). Query text toàn trang không có chuỗi "in báo cáo" trên toolbar.

| Mã TC | Báo cáo | Dữ liệu khi Xem BC | Toolbar quan sát được | Có nút "In báo cáo"? | Evidence |
|---|---|---|---|:-:|---|
| `SLHDVM_08` | Số lượng hỏi đáp | Tổng hỏi đáp 11 | Làm mới · Xem báo cáo · Xuất Excel · Xuất PDF | KHÔNG | `../../reverify-audit/SLHDVM_08/SLHDVM_08-toolbar.png` |
| `VVDTN_08` | VV đã tiếp nhận | Tổng vụ việc 14 | Làm mới · Xem báo cáo · Xuất Excel · Xuất PDF | KHÔNG | `../../reverify-audit/VVDTN_08/VVDTN_08-toolbar.png` |
| `VVDHT_08` | VV đang hỗ trợ | Tổng vụ việc 7 | Làm mới · Xem báo cáo · Xuất Excel · Xuất PDF | KHÔNG | `../../reverify-audit/VVDHT_08/VVDHT_08-toolbar.png` |
| `VVDHTHT_08` | VV đã hoàn thành | Tổng vụ việc 5 | Làm mới · Xem báo cáo · Xuất Excel · Xuất PDF | KHÔNG | `../../reverify-audit/VVDHTHT_08/VVDHTHT_08-toolbar.png` |
| `VVTTG_07` | VV theo thời gian | Tổng vụ việc toàn kỳ 6 | Làm mới · Xem báo cáo · Xuất Excel · Xuất PDF | KHÔNG | `../../reverify-audit/VVTTG_07/VVTTG_07-toolbar.png` |
| `CLDTBDDDR_08` | Lớp ĐT đang diễn ra | Tổng số 1 | Làm mới · Xem báo cáo · Xuất Excel · Xuất PDF | KHÔNG | `../../reverify-audit/CLDTBDDDR_08/CLDTBDDDR_08-toolbar.png` |

- **Kiểm tra bổ sung nút Xuất PDF (CLDTBDDDR_08):** bấm Xuất PDF → mở hộp thoại **"Tùy chọn in báo cáo PDF"** (Khổ giấy A4/A3/Letter, Hướng Dọc/Ngang) → bấm "Xuất file" → `POST /api/v1/bao-cao/export` trả **200**, toast "Đang tạo file...", tạo PDF thành công (không lỗi trên env test).
  - Evidence: `../../reverify-audit/CLDTBDDDR_08/export-pdf-toast.png` (hộp thoại "Tùy chọn in báo cáo PDF") · `../../reverify-audit/CLDTBDDDR_08/export-pdf-result.png` (sau khi xuất, 200).

**Kết luận QA**

- Cả 6 case: actual đối tác **đúng thực tế** (màn Báo cáo thống kê không có nút "In báo cáo" riêng), nhưng đây là bất đồng về **đặc tả** — SRS SCR-IX-01 không quy định nút In. App hiện đúng SRS → **không phải bug (không Open)**, cũng **không Reject** (đối tác quan sát đúng, chỉ khác kỳ vọng spec).
- Chức năng in báo cáo mà đối tác cần thực chất **đã có phần đáp ứng** qua nút **Xuất PDF** — hộp thoại này được đặt tên "Tùy chọn in báo cáo PDF", tạo PDF theo khổ giấy/hướng giấy để in.
- Khác biệt còn lại so với kỳ vọng đối tác: đối tác muốn nút "In báo cáo" mở thẳng hộp thoại in của trình duyệt (in trực tiếp), còn app đang đi qua bước tạo file PDF rồi người dùng in từ file.

**Nội dung đề xuất BA phản hồi đối tác**

Đề nghị BA chốt cho cụm 6 case (`SLHDVM_08`, `VVDTN_08`, `VVDHT_08`, `VVDHTHT_08`, `VVTTG_07`, `CLDTBDDDR_08`):

1. Màn Báo cáo thống kê (SCR-IX-01) hiện **không có nút "In báo cáo" riêng** — đúng theo SRS v3.5 (SRS chỉ quy định Làm mới / Xem báo cáo / Xuất Excel / Xuất PDF). Có **bổ sung** một nút "In báo cáo" (mở xem trước + hộp thoại in trình duyệt) như kỳ vọng đối tác không, hay coi chức năng **Xuất PDF** (đã có hộp thoại "Tùy chọn in báo cáo PDF") là đủ đáp ứng nhu cầu in?
   - Nếu BA coi Xuất PDF là đủ → cập nhật expected 6 case (bỏ yêu cầu nút In riêng); verdict `Không phải bug theo SRS`. Hướng dẫn đối tác: bấm **Xuất PDF** → chọn khổ giấy/hướng → in từ file PDF.
   - Nếu BA muốn bổ sung nút "In báo cáo" in trực tiếp → gửi Dev FE bổ sung + cập nhật SRS SCR-IX-01; verdict `Vẫn lỗi — owner: Dev FE`.
- Verdict QA đề xuất hiện tại: `Cần BA xác nhận` (đã ghi Google Sheet cả 6 dòng: `BA confirm`), chưa gửi Dev tới khi BA chốt.

---

> **Ghi chú ngoài phạm vi (postmortem #3):** Ảnh bằng chứng đối tác (env `htpldn-uat.ospgroup.vn`) ở 4/6 case có toast đỏ "Không thể tạo file xuất. Vui lòng thử lại." khi thao tác xuất file. Verify lại trên env test (`18.143.165.120.nip.io`): Xuất PDF `POST /api/v1/bao-cao/export` trả **200**, tạo file thành công — lỗi export **KHÔNG tái hiện**. Do 2 env cho kết quả khác nhau (candidate không tái hiện trên env test) nên **chưa log thành bug**; nếu lỗi export còn xảy ra trên env đối tác thì có thể là sự cố env/tạm thời của môi trường đó, đề nghị đối tác thử lại + báo lại nếu vẫn lỗi.
