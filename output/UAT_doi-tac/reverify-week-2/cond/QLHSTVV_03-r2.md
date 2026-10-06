# Bảng đối chiếu điều kiện — QLHSTVV_03 (verify phản ánh vòng 2)

**Claim vòng 2 của đối tác:**
- (a) "Nhóm 2 thông tin nghề nghiệp thừa trường **Số quyết định (công nhận)**"
- (b) "Nhóm 3 — Tổ chức thừa trường **Địa bàn**"

**Evidence:** `QLHSTVV_03_v2.jpg` — ảnh tĩnh 1 khung hình, `htpldn-uat.ospgroup.vn/chuyen-gia-tvv/b88271a7-…`,
breadcrumb "Trang chủ / Mạng lưới Tư vấn viên / Chi tiết", header **"BTP · TW · Cán bộ NV Trung ương · CB_NV_TW"**, 25/07/2026 16:19.
Ảnh đọc được đầy đủ 2 nhóm đang tranh luận:
- **Nghề nghiệp**: Trình độ `Cử nhân` · Chuyên ngành `Luật dân sự` · Chức vụ `Luật sư` · Nơi công tác `TKM` · Số thẻ hành nghề `1123` ·
  Số QĐ công bố `QĐ-TVV/CG-1123` · Ngày QĐ công bố `25/07/2026` · **Số quyết định (công nhận) `—`** · Số năm kinh nghiệm `1 năm` ·
  Chứng chỉ hành nghề `1123` · Chứng chỉ chi tiết · Mô tả kinh nghiệm.
- **Tổ chức & Mạng lưới**: Tổ chức chính `Test thêm mới tổ chức địa phương` · Đối tác · **Địa bàn `—`**.

| Điều kiện có thể đổi kết quả | Đối tác (từ evidence, full-res) | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò / cấp | Cán bộ Nghiệp vụ **Trung ương** (`CB_NV_TW`), badge "BTP · TW" | `cbnv_tw` — vai trò **CB_NV_TW**, badge "BTP · TW" (trùng khít) | Không |
| Màn hình + thẻ | Màn chi tiết tư vấn viên `/chuyen-gia-tvv/{id}`, thẻ **Hồ sơ**, chế độ chỉ xem | Cùng đường dẫn, cùng thẻ Hồ sơ, cùng chế độ chỉ xem | Không |
| Nhóm đang xét | Nhóm "Nghề nghiệp" và nhóm "Tổ chức & Mạng lưới", cả hai đang mở | Cùng 2 nhóm, đã mở toàn bộ và đọc **hết nhãn** bằng DOM (không phụ thuộc vùng nhìn) | Không |
| Dữ liệu của 2 trường tranh luận | Cả hai đều hiển thị `—` (rỗng) ⇒ 2 mục này **hiện ra bất kể có dữ liệu hay không** | Kiểm cả 2 chiều: bản ghi **có** số quyết định công nhận (`TVV-BTP-TW-0016`, đã phê duyệt, `soQuyetDinh = QĐ-8017/QĐ-BTP`) và bản ghi **không có** (`TVV-STP-AG-0001`) | Không |
| Trạng thái hồ sơ | Mới đăng ký | Kiểm 2 trạng thái khác nhau: Chờ kích hoạt tài khoản (`TVV-BTP-TW-0016`) và Đang hoạt động (`TVV-STP-AG-0001`) | Không |
| Quan hệ đơn vị | TVV thuộc Sở Tư pháp Hà Nội, người xem là cán bộ Trung ương (xem chéo đơn vị) | Kiểm cả cùng đơn vị (`TVV-BTP-TW-0016` — Cục Bổ trợ tư pháp) và khác đơn vị (`TVV-STP-AG-0001` — Sở Tư pháp An Giang) | Không |

**Kết luận:** 0 GAP — cùng vai trò, cùng màn/thẻ/nhóm; phạm vi của mình rộng hơn (2 bản ghi, 2 trạng thái, có/không dữ liệu, cùng/khác đơn vị).

**Kết quả tái hiện:** ở tất cả tổ hợp trên, thẻ Hồ sơ **không hiển thị** mục "Số quyết định (công nhận)" và **không hiển thị** mục "Địa bàn".
Xử lý tình huống "không tái hiện nhưng đối tác có bằng chứng rõ": xem [`../reverify-audit/QLHSTVV_03/audit.md`](../reverify-audit/QLHSTVV_03/audit.md) §Verdict từng ý.
