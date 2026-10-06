# QLNDTVVCG_19 — Nhóm 4 Đánh giá chất lượng (sheet `bug` row 285)

**Đợt:** re-verify trên MÔI TRƯỜNG NGHIỆM THU `https://htpldn-uat.ospgroup.vn`
**Ngày đo:** 2026-08-07
**Bản dựng:** V1.0.10 · bó mã `index-Bd1akG3f.js` (đọc trực tiếp trong tab trước khi đo)
**Tài khoản:** `cbnv_tw` — Cán bộ Nghiệp vụ Trung ương, BTP·TW, phạm vi Toàn quốc
**Trạng thái sheet trước đo:** `Trạng thái dev fix` = `Test done`

## Verdict: 🚫 KHÔNG KẾT LUẬN ĐƯỢC — blocker khách quan (nhóm D: tích hợp ngoài không khả dụng trên env)

**KHÔNG ghi Pass, KHÔNG ghi Reopen.** Ô `Trạng thái dev fix` giữ nguyên `Test done`.

## Đã đo được (đạt)

- Màn Chi tiết tư vấn chuyên sâu CÓ khối "Đánh giá chất lượng", nằm **thứ 4** trong dãy khối:
  `Thông tin cơ bản → Nội dung tư vấn → Tư liệu pháp lý liên kết → Đánh giá chất lượng → Nhật ký thao tác → Công khai chuyên trang`.
  Khớp thứ tự accordion tại `srs-fr-12-tv-chuyen-sau.md:1160`.
- Khối mở ra được, hiển thị **empty state hợp lệ**: "Chưa có đánh giá chất lượng." kèm hình minh hoạ trống.
  KHÔNG phải "Chức năng đang phát triển" → không phải lỗi UI chưa build.
- Trong khối không có phần tử nhập/ghi nào (0 input/textarea/select/button/link) — nhất quán với
  `srs-fr-12-tv-chuyen-sau.md:1006` "Không có màn hình CMS (API inbound từ Cổng PLQG)".

Bằng chứng: [image/QLNDTVVCG_19-khoi-danhgia-rong-uat.png](../image/QLNDTVVCG_19-khoi-danhgia-rong-uat.png)

## KHÔNG đo được — vì sao

Yêu cầu của phiếu gồm 4 cột (Mã đánh giá / Điểm 1-5 / Nhận xét DN / Ngày đánh giá) và dòng tổng hợp
(điểm trung bình + số lượng). Bảng chỉ render khi có ≥1 đánh giá. **Toàn env nghiệm thu không có bản ghi nào
có đánh giá.**

Đã quét **56/56** bản ghi tư vấn chuyên sâu (đủ 3 thẻ: Chờ xử lý 38 + Đang tư vấn 5 + Hoàn thành 13),
gọi `GET /api/v1/danh-gia-chat-luong-tvs?noiDungTvId=<id>` cho từng bản ghi → **0 bản ghi có đánh giá**.

## Bảng cạn kiệt — mọi đường tạo dữ liệu đánh giá đã thử

| # | Đường tạo | Endpoint / màn | Yêu cầu xác thực | Kết quả thử thật |
|---|---|---|---|---|
| 1 | Webhook Cổng PLQG | `POST /api/v1/danh-gia-chat-luong-tvs/inbound` | mTLS (X-Client-Verify) + OAuth2 scope `inbound:danh-gia:write` | **401 `ERR-AUTH-MTLS-01`** — "mTLS client certificate verification failed" |
| 2 | Chuyên trang doanh nghiệp | `POST /api/v1/public/me/tu-van-chuyen-saus/{id}/danh-gia` | mTLS + OAuth2 scope `htpldn:tvcs:write` | **401 từ nginx** — chặn ở tầng biên, trước routing |
| 3 | Màn CMS bất kỳ | — | — | **Không tồn tại.** `srs-fr-12-tv-chuyen-sau.md:1006`: "Không có màn hình CMS (API inbound từ Cổng PLQG)" |

Đã liệt kê TOÀN BỘ đường ghi đánh giá TVCS trong `/api/docs-json`: đúng 2 endpoint ở hàng 1–2, cả hai đều
sau mTLS. QA không được cấp chứng thư client trên env này → **tiền đề không thể tự tạo**, không phải "lười seed".

## Đối chiếu SRS

| SRS yêu cầu | Dẫn nguồn | Thực tế env nghiệm thu |
|---|---|---|
| Accordion "Đánh giá chất lượng", bảng read-only, cột: Mã đánh giá / Điểm (1-5 sao) / Nhận xét DN / Ngày; tổng hợp: Điểm TB + Số lượng | `srs-fr-12-tv-chuyen-sau.md:1172` | Khối có · bảng **chưa quan sát được** (không có dữ liệu) |
| Dữ liệu chỉ vào qua API inbound Cổng PLQG, không có màn CMS | `srs-fr-12-tv-chuyen-sau.md:1006` · `:1172` | Khớp — không có đường nhập trong CMS |
| Thứ tự accordion | `srs-fr-12-tv-chuyen-sau.md:1160` | Khớp (vị trí 4/6) |

UC: `srs-fr-12-tv-chuyen-sau.md:1002` — **UC 153** (FR-X.1-07).

## Cần gì để đóng phiếu

Bên phát triển nạp sẵn **≥2 đánh giá có điểm khác nhau** (để dòng "điểm trung bình" có tính phân biệt) cho
ít nhất 1 hồ sơ tư vấn chuyên sâu ở trạng thái Đã duyệt trên env nghiệm thu — đúng như đã làm trên env nội bộ
(hồ sơ `TVCS-QLND19-UAT`). Có dữ liệu là đo được ngay trong 1 lượt.

## Ngoài phiếu này, có thấy gì bất thường không?

Không phát hiện thêm. Console sạch trong suốt lượt đo; empty state đúng chuẩn.

> **Ghi nhận về phiên đăng nhập (không phải lỗi của phiếu):** env nghiệm thu rớt phiên rất nhanh, thao tác
> tải lại trang bằng địa chỉ trực tiếp là bị đá về màn đăng nhập. Đã xử lý bằng cách điều hướng trong ứng dụng
> thay vì tải lại trang.
