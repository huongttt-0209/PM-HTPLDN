# Lỗi phát hiện thêm ngoài phạm vi — QTHT Batch 6 (21/07/2026)

Phát hiện khi verify QLVT_14 trên màn Vai trò (`/quan-tri/vai-tro`), env `18.143.165.120.nip.io`, account `admin`/QTHT.

## AN-1 — Vai trò "DN" (Doanh nghiệp) mất toàn bộ dấu tiếng Việt trong Tên + Mô tả

**Mức:** Minor (data-quality / cosmetic). Owner đề xuất: Dev BE (sửa seed VAI_TRO) hoặc DBA.

**Quan sát (2 phương pháp — C2 postmortem):**
- UI a11y snapshot: Tên vai trò = "Doanh nghiep", Mô tả = "Doanh nghiep tu dang ky, dang nhap CMS de xem vu viec cua chinh minh."
- API `GET /api/v1/vai-tro`: `{ma:"DN", ten:"Doanh nghiep", moTa:"Doanh nghiep tu dang ky, dang nhap CMS de xem vu viec cua chinh minh."}`
- Ảnh: `reverify-audit/QLVT_14/vaitro-baseline.png` (dòng DN).

**So sánh:** 10/11 vai trò còn lại có dấu đầy đủ (Cán bộ Nghiệp vụ Bộ/Ngành, Chuyên gia tư vấn, Người hỗ trợ, Quản trị hệ thống, Tư vấn viên...). Chỉ DN mất dấu.

**Kỳ vọng:** "Doanh nghiệp" + "Doanh nghiệp tự đăng ký, đăng nhập CMS để xem vụ việc của chính mình."

**Ảnh hưởng:** Tên vai trò DN hiện sai chính tả tiếng Việt ở mọi nơi dùng lại (list Vai trò, tag vai trò ở màn Tài khoản, dropdown lọc vai trò, màn phân quyền).

**Chưa log lên sheet** — chờ user xác nhận có mở dòng TC mới (`sheet_add_bug_row.py`) gửi dev hay không (thao tác ghi thêm vào sheet đối tác).
