# Audit — TPDHSVV_04 (row 5) · Trình phê duyệt thành công — "Cán bộ phê duyệt không nhận thông báo"

## Cổng 1 — Bằng chứng (ĐÓNG)

- File: `partner-evidence/TPDHSVV_04-2.webm` (8.0 MB, `fetch_evidence.py --row 5` exit 0) + `TPDHSVV_04-1.webm` (203 KB). Video quay màn hình.
- Frame chứa LỖI đối tác báo: `t021.10s` — sau khi trình phê duyệt (frame `t000` là CB_NV_TW ở vụ việc VV-BTP-TW-20260709-001 "Đang xử lý"), đối tác đăng nhập **CB_PD_TW** (chuông 28), mở dropdown "Thông báo" → chỉ có "Tài khoản vừa đăng nhập ở nơi khác" + "Đăng ký đào tạo mới cho khóa học" — **không** có thông báo vụ việc chờ phê duyệt.

### 3 dữ kiện neo

| # | Dữ kiện | Giá trị đọc từ evidence |
|---|---|---|
| (a) | URL / ID vụ việc | `htpldn-uat.ospgroup.vn/vu-viec/9ed9d021-f308-40cc-b4d7-b60b80fbc1dd` — VV-BTP-TW-20260709-001, "Đang xử lý", "Còn 15 ngày LV", lĩnh vực Thuế |
| (b) | Hiện tượng | Vụ việc trình phê duyệt thành công (Đang xử lý → Chờ phê duyệt). Sau đó đăng nhập **CB_PD_TW**, mở chuông → **không** thấy thông báo về vụ việc vừa trình |
| (c) | Vai trò 2 người | Người trình: **CB_NV_TW** (chuông 96, frame t000). Người kiểm thông báo: **CB_PD_TW** (chuông 28, frame t021) — "Cán bộ PD Trung ương" |

## Cổng 2 — Hiểu bug (3 dòng)

1. **Evidence đã xem:** 2 video — CB_NV_TW trình phê duyệt vụ việc "Đang xử lý" (đã có kết quả hỗ trợ) thành công; chuyển sang CB_PD_TW mở chuông, danh sách thông báo chỉ có login + đăng ký đào tạo, **thiếu** thông báo "vụ việc chờ phê duyệt".
2. **Đối tác phản ánh CỤ THỂ (cột "Kết quả thực tế"):** "**Cán bộ phê duyệt cùng đơn vị không nhận được thông báo**". KQ mong đợi của đối tác (cột KQ mong đợi): trình thành công + "**Gửi thông báo cho Cán bộ phê duyệt cùng đơn vị**".
3. **Data + bước tái hiện:** login CB_NV_TW → vụ việc "Đang xử lý" đã có kết quả hỗ trợ → [Trình phê duyệt] → xác nhận → sang tài khoản CB_PD_TW cùng đơn vị → mở chuông/kiểm email xem có thông báo không.

## Bảng đối chiếu điều kiện

→ [`../../cond/TPDHSVV_04.md`](../../cond/TPDHSVV_04.md) — **0 GAP**.

## Cổng 3 — Đối chiếu SRS (v3.5, bản được giao chấm)

| # | Yêu cầu SRS (trích nguyên văn) | Vị trí | Web thực tế | Khớp? |
|---|---|---|---|:-:|
| 1 | "CB NV nhấn 'Trình phê duyệt' → auto CHO_PHE_DUYET + **thông báo CB PD**" | `srs-fr-05-vu-viec.md:78` (AT-03) | Vụ việc chuyển CHO_PHE_DUYET đúng, **nhưng CB PD không nhận thông báo** | ❌ |
| 2 | FR-V.I-11 Trình phê duyệt — Processing bước 3: "**Gửi thông báo CB PD cùng cấp**" (BR-FLOW-03) | `srs-fr-05-vu-viec.md:877` | Không gửi | ❌ |
| 3 | FR-V.I-11 Postconditions: "VV chuyển trạng thái CHO_PHE_DUYET" + "**CB PD cùng cấp nhận thông báo**" | `srs-fr-05-vu-viec.md:884-885` | Postcond 1 đạt (đã chuyển CHO_PHE_DUYET); **postcond 2 KHÔNG đạt** (CB PD không nhận thông báo) | ❌ |
| 4 | BR-NOTIF-01: "Mọi sự kiện workflow (phân công, xác nhận, từ chối, **phê duyệt**, hoàn thành, ...) đều gửi thông báo cho người liên quan qua **2 kênh: in-app (THONG_BAO) + email**" | `srs-fr-05-vu-viec.md:2453-2455` | Cả in-app lẫn email đều không có thông báo trình phê duyệt vụ việc | ❌ |

## Kết quả verify trên env được giao (https://18.143.165.120.nip.io)

Vụ việc **VV-BTP-TW-20260712-001** (`8e259653...`), đơn vị BTP·TW.

### Chuẩn bị tiền đề
- `qa_tvvseed28` (TVV·CG, người được phân công) cập nhật kết quả hỗ trợ: `POST .../cap-nhat-ket-qua` → **201**; nhóm "Kết quả hỗ trợ" hiện nội dung. → vụ việc đủ điều kiện trình phê duyệt.

### Baseline CB_PD_TW (`cbpd_tw`, CB_PD_TW · BTP·TW) — TRƯỚC khi trình
- Chuông in-app: **27 chưa đọc**; thông báo mới nhất **2026-07-16T15:20** (không có gì mới hơn 16/07); **0** thông báo về vụ việc `8e259653` / "vụ việc chờ phê duyệt".
- Email (MailHog `cbpd_tw@htpldn.test`): 16 thư, **toàn bộ là mã OTP đăng nhập**, 0 thư nghiệp vụ.

### Thao tác trình (CB_NV_TW `cbnv_tw`) — bộ đo tools/toast-capture.js, tự kiểm observer = 1
- 1 request `POST .../trinh-phe-duyet` + **1 toast** "Đã trình phê duyệt" (không nhân đôi, không lộ mã lỗi).
- Vụ việc → **CHO_PHE_DUYET**; timeline "TRINH_PD 2026-07-20T05:43:08Z (CB Nghiệp vụ - Trung ương)".

### Sau khi trình — kiểm lại CB_PD_TW
- Chuông in-app **vẫn 27 chưa đọc**; thông báo mới nhất **vẫn 16/07**; **0** thông báo về vụ việc vừa trình (kiểm cả API `/thong-baos` 20 mục mới nhất + dropdown chuông trên UI — 5 mục đầu đều "4 ngày trước").
- Email `cbpd_tw@htpldn.test`: 18 thư, **vẫn 0 thư nghiệp vụ** (2 thư mới chỉ là OTP đăng nhập mình vừa kích).

### Loại trừ nhiễu (bài học XNTGHTVV_04)
- **Không phải rớt toàn hệ thống:** CB_PD_TW **vẫn nhận** thông báo "chờ phê duyệt" cho khóa học (KH-20260716-*) + hồ sơ TVV → kênh thông báo hoạt động, chỉ **thiếu riêng** thông báo trình phê duyệt vụ việc.
- **Không phải sai người nhận:** vụ việc đã nằm trong danh sách "Chờ phê duyệt" của chính `cbpd_tw` (API `?trangThai=CHO_PHE_DUYET` trả đúng vụ việc này; UI hiện nút [Phê duyệt]/[Từ chối]) → `cbpd_tw` đúng là người phê duyệt cần được thông báo.
- **Không phải sai trạng thái/role:** vụ việc chuyển CHO_PHE_DUYET thành công; `cbpd_tw` là CB_PD_TW cùng đơn vị BTP·TW.

## Verdict

**`Open`** — Lỗi thật, tái hiện đúng điều kiện đối tác nêu. Vụ việc trình phê duyệt thành công (chuyển CHO_PHE_DUYET, có toast) nhưng **Cán bộ Phê duyệt cùng đơn vị KHÔNG nhận được bất kỳ thông báo nào** (cả in-app lẫn email) về vụ việc chờ duyệt, dù vụ việc đã nằm trong hàng chờ phê duyệt của đúng cán bộ đó. Vi phạm FR-V.I-11 Processing bước 3 (:877) + Postcondition (:885) + AT-03 (:78) + BR-NOTIF-01 (:2455). Cùng nhóm lỗi thiếu thông báo với XNTGHTVV_04.

Bug ID: **BUG-TPDHSVV_04** (Major) — ghi trong Pass-bug-report-UAT-tuan-3.md.

## Bất thường ngoài tiêu chí đối tác báo

- Email nghiệp vụ trên env này chưa từng gửi (chỉ có OTP) — nên bằng chứng chắc chắn nhất là kênh in-app (chuông). Đối tác cũng chỉ quan sát kênh in-app. Việc email cũng thiếu là **nhất quán** với lỗi, nhưng do env không phát thư nghiệp vụ cho bất kỳ ai nên không tách riêng thành lỗi email độc lập — chỉ nêu để đầy đủ.
