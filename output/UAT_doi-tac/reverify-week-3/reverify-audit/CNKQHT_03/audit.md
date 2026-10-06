# Audit — CNKQHT_03 (row 11) · Nhóm 6 Kết quả hỗ trợ — bộ trường modal "Cập nhật kết quả hỗ trợ"

## Cổng 1 — Bằng chứng (ĐÓNG)

- File: `partner-evidence/CNKQHT_03.jpg` (211 KB, `fetch_evidence.py --row 11` exit 0). 1 ảnh chụp màn (không phải video).
- Frame chứa nội dung đối chiếu: chính ảnh này — modal "Cập nhật kết quả hỗ trợ" đang mở.

### 3 dữ kiện neo

| # | Dữ kiện | Giá trị đọc từ ảnh |
|---|---|---|
| (a) | URL / ID vụ việc | `htpldn-uat.ospgroup.vn/vu-viec/9ed9d021-f308-40cc-b4d7-b60b80fbc1dd` — **VV-BTP-TW-20260709-001**, tiêu đề "TKM kiểm thử chức năng...", lĩnh vực **Thuế**, ưu tiên **Trung bình**, ngày tiếp nhận 10/07/2026 |
| (b) | Trạng thái + màn đối chiếu | Vụ việc ở **Đang xử lý** (nút [Cập nhật kết quả] [Trình phê duyệt] hiện trên header), modal **"Cập nhật kết quả hỗ trợ"** đang mở với 3 trường: `* Nội dung kết quả` (đếm 0/5000), `Kết luận` ("Kết luận ngắn gọn"), `Ghi chú` ("Ghi chú thêm") — nút [Hủy] [Xác nhận]. **Không có ô đính kèm tệp** |
| (c) | Vai trò người thao tác | Header: `huongcg` · **TVV · CG** · **BTP · TW** · chuông 19 — là người được phân công |

## Cổng 2 — Hiểu bug (3 dòng)

1. **Evidence đã xem:** `CNKQHT_03.jpg` — 1 frame, modal "Cập nhật kết quả hỗ trợ" mở trên vụ việc VV-BTP-TW-20260709-001 (Đang xử lý), tài khoản huongcg (TVV·CG). Modal chỉ có 3 trường Nội dung kết quả / Kết luận / Ghi chú, đếm "0 / 5000", không có ô upload tệp.
2. **Đối tác phản ánh CỤ THỂ (cột "Kết quả thực tế"):** "Các trường thông tin không giống với thiết kế: **thiếu Tệp kết quả hỗ trợ**, **thừa trường thông tin Kết luận**, nội dung **chỉ cho phép tối đa 5000 ký tự** (SRS yêu cầu cho phép tối đa 10.000 ký tự)". → 3 ý con.
3. **Data + bước tái hiện:** login người được phân công (TVV·CG) → Vụ việc HTPL → mở vụ việc trạng thái "Đang xử lý" → bấm [Cập nhật kết quả] → đối chiếu bộ trường modal với thiết kế Nhóm 6 (FR-V.I-15).

## Cổng 3 — Đối chiếu SRS (v3.5, bản được chỉ định dùng)

| SRS yêu cầu (dẫn line) | Thực tế web | Ý con | Đủ/Thiếu |
|---|---|---|:-:|
| `srs-fr-05-vu-viec.md:1083-1085` — FR-V.I-15 §Inputs (chức năng "Cập nhật kết quả" của **người được phân công**): (2) `noi_dung_ket_qua` (Y), (3) `file_ket_qua` FILE[] "Tài liệu kết quả (văn bản TV, báo cáo)" (N), (4) `ghi_chu` (N) | Modal có Nội dung kết quả + Ghi chú, **không có** ô `file_ket_qua` (đo: 0 input file, 0 vùng upload) | Ý 1 — thiếu Tệp kết quả | ❌ **Thiếu** |
| `srs-fr-05-vu-viec.md:1721` — Accordion 6 "Kết quả Hỗ trợ" liệt kê `noi_dung_ket_qua` (người được phân công), **`file_ket_qua`**, `ket_luan_cuoi` (CB NV), `ngay_hoan_thanh` | Không có `file_ket_qua` trong modal cập nhật của người được phân công | Ý 1 — thiếu Tệp kết quả | ❌ **Thiếu** |
| `srs-fr-05-vu-viec.md:1083-1085` — FR-V.I-15 §Inputs **KHÔNG** có trường "Kết luận"; `srs-fr-05-vu-viec.md:1139` — `ket_luan_cuoi` là input của **FR-V.I-16** (chức năng của **CB NV**), và `:1721` ghi rõ `ket_luan_cuoi (CB NV)` | Modal cập nhật của người được phân công (TVV·CG) lại có thêm trường **"Kết luận"** | Ý 2 — thừa Kết luận | ❌ **Thiếu** (đúng thiết kế = không có trường này ở đây) |
| `srs-fr-05-vu-viec.md:1083` — `noi_dung_ket_qua` "Nội dung kết quả hỗ trợ" — v3.5 **KHÔNG nêu giới hạn ký tự** cho trường này | Modal giới hạn 5000 ký tự (đếm "0 / 5000") | Ý 3 — 5000 vs 10.000 | ⚠️ **Cần BA chốt phiên bản** — con số 10.000 đối tác nêu KHÔNG có trong v3.5 |

## Bảng đối chiếu điều kiện

→ [`../../cond/CNKQHT_03.md`](../../cond/CNKQHT_03.md) — **0 GAP**.

## Kết quả verify trên env được giao (https://18.143.165.120.nip.io)

Tài khoản `qa_tvvseed28` (TVV·CG, BTP·TW, người được phân công), vụ việc VV-BTP-TW cấp TW ở trạng thái **Đang xử lý**, mở modal "Cập nhật kết quả hỗ trợ".

### Phép đo bộ trường modal

```json
{"tieuDe":"Cập nhật kết quả hỗ trợ",
 "truong":[{"nhan":"Nội dung kết quả","tag":"TEXTAREA","maxLength":5000,"batBuoc":true},
           {"nhan":"Kết luận","tag":"INPUT","maxLength":500,"batBuoc":false},
           {"nhan":"Ghi chú","tag":"TEXTAREA","maxLength":1000,"batBuoc":false}],
 "coInputFile":0,"coAntUpload":0,"chuChuaTuTep":false}
```

→ Trùng đúng frame đối tác: 3 trường, đếm 0/5000, không ô đính kèm tệp.

### Kết luận từng ý con (đối chiếu v3.5)

| Ý con của đối tác | Kết luận | Căn cứ |
|---|:-:|---|
| (1) Thiếu "Tệp kết quả hỗ trợ" | **Lỗi thật (Open)** | v3.5 `:1084` liệt kê `file_ket_qua` là input của FR-V.I-15; `:1721` Accordion 6 cũng có. Modal thực tế không có ô đính kèm tệp nào |
| (2) Thừa trường "Kết luận" | **Lỗi thật (Open) theo v3.5** | FR-V.I-15 §Inputs (`:1083-1085`) chỉ gồm Nội dung kết quả / Tệp kết quả / Ghi chú — không có "Kết luận". "Kết luận cuối" (`ket_luan_cuoi`) là trường của **CB NV** ở FR-V.I-16 (`:1139`, `:1721`), không phải của người được phân công |
| (3) Nội dung chỉ tối đa 5000, "SRS yêu cầu 10.000" | **Cần BA chốt phiên bản** | v3.5 KHÔNG nêu giới hạn cho `noi_dung_ket_qua`. Con số **10.000** chỉ có ở **SRS v4** (`srs-v4/srs-fr-05-vu-viec.md:1127`: "max 10.000 ký tự"). Đối tác đang đối chiếu theo v4, còn bản được chỉ định dùng là v3.5 → xem [`../../ba-confirm/vu-viec/ba-confirmation-needed-vu-viec.md`](../../ba-confirm/vu-viec/ba-confirmation-needed-vu-viec.md) BA-01 |

## Verdict

**`BA confirm`** — cập nhật 2026-07-20 (mới nhất): gộp về **1 trạng thái `BA confirm`** theo yêu cầu. **LƯU Ý:** 2 ý con (thiếu Tệp kết quả, thừa Kết luận) là **lỗi thật theo v3.5, dev fix bất kể BA** — không nên hiểu nhầm cả case là "chờ BA"; chỉ ý (3) char-limit mới chờ BA chốt phiên bản.

- **✅ 2 lỗi thật (dev fix bất kể BA):** 2/3 ý con là lỗi thật so với v3.5 — (1) thiếu trường `file_ket_qua` (Tệp kết quả hỗ trợ); (2) thừa trường "Kết luận" (thuộc CB NV ở FR-V.I-16, không thuộc người được phân công). Không phụ thuộc phiên bản → chuyển dev ngay.
- **⚠️ CẦN BA CONFIRM:** ý (3) "5000 vs 10.000 ký tự" — con số 10.000 chỉ có ở SRS v4, bản v3.5 được giao không nêu giới hạn → BA chốt phiên bản SRS chuẩn để chấm.

Bug ID: `BUG-CNKQHT_03` → [`../../bug-reports/vu-viec/Pass-bug-report-UAT-tuan-3.md`](../../bug-reports/vu-viec/Pass-bug-report-UAT-tuan-3.md). BA: mục CNKQHT_03 trong [`../../ba-confirm/vu-viec/ba-confirmation-needed-vu-viec.md`](../../ba-confirm/vu-viec/ba-confirmation-needed-vu-viec.md).

## Bất thường ngoài tiêu chí BA (postmortem 16/07 mục C1)

- Không phát hiện thêm bất thường ngoài 3 ý con của đối tác trong phạm vi modal này. Nhóm "Kết quả hỗ trợ" ở chế độ đọc hiển thị đúng placeholder "Tư vấn viên chưa cập nhật kết quả." khi vụ việc chưa có kết quả (empty state hợp lệ, không phải bug).
- **Không** thực hiện thao tác Lưu kết quả trên vụ việc này để giữ nguyên trạng thái "chưa có kết quả hỗ trợ" — cần cho case **TPDHSVV_02** (row 4) chạy sau (Trình phê duyệt khi chưa có kết quả hỗ trợ).
