# Re-verify QLDX_03 — Tự động đăng xuất khi hết phiên

**Ngày chạy:** 10/08/2026 (03:28–03:43 UTC)
**Môi trường:** https://htpldn-uat.ospgroup.vn — build **HTPLDN · V1.0.10**
**Tài khoản:** `cbnv_tw` / CB Nghiệp vụ Trung ương (OTP lấy tại MailHog của chính env)
**Nguồn sheet:** `1OKBN2otlmdZ44THkmhtsn-_63M2Boh7zQwearwjYR3s`, tab `bug` (gid 1714340219), **dòng 163**
**Trạng thái dòng trước khi verify:** `Trạng thái = Fail` · `Trạng thái dev fix = BA confirm` · `Kết quả verify` đang TRỐNG

## Verdict: ✅ Pass — không còn tái hiện

Không tái hiện được **cả hai** vế:
- Claim gốc (15/07): "hệ thống không hiển thị hộp thoại cảnh báo dù không thao tác suốt 30 phút".
- TKM retest (31/07): "không hiện hộp thoại xác nhận mà chuyển thẳng màn Đăng nhập + *Đăng xuất thành công*".

## Đối chiếu SRS

| Nguồn | Nội dung | App V1.0.10 |
|---|---|---|
| `srs-v3.5/srs-fr-10-quan-tri.md:1959` | "Dang xuat tu dong: 25 phut idle → Modal canh bao → 30 phut → Auto invalidate → Redirect MH-10.8b" | Khớp |
| `srs-v3.5/srs-fr-10-quan-tri.md:1020` | "Given user không thao tác quá 30 phút When hết timeout Then tự động đăng xuất" | Khớp |
| `srs-v3.5/srs-fr-10-quan-tri.md:1011` | message = "Đăng xuất thành công" / "Phiên hết hạn" | Khớp bản chất (chi tiết ở mục Quan sát thêm) |
| `srs-v3.5/srs-fr-10-quan-tri.md:2369` (BR-AUTH-06) | Session CMS 30 phút idle timeout | Khớp |

## Kết quả đo

| # | Điểm kiểm | Kết quả | Bằng chứng |
|---|---|---|---|
| 1 | Modal cảnh báo bật đúng mốc 25 phút | Mẫu cuối **không** hiện ở `idleSec = 1500`; mẫu đầu **có** hiện ở `idleSec = 1501` | ảnh `QLDX_03-modal-canh-bao-25p-2026-08-10.png` |
| 2 | Modal có đúng 2 lựa chọn theo phiếu | Tiêu đề "Phiên làm việc sắp hết hạn" + nút **"Gia hạn phiên"** / **"Đăng xuất"** + đếm ngược thật ("tự đăng xuất sau 4:20", chạy từng giây) | ảnh mục 1 |
| 3 | "Gia hạn phiên" có tác dụng thật | Bấm → modal đóng (`width>0`+`display` đều tắt), idle reset về 6s, `GET /api/v1/auth/me` → **200** | log phiên |
| 4 | Tự đăng xuất đúng mốc 30 phút | Mẫu cuối trên `/dashboard` ở `idleSec = 1800` rồi chuyển `/login` | ảnh `QLDX_03-tu-dang-xuat-30p-2026-08-10.png` |
| 5 | Thông báo sau khi hết phiên | **"Phiên làm việc đã hết hạn do không có thao tác"** (kiểu info) — **KHÔNG** phải "Đăng xuất thành công" | snapshot a11y bắt live (`alert` + `info-circle`); ảnh `QLDX_03-thong-bao-het-phien-2026-08-10.png` |
| 6 | Lý do app tự ghi ra khi hết phiên | Bắt được `logout-notice = idle` (không phải `user`) — đo 2 lượt độc lập | patch `Storage.setItem` |
| 7 | Phiên có bị hủy thật phía server không | `GET /api/v1/auth/me` sau khi tự đăng xuất → **401** `ERR-AUTH-SYS-00-01`; `auth-store` = null | log phiên |
| 8 | Áp dụng cho phiên "Ghi nhớ đăng nhập" | Đăng nhập có tick "Ghi nhớ đăng nhập" → vẫn bật modal ở `idleSec = 1501` | log phiên |

## 3 chốt chống Pass oan

1. **Mốc idle không bị request nền ghi đè** — đo im lặng 188 giây / 378 mẫu: `auth-last-activity` giữ đúng **1 giá trị duy nhất**, bộ đếm idle tăng đều 34s → 223s. Nếu mốc bị request nền ghi đè thì người dùng thật sẽ chẳng bao giờ thấy modal, và Pass sẽ là Pass oan.
2. **Kẹp hai đầu ngưỡng** — 24:50 không bật, 25:01 tự bật (không có thao tác nào chen giữa) → chứng minh có timer nền chạy thật, không phải modal chỉ phản ứng theo thao tác.
3. **Loại trừ rớt mạng** — watchdog `curl` 25s/lần: **32/32 lần HTTP 200** liên tục 03:29:26–03:42:24, phủ kín toàn bộ khoảng đo.

## Khai rõ về cách rút ngắn thời gian chờ

Không ngồi chờ đủ 25/30 phút. Cách làm: đặt lại mốc `auth-last-activity` — đúng mốc mà FE đọc để đo idle —
rồi để **đồng hồ thật** chạy qua ngưỡng. Nhánh 30 phút có 1 lượt chạy đồng hồ thật hoàn toàn (đặt 29:50,
để thật chạy tiếp 10 giây tới đúng 30:00). Ba chốt ở trên là để bù cho việc rút ngắn này.

Riêng ảnh `QLDX_03-thong-bao-het-phien-*.png`: lần chạy thật, thông báo tự tắt trước khi kịp chụp, nên
**bằng chứng live của lần chạy thật là snapshot a11y** (node `alert` + icon `info-circle` + đúng nguyên văn
câu thông báo). Ảnh đính kèm là lần **dựng lại khâu hiển thị** — đặt lại đúng giá trị `logout-notice=idle`
mà app đã ghi ra ở lần chạy thật rồi tải lại trang đăng nhập.

## Quan sát thêm (không log thành bug)

- SRS dòng 1011 ghi message là `"Đăng xuất thành công" / "Phiên hết hạn"`; app dùng câu dài hơn
  **"Phiên làm việc đã hết hạn do không có thao tác"** cho nhánh hết phiên do idle. Đúng bản chất mà SRS
  yêu cầu (phân biệt hết-hạn với đăng-xuất-chủ-động), chỉ khác câu chữ → không đủ căn cứ log bug.
- App phân biệt 3 nhánh thông báo: `user` → "Đăng xuất thành công"; `idle` → "Phiên làm việc đã hết hạn
  do không có thao tác"; `expired` (401 từ server) → "Phiên làm việc hết hạn". Đây chính là phần TKM báo
  sai ở vòng 31/07 và nay đã đúng.
- Ngoài bug này, không thấy bất thường nào khác trên các màn đã đi qua.

## Bằng chứng

- [evidence/QLDX_03-modal-canh-bao-25p-2026-08-10.png](evidence/QLDX_03-modal-canh-bao-25p-2026-08-10.png)
- [evidence/QLDX_03-tu-dang-xuat-30p-2026-08-10.png](evidence/QLDX_03-tu-dang-xuat-30p-2026-08-10.png)
- [evidence/QLDX_03-thong-bao-het-phien-2026-08-10.png](evidence/QLDX_03-thong-bao-het-phien-2026-08-10.png)
- [evidence/QLDX_03-canh-mang-2026-08-10.log](evidence/QLDX_03-canh-mang-2026-08-10.log)
- [cond/QLDX_03.md](cond/QLDX_03.md) — bảng đối chiếu điều kiện
