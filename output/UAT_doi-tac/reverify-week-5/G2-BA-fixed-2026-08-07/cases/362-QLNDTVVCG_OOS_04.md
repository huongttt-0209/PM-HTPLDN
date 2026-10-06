# Dòng 362 — `QLNDTVVCG_OOS_04` — Nhật ký thao tác của lượt "CG từ chối phân công" có mang lý do không

**Verdict: ✅ Test done** (bug gốc hết — đủ cả 4 điều kiện của phiếu tiêu chí)

---

## 1. Bug gốc là gì

Nguyên văn ô `Kết quả thực tế` (cột L):

> Nhật ký có ghi thao tác nhưng **mất lý do**, đo bằng 2 đường:
> - Bảng "Nhật ký thao tác" trên màn chi tiết hiển thị "06/08/2026 09:31 · **Cập nhật** · QA TVV Seed28
>   Active (qa_tvvseed28) · Chuyên gia tư vấn, Tư vấn viên" — hành động ghi chung chung là "Cập nhật",
>   **không có cột hay dòng nào chứa lý do**; bảng cũng **không phân biệt được thao tác từ chối với thao
>   tác chấp nhận**.
> - Bản ghi nhật ký đọc trực tiếp từ hệ thống có **18 trường** (…) — **không có trường nào mang lý do**.

Ba triệu chứng con: **(1)** nhãn hành động bị gộp thành "Cập nhật" · **(2)** giao diện không có chỗ nào
chứa lý do · **(3)** bản ghi nhật ký ở tầng dữ liệu không có trường lý do.

**Đạt khi** (theo `criteria/362-QLNDTVVCG_OOS_04.md`) đủ CẢ BỐN: có dòng nhật ký cho lượt từ chối · dòng
đó mang lý do · nhãn hành động tách riêng khỏi "Cập nhật" · lý do không bị mất/ghi đè sau khi hồ sơ được
phân công lại.

---

## 2. Đo thế nào

| Hạng mục | Giá trị |
|---|---|
| Môi trường | `https://18.143.165.120.nip.io` |
| Bó mã FE | `assets/index-BbPPdate.js` · `GET /` last-modified `Fri, 07 Aug 2026 06:47:57 GMT` (nhãn sidebar `HTPLDN · V1.0.10`) |
| Bản ghi | `TVCS-20260803-0003` (id `099a739d-02f6-4823-b2f8-1ac9cd2b60e6`) — chính bản ghi ghi trong phiếu |
| Vai trò thao tác từ chối | `qa_tvvseed28` / `Test@1234` — "QA TVV Seed28 Active", Tư vấn viên · **Chuyên gia tư vấn**, cùng đơn vị Cục Bổ trợ tư pháp – BTP · TW |
| Vai trò đọc nhật ký (quyết định) | `cbnv_tw_01` / `Test@1234` — Cán bộ Nghiệp vụ Trung ương |
| Giờ đo | 07/08/2026 16:57 (phân công) · 16:59 (từ chối) · 17:03–17:06 (đọc nhật ký 2 vai trò) |

### 2.1 Đã seed gì (khai báo đầy đủ)

Không có sẵn bản ghi TVCS nào ở trạng thái **Phân công** gắn với tài khoản chuyên gia mà lượt này có mật
khẩu. Seed **tối thiểu, tự hoàn nguyên**:

1. Đăng nhập `cbnv_tw_01` → mở `TVCS-20260803-0003` (đang ở `Tiếp nhận`) → bấm nút thật **[Phân công]**
   trên giao diện → chọn "QA TVV Seed28 Active" → trạng thái sang **Phân công** (16:57).
2. Đăng nhập `qa_tvvseed28` → bấm nút thật **[Từ chối nhiệm vụ]** → nhập lý do → **[Từ chối]** (16:59).
3. Sau bước 2 bản ghi **quay lại đúng trạng thái `Tiếp nhận`, `chuyenGiaId = null`** như trước khi seed
   (kiểm chứng: `GET /api/v1/noi-dung-tu-van-cs/099a739d-…` → `{"trangThai":"TIEP_NHAN","chuyenGiaId":null}`).

⇒ **Không tạo bản ghi nghiệp vụ mới, không xoá, không sửa dữ liệu khác.** Ròng lại trạng thái hồ sơ
không đổi; chỉ phát sinh 2 dòng nhật ký (bản chất của phép đo).

**Lý do từ chối nhập vào** — chuỗi có dấu nhận dạng riêng để chống nhầm với lượt đo cũ:

```
QA G2 OOS04 - ly do tu choi luot moi luc 20260807-1700 - ma nhan dang RJ7A9K
```

---

## 3. Thấy gì

### 3.1 Đọc bằng vai trò nội bộ `cbnv_tw_01` — khối "Nhật ký thao tác" (đã MỞ accordion)

Accordion "Nhật ký thao tác" ở trạng thái **thu gọn** khi vào màn — đã bấm mở trước khi đọc.

| Thời gian | Hành động | Người thực hiện | Lý do |
|---|---|---|---|
| 07/08/2026 16:59 | **Từ chối phân công** | QA TVV Seed28 Active (qa_tvvseed28) | `QA G2 OOS04 - ly do tu choi luot moi luc 20260807-1700 - ma nhan dang RJ7A9K` |
| 07/08/2026 16:57 | Phân công | CB Nghiệp vụ - Trung ương #01 (cbnv_tw_01) | — |
| 07/08/2026 00:45 | **Từ chối phân công** | QA TVV Seed28 Active (qa_tvvseed28) | `QA verify 120 v1.0.10 - khong dung linh vuc chuyen mon, de nghi phan cong nguoi khac` |
| 06/08/2026 09:31 | Cập nhật | QA TVV Seed28 Active (qa_tvvseed28) | — |
| 06/08/2026 09:28 | Phân công | CB Nghiệp vụ - Trung ương (cbnv_tw) | — |
| 03/08/2026 21:58 | Xem tư liệu pháp lý | QA TVV Seed28 Active (qa_tvvseed28) | — |
| 03/08/2026 20:24 | Cập nhật | QA TVV Seed28 Active (qa_tvvseed28) | — |
| 03/08/2026 20:21 | Phân công | CB Nghiệp vụ - Trung ương #04 (cbnv_tw_04) | — |
| 03/08/2026 20:19 | Tạo mới | CB Nghiệp vụ - Trung ương #04 (cbnv_tw_04) | — |

Khối nhật ký nay có hẳn **cột "Lý do"**; nhãn hành động **"Từ chối phân công"** đứng riêng, khác hẳn nhãn
**"Cập nhật"** và khác cả **"Phân công"** / **"Tạo mới"** / **"Xem tư liệu pháp lý"**.

### 3.2 Đối chiếu bằng đường thứ hai — đọc bản ghi nhật ký ở tầng dữ liệu

`GET /api/v1/noi-dung-tu-van-cs/099a739d-…/audit-logs?pageSize=100&sort=thoiGian&order=desc` → **200**.

Danh sách trường của một bản ghi nhật ký nay là **19 trường**, có thêm đúng trường còn thiếu:

```
id · entityType · entityId · hanhDong · nguoiThucHienId · systemActor · consumerId · thoiGian ·
ipAddress · endpoint · responseCode · sessionId · module · nguoiThucHienUsername · nguoiThucHienHoTen ·
donViId · donViTen · nguoiThucHienVaiTro · lyDo   ← trường mới
```

Hai bản ghi từ chối, mỗi bản mang **lý do riêng của chính nó**:

| `thoiGian` | `hanhDong` | `lyDo` |
|---|---|---|
| `2026-08-07T09:59:19.194Z` | `TU_CHOI_PHAN_CONG` | `QA G2 OOS04 - ly do tu choi luot moi luc 20260807-1700 - ma nhan dang RJ7A9K` |
| `2026-08-07T09:57:27.415Z` | `PHAN_CONG` | *(trống)* |
| `2026-08-06T17:45:26.342Z` | `TU_CHOI_PHAN_CONG` | `QA verify 120 v1.0.10 - khong dung linh vuc chuyen mon, de nghi phan cong nguoi khac` |
| `2026-08-06T02:31:47.124Z` | `UPDATE` | *(trống)* |

Mã hành động ở tầng dữ liệu cũng tách bạch: `TU_CHOI_PHAN_CONG` ≠ `UPDATE`.

### 3.3 Đọc lại chính hồ sơ đó bằng vai trò CG `qa_tvvseed28`

Cùng 9 dòng nhật ký, cùng nhãn "Từ chối phân công", nhưng **cột "Lý do" hiển thị "—" ở tất cả các dòng**
— chuyên gia không đọc được nội dung lý do. Khớp đúng tiêu chí chấp nhận
`srs-fr-12-tv-chuyen-sau.md:348`: *"Given CG mở chính hồ sơ đó When xem khối Nhật ký thao tác Then thấy
đủ các dòng nhật ký nhưng **không** thấy dòng phụ 'Lý do'"*.

---

## 4. Verdict + vì sao

**✅ Test done.** Bốn điều kiện của phiếu tiêu chí đều đạt:

| # | Điều kiện | Kết quả | Bằng chứng |
|---|---|---|---|
| 1 | Có dòng nhật ký cho lượt từ chối | ✅ | dòng 07/08/2026 16:59 (§3.1) |
| 2 | Dòng đó mang lý do | ✅ | đúng nguyên văn chuỗi nhận dạng `…RJ7A9K` ở cả giao diện lẫn trường `lyDo` (§3.1, §3.2) |
| 3 | Nhãn hành động tách khỏi "Cập nhật" | ✅ | giao diện "Từ chối phân công"; tầng dữ liệu `TU_CHOI_PHAN_CONG` ≠ `UPDATE` |
| 4 | Lý do không mất/ghi đè khi hồ sơ được phân công lại | ✅ | lượt từ chối 07/08 00:45 vẫn giữ nguyên lý do riêng của nó **sau khi** hồ sơ được phân công lại lúc 16:57 và bị từ chối lần nữa lúc 16:59 với lý do khác hẳn — chứng tỏ lý do lưu theo từng dòng nhật ký, không phải một ô dùng chung bị đè |

Cả ba triệu chứng con của cột L đều không còn tái hiện: nhãn không còn bị gộp, giao diện đã có chỗ chứa
lý do, tầng dữ liệu đã có trường mang lý do.

**Căn cứ đặc tả** (số dòng do chính lượt này mở file đọc ngày 07/08/2026 — bản SRS bị sửa 06/08/2026
22:52 nên mọi số dòng trong `00-BRIEF.md`, phiếu BA và ô verify cũ đều đã lệch):

- `srs-fr-12-tv-chuyen-sau.md:204` — bước 6 luồng "CG từ chối": *"Ghi nhật ký thao tác (kèm lý do từ
  chối) — **lý do hiển thị trên khối Nhật ký thao tác của hồ sơ** (SCR-X1-02 thành phần 8), nhãn hành
  động là 'Từ chối' (không gộp vào 'Cập nhật')"* `[BA chốt 2026-08-06]`.
- `srs-fr-12-tv-chuyen-sau.md:1173` — thành phần 8 màn SCR-X1-02: *"Riêng hành động Từ chối … thêm dòng
  phụ 'Lý do: {nội dung}' … **Dòng phụ Lý do chỉ hiện với vai trò nội bộ** (CB NV, CB PD, NHT theo phạm
  vi đơn vị); **KHÔNG** hiện với người trong mạng lưới tư vấn … thao tác Từ chối phải có nhãn riêng,
  không gộp vào 'Cập nhật'"* `[BA chốt 2026-08-06]`.
- `srs-v3.5.md:1442` — bảng action-level `TU_VAN_CHUYEN_SAU`, dòng `TVCS_REJECT`: *"Từ chối nhận việc
  (nhãn hiển thị trên Nhật ký thao tác: 'Từ chối', KHÔNG gộp vào 'Cập nhật')"*.
- Tiêu chí chấp nhận `srs-fr-12-tv-chuyen-sau.md:347` (vai trò nội bộ thấy lý do) và `:348` (vai trò CG
  KHÔNG thấy lý do) — hệ thống làm đúng cả hai vế.

> ⚠️ **Không dùng `BR-DATA-05` làm căn cứ đòi lý do.** BR-DATA-05 chỉ quy định phải ghi nhật ký, không
> quy định trường nào. Căn cứ đòi lý do nằm ở chính câu chữ `:204` và `:1173` nêu trên.

### Điểm khác biệt về cách trình bày — KHÔNG chấm lỗi

Đặc tả `:1173` mô tả khối nhật ký là `timeline` và gọi phần lý do là **"dòng phụ"**; hệ thống hiện dựng
khối này thành **bảng có cột "Lý do"**. Khác biệt này thuộc hình thức trình bày của cả khối nhật ký,
**không** nằm trong triệu chứng ghi ở cột L (mất lý do / gộp nhãn / thiếu trường), nên theo §PHẠM VI của
`00-BRIEF.md` không dùng để giữ phiếu ở trạng thái còn lỗi. Nội dung bắt buộc — lý do, có kiểm soát theo
vai trò — đã hiện đúng và đủ.

---

## 5. Bằng chứng

| Tệp | Nội dung |
|---|---|
| `image/QLNDTVVCG_OOS_04-02-nhat-ky-vai-tro-CBNV-co-ly-do.png` | Nhật ký đọc bằng `cbnv_tw_01`: dòng 16:59 nhãn "Từ chối phân công" + cột "Lý do" có nội dung |
| `image/QLNDTVVCG_OOS_04-01-nhat-ky-vai-tro-CG.png` | Cùng hồ sơ đọc bằng `qa_tvvseed28` (CG): đủ dòng nhật ký nhưng cột "Lý do" toàn "—" |
