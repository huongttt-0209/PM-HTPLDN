# Bảng đối chiếu điều kiện — QLLSHTCTVV_01 (row 81)

**Claim đối tác:** "Hệ thống **không hiển thị lịch sử** mặc dù **tồn tại dữ liệu**" — tab "Lịch sử hỗ trợ" của chi tiết Tư vấn viên.

**Evidence đã xem:** `partner-evidence/QLLSHTCTVV_01.webm` (9.49s, đã trích 10 khung hình full-res 1920×1080 → `reverify-audit/QLLSHTCTVV_01/frames/`).
- **Khung chứa LỖI: t = 9.2s (đồng hồ ghi màn hình 00:09)** — tab "Lịch sử hỗ trợ" của TVV `TVV-BTP-TW-0032` ("TVV R11 Verify Mail Fix", Đang hoạt động, điểm 8.3/10): **Tổng vụ việc = 0**, **Đã hoàn thành = 0**, Điểm trung bình = "—", bảng rỗng với dòng "**Tư vấn viên chưa tham gia hỗ trợ vụ việc nào**".
- Khung t = 5.5s cho thấy chính TVV đó có **2 đánh giá đều gắn vụ việc** `8d074115-4da5-427c-af55-3909f1e4e675` ⇒ dữ liệu tham gia vụ việc **có tồn tại**, nhưng tab Lịch sử vẫn báo 0.

| Điều kiện có thể đổi kết quả | Đối tác (từ evidence, full-res) | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | CB Nghiệp vụ Trung ương (CB_NV_TW) | `cbnv_tw` — CB Nghiệp vụ Trung ương (CB_NV_TW) | Không |
| Entity + trạng thái (state machine) | Tư vấn viên "Đang hoạt động" (TVV-BTP-TW-0032) | Tư vấn viên `TVV-BTP-TW-0002` (98cfd963…), "Đang hoạt động" | Không |
| Dữ liệu tiền đề | TVV **đã tham gia vụ việc** (đánh giá gắn vụ việc `8d074115…`) | TVV **đã được phân công vụ việc** `VV-BTP-TW-20260712-001` — trạng thái "Đã phân công", `ngayPhanCong` = 12/07/2026, `nguoiXuLyId` = `5432719c-c542-4a5d-8c3a-db1b8a918bbf` = **đúng `taiKhoanId` của TVV-BTP-TW-0002** | Không |
| Input / filter | Không đặt bộ lọc (Từ ngày / Đến ngày / Trạng thái vụ việc đều trống) | Không đặt bộ lọc — bảng vẫn rỗng | Không |

**Ghi chú đóng GAP dữ liệu (Nguyên tắc 4):** tiền đề "TVV có vụ việc" **đã tồn tại thật** trên env được giao và **kiểm chứng được từ UI**: màn "Vụ việc HTPL → Danh sách" hiển thị `VV-BTP-TW-20260712-001` · trạng thái **Đã phân công** · **Người xử lý = "QA TVV Seed28 Active"** · ngày 12/07/2026. Liên kết id đã xác minh: `vu_viec.nguoiXuLyId` == `tu_van_vien.taiKhoanId` (`5432719c…`). 0 GAP.

**Kết luận:** 0 GAP → đủ điều kiện chốt verdict.

## Cổng 3 — SRS vs web (dạng gạch đầu dòng)

- **SRS** `srs-fr-04-chuyen-gia-tvv.md:749` — FR-IV-10 "Xem lịch sử hỗ trợ (**UC48**)", Mô tả (dòng 754): "Xem danh sách vụ việc TVV **đã tham gia hỗ trợ**, kèm thống kê và timeline".
- **SRS** `:772-773` §Processing: bước 1 "Lấy danh sách VU_VIEC liên kết qua **PHAN_CONG_VU_VIEC**"; bước 2 "Tính thống kê: **tổng VV, hoàn thành, điểm TB**".
- **SRS** `:801` §Acceptance Criteria: "**Given** user xem chi tiết TVV **When** chọn tab 'Lịch sử' **Then** danh sách VV + thống kê + timeline".
- **SRS** `:1567` — SCR-IV-03 cell 22: bảng gồm Mã vụ việc (đường liên kết) + Tên vụ việc + Doanh nghiệp + Lĩnh vực + Vai trò + Ngày phân công + Ngày hoàn thành + Kết quả + Đánh giá; thống kê "Tổng vụ việc: {N}".
- **SRS** `:1569` — cell 22c: dòng "Tư vấn viên chưa tham gia hỗ trợ vụ việc nào" **CHỈ hiển thị khi rỗng** (điều kiện: "Khi chưa có vụ việc").
- **Web (18.143.165.120):** TVV **đã có 1 vụ việc được phân công** nhưng tab "Lịch sử hỗ trợ" hiển thị **Tổng vụ việc = 0**, Đã hoàn thành = 0, Điểm trung bình "—", và bảng hiện trạng thái rỗng "Tư vấn viên chưa tham gia hỗ trợ vụ việc nào".
- Kiểm chứng bằng phương pháp thứ 2 (API cùng dữ liệu): `GET /api/v1/tu-van-viens/98cfd963…/lich-su-ho-tro` → `{"data": [], "meta": {"total": 0}}` — trùng khớp UI (không mâu thuẫn UI vs API).
- ⇒ ❌ **Sai SRS** (`:772` bước 1 + `:801` AC + `:1569` điều kiện hiển thị trạng thái rỗng) → `Open` (BUG-QLLSHTCTVV_01). **Tái hiện đúng claim đối tác.**

**Artifact quan sát:**
- `bug-reports/image/BUG-QLLSHTCTVV_01-web-lichsu-rong-du-da-phan-cong.png` (tab Lịch sử hỗ trợ = 0 / rỗng).
- `bug-reports/image/BUG-QLLSHTCTVV_01-web-vuviec-da-phan-cong-cho-chinh-tvv.png` (màn Vụ việc HTPL: chính vụ việc đó **Đã phân công** cho **QA TVV Seed28 Active** → chứng minh dữ liệu tồn tại).

---

## RE-VERIFY 2026-07-15 (sau dev fix) — `Reopen` (lỗi gốc đã fix, nhưng đẻ lỗi mới cùng luồng)

**Điều kiện re-test khớp bug gốc (0 GAP):** `cbnv_tw` (CB_NV_TW) · TVV-BTP-TW-0002 "Đang hoạt động" · đã được phân công vụ việc (tiền đề còn nguyên) · không đặt bộ lọc.

**Chạy trên web (tab Lịch sử hỗ trợ, reload fresh):**
- ✅ **Lỗi gốc đã khắc phục:** tab **KHÔNG còn rỗng** — **Tổng vụ việc = 2**, hiển thị 2 dòng (`VV-BTP-TW-20260712-003`, `VV-BTP-TW-20260712-001`) với Mã VV (link) + Tên vụ việc + Doanh nghiệp + Lĩnh vực + Vai trò (NHT) + Ngày phân công 12/07/2026. Đúng SRS `:772/:801/:1567`.
- ❌ **Lỗi MỚI cùng luồng:** cột **"Ngày hoàn thành"** hiển thị **"Invalid Date"** cho cả 2 vụ việc **chưa hoàn thành** (đọc DOM: 2 ô `<td>` = "Invalid Date"). Vụ việc chưa hoàn thành thì Ngày hoàn thành phải để trống/"—" (SRS `:1567` liệt kê cột "Ngày hoàn thành" — giá trị null không được render thành "Invalid Date").

**Evidence:** `bug-reports/image/BUG-QLLSHTCTVV_01-reverify-lichsu-hien-nhung-ngayhoanthanh-invalid-date.png`.

**Verdict re-verify:** `Reopen` — theo tiêu chí "fix đẻ ra bug mới cùng luồng". Phần chính (lịch sử rỗng) đã fix; còn 1 lỗi hiển thị "Ngày hoàn thành = Invalid Date" cần dev xử nốt.
