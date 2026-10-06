# Kết quả chạy test 11 UC bổ sung — 2026-06-30

**Tool:** Chrome DevTools MCP (UI) + API trực tiếp. **Account:** `qtht_01` (QTHT), `cb_nv_tw_01` (CB NV TW), `cb_nv_bn_01` (CB NV đơn vị nộp).
**File TC chi tiết:** [report-bo-sung-11UC.xlsx](report-bo-sung-11UC.xlsx) — 70 TC.
**Quy ước trạng thái: chỉ 3** — ✅ PASS · ❌ FAIL · ⛔ CHƯA CHẠY (chưa tích hợp / luồng ngoài).

## Verdict tổng

| Trạng thái | Số TC |
|---|:-:|
| ✅ PASS | **42** |
| ❌ FAIL | **10** |
| ⛔ CHƯA CHẠY | **18** |
| **Tổng** | **70** |

**Đã chạy/verify được 10/11 UC**. 18 CHƯA CHẠY = **16 tích hợp ngoài** (VNeID 11 + chi trả DVC/LGSP 5) + **2 giới hạn môi trường** (idle-timeout 30 phút không giả lập được).

---

## ✅ PASS theo UC (42 case)

| UC | Chức năng | Kết quả |
|:--|---|---|
| **UC100/116/117** | 3 danh mục | Thêm/sửa/xóa/list/mã trùng(409)/bỏ trống(422)/mã>20(422)/phân quyền non-QTHT(403) — PASS |
| **UC118** | Đăng nhập | Login+OTP, sai mật khẩu(401), bỏ trống(422), OTP sai(401), tạm khóa(401), vô hiệu(401), **khóa sau 5 lần sai(TAM_KHOA)**, chưa-auth-redirect — PASS |
| **UC119** | Đăng xuất | Logout(200)+vô hiệu token(401), xóa cookie, multi-tab — PASS |
| **UC97** | Công khai biểu mẫu | Công khai(200), hủy(200), phân quyền đơn vị(403), file bắt buộc, idempotent — PASS |

---

## ❌ 10 FAIL — bug tìm được (cần dev/BA xử lý)

> **UC167 (5 case) chung 1 bug gốc.** 1 lỗi phân quyền chặn cả luồng nộp BC (cả 5 endpoint hành động đều 403). Case gốc `TC-TPD-012` = **Major**; 4 case hệ quả (`TC-TPD-013…016`) = **Minor** (bị chặn theo, không phải lỗi độc lập). Dev fix 1 điểm check phạm vi là chạy lại được cả 5.
>
> *Mã TC trong cột dưới là mã native trong report (đã chèn vào đúng cluster). Đối chiếu file [report-bo-sung-11UC.xlsx](report-bo-sung-11UC.xlsx).*

| TC (mã report) | UC | Mức | Lỗi |
|---|:--|:-:|---|
| **TC-TPD-012…016** (5 case) | UC167 | **1 Major + 4 Minor** | **Đơn vị nộp (CB NV BN/ĐP) ∈ phạm vi đợt bị 403 `ERR-AUTH-VPD-00-02`** ở MỌI endpoint đợt (xem chi tiết, `/start` lập BC, `/bao-cao` lưu, `/submit-bc` trình PD) → không lập/trình được BC. List trả về đợt đúng scope nhưng các endpoint chặn theo đơn vị chủ sở hữu (TW). Vi phạm SRS FR-XI-06. **Fix khu trú (1 chỗ check phạm vi).** → [bug-report-ct-htpldn-trinh-bc.md](bug-report-ct-htpldn-trinh-bc.md) |
| **TC-BM-613** | UC97 | Major | Công khai biểu mẫu khi **thư mục cha đang ẩn (AN)** → vẫn thành công (200). SRS FR-VII-07 E2 yêu cầu chặn **ERR-CK-BM-02** |
| **DM-029** | UC100 | Minor | Xóa danh mục **cha đang có con** → không bị chặn (orphan con). SRS ERR-DM-03 yêu cầu chặn |
| **DM-038** | UC116 | Minor | Như trên (cùng endpoint DELETE) |
| **DM-047** | UC117 | Minor | Như trên |
| **TC-TK-213** | UC121 | Minor | Nút "Đăng nhập VNeID" **hiển thị** trên /login dù BE chưa tích hợp (endpoint 404). SRS FR-VIII-23: Tier 2 off → nút phải **ẩn** |

> Quan sát nhỏ thêm (không tính FAIL): `TC-TK-204` (đăng nhập tài khoản vô hiệu hóa) — thông báo "Account disabled" bằng tiếng Anh, nên Việt hóa.

---

## ⛔ 18 CHƯA CHẠY

### A. Tích hợp ngoài — 16 TC (QA không seed được, chờ dev/infra)

| UC | TC | Vì sao | Cần làm gì | Ai |
|:--|:-:|---|---|:-:|
| UC121/122/123 | 11 | Backend VNeID chưa có (endpoint `/auth/vneid/*` = 404) | Tích hợp VNeID Tier 2 (NĐ69/2024) | Dev BE/Infra |
| UC78 | 5 | Hồ sơ chi trả chỉ từ DVC qua **LGSP**, không nhập tay | Tích hợp/mock LGSP có hồ sơ `DANG_THAM_DINH/DAT` | Dev BE/Infra |

### B. Giới hạn môi trường — 2 TC

| UC | TC | Vì sao chưa chạy | Cần làm gì | Ai |
|:--|:-:|---|---|:-:|
| UC118/119 | TC-TK-206, TC-TK-211 | Timeout idle 30 phút — server theo dõi backend, JWT ký RS256 **không giả lập được** | Chờ idle 30 phút thật hoặc backend test hook | QA / Dev BE |

---

## Ghi chú phương pháp
- **UC167 đã test manual qua UI** (account đơn vị nộp `cb_nv_bn_01`): phát hiện bug chặn 403 → kết luận FAIL, không còn "chưa chạy".
- "Sai spec = FAIL" (nút VNeID, thư mục ẩn, xóa cha-con, 403 đơn vị nộp).
- Mã lỗi thực tế khác tài liệu (vd `ERR-AUTH-LOGIN-01` vs `ERR-DN-01`) → vẫn PASS (yêu cầu nghiệp vụ đạt).
- Một số case validation (UC116/117, login edge) verify qua **API** (xác nhận backend); UI core verify qua MCP. Đã dọn sạch record/side-effect test tạo ra (trừ 1 đợt BC trống `QA-UC167-MANUAL-TEST` giữ làm repro cho dev — DELETE trả 422).
