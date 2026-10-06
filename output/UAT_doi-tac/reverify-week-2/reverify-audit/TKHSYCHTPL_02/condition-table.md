# TKHSYCHTPL_02 — Bảng đối chiếu điều kiện

**Case:** Kiểm tra các trường thông tin tìm kiếm trên màn Danh sách Vụ việc HTPL (SCR-V.I-01 · FR-V.I-08 UC58).

**Evidence đối tác:** `partner-evidence/TKHSYCHTPL_02.jpg` — **CÓ khoảnh khắc lỗi**.
Full-res: URL `htpldn-uat.ospgroup.vn/vu-viec/danh-sach?tab=TAT_CA`, tài khoản **"Cán bộ NV Trung ương / CB_NV_TW"** (cấp Trung ương, thấy 53 VV toàn quốc).
Thanh tìm kiếm đã bung "Bộ lọc nâng cao (2)": **Tìm theo mã VV hoặc tên DN · Lĩnh vực PL · Kênh tiếp nhận · Mức SLA · Trạng thái · Từ ngày · Đến ngày**.
**KHÔNG có trường lọc "Đơn vị"** — đúng như đối tác phản ánh.

**Đối tác phản ánh:** không hiển thị trường tìm kiếm theo **"Đơn vị"** đối với người dùng cấp Trung ương.

| Điều kiện có thể đổi kết quả | Đối tác (từ evidence, full-res) | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản (quyết định cấp + phạm vi dữ liệu) | **CB_NV_TW** — header ảnh "Cán bộ NV Trung ương / CB_NV_TW", badge "BTP · TW", thấy VV nhiều đơn vị (VV-STP-AG, VV-BTP-TW, VV-BKH) | **`cbnv_tw`** — header "CB Nghiệp vụ - Trung ương / CB_NV_TW", badge "BTP · TW", thấy 17 VV nhiều đơn vị (VV-STP-AG, VV-BTP-TW, VV-SEED, EEE, DDD) → đúng cấp TW, đúng bối cảnh "nhìn được nhiều đơn vị" | Không |
| Màn hình + trạng thái bộ lọc | Màn Danh sách VV, đã **bung "Bộ lọc nâng cao"** (hiện Từ ngày/Đến ngày) | Đúng màn `/vu-viec/danh-sach`, đã bung "Bộ lọc nâng cao (2)" | Không |
| Dữ liệu tiền đề | Có VV thuộc **nhiều đơn vị khác nhau** (điều kiện để nhu cầu lọc theo đơn vị phát sinh) | Có VV thuộc nhiều đơn vị (Sở Tư pháp An Giang + Bộ Tư pháp TW + đơn vị khác) | Không |

## Quan sát (real-data) — cbnv_tw, thanh tìm kiếm màn Danh sách VV

```json
{"o_nhap":    [{"placeholder":"Tìm theo mã VV hoặc tên DN..."},
               {"placeholder":"Từ ngày"}, {"placeholder":"Đến ngày"}],
 "danh_sach_chon": ["Lĩnh vực PL", "Kênh tiếp nhận", "Mức SLA", "Trạng thái"],
 "nut":       ["Bộ lọc nâng cao (2)", "Xóa bộ lọc", "Tìm kiếm"],
 "co_truong_don_vi": false}
```

Ảnh: `web-thanh-tim-kiem-tw-khong-co-truong-don-vi.png`

## Đối chiếu SRS (Cổng 3)

- **SRS quy định thanh lọc** — `srs-fr-05-vu-viec.md:1622-1628` (SCR-V.I-01 §Thành phần #4→#10, vùng `filter-bar`): **Ô tìm kiếm (từ khóa mã VV/tên DN)** · **Lĩnh vực PL** · **Trạng thái** · **Kênh tiếp nhận** · **Mức SLA** · **Bộ chọn ngày (từ–đến)** · nút **Tìm kiếm / Xóa bộ lọc**. → **6 trường lọc, KHÔNG có "Đơn vị"**.
- **SRS quy định input tìm kiếm** — `srs-fr-05-vu-viec.md:645-652` (FR-V.I-08 / UC58 §Inputs): `tu_khoa`, `linh_vuc_id`, `trang_thai`, `kenh_tiep_nhan`, `tu_ngay`, `den_ngay`. → **KHÔNG có `don_vi_id`**.
- **Đối chiếu:** web hiển thị **ĐÚNG 6 trường** SRS liệt kê, không thừa không thiếu ⇒ **web đang đúng SRS**.
- **Kỳ vọng đối tác** ("phải có trường lọc theo Đơn vị cho người dùng cấp Trung ương") **KHÔNG có trong SRS** — SRS **im lặng** về nhu cầu này.
- **Bối cảnh khiến kỳ vọng của đối tác hợp lý:** `srs-fr-05-vu-viec.md:1637` (SCR-V.I-01 §Quy tắc tương tác, BR-AUTH-03/04): *"Cán bộ TW xem toàn quốc; cán bộ BN/ĐP chỉ thấy vụ việc của đơn vị mình"* ⇒ riêng người dùng TW nhìn thấy VV của **mọi đơn vị**, nhưng lại **không có cách lọc theo đơn vị** — trong khi cột "Mã VV" đã mã hoá đơn vị (VV-**STP-AG**, VV-**BTP-TW**...). Đây là khoảng trống đặc tả có thật, không phải đối tác báo sai.

**Kết luận:** Đối tác quan sát **ĐÚNG thực tế** (web không có trường lọc Đơn vị), nhưng đây là **bất đồng về ĐẶC TẢ** — SRS không quy định trường này. QA **không tự Reject** → **BA confirm**.

**Câu hỏi cho BA:** Với người dùng cấp Trung ương (xem VV toàn quốc theo BR-AUTH-03/04), có bổ sung trường lọc **"Đơn vị"** vào thanh tìm kiếm màn Danh sách Vụ việc (SCR-V.I-01) + input `don_vi_id` vào FR-V.I-08 không? Nếu có, chỉ hiện với cấp TW hay hiện cho mọi cấp?
