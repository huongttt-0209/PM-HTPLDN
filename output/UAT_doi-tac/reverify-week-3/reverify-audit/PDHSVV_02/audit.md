# Audit — PDHSVV_02 (row 7) · Phê duyệt vụ việc thành công — "không gửi thông báo cho CB Nghiệp vụ + lỗi hiển thị Người duyệt"

## Cổng 1 — Bằng chứng (ĐÓNG)

- File đối tác: `partner-evidence/PDHSVV_02.*` (`fetch_evidence.py --row 7`). Quay lại thao tác Phê duyệt thành công rồi kiểm chuông của CB nghiệp vụ (trống) + mở nhóm "Phê duyệt" thấy Người duyệt hiển thị sai.
- Frame chứa LỖI đối tác báo: chuông CB nghiệp vụ không có thông báo duyệt + trường "Người duyệt" ở nhóm Phê duyệt hiển thị lỗi.

### 3 dữ kiện neo (từ evidence + cột sheet)

| # | Dữ kiện | Giá trị |
|---|---|---|
| (a) | Điều kiện đối tác | CB phê duyệt **cùng đơn vị** với đơn vị tạo hồ sơ; vụ việc ở **"Chờ phê duyệt"** |
| (b) | Hiện tượng đối tác báo (cột "Kết quả thực tế") | (1) "Hệ thống **không gửi thông báo** cho cán bộ nghiệp vụ phụ trách hồ sơ"; (2) "**Lỗi hiển thị thông tin Người duyệt** trong nhóm Phê duyệt" |
| (c) | Kỳ vọng đối tác (cột "Kết quả mong đợi") | Chuyển "Chờ phê duyệt" → "Đã duyệt" + **ghi người phê duyệt và thời điểm** + **gửi thông báo cho CB nghiệp vụ phụ trách** + lưu vết |

## Cổng 2 — Hiểu bug (3 dòng)

1. **Evidence đã xem:** video/ảnh PDHSVV_02 — CB PD cùng đơn vị phê duyệt vụ việc ở "Chờ phê duyệt" thành công, nhưng CB nghiệp vụ phụ trách không nhận thông báo và trường Người duyệt hiển thị sai.
2. **Đối tác phản ánh CỤ THỂ:** 2 ý — (1) không gửi thông báo cho CB nghiệp vụ phụ trách; (2) trường Người duyệt trong nhóm Phê duyệt hiển thị lỗi.
3. **Data + bước tái hiện:** login CB PD cùng đơn vị → vụ việc "Chờ phê duyệt" → [Phê duyệt] → xác nhận → kiểm (a) chuông + email của CB NV phụ trách, (b) nhóm Phê duyệt xem trường Người duyệt.

## Bảng đối chiếu điều kiện

→ [`../../cond/PDHSVV_02.md`](../../cond/PDHSVV_02.md) — **0 GAP** về role/state/data. Đã xác nhận app thực tế đúng điều kiện đối tác.

## Cổng 3 — Đối chiếu SRS (bản được giao: v3.5)

### Ý (1) — Thông báo cho CB Nghiệp vụ khi phê duyệt

| Nguồn SRS v3.5 | Yêu cầu | Vị trí |
|---|---|---|
| FR-V.I-13 §Processing bước 2 + 4 | Bước 2: PHE_DUYET → DA_DUYET, set `nguoi_phe_duyet_id`, `ngay_phe_duyet`. Bước 4: "Gửi thông báo **CB NV phụ trách** + NHT (nếu từ chối)" | `srs-fr-05-vu-viec.md:984, :986` |
| FR-V.I-13 §Postconditions | "**CB NV phụ trách** + NHT (nếu từ chối) nhận thông báo kết quả" | `:995` |
| BR-NOTIF-01 | "Mọi sự kiện workflow (phân công, xác nhận, từ chối, **phê duyệt**, hoàn thành...) đều gửi thông báo cho người liên quan qua **2 kênh: in-app (THONG_BAO) + email**" | `:2453-2455` |

→ "Phê duyệt" là sự kiện workflow (BR-NOTIF-01 liệt kê rõ), và CB NV phụ trách là người nhận kết quả (bước 4 + postcond). Kết quả test: sau khi phê duyệt (06:23:32Z), `cbnv_tw` **KHÔNG có thông báo** phê duyệt vụ việc (in-app: unread giữ 117, không có mục sau 06:10Z; email: chỉ OTP). ❌ **Vi phạm SRS**.

### Ý (2) — Hiển thị Người duyệt

| Nguồn SRS v3.5 | Yêu cầu | Vị trí |
|---|---|---|
| Màn chi tiết SCR — Accordion 7 (Phê duyệt) | "Common Approval Fields: thoi_gian_duyet, **nguoi_duyet**, quyết định (PHE_DUYET/TU_CHOI), ly_do_tu_choi" | `:1722` |

→ Trường `nguoi_duyet` phải hiển thị **danh tính người duyệt** (tên/chức danh) cho người dùng nghiệp vụ đọc. Kết quả test: nhóm "Phê duyệt" hiển thị `Người duyệt` = **"ID: 4101cf26-cdbd-4f00-ae38-bc3e380366a3"** (mã định danh UUID nội bộ) thay vì tên "CB Phê duyệt - Trung ương". ❌ **Vi phạm** — lộ mã định danh kỹ thuật ra giao diện thay vì tên (cùng loại lộ mã nội bộ với BUG-VV-MALOI-LO-UI). Nguyên nhân: API chi tiết trả `nguoiDuyetId` (UUID) nhưng không kèm tên phân giải; FE đổ thẳng UUID kèm tiền tố "ID: ".

## Kết quả verify trên env được giao (https://18.143.165.120.nip.io)

- Vụ việc **VV-BTP-TW-20260712-001** (id `8e259653-...`), đơn vị BTP·TW. `cbnv_tw` trình lại phê duyệt → CHO_PHE_DUYET (tiền đề).
- `cbpd_tw` (CB_PD_TW, cùng đơn vị) bấm [Phê duyệt] → hộp thoại xác nhận → toast **"Đã phê duyệt"**, VV → **DA_DUYET**, `nguoiDuyetId=4101cf26-...`, `ngayDuyet=2026-07-20T06:23:32Z`. Đo bằng `tools/toast-capture.js` (tự kiểm observer=1): 1 toast "Đã phê duyệt" (không lặp).
- **Ý (1):** `cbnv_tw` kiểm chuông (`/api/v1/thong-baos`, unread-count) + email — không có thông báo duyệt. Loại trừ nhiễu: `cbnv_tw` vẫn nhận `PHE_DUYET` cho khóa học. Ảnh: `BUG-PDHSVV_02-cbnv-khong-co-thong-bao-duyet.png`.
- **Ý (2):** nhóm "Phê duyệt" render `Người duyệt` = "ID: 4101cf26-cdbd-4f00-ae38-bc3e380366a3", `Ngày duyệt` = "20/07/2026 13:23", `Ghi chú` = "—". Ảnh: `BUG-PDHSVV_02-nguoi-duyet-hien-uuid.png`.

## Verdict

**`Open`** — Cả 2 ý đối tác báo đều là **lỗi thật theo v3.5**: (1) thiếu thông báo phê duyệt cho CB NV phụ trách (vi phạm FR-V.I-13 :986/:995 + BR-NOTIF-01 :2455); (2) trường Người duyệt ở nhóm Phê duyệt hiển thị UUID thay vì tên (vi phạm Accordion 7 :1722 — lộ mã định danh nội bộ). Không phụ thuộc phiên bản SRS. Đã log **BUG-PDHSVV_02** (2 ý).

Ý (1) cùng nhóm lỗi thiếu thông báo với **PDHSVV_05 / TPDHSVV_04 / XNTGHTVV_04** → gợi ý cùng root-cause tầng gửi thông báo workflow vụ việc.
