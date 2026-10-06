# Audit verify vòng 2 — QLTVV_02 (row 36, tab tuần 2)

**Verdict tổng:** `Open` · **Bug ID:** `BUG-QLTVV_02` · **Ngày:** 2026-07-27
**Bảng đối chiếu điều kiện (0 GAP):** [`../../cond/QLTVV_02-r2.md`](../../cond/QLTVV_02-r2.md)

> Verdict tổng `Open` theo QA_VERIFY_PROTOCOL §"1 case gộp nhiều lỗi con" (≥1 ý Open).
> **Lưu ý đọc kỹ:** 3 ý đối tác nêu **KHÔNG tái hiện** trên bản hiện tại của env test; ý `Open` là **lỗi khác** phát hiện khi soi đúng cột Hành động mà họ phản ánh.

## Cổng 1 — bằng chứng đối tác

| Mục | Nội dung |
|---|---|
| File | `QLTVV_02_v2.png` (305.550 byte, ảnh tĩnh) |
| Nội dung lỗi thấy trong ảnh | (1) 2 dòng có điểm: "★★★★ 3.7/5" và "★★★★★ 8.3/5" nằm sát/chồng lên chữ "Đang hoạt động" của cột Trạng thái (đối tác khoanh đỏ) · (2) dòng chưa có điểm chỉ hiện "—/5" **không có sao**, dòng có điểm mới hiện sao · (3) cột Hành động hẹp, chữ vỡ giữa từ: "Xe/m", "Sử/a", "Xóa" (đối tác khoanh đỏ) |
| Dữ kiện neo | (a) `htpldn-uat.ospgroup.vn/chuyen-gia-tvv/danh-sach` · (b) tab "Đang hoạt động", 1-10 / 10 mục, bảng đang cuộn ngang · (c) vai trò CB_NV_TW, BTP·TW · (d) 2026-07-25 11:28 |

## Verdict từng ý

| # | Ý đối tác nêu | Kết quả verify | Verdict ý |
|:-:|---|---|---|
| 1 | Điểm ĐG tràn/đè lên cột Trạng thái | **Không tái hiện** ở cả 1920 / 1440 / 1280 với dữ liệu đã seed cho khớp. Nội dung ô Điểm ĐG luôn nằm **trong** ô, cách mép phải ô 26–42 px, không chạm biên trái cột Trạng thái | Không tái hiện |
| 2 | Hiển thị không đồng nhất (chưa có điểm: "-/5"; có điểm: số sao) | **Không tái hiện** — bản hiện tại hiện **5 sao ở CẢ HAI** trạng thái: chưa có điểm = 5 sao xám + "—/5"; có điểm = sao vàng theo mức + "4.2/5". Đúng `srs-fr-04-chuyen-gia-tvv.md:1447` | Không tái hiện |
| 3 | Nút Xem, Sửa bị xuống dòng | **Không tái hiện** — cột Hành động rộng 160–165 px ở mọi mức đo, 3 nút nằm trên 1 dòng (Xem 28,2 px · Sửa 24,3 px · Xóa 29,6 px), không có nút nào cao quá 1 dòng chữ | Không tái hiện |
| 4 | *(phát hiện khi soi đúng cột Hành động — không phải ý đối tác nêu)* | Cột Hành động đang là **liên kết chữ** "Xem / Sửa / Xóa" (`<a>Xem</a><a>Sửa</a><button>Xóa</button>`), trong khi `srs-fr-04-chuyen-gia-tvv.md:1450` quy định cột này là **"nhóm icon"** — Icon Xem (mắt) · Icon Sửa (bút chì) · Icon Xóa (thùng rác) | **`Open`** |

## Cổng 3 — đối chiếu SRS vs thực tế web (loại bug: Hiển thị)

| SRS yêu cầu (dẫn line) | Thực tế web | Đủ/Thiếu |
|---|---|---|
| `srs-fr-04-chuyen-gia-tvv.md:1447` — SCR-IV-01 dòng 24: Điểm đánh giá = "số + sao. Ví dụ: '4.5/5' + 5 sao. Nếu chưa có đánh giá: hiển thị '—/5'" | Có điểm → 5 sao (tô theo mức) + "4.2/5"; chưa có điểm → 5 sao xám + "—/5" | **Đủ** |
| `srs-fr-04-chuyen-gia-tvv.md:1450` — SCR-IV-01 dòng 27: Hành động = "**nhóm icon**": Icon Xem (mắt) → SCR-IV-03; Icon Sửa (bút chì) → SCR-IV-02 (ẩn nếu trạng thái Vô hiệu hóa); Icon Xóa (thùng rác) | 3 **liên kết chữ** "Xem" / "Sửa" / "Xóa", không có icon nào | **Thiếu** |
| `srs-fr-04-chuyen-gia-tvv.md:190` + `:259` — `diem_danh_gia_tb` phạm vi **1.0–5.0** (1 chữ số thập phân); `:740` ERR-DG-01 "Điểm đánh giá phải từ 1 đến 5" | Env test: `diemDanhGiaTb = 4.2` — trong thang. **Ảnh đối tác: 8.3/5** — ngoài thang (xem mục "Ngoài tiêu chí BA") | Env test **Đủ** — env đối tác **Thiếu** |

## Phép đo đã chạy (artifact QUAN SÁT trên data thật)

| # | Phép đo | Kết quả | Artifact |
|---|---|---|---|
| 1 | Seed cho khớp mật độ dữ liệu đối tác: `PATCH /api/v1/tu-van-viens/{id}` đặt 4 lĩnh vực + tổ chức tên dài cho 2 bản ghi | Bảng hiện "Đất đai · Lao động · Thuế +1" (2 dòng thẻ) + "Công ty Luật TNHH Demo Kiểm Thử" — giống mật độ ảnh đối tác. (Bản ghi thứ 3 trả 403 `ERR-AUTH-VPD-00-03` "khác đơn vị" — đúng phân quyền, không phải lỗi) | — |
| 2 | Đo hình học ô Điểm ĐG ở **1920** (vùng nội dung 1593 px ≈ 1580 px của đối tác) | Ô rộng 186 px; mép phải nội dung 1262,1 vs mép phải ô 1294,5 ⇒ **thừa 32,4 px trong ô**; biên trái cột Trạng thái 1294,5 ⇒ **không chạm** | `QLTVV_02-r2-bang-1920-du-lieu-day.png` |
| 3 | Lặp ở **1440** (bảng đã có cuộn ngang: scrollWidth 1542 > clientWidth 1113 — giống ảnh đối tác) | Thừa 26,5 px trong ô, không đè cột Trạng thái; cột Hành động 160 px, 3 nút 1 dòng | — |
| 4 | Lặp ở **1280**, cuộn hết sang phải để nhìn đúng vùng đối tác chụp | Thừa 26,5 px trong ô, không đè; cột Hành động 160 px; "Xem/Sửa/Xóa" mỗi nút cao 16,5–24 px = 1 dòng | `QLTVV_02-r2-bang-1280-cuon-het-phai.png` |
| 5 | Đọc DOM cột Hành động | `<a>Xem</a><a>Sửa</a><button><span>Xóa</span></button>` — **không có phần tử icon nào** | — |
| 6 | Kiểm thang điểm thực tế của bản ghi có điểm | `GET /api/v1/tu-van-viens/{id}/danh-gia` → 2 lượt đánh giá (5/4 và 4/4), `diemDanhGiaTb = 4.2` ⇒ env test tính đúng thang 1–5 | — |

**Vì sao 3 ý đối tác KHÔNG được đánh `Reject`:** đối tác có ảnh lỗi thật, và không chứng minh được họ thao tác hay hiểu sai —
đây là chênh lệch **bản dựng/môi trường** (ảnh của họ chụp trên `htpldn-uat.ospgroup.vn`, bản có cột Hành động hẹp hơn và
không vẽ sao cho dòng chưa có điểm). Theo QA_VERIFY_PROTOCOL §Verdict, trường hợp "không tái hiện + đối tác CÓ bằng chứng"
phải ghi `Resolved`, **KHÔNG** `Reject`. Cột `Trạng thái dev fix 2` (W) không có giá trị `Resolved` trong dropdown, nên phần
"đã kiểm lại, không còn thấy trên bản hiện tại" được ghi rõ bằng lời trong note cột X.

## Ngoài tiêu chí BA — có thấy gì bất thường không?

**Có 2 điểm:**

1. **Cột Hành động là chữ, không phải icon** (đã đưa thành ý `Open` số 4 ở trên) — cùng phần mềm, màn danh sách
   Giảng viên / Trợ giảng lại dùng icon 👁 đúng kiểu. Nếu cột này làm đúng đặc tả (3 icon) thì hiện tượng "nút xuống dòng"
   mà đối tác phản ánh cũng khó xảy ra, vì icon chiếm ít chỗ hơn chữ rất nhiều.

2. **"8.3/5" trong ảnh đối tác là số NGOÀI thang** — `srs-fr-04-chuyen-gia-tvv.md:190`/`:259` chốt `diem_danh_gia_tb` ∈ 1.0–5.0
   và `:740` có lỗi ERR-DG-01 "Điểm đánh giá phải từ 1 đến 5". Đây đúng là phần còn sót của bug vòng 1 (số thô thang /10 gắn nhãn "/5").
   **Không log thành bug riêng** vì trên env test số liệu đã đúng thang (4.2, khớp với 2 lượt đánh giá thành phần) — không tái hiện được.
   Đã nêu trong note để dev soát lại dữ liệu cũ trên env của đối tác.

## Ghi chú nội bộ (KHÔNG đưa vào note sheet)

- **Dữ liệu seed đã trả về nguyên trạng:** 2 bản ghi (`98cfd963-…` và `5eed0003-…`) đã PATCH về `linhVucIds=['bbbbbbbb-…-001c']`
  và `toChucChinhId` cũ (`5eed0004-…-001` / `null`), xác nhận bằng phép đọc lại — không để lại rác dữ liệu.
- **Khác biệt bản dựng là giả thuyết mạnh nhất** cho cả 3 ý: ảnh đối tác cho thấy cột Hành động hẹp tới mức vỡ chữ giữa từ,
  trong khi bản hiện tại đặt chiều rộng tối thiểu cho bảng (scrollWidth cố định 1542 px) nên cột không co dưới 160 px ở bất kỳ
  chiều rộng cửa sổ nào đã thử. Không có cách xác minh phiên bản build từ giao diện (cả 2 đều ghi "HTPLDN · V1.0").
- **Bug ID trùng tên với vòng 1:** vòng 1 đã có `BUG-QLTVV_02` (cột Loại hiện mã viết tắt + Điểm ĐG thang /10) — đã đóng, Verify=Pass.
  Entry lần này giữ đúng quy ước `BUG-<mã TC>` nhưng là **nội dung khác** (cột Hành động không phải icon); đã ghi rõ trong entry.
