# Bảng đối chiếu điều kiện — PDNDCHTV_07 (row 22) — Duyệt hàng loạt: cán bộ tạo không nhận được thông báo

**Kết luận:** Open (Major) — cùng nguyên nhân gốc với PDNDCHTV_01.

- Phần **duyệt hàng loạt chạy đúng**: chọn 2 dòng → 1 lần gọi máy chủ → cả 2 bản ghi thành `DA_DUYET`. Không có nút từ chối hàng loạt (đúng `:537`).
- Phần **thông báo không chạy**: 2 câu hỏi được duyệt, cán bộ tạo nhận **0 thông báo**.
- Căn cứ chấm Open: `:537` (dòng "Duyet hang loat") **không nhắc lại** cụm "TB CB NV", nhưng nó chỉ mô tả hành vi của nút (có modal xác nhận, không từ chối hàng loạt) chứ **không định nghĩa lại hành động Duyệt**. Hành động Duyệt được định nghĩa ở `:536` = *"SET DA_DUYET + hieu_luc=1 + TB CB NV"*. Duyệt hàng loạt tạo ra **đúng cùng một chuyển trạng thái** `CHO_DUYET → DA_DUYET` cho N bản ghi ⇒ áp dụng cùng yêu cầu thông báo. Đã ghi rõ căn cứ này trong note để đối tác/BA phản biện được nếu không đồng ý.

| Điều kiện có thể đổi kết quả | Đối tác (evidence `partner-evidence/PDNDCHTV_07.webm`, frame t018/t030/t042) | Mình test (env nip.io, 27/07/2026 12:53) | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | Người duyệt `CB_PD_TW` — "Cán bộ PD Trung ương", BTP · TW. Người kiểm thông báo `CB_NV_TW` | Người duyệt `cbpd_tw` (CB Phê duyệt - Trung ương, BTP · TW); người kiểm thông báo `cbnv_tw` (CB Nghiệp vụ - Trung ương, BTP · TW) — TRÙNG KHỚP | Không |
| Entity + trạng thái (state machine) | Nhiều bản ghi ở tab "Chờ duyệt", tích chọn hàng loạt rồi bấm Duyệt | 2 bản ghi `QA-20260727-0003` + `QA-20260727-0004`, cả 2 ở `CHO_DUYET`, tích chọn cả 2 → bấm [Duyệt hàng loạt] → cả 2 thành `DA_DUYET`, `ngayDuyet = 2026-07-27T05:53:24` — TRÙNG KHỚP | Không |
| Dữ liệu tiền đề | Các câu hỏi do cán bộ nghiệp vụ tạo | Cả 2 câu hỏi có `nguoiTaoId` = chính tài khoản `cbnv_tw` dùng để kiểm thông báo (xác minh `GET /api/v1/auth/me`). Cùng một người tạo cả 2 ⇒ nếu hệ thống gửi thông báo thì phải thấy ít nhất 1, thực tế 0 | Không |
| Input / filter / giá trị nhập | Tích ô chọn nhiều dòng rồi bấm duyệt hàng loạt, xác nhận modal | Tích 2 ô chọn → nút [Duyệt hàng loạt] hiện ra → bấm → modal "Bạn xác nhận phê duyệt 2 câu hỏi đã chọn?" → [Duyệt]. Đo bằng bộ bắt thông báo dùng chung (tự kiểm `soObserverDangSong = 1`) | Không |

## Artifact real-data (Gate bằng chứng — loại claim: Hành vi + Dữ liệu)

- `bug-reports/image/BUG-PD-07-duyet-hang-loat-truoc-khi-bam.png` — đã mở đọc: 2 dòng `QA-20260727-0003` và `QA-20260727-0004` đã tích chọn, thanh công cụ hiện **"Đã chọn 2 câu hỏi"** kèm nút **[Duyệt hàng loạt]**, và **không có** nút từ chối hàng loạt.
- `bug-reports/image/BUG-PD-THONG-BAO-can-bo-tao-khong-nhan.png` — đã mở đọc: khung Thông báo của `CB_NV_TW` sau cả 3 thao tác vẫn không có mục nào về câu hỏi được duyệt; mục mới nhất "11 phút trước" (05:43), thao tác hàng loạt lúc 05:53.
- Đo bằng bộ bắt thông báo: `SO_REQUEST = 1` (`POST /api/v1/kho-cau-hois/approve-bulk`), `SO_KHUNG_THONG_BAO = 1` ("Duyệt hàng loạt thành công"), không lặp ⇒ 2 bản ghi được xử lý trong 1 lần gọi, không phải 2 lần gọi lẻ.

## Phương pháp thứ hai (bắt buộc)

- **Đếm ở tầng dữ liệu (phép thử quyết định):** thao tác duyệt hàng loạt lúc 05:53:24; đo lại `GET /api/v1/thong-baos` của `cbnv_tw` lúc 05:53:58 (chờ thêm 34 giây phòng gửi bất đồng bộ) → `total = 253` giữ nguyên so với baseline 253, **chênh lệch 0**; thông báo mới nhất vẫn `2026-07-27T05:43:25`; `unread-count = 252` không đổi; 0 bản ghi nhắc `QA-20260727-0003/0004`.
- **Đối chứng dương:** trong 253 thông báo hiện có của chính tài khoản này, `PHE_DUYET` xuất hiện đủ ở 8 entity khác (HOI_DAP 25, DANG_KY_DAO_TAO 12, VU_VIEC 4, CHUONG_TRINH_HTPL 3…), riêng `KHO_CAU_HOI` = **0**. ⇒ Không phải lỗi hạ tầng thông báo hay lỗi tài khoản.
- **Kiểm chéo kết quả duyệt để tách biệt hai vấn đề:** `GET /api/v1/kho-cau-hois/{id}` cho cả 2 mã đều trả `"trangThai": "DA_DUYET"`, `"hieuLuc": true`, `"nguoiDuyetId" = 4101cf26-…` (`cbpd_tw`). ⇒ **Nghiệp vụ duyệt hàng loạt đúng**; chỉ thiếu bước thông báo. Ghi rõ để dev không sửa nhầm phần đang chạy đúng.
- **Đối chiếu đặc tả — trích nguyên văn 2 dòng liên quan:**
  - `srs-fr-13-tv-nhanh.md:537` (dòng 11 "Duyet hang loat"): *"| 11 | content | Duyet hang loat | button | [Duyet hang loat] -> modal xac nhan. Khong tu choi hang loat | click -> action | khi >= 1 checkbox trong tab Cho duyet |"* — mô tả hành vi nút, khớp thực tế 100% (có modal xác nhận ✅, không có từ chối hàng loạt ✅).
  - `srs-fr-13-tv-nhanh.md:536` (dòng 10 "Duyet don le"): *"[Duyet] SET DA_DUYET + hieu_luc=1 + **TB CB NV**"* — định nghĩa hành động Duyệt, trong đó có nghĩa vụ thông báo.
- **Kiểm quy trình xử lý FR-X.2-01** (`srs-fr-13-tv-nhanh.md:95-163`, 7 bước): mô tả luồng phê duyệt nhưng **không tách riêng bước thông báo**, cũng không có câu nào miễn trừ thông báo cho thao tác hàng loạt. ⇒ Không có căn cứ nào trong đặc tả cho phép duyệt hàng loạt bỏ qua thông báo.
