# Bảng đối chiếu điều kiện — PDHSTVV_09

**Evidence đã xem:** `partner-evidence/PDHSTVV_09.webm` → frames `reverify-audit/PDHSTVV_09/frames/`
- f001-f008: đối tác (CB_NV_TW) thẩm định hồ sơ "TTV TKM Test 1" (TVV-BTP-TW-0056) → kết luận ĐẠT → trình duyệt.
- f013-f018: đăng nhập CB_PD_TW → mở hồ sơ (Chờ phê duyệt) → hộp thoại "Xác nhận phê duyệt" → nhập số quyết định **`QĐ-123/QĐ-BTP`** — **TRÙNG** với số QĐ đã dùng cho hồ sơ TVV-BTP-TW-0055 trước đó (case PDHSTVV_06).
- f019-f020 — **frame chứa LỖI**: toast **"Phê duyệt TVV thành công"**, hồ sơ chuyển **"Chờ kích hoạt tài khoản"**, thẻ Hồ sơ hiển thị "Số quyết định: QĐ-123/QĐ-BTP" ⇒ hệ thống **chấp nhận số QĐ trùng**, không báo lỗi.

**Đối tác phản ánh cụ thể:** nhập **trùng** số quyết định công nhận (đã tồn tại trên hồ sơ khác) mà hệ thống vẫn báo thành công, thay vì hiển thị thông báo lỗi.

| Điều kiện có thể đổi kết quả | Đối tác (từ evidence, full-res) | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | Cán bộ PD Trung ương (CB_PD_TW) | cbpd_tw (CB_PD_TW) | Không |
| Entity + trạng thái (state machine) | TVV "TTV TKM Test 1" (TVV-BTP-TW-0056) cấp TW, **Chờ phê duyệt**; đã tồn tại hồ sơ khác (TVV-BTP-TW-0055) mang số QĐ `QĐ-123/QĐ-BTP` | TVV-BTP-TW-0008 "QA TVV PheDuyet W2 C" cấp TW, **Chờ phê duyệt**; đã tồn tại hồ sơ khác **TVV-BTP-TW-0006** mang đúng số QĐ `QĐ-123/QĐ-BTP` (duyệt ở case PDHSTVV_06 cùng phiên) | Không |
| Input / giá trị nhập | Số quyết định **`QĐ-123/QĐ-BTP`** (trùng) | Số quyết định **`QĐ-123/QĐ-BTP`** (trùng, y hệt) | Không |

**Kết quả verify trên web (cbpd_tw):**
- Bấm "Phê duyệt" với số QĐ trùng → toast **"Phê duyệt TVV thành công"**; `.ant-form-item-explain-error` **rỗng**; hồ sơ chuyển **"Chờ kích hoạt tài khoản"**, Ngày công nhận 12/07/2026.
- Sau thao tác, **2 hồ sơ khác nhau cùng mang 1 số quyết định**:
  - `TVV-BTP-TW-0006` (QA TVV PheDuyet W2 A) — `soQuyetDinh: "QĐ-123/QĐ-BTP"`, CHO_KICH_HOAT
  - `TVV-BTP-TW-0008` (QA TVV PheDuyet W2 C) — `soQuyetDinh: "QĐ-123/QĐ-BTP"`, CHO_KICH_HOAT
- → **TÁI HIỆN** đúng như đối tác (hệ thống không chặn số QĐ trùng).

**Đối chiếu SRS v3.5 (`srs-fr-04-chuyen-gia-tvv.md`) — SRS IM LẶNG:**
- Entity TU_VAN_VIEN, thuộc tính `so_quyet_dinh_cong_nhan` (dòng 2025): *"text | N | **Format QĐ-{số}/QĐ-{đơn_vị}**"* — **KHÔNG có ràng buộc UNIQUE**.
- Đối chiếu: SRS ghi UNIQUE rất rõ ở các trường khác — `ma_tvv` (dòng 2006: "UNIQUE"), `cmnd_cccd` (dòng 138: "unique toàn hệ thống" + lỗi ERR-TVV-02 "Số Căn cước công dân đã tồn tại"), `email` (dòng 296 + ERR-DK-09 "Email này đã được sử dụng bởi tư vấn viên khác").
- FR-IV-07 §Error Handling (dòng 611-615) chỉ có **ERR-PD-02** (khác đơn vị), **ERR-PD-03** (thiếu lý do từ chối), **ERR-PD-04** (khóa lạc quan), **ERR-PD-05** (thiếu số QĐ) — **KHÔNG có mã lỗi nào cho số QĐ trùng**.
- ⇒ SRS **không quy định** số quyết định công nhận phải duy nhất, cũng không có thông báo lỗi tương ứng. Không có căn cứ SRS để kết luận web sai.
- Ghi chú nghiệp vụ: trên thực tế **1 quyết định công nhận có thể công nhận nhiều tư vấn viên cùng lúc** (danh sách kèm theo QĐ) — nếu ép duy nhất thì luồng này sẽ bị chặn sai. Cần BA cân nhắc trước khi chốt.

**Verdict:** `BA confirm` (đối tác quan sát ĐÚNG thực tế — web nhận số QĐ trùng; nhưng kỳ vọng "phải báo lỗi" KHÔNG có trong SRS → bất đồng về ĐẶC TẢ, để BA chốt. QA không tự Reject).
