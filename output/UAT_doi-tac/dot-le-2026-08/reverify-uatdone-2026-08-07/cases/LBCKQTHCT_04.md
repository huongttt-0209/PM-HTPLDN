# LBCKQTHCT_04 — Chi tiết đợt báo cáo, Biểu mẫu 21b (sheet `bug` row 337)

**Đợt:** re-verify trên MÔI TRƯỜNG NGHIỆM THU `https://htpldn-uat.ospgroup.vn`
**Ngày đo:** 2026-08-07
**Bản dựng:** V1.0.10 · bó mã chính `index-Bd1akG3f.js` · bó mã màn Chi tiết đợt BC `index-BX28rPGx.js`
**Tài khoản:** `cbnv_tw` (Cán bộ Nghiệp vụ Trung ương) — lượt đo 1 · `admin` (Quản trị hệ thống) — lượt đo 2
**Bản ghi:** đợt `DOT-SO_BO_NAM-2026-2` và `DOT-TRON_NAM-2026-1`, cả hai áp dụng **cả hai biểu mẫu** (`CA_HAI`)
**Phiếu báo:** "Hệ thống hiển thị thiếu các cột: Số liệu kỳ trước, Ghi chú"

## Verdict: ✅ PASS → `Trạng thái dev fix` = `UAT done`

Không tái hiện: bảng Biểu mẫu 21b hiển thị **đủ 4 cột**, đúng thứ tự đặc tả.

## Bảng đối chiếu điều kiện

| Điều kiện có thể đổi kết quả | Bug gốc (phiếu đối tác) | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | "Đăng nhập hệ thống thành công" (phiếu không chỉ định vai trò) | Đo bằng 2 vai trò: Cán bộ NV Trung ương và Quản trị hệ thống | Không |
| Màn + thao tác | 1. Menu "Đợt báo cáo" → 2. Mở Chi tiết đợt báo cáo | Đúng y 2 bước đó, điều hướng trong ứng dụng | Không |
| **Biểu mẫu áp dụng** | Ảnh bị cắt tiêu đề thẻ nên không đọc được | **Bắt buộc phải là đợt có áp dụng 21b** — cả 4 đợt trên env đều `CA_HAI` nên 21b chắc chắn phải hiện | Không |
| Trạng thái đợt / chế độ bảng | (phiếu không nêu) | Đo ở "Tạo đợt" → bảng chỉ đọc. Đã đóng khoảng trống ở mục "Chế độ nhập liệu" | Không (đã đóng) |

0 GAP → đủ điều kiện chốt verdict.

> **Vì sao phải soi điều kiện "biểu mẫu áp dụng":** đặc tả `srs-fr-15-ct-htpldn.md:1168` quy định khối 21b chỉ hiện
> "khi biểu mẫu được áp dụng". Nếu đo trên một đợt chỉ dùng 21a rồi kết luận "thiếu 21b" thì sẽ chấm oan, vì
> 21b vắng mặt trong tình huống đó là ĐÚNG đặc tả. Đã đọc dữ liệu nguồn của cả 4 đợt trên env: **tất cả đều
> `CA_HAI`** → điều kiện hiển thị 21b thỏa mãn, không cần dựng thêm dữ liệu.

## Kết quả đo

**Nhận diện đúng bảng 21b bằng NHÃN THẺ, không bằng vị trí hay nội dung.** Hai bảng 21a và 21b trên màn có nội
dung giống hệt nhau, nên đã tìm thẻ có tiêu đề đúng chữ **"Biểu mẫu 21b/TP/HTPLDN"** rồi mới đọc bảng bên trong.

| # | Tiêu đề cột của bảng 21b | Có mặt |
|---|---|:-:|
| 1 | Chỉ tiêu | ✅ |
| 2 | **Số liệu kỳ trước** | ✅ (phiếu báo thiếu) |
| 3 | Kỳ này | ✅ |
| 4 | **Ghi chú** | ✅ (phiếu báo thiếu) |

- Bảng có **đúng 13 dòng chỉ tiêu**, dòng cuối đọc được: `13. KP xã hội hóa | — | 0 | —`.
- **13/13 ô của cột "Ghi chú" đều được vẽ ra** (không có ô rỗng bị bỏ trống do lỗi kết xuất).
- Lặp lại trên **2 đợt khác nhau** và bằng **2 vai trò khác nhau** — cả 4 tổ hợp đều đủ 4 cột.

Bằng chứng: [image/LBCKQTHCT_04-bieu-mau-21b-du-cot-uat.png](../image/LBCKQTHCT_04-bieu-mau-21b-du-cot-uat.png)

**Cột không bị ẩn khi rỗng:** dữ liệu nguồn của đợt có trường số liệu kỳ trước **rỗng** (`soLieuKyTruoc: null`),
vậy mà cột "Số liệu kỳ trước" vẫn hiện đủ 13 ô ghi dấu "—" → cột hiện theo cấu trúc bảng, không phải "có dữ liệu
mới hiện".

**Không tràn / không đè lên nhau:** đo tọa độ từng ô của cả 13 dòng bảng 21b — **0 ô chồng lấn**, **0 cột bị đẩy
khuất ngoài khung nhìn**.

**Đồng nhất ngôn ngữ:** không có chuỗi tiếng Anh lọt, không có `null` / `undefined` / `[object Object]` hiển thị.

## Chế độ nhập liệu — vì sao vẫn kết luận được dù bảng đang chỉ đọc

Đã đọc mã nguồn giao diện màn này (`index-BX28rPGx.js`): **21a và 21b dùng CHUNG một thành phần bảng**, tập 4 cột
khai báo một lần duy nhất, chỉ khác nhau ở nhãn tiêu đề thẻ. Chế độ nhập/chỉ đọc chỉ đổi **cách vẽ ô**
(chế độ nhập: "Kỳ này" là ô số, "Ghi chú" là ô chữ tối đa 500 ký tự) — không có nhánh nào bỏ bớt cột.
Vì dùng chung thành phần, kết quả đo được ở 21a áp thẳng cho 21b và ngược lại.

## Đối chiếu SRS

| SRS yêu cầu | Dẫn nguồn | Thực tế env nghiệm thu |
|---|---|---|
| Biểu mẫu 21b "Tương tự 21a" — tức `Chi tieu / So lieu ky truoc / Ky nay / Ghi chu` | `srs-fr-15-ct-htpldn.md:1168` (dẫn về `:1167`) | **Khớp đủ 4 cột, đúng thứ tự** |
| Khối 21b hiện khi biểu mẫu được áp dụng | `srs-fr-15-ct-htpldn.md:1168` | Khớp — đợt `CA_HAI` nên 21b hiện |
| Đợt chọn biểu mẫu `MAU_21A / MAU_21B / CA_HAI` | `srs-fr-15-ct-htpldn.md:730` · `:1158` | Khớp |
| `CA_HAI` → phải đủ chỉ tiêu của **cả hai biểu** `[BA chốt 2026-08-06]` | `srs-fr-15-ct-htpldn.md:802` | Khớp — cả hai bảng đều đủ 13 dòng |

UC: `srs-fr-15-ct-htpldn.md:703` — **UC 166**.

> **Ghi nhận để BA xem xét — KHÔNG ảnh hưởng kết luận phiếu này.** Bảng 21b trên màn đang dựng giống hệt 21a
> (13 dòng chỉ tiêu × 4 cột), trong khi Phụ lục D của tài liệu tổng mô tả mẫu 21b là **bảng tổng hợp cấp tỉnh**:
> `srs-v3.5.md:6601` (D.1.3) vẽ khung `STT | Sở/ban ngành | -1 … -13 | -14 Ghi chú`, mỗi dòng là một Sở/ban ngành
> kèm dòng "Tổng tỉnh"; `srs-v3.5.md:6694` (D.2.2) chốt cột A = STT, cột B = Sở/ban ngành, `-1 → -13` "tương tự 21a"
> tổng hợp SUM từ các Sở/ban ngành thuộc tỉnh.
> Hai chỗ này thuộc **hai tầng khác nhau**: Phụ lục D mô tả **tệp văn bản xuất ra** (tham chiếu FR-VI-07, FR-XI-09),
> còn `:1168` mô tả **biểu mẫu nhập trên màn** và chỉ ghi vắn tắt "tương tự 21a" — dev đang làm đúng câu chữ của
> phần đặc tả màn hình. Đề nghị BA ghi rõ tập cột và cấu trúc dòng của 21b vào phần đặc tả màn hình để hai bên
> không chấm bằng hai thước đo khác nhau. Đây là đề nghị bổ sung đặc tả, **không chặn bàn giao**.

## Ngoài phiếu này, có thấy gì bất thường không?

Không phát hiện thêm lỗi. Các ghi nhận không phải lỗi đã nêu ở phiếu [LBCKQTHCT_03](LBCKQTHCT_03.md)
(thanh cuộn ngang dư 4 điểm ảnh; hai bảng dùng chung khóa ghi nhớ độ rộng cột) áp dụng y nguyên cho 21b.

> Không thay đổi bất kỳ dữ liệu nào của đối tác trong lượt đo này (chỉ xem, không lưu, không tạo đợt mới).
