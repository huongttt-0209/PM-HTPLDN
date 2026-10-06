# Audit — TBKQTNHS_01 (row 6) · "Gửi thông báo kết quả tiếp nhận hồ sơ — không có chức năng"

## Cổng 1 — Bằng chứng (ĐÓNG)

- File đối tác: `partner-evidence/TBKQTNHS_01-1.webm` + `TBKQTNHS_01-2.webm` (video, `fetch_evidence.py --row 6`). Không trích được frame (thiếu ffmpeg), nhưng cột mô tả sheet đã nêu rõ điều kiện + bước + kỳ vọng + kết quả thực tế (đọc trực tiếp từ sheet, dưới đây).
- Text sheet đối tác (row 6):
  - **Tên chức năng:** Thông báo kết quả tiếp nhận hồ sơ.
  - **Tác nhân:** Cán bộ nghiệp vụ TW/BN/ĐP.
  - **Mô tả / Kết quả mong đợi:** cung cấp chức năng gửi thông báo kết quả kiểm tra hồ sơ (Đạt/Không đạt) cho DNNVV.
  - **Điều kiện:** đã đăng nhập; hồ sơ vụ việc đã qua bước kiểm tra; DN có ≥1 kênh nhận thông báo hợp lệ.
  - **Các bước:** menu "Vụ việc HTPL" → Xem chi tiết → **bấm nút "Gửi thông báo kết quả"**.
  - **Kết quả thực tế:** *"Màn hình không hiển thị/cung cấp chức năng"*.

### 3 dữ kiện neo

| # | Dữ kiện | Giá trị |
|---|---|---|
| (a) | Điều kiện đối tác | CB NV, hồ sơ **đã qua bước kiểm tra** |
| (b) | Hiện tượng đối tác báo | Không có nút/chức năng **"Gửi thông báo kết quả"** trên màn chi tiết |
| (c) | Kỳ vọng đối tác | Có nút bấm tay để gửi thông báo kết quả kiểm tra (Đạt/Không đạt) cho DN |

## Cổng 2 — Hiểu bug (3 dòng)

1. **Evidence:** cột sheet — CB NV mở chi tiết vụ việc đã qua kiểm tra, tìm nút "Gửi thông báo kết quả" nhưng không thấy.
2. **Đối tác phản ánh CỤ THỂ:** thiếu nút bấm tay "Gửi thông báo kết quả" (theo AC `:947` "nhấn Gửi Thông báo").
3. **Data + bước tái hiện:** mở vụ việc ở trạng thái đã qua kiểm tra (DANG_KIEM_TRA có kết luận + HOAN_THANH) → quét toàn bộ nút thanh hành động + accordion + tìm nguyên văn "Gửi thông báo kết quả" → đối chiếu đặc tả FR-V.I-12 (auto hay tay?).

## Bảng đối chiếu điều kiện

→ [`../../cond/TBKQTNHS_01.md`](../../cond/TBKQTNHS_01.md) — **0 GAP**. Test đúng vai trò CB NV + đúng điều kiện "đã qua kiểm tra".

## Cổng 3 — Đối chiếu SRS (bản được giao: v3.5) — PHÁT HIỆN MÂU THUẪN NỘI TẠI

| Nguồn SRS v3.5 | Nói gì về "gửi thông báo kết quả" | Vị trí |
|---|---|---|
| FR-V.I-12 §Màn hình | FR-V.I-12 là **"Auto action — Thông báo KQ"** → hành động **tự động** | `srs-fr-05-vu-viec.md:905` |
| SCR-V.I-03 §Quy tắc nghiệp vụ bổ sung | "Thông báo kết quả = **auto trigger khi chuyển trạng thái**. Gửi tự động qua Cổng PLQG + in-app" → **KHÔNG có nút bấm tay** | `srs-fr-05-vu-viec.md:1758` |
| FR-V.I-12 §Acceptance Criteria | "**When** nhấn **'Gửi Thông báo'** **Then** gửi kết quả (Đạt/Không đạt) qua in-app + email" → hàm ý **CÓ nút bấm tay** | `srs-fr-05-vu-viec.md:947` |

→ **Mâu thuẫn trong chính đặc tả:** §Màn hình (`:905`) + quy tắc màn hình (`:1758`) nói **auto (không nút)**; AC (`:947`) nói **nhấn nút**. Không thể tự quyết bên nào đúng.

→ App thực tế: **không có nút** "Gửi thông báo kết quả" → khớp cách hiểu **auto** (`:1758`), trái AC `:947`. Đối tác kỳ vọng theo AC `:947` (có nút).

## Kết quả verify trên env được giao (https://18.143.165.120.nip.io)

- `cbnv_tw` (CB_NV_TW) mở 2 vụ việc:
  - **VV-STP-AG-20260712-001** (DANG_KIEM_TRA — đang/kết luận kiểm tra): thanh hành động chỉ có **[Phân công]** + **[Kiểm tra lại]**; không có nút "Gửi thông báo kết quả".
  - **VV-BTP-TW-20260712-001** (HOAN_THANH — đã qua kiểm tra): không có nút "Gửi thông báo kết quả".
- Quét toàn bộ phần tử click được (thanh hành động + accordion) + tìm nguyên văn "Gửi thông báo kết quả"/"Gửi thông báo" trong innerText toàn trang → **không tồn tại** (`hasPartnerLabel=false`) ở cả 2 trạng thái.
- Ảnh: `image/TBKQTNHS_01-khong-co-nut-gui-thongbao.png`.

### Chưa xác minh được (cần DN account / BA)

- Nếu đặc tả chốt là **auto** (`:1758`): cần xác minh **thông báo kết quả có THỰC SỰ tự gửi tới DN** khi chuyển trạng thái không. Recipient là **doanh nghiệp** → cần tài khoản DN để kiểm hộp thư (không có sẵn trong bộ tài khoản test). Lưu ý rủi ro cao: cùng module này đã xác nhận **4 bug thông báo KHÔNG được gửi** ở các transition khác (BUG-TPDHSVV_04, BUG-PDHSVV_05, BUG-PDHSVV_02, BUG-XNTGHTVV_04) → nếu auto-send cũng hỏng thì đây là lỗi chức năng thật (không chỉ là chuyện nút). → Đề nghị BA/dev xác minh phần auto-send tới DN.

## Verdict

**`BA confirm`** — Đối tác báo đúng hiện tượng (không có nút "Gửi thông báo kết quả"), nhưng đây là **mâu thuẫn nội tại trong đặc tả**: §Màn hình `:905` + quy tắc màn hình `:1758` quy định thông báo kết quả là **tự động (không nút)**, còn AC `:947` lại ghi **"nhấn Gửi Thông báo"** (có nút). App (không nút) khớp cách hiểu auto → **không thể tự kết luận Open hay Reject**. → BA chốt: thông báo kết quả kiểm tra là **tự động** (không cần nút — app đúng, sửa AC `:947`) hay **thủ công** (cần bổ sung nút — app thiếu). **Kèm yêu cầu:** nếu chốt "auto", BA/dev xác minh DN có thực nhận thông báo tự động không (chưa test được vì thiếu tài khoản DN; module này đã có 4 bug thông báo không gửi). Ghi mục [`../../ba-confirm/vu-viec/ba-confirmation-needed-vu-viec.md`](../../ba-confirm/vu-viec/ba-confirmation-needed-vu-viec.md).
