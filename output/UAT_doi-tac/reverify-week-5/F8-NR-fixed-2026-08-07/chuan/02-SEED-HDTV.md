# Seed dữ liệu nền — cụm 18 phiếu `QLHDTVVCG`

**Ngày:** 2026-08-07 13:2x · **Env:** `https://18.143.165.120.nip.io` (nội bộ) · **Tài khoản seed:** `cbnv_tw_03`
**Kết quả máy đọc được:** [`02-SEED-HDTV-ket-qua.json`](02-SEED-HDTV-ket-qua.json)

---

## 0. Phát hiện quyết định — **chốt chặn ngữ cảnh là CỐ Ý, không phải lỗi phân quyền**

```
GET /api/v1/hop-dong-tu-vans            (không kèm tham số ngữ cảnh)
→ HTTP 403  ERR-PERM-SYS-00-01
  "Hợp đồng tư vấn chỉ truy cập trong ngữ cảnh vụ việc/tư vấn viên/tổ chức."
```

Đây là **chốt chặn dev dựng có chủ đích**, khớp `srs-fr-14-hop-dong-tv.md:266` + `:268`
(*"không còn là mục menu riêng"*, *"route standalone … không được QA coi là luồng chính"*).

⇒ **403 KHÔNG được log thành bug phân quyền.** Cùng phiên `cbnv_tw_03` gọi **có** tham số ngữ cảnh
thì trả **HTTP 200** — chứng minh không phải vấn đề quyền.

Tham số ngữ cảnh hợp lệ (đọc từ `/api/docs-json`, **không đoán**):
`vuViecId` · `tuVanVienId` · `toChucTuVanId` — kèm `trangThai` · `tuNgay` · `denNgay`.

> Việc này **không đổi quan hệ đã khóa** ở [`00-TONG-HOP-QLHDTVVCG.md`](00-TONG-HOP-QLHDTVVCG.md) §5.1 —
> theo luật khóa 5, chỉ **dòng SRS mới đọc được** mới đổi được `MATCH`/`DIFF`/`GAP`. Đây là dữ kiện
> **củng cố câu hỏi BA**, và là **tiền đề/đường đi** cho người đo, không phải vế chấm.

---

## 1. Tình trạng TRƯỚC khi seed

| Hạng mục | Số lượng | Nguồn |
|---|---|---|
| **Hợp đồng tư vấn** | **0** | quét 20 vụ việc + 10 TVV theo ngữ cảnh → `n=0` toàn bộ (HTTP 200, tức truy vấn hợp lệ) |
| Vụ việc | 60 | `GET /api/v1/vu-viecs` (duyệt hết trang) |
| Vụ việc có tên DN > 40 ký tự | 3 | `VV-BTP-TW-20260804-002/003/004` — DN `"Cong ty QA R3 kiem trang thai sau dang ky"` (41 ký tự) |
| Tư vấn viên | 44 · **7 `HOAT_DONG`** | phân bố: `TU_CHOI` 12 · `MOI_DANG_KY` 9 · `CHO_KICH_HOAT` 8 · `HOAT_DONG` 7 · `YEU_CAU_BO_SUNG` 5 · `CHO_PHE_DUYET` 2 · `DANG_THAM_DINH` 1 |

⇒ **D7 đã đủ** (≥3 vụ việc). **D1–D6 phải seed toàn bộ.**

---

## 2. Nguyên tắc seed — **KHÔNG seed HĐ-1 bằng API**

Hợp đồng "đầy đủ" HĐ-1 (D2+D3+D4) **do phiếu `_15` tạo bằng giao diện thật**, vì *tạo hợp đồng chính là
hành động đang tranh chấp* của phiếu đó. Seed sẵn bằng API rồi chấm `_15` bằng cách nhìn bản ghi có sẵn
= **Pass bằng quan sát tĩnh**, đúng thứ yêu cầu cấm.

API chỉ dựng **hợp đồng nền** — thứ mà các phiếu khác cần *tồn tại*, không phải thứ chúng đo.

**Ràng buộc phái sinh từ chốt chặn ngữ cảnh:** hợp đồng không gắn vụ việc **lẫn** tư vấn viên thì
**không màn nào với tới được**. Nên HĐ-2 (phải sạch vụ việc để `_17` xóa) vẫn **buộc gắn 1 tư vấn viên**,
nếu không nó vô hình. Điều này **không** phá điều kiện của `_17` — `_17` yêu cầu *0 vụ việc liên kết*.

---

## 3. Năm hợp đồng nền đã tạo (đã đọc lại xác nhận)

| Mã | Nhãn | Tên hợp đồng | Trạng thái | Kết thúc | Tư vấn viên | Phục vụ phiếu |
|---|---|---|---|---|---|---|
| `HDTV-20260807-0001` | **HĐ-2** | Hợp đồng tư vấn pháp lý thường xuyên cho doanh nghiệp nhỏ và vừa năm 2026 (73 ký tự) | `DANG_THUC_HIEN` | 2026-12-05 | Chuyên gia UAT QLNDTVVCG 38 | **`_17`** (xóa mềm — **cố ý 0 vụ việc**) |
| `HDTV-20260807-0002` | **HĐ-3** | Hợp đồng tư vấn chuyên sâu lĩnh vực sở hữu trí tuệ và chuyển giao công nghệ (75 ký tự) | `DANG_THUC_HIEN` | 2027-02-23 | QA TVV PheDuyet TW R19 | **`_22` C5** (gắn chéo cùng 1 vụ việc vào 2 hợp đồng) |
| `HDTV-20260807-0003` | **HĐ-4** | Hợp đồng tư vấn pháp luật lao động và bảo hiểm xã hội cho doanh nghiệp siêu nhỏ (79 ký tự) | `DANG_THUC_HIEN` | **2026-08-25** | Chuyên gia UAT QLNDTVVCG 38 | `_02` C3 — **ngưỡng ≤30 ngày** (`:288` tô đỏ) |
| `HDTV-20260807-0004` | **HĐ-5** | Hợp đồng tư vấn tái cấu trúc doanh nghiệp giai đoạn hai năm 2025 (64 ký tự) | **`HOAN_THANH`** | 2026-07-08 | QA TVV PheDuyet TW R19 | bộ lọc trạng thái có ≥2 giá trị khác nhau |
| `HDTV-20260807-0005` | **HĐ-6** | Hợp đồng tư vấn xác lập quyền sở hữu trí tuệ đối với kiểu dáng công nghiệp (74 ký tự) | `DANG_THUC_HIEN` | 2026-11-05 | Chuyên gia UAT QLNDTVVCG 38 | `_03` — cặp khớp từ khóa với HĐ-3 |

**Mọi tên đều > 30 ký tự** (64–79) ⇒ phục vụ vế "tên dài không tràn/đè" (`_02` C4). `ghiChu` mang dấu
`QA-F8-SEED-20260807` để phân biệt với dữ liệu đối tác.

### Thiết kế từ khóa cho `_03` / `_04`

| Từ khóa | Khớp | Bị loại | Dùng cho |
|---|---|---|---|
| `sở hữu trí tuệ` | **2** (HĐ-3, HĐ-6) | 3 | **`_03`** — chứng minh có lọc thật, không phải trả về tất cả |
| `lao động` | 1 (HĐ-4) | 4 | dự phòng |
| `tái cấu trúc` | 1 (HĐ-5) | 4 | dự phòng |
| chuỗi vô nghĩa (vd `zzqq`) | 0 | 5 | **`_04`** — không có kết quả |

> ⚠️ Chưa biết ô tìm kiếm quét những trường nào (tên / số HĐ / bên B) — **đó chính là thứ `_03` phải đo**,
> không được giả định trước.

---

## 4. Mã hợp đồng sinh **khi lưu**, khuôn `HDTV-YYYYMMDD-NNNN`

5 bản ghi nhận mã `HDTV-20260807-0001` … `-0005` theo đúng thứ tự tạo. Có endpoint riêng
`GET /api/v1/hop-dong-tu-vans/ma-preview` (trả HTTP 200).

> Liên quan vế **`_13` C2** (`GAP`: `:290` khai "Mã (auto)" như trường trên biểu mẫu ↔ `:119` xếp sinh mã
> vào bước xử lý **khi lưu**). Dữ kiện này **không** đổi `GAP` → `MATCH`; nó là **manh mối để đo** xem
> giao diện có gọi `ma-preview` lúc mở biểu mẫu hay không, và là dữ kiện đưa vào câu hỏi BA.

---

## 5. Tình trạng sau khi chạy `_15` (cập nhật 14:5x)

**HĐ-1 = `HDTV-20260807-0006`** (`d16487f4-3ccc-4629-8e07-bb63ea9a12be`) — tạo **bằng giao diện thật** ở
phiếu `_15`, ngày kết thúc **25/08/2026** (18 ngày ⇒ rơi đúng ngưỡng ≤30 ngày của `:288`).

| Mã | Yêu cầu | Tình trạng | Dựng ở đâu |
|---|---|---|---|
| **D2** | HĐ-1 đầy đủ + **≥1 tệp đính kèm** | ✅ **ĐỦ** — xem §7 | `_15` (giao diện) + §7 (API) |
| **D3** | HĐ-1 có ≥2 vụ việc liên kết, ≥1 tên DN > 40 ký tự | ✅ **ĐỦ — 3 vụ việc** `VV-BTP-TW-20260804-002/003/004` | `_15` (chọn lúc tạo) |
| **D4** | ≥2 mốc tiến độ + ≥2 giai đoạn thanh toán, ≥1 **đã thanh toán** | ⚠️ **mới có 1 + 1, chưa có dòng đã thanh toán** | **`_24`** (mốc) + **`_26`** (thanh toán) |
| **D8** | Bộ tệp fixture thật | ✅ `files/fixture-hdtv/` — 4 tệp, kiểm bằng chữ ký nhị phân + mở đọc lại | — |

---

## 6. 🔴 Phát hiện ở `_15`: **không đính kèm được lúc tạo**

Ở chế độ **Thêm mới**, mục "Tài liệu đính kèm" **không có ô chọn tệp** (`input[type=file]` đếm được = **0**),
chỉ hiện dòng *"Vui lòng lưu hợp đồng trước khi đính kèm tài liệu."* Chỉ chế độ **Sửa** mới có vùng kéo-thả.
Khớp với thiết kế API: điểm nạp là `POST /hop-dong-tu-vans/{id}/files` ⇒ **buộc có `id` trước**.

**Đặc tả đứng ở đâu:**

| Chỗ | Có nhắc tệp đính kèm? |
|---|---|
| `:92` bảng Inputs | **có** — `file_dinh_kem · file[] · N (không bắt buộc) · "Upload nhiều file"` |
| `:290` bảng thành phần biểu mẫu | **có** — "File đính kèm", trang **thêm/sửa** |
| `:122`, `:123` **bước xử lý khi lưu** | **KHÔNG** — chỉ mốc tiến độ + thanh toán + liên kết vụ việc |
| `:159`–`:162` **Outputs** | **KHÔNG** — 4 mục, không có tệp đính kèm |

⇒ Đặc tả **có** trường tệp trên biểu mẫu nhưng **không phát biểu** tệp phải lưu **cùng lúc** tạo bản ghi.
Cột `Kết quả mong đợi` của phiếu thì đòi *"cùng toàn bộ … tệp đính kèm đã nhập"*.
**Quan hệ cho riêng phần này = `GAP`** ⇒ CẤM Pass, **CẤM kết "lỗi dev"**, đưa vào câu hỏi BA.

---

## 7. Nạp tệp cho HĐ-1 bằng **API** — quyết định của điều phối, có lý do

**Đã làm lúc 14:57**, phiên `cbnv_tw_05` (không dùng `_03` vì nhóm đo đang dùng — QĐ-05):

```
POST /api/v1/hop-dong-tu-vans/d16487f4-…/files   (multipart, tên trường "file")  → HTTP 201
  → id 2fa6f9dc-a4fe-4b18-80cb-27f61d7edf7a · tenFile "phu-luc-hop-dong.pdf"
    dungLuong 1248 · loaiFile application/pdf · trangThaiQuet "SACH"
Đọc lại GET /hop-dong-tu-vans/d16487f4-… → fileDinhKem = [ …đúng 1 phần tử trên… ]
```

**Vì sao API mà không dùng chức năng Sửa trên giao diện:** nạp tệp **không** phải hành động đang tranh chấp
của phiếu nào; còn **`_21` (đợt C) tranh chấp ở chính thao tác *lưu bản sửa*** và vế C3 của nó đo *"lưu bản
sửa có thay thế toàn bộ 4 danh sách con không"*. Dùng Sửa để đính kèm bây giờ = **tiêu thụ trước** hành động
đó và làm mờ phép đo. Tệp phải **có sẵn trước** `_21` thì C3 mới đo được.

**Không giấu phát hiện §6:** `_15` đã đo và ghi xong việc không đính kèm được lúc tạo **trước khi** seed này
chạy. Seed đây chỉ dựng tiền đề cho `_21`/`_08`/`_19`.

**Tên trường `file`** — tài liệu `/api/docs-json` **không khai `requestBody`** cho điểm nạp này; đã thử lần
lượt `file` → trúng ngay lần đầu. Ghi lại để người sau khỏi đoán.

---

## 6. Dữ liệu đã thay đổi trên môi trường (khai bắt buộc)

| Đổi gì | Bản ghi | Env | Lúc |
|---|---|---|---|
| **Tạo mới 5 hợp đồng tư vấn** (`HDTV-20260807-0001`…`-0005`) qua `POST /api/v1/hop-dong-tu-vans`, phiên `cbnv_tw_03` | như bảng §3 | `18.143.165.120.nip.io` (nội bộ) | 2026-08-07 13:2x |

- **Không** đụng dữ liệu đối tác. **Không** đụng vụ việc / tư vấn viên nào (chỉ tham chiếu `tuVanVienId`).
- Trước khi seed đã quét chống trùng: **0 hợp đồng** tồn tại ⇒ toàn bộ 5 bản ghi là của QA.
- HĐ-2 sẽ **bị xóa mềm thật** ở phiếu `_17` — đó là mục đích tạo ra nó.
