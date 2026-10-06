# Bảng đối chiếu điều kiện — re-verify PDHSTVV_08 (row 75)

Bug gốc: CB Phê duyệt từ chối hồ sơ TVV kèm lý do → chủ hồ sơ KHÔNG nhận thông báo/mail kèm lý do
(trong khi nhánh phê duyệt cùng phiên vẫn gửi mail). Re-test 2026-07-15: từ chối hồ sơ "Chờ phê duyệt"
→ kiểm hộp thư chủ hồ sơ trên MailHog (UI browser).

| Điều kiện | Bug gốc (bước tái hiện) | Mình test | GAP? |
|---|---|---|---|
| Vai trò/tài khoản thực hiện từ chối | CB Phê duyệt (`cbpd_tw` — CB_PD_TW) từ chối hồ sơ TVV cùng đơn vị | CB Phê duyệt (`cbpd_dp` — CB_PD_DP An Giang) từ chối hồ sơ TVV cùng đơn vị — cùng là "CB Phê duyệt" thực hiện đúng thao tác Từ chối; hồ sơ "Chờ phê duyệt" hiện có đều thuộc đơn vị Địa phương nên `cbpd_tw` không có thẩm quyền (không có nút Từ chối), `cbpd_dp` là officer đúng đơn vị; hook gửi mail chủ hồ sơ độc lập cấp officer | Không |
| Trạng thái hồ sơ TVV khi từ chối | Hồ sơ ở "Chờ phê duyệt" (có nút Từ chối) | Hồ sơ TVV-STP-AG-0002 ở "Chờ phê duyệt" → Từ chối → chuyển "Từ chối" | Không |
| Lý do từ chối (input) | Lý do hợp lệ ≥10 ký tự (bug gốc 98 ký tự) | Lý do hợp lệ 161 ký tự | Không |
| Kênh kiểm thông báo chủ hồ sơ | Hộp thư MailHog của chủ hồ sơ bị từ chối | Hộp thư MailHog của `qa.tvv.rv18.dp@htpldn.test` (chủ hồ sơ TVV-STP-AG-0002) | Không |
