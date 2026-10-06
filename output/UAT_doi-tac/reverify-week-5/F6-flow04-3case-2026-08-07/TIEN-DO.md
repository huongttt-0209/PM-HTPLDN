# FLOW 04 · lô F6-flow04-3case-2026-08-07 — 3 case

**Bảng:** `1OKBN2otlmdZ44THkmhtsn-_63M2Boh7zQwearwjYR3s` · tab `bug` (gid 1714340219)
**Môi trường đo:** `https://18.143.165.120.nip.io` (env NỘI BỘ) · MailHog `http://18.143.165.120:8025`
**SRS nguồn chuẩn (prompt chỉ định):** `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/`
**Tài khoản:** bộ `_05` (`cbnv_tw_05` / `cbnv_dp_05` / … `Test@1234`) — nguồn `output/UAT_doi-tac/input/input.md`

**Ánh xạ ghi bảng (prompt quyết định, flow không được tự mở rộng):**

| Verdict logic Flow 04 | Ô `Trạng thái dev fix` (cột R) |
|---|---|
| Pass | `Test done` |
| Reopen | `Reopen` |
| Cần BA | `BA confirm` |

Diễn giải → ô `Kết quả verify` (cột T).
**Ô CHỈ ĐỌC, cấm ghi đè:** `Trạng thái` (N) · `Kết quả thực tế` (L) · `TKM phản hồi lần 1` (Q) · `DEV phản hồi lần 1` (S).

> ⚠️ Prompt KHÔNG cấp ô riêng cho ảnh bằng chứng vòng verify ⇒ không ghi cột `Ảnh/video verify`;
> link Drive xem được nhúng trong chính ô `Kết quả verify`.

---

## BƯỚC 0 — chốt phạm vi (đọc live 2026-08-07)

### Trạng thái bảng lúc bắt đầu

| Dòng | Mã TC | Mô tả | Trạng thái | Dopai | Trạng thái dev fix | TKM phản hồi lần 1 | DEV phản hồi lần 1 | Kết quả verify | Ảnh/vieo 1 |
|---:|---|---|---|---|---|---|---|---|---|
| 301 | QLTLPLCVV_22 | Tìm kiếm tư liệu hỗ trợ tiếng Việt **có dấu** | Fail | `N/R` | `Fixed` | *Màn hình không có chức năng* | *(trống)* | *(trống)* | `QLTLPLCVV_23.jpg` ✅ tải được |
| 302 | QLTLPLCVV_23 | Tìm kiếm hỗ trợ tiếng Việt **không dấu** | Fail | `N/R` | `Fixed` | *Màn hình không có chức năng* | *(trống)* | *(trống)* | `QLTLPLCVV_24.jpg` ✅ tải được |
| 35 | DKTGMLTVV_13 | Gửi đăng ký khi dữ liệu hợp lệ | Fail | `N/R` | `Fixed` | *(2 ý — xem dưới)* | *(trống)* | *(trống)* | `DKTGMLTVV_13.jpg` ✅ tải được |

Ô `TKM phản hồi lần 1` dòng 35 (nguyên văn, CHỈ ĐỌC):
> - Màn hình chức năng không có button Gửi đăng ký, chỉ có button Lưu là do tên button sai hay thiếu nút chức năng vậy ạ - BA xác nhận tên button sai
> - 25/7: Do các trường thông tin đang không đúng với thiết kế nên test sau

- Cột `Kết quả verify` **trống ở cả 3 dòng** ⇒ không có nội dung cũ để đè.
- Cột `Tác nhân` trống ⇒ vai trò suy từ bằng chứng đối tác (ảnh) + SRS, không tự chọn.

### Lệch mã ↔ tên tệp bằng chứng (ghi nhận, không tự sửa bảng)

⚠️ Dòng 301 mã `QLTLPLCVV_22` nhưng ảnh đính `QLTLPLCVV_23.jpg`; dòng 302 mã `QLTLPLCVV_23` ảnh `QLTLPLCVV_24.jpg`
(lệch 1 — đúng pattern renumber đã biết). Chuẩn chấm vì thế lấy theo **Mô tả + Các bước + KQ mong đợi của
chính dòng**, không lấy theo chuỗi mã.

🔴 **Hai ảnh `QLTLPLCVV_23.jpg` và `QLTLPLCVV_24.jpg` TRÙNG KHÍT** (md5 `3d926926a8bbdfd3352f9328d55c1c39`,
275103 bytes cả hai) ⇒ đối tác dùng **cùng một ảnh** cho cả hai dòng. Ảnh chỉ chứng minh *trạng thái màn*,
không phân biệt được vế "có dấu" với vế "không dấu" ⇒ **cấm suy 1 case ra case kia**, phải đo riêng từng vế
trên đúng màn (Flow 04 §Bước 0, luật "cùng chữ không có nghĩa cùng nguyên nhân").

### Phân nhánh Flow 03 vs Flow 04

Grep toàn bộ `output/` cho 3 mã + 2 mã tệp lệch:

| Mã TC | Có bug entry nội bộ? | Có khối `CÁCH VERIFY`? | Nhánh |
|---|---|---|---|
| QLTLPLCVV_22 | không (chỉ xuất hiện ở danh sách đối soát + BATCH-PLAN) | ❌ | **Flow 04** |
| QLTLPLCVV_23 | không | ❌ | **Flow 04** |
| DKTGMLTVV_13 | không | ❌ | **Flow 04** |

⇒ **3/3 đúng nhánh Flow 04.**

### Cổng bằng chứng

| Dòng | Bằng chứng | Đã mở xem full-res | Neo lấy được |
|---:|---|---|---|
| 301 | `partner-evidence/QLTLPLCVV_23.jpg` (275 KB) | ✅ | URL `htpldn-uat.ospgroup.vn/tv-chuyen-sau/287c1cd1-ea2e-4d17-8f2d-9be79d617167` · vai trò **CB_NV_TW** (`Cán bộ NV Trung ương`, BTP·TW) · section **"Tư liệu pháp luật"** trong màn chi tiết TVCS · bảng 7 cột (Tên tư liệu/Loại/Lĩnh vực/File/Trạng thái/Công khai lúc/Hành động) + nút `Thêm tư liệu`; **KHÔNG thấy ô nhập từ khóa / bộ lọc nào trong section** · 3 bản ghi (2 `Nháp`, 1 `Đã công khai`) · mốc 17/07/2026 21:09 · bản `HTPLDN · V1.0` |
| 302 | `partner-evidence/QLTLPLCVV_24.jpg` | ✅ (trùng ảnh dòng 301) | như trên |
| 35 | `partner-evidence/DKTGMLTVV_13.jpg` (202 KB) | ✅ | URL `htpldn-uat.ospgroup.vn/chuyen-gia-tvv/tao-moi` · vai trò **NHT** (`hương 3 NHT`, BTP·DP) · cuối form là cặp nút **`Hủy`** + **`Lưu`**, không có nút `Gửi đăng ký` · khối `File đính kèm (Bằng cấp / Chứng chỉ)` đã có 3 tệp pdf · mốc 08/07/2026 14:54 · bản `HTPLDN · V1.0` |

### Vân tay bản dựng (đo đầu lô)

Đo **2026-08-07** (`GET /` trên env nội bộ, `curl -sk`):

| Hạng mục | Giá trị |
|---|---|
| `GET /` last-modified | `Thu, 06 Aug 2026 17:39:54 GMT` |
| `GET /` etag | `W/"6a74c6ea-428"` |
| Bó mã FE | `assets/index-B2W2Krcs.js` · `assets/index-DVlgOkLg.css` |
| Bản dựng | **V1.0.9** — *(sửa 2026-08-07: dòng này ban đầu ghi `V1.0.10` do suy từ ghi chú lô `F5-flow04-2026-08-07`, KHÔNG phải đo. Đọc trực tiếp chuỗi ở chân sidebar trong 3 phiên đo của lô này — cả 3 đều là `HTPLDN · V1.0.9` trên cùng etag/bó mã ở trên. Mọi báo cáo của lô ghi giá trị **đo được** là V1.0.9.)* |
| Máy chủ | `nginx/1.27.5` sau `Caddy` |

### Giới hạn hiệu lực verdict

Đối tác đo trên env nghiệm thu `htpldn-uat.ospgroup.vn` bản `HTPLDN · V1.0`; lô này đo env nội bộ bản
`V1.0.9` ⇒ mọi verdict chỉ có hiệu lực cho bản dựng ghi ở bảng trên.

---

## Tiến độ

| # | Dòng | Mã TC | Giai đoạn A | Giai đoạn B | Verdict | Ghi bảng | Đọc lại |
|--:|---:|---|---|---|---|---|---|
| 1 | 301 | QLTLPLCVV_22 | ✅ [chuẩn](chuan/QLTLPLCVV-301-302.md) | ✅ [báo cáo](do/r301-QLTLPLCVV_22.md) | **Cần BA** | ✅ `BA confirm` + `Kết quả verify` | ✅ |
| 2 | 302 | QLTLPLCVV_23 | ✅ [chuẩn](chuan/QLTLPLCVV-301-302.md) | ✅ [báo cáo](do/r302-QLTLPLCVV_23.md) | **Cần BA** | ✅ `BA confirm` + `Kết quả verify` | ✅ |
| 3 | 35 | DKTGMLTVV_13 | ✅ [chuẩn](chuan/DKTGMLTVV_13-row35.md) | ✅ [báo cáo](do/r35-DKTGMLTVV_13.md) | **Cần BA** | ✅ `BA confirm` + `Kết quả verify` | ✅ |

**Xong 3/3 case.** Không case nào ra `Pass` — cả 3 đều có ít nhất một vế `DIFF`/`GAP` khóa từ Giai đoạn A,
nên theo Flow 04 verdict tối đa là `Cần BA`. Không case nào ra `Reopen`: mọi vế `MATCH` đều ĐẠT.

### Tổng hợp câu hỏi BA của lô (5 câu)

> **Bản gửi BA (đầy đủ, tự chứa): [`ba-confirmation-needed-F6-QLTLPLCVV-DKTGMLTVV-2026-08-07.md`](../ba-confirm/ba-confirmation-needed-F6-QLTLPLCVV-DKTGMLTVV-2026-08-07.md).**
> Bảng dưới chỉ là mục lục.

| Nguồn | Vế | Nội dung cần BA chốt |
|---|---|---|
| Dòng 301 + 302 | C1 (`GAP`) | Bổ sung ô tìm kiếm + bộ lọc của nhóm "Tư liệu pháp lý liên kết" vào SCR-X1-02 §Thành phần màn hình + tiêu chí chấp nhận cho FR-X.1-06 |
| Dòng 302 | C2 (phụ) | Tìm kiếm tư liệu có bắt buộc hỗ trợ tiếng Việt không dấu không; đồng bộ phạm vi BR-DATA-08 giữa file chính và bản trích ở FR-12 |
| Dòng 35 | C2 (`DIFF`) | Loại hồ sơ ở màn Thêm mới TVV: giữ `TVV`/`CG` (sửa expected đối tác) hay thêm giá trị "Người hỗ trợ" (sửa SRS) |
| Dòng 35 | C9 (`GAP`) | Câu thông báo sau khi đăng ký có bắt buộc kèm mã hồ sơ không |
| Dòng 35 | C10 (`DIFF`) | Giữ §H7 (về trang Danh sách) hay định nghĩa màn "theo dõi tiến độ" + ghi ngoại lệ tại FR-IV-03 |

### Bug mới ngoài phạm vi

**Không có.** 3 candidate ghi nhận trong báo cáo (2 ở dòng 35 §5, 1 ở dòng 301 §click accordion) đều **không**
đủ căn cứ log thành bug: hoặc quy được cho thao tác của công cụ đo, hoặc nằm ngoài `Kết quả mong đợi` của case
đang verify. Theo Flow 04, không mở rộng điều tra và không thêm dòng mới vào bảng.

### Mutate môi trường đã khai

| Case | Thay đổi | Env |
|---|---|---|
| 301 | Thêm 1 tư liệu `Nghị định 55/2019 hỗ trợ pháp lý cho doanh nghiệp nhỏ và vừa` (loại Văn bản pháp luật, Nháp) vào TVCS-20260806-0003 | nội bộ V1.0.9 |
| 302 | Không thêm — dùng lại nguyên tiền đề dòng 301 | — |
| 35 | Thêm 1 hồ sơ TVV `TVV-STP-AG-0004` (`QA F6 DKTGMLTVV13 0225`, `MOI_DANG_KY`) + 2 tệp PDF đính | nội bộ V1.0.9 |
