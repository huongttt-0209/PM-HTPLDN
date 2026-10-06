# Bảng đối chiếu điều kiện — CNTTTVV_06 (row 82)

**Claim đối tác:** Khi sửa hồ sơ tư vấn viên **không phải chủ hồ sơ** (khác đơn vị) → "Thông báo hiển thị **bị duplicate** và **không giống với thiết kế**". Expected của case: báo "Bạn không có quyền cập nhật hồ sơ này".

**Evidence đã xem:** `partner-evidence/CNTTTVV_06.jpg` (full-res) — màn `/chuyen-gia-tvv/b8b5e09c-a18b-4776-a510-7fa577a50674/**chinh-sua**`, role CB_NV_TW. Frame chứa lỗi: **2 toast đỏ giống hệt nhau** cùng nội dung "**Đơn vị của bạn khác đơn vị của tư vấn viên**" xếp chồng ở phía trên; biểu mẫu vẫn ở chế độ sửa (không lưu được).

| Điều kiện có thể đổi kết quả | Đối tác (từ evidence, full-res) | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | CB Nghiệp vụ Trung ương (CB_NV_TW), đơn vị BTP · TW | `cbnv_tw` — CB Nghiệp vụ Trung ương (CB_NV_TW), đơn vị `00000000-0000-4000-8000-000000000001` (BTP · TW) | Không |
| Entity + trạng thái (state machine) | Tư vấn viên **khác đơn vị** với cán bộ đang đăng nhập (thông báo web xác nhận "Đơn vị của bạn khác đơn vị của tư vấn viên") | Tư vấn viên `TVV-STP-AG-0001` ("QA TVV Dia Phuong R18"), đơn vị `00000000-0000-4000-8002-000000000006` — **khác đơn vị** với `cbnv_tw` | Không |
| Dữ liệu tiền đề | Mở màn "Chỉnh sửa hồ sơ TVV" của hồ sơ không thuộc đơn vị mình | Mở đúng màn "Chỉnh sửa hồ sơ TVV" `/chuyen-gia-tvv/4c1d3aab…/chinh-sua` của hồ sơ khác đơn vị | Không |
| Input / filter | Bấm **Lưu** | Bấm **Lưu** (giữ nguyên dữ liệu sẵn có) | Không |

**Kết luận:** 0 GAP → đủ điều kiện chốt verdict.

## Cổng 3 — SRS vs web (dạng gạch đầu dòng)

- **SRS** `srs-fr-04-chuyen-gia-tvv.md:1519` — SCR-IV-02 (màn Thêm mới / **Sửa hồ sơ TVV**) §Tham chiếu nội bộ: *"mã lỗi ERR-TVV-01/02/03/04, ERR-DK-…, ERR-NL-…, **ERR-CN-01/02/03**; quy tắc **BR-AUTH-08** (phân quyền theo đơn vị)"* ⇒ màn sửa hồ sơ phải dùng thông báo lỗi ERR-CN-02 cho tình huống khác đơn vị.
- **SRS** `srs-fr-04-chuyen-gia-tvv.md:854` — FR-IV-11 (UC49) §Error Handling E2: điều kiện "không cùng đơn vị với TVV" → thông báo **"Bạn không có quyền cập nhật hồ sơ tư vấn viên này (khác đơn vị)"**. Cùng quy ước ở `:420` (FR-IV-04 §Error Handling E1, ERR-NL-01) — **cùng một câu chữ**.
- **Web (18.143.165.120):** hệ thống **CÓ chặn** thao tác (đúng — không lưu, ở lại màn sửa) nhưng:
  1. ❌ Thông báo hiển thị **2 lần trùng lặp** — đếm DOM: **2** phần tử `.ant-message-notice-wrapper`, nội dung giống hệt nhau ("Đơn vị của bạn khác đơn vị của tư vấn viên").
  2. ❌ Nội dung thông báo **không nêu rõ người dùng không có quyền cập nhật hồ sơ** như SRS `:854` quy định — chỉ nêu sự kiện "Đơn vị của bạn khác đơn vị của tư vấn viên".
- ⇒ **Tái hiện đúng cả 2 ý đối tác** → `Open` (BUG-CNTTTVV_06). Việc chặn thao tác là đúng SRS/BR-AUTH-08; lỗi nằm ở **cách hiển thị thông báo** (lặp 2 lần + không đúng thông báo SRS quy định cho màn này).

**Artifact quan sát:** `bug-reports/image/BUG-CNTTTVV_06-web-toast-loi-hien-2-lan-trung-lap.png` (full-res — loại claim = Thao tác/state + Hiển thị: chụp đúng kết quả thao tác bấm Lưu, thấy rõ **2 toast đỏ giống hệt nhau**; đã đếm DOM xác nhận 2 wrapper, không phải ảo giác thị giác).

---

## RE-VERIFY 2026-07-15 (sau dev fix) — `Pass`

**Điều kiện re-test khớp bug gốc (0 GAP):** `cbnv_tw` (CB_NV_TW, BTP·TW) · mở màn Chỉnh sửa TVV-STP-AG-0001 (An Giang — **khác đơn vị**) qua `/chuyen-gia-tvv/4c1d3aab…/chinh-sua` · bấm Lưu (giữ nguyên dữ liệu).

**Chạy trên web (reload form fresh, bấm Lưu 1 lần, đo bằng MutationObserver):**
- ✅ **Hết trùng lặp:** đếm số node `.ant-message-notice-wrapper` được add = **1** (vòng 1 là **2**). Xác định 2 node bắt được lúc đầu là container `.ant-message` (cha) + 1 wrapper (con lồng nhau) = **1 toast thật**.
- ✅ **Wording đúng SRS:** nội dung toast = **"Bạn không có quyền cập nhật hồ sơ tư vấn viên này (khác đơn vị)"** — nêu rõ "không có quyền cập nhật hồ sơ" đúng FR-IV-11 (UC49) §E2 (dòng 854) / FR-IV-04 §E1 (dòng 420). Vòng 1 chỉ ghi "Đơn vị của bạn khác đơn vị của tư vấn viên".
- Chặn thao tác đúng: `PATCH /api/v1/tu-van-viens/4c1d3aab…` → **403**, form giữ nguyên ở màn sửa (không lưu).

**Evidence:** `bug-reports/image/BUG-CNTTTVV_06-reverify-pass-1-toast-wording-dung.png`.

**Kết luận:** cả 2 ý (trùng lặp + wording) đều đã khắc phục đúng SRS → **Pass**.
