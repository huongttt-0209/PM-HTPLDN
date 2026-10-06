# Re-verify NHSYC_02 — 2026-07-31, env UAT đối tác

**Env:** https://htpldn-uat.ospgroup.vn (build HTPLDN · V1.0.3) · MailHog https://htpldn-uat.ospgroup.vn/mailhog/
**Tài khoản:** `cbnv_tw` / Test@1234 — CB Nghiệp vụ Trung ương (CB_NV_TW), đơn vị BTP · TW — trùng vai trò đối tác log.
**Màn:** `/vu-viec/tao-moi` — "Thêm mới Hồ sơ Vụ việc" (vào bằng Vụ việc HTPL → nút [Nhập thủ công]).
**SRS đối chiếu:** `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/` (bản đã dọn theo BA chốt 16/07/2026).

---

## 1. Ý chính của case — BUG-NHSYC_02 (thiếu "Ngày tiếp nhận"): ✅ ĐÃ FIX

Nhóm 4 "Thông tin Tiếp nhận" nay có **3 trường**, đọc trực tiếp từ DOM:

| Trường | Bắt buộc | Kiểu | Giá trị lúc mở form |
|---|:-:|---|---|
| Kênh tiếp nhận | ✓ | dropdown | "Trực tiếp" (mặc định) |
| **Ngày tiếp nhận** | **✓** | **ô chọn ngày** | **31/07/2026 (= hôm nay), sửa được** |
| Người tiếp nhận | — | ô khóa, tự điền | "Cán bộ NV Trung ương" |

→ Khớp SRS `srs-fr-05-vu-viec.md` dòng 1697 / 1698 / 1699 (SCR-V.I-02 rows 18-20).

## 2. Đối chiếu lại 8 ý đối tác nêu

| # | Ý đối tác | Thực tế 31/07 | Trạng thái |
|---|---|---|---|
| 1 | Nhóm 1 Thông tin DN không giống thiết kế | 0 ô nhập, chỉ nút [Tìm doanh nghiệp]. Chọn DN → thẻ chỉ-đọc "Công ty TNHH Mẫu Test · MST: 0101234567 · Mã: DN-XX-0005" + nút [Bỏ chọn]. MST chưa có → hộp thoại **"Tạo doanh nghiệp mới" đúng 2 trường bắt buộc** (Tên DN + Mã số thuế) | ✅ Đúng SRS dòng 1683-1685 (BA chốt 30/05) |
| 2 | Loại hình hỗ trợ: thiết kế 4, hệ thống 6 | Nay **8 giá trị**: Tư vấn pháp luật, Tham gia tố tụng, Đại diện ngoài tố tụng, Hòa giải, Đào tạo/bồi dưỡng, Trợ giúp khác, Văn bản trả lời UBND, Văn bản tư vấn mạng lưới TVV. Nạp từ `/api/v1/danh-muc/tree?loaiDanhMuc=LOAI_HINH_HO_TRO` | ⚠️ Chờ BA ban hành danh mục chuẩn (không phải lỗi code — danh mục cấu hình được) |
| 3 | Lĩnh vực pháp lý: thiết kế 8, hệ thống 7, thiếu "Khác" | **10 giá trị**, vẫn không có "Khác". Nạp từ `/api/v1/danh-muc/tree?loaiDanhMuc=LINH_VUC_PL` | ⚠️ Chờ BA chốt có "Khác" hay không |
| 4 | Nội dung vụ việc / vướng mắc nên gộp 1 trường | Vẫn 2 trường riêng: "Nội dung yêu cầu" + "Vướng mắc" | ✅ Đúng SRS dòng 1688 + 1691 (kỳ vọng đối tác trái SRS) |
| 5 | Thiếu "Thời điểm phát sinh" | Không có | ⚠️ BA: đưa vào yêu cầu cải tiến nếu có nhu cầu thật |
| 6 | Nhóm 3 thiếu "Hướng dẫn hồ sơ cần nộp" | Không có | ⚠️ BA: yêu cầu chưa rõ, cần làm rõ trước |
| 7 | **Nhóm 4 thiếu "Ngày tiếp nhận"** | **Đã có** (xem §1) | ✅ **FIXED** |
| 8 | Thiếu "Ghi chú tiếp nhận"; Kênh tiếp nhận sai thiết kế | Không thêm "Ghi chú tiếp nhận" (đã có "Ghi chú" ở nhóm 2). Kênh tiếp nhận = **đúng 3 giá trị**: Trực tiếp / Điện thoại / Bưu chính | ✅ Đúng SRS dòng 1697 (BA chốt 16/07 bỏ DVC + Hệ thống khác) |

## 3. Xác nhận thêm — 2 bug cùng màn cũng đã fix

- **BUG-NHSYC_05**: ô "Nội dung yêu cầu" nay `maxlength=10000`, bộ đếm hiện "0 / 10000" (trước là 50000). ✅
- **BUG-NHSYC_06**: chú thích vùng tải tệp "Tối đa 10 tệp… 20MB/tệp, **tổng 100MB**" + thanh "Tổng dung lượng 0 B / 100MB". ✅

## 4. 🔴 Ba lỗi MỚI phát hiện trong lúc verify (chưa từng log)

### 4.1 [Major] Thang "Độ ưu tiên" hiển thị đảo ngược so với đặc tả

- **Trên form:** `1 — Rất cao` · `2 — Cao` · `3 — Trung bình (mặc định BR-CALC-04)` · `4 — Thấp` · `5 — Rất thấp`.
- **SRS `srs-fr-05-vu-viec.md` dòng 1524-1528** (bảng nhãn mức ưu tiên): `1 → Thấp` · `2 → Thấp` · `3 → Bình thường` · `4 → Cao` · `5 → Khẩn cấp`.
- **SRS dòng 196 + 341 (BR-CALC-07)** tính điểm theo phép **cộng**: DN nữ làm chủ +3, nhiều lao động nữ +2, ≥30% lao động khuyết tật +2, FIFO +1; *"Tối thiểu `uu_tien=1` (FIFO) cho mọi VV"* → **điểm càng cao = càng ưu tiên**.
- **SRS dòng 737 (FR-V.I-09):** *"Sắp xếp: ưu tiên DN giảm dần"*.
- **Kiểm bằng phương pháp thứ 2 (API + màn khác):** `GET /api/v1/vu-viecs/d72ca300-…` trả `uuTien: 5` cho `VV-STP-AG-20260709-001`; màn Chi tiết vụ việc in **"Ưu tiên: Rất thấp"**.
- **Hệ quả nghiệp vụ:** doanh nghiệp thuộc diện ưu tiên NĐ55 Điều 4 (điểm cao nhất) bị gắn nhãn "Rất thấp"; ngược lại cán bộ muốn đánh dấu vụ việc gấp sẽ chọn "1 — Rất cao" nhưng giá trị lưu là 1 = điểm thấp nhất → vụ việc xếp cuối hàng đợi gợi ý phân công.
- Ảnh: `../../bug-reports/image/NHSYC_02-thang-do-uu-tien-dao-nguoc.png` · `../../bug-reports/image/NHSYC_02-chitiet-uutien5-hien-rat-thap.png`
- *Lưu ý công bằng:* SRS dòng 1522 ghi nhãn chữ là "đề xuất, cần CĐT xác nhận". Nhưng **chiều của thang** thì không phải đề xuất — nó suy ra từ luật cộng điểm BR-CALC-07 và quy tắc sắp xếp giảm dần, nên phần đảo chiều vẫn là sai lệch thật.

### 4.2 [Minor] Nhãn người dùng lộ mã quy tắc nội bộ, lại là mã đã bị khai tử

- Nhãn hiển thị cho cán bộ: `3 — Trung bình (mặc định BR-CALC-04)`.
- `BR-CALC-04` đã được đổi thành `BR-CALC-07` trong `srs-fr-05` từ v3.5 — `CHANGELOG-v3-to-v3.5.md` dòng 37: *"BR-CALC-04 ID collision: đổi mã ở srs-fr-05 thành BR-CALC-07"*.
- Cùng nhóm: placeholder ô "Lý do ưu tiên" = *"Bắt buộc khi override mức ưu tiên khác mặc định"* — lẫn tiếng Anh, trái ràng buộc C-05 (`srs-v3.5.md` dòng 515: "Giao diện tiếng Việt") và I18N-07 (dòng 4641).
- *Lưu ý công bằng:* chính SRS dòng 362 (ERR-NH-05) cũng viết "override" → nên dọn câu chữ ở cả đặc tả lẫn giao diện, không quy hết cho dev.

### 4.3 [Minor] Dropdown ≥10 lựa chọn không tìm được khi gõ không dấu

- `srs-v3.5.md` dòng 6686 — quy ước **H5, mức BẮT BUỘC**: *"Mọi dropdown có ≥10 lựa chọn phải hỗ trợ tìm kiếm bằng cách gõ (autocomplete) với so khớp tương đối (chứa chuỗi, không phân biệt hoa thường, **hỗ trợ bỏ dấu tiếng Việt**)"*.
- "Lĩnh vực pháp luật" có **đúng 10 lựa chọn** → thuộc phạm vi H5.
- Thực đo: gõ `Đất` → lọc ra "Đất đai" ✅ · gõ `lao` → lọc ra "Lao động" ✅ (không phân biệt hoa thường đạt) · gõ `dat` (không dấu) → **0 kết quả** ❌.

## 5. Đã loại trừ — KHÔNG phải bug

- **"Form tự xóa dữ liệu đã nhập":** quan sát thấy 2 lần dữ liệu nhóm 1 biến mất. Truy nguyên: phiên đăng nhập bị hết hạn → SPA vẽ lại màn, **không phải** form tự reset. Kiểm chủ động: chọn DN → mở lại hộp thoại → đóng bằng [X] và bằng [Hủy] của hộp thoại "Tạo DN mới" → lựa chọn DN **vẫn giữ nguyên** (`doanhNghiepId` không đổi). Không log.
- Console sạch trong suốt phiên (chỉ 1 cảnh báo router không liên quan).

## 6. Quan sát env (chưa đủ để log)

Phiên bị đăng xuất sau ~7 phút thao tác liên tục, dù JWT khai `idleTtl: 1800` (30 phút) và `exp` còn rất xa. Chưa cô lập được nguyên nhân (có thể do gọi API bằng script trong trang). Nêu để theo dõi, chưa log thành bug.
