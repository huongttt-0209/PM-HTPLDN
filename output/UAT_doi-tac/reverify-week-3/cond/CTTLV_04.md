# Bảng đối chiếu điều kiện — CTTLV_04 (row 272)

**Case:** BC Chương trình theo lĩnh vực (FR-IX-22 / UC145) — đối tác phản ánh "Dữ liệu hiển thị 'Không xác định'".
**Verdict:** BA confirm — hiện tượng "Không xác định" TÁI HIỆN đúng (chương trình không gán lĩnh vực), nhưng SRS mâu thuẫn + im lặng về cách xử lý → BA chốt.
**Verify:** 22/07/2026, Chrome DevTools MCP, tài khoản `cbnv_tw` (CB Nghiệp vụ - Trung ương / CB_NV_TW, phạm vi Toàn quốc), kỳ Năm 2026.

> **Điều kiện đối tác (đọc full-res `partner-evidence/CTTLV_04.jpg`):** đối tác mở BC Chương trình theo lĩnh vực, thấy biểu đồ + bảng có nhóm **"Không xác định"** và cho rằng đây là dữ liệu hiển thị SAI.

| Điều kiện có thể đổi kết quả | Đối tác (từ evidence full-res CTTLV_04.jpg) | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | Đăng nhập admin (QTHT), xem báo cáo CT theo lĩnh vực (báo cáo read-only) | `cbnv_tw` (CB Nghiệp vụ - Trung ương, Toàn quốc) — dùng đúng vai trò nghiệp vụ (KHÔNG dùng admin ra verdict, Nguyên tắc 3); báo cáo là hiển thị/gom nhóm độc lập vai trò, cùng phạm vi Toàn quốc | Không |
| Entity + trạng thái | Chương trình HTPLDN được báo cáo đếm trong kỳ | Chương trình đã duyệt/đếm trong kỳ Năm 2026 — cùng trạng thái vào báo cáo | Không |
| Dữ liệu tiền đề: lĩnh vực của chương trình | Các chương trình trong kỳ KHÔNG có lĩnh vực → biểu đồ chỉ nhóm "Không xác định" | Test CẢ HAI nhánh: (a) 3 chương trình KHÔNG lĩnh vực → gom "Không xác định"=3 (đúng như đối tác thấy); (b) 1 chương trình CÓ lĩnh vực "Thương mại" → nhóm "Thương mại"=1. API trả `linhVucId=null,tenLinhVuc="Không xác định"` cho nhóm chưa gán, trả tên đúng khi có gán | Không |
| Input / filter | Kỳ Năm 2026, Toàn quốc, không lọc lĩnh vực | Kỳ Năm 2026, Toàn quốc, không lọc lĩnh vực — trùng khớp | Không |

**Kết luận: 0 GAP điều kiện.** Đã tái hiện đúng điều kiện đối tác (chương trình không lĩnh vực → "Không xác định") VÀ nhánh đối chứng (có lĩnh vực → tên đúng). Hiện tượng "Không xác định" **TÁI HIỆN** — đối tác quan sát ĐÚNG thực tế; đây KHÔNG phải bất đồng về THỰC TẾ (→ không Reject). Tranh chấp nằm ở ĐẶC TẢ: (1) SRS FR-IX-22 (dòng 961, 981-982) yêu cầu báo cáo gom "theo lĩnh vực" nhưng entity CHUONG_TRINH_HTPL (data model dòng 1323-1334) + form tạo CT (FR-XI-01 dòng 129-137) **KHÔNG có trường lĩnh vực** → theo SRS chương trình không thể gán lĩnh vực → mọi CT rơi vào "Không xác định"; (2) SRS **im lặng** về cách xử lý CT chưa gán lĩnh vực (bucket "Không xác định" / ẩn / bắt buộc gán). Mâu thuẫn nội bộ SRS + SRS silent → **BA confirm**.

**Evidence:**
- `reverify-audit/CTTLV_04/cttlv-report-live-chart-table-2buckets.png` — biểu đồ + bảng 2 nhóm: "Không xác định"=3, "Thương mại"=1 (Số DN=0).
- `reverify-audit/CTTLV_04/cttlv-report-live-2buckets-2026-07-22.png` — header báo cáo (Năm 2026, Toàn quốc, Tổng chương trình=4).
- API `GET /api/v1/bao-cao/ct-theo-linh-vuc?kyBaoCao=NAM&...` → 200: `data:[{linhVucId:null,tenLinhVuc:"Không xác định",soCt:3},{linhVucId:"bbbb...",tenLinhVuc:"Thương mại",soCt:1}]`.
