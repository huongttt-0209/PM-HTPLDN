# Bảng đối chiếu điều kiện — TDHSTVV_13 (Gửi kết quả thẩm định, kết luận "Yêu cầu bổ sung")

Evidence đối tác: `partner-evidence/TDHSTVV_13.webm` — frame 00:45: hồ sơ `TVV-BTP-TW-0011` ("Lê Văn Chuyên Gia (R32 NHT edit)") **đã chuyển sang trạng thái "Yêu cầu bổ sung"** (nghiệp vụ chạy được), đối tác mở bảng Thông báo để kiểm tra. Khiếu nại của đối tác trong sheet chỉ có **1 ý**: "Hệ thống không hiển thị thông báo".

| Điều kiện | Đối tác (từ evidence full-res) | Mình test | GAP? |
|---|---|---|---|
| Vai trò / tài khoản | CB Nghiệp vụ Trung ương — CB_NV_TW, đơn vị BTP · TW | CB Nghiệp vụ Trung ương — `cbnv_tw`, CB_NV_TW, đơn vị BTP · TW (trùng khớp) | Không |
| Entity + trạng thái | Hồ sơ TVV `TVV-BTP-TW-0011`, trạng thái trước thao tác = "Đang thẩm định" (sau thao tác chuyển "Yêu cầu bổ sung") | Hồ sơ TVV `TVV-BTP-TW-0003`, trạng thái trước thao tác = "Đang thẩm định" (đã seed), sau thao tác chuyển "Yêu cầu bổ sung" | Không |
| Dữ liệu tiền đề | Biểu mẫu thẩm định đã điền, Kết luận Pháp lý đã chọn | Biểu mẫu đã điền: Kết luận Pháp lý = Đạt, điểm Nhóm 2/3 = 3, Lý do yêu cầu bổ sung 82 ký tự (> mức tối thiểu 10) | Không |
| Input / thao tác | Chọn Kết luận thẩm định = "YÊU CẦU BỔ SUNG" → bấm "Gửi KQ" | Chọn Kết luận thẩm định = "YÊU CẦU BỔ SUNG" → nhập Lý do → bấm "Gửi KQ" (cùng nút, cùng màn) | Không |

Kết luận: **0 GAP** — đúng vai trò CB_NV_TW, đúng trạng thái "Đang thẩm định" trước thao tác, đúng kết luận "Yêu cầu bổ sung" của đối tác.

## Quan sát (artifact real-data — loại claim "absence": phải hiện thông báo nhưng không hiện)

- MutationObserver cài **trước** cú bấm "Gửi KQ", theo dõi 4 giây: `addedNodes = 0`.
- Không có `.ant-message-notice-wrapper` / `.ant-message-notice` / `.ant-notification-notice` nào trên trang.
- Network: `POST /api/v1/tu-van-viens/{id}/tham-dinh` → **200 OK**; dữ liệu gửi lên: `{"ketLuan":"YEU_CAU_BO_SUNG","lyDo":"Ho so thieu ban sao the hanh nghe cong chung...","version":3,...}`.
- Phản hồi máy chủ: `trangThai` chuyển `DANG_THAM_DINH` → **`YEU_CAU_BO_SUNG`**; bản ghi thẩm định lưu đúng `ketLuan` + `lyDo`.
- ⇒ **Nghiệp vụ chạy ĐÚNG** (đổi trạng thái + lưu lý do), **chỉ thiếu thông báo phản hồi cho người dùng** — đúng y khiếu nại của đối tác.
- Ảnh: `bug-reports/image/BUG-TDHSTVV_13-web-sau-gui-ket-qua-doi-trang-thai-nhung-khong-toast.png` — huy hiệu trạng thái đã là "Yêu cầu bổ sung", không có thông báo nào trên màn.

## Đối chiếu SRS (Cổng 3)

- `srs-v3.5.md` dòng 571 — **UI-04 (Đặc điểm logic UI, áp dụng toàn hệ thống)**: "Kiểm tra thời gian thực + viền đỏ + thông báo lỗi dưới ô nhập. Popup xác nhận trước xóa. **Toast notification cho thao tác thành công**". → Web: thao tác thành công nhưng **không có toast**. **KHÔNG khớp.**
- `srs-fr-04-chuyen-gia-tvv.md` dòng 1564 (ô 20c) — nút "Gửi kết quả thẩm định": "nếu 'Yêu cầu bổ sung' → đặt trạng thái Yêu cầu bổ sung + thông báo chủ hồ sơ". → Web: đổi trạng thái **đúng**. Khớp phần trạng thái.
- Lưu ý cho BA/dev: câu chữ toast đối tác kỳ vọng ("Đã gửi yêu cầu bổ sung đến Người hỗ trợ") **không có trong SRS**, và SRS dòng 519 + 1564 quy định thông báo gửi cho **chủ hồ sơ (TVV/CG)** chứ không phải "Người hỗ trợ". Vì vậy bug chỉ nêu **yêu cầu phải có thông báo thành công** (UI-04), **không** áp đặt câu chữ cụ thể.

---

## Re-verify 2026-07-15 (sau dev fix — vòng 2)

Re-test đúng vai trò/state/data bug gốc: **CB_NV_TW `cbnv_tw`, BTP·TW**, hồ sơ **TVV-BTP-TW-0009** trạng thái "Đang thẩm định", tab Thẩm định. Chọn Kết luận Pháp lý=Đạt, Kết luận thẩm định=**YÊU CẦU BỔ SUNG**, nhập Lý do (≥10 ký tự) → bấm "Gửi KQ".

**Kết quả FIXED (MutationObserver cài trước click):**
- Toast thành công **"Đã lưu kết quả thẩm định"** hiện ngay sau click (buffer observer đã reset trước thao tác ⇒ toast là của chính lần Gửi KQ này).
- Hồ sơ chuyển trạng thái **"Yêu cầu bổ sung"** (nghiệp vụ chạy đúng).

⇒ Thao tác thành công nay CÓ thông báo phản hồi (UI-04). **PASS.** Ảnh: `bug-reports/image/TDHSTVV_13-reverify-guikq-ycbs-doi-trang-thai.png`.
