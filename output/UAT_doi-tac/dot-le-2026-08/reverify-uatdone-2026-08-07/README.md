# Re-verify bug dev đã fix — MÔI TRƯỜNG NGHIỆM THU (2026-08-07)

**Env đo:** `https://htpldn-uat.ospgroup.vn` · bản dựng **V1.0.10** · bó mã chính `index-Bd1akG3f.js`
**Sheet:** `1OKBN2otlmdZ44THkmhtsn-_63M2Boh7zQwearwjYR3s` · tab **`bug`**
**Nguồn đặc tả:** `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/`
**Quy tắc ghi sheet:** Pass → `Trạng thái dev fix` = `UAT done` · Reopen → `Reopen` + diễn giải vào `Kết quả verify`.
Các ô `Trạng thái` / `Kết quả thực tế` / `TKM phản hồi lần 1` / `DEV phản hồi lần 1` **chỉ đọc — không đụng tới**.

## Cổng lọc đầu vào

Yêu cầu: chỉ chạy case đang ở `Trạng thái dev fix` = **`Test done`**. Đọc sheet trước khi chạy:

| Tình trạng trước khi chạy | Số case | Xử lý |
|---|:-:|---|
| Đã là `UAT done` từ đợt trước | 8 | **Bỏ qua**, không đo lại |
| Đang là `Test done` | **5** | **Chạy verify** |

Case bỏ qua: `QLNDTVVCG_26` · `QLHSPLDN_06` · `QLHSPLDN_07` · `QLHSPLDN_11` · `QLHSPLDN_12` · `QLHSPLDN_13`
· `QLHSPLDN_14` · `QLTLPLCVV_17`.

## Kết quả 5 case đã chạy

| # | Mã TC | Dòng | Kết luận | Sheet sau khi ghi | Báo cáo |
|:-:|---|:-:|---|---|---|
| 1 | QLNDTVVCG_19 | 285 | 🚫 **Không kết luận được** — blocker khách quan | **giữ `Test done`** | [cases/QLNDTVVCG_19.md](cases/QLNDTVVCG_19.md) |
| 2 | QLTLPLCVV_15 | 299 | ✅ **PASS** | `UAT done` | [cases/QLTLPLCVV_15.md](cases/QLTLPLCVV_15.md) |
| 3 | QLKCHTV_37 | 305 | ✅ **PASS** | `UAT done` | [cases/QLKCHTV_37.md](cases/QLKCHTV_37.md) |
| 4 | LBCKQTHCT_03 | 336 | ✅ **PASS** | `UAT done` | [cases/LBCKQTHCT_03.md](cases/LBCKQTHCT_03.md) |
| 5 | LBCKQTHCT_04 | 337 | ✅ **PASS** | `UAT done` | [cases/LBCKQTHCT_04.md](cases/LBCKQTHCT_04.md) |

**4 PASS · 0 Reopen · 1 blocker.** Mọi lượt ghi sheet đều có đọc lại xác nhận; nhật ký ở
`output/UAT_doi-tac/tools/sheet_update_audit.jsonl`.

## Case duy nhất chưa đóng được — QLNDTVVCG_19

Khối "Đánh giá chất lượng" trên màn Chi tiết tư vấn chuyên sâu **có mặt** và ở trạng thái rỗng hợp lệ, nhưng
bảng 4 cột mà phiếu yêu cầu chỉ vẽ ra khi có ≥1 đánh giá — mà **toàn env nghiệm thu không có bản ghi nào có
đánh giá** (đã quét đủ 56/56 hồ sơ).

Đánh giá chỉ vào hệ thống qua 2 đường, cả hai đều nằm sau xác thực chứng thư hai chiều mà QA không được cấp;
đặc tả `srs-fr-12-tv-chuyen-sau.md:1006` ghi rõ **không có màn hình nhập trong phần mềm quản trị**. Vì vậy
không thể ghi Pass (chưa nhìn thấy bảng) cũng không thể ghi Reopen (chưa chứng minh được là lỗi).

**Cần bên phát triển nạp sẵn ≥2 đánh giá điểm khác nhau cho ít nhất 1 hồ sơ tư vấn chuyên sâu trên env
nghiệm thu.** Có dữ liệu là đo xong trong 1 lượt.

## Việc cần đối tác/BA quyết (không chặn bàn giao)

1. **Cấu trúc biểu mẫu 21b** — đặc tả màn hình (`srs-fr-15-ct-htpldn.md:1168`) ghi "tương tự 21a", còn Phụ lục D
   (`srs-v3.5.md:6601`, `:6694`) vẽ 21b là bảng tổng hợp cấp tỉnh với cột `STT | Sở/ban ngành | -1…-13 | Ghi chú`.
   Phần mềm đang làm theo đặc tả màn hình. Đề nghị BA ghi rõ tập cột của 21b vào phần đặc tả màn hình.
2. **Điều kiện hiển thị biểu mẫu 21a/21b** — đặc tả buộc "khi đợt ở Đang lập BC", phần mềm cho hiện từ "Tạo đợt"
   và bật chế độ nhập theo **trạng thái nộp của ĐƠN VỊ**. Theo dõi ở phiếu **TPDBCKQTHCT_01**.

## Lệch tài liệu cần dọn (KHÔNG tự sửa — theo quy tắc ô chỉ đọc)

Ô `Kết quả verify` của các dòng đã chuyển `UAT done` ở đợt này (299, 305) và của 8 dòng bỏ qua vẫn đang mang
nội dung đo trên **môi trường nội bộ** `18.143.165.120.nip.io`, kèm câu lưu ý "chưa có giá trị cho môi trường
nghiệm thu". Nay đã đo lại trên env nghiệm thu và kết quả trùng khớp, nên câu lưu ý đó đã lỗi thời.
Cần đối tác/QA chủ trì quyết có làm mới các ô này không.

## Dữ liệu QA đã dựng trên env nghiệm thu (có thể xóa sau khi đọc xong)

- Phiên tư vấn nhanh `TVN-20260807-0001` + 1 đánh giá của doanh nghiệp — dựng cho case QLKCHTV_37.
- Không tạo/sửa/xóa dữ liệu nào khác của đối tác. Case QLTLPLCVV_15 đã bấm Hủy và kiểm lại tư liệu giữ nguyên.
