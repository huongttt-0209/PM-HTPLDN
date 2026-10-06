# Audit — PDHSVV_04 (row 9) · Modal Từ chối phê duyệt — "giới hạn 1.000 vs SRS 2.000 ký tự"

## Cổng 1 — Bằng chứng (ĐÓNG)

- File: `partner-evidence/PDHSVV_04.jpg` (222 KB, `fetch_evidence.py --row 9` exit 0). 1 ảnh chụp màn.
- Frame chứa LỖI đối tác báo: chính ảnh này — modal **"Từ chối phê duyệt"**, ô "Lý do" gõ "a", bộ đếm hiển thị **"1 / 1000"** → tối đa 1000 ký tự.

### 3 dữ kiện neo

| # | Dữ kiện | Giá trị đọc từ ảnh |
|---|---|---|
| (a) | URL / ID vụ việc | `htpldn-uat.ospgroup.vn/vu-viec/9d44d0dc-44e9-4bb0-aebd-4928f4496f69` — VV-BKH-2026..., stepper đang ở "Chờ phê duyệt" |
| (b) | Hiện tượng | Modal "Từ chối phê duyệt", ô "Lý do" (bắt buộc), hint "Tối thiểu 10 ký tự", bộ đếm **"1 / 1000"** |
| (c) | Vai trò | Header: **Cán bộ PD Bộ ngành · CB_PD_BN**, đơn vị BTP·BN, chuông 3 |

## Cổng 2 — Hiểu bug (3 dòng)

1. **Evidence đã xem:** `PDHSVV_04.jpg` — CB_PD_BN mở modal "Từ chối phê duyệt" ở vụ việc "Chờ phê duyệt", ô Lý do có bộ đếm "1 / 1000" → app cho tối đa 1000 ký tự.
2. **Đối tác phản ánh CỤ THỂ (cột "Kết quả thực tế"):** "Hệ thống cho phép **tối đa 1.000 ký tự**" — trong khi cột "Kết quả mong đợi" ghi "tối thiểu 10, **tối đa 2.000 ký tự**". Tức đối tác cho rằng SRS yêu cầu max 2000, app chỉ cho 1000.
3. **Data + bước tái hiện:** login CB PD cùng đơn vị → vụ việc "Chờ phê duyệt" → bấm [Từ chối] → mở modal → đo maxlength ô Lý do.

## Bảng đối chiếu điều kiện

→ [`../../cond/PDHSVV_04.md`](../../cond/PDHSVV_04.md) — **0 GAP** về role/state/data; GAP còn lại là **phiên bản SRS**.

## Cổng 3 — Đối chiếu SRS (điểm mấu chốt: LỆCH PHIÊN BẢN)

| Nguồn | Ràng buộc trường "Lý do" (`ly_do`) từ chối phê duyệt | Vị trí |
|---|---|---|
| **SRS v3.5** (bản được giao chấm) | FR-V.I-13 §Inputs: "Bắt buộc nếu TU_CHOI" — **KHÔNG nêu max**. AC: "nhập lý do (≥ 10 ký tự)" — chỉ min | `srs-v3.5/srs-fr-05-vu-viec.md:977` + `:1008` |
| **SRS v4** | FR-V.I-13 §Inputs: "Bắt buộc nếu TU_CHOI; **min 10 ký tự, max 2000**, sanitize C16" | `srs-v4/srs-fr-05-vu-viec.md:1007` |
| **App thực tế** | Ô Lý do: min 10, **max 1000** | Env test |

**Nhận định:** con số **2.000** đối tác dẫn **chỉ tồn tại ở v4**, không có trong v3.5. Theo v3.5 (bản được giao), trường Lý do **không bị quy định max** → app giới hạn 1000 **không vi phạm v3.5**. Theo v4, max phải là 2000 → app 1000 là thiếu. → Kết quả Đạt/Không đạt **đổi theo phiên bản** — đúng loại câu hỏi BA-01.

## Kết quả verify trên env được giao (https://18.143.165.120.nip.io)

- Tài khoản `cbpd_tw` (CB_PD_TW · BTP·TW — Cán bộ Phê duyệt cùng đơn vị với đơn vị tạo hồ sơ), vụ việc **VV-BTP-TW-20260712-001** ở **CHO_PHE_DUYET**.
- Bấm [Từ chối] → mở modal **"Từ chối phê duyệt"**, ô "Lý do" (bắt buộc), placeholder "Nhập lý do...", hint "Tối thiểu 10 ký tự", bộ đếm "0 / 1000".
- Đọc trực tiếp DOM: `textarea.maxLength = **1000**` → xác nhận app giới hạn cứng tối đa 1000 ký tự (khớp đối tác). Thao tác không phá trạng thái (bấm Hủy, vụ việc giữ CHO_PHE_DUYET).
- Ảnh: `modal-tu-choi-max-1000.png`.

## Verdict

**`BA confirm`** — App thực tế **đúng như đối tác báo** (ô Lý do từ chối tối đa 1000 ký tự), KHÔNG bất đồng về thực tế nên không phải Reject. Nhưng "phải là 2.000" là **yêu cầu chỉ có ở SRS v4**, còn SRS v3.5 (bản được giao chấm) **không quy định max** → theo v3.5 thì app 1000 không vi phạm; theo v4 thì thiếu. Verdict phụ thuộc phiên bản SRS chuẩn → chuyển BA quyết (gộp vào **BA-01**, đã bổ sung PDHSVV_04 vào bảng divergence).

Không tạo entry bug (chưa xác định là lỗi theo bản được giao) — chờ BA chốt version. Nếu BA chốt v4 → mở bug "ô Lý do từ chối giới hạn 1000 < yêu cầu 2000".
