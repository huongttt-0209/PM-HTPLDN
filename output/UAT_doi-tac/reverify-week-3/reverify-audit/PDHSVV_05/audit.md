# Audit — PDHSVV_05 (row 10) · Từ chối phê duyệt thành công — "không gửi thông báo + không hiển thị lý do từ chối"

## Cổng 1 — Bằng chứng (ĐÓNG)

- File đối tác: `partner-evidence/PDHSVV_05-main.webm` (video, `fetch_evidence.py --row 10` exit 0) + ảnh `PDHSVV_05.jpg`.
- Frame chứa LỖI đối tác báo: video quay lại thao tác Từ chối thành công (toast + đổi trạng thái) rồi kiểm chuông thông báo của người phụ trách → **trống, không có mục từ chối**; mở chi tiết vụ việc → **không thấy lý do từ chối**.

### 3 dữ kiện neo (từ evidence + cột sheet)

| # | Dữ kiện | Giá trị |
|---|---|---|
| (a) | Điều kiện đối tác | CB phê duyệt **cùng đơn vị** với đơn vị tạo hồ sơ; vụ việc ở **"Chờ phê duyệt"** |
| (b) | Hiện tượng đối tác báo (cột "Kết quả thực tế") | (1) "Hệ thống **không gửi thông báo**"; (2) "Chi tiết bản ghi **không hiển thị lý do từ chối**" |
| (c) | Kỳ vọng đối tác (cột "Kết quả mong đợi") | Đổi trạng thái Chờ phê duyệt → Đang xử lý (ĐẠT) + **gửi thông báo cho CB nghiệp vụ và người hỗ trợ phụ trách kèm lý do** + lưu vết |

## Cổng 2 — Hiểu bug (3 dòng)

1. **Evidence đã xem:** video PDHSVV_05 — CB PD cùng đơn vị từ chối vụ việc ở "Chờ phê duyệt" thành công (đổi trạng thái + toast), nhưng người phụ trách không nhận thông báo và màn chi tiết không hiện lý do từ chối.
2. **Đối tác phản ánh CỤ THỂ:** 2 ý — (1) không gửi thông báo cho CB nghiệp vụ + người hỗ trợ; (2) chi tiết vụ việc không hiển thị lý do từ chối.
3. **Data + bước tái hiện:** login CB PD cùng đơn vị → vụ việc "Chờ phê duyệt" → [Từ chối] → nhập lý do hợp lệ → Xác nhận → kiểm (a) chuông + email của CB NV/assignee, (b) màn chi tiết vụ việc có hiện lý do không.

## Bảng đối chiếu điều kiện

→ [`../../cond/PDHSVV_05.md`](../../cond/PDHSVV_05.md) — **0 GAP** về role/state/data. Đã xác nhận app thực tế đúng điều kiện đối tác.

## Cổng 3 — Đối chiếu SRS (bản được giao: v3.5)

### Ý (1) — Thông báo khi từ chối

| Nguồn SRS v3.5 | Yêu cầu | Vị trí |
|---|---|---|
| FR-V.I-13 §Processing bước 4 | "Gửi thông báo **CB NV phụ trách + NHT** (nếu từ chối)" — BR-NOTIF-01 | `srs-fr-05-vu-viec.md:986` |
| FR-V.I-13 §Postconditions | "**CB NV phụ trách + NHT** (nếu từ chối) nhận thông báo kết quả" | `:995` |
| FR-V.I-13 §Acceptance Criteria | "Given CB PD từ chối When nhập lý do (≥10) Then trạng thái → DANG_XU_LY..., **thông báo CB NV + người được phân công**" | `:1008` |
| BR-NOTIF-01 | "Mọi sự kiện workflow (phân công, xác nhận, **từ chối**, phê duyệt...) đều gửi thông báo cho người liên quan qua **2 kênh: in-app (THONG_BAO) + email**" | `:2453-2455` |

→ Kết quả test: sau khi từ chối (06:03Z), **cả `cbnv_tw` (CB NV phụ trách) lẫn `qa_tvvseed28` (người được phân công) đều KHÔNG có thông báo từ chối** (in-app `noticesSince0555Z=[]`, `anyRejectNoticeEver=[]`; email MailHog không có mail từ chối). ❌ **Vi phạm SRS** (thiếu thông báo cho cả 2 người nhận bắt buộc, cả 2 kênh).

### Ý (2) — Hiển thị lý do từ chối

| Nguồn SRS v3.5 | Yêu cầu | Vị trí |
|---|---|---|
| FR-V.I-13 §Processing bước 3 | Nếu TU_CHOI: "ghi `ly_do` vào **LICH_SU_VU_VIEC**" | `:985` |
| Màn chi tiết SCR — Accordion 7 (Phê duyệt) | "Common Approval Fields: thoi_gian_duyet, nguoi_duyet, quyết định (PHE_DUYET/TU_CHOI), **ly_do_tu_choi**" — hiển thị "Khi VV đã qua CHO_PHE_DUYET" | `:1722` |
| BR-FLOW-04 | "Mọi hành động 'Từ chối' phải nhập lý do. **Lý do hiển thị cho người tạo ban đầu.**" | `:2395` |

→ Kết quả test: lý do **có lưu** ở `VU_VIEC.ghiChuPheDuyet` + `LICH_SU_VU_VIEC.duLieuMoi.lyDo` (bước 3 ĐẠT ở tầng dữ liệu), **nhưng UI không hiển thị ở đâu khi VV bị từ chối về DANG_XU_LY**: Dòng thời gian chỉ hiện "Từ chối duyệt" + giờ + người (không kèm lý do); **nhóm "Phê duyệt" (Accordion 7) KHÔNG hiển thị ở trạng thái DANG_XU_LY** — app chỉ hiện nhóm này khi VV đang CHO_PHE_DUYET hoặc DA_DUYET (xác nhận thêm khi verify PDHSVV_02: ở DA_DUYET nhóm Phê duyệt hiện Người duyệt/Ngày duyệt/Ghi chú). Kiểm cả 2 view (assignee + CB NV): `hasReasonTextOnPage=false`. ❌ **Vi phạm SRS**: Accordion 7 (:1722) quy định hiển thị "khi VV đã qua CHO_PHE_DUYET" — VV bị từ chối ĐÃ đi qua CHO_PHE_DUYET nên nhóm này (kèm `ly_do_tu_choi`) phải vẫn hiển thị; BR-FLOW-04 (:2395) yêu cầu lý do hiển thị cho người tạo/người sửa — đúng lúc người được phân công cần biết lý do để sửa lại thì không thấy.

## Kết quả verify trên env được giao (https://18.143.165.120.nip.io)

- Vụ việc **VV-BTP-TW-20260712-001** (id `8e259653-e0a5-49e8-ae7c-5fb07734ce09`), đơn vị BTP·TW.
- `cbpd_tw` (CB_PD_TW, cùng đơn vị) từ chối ở CHO_PHE_DUYET với lý do hợp lệ 110 ký tự → toast "Đã từ chối phê duyệt", VV → DANG_XU_LY (đổi trạng thái ĐẠT).
- **Ý (1):** `cbnv_tw` + `qa_tvvseed28` kiểm chuông (fetch `/api/v1/thong-baos`) + email — không có thông báo từ chối. Loại trừ nhiễu: cả 2 vẫn nhận thông báo khác. Ảnh: `BUG-PDHSVV_05-cbnv-khong-co-thong-bao.png`, `BUG-PDHSVV_05-assignee-khong-co-thong-bao.png`.
- **Ý (2):** màn chi tiết VV (cả assignee + CB NV) không hiện lý do; timeline "Từ chối duyệt" trống lý do; không có accordion Phê duyệt. Ảnh: `BUG-PDHSVV_05-timeline-tu-choi-khong-ly-do.png`, `BUG-PDHSVV_05-cbnv-vv-detail-khong-hien-ly-do.png`.

## Verdict

**`Open`** — Cả 2 ý đối tác báo đều là **lỗi thật theo v3.5**: (1) thiếu thông báo từ chối cho CB NV + người được phân công (vi phạm FR-V.I-13 :986/:995/:1008 + BR-NOTIF-01 :2455); (2) màn chi tiết không hiển thị lý do từ chối (vi phạm Accordion 7 :1722 + BR-FLOW-04 :2395). Không phụ thuộc phiên bản SRS (khác PDHSVV_04). Đã log **BUG-PDHSVV_05** (2 ý) vào `Pass-bug-report-UAT-tuan-3.md`.

Ý (1) cùng nhóm lỗi thiếu thông báo với **TPDHSVV_04** (thiếu thông báo khi trình phê duyệt) và **XNTGHTVV_04** (thiếu thông báo khi chấp nhận tham gia) → gợi ý cùng root-cause tầng gửi thông báo workflow vụ việc.
