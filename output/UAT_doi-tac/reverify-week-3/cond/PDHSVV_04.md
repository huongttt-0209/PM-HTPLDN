# Bảng đối chiếu điều kiện — PDHSVV_04

Loại bug: **giới hạn ký tự trường "Lý do" của modal Từ chối phê duyệt** — thuộc tính component (maxlength), không đổi theo dữ liệu/đơn vị, nhưng vẫn phụ thuộc role (CB PD) + state (Chờ phê duyệt) để mở được modal → điền bảng, xác nhận app thực tế trước khi kết luận.

| Điều kiện có thể đổi kết quả | Đối tác (từ evidence, full-res) | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò người thao tác | Header: **Cán bộ PD Bộ ngành · CB_PD_BN**, đơn vị BTP·BN | `cbpd_tw` — CB_PD_TW, đơn vị BTP·TW (cùng đơn vị với đơn vị tạo hồ sơ). Cùng loại vai trò Cán bộ Phê duyệt, cùng component modal | Không |
| Entity + trạng thái | Vụ việc VV-BKH-2026... ở **Chờ phê duyệt** (có nút [Phê duyệt] [Từ chối]) | Vụ việc VV-BTP-TW-20260712-001 ở **CHO_PHE_DUYET** (có nút [Phê duyệt] [Từ chối]) | Không |
| Thao tác mở modal | Bấm [Từ chối] → modal "Từ chối phê duyệt" | Bấm [Từ chối] → modal "Từ chối phê duyệt" (đúng cùng modal) | Không |
| Trường đo giới hạn | Ô "Lý do" (bắt buộc), bộ đếm hiển thị **"1 / 1000"** khi gõ 1 ký tự → tối đa 1000 | Ô "Lý do", `maxLength=1000` (đọc trực tiếp DOM), bộ đếm **"0 / 1000"**, placeholder "Nhập lý do...", hint "Tối thiểu 10 ký tự" | Không |

**Kết luận: 0 GAP về role/state/data.** App thực tế được xác nhận: modal "Từ chối phê duyệt", ô Lý do **giới hạn tối đa 1000 ký tự** (đúng như đối tác báo), tối thiểu 10 ký tự.

**GAP duy nhất còn lại là GAP PHIÊN BẢN SRS (không phải GAP test):**
- **SRS v3.5** (bản được giao chấm) — FR-V.I-13 §Inputs (`srs-fr-05-vu-viec.md:977`) ô `ly_do`: ràng buộc chỉ ghi "Bắt buộc nếu TU_CHOI", **KHÔNG nêu max**; AC (`:1008`) chỉ ghi "≥ 10 ký tự" (min). → v3.5 **không yêu cầu** max 2000.
- **SRS v4** — FR-V.I-13 §Inputs (`srs-v4/srs-fr-05-vu-viec.md:1007`) ô `ly_do`: "Bắt buộc nếu TU_CHOI; **min 10 ký tự, max 2000**, sanitize C16".
- App: max **1000**.

→ Con số "2.000" đối tác dẫn **chỉ có ở v4**, không có trong v3.5. Verdict phụ thuộc phiên bản SRS nào là chuẩn chấm → **BA confirm** (cùng câu hỏi BA-01).

Chi tiết: xem [`../reverify-audit/PDHSVV_04/audit.md`](../reverify-audit/PDHSVV_04/audit.md) + [`../ba-confirm/vu-viec/ba-confirmation-needed-vu-viec.md`](../ba-confirm/vu-viec/ba-confirmation-needed-vu-viec.md).
