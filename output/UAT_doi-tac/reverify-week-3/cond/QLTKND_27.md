# Bảng đối chiếu điều kiện — QLTKND_27 (row 171)

**Case:** Nút "Đặt lại mật khẩu" trên màn Quản lý tài khoản (SCR-VIII-03).
**Đối tác phản ánh:** Màn hình KHÔNG hiển thị nút "Đặt lại mật khẩu" (kỳ vọng hiện khi TK Đang hoạt động / Tạm khóa).
**Loại bug:** phụ thuộc **trạng thái TK** → cần bảng đối chiếu.
**Verdict:** `BA confirm` — quan sát của đối tác (không có nút) TÁI HIỆN đúng; nhưng SRS v3.5 [STT80 UAT 2026-06-02] đã BỎ nút này → tranh chấp expected/spec.

| Điều kiện có thể đổi kết quả | Đối tác (evidence QLTKND_27.jpg) | Mình test (18.143.165.120.nip.io, 21/07) | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | QTHT ("Quản trị viên QTHT") | admin / QTHT | Không |
| Trạng thái TK (điều kiện kỳ vọng hiện nút) | Đang hoạt động **và** Tạm khóa | Đang hoạt động (qa_tvv_dp_r18, cbpd_hn, cbnv_hn… ≥14) **và** Tạm khóa (cbpd_bn) | Không |
| Nơi tìm nút | Cột "Hành động" trên danh sách | Cột "Hành động" trên danh sách (cùng view đối tác) | Không |

**0 GAP.** Đã tái hiện cả 2 trạng thái đối tác nêu (Active + Tạm khóa) — dùng account có sẵn, không cần seed.

## Kết quả test (real-data, artifact)
- Trích action theo từng trạng thái (DOM thực):
  - **Hoạt động** (qa_tvv_dp_r18): Sửa · Phân quyền · **Khóa TK · Vô hiệu hóa** — KHÔNG có "Đặt lại mật khẩu".
  - **Tạm khóa** (cbpd_bn): Sửa · Phân quyền · **Mở khóa** — KHÔNG có "Đặt lại mật khẩu".
  - Chờ kích hoạt (qa_tvv_tw_r19): **Gửi lại email kích hoạt**. Vô hiệu hóa (qa_tvv_pheduyet_c): Khôi phục.
- `anyResetButtonAnywhere = false` — không nút "Đặt lại mật khẩu"/"Đổi MK" ở bất kỳ trạng thái nào.
- Ảnh: `reverify-audit/QLTKND_27/web-hanh-dong-active-no-reset.png`. Audit: `reverify-audit/QLTKND_27/audit.md`.

## Đối chiếu SRS
- SCR-VIII-03 cột Hành động (`srs-fr-10-quan-tri.md:1660`, row 16): "Xem / Sửa / Mở khóa / Khóa / Gửi lại email kích hoạt" — **[STT80 UAT 2026-06-02] Bỏ "Đổi MK"** — admin không đặt/đổi mật khẩu user; reset MK qua "Gửi lại email kích hoạt".
- FR-VIII-15 §Inputs (`:695`, `:703`) [STT80]: admin KHÔNG đặt mật khẩu; user tự đặt qua link kích hoạt.
- FR-VIII-26 (`:1260`+): reset/đặt lại mật khẩu là luồng tự phục vụ của user ("Quên mật khẩu" ở màn đăng nhập), KHÔNG phải nút admin trên list.
- → App KHÔNG hiện nút "Đặt lại mật khẩu" = ĐÚNG SRS v3.5. Kỳ vọng của đối tác theo spec CŨ (trước STT80).

## Kết luận
`BA confirm` — Không thể **Open** (app đúng SRS v3.5, nút bị bỏ có chủ đích [STT80]); không thể **Reject** (quan sát "không có nút" của đối tác TÁI HIỆN đúng, chỉ tranh chấp expected/spec). Cần BA xác nhận: kỳ vọng của đối tác dựa trên spec cũ, nút "Đặt lại mật khẩu" đã được BA bỏ 2026-06-02 (reset qua "Gửi lại email kích hoạt" + tự phục vụ "Quên mật khẩu"). Log §QLTKND_27 trong ../ba-confirm/qtht/ba-confirmation-needed-qtht-batch8.md.
