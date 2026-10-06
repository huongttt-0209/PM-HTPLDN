# Bảng đối chiếu điều kiện — PDHSTVV_02

**Evidence đã xem:** `partner-evidence/PDHSTVV_02.webm` → frames `reverify-audit/PDHSTVV_02/frames/`
- f006 (00:16, form Chỉnh sửa): mục "File thẻ hành nghề (PDF)" có tệp đã lưu **"Thẻ hành nghề.pdf"** → dữ liệu tệp TỒN TẠI.
- f009 (00:25, thẻ Hồ sơ): mục "File đính kèm" hiển thị **"Chưa có file đính kèm"** → lỗi đối tác phản ánh.
- f025 (01:13, thẻ Năng lực): trường "Bằng cấp" in chuỗi JSON thô `{"tenTruong":"Đại học Luật Hà Nội","chuyenNganh":"Luật","namTotNghiep":2000}`.
- f027 (01:19, thẻ Đánh giá): khối tổng hợp hiển thị **"—/10"** + "0.0/10" mỗi tiêu chí.

**Đối tác phản ánh cụ thể:** (a) không hiển thị tệp đính kèm dù có dữ liệu; (b) lỗi hiển thị "Bằng cấp" ở thẻ Năng lực; (c) thẻ Đánh giá dùng thang 10 thay vì thang 1–5.

| Điều kiện có thể đổi kết quả | Đối tác (từ evidence, full-res) | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | CB Phê duyệt - Trung ương (CB_PD_TW) ở f018-f027; đoạn đầu (f009) xem bằng CB Nghiệp vụ - Trung ương (CB_NV_TW) | cbpd_tw (CB_PD_TW) — chốt verdict; dùng thêm cbnv_tw chỉ để nạp tiền đề (không ra verdict) | Không |
| Entity + trạng thái (state machine) | TVV-BTP-TW-0055 "Tester TKM", trạng thái **Chờ phê duyệt**, cấp TW (BTP) | TVV-BTP-TW-0005 "QA TVV Trinh Duyet R17", trạng thái **Chờ phê duyệt**, cấp TW (BTP), URL /chuyen-gia-tvv/e6fdc062-d77d-4e45-9076-58a00b8ac068 | Không |
| Dữ liệu tiền đề | Hồ sơ CÓ tệp thẻ hành nghề ("Thẻ hành nghề.pdf") + CÓ Bằng cấp chi tiết (Đại học Luật Hà Nội / Luật / 2000) + 0 đánh giá | Đã nạp đúng tiền đề: `fileTheHanhNgheId=f7f09870-edc1-40aa-a7ee-53d02c2b406d` ("Thẻ hành nghề.pdf") + Bằng cấp chi tiết (Đại học Luật Hà Nội / Luật / 2005) + Số thẻ STHN-QA-2026/001 + 0 đánh giá | Không |

**Kết quả verify trên web (cbpd_tw):**
- (a) Thẻ Hồ sơ → "File đính kèm" = "Chưa có file đính kèm" dù máy chủ trả `fileTheHanhNgheId` khác rỗng → **TÁI HIỆN**. SRS: FR-IV-05 §Outputs #7 (srs-fr-04 dòng 468) + SCR-IV-03 thẻ Hồ sơ nhóm (e) (dòng 1554).
- (b) Thẻ Năng lực → "Bằng cấp" in `{"tenTruong":"Đại học Luật Hà Nội","chuyenNganh":"Luật","namTotNghiep":2005}` → **TÁI HIỆN**. SRS: SCR-IV-03 thẻ Năng lực (dòng 1566). Trùng gốc BUG-QLHSTVV_06.
- (c) Thẻ Đánh giá → hiển thị "—/5" + "0.0/5" (đúng thang 1–5 theo SCR-IV-03 dòng 1570-1572) → **KHÔNG tái hiện** trên env được giao.

**Verdict:** `Open` (≥1 ý Open → verdict tổng Open theo QA_VERIFY_PROTOCOL §"1 case gộp nhiều lỗi con").

---
## Re-verify 2026-07-15 (sau dev fix — vòng 2)
Vai trò CB_PD_TW `cbpd_tw` mở hồ sơ "Chờ phê duyệt" TVV-BTP-TW-0010 (có tệp đính kèm) + TVV-BTP-TW-0002 (có bằng cấp chi tiết).
- Thẻ Hồ sơ → File đính kèm: hiển thị `the-hanh-nghe-qa.pdf (349 B)` + nút Xem/Tải — KHÔNG còn "Chưa có file đính kèm". **FIXED (a).**
- Thẻ Năng lực → Bằng cấp: render "Luật Kinh tế — Đại học Luật Hà Nội — Năm tốt nghiệp 2010" (đọc được), KHÔNG còn chuỗi JSON thô. **FIXED (b)** (cùng gốc QLHSTVV_06 Closed).
⇒ PASS. Ảnh: `bug-reports/image/PDHSTVV_02-reverify-cbpd-hoso-file-hien-thi.png`, `PDHSTVV_02-reverify-nangluc-bangcap-render-sach.png`.
