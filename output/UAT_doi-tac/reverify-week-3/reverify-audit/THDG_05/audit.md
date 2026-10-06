# Audit — THDG_05 (row 72) — Open

**Verdict: Open — bug ĐÚNG (dev reject sai).** Ở đợt đánh giá **nhiều người**, màn Chấm điểm cho người đăng nhập nhập điểm vào vụ việc đã phân cho **người đánh giá khác**; khi lưu, backend trả **HTTP 422 `ERR-DG-SC-04`** với thông báo *"Vụ việc '…' không có kết quả đánh giá trong kế hoạch này"* — **sai bản chất** (VV vẫn thuộc kế hoạch, chỉ phân cho người khác) và **trái FR-VI-06** (người đánh giá chỉ chấm VV được phân công).

> ⚠️ **Đính chính so với audit round trước:** Bản cũ verdict `Reject` ("lưu một phần chạy đúng, lỗi không tái hiện"). **Sai** vì test SAI kịch bản: chỉ dựng đợt **1 người đánh giá**. Ở đợt 1 người, mọi VV đều thuộc người đăng nhập nên "lưu một phần / để trống VV" chạy đúng và không bao giờ chạm điều kiện gây lỗi. Toast của đối tác trích **mã VV nội bộ** (`aad90004-…-002`) ⇒ payload có VV **không gắn kết quả của người đăng nhập** ⇒ điều kiện thực = **đợt NHIỀU người đánh giá + chấm VV đã phân cho người khác**. Dựng đúng đợt nhiều người → lỗi **TÁI HIỆN** → verdict đổi `Reject` → `Open`.

## Cổng 1 — Bằng chứng (ĐÓNG)

- File đối tác: `partner-evidence/THDG_05.jpg` — full-res. Tài khoản **CB Nghiệp vụ - Trung ương (CB_NV_TW)**, tab **Chấm điểm**, đợt có **4 VV** ("Số VV đã chấm 0/4"). Đối tác chấm 3 VV, bấm **"Lưu kết quả"** → toast đỏ: *"Vụ việc 'aad90004-0000-4000-8000-000000000002' không có kết quả đánh giá trong kế hoạch này"*.

### 3 dữ kiện neo
| # | Dữ kiện | Giá trị |
|---|---|---|
| (a) | URL/ID | `/danh-gia/ke-hoach/7a28f369-b2d5-4a81-…` (env đối tác), tab Chấm điểm |
| (b) | Trạng thái entity | Đợt bước chấm điểm, "Số VV đã chấm 0/4" |
| (c) | Hiện tượng | Toast lỗi trích **mã VV nội bộ** khi bấm "Lưu kết quả" ⇒ có VV không gắn kết quả của người đăng nhập ⇒ đợt nhiều người |

## Cổng 2 — Hiểu bug (3 dòng)

1. **Evidence đã xem:** ảnh THDG_05.jpg — frame chứa toast lỗi đỏ *"Vụ việc 'aad90004-…-002' không có kết quả đánh giá trong kế hoạch này"* khi bấm "Lưu kết quả".
2. **Đối tác phản ánh CỤ THỂ:** thao tác "Lưu kết quả" ở màn chấm điểm phát sinh lỗi, không lưu được — mã VV trong thông báo không phải VV người dùng chủ ý chấm ⇒ màn cho chạm tới VV của người khác.
3. **Data + bước tái hiện:** login CB_NV_TW → đợt nhiều người đánh giá, mỗi VV phân 1 người → tab Chấm điểm → nhập điểm cho VV phân cho người khác → "Lưu kết quả" → quan sát toast + network.

## Bảng đối chiếu điều kiện

→ [`../../cond/THDG_05.md`](../../cond/THDG_05.md) — **0 GAP** (role CB_NV_TW, tab Chấm điểm, đợt 2 người đánh giá, chấm VV đã phân cho người khác). Lỗi TÁI HIỆN.

## Cổng 3 — Đối chiếu SRS (bản được giao: v3.5)

- **FR-VI-06 (UC88) — Thực hiện đánh giá.** §Preconditions dòng 471: *"User là người được phân công"*. §Processing **Bước 2** dòng 488: *"Kiểm tra quyền: user là người được phân công — BR-AUTH-01"*. → SRS quy định rõ **người đánh giá chỉ chấm VV được phân công cho mình**.
- **Data model KET_QUA_DANH_GIA** dòng 1048: trường `nguoi_danh_gia_id` (FK → TAI_KHOAN) → mỗi bản ghi kết quả (mỗi VV) gắn với **một người đánh giá cụ thể**. Bảng phân công (dòng 862) gán người đánh giá theo **Lĩnh vực phụ trách** → VV phân round-robin cho từng người.
- **§Error Handling FR-VI-06** dòng 517-520: chỉ có 4 mã lỗi (E1 điểm vượt max, E2 tổng trọng số, E3 sửa tiêu chí khi đang chấm, E4 0 VV). **KHÔNG có** mã lỗi cho tình huống "chấm VV đã phân cho người khác". Mã `ERR-DG-SC-04` và thông báo *"…không có kết quả đánh giá trong kế hoạch này"* **không tồn tại trong SRS v3.5** (grep toàn bộ `srs-fr-08-danh-gia.md` + thư mục `srs-v3.5/` → 0 kết quả).

**Phân tích Open vs BA confirm:** App sai một clause SRS rõ ràng (FR-VI-06 §Preconditions + §Processing Bước 2): người đánh giá chỉ chấm VV được phân công, nhưng FE cho nhập điểm VV của người khác. Dù đọc SRS theo hướng nào thì hành vi hiện tại vẫn **defective**: nếu mỗi người chỉ chấm VV của mình (đúng data model) → FE lỗi vì hiện VV người khác dạng nhập được; nếu bất kỳ người đánh giá nào cũng được chấm mọi VV → backend 422 lại là lỗi. Defective ở **cả hai cách hiểu** ⇒ **Open**, không phải BA confirm. Đây không phải bất đồng đặc tả mà là app trả lỗi sai + FE không tuân điều kiện tiên quyết.

## Kết quả verify trên env được giao (https://18.143.165.120.nip.io)

- Tự seed đợt `DG-20260722-0002` (id `de086bc5-…`): tạo tiêu chí (4 tiêu chí, tổng 100%) → phân công **2 người đánh giá** (`cbnv_tw` Trưởng nhóm + `cbnv_tw_02` Đánh giá viên) → Trình phê duyệt → `cbpd_tw` duyệt phân công → Thực hiện → chọn 2 VV.
- Round-robin phân công (xác nhận qua API `GET .../ket-quas`): **`EEE-VH-013` → `nguoiDanhGiaId f2e93500`** (cbnv_tw, người đăng nhập); **`EEE-VH-014` → `nguoiDanhGiaId 75ef9f6b`** (cbnv_tw_02).
- Tab Chấm điểm (đăng nhập `cbnv_tw`): **hiển thị cả 2 VV** với ô nhập điểm mở như nhau; **không có cột/nhãn người phụ trách** → không phân biệt được VV nào của mình.
- Nhập điểm 8 cho `EEE-VH-014` (của `cbnv_tw_02`) → "Lưu kết quả":
  - Toast đỏ (MutationObserver, không dedupe — 2 node wrapper + 2 node notice-error, không phải lọc trùng): *"Vụ việc 'eeeeeeee-0000-4000-8000-000000000014' không có kết quả đánh giá trong kế hoạch này"*.
  - Network `PUT .../ket-quas` → **[422]** `{"code":"ERR-DG-SC-04", "message":"Vụ việc 'eeeeeeee-…-014' không có kết quả đánh giá trong kế hoạch này"}`.
- Đối chứng API độc lập: cùng PUT cho `EEE-VH-014` (VV thuộc kế hoạch nhưng phân người khác) cũng trả **422 ERR-DG-SC-04** cùng thông báo → xác nhận cả UI lẫn API cùng lỗi.
- Happy-path: nhập điểm VV của chính mình (`EEE-VH-013`) lưu được bình thường → chức năng chấm điểm cơ bản đúng; lỗi chỉ ở không phân biệt VV theo người đánh giá + thông báo sai bản chất.
- **→ Hiện tượng đối tác báo TÁI HIỆN.**

## Verdict

**`Open`** — App vi phạm FR-VI-06 (UC88) §Preconditions dòng 471 + §Processing Bước 2 (BR-AUTH-01) dòng 488: người đánh giá chỉ chấm VV được phân công, nhưng màn Chấm điểm cho nhập điểm VV đã phân cho người khác rồi backend trả lỗi **sai bản chất** (`ERR-DG-SC-04` + thông báo không có trong SRS, hàm ý VV không thuộc kế hoạch trong khi thực tế VV **thuộc** kế hoạch). Bug đối tác báo là **đúng** — chuyển Dev. Bug ID `BUG-THDG_05` (xem `../../bug-reports/thdg/Pass-bug-report-THDG_05.md`).

> **Cập nhật re-verify 2026-07-22 (sau dev fix): `Closed / PASS`.** Tab Chấm điểm nay khoá ô nhập + gắn nhãn "Người khác chấm" cho VV phân cho người đánh giá khác; payload lưu chỉ gồm VV của người đăng nhập → `PUT .../ket-quas` **200**, không còn 422 `ERR-DG-SC-04`.

## Evidence
- `../../bug-reports/thdg/image/THDG_05-01-scoringtable-shows-foreign-vv-editable.png` — tab Chấm điểm hiển thị cả VV của người khác với ô nhập điểm mở.
- `../../bug-reports/thdg/image/THDG_05-02-foreign-vv-save-422-toast.png` — nhập điểm 8 cho VV `EEE-VH-014` (của người khác).
- Toast `ant-message-notice-error`: *"Vụ việc 'eeeeeeee-…-014' không có kết quả đánh giá trong kế hoạch này"*.
- Network `PUT .../ket-quas` → 422 `ERR-DG-SC-04`; API `GET .../ket-quas` xác nhận `nguoiDanhGiaId` khác nhau giữa 2 VV.
- Bảng điều kiện: [`../../cond/THDG_05.md`](../../cond/THDG_05.md).
