# Bảng đối chiếu điều kiện — CPCTHTTTG_03 (re-verify vòng 2, 04/08/2026)

Loại bug: **hiển thị phụ thuộc dữ liệu (nhãn trục tung biểu đồ đường)** → bắt buộc điền bảng, 0 GAP.
Re-verify chạy **trên chính môi trường đối tác** `https://htpldn-uat.ospgroup.vn`.

| Điều kiện | Đối tác (từ evidence full-res `CPCTHTTTG_03.jpg`) | Mình test | GAP? |
|---|---|---|---|
| Môi trường | `htpldn-uat.ospgroup.vn` | `htpldn-uat.ospgroup.vn` — cùng môi trường, bản dựng HTPLDN **V1.0.5** | Không |
| Vai trò / phạm vi dữ liệu | Quản trị viên · QTHT, đơn vị BTP · TW | `cbnv_tw` (CB_NV_TW) — đúng Tác nhân của FR-IX-19; đơn vị BTP · TW, phạm vi Toàn quốc | Không |
| Bộ lọc (loại BC · kỳ · đơn vị) | BC Chi phí theo thời gian · Kỳ Năm · 01/01/2026 → 31/12/2026 · Toàn quốc | Y hệt — URL `?loai=chi-phi-theo-thoi-gian&kyBaoCao=NAM&tuNgay=2026-01-01&denNgay=2026-12-31`, Đơn vị Toàn quốc | Không |
| Dữ liệu tiền đề (thang tiền sinh vạch chia trục tung) | Tổng chi phí toàn kỳ **226.308.268** · **25** hồ sơ | **226.308.268** · **25** hồ sơ — **trùng khít từng con số** với ảnh đối tác | Không |

**Kết luận: 0 GAP** — cùng môi trường, cùng bộ lọc, cùng bộ số liệu, vai trò đúng Tác nhân đặc tả.

## Đo lường trực tiếp (04/08/2026 15:54, `htpldn-uat.ospgroup.vn`, build V1.0.5)

So sánh *ảnh đối tác 16/07/2026* → *hôm nay*:

- **Nhãn trục tung trái (Tổng chi phí):** 5 vạch chia **đều in `000.000`**, không đọc được giá trị nào
  → `0 · 60 triệu · 120 triệu · 180 triệu · 240 triệu`, **đọc được đầy đủ**.
- **Trục tung phải (Số hồ sơ):** **không có** — Số hồ sơ vẽ chung thang tiền nên bị nén sát đáy 0
  → `0 · 7 · 14 · 21 · 28`, **trục phụ riêng**, điểm Số hồ sơ nằm đúng mốc 25.
- **Điểm Tổng chi phí:** ở đỉnh, không đối chiếu được vạch chia nào → ngay dưới mốc 240 triệu, khớp 226.308.268.
- **KPI:** Tổng chi phí 226.308.268 · Tổng hồ sơ 25 → y hệt.
- **Bảng tổng hợp:** Năm 2026 · 01/01–31/12 · 25 · 226.308.268 đ → y hệt.

- `Thời điểm tạo: 04/08/2026 15:54` → báo cáo tạo mới, không phải bản cache cũ.
- Đối chiếu chéo cùng ngày trên môi trường nội bộ `18.143.165.120.nip.io` (cũng V1.0.5, số liệu 23.000.000 · 2 hồ sơ):
  trục trái `0 · 6 · 12 · 18 · 24 triệu`, trục phải `0 · 1 · 2 · 3 · 4` → cùng hành vi, fix không phụ thuộc thang số.

**Đối chiếu 2 ý BA nêu:**

1. *"Nội dung biểu đồ — SRS docx outdate, sẽ gửi bản cập nhật"* → biểu đồ nay tách trục phụ cho Số hồ sơ nên
   cả 2 chỉ tiêu đều đọc được; "Kết quả mong đợi" của phiếu (biểu đồ đường xu hướng chi phí + bảng tổng hợp
   Kỳ / Tổng chi phí / Số hồ sơ) đã được đáp ứng đủ.
2. *"Nhãn trục tung hiển thị không đọc được — ghi nhận là lỗi, sẽ khắc phục"* → **đã khắc phục**, hết chuỗi `000.000`.

**Verdict vòng 2: `Pass`** (cột `Verify 2`) — cả 2 ý đều hết lỗi, đo trên đúng môi trường + đúng bộ số liệu của đối tác.

## Ghi chú môi trường (không phải lỗi của case này)

`htpldn-uat.ospgroup.vn` **rớt phiên đăng nhập rất nhanh** — vài lần đang thao tác thì bị đá về `/login`,
và `fetch` gọi API ngay sau khi trang đã render trả `401`. Không cần OTP khi đăng nhập (khác env nội bộ).
Đã lấy trọn bằng chứng UI trong lúc phiên còn hiệu lực; verdict căn cứ UI theo §Nguyên tắc 2.
