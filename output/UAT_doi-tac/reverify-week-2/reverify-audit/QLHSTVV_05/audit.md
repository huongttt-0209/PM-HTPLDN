# Audit verify vòng 2 — QLHSTVV_05

| Mục | Nội dung |
|---|---|
| **Mã ca kiểm thử** | QLHSTVV_05 (dòng 60, tab `UAT_TGPL Doanh Nghiệp-tuần 2`) |
| **Mô tả ca** | Kiểm tra hiển thị thẻ "Thẩm định" khi người dùng là Người hỗ trợ hoặc Doanh nghiệp |
| **Kết quả mong đợi của ca** | Thẻ "Thẩm định" bị ẩn hoàn toàn |
| **Phản ánh vòng 2 của đối tác** | "Khi nhấn xem chi tiết hệ thống điều hướng đến màn hình thông báo '403-Forbidden'" |
| **Bằng chứng đối tác** | `QLHSTVV_04_v2.webm` (số hiệu tệp lệch một bậc — đối chiếu theo nội dung) |
| **Môi trường QA kiểm lại** | https://18.143.165.120.nip.io — tài khoản `nht_qa_01` (NHT, Sở Tư pháp An Giang) |
| **Thời điểm** | 2026-07-27 15:12–15:30 |
| **Bảng đối chiếu điều kiện** | [`../../cond/QLHSTVV_05-r2.md`](../../cond/QLHSTVV_05-r2.md) — **0 GAP** |
| **Kết luận** | **Open** |

---

## Cổng 1 — Bằng chứng đọc được gì

| Dữ kiện | Giá trị đọc từ video |
|---|---|
| Vai trò | **NHT**, badge "BTP · DP", tài khoản "hương 3 NHT" |
| Màn xuất phát | `/chuyen-gia-tvv/danh-sach?trangThai=MOI_DANG_KY` — tab "Mới đăng ký (3)" |
| Thao tác | t≈5,1 s con trỏ trên liên kết **"Xem"** của `TVV-STP-HN-0004 — NHT TKM` (trạng thái Mới đăng ký) |
| Kết quả | t≈5,6 s trang thành **`/403` — Forbidden — `ERR-PERM-SYS-00-01` — "Vai trò hiện tại: NHT"**, giữ tới hết video |
| Ghi nhận thêm | Cột Hành động của NHT hiển thị đủ **Xem · Sửa · Xóa** |

Video **không** chứa hình ảnh của tiêu chí gốc ca kiểm thử (thẻ "Thẩm định" ẩn hay hiện) — vì màn chi tiết không mở được nên không thể đánh giá tiêu chí đó trên bản của đối tác.

## Cổng 2 — Hiểu đúng bug đối tác báo

Đối tác báo: vai trò NHT **không xem được** hồ sơ tư vấn viên trong đơn vị mình — hệ thống đẩy sang trang lỗi quyền.
Không phải "thẻ Thẩm định vẫn hiện" (đó là phản ánh vòng 1); vòng 2 họ **không đánh giá được** tiêu chí gốc vì bị chặn từ trước.

## Cổng 3 — Đối chiếu đặc tả

| # | Điểm đối chiếu | Đặc tả (`Docs-PM-HTPLDN/…/srs-v3.5/srs-fr-04-chuyen-gia-tvv.md`) | Bản đang chạy | Đánh giá |
|---|---|---|---|---|
| 1 | Thẻ "Lịch sử hỗ trợ" phải xem được | `:1569` — SCR-IV-03 dòng 22, thẻ "Lịch sử hỗ trợ ({N})", cột **Điều kiện hiển thị = "Luôn"** | NHT bấm thẻ này → **cả trang** bị đẩy sang `/403 — ERR-PERM-SYS-00-01 — "Vai trò hiện tại: NHT"` | **Sai** — thẻ "Luôn" hiển thị lại trở thành rào chắn làm mất cả màn |
| 2 | NHT phải thao tác được trên màn chi tiết | `:372` FR-IV-04 §Tác nhân = **Người hỗ trợ pháp lý**; `:368` §Màn hình = **SCR-IV-03 (Tab Năng lực)**; `:429` §AC *"Given NHT xem chi tiết TVV cùng đơn vị…"* | NHT vào được màn nhưng mất màn ngay khi chạm thẻ Lịch sử hỗ trợ | **Sai** — luồng hợp lệ bị chặn giữa chừng |
| 3 | Nút "Bắt đầu thẩm định" chỉ dành cho Cán bộ Nghiệp vụ | `:1545` — SCR-IV-03 dòng 6, cột Điều kiện hiển thị: **"Vai trò = Cán bộ Nghiệp vụ cùng đơn vị; trạng thái ∈ {Mới đăng ký, Chờ thẩm định}"** | Nút **hiện** với vai trò NHT trên hồ sơ "Mới đăng ký"; bấm vào thì bị từ chối | **Sai** — hiển thị nút cho vai trò không được phép |
| 4 | Thông báo từ chối phải đọc hiểu được | `:198-199` bảng lỗi FR-IV-03 và `:422` bảng lỗi FR-IV-04 đều gán **thông báo tiếng Việt cụ thể** cho từng tình huống | Bấm "Bắt đầu thẩm định" với vai trò NHT → hộp thông báo hiện đúng một chữ **"Forbidden"** | **Sai** — thông báo tiếng Anh, không nói lên điều gì |
| 5 | **Tiêu chí gốc của ca:** thẻ "Thẩm định" ẩn với NHT | `:1557` — SCR-IV-03 dòng 13: *"**Ẩn hoàn toàn với chủ hồ sơ.** Hiển thị khi: vai trò = Cán bộ Nghiệp vụ HOẶC Cán bộ Phê duyệt cùng đơn vị; trạng thái ∈ {Đang thẩm định, Chờ phê duyệt}"* | Danh sách thẻ khi đăng nhập NHT: **Hồ sơ · Năng lực · Lịch sử hỗ trợ (0) · Đánh giá (0)** — **không có** thẻ "Thẩm định" | **Đúng** — phản ánh vòng 1 đã được sửa thật |

**Ghi chú về mâu thuẫn nội tại của đặc tả:** bảng "Quyền truy cập" của SCR-IV-03 (`:1530-1533`) liệt kê Cán bộ Nghiệp vụ, Cán bộ Phê duyệt và chủ hồ sơ — **không** liệt kê NHT; trong khi `:368`/`:372`/`:429` lại giao chức năng "Cập nhật năng lực" **trên chính màn này** cho NHT. Đã ghi vào bug ở mức **yêu cầu nghiệp vụ** ("NHT phải thao tác được chức năng đặc tả giao cho họ"), để dev tự chọn cách sửa. Cùng gốc với ghi nhận đã nêu ở audit `CNHSNLTVV_02`.

---

## Các phép đo

### Đo 1 — Dựng đúng điều kiện của đối tác

| Bước | Thao tác | Kết quả đo |
|---|---|---|
| 1 | Đăng nhập `nht_qa_01`, đọc dữ liệu tài khoản | `vaiTro = ["NHT"]`, mã đơn vị `…8002-000000000006` |
| 2 | Mở danh sách Tư vấn viên | Thấy 2 bản ghi, cả 2 **cùng mã đơn vị** với tài khoản; tab "Mới đăng ký" **rỗng** |
| 3 | Tạo 1 bản ghi Mới đăng ký để khớp điều kiện đối tác (dùng chính tài khoản NHT) | Tạo thành công `TVV-STP-AG-0003`, trạng thái **MOI_DANG_KY**, cùng đơn vị. ⇒ NHT **được phép** tạo hồ sơ tư vấn viên |
| 4 | Tab "Mới đăng ký" → bấm liên kết **"Xem"** ở cột Hành động | Cột Hành động của NHT có **Xem · Sửa · Xóa** (giống video). Màn chi tiết **mở bình thường**, **không** chuyển `/403` |
| 5 | Đọc danh sách thẻ trên màn chi tiết | **Hồ sơ · Năng lực · Lịch sử hỗ trợ (0) · Đánh giá (0)** — **không có** thẻ "Thẩm định" ⇒ tiêu chí gốc của ca **đạt** |

### Đo 2 — Bấm từng thẻ trên màn chi tiết (vai trò NHT)

| Thẻ | Kết quả |
|---|---|
| Hồ sơ | Mở bình thường |
| Năng lực | Mở bình thường (hiện nút "Cập nhật năng lực") |
| **Lịch sử hỗ trợ** | **Cả trang chuyển `/403` — Forbidden — `ERR-PERM-SYS-00-01` — "Vai trò hiện tại: NHT"** |
| Đánh giá | Mở bình thường (khối tổng hợp "—/5", 3 thanh Chuyên môn / Thái độ / Đúng hạn) |

Lời gọi gây ra việc chuyển trang, đọc từ nhật ký mạng của đúng lần bấm đó:

```
GET /api/v1/tu-van-viens/{id}                              -> 200
GET /api/v1/tu-van-viens/{id}/lich-su-ho-tro?page=1&…      -> 200   (còn 304 khi có cache)
GET /api/v1/hop-dong-tu-vans?tuVanVienId={id}&page=1&…     -> 403   <-- lời gọi bị từ chối
GET /403                                                    -> trang lỗi
```

Lặp lại trên **cả 3 bản ghi** của đơn vị (Đang hoạt động / Từ chối / Mới đăng ký): **đều** như nhau.

### Đo 3 — Kiểm lại bằng cách khác (gọi thẳng máy chủ, không qua giao diện)

| Bản ghi | Lấy chi tiết | Lấy lịch sử hỗ trợ | Lấy đánh giá |
|---|:-:|:-:|:-:|
| `TVV-STP-AG-0001` (Đang hoạt động) | 200 | 200 | **403** `ERR-PERM-SYS-00-01` |
| `TVV-STP-AG-0002` (Từ chối) | 200 | 200 | **403** `ERR-PERM-SYS-00-01` |
| `TVV-STP-AG-0003` (Mới đăng ký) | 200 | 200 | **403** `ERR-PERM-SYS-00-01` |

⇒ Vai trò NHT bị chặn ở **nhiều** lời gọi của chính màn chi tiết, không riêng lời gọi mà giao diện đang dùng.

### Đo 4 — Nút "Bắt đầu thẩm định" hiện với vai trò NHT

| Bước | Kết quả |
|---|---|
| Đọc danh sách nút ở đầu màn chi tiết `TVV-STP-AG-0003` (Mới đăng ký), vai trò NHT | `["Quay lại danh sách", "Sửa hồ sơ", **"Bắt đầu thẩm định"**]` |
| Bấm **"Bắt đầu thẩm định"** (bộ bắt thông báo tự kiểm: `soObserverDangSong = 1`, không lọc trùng) | Hộp thông báo hiện đúng một chữ **"Forbidden"**; đọc lại hồ sơ ngay sau đó: trạng thái vẫn **MOI_DANG_KY**, phiên bản vẫn **1** ⇒ không đổi dữ liệu |
| Kiểm hộp thông báo trùng | Ghi nhận 2 khung cùng chữ; số hộp **cùng tồn tại** tại mọi thời điểm lấy mẫu (120 ms/lần) tối đa = **1** ⇒ chỉ một hộp thông báo thật |

### Đo 5 — Đối chiếu với phép đo cùng ngày ở audit `CNHSNLTVV_02`

Sáng cùng ngày (≈13:00), cùng tài khoản `nht_qa_01` và cùng bản ghi `TVV-STP-AG-0001`, màn chi tiết **tự chuyển `/403` ngay khi mở**, và nhật ký mạng cho thấy giao diện gọi `…/danh-gia?page=1&pageSize=1` (trả 403) lúc tải màn.

Đo lại lúc 15:20 cùng ngày: giao diện **không còn gọi** lời gọi đó khi tải màn, nên màn chi tiết mở được. Bản thân lời gọi đó **vẫn trả 403** khi gọi thẳng (xem Đo 3).

⇒ Hành vi phía giao diện có thay đổi trong ngày. Điều **không** đổi: vai trò NHT vẫn bị đẩy sang trang `/403` khi dùng màn chi tiết, chỉ là chậm hơn một thao tác. Đã bổ sung ghi chú đính chính vào mục lỗi `BUG-CNHSNLTVV_02` để dev không tái hiện hụt.

---

## Verdict

| # | Ý | Kết quả verify | Verdict ý |
|:-:|---|---|---|
| 1 | "Nhấn xem chi tiết → 403 Forbidden" | **Tái hiện một phần, đúng bản chất.** Mở chi tiết không còn 403; nhưng bấm thẻ "Lịch sử hỗ trợ" (điều kiện hiển thị "Luôn" theo `:1569`) thì cả trang bị đẩy sang đúng trang 403 với đúng mã lỗi đối tác chụp được | **Open** |
| 2 | *(QA phát hiện thêm)* Nút "Bắt đầu thẩm định" hiện với vai trò NHT, trái `:1545` | Nút hiện; bấm bị từ chối, dữ liệu không đổi | **Open** — gộp vào cùng mục lỗi |
| 3 | *(QA phát hiện thêm)* Thông báo từ chối là chữ tiếng Anh "Forbidden" | Đo trực tiếp trên giao diện | **Open** — gộp vào cùng mục lỗi |
| 4 | Tiêu chí gốc của ca: thẻ "Thẩm định" ẩn với NHT | **Đạt** — danh sách thẻ không có "Thẩm định" | Không phải lỗi |

**Verdict tổng: `Open`** (đa ý → tổng là `Open` nếu ≥1 ý Open).

**Vì sao không `Reject`:** `Reject` chỉ dùng khi chứng minh được đối tác thao tác/hiểu sai hoặc báo cáo vô hiệu. Ở đây đối tác không sai: cùng vai trò, cùng đơn vị, cùng đường vào, và trang 403 mà họ chụp **vẫn còn** trên bản đang chạy, chỉ dịch chuyển sang thao tác kế tiếp trên chính màn đó.

Mục lỗi: [`../../bug-reports/mang-luoi-tvv/Pass-bug-report-tuan-2-r2-mang-luoi-tvv.md`](../../bug-reports/mang-luoi-tvv/Pass-bug-report-tuan-2-r2-mang-luoi-tvv.md) → `BUG-QLHSTVV_05`.

## Dữ liệu để lại

`TVV-STP-AG-0003 — QA TVV QLHSTVV05 R2` (Sở Tư pháp An Giang, trạng thái Mới đăng ký) do QA tạo để khớp điều kiện đối tác. **Giữ lại** để dev tái hiện trực tiếp.
