# Audit QLTKND_27 — Nút "Đặt lại mật khẩu" (màn Quản lý tài khoản, SCR-VIII-03)

- **Verdict:** BA confirm (row 171, P171, 2026-07-21).
- **Tài khoản:** admin (QTHT). Env https://18.143.165.120.nip.io. Màn `/quan-tri/tai-khoan`, 27 TK thật.

## Cổng 1 — Evidence đối tác
- KQ thực tế đối tác: màn hình không hiển thị nút "Đặt lại mật khẩu".
- KQ mong đợi đối tác: nút hiện khi TK Đang hoạt động / Tạm khóa.

## Cổng 2 — Tái hiện (web, data thật, cả 2 trạng thái)
Action theo trạng thái (DOM thực, `td:last-child`):
| Trạng thái | Account ví dụ | Nút hành động | Có "Đặt lại mật khẩu"? |
|---|---|---|:-:|
| Hoạt động | qa_tvv_dp_r18, cbpd_hn, cbnv_hn (≥14) | Sửa · Phân quyền · **Khóa TK · Vô hiệu hóa** | KHÔNG |
| Tạm khóa | cbpd_bn | Sửa · Phân quyền · **Mở khóa** | KHÔNG |
| Chờ kích hoạt | qa_tvv_tw_r19 | **Gửi lại email kích hoạt** | KHÔNG |
| Vô hiệu hóa | qa_tvv_pheduyet_c | Khôi phục | KHÔNG |

- `anyResetButtonAnywhere = false`. Ảnh `web-hanh-dong-active-no-reset.png`.
- ⇒ Xác nhận đúng: không nút "Đặt lại mật khẩu" ở bất kỳ trạng thái nào (kể cả 2 trạng thái đối tác nêu).

## Cổng 3 — SRS đối chiếu (v3.5)
| Nguồn SRS | Nội dung | Kết luận |
|---|---|---|
| SCR-VIII-03 cột Hành động (`srs-fr-10-quan-tri.md:1660`) | "[STT80 UAT 2026-06-02] Bỏ 'Đổi MK' — admin không đặt/đổi mật khẩu user; reset MK qua 'Gửi lại email kích hoạt'" | Nút reset MK bị BỎ có chủ đích |
| FR-VIII-15 §Inputs (`:695`, `:703`) | [STT80] admin KHÔNG đặt mật khẩu; user tự đặt qua link kích hoạt | không có thao tác đặt MK của admin |
| FR-VIII-26 (`:1260`+) | reset/đặt lại mật khẩu = luồng tự phục vụ "Quên mật khẩu" của user | reset MK không phải nút admin trên list |

## Vì sao BA confirm (không Open, không Reject)
- Không **Open**: app KHÔNG hiện nút = ĐÚNG SRS v3.5 (STT80 bỏ nút). Session prompt giả định "SRS: hiện khi Active/Tạm khóa" là theo spec CŨ (trước STT80) — 3-Step Verify (check SRS version) cho thấy v3.5 đã bỏ.
- Không **Reject**: quan sát "không có nút" của đối tác TÁI HIỆN đúng; chỉ tranh chấp expected/spec (đối tác kỳ vọng nút tồn tại).
- ⇒ evidence đúng actual, tranh chấp expected/spec → **BA confirm** (QA_VERIFY_PROTOCOL dòng 80).

## Kết luận
- **BA confirm** — kỳ vọng đối tác dựa trên spec cũ; nút "Đặt lại mật khẩu"/"Đổi MK" đã được BA bỏ 2026-06-02 (STT80), reset MK nay qua "Gửi lại email kích hoạt" (TK chờ kích hoạt) + tự phục vụ "Quên mật khẩu" (FR-VIII-26). Log §QLTKND_27 trong ../../ba-confirm/qtht/ba-confirmation-needed-qtht-batch8.md.
