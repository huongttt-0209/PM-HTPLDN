# Bảng đối chiếu điều kiện — PDNDCHTV_01 (row 20) — Duyệt câu hỏi: cán bộ tạo không nhận được thông báo

**Kết luận:** Open (Major).
- 2 trong 3 yêu cầu của `:536` **chạy đúng**: trạng thái `CHO_DUYET → DA_DUYET` ✅, `hieu_luc = true` ✅.
- Yêu cầu thứ 3 — **"TB CB NV"** (thông báo cán bộ nghiệp vụ) — **KHÔNG chạy**: tổng thông báo của cán bộ tạo giữ nguyên **253 → 253** sau thao tác duyệt.
- Có **đối chứng dương** loại trừ "hệ thống thông báo hỏng nói chung": chính tài khoản này ĐANG nhận được thông báo `PHE_DUYET` từ 8 entity khác (CT HTPL, Vụ việc, Kế hoạch đánh giá…). Chỉ `KHO_CAU_HOI` là 0.

| Điều kiện có thể đổi kết quả | Đối tác (evidence `partner-evidence/PDNDCHTV_01.webm`, frame t012/t024/t036) | Mình test (env nip.io, 27/07/2026 12:47) | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | Người duyệt `CB_PD_TW` — "Cán bộ PD Trung ương", BTP · TW. Người kiểm thông báo `CB_NV_TW` — "Cán bộ NV Trung ương", BTP · TW | Người duyệt `cbpd_tw` (CB Phê duyệt - Trung ương, BTP · TW); người kiểm thông báo `cbnv_tw` (CB Nghiệp vụ - Trung ương, BTP · TW) — TRÙNG KHỚP cả 2 vai trò | Không |
| Entity + trạng thái (state machine) | Bản ghi kho câu hỏi ở tab "Chờ duyệt", nguồn Import. Sau duyệt: `QA-20260720-0005` = "Đã duyệt", Hiệu lực "Có", Ngày duyệt 20/07/2026 10:49 | Bản ghi `QA-20260727-0001` trạng thái `CHO_DUYET` → sau duyệt `DA_DUYET`, `hieuLuc = true`, `ngayDuyet = 2026-07-27T05:47:16.619Z` — TRÙNG KHỚP | Không |
| Dữ liệu tiền đề | Câu hỏi do một cán bộ nghiệp vụ tạo; tài khoản kiểm thông báo là `CB_NV_TW` | Câu hỏi có `nguoiTaoId = f2e93500-…` = **chính tài khoản `cbnv_tw` dùng để kiểm thông báo**. Đã xác minh bằng `GET /api/v1/auth/me`. Đây là điều kiện CHẶT HƠN đối tác: loại trừ khả năng "thông báo có gửi nhưng gửi cho người khác" | Không |
| Input / filter / giá trị nhập | Bấm nút Duyệt trên dòng → xác nhận modal | Bấm đúng nút Duyệt trên dòng → modal "Bạn xác nhận phê duyệt câu hỏi?" → bấm [Duyệt]. Đo bằng bộ bắt thông báo dùng chung (tự kiểm `soObserverDangSong = 1`) | Không |

## Artifact real-data (Gate bằng chứng — loại claim: Hành vi + Dữ liệu)

- `bug-reports/image/BUG-PD-01-modal-duyet-don-le.png` — đã mở đọc: modal "Duyệt câu hỏi / Bạn xác nhận phê duyệt câu hỏi?" với 2 nút [Hủy] [Duyệt].
- `bug-reports/image/BUG-PD-THONG-BAO-can-bo-tao-khong-nhan.png` — đã mở đọc: khung Thông báo của `CB_NV_TW`, 5 mục hiển thị **đều là "Tài khoản vừa đăng nhập ở nơi khác"**, mục mới nhất **"11 phút trước"** (tức 05:43) — trong khi thao tác duyệt diễn ra lúc **05:47** (7 phút trước thời điểm chụp). Không có mục nào về phê duyệt câu hỏi.
- Đo bằng bộ bắt thông báo (đã tự kiểm 1 observer): `SO_REQUEST = 1` (`POST /api/v1/kho-cau-hois/{id}/approve`), `SO_KHUNG_THONG_BAO = 1` ("Duyệt câu hỏi thành công"), không lặp.

## Phương pháp thứ hai (bắt buộc)

- **Đếm ở tầng dữ liệu, không dựa vào khung thông báo trên màn (phép thử quyết định).**
  - Baseline TRƯỚC thao tác: `GET /api/v1/thong-baos` của `cbnv_tw` → `total = 253`; quét đủ 3 trang (253/253 bản ghi) → **`entityType = KHO_CAU_HOI` xuất hiện 0 lần**.
  - SAU cả 3 thao tác (duyệt 05:47:16 · từ chối 05:49:57 · duyệt hàng loạt 05:53:24), đo lúc 05:53:58 (chờ thêm 4 giây phòng gửi bất đồng bộ): `total = 253`, **chênh lệch = 0**; thông báo mới nhất vẫn là `2026-07-27T05:43:25` (trước cả 3 thao tác); `unread-count = 252` không đổi.
  - Số bản ghi nhắc tới mã `QA-20260727-0001…0004`: **0**.
- **Đối chứng dương — loại trừ "cả hệ thống thông báo hỏng".** Trong chính 253 thông báo của tài khoản này có đủ các loại `PHE_DUYET` từ module khác: `CHUONG_TRINH_HTPL` (3), `VU_VIEC` (4), `KE_HOACH_DANH_GIA` (2), `NOI_DUNG_TU_VAN_CS` (1), `DANG_KY_DAO_TAO` (12), `HOI_DAP` (25), `KHOA_HOC` (1), `DE_XUAT_DAO_TAO` (1). ⇒ Đường ống thông báo hoạt động bình thường với tài khoản này; **chỉ riêng `KHO_CAU_HOI` không sinh thông báo nào**. Đây là bằng chứng khoanh vùng lỗi cho dev.
- **Đối chiếu đặc tả — trích nguyên văn:** `srs-fr-13-tv-nhanh.md:536` (§3 SCR-X2-01, dòng 10 "Duyet don le"): *"Tab "Cho duyet": **[Duyet] SET DA_DUYET + hieu_luc=1 + TB CB NV**. [Tu choi] modal ly do bat buoc + SET NHAP + TB CB NV"*. Hai vế đầu chạy đúng, vế "TB CB NV" không chạy.
- **Kiểm phần "bật hiệu lực mặc định" mà phiếu test nêu:** `GET /api/v1/kho-cau-hois/{id}` sau duyệt trả `"hieuLuc": true` ⇒ đúng `hieu_luc=1`. Ý này **không phải lỗi**, đã ghi rõ trong note gửi đối tác để tránh dev sửa nhầm phạm vi.
- **Kiểm phần "lưu vết thao tác":** bản ghi sau duyệt có `nguoiDuyetId = 4101cf26-…` (= `cbpd_tw`) và `ngayDuyet = 2026-07-27T05:47:16.619Z` ⇒ có lưu vết người duyệt và thời điểm. Ý này **không phải lỗi**.
