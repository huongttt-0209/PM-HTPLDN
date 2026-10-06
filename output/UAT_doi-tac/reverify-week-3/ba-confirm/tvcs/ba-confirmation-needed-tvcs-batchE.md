# BA confirmation needed — TVCS Batch E (Tư liệu PL — QLTLPLCVV, tab SCR-X1-02) — 2026-07-21

> Gom các testcase Batch E mà QA **không tự chốt verdict được** (SRS tự mâu thuẫn / không quy định) hoặc cần BA phản hồi đối tác. Case Open có SRS reference rõ (QLTLPLCVV_08) đã log riêng ở `../../bug-reports/tvcs/Pass-bug-report-tvcs-batchE.md`.
>
> Verify 21/07/2026 qua Chrome DevTools MCP, tài khoản `cbnv_tw_05` / `CB_NV_TW` (CB NV có CRUD đầy đủ tư liệu — SRS dòng 806/812). SRS trích từ `input/srs-update-2026-5-5/srs-fr-12-tv-chuyen-sau.md` (v3.5), số dòng mở file verify trực tiếp.

---

## QLTLPLCVV_02 — Bảng tư liệu thiếu cột "Ngày tạo" / "Người tạo" (Dạng B — SRS tự mâu thuẫn)

**Bối cảnh testcase**

- Dòng Excel: 294, mã TC `QLTLPLCVV_02`.
- Nội dung kiểm tra: CB NV mở tab "Tư liệu PL liên kết" trong Chi tiết TVCS → xem cột bảng danh sách tư liệu.
- Expected trong file UAT (đối tác): bảng tư liệu **thiếu cột "Ngày tạo" và "Người tạo"**.

**Kết quả verify UI hiện tại**

- Mở accordion "Tư liệu pháp luật" trong Chi tiết TVCS (`/tv-chuyen-sau/{id}`).
- Bảng hiển thị **7 cột**: `Tên tư liệu | Loại | Lĩnh vực | File | Trạng thái | Công khai lúc | Hành động` (đọc `<thead>` trực tiếp, cố định trên cả record TIEP_NHAN và DA_DUYET).
- **Không có** cột "Ngày tạo", "Người tạo" → khớp phản ánh đối tác. Có cột "Công khai lúc" (thời gian công khai) thay vì "Ngày tạo".
- Evidence: `../../reverify-audit/QLTLPLCVV_02/tvcs-batchE-02-cot-bang-tu-lieu.png`

**Điểm mâu thuẫn trong SRS v3.5**

1. Theo mục **Outputs (FR-X.1-06)**, danh sách tư liệu phải có `nguoi_tao` + `ngay_tao` (đều "luôn"):
   - #8 `nguoi_tao | text | luôn`
   - #9 `ngay_tao | datetime | luôn | dd/mm/yyyy HH:mm`

   Citation:
   - `input/srs-update-2026-5-5/srs-fr-12-tv-chuyen-sau.md:937`
   - `input/srs-update-2026-5-5/srs-fr-12-tv-chuyen-sau.md:938`

2. Nhưng mục **Thành phần màn hình SCR-X1-02** lại mô tả bảng tư liệu chỉ gồm `Tên / Loại / Trạng thái / Số file / Hành động` — KHÔNG có "Ngày tạo"/"Người tạo" (và cũng không có "Lĩnh vực"/"Công khai lúc" mà UI đang thêm):
   - "Bảng tư liệu: Tên / Loại / Trạng thái / Số file / Hành động. Nút [+ Thêm tư liệu]"

   Citation:
   - `input/srs-update-2026-5-5/srs-fr-12-tv-chuyen-sau.md:1144`

**Câu hỏi cần BA xác nhận**

Bảng danh sách tư liệu (tab "Tư liệu PL liên kết") phải gồm những cột nào? Đang có 2 nguồn SRS mâu thuẫn:

1. **Hướng 1 — theo Outputs (937/938):** phải bổ sung cột "Người tạo" + "Ngày tạo (dd/mm/yyyy HH:mm)" → UI hiện **thiếu 2 cột** (là lỗi).
2. **Hướng 2 — theo Thành phần màn hình (1144):** bảng không cần 2 cột này → UI hiện **không phải lỗi** (thậm chí đã có thêm Lĩnh vực + Công khai lúc).

**Đề xuất QA tạm thời**

- Chưa gửi bug này cho Dev cho tới khi BA chốt source truth (Outputs vs Thành phần màn hình).
- Tạm verdict `QLTLPLCVV_02`: **Cần BA xác nhận**.
- Nếu BA chọn hướng 1: UI `Vẫn lỗi` (thiếu cột Người tạo/Ngày tạo), owner `Dev FE` (+ Dev BE nếu API chưa trả 2 field).
- Nếu BA chọn hướng 2: UI **không phải lỗi**, cập nhật lại expected của TC cho khớp; đối tác nên bỏ kỳ vọng 2 cột này.

---

## QLTLPLCVV_03 — Nút "Thêm tư liệu" hiện khi TVCS "Đã duyệt"/"Hủy" (Dạng B — SRS không quy định gating theo state)

**Bối cảnh testcase**

- Dòng Excel: 295, mã TC `QLTLPLCVV_03`.
- Nội dung kiểm tra: CB NV mở tab Tư liệu của TVCS ở các trạng thái khác nhau → nút **[+ Thêm tư liệu]** có hiện không.
- Expected trong file UAT (đối tác): nút "Thêm mới" **chỉ hiện khi TVCS ở Tiếp nhận / Đã phân công / Đang tư vấn / Hoàn thành / Chờ phê duyệt**; phải **ẩn khi TVCS "Đã duyệt" và "Hủy"**.

**Kết quả verify UI hiện tại**

- TVCS **TIEP_NHAN** (baseline): [+ Thêm tư liệu] hiện + enable.
- TVCS **DA_DUYET** (record `5eed0008`): nút **hiện, enable**; bấm vào **mở được form "Thêm tư liệu pháp luật"** đủ field enable + nút [Thêm mới] enable (không seed thêm).
- TVCS **HUY** (record `758383f6`, seed→huy): nút **hiện, enable**; banner record "Nội dung tư vấn đã bị hủy".
- → Nút [+ Thêm tư liệu] hiện ở **mọi state** (kể cả DA_DUYET + HUY) → khớp phản ánh đối tác.
- Evidence: `../../reverify-audit/QLTLPLCVV_03/tvcs-batchE-03-nut-them-tu-lieu-tren-TVCS-DADUYET.png` + `...-HUY.png`

**Điểm mâu thuẫn trong SRS v3.5**

1. Theo **Thành phần màn hình SCR-X1-02**, nút [+ Thêm tư liệu] "**luôn hiển thị**" (không gate theo state TVCS):
   - "Nút [+ Thêm tư liệu] (inline trong tab này)" — cột điều kiện hiển thị = "luôn hiển thị".

   Citation:
   - `input/srs-update-2026-5-5/srs-fr-12-tv-chuyen-sau.md:1144`
   - `input/srs-update-2026-5-5/srs-fr-12-tv-chuyen-sau.md:1156` (Tư liệu PL: "CRUD tư liệu inline" — không nêu gate theo state TVCS)

2. Nhưng **Quy tắc tương tác** lại giới hạn mode sửa (nếu áp cho cả CRUD tư liệu) chỉ 2 state:
   - "Mode sửa chỉ khi trạng thái IN (TIEP_NHAN, DANG_TU_VAN)"

   Citation:
   - `input/srs-update-2026-5-5/srs-fr-12-tv-chuyen-sau.md:1152`

**Câu hỏi cần BA xác nhận**

Thao tác **Thêm/CRUD tư liệu PL** có bị chặn theo trạng thái TVCS không, và nếu có thì cho phép ở những state nào?

1. **Hướng 1 — theo 1144 (luôn hiển thị):** nút Thêm hiện ở mọi state → UI hiện **đúng SRS**, kỳ vọng đối tác (ẩn ở DA_DUYET/HUY) **không có cơ sở SRS**.
2. **Hướng 2 — theo 1152 (chỉ TIEP_NHAN/DANG_TU_VAN):** nút Thêm chỉ nên hiện ở 2 state → UI hiện **sai** (thừa ở PHAN_CONG/HOAN_THANH/CHO_PHE_DUYET/DA_DUYET/HUY), đồng thời kỳ vọng đối tác (5 state) **cũng lệch** (thừa PHAN_CONG/HOAN_THANH/CHO_PHE_DUYET).

> Lưu ý: kỳ vọng đối tác (hiện 5 state, ẩn DA_DUYET+HUY) **không khớp** cả hướng 1 lẫn hướng 2. Về nghiệp vụ, thêm tư liệu vào TVCS đã **Hủy**/đã **Duyệt** (chốt) có thể không hợp lý — nhưng SRS 1144 lại nói "luôn hiển thị".

**Đề xuất QA tạm thời**

- Chưa gửi Dev tới khi BA chốt: CRUD tư liệu có gate theo state TVCS không + state nào được phép.
- Tạm verdict `QLTLPLCVV_03`: **Cần BA xác nhận**.
- Nếu BA chọn hướng 1: UI **không phải lỗi** (đúng 1144); cập nhật expected TC.
- Nếu BA chọn hướng 2 (hoặc rule mới theo đối tác): UI `Vẫn lỗi` (không gate), owner `Dev FE` (+ BE chặn API create khi state chốt); cần định nghĩa rõ danh sách state cho phép.

---

## QLTLPLCVV_07 — Nút "Sửa" hiện + cho sửa (mô tả/file) trên tư liệu "Đã công khai" (Dạng A — app diverge SRS 888 có chủ đích)

**Bối cảnh testcase**

- Dòng Excel: 296, mã TC `QLTLPLCVV_07`.
- Nội dung kiểm tra: CB NV xem tư liệu ở trạng thái **CONG_KHAI ("Đã công khai")** → nút **[Sửa]** có hiện + bấm được không.
- Expected trong file UAT (đối tác): nút "Sửa" **chỉ nên hiện khi tư liệu "Nháp"**; hiện trên "Công khai" là sai.
- Actual đối tác ghi: nút "Sửa" vẫn hiện với tư liệu "Công khai".

**Đối chiếu SRS v3.5**

- SRS quy định về **hành động sửa** (không nói ẩn nút): khi tư liệu CONG_KHAI → **từ chối sửa, phải hủy công khai trước** (chặn toàn bộ chỉnh sửa).
- Bước cập nhật field (ten/loai/linh_vuc/mo_ta) chỉ chạy khi KHÔNG bị từ chối ở bước kiểm trạng thái → SRS = chặn **mọi** field khi CONG_KHAI, không có carve-out cho mô tả/file.

**Citation**

- `input/srs-update-2026-5-5/srs-fr-12-tv-chuyen-sau.md:888` (step 3: CONG_KHAI → từ chối sửa, phải hủy công khai trước)
- `input/srs-update-2026-5-5/srs-fr-12-tv-chuyen-sau.md:890` (step 5: cập nhật ten_tu_lieu, loai_tu_lieu, linh_vuc_id, mo_ta — chỉ khi qua được step 3)

**Kết quả verify UI hiện tại**

- Tài khoản `cbnv_tw_05` / `CB_NV_TW`, tư liệu `90268a74` trạng thái **CONG_KHAI ("Đã công khai")**.
- Nút **[Sửa] hiện + enable** trên tư liệu CONG_KHAI (khớp đối tác). (Nút [Xóa] cùng hàng thì bị disable — xem mục "bất thường".)
- Bấm [Sửa] → modal "Sửa tư liệu pháp luật" mở, banner cam "Tư liệu đã công khai — chỉ được cập nhật mô tả và file đính kèm". Field Tên/Loại/Lĩnh vực **khóa (disabled)**; File đính kèm **enable**; [Lưu] **enable**. (Mô tả hiển thị disabled trong form dù banner nói được sửa — nhưng API vẫn nhận cập nhật mô tả, xem dưới.)
- **Điểm chốt — hệ thống CHO SỬA THẬT tư liệu công khai:**
  - FE bấm [Lưu] (payload gồm cả field khóa) → `PATCH /tu-lieu-phap-ly-vvs/90268a74` trả **400** `ERR-STATE-X1-06-01` "Tư liệu đã công khai, chỉ cho phép cập nhật: moTa, fileDinhKemIds".
  - Test chốt bằng API chỉ gửi field cho phép: `PATCH {"moTa":"...","version":3}` → **200 success**, `moTa` đổi thật, `version` 3→4, `trangThai` vẫn **CONG_KHAI**. (Đã khôi phục mô tả gốc sau test.)
- → App **không** "từ chối sửa hoàn toàn" như SRS 888; mà thực thi 1 rule khác **có chủ đích**: cho cập nhật `moTa` + `fileDinhKemIds` trên tư liệu CONG_KHAI, chỉ khóa các field lõi (có mã lỗi riêng `ERR-STATE-X1-06-01` liệt kê rõ field được phép).
- Evidence: `../../reverify-audit/QLTLPLCVV_07/tvcs-batchE-07-modal-sua-mo-tren-tu-lieu-cong-khai.png` (modal mở) + `...-luu-400-err-state.png` (toast 400 khi kèm field khóa).

**Kết luận QA**

- Về **nút hiện**: SRS 888 không yêu cầu ẩn nút [Sửa] khi CONG_KHAI (chỉ chặn hành động) → riêng việc nút hiện chưa đủ để kết luận lỗi; kỳ vọng "ẩn nút" của đối tác là ý muốn UX, không có trong SRS.
- Về **hành động**: đây là điểm quan trọng — app **cho sửa thật** (mô tả + file) tư liệu CONG_KHAI (đã verify 200, persist), trong khi SRS 888 nói phải **từ chối sửa, hủy công khai trước**. Đây là **xung đột spec-vs-implementation có chủ đích** (dev cố ý cho phép sửa mô tả/file khi công khai), không phải app quên enforce → QA không tự chốt "SRS 888 thắng" được, cần BA quyết.

**Nội dung đề xuất BA phản hồi đối tác**

Đề nghị BA xác nhận hướng xử lý:

- Quy tắc chuẩn cho tư liệu **đã công khai**: (a) chặn sửa **toàn bộ** (theo SRS 888, phải hủy công khai trước) hay (b) cho sửa **mô tả + file đính kèm**, chỉ khóa field lõi (theo hành vi app hiện tại `ERR-STATE-X1-06-01`)?
- Nút [Sửa] trên tư liệu công khai nên **ẩn** (ý đối tác) hay **hiện-nhưng-hạn-chế** (app hiện tại)?
- Verdict QA đề xuất: **Cần BA xác nhận**. Chưa gửi Dev tới khi chốt:
  - Nếu BA chọn (a) SRS 888: app `Vẫn lỗi` (đang cho sửa mô tả/file khi công khai), owner `Dev BE` (chặn PATCH khi CONG_KHAI) + `Dev FE` (ẩn/khóa nút Sửa).
  - Nếu BA chọn (b) rule app: **không phải lỗi**; cập nhật SRS 888 + expected TC (nút hiện-nhưng-hạn-chế là đúng), riêng nút [Sửa] có thể vẫn cân nhắc UX theo ý đối tác.
