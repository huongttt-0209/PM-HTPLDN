# LBCKQTHCT_03 — Chi tiết đợt báo cáo, Biểu mẫu 21a (sheet `bug` row 336)

**Đợt:** re-verify trên MÔI TRƯỜNG NGHIỆM THU `https://htpldn-uat.ospgroup.vn`
**Ngày đo:** 2026-08-07
**Bản dựng:** V1.0.10 · bó mã chính `index-Bd1akG3f.js` · bó mã màn Chi tiết đợt BC `index-BX28rPGx.js`
**Tài khoản:** `cbnv_tw` (Cán bộ Nghiệp vụ Trung ương) — lượt đo 1 · `admin` (Quản trị hệ thống) — lượt đo 2
**Bản ghi:** đợt `DOT-SO_BO_NAM-2026-2` (đúng đợt xuất hiện trong video của phiếu) và `DOT-TRON_NAM-2026-1`
**Phiếu báo:** "Hệ thống hiển thị thiếu các cột: Số liệu kỳ trước, Ghi chú"

## Verdict: ✅ PASS → `Trạng thái dev fix` = `UAT done`

Không tái hiện: bảng Biểu mẫu 21a hiển thị **đủ 4 cột**, đúng thứ tự đặc tả.

## Bảng đối chiếu điều kiện

| Điều kiện có thể đổi kết quả | Bug gốc (phiếu đối tác) | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | "Đăng nhập hệ thống thành công" (phiếu không chỉ định vai trò) | Đo bằng 2 vai trò khác nhau: Cán bộ NV Trung ương và Quản trị hệ thống | Không |
| Màn + thao tác | 1. Menu "Đợt báo cáo" → 2. Mở Chi tiết đợt báo cáo | Đúng y 2 bước đó, điều hướng trong ứng dụng | Không |
| Dữ liệu tiền đề | Đợt báo cáo trong video: `DOT-SO_BO_NAM-2026-2` | Đợt đó **có tồn tại** trên env nghiệm thu, đã mở đúng nó | Không |
| Biểu mẫu áp dụng | (phiếu không nêu) | Đợt dùng **cả hai biểu** (`CA_HAI`) nên khối 21a chắc chắn phải hiện | Không |
| Trạng thái đợt / chế độ bảng | (phiếu không nêu) | Đo ở trạng thái "Tạo đợt" → bảng ở chế độ **chỉ đọc**. Đã đóng khoảng trống này ở mục "Chế độ nhập liệu" bên dưới | Không (đã đóng) |

0 GAP → đủ điều kiện chốt verdict.

## Kết quả đo

**Hàng tiêu đề bảng "Biểu mẫu 21a/TP/HTPLDN" đọc được đúng 4 cột, đúng thứ tự:**

| # | Tiêu đề cột | Có mặt |
|---|---|:-:|
| 1 | Chỉ tiêu | ✅ |
| 2 | **Số liệu kỳ trước** | ✅ (phiếu báo thiếu) |
| 3 | Kỳ này | ✅ |
| 4 | **Ghi chú** | ✅ (phiếu báo thiếu) |

- Bảng có **đúng 13 dòng chỉ tiêu** (1. Số TVV kiện toàn … 13. KP xã hội hóa).
- Lặp lại trên **2 đợt khác nhau** (`DOT-SO_BO_NAM-2026-2`, `DOT-TRON_NAM-2026-1`) và bằng **2 vai trò khác nhau** — cả 4 tổ hợp đều hiện đủ 4 cột.

Bằng chứng: [image/LBCKQTHCT_03-bieu-mau-21a-du-cot-uat.png](../image/LBCKQTHCT_03-bieu-mau-21a-du-cot-uat.png)

**Cột không bị ẩn khi rỗng (loại khả năng chấm oan).** Đọc thẳng dữ liệu nguồn của đợt: trường số liệu kỳ trước
đang **rỗng** (`soLieuKyTruoc: null`). Vậy mà cột "Số liệu kỳ trước" vẫn hiển thị đủ 13 ô, mỗi ô ghi dấu "—".
Tức cột hiện theo cấu trúc bảng, không phải "có dữ liệu mới hiện" → không rơi vào trường hợp may mắn có số liệu.

**Không tràn / không đè lên nhau** (yêu cầu thứ 3 của phiếu): đo tọa độ từng ô của cả 13 dòng —
**0 ô chồng lấn nhau**, **0 cột bị đẩy khuất ngoài khung nhìn**. Bốn cột trải kín bề ngang bảng
(335 / 179 / 179 / 311 điểm ảnh trên cửa sổ rộng 1440).

**Đồng nhất ngôn ngữ:** quét toàn bộ chữ trên màn — không có chuỗi tiếng Anh lọt, không có `null` / `undefined` /
`[object Object]` hiển thị ra ngoài.

## Chế độ nhập liệu — vì sao vẫn kết luận được dù bảng đang chỉ đọc

Trên env nghiệm thu cả 4 đợt đều ở trạng thái "Tạo đợt", nên bảng 21a đang ở **chế độ chỉ đọc**; đặc tả thì mô tả
21a là bảng **nhập liệu**. Để chắc chắn không phải "chế độ chỉ đọc thì đủ cột, chế độ nhập thì thiếu cột",
đã đọc mã nguồn giao diện của chính màn này (`index-BX28rPGx.js`): **tập 4 cột được khai báo một lần duy nhất**,
dùng chung cho cả hai chế độ; chỉ **cách vẽ ô** đổi (chế độ nhập thì ô "Kỳ này" là ô số, ô "Ghi chú" là ô chữ
tối đa 500 ký tự; chế độ chỉ đọc thì hiển thị chữ). Không có nhánh nào bỏ bớt cột.

Cũng đã kiểm khả năng bố cục cũ lưu lại làm hỏng cột: độ rộng cột có được ghi nhớ, nhưng có **chặn dưới 60 điểm ảnh**
và không có đường nào xóa cột. Phiên đo dùng hồ sơ trình duyệt sạch, không có bố cục cũ lưu lại.

## Đối chiếu SRS

| SRS yêu cầu | Dẫn nguồn | Thực tế env nghiệm thu |
|---|---|---|
| Biểu mẫu 21a gồm: `Chi tieu / So lieu ky truoc / Ky nay / Ghi chu` | `srs-fr-15-ct-htpldn.md:1167` | **Khớp đủ 4 cột, đúng thứ tự** |
| `MAU_21A` → 13 chỉ tiêu biểu 21a `[BA chốt 2026-08-06]` | `srs-fr-15-ct-htpldn.md:802` | Khớp — đúng 13 dòng |
| Khối 21a hiện khi biểu mẫu áp dụng | `srs-fr-15-ct-htpldn.md:1167` | Khớp — đợt dùng `CA_HAI` nên 21a hiện |
| Modal tạo đợt có lựa chọn biểu mẫu `MAU_21A / MAU_21B / CA_HAI` | `srs-fr-15-ct-htpldn.md:1158` | Khớp — cả 4 đợt trên env đều đang là `CA_HAI` |

UC: `srs-fr-15-ct-htpldn.md:703` — **UC 166**.

> **Điểm lệch đã biết, KHÔNG thuộc phiếu này:** đặc tả tại `:1167` ràng buộc 21a hiển thị "khi đợt ở trạng thái
> Đang lập BC", nhưng phần mềm cho hiện bảng ngay từ trạng thái "Tạo đợt" và bật/tắt chế độ nhập theo **trạng thái
> nộp của ĐƠN VỊ** chứ không theo trạng thái của ĐỢT. Điểm này đã được theo dõi ở phiếu **TPDBCKQTHCT_01** —
> phiếu có kết quả mong đợi nhắm thẳng vào trạng thái đợt. Nó không đổi kết luận của phiếu 03 (phiếu 03 hỏi về
> tập cột, và tập cột đã đủ).

## Ngoài phiếu này, có thấy gì bất thường không?

Không phát hiện thêm lỗi. Hai ghi nhận không phải lỗi:

- Bảng có thanh cuộn ngang do dư đúng **4 điểm ảnh** so với bề ngang khung — sai số làm tròn của thư viện bảng,
  không cột nào bị che.
- Hai bảng 21a và 21b dùng chung một khóa ghi nhớ độ rộng cột, nên kéo giãn cột ở bảng này thì bảng kia giãn theo.
  Hai bảng có tập cột giống hệt nhau nên đồng bộ như vậy là nhất quán, không gây sai lệch dữ liệu.

> **Ghi nhận về tài khoản:** lượt đo 1 dùng `cbnv_tw`; giữa buổi có một phiên QA khác cần độc quyền tài khoản này
> nên lượt đo 2 chuyển sang `admin`. Cả hai lượt cho kết quả giống hệt nhau, nên việc đổi tài khoản không ảnh
> hưởng kết luận. Không thay đổi bất kỳ dữ liệu nào của đối tác trong lượt đo này (chỉ xem, không lưu).
