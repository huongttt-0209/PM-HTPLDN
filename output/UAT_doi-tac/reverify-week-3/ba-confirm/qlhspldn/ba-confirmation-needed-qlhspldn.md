# BA confirmation needed — Quản lý hồ sơ pháp lý doanh nghiệp (QLHSPLDN) — Tuần 3 — 2026-07-21

> **File này để làm gì:** gom các ý con của QLHSPLDN_02 / QLHSPLDN_03 mà QA **không tự chốt Open/Reject được** vì kỳ vọng đối tác **vượt/khác SRS** (SRS không quy định). Các ý con **Open** (thiếu trường/cột có SRS reference rõ) nằm ở [../../bug-reports/qlhspldn/Pass-bug-report-qlhspldn.md) — KHÔNG lặp ở đây.

> **SRS dùng để chấm:** `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-12-tv-chuyen-sau.md` — **FR-X.1-04 (UC150)**. Màn cũ SCR-X1-03 DEPRECATED v2.1 → tab "Hồ sơ pháp lý" trong MH-07.2 chi tiết DN.

> **Môi trường verify:** `https://18.143.165.120.nip.io` — Chrome DevTools MCP — tài khoản `cbnv_hn`/CB_NV_DP (Sở Tư pháp Hà Nội), DN DN-HNI-0001, seed hồ sơ HSPL-20260721-0001. Ngày verify: 21/07/2026.

> **Bối cảnh chung:** Bằng chứng đối tác gửi là **tài liệu thiết kế của đối tác** (`HTPLDN-PTYC-CT-v2.0.docx` §4.12.4 "PM12.TVCS.HSPL — Quản lý hồ sơ pháp lý doanh nghiệp"), liệt kê các cột/trường đối tác kỳ vọng. Một số cột/trường trong tài liệu này **KHÔNG có trong SRS v3.5 §Inputs/§Outputs** → cần BA chốt có bổ sung spec không.

| Case | Dòng Excel | Ý con | Verdict | Câu hỏi gốc |
|------|:---------:|---|:-------:|-------------|
| QLHSPLDN_02 | 292 | Bảng danh sách **thừa cột "Số/Ký hiệu"** | BA confirm | Cột "Số/Ký hiệu" không có trong SRS §Outputs — giữ hay bỏ? |
| QLHSPLDN_02 | 292 | Bảng danh sách **thiếu "Lĩnh vực pháp lý"** | BA confirm | Đối tác kỳ vọng có cột này (thiết kế), SRS §Outputs không liệt kê — có bổ sung không? |
| QLHSPLDN_02 | 292 | Bảng danh sách **thiếu "Nguồn"** | BA confirm | Đối tác kỳ vọng cột "Nguồn" (Thủ công / Cổng PLQG), SRS §Outputs không liệt kê — có bổ sung không? |
| QLHSPLDN_03 | 293 | Biểu mẫu **thừa trường "Số/Ký hiệu"** | BA confirm | Trường "Số/Ký hiệu" không có trong SRS §Inputs — giữ hay bỏ? |
| QLHSPLDN_03 | 293 | Biểu mẫu **"Mô tả" hiển thị dưới nhãn "Ghi chú"** | BA confirm | `mo_ta` (dòng 560, nhãn "Mô tả") đang là nhãn "Ghi chú" — có phải cùng trường? Đổi nhãn? |

> Các ý con **Open** (không thuộc file này, xem bug-report): danh sách thiếu cột "Có tệp đính kèm" (co_file, §Outputs dòng 654); biểu mẫu thiếu "Lĩnh vực pháp lý" (linh_vuc_id, §Inputs dòng 556) + "Tệp đính kèm" (file_dinh_kem, §Inputs dòng 562).

---

## QLHSPLDN_02 — Bảng danh sách: thừa "Số/Ký hiệu", thiếu "Lĩnh vực pháp lý" & "Nguồn"

**Bối cảnh testcase**

- Dòng Excel 292, mã TC `QLHSPLDN_02`. Đối tác phản ánh bảng danh sách hồ sơ pháp lý **thiếu "Lĩnh vực pháp lý", "Nguồn", "Có tệp đính kèm"** và **thừa "Số/Ký hiệu"**.
- Kỳ vọng đối tác lấy từ tài liệu thiết kế `HTPLDN-PTYC-CT-v2.0.docx §4.12.4.2.1 "Mô tả thông tin trên màn hình"` — liệt kê 10 cột: Mã hồ sơ, Tên hồ sơ, Loại hồ sơ, **Lĩnh vực pháp lý**, Ngày cấp, Ngày hết hạn, Cơ quan cấp, Trạng thái, **Có tệp đính kèm**, **Nguồn**.

**Đối chiếu SRS v3.5 (FR-X.1-04 §Outputs, dòng 642-656)**

SRS §Outputs liệt kê: `id, ma_ho_so, ten_ho_so, ten_doanh_nghiep, loai_ho_so, ngay_cap, ngay_het_han, trang_thai, co_file (dòng 654), ngay_tao, total_count`.

- **"Có tệp đính kèm" (co_file)** → CÓ trong SRS dòng 654 → đã kết luận **Open** (xem bug-report).
- **"Lĩnh vực pháp lý"** → **KHÔNG** có trong SRS §Outputs.
- **"Nguồn"** → **KHÔNG** có trong SRS §Outputs.
- **"Số/Ký hiệu"** → **KHÔNG** có trong SRS §Outputs (cũng không có trong §Inputs).

**Citation**

- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-12-tv-chuyen-sau.md:642-656` (§Outputs — danh sách trường đầu ra)

**Kết quả verify UI hiện tại**

- Bảng danh sách có 8 cột (đọc `<thead>` qua DOM): `Mã hồ sơ · Tên hồ sơ · Loại · Số/Ký hiệu · Ngày cấp · Ngày hết hạn · Trạng thái · Hành động`.
- Có cột **"Số/Ký hiệu"** (đối tác báo thừa) — đúng, không có trong SRS §Outputs.
- Không có cột "Lĩnh vực pháp lý", "Nguồn" (đối tác báo thiếu) — đúng, cũng không có trong SRS §Outputs.
- Evidence: `bug-reports/image/BUG-QLHSPLDN_02-list-header-with-data.png`

**Câu hỏi cho BA**

1. Cột **"Số/Ký hiệu"** đang hiển thị trên bảng nhưng SRS §Outputs không quy định → **giữ (bổ sung vào spec) hay bỏ**?
2. Đối tác kỳ vọng bảng có cột **"Lĩnh vực pháp lý"** và **"Nguồn"** (theo tài liệu thiết kế đối tác), nhưng SRS §Outputs không liệt kê → **có bổ sung 2 cột này vào spec + web không**? (Riêng "Nguồn" gắn với cơ chế Thủ công / Cổng PLQG — cần chốt luôn nguồn dữ liệu.)

---

## QLHSPLDN_03 — Biểu mẫu Thêm/Sửa: thừa "Số/Ký hiệu", "Mô tả" hiển thị dưới nhãn "Ghi chú"

**Bối cảnh testcase**

- Dòng Excel 293, mã TC `QLHSPLDN_03`. Đối tác phản ánh biểu mẫu thêm mới **thiếu "Lĩnh vực pháp lý", "Mô tả", "Tệp đính kèm"** và **thừa "Số/Ký hiệu"**.

**Đối chiếu SRS v3.5 (FR-X.1-04 §Inputs, dòng 548-562)**

SRS §Inputs (Thêm mới/Chỉnh sửa): `ma_ho_so (auto), doanh_nghiep_id, ten_ho_so, loai_ho_so, linh_vuc_id (556), ngay_cap, ngay_het_han, co_quan_cap, mo_ta (560), trang_thai, file_dinh_kem (562)`. **KHÔNG** có trường "Số/Ký hiệu".

- **"Lĩnh vực pháp lý" (linh_vuc_id, 556)** + **"Tệp đính kèm" (file_dinh_kem, 562)** → CÓ trong SRS → đã kết luận **Open** (xem bug-report).
- **"Mô tả" (mo_ta, 560)** → CÓ trong SRS, nhãn "Mô tả". Web hiển thị trường tự do dạng long-text dưới nhãn **"Ghi chú"**.
- **"Số/Ký hiệu"** → **KHÔNG** có trong SRS §Inputs.

**Citation**

- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-12-tv-chuyen-sau.md:548-562` (§Inputs — Thêm mới/Chỉnh sửa)

**Kết quả verify UI hiện tại**

- Biểu mẫu có các trường (đọc label qua DOM): `Tên hồ sơ*, Loại hồ sơ*, Số/Ký hiệu, Ngày cấp, Ngày hết hạn, Cơ quan cấp, Trạng thái, Ghi chú`.
- Có trường **"Số/Ký hiệu"** (đối tác báo thừa) — đúng, không có trong SRS §Inputs.
- Có trường **"Ghi chú"** (long-text) — nhiều khả năng ứng với `mo_ta` (nhãn SRS là "Mô tả") nhưng khác nhãn.
- Evidence: `bug-reports/image/BUG-QLHSPLDN_03-form-them-moi.png`, `...-bottom.png`

**Câu hỏi cho BA**

1. Trường **"Số/Ký hiệu"** trên biểu mẫu không có trong SRS §Inputs → **giữ (bổ sung spec) hay bỏ**?
2. Trường **"Ghi chú"** (long-text) trên biểu mẫu có phải chính là `mo_ta` ("Mô tả", dòng 560) không? Nếu đúng → **đổi nhãn về "Mô tả"** cho khớp SRS, hay chấp nhận nhãn "Ghi chú"? (Đối tác đang hiểu là "thiếu Mô tả" vì không thấy đúng nhãn.)

---

*BA confirmation file generated: 2026-07-21 17:35:17 | QA Automation via Claude Code*
