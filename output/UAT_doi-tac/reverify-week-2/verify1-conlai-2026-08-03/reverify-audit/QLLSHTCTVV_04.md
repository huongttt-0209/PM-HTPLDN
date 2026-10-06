# QLLSHTCTVV_04 — evidence audit (verify vòng 1, 2026-08-03)

## 0. Note CŨ của dev ở cột R (backup TRƯỚC khi đè)

> **R126 (DEV phản hồi lần 1) — giá trị cũ, dev ghi:**
> KHÔNG phải bug: Filter Trạng thái tab Lịch sử hỗ trợ là tập rút gọn (Tất cả/Đang xử lý/Hoàn thành/Từ chối) theo SRS SCR-IV-03:1578, không phải toàn bộ enum 12 trạng thái Quản lý vụ việc. Kỳ vọng lệch SRS v3.5.

> **P126 (Trạng thái dev fix 1) — giá trị hiện tại:** `Reject` (KHÔNG đụng vào cột P)

---

## 1. Cổng 1 — Bằng chứng đối tác

**File:** `partner-evidence/QLLSHTCTVV_04.jpg` — md5 `4923d2d170b52a2d62c9ebdeb4b9d2ed`, 283.499 bytes.
**KHÔNG trùng md5** với ảnh nào khác trong lô (khác với cặp `DKTGMLTVV_04_v2` / `_05_v2` bị trùng).
Đã mở **full-res** bằng Read tool, không đọc từ ảnh thu nhỏ.

### 3 dữ kiện neo (viết TRƯỚC khi hình thành giả thuyết)

| # | Dữ kiện | Giá trị đọc từ ảnh |
|---|---|---|
| (a) | URL / ID bản ghi | `htpldn-uat.ospgroup.vn/chuyen-gia-tvv/06748bb5-e5d4-453f-9490-f07b17fd0a4a` — màn Hồ sơ chi tiết Tư vấn viên |
| (b) | Trạng thái entity đối tác đang đứng | Tab **"Lịch sử hỗ trợ (4)"** đang được chọn. Hồ sơ đã có "Ngày công nhận: 08/05/2026" ⇒ đã qua phê duyệt. Vai trò đăng nhập: **"Cán bộ NV Trung ương · CB_NV_TW"**, đơn vị **"BTP · TW"** |
| (c) | Dữ liệu tiền đề | Thẻ thống kê: Tổng vụ việc **4** · Đã hoàn thành **2** · Điểm trung bình **8.3**. Bảng 4 dòng (`VV-HDSD-003`, `VV-QA-R9-HTK-001`, `VV-QA-R7-SLA-BT`, `VV-BTP-TW-20260509-008`), phân trang "1-4 / 4 mục" |

## 2. Cổng 2 — Hiểu bug (3 dòng bắt buộc)

1. **Evidence đã xem:** `QLLSHTCTVV_04.jpg`, vùng chứa lỗi = **dropdown "Trạng thái vụ việc" đang MỞ**, nằm ngay dưới 3 thẻ thống kê. Trong khung dropdown đọc được **đúng 3 mục**: "Đang xử lý" · "Hoàn thành" · "Từ chối". Không có "Tất cả", không có "Đã hủy". Ảnh bắt đúng khoảnh khắc lỗi (dropdown mở), không phải ảnh chụp sau.
2. **Đối tác phản ánh CỤ THỂ:** *"Danh sách chọn Trạng thái chưa đủ giá trị theo định nghĩa của nhóm chức năng Quản lý vụ việc"* — tức bộ lọc trạng thái ở tab này ít giá trị hơn tập trạng thái vụ việc đầy đủ mà nhóm Quản lý vụ việc dùng.
3. **Data + bước tái hiện:** đăng nhập vai Cán bộ Nghiệp vụ → Mạng lưới TVV → Tư vấn viên/Chuyên gia → xem chi tiết 1 ứng viên đã công nhận, có lịch sử hỗ trợ → tab "Lịch sử hỗ trợ" → mở dropdown "Trạng thái vụ việc".

## 3. Cổng 3 — Bảng đối chiếu SRS vs web

Tài khoản dùng: **`cbnv_tw_02`** ("CB Nghiệp vụ - Trung ương #02", `CB_NV_TW`, đơn vị BTP·TW).
KHÔNG dùng admin. Bản dựng: **HTPLDN · V1.0.5**. Hồ sơ test: `TVV-BTP-TW-0002` (Đang hoạt động,
tab "Lịch sử hỗ trợ (6)"). Trang đã **tải lại** (`reload` + bỏ cache) trước khi đo, tránh chạy JS cũ
của tab mở lâu.

| # | SRS yêu cầu (dẫn line) | Thực tế web | Đạt? |
|---|---|---|:-:|
| 1 | `SCR-IV-03:1578` — bộ lọc gồm **Khoảng ngày** + **Trạng thái vụ việc** | Có đủ 2 bộ lọc: cặp ô "Từ ngày → Đến ngày" + ô "Trạng thái vụ việc" | ✅ |
| 2 | `SCR-IV-03:1578` — tập giá trị: `"Tất cả" / "Đang xử lý" / "Hoàn thành" / "Đã hủy"` | 3 option: `"Đang xử lý"` / `"Hoàn thành"` / `"Từ chối"` | ⚠️ xem §4 ý B |
| 3 | `SCR-IV-03:1578` — kiểu điều khiển **"chọn nhiều"** | **Chọn đơn** — xác minh 3 cách ở §5 | ❌ |
| 4 | `SCR-IV-03:1578` — "Tất cả" (xem toàn bộ, không lọc) | Không có option tên "Tất cả", **nhưng** ô lọc có nút xóa (⊗); bấm xóa → gửi request không kèm `trangThaiVv` → trả về đủ 6/6 dòng. Hành vi "xem tất cả" **vẫn đạt được** | ✅ (khác cách thể hiện) |
| 5 | `FR-IV-10:773` — cho phép lọc theo `trang_thai_vv` | Có, tham số gửi lên là `trangThaiVv=<ENUM>` | ✅ |
| 6 | `srs-fr-05-vu-viec.md:1492` — mã DB không bao giờ xuất hiện trên giao diện, phải dịch sang nhãn tiếng Việt theo bảng `:1498-1509` | Giao diện hiện nhãn tiếng Việt ("Đang xử lý"/"Hoàn thành"/"Từ chối"), mã enum chỉ nằm trong tham số request | ✅ |

## 4. Verdict từng ý

### Ý A — "dropdown thiếu giá trị so với nhóm Quản lý vụ việc" → **BA confirm**

Đối tác **quan sát đúng thực tế**: dropdown thật sự chỉ có 3 giá trị, ít hơn tập 12 trạng thái vụ việc
(`srs-fr-05-vu-viec.md:1498-1509`). Nhưng `SCR-IV-03:1578` **cố ý** quy định tập **rút gọn** cho riêng
tab này, không phải toàn bộ enum. Phần mềm bám tập rút gọn ⇒ không lệch đặc tả màn hình.
Kỳ vọng đối tác (đủ 12 giá trị) ≠ SRS ⇒ bất đồng **ĐẶC TẢ**, không phải bất đồng **THỰC TẾ**.
QA_VERIFY_PROTOCOL §Verdict: ca này là `BA confirm`, **CẤM `Reject`**.

### Ý B — nhãn `"Đã hủy"` trong SRS là nhãn mồ côi → **BA confirm**

- SRS `SCR-IV-03:1578` nguyên văn ghi `"Đã hủy"` (đã mở file verify, không dựa trí nhớ).
- Bảng ánh xạ mã DB → nhãn UI `srs-fr-05-vu-viec.md:1498-1509` liệt kê 12 trạng thái, **không có
  "Đã hủy"**; giá trị gần nhất là `TU_CHOI` → nhãn **"Từ chối"**.
- Web hiển thị **"Từ chối"** và gửi `trangThaiVv=TU_CHOI` ⇒ web **khớp bảng ánh xạ `:1509`**, chỉ lệch
  nguyên văn `:1578`. Nói cách khác, ở điểm này **web đúng hơn SRS**.
- ⇒ Hai chỗ trong SRS mâu thuẫn nhau ⇒ `BA confirm`, không log lỗi cho dev.

> **Đính chính note dev:** dev viết ở R126 rằng SRS `:1578` ghi *"Tất cả/Đang xử lý/Hoàn thành/**Từ chối**"*.
> Nguyên văn `:1578` là **"Đã hủy"**, không phải "Từ chối". Dev đã mô tả **giao diện đang chạy** rồi gán
> cho SRS. Kết luận cuối của dev (tập rút gọn là chủ ý) vẫn đúng, nhưng trích dẫn thì sai —
> nếu không kiểm lại thì chính điểm mâu thuẫn ở ý B sẽ bị bỏ qua.

### Ý C — bộ lọc chỉ phủ 2/6 bản ghi thật → **BA confirm** (là bằng chứng cho câu hỏi BA, không phải lỗi phần mềm)

Đo thật trên `TVV-BTP-TW-0002` (baseline 6 dòng):

| Giá trị chọn | Tham số gửi BE | Số dòng trả về | Mã vụ việc |
|---|---|:-:|---|
| *(không lọc)* | — | **6** | cả 6 |
| Đang xử lý | `trangThaiVv=DANG_XU_LY` | 1 | `VV-BTP-TW-20260712-004` |
| Hoàn thành | `trangThaiVv=HOAN_THANH` | 1 | `VV-BTP-TW-20260712-005` |
| Từ chối | `trangThaiVv=TU_CHOI` | **0** | — |

⇒ Tổng số bản ghi chạm tới được bằng bộ lọc: **2/6**. Bốn vụ việc **không giá trị nào lọc ra được**:
`DA_DUYET` ×1 (`VV-BTP-TW-20260730-002`), `DA_DANH_GIA` ×2 (`VV-BTP-TW-20260730-001`,
`VV-BTP-TW-20260712-001`), `DA_PHAN_CONG` ×1 (`VV-BTP-TW-20260712-003`).

Đây là **hệ quả của chính tập rút gọn mà SRS quy định**, không phải phần mềm làm sai SRS ⇒ không log
`Open`. Nhưng nó là số liệu làm câu hỏi BA trở nên cụ thể: tập rút gọn hiện không phủ được 2/3 dữ liệu
mà chính tab này đang hiển thị.

### Ý D — bộ lọc là **chọn đơn** trong khi SRS ghi **"chọn nhiều"** → **Open** (BUG-QLLSHTCTVV_04)

`SCR-IV-03:1578` ghi rõ `Trạng thái vụ việc (**chọn nhiều**: …)`. Web chỉ giữ 1 giá trị tại một thời điểm.
Xác minh 3 cách độc lập ở §5. Đây là clause SRS cụ thể mà phần mềm không đáp ứng ⇒ `Open`.

**Đối chiếu chéo củng cố:** SRS dùng đúng cụm "dropdown chọn nhiều" như một **kiểu điều khiển chính
thức** ở `:1516` (Tổ chức đối tác) và `:1517` (Lĩnh vực pháp luật), và lặp lại nguyên văn cụm
`(chọn nhiều: "Tất cả" / "Đang xử lý" / "Hoàn thành" / "Đã hủy")` ở `:1856` cho tab "Vụ việc đã hỗ trợ"
của màn Người hỗ trợ pháp lý. Tức "chọn nhiều" là quy định có chủ ý, lặp ở 2 màn, không phải chữ thừa.

**Verdict TỔNG = `Open`** (theo §"1 case gộp nhiều lỗi con": ≥1 ý Open → tổng Open).
Ý đối tác nêu (ý A) tự nó là `BA confirm` — note gửi đối tác nói rõ tách bạch điều này.

## 5. Xác minh ý D bằng 3 phương pháp độc lập (postmortem C2 — bug candidate ≠ bug)

| # | Phương pháp | Kết quả |
|---|---|---|
| 1 | Đọc lớp CSS của điều khiển | `ant-select ... **ant-select-single** ant-select-show-arrow` — không có `ant-select-multiple` |
| 2 | **Thao tác thật**: chọn "Đang xử lý" rồi chọn tiếp "Hoàn thành" | Giá trị sau **đè** giá trị trước: ô lọc hiện "Hoàn thành" (không phải 2 thẻ), request chỉ mang `trangThaiVv=HOAN_THANH`, bảng còn 1 dòng. Không tích lũy |
| 3 | Đọc thuộc tính trợ năng của danh sách | `aria-multiselectable` = `null`; **0** checkbox trong dropdown; **0** thẻ tag trong ô lọc |

Ba phương pháp cùng kết luận ⇒ đủ điều kiện log (không mâu thuẫn giữa các phép đo).

> Ghi chú kỹ thuật cho lần sau: bản dựng này render ô select bằng `.ant-select-content`,
> **không** phải `.ant-select-selector` như thư viện selector cũ ghi. Selector cũ trả `null`.

## 6. Ảnh đã chụp — và đã MỞ ĐỌC (postmortem A2)

| Ảnh | Nội dung đọc được |
|---|---|
| `image/QLLSHTCTVV_04-web-dropdown-3option.png` | Dropdown mở, đúng **3 mục** "Đang xử lý"/"Hoàn thành"/"Từ chối", không có "Tất cả"/"Đã hủy". Thẻ thống kê: Tổng 6 · Hoàn thành 3 · Điểm TB **8.9**. Header: `CB Nghiệp vụ - Trung ương #02 · CB_NV_TW`, `BTP · TW`, bản dựng `HTPLDN · V1.0.5` |
| `image/QLLSHTCTVV_04-web-chondon-de-gia-tri.png` | Ô lọc chỉ chứa **1** giá trị "Hoàn thành" kèm nút xóa ⊗; dropdown mở, chỉ 1 mục được tô sáng, **không có checkbox**; bảng còn 1 dòng "1-1 / 1 mục"; thẻ thống kê đổi theo bộ lọc (Tổng 1 · Hoàn thành 1 · Điểm TB —) |

## 7. Quan sát ngoài phạm vi

- **Điểm trung bình 8.9 / điểm từng vụ `"9.0"`, `"8.7"`** (thang 10 đổ vào ô hiển thị thang 5 theo
  `:1578` mục (c) "Điểm trung bình: {X}/5"). **Đã được log ở case 125** — `BUG-QLLSHTCTVV_03-B`.
  Đáng ghi nhận thêm: ảnh bằng chứng của **chính đối tác** cũng hiện "Điểm trung bình **8.3**"
  ⇒ lỗi này tồn tại trên cả môi trường của đối tác, không phải đặc thù env QA. Không log trùng.
- **Console 0 lỗi / 0 cảnh báo.** Network 26 request, toàn 200/304, không 4xx/5xx.
  Mỗi lần đổi bộ lọc phát **đúng 1 request** — không có hiện tượng gọi lặp.
- Bảng "Hợp đồng tư vấn" ngay dưới cùng tab **có** cột "Trạng thái" — đối chứng hữu ích cho câu hỏi
  BA của case 125 (ý "thiếu cột Trạng thái" ở bảng Lịch sử hỗ trợ).

## 8. Dữ liệu để lại trên môi trường

Không tạo / sửa / xóa bản ghi nào. Bộ lọc đã được **gỡ về trạng thái ban đầu** (ô "Trạng thái vụ việc"
trống, bảng trả về đủ 6/6 dòng). Hàm `fetch` bị vá tạm để đếm request đã được **khôi phục nguyên bản**.
