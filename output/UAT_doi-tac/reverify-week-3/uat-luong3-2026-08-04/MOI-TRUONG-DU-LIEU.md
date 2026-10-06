# Recon môi trường + dữ liệu — htpldn-uat.ospgroup.vn (đo 04/08/2026 ~13:00, tài khoản admin + cbnv_tw)

Đây là kết quả **đã đo sẵn** để bạn khỏi dò lại. Vẫn phải tự kiểm chứng lại điều nào bạn dựa vào để ra verdict.

## Đăng nhập

| Tài khoản | Mật khẩu | Vai trò / loại |
|---|---|---|
| `admin` | `Secret@123` | Quản trị hệ thống (dùng để tra tài khoản, đổi trạng thái tài khoản) |
| `cbnv_tw` `cbnv_bn` `cbnv_dp` | `Test@1234` | Cán bộ nghiệp vụ TW/BN/ĐP |
| `cbpd_tw` `cbpd_bn` `cbpd_dp` | `Test@1234` | Cán bộ phê duyệt TW/BN/ĐP |
| `huongcg` | **`Secret@123`** | **Chuyên gia** (kiêm TVV), mã `TVV-BTP-TW-0030`, đơn vị Cục Bổ trợ tư pháp |
| `0151554887` | **`Secret@123`** | **Doanh nghiệp** "TKM Company" (mã `DN-HNI-0013`, email tkm@gmail.com) |

**OTP luôn là `666666`.** Thư OTP KHÔNG về MailHog — đừng chờ mail.

Tài khoản nghiệp vụ dùng `Test@1234`; tài khoản Chuyên gia / Doanh nghiệp / Người hỗ trợ trên env này dùng `Secret@123`.
Login fail → curl `POST /api/v1/auth/login` đọc `error.code`: `ERR-AUTH-LOGIN-01` = sai mật khẩu · `ERR-SYS-00-29-01` = bị chặn vì thử nhiều (đợi ~75s, ĐỪNG thử dồn).

Tra tài khoản bằng admin: `GET /api/v1/tai-khoan?page=1&limit=20&search=<từ khoá>` (tham số đúng là `search`, tổng 212 tài khoản).
Chuyên gia đang hoạt động khác: `ho_18` `mai_17` `truong_16` `ngo_15` `dinh_14` `ly_13`.
Người hỗ trợ đang hoạt động: `nhttest` `huong2nht` `huong3nht` `nht_01` `nht_02` `nht_03` `nht_04_ui` `nht_tc001_btp_tw`...

## Gọi API trong phiên trình duyệt

Token là cookie HttpOnly → **không curl bằng tay được từ ngoài phiên**. Cách đúng: `evaluate_script` gọi
`fetch('/api/v1/...', {credentials:'include'})` ngay trong tab đang đăng nhập.
(Ngoài trình duyệt, muốn curl thì tự lấy cookie: `POST /api/v1/auth/login` → `POST /api/v1/auth/verify-otp` với `{"otpToken":"...","otpCode":"666666"}` kèm `-c cookiejar`.)

## Dữ liệu có sẵn (đếm lúc 13:00, phạm vi cbnv_tw)

| Thực thể | Endpoint | Tổng | Phân bố trạng thái đáng chú ý |
|---|---|---|---|
| Tổ chức tư vấn | `/api/v1/to-chuc-tu-vans` | 10 | — |
| Hồ sơ pháp lý DN | `/api/v1/ho-so-phap-ly-dns` | 34 | — |
| Tư liệu pháp lý vụ việc | `/api/v1/tu-lieu-phap-ly-vvs` | 8 | — |
| Vụ việc | `/api/v1/vu-viecs` | 62 | — |
| Kế hoạch/đợt đánh giá | `/api/v1/ke-hoach-danh-gias` | 21 | **BAO_CAO 1** · DANG_DANH_GIA 2 · THUC_HIEN 5 · CHO_DUYET_PC 2 · LAP_KE_HOACH 3 · HOAN_THANH 7 |
| Nội dung tư vấn chuyên sâu | `/api/v1/noi-dung-tu-van-cs` | 55 | **PHAN_CONG 6** · TIEP_NHAN 10 · CHO_PHE_DUYET 2 · DA_DUYET 1 · HUY 1 |
| Thông báo (của chính mình) | `/api/v1/thong-baos` · `/api/v1/thong-baos/unread-count` | — | dùng để đếm trước/sau |

**Cơ sở dữ liệu đã mang theo dữ liệu vòng 1** (ví dụ `TVCS-20260803-0003` do `cbnv_tw` tạo ngày 03/08 vẫn còn).
Nhưng **tài khoản `qa_tvvseed28` mà vòng 1 dùng thì KHÔNG tồn tại trên env này** (`search=qa_tvvseed` → 0) — đừng đi tìm.

### Bản ghi tư vấn chuyên sâu đang ở "Phân công" (dùng cho QLNDTVVCG_24 / _26)

| Mã | Chuyên gia được phân công | Doanh nghiệp | Người tạo |
|---|---|---|---|
| `TVCS-20260803-0003` | `huongcg` (TVV-BTP-TW-0030) | TKM Company — **có tài khoản `0151554887`** | `cbnv_tw` |
| `TVCS-20260804-0005` | `huongcg` | Công ty TNHH Bình Minh AG (DN-AG-001) | (tài khoản khác) |
| `TVCS-20260804-0006..0009` | TVV-MOCK-999 (**không gắn tài khoản** → không đăng nhập được) | Công ty TNHH Bình Minh AG | — |

⇒ Case cần **đăng nhập bằng chuyên gia được phân công** thì chỉ dùng được bản ghi của `huongcg`.
⇒ Case cần kiểm **hộp thông báo của doanh nghiệp** thì phải chọn bản ghi của TKM Company (có tài khoản đăng nhập được).
⇒ Nếu 2 bản ghi này không đủ (một cho Chấp nhận, một cho Từ chối), tự dựng thêm: `cbnv_tw` tạo yêu cầu tư vấn chuyên sâu cho DN TKM Company rồi phân công `huongcg`.
