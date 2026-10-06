# BA confirmation needed — CTTLV_04 (row 272) · BC Chương trình theo lĩnh vực — nhóm "Không xác định" — 2026-07-22

> **File này để làm gì:** testcase `CTTLV_04` (BC Chương trình theo lĩnh vực, FR-IX-22 / UC145). Đối tác phản ánh báo cáo hiển thị nhóm **"Không xác định"** và cho là dữ liệu sai. QA verify: hiện tượng **tái hiện đúng** (do chương trình chưa gán lĩnh vực) nên KHÔNG phải Reject; nhưng gốc rễ là **mâu thuẫn nội bộ SRS** (báo cáo gom theo lĩnh vực nhưng entity/form chương trình không có trường lĩnh vực) + SRS im lặng về cách xử lý CT chưa gán lĩnh vực → QA không tự chốt, cần BA quyết.
>
> **Vai trò verify:** `cbnv_tw` (CB Nghiệp vụ - Trung ương, Toàn quốc). Môi trường `https://18.143.165.120.nip.io`. Kỳ = Năm 2026, Đơn vị = Toàn quốc (trùng cấu hình đối tác).
>
> **SRS:** `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/` — `srs-fr-11-bao-cao.md` (báo cáo) + `srs-fr-15-ct-htpldn.md` (entity chương trình).
>
> **Cập nhật trạng thái:** round trước để `Reject` (lưu ở `../../reverify-audit/CTTLV_04/`); re-verify 22/07/2026 đổi thành **`BA confirm`** vì hiện tượng tái hiện + tranh chấp thuộc đặc tả.

---

## CTTLV_04 — Báo cáo "theo lĩnh vực" gom nhóm "Không xác định" vì chương trình không có trường lĩnh vực

**Bối cảnh testcase**

- Dòng Excel: **272**, mã TC `CTTLV_04` — BC Chương trình theo lĩnh vực (FR-IX-22 / UC145).
- Nội dung kiểm tra: mở Báo cáo thống kê → BC Chương trình theo lĩnh vực → Kỳ Năm 2026 → Toàn quốc → Xem báo cáo → đối chiếu biểu đồ + bảng gom theo lĩnh vực.
- Actual đối tác ghi: "Dữ liệu hiển thị 'Không xác định'" — đối tác cho rằng nhóm "Không xác định" là dữ liệu hiển thị sai.
- Expected ngầm của đối tác: hiển thị đúng tên lĩnh vực, không có nhóm "Không xác định".

**Đối chiếu SRS v3.5 — phát hiện mâu thuẫn nội bộ**

1. **Báo cáo YÊU CẦU gom theo lĩnh vực:** FR-IX-22 §Mô tả — "Báo cáo chương trình theo lĩnh vực: hàng = lĩnh vực, cột = số CT + số DN tham gia"; §Output liệt kê `linh_vuc_id` + `ten_linh_vuc` điều kiện "Luôn".
2. **NHƯNG entity chương trình KHÔNG có trường lĩnh vực:**
   - Data model `CHUONG_TRINH_HTPL` không có attribute `linh_vuc_id` (chỉ có: mã, tên, mục tiêu, đối tượng, thời gian bắt đầu/kết thúc, ngân sách, trạng thái, người/ngày phê duyệt, cờ công bố).
   - Form tạo chương trình (FR-XI-01 §Input) cũng KHÔNG có trường lĩnh vực.
   - → Theo SRS, người dùng **không có cách nào gán lĩnh vực cho chương trình** → mọi chương trình đều rơi vào nhóm "Không xác định". Đây chính là hiện tượng đối tác thấy.
3. **SRS im lặng:** FR-IX-22 không quy định cách xử lý chương trình có lĩnh vực = null (tạo nhóm "Không xác định" / ẩn / bắt buộc gán).

**Citation**

- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md:961` (FR-IX-22 §Mô tả — báo cáo theo lĩnh vực)
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md:981-982` (FR-IX-22 §Output — linh_vuc_id, ten_linh_vuc "Luôn")
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-15-ct-htpldn.md:1323-1334` (entity CHUONG_TRINH_HTPL — KHÔNG có linh_vuc_id)
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-15-ct-htpldn.md:129-137` (FR-XI-01 §Input — form tạo CT không có trường lĩnh vực)

**Kết quả verify UI hiện tại**

- Verify 22/07/2026 qua Chrome DevTools MCP, `cbnv_tw` / CB_NV_TW (Toàn quốc). URL `.../bao-cao?loai=ct-theo-linh-vuc&kyBaoCao=NAM&tuNgay=2026-01-01&denNgay=2026-12-31`.
- Seed đối chứng 2 nhánh: 3 chương trình KHÔNG gán lĩnh vực + 1 chương trình gán lĩnh vực "Thương mại" (đều đã duyệt, trong kỳ).
- Báo cáo hiển thị đúng 2 nhóm: **"Không xác định" = 3** + **"Thương mại" = 1** (Số DN tham gia = 0). Tổng chương trình = 4.
- API `GET /api/v1/bao-cao/ct-theo-linh-vuc` → 200: `data:[{"linhVucId":null,"tenLinhVuc":"Không xác định","soCt":3},{"linhVucId":"bbbbbbbb-...","tenLinhVuc":"Thương mại","soCt":1}]`.
- → Hiện tượng đối tác báo TÁI HIỆN. FE map trung thực dữ liệu BE; khi chương trình CÓ lĩnh vực thì hiển thị tên đúng, khi null thì gom "Không xác định". Không phải lỗi render/mapping.
- Evidence: `../../reverify-audit/CTTLV_04/cttlv-report-live-chart-table-2buckets.png`, `cttlv-report-live-2buckets-2026-07-22.png`.

**Kết luận QA**

- `CTTLV_04` KHÔNG phải Reject: hiện tượng "Không xác định" tái hiện đúng, đối tác quan sát chính xác.
- Cũng KHÔNG kết luận Open được: app không sai một clause SRS rõ ràng — SRS im lặng về xử lý CT chưa gán lĩnh vực, và mâu thuẫn nằm ngay trong SRS (báo cáo gom theo lĩnh vực nhưng entity chương trình không có trường lĩnh vực).
- → `Cần BA xác nhận`.

**Nội dung đề xuất BA phản hồi đối tác**

Câu hỏi cốt lõi cho BA: **Chương trình HTPLDN có cần trường "lĩnh vực" không, và báo cáo BC Chương trình theo lĩnh vực xử lý chương trình chưa gán lĩnh vực thế nào?**

- **Hướng 1 — Bổ sung trường lĩnh vực cho chương trình:** thêm `linh_vuc_id` vào entity + form tạo/sửa chương trình (FR-XI-01), quy định bắt buộc hay tùy chọn. Khi đó báo cáo FR-IX-22 mới gom theo lĩnh vực thật; cần cập nhật SRS entity + gửi Dev. (Nếu bắt buộc → nhóm "Không xác định" sẽ không còn.)
- **Hướng 2 — Giữ nhóm "Không xác định" (hiện tại):** chấp nhận báo cáo có nhóm "Không xác định" cho chương trình chưa gán lĩnh vực → cập nhật expected của `CTTLV_04` cho khớp; đồng thời làm rõ trong SRS FR-IX-22 rằng CT null lĩnh vực gom vào "Không xác định".
- **Hướng 3 — Ẩn/loại nhóm "Không xác định":** nếu BA muốn báo cáo chỉ hiển thị lĩnh vực đã gán → gửi Dev điều chỉnh; nhưng cần định nghĩa nguồn lĩnh vực cho chương trình trước (liên quan Hướng 1).
- Verdict QA đề xuất cho `CTTLV_04` (row 272): **`Cần BA xác nhận`** (mâu thuẫn + khoảng trống đặc tả giữa FR-IX-22 và entity CHUONG_TRINH_HTPL), chưa gửi Dev tới khi BA chốt.
