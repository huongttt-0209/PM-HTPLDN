# Đối chiếu 15 FAIL — Module 04 Đào tạo tập huấn × SRS v3.5

**Ngày:** 2026-06-26 · **SRS nguồn:** `input/srs-update-2026-5-5/srs-fr-03-dao-tao.md` (2153 dòng) · **Tester:** QA

Mục tiêu: với mỗi TC FAIL trong `report-dot-3.xlsx`, kiểm xem **kỳ vọng (KQ mong đợi) của TC còn đúng SRS mới nhất không**. Nếu TC vượt/khác SRS → sửa TC. Nếu TC đúng → re-test.

## Phân loại kết quả đối chiếu

| Nhóm | Số TC | Ý nghĩa |
|---|--:|---|
| **A — TC đúng SRS, re-test as-is** | 5 | Kỳ vọng khớp SRS line cụ thể → chạy lại |
| **B — TC sai SRS (over-specify), phải SỬA TC + re-test** | 5 | TC tự thêm yêu cầu SRS không có → sửa rồi chạy |
| **C — TC test hành vi SRS KHÔNG quy định → reclass "Chờ BA"** | 5 | Optimistic-lock / idempotency / update-warning không có trong SRS → KHÔNG nên đánh FAIL |

---

## Nhóm A — TC đúng SRS, re-test as-is (5 TC)

| TC ID | Kỳ vọng TC | SRS line | Khớp? |
|---|---|---|:-:|
| TC-KH-NAM-N-007 | Tên KH năm trống → ERR-KH-01 "Tên kế hoạch là bắt buộc" | `:1153` ERR-KH-01 nguyên văn | ✅ |
| TC-KQ-N-001 | Điểm KT = -1 → ERR-KQ-01 "Điểm kiểm tra phải từ 0 đến 10" | `:600` ERR-KQ-01 nguyên văn | ✅ |
| TC-KQ-N-002 | Điểm KT = 11 → ERR-KQ-01 | `:600` ERR-KQ-01 | ✅ |
| TC-DK-H-006 | Duyệt ĐK CHO_DUYET → DA_DUYET, ghi nhật ký | `:430` "phê duyệt đăng ký → DA_DUYET, ghi nhật ký"; `:472,484` ĐK tạo ở CHO_DUYET | ✅ (toast wording là giả định, core đúng) |
| TC-GV-002 | Filter `linh_vuc_id` + `vai_tro=TRO_GIANG` (AND) | `:992` FR-III-12 Inputs: `vai_tro (text, N: GIANG_VIEN/TRO_GIANG)` | ✅ |

> Lưu ý TC-DK-H-006: SRS chỉ yêu cầu "trạng thái → DA_DUYET, ghi nhật ký". Toast "Đã duyệt đăng ký" là SPEC-CLARIFY-DT-DK-01 (giả định) → khi re-test chỉ cần verify state đổi + nhật ký, không bắt buộc đúng chữ toast.
> Lưu ý TC-GV-002: SRS STT26 UAT 2026-05-26 chuyển `vai_tro` từ cấp Khóa (`KHOA_HOC_GIANG_VIEN`) xuống cấp buổi (`LICH_HOC_GIANG_VIEN`), nhưng **filter search theo vai_tro vẫn giữ ở FR-III-12** → TC vẫn hợp lệ; nếu filter trả sai do đổi data-model thì là **bug thật**.

---

## Nhóm B — TC sai SRS, phải SỬA TC rồi re-test (5 TC)

### B1. Ký số export — TC over-specify outbound signing (3 TC: TC-XUAT-H-003 / -004 / -006)

**SRS FR-III-20 (`:1366–1386`):**
- Mô tả: "Xuất thông tin CTDT ra file docx hoặc PDF cho mục đích **in/phê duyệt**."
- Processing: "Chọn CTDT → Chọn định dạng → **Sinh file từ template → Trả file download**."
- AC: "Xuất docx → tạo file docx đầy đủ" · "Xuất PDF → tạo file PDF **sẵn sàng in/ký**".

**TC hiện tại kỳ vọng (SAI vs SRS):** BE gọi outbound `POST /api/v1/ky-so/sign-doc`, AUDIT_LOG `hanh_dong='EXPORT_SIGNED'`, file có **dấu ký số nhúng** (panel Signatures), toast "Xuất tài liệu thành công".

→ **SRS KHÔNG yêu cầu** outbound signing service, embedded digital signature, hay audit action `EXPORT_SIGNED`. Đây là phần TC tự suy diễn (SPEC-CLARIFY-DT-EXP-01/03). FAIL của 3 TC này nhiều khả năng là **false-FAIL**: app xuất file đúng template nhưng không ký số (vì SRS không bắt).

**Sửa TC →** kỳ vọng mới bám SRS AC: *"Mở chi tiết CTDT (DA_DUYET/DA_CONG_KHAI/HOAN_THANH) → chọn Xuất DOCX/PDF → hệ thống sinh file từ template và trả file download; file mở được, nội dung CTDT đầy đủ (tên/mã/đơn vị/danh sách KH)."* Bỏ mọi kỳ vọng outbound `/ky-so/sign-doc` + embedded signature + audit `EXPORT_SIGNED`.

### B2. Hủy khóa học — TC sai tên state (2 TC: TC-KH-H-015 / TC-KH-S-026)

**SRS SM-KHOAHOC (`:2011`):** `DU_THAO --> DA_HUY : CB NV hủy` — state chuẩn là **`DA_HUY`** (9 trạng thái chuẩn `:59`).

**TC hiện tại:** `trang_thai='HUY'` (thiếu tiền tố `DA_`). Toast "Hủy khóa học thành công" = SPEC-CLARIFY-DT-21 (giả định).

→ Transition DU_THAO → DA_HUY **đúng SRS**, nhưng TC ghi sai enum `HUY` → **Sửa TC** thành `DA_HUY`; badge "Đã hủy" giữ nguyên. Toast coi là giả định (verify state + nhật ký là chính). Sau sửa → re-test.

---

## Nhóm C — TC test hành vi SRS KHÔNG quy định → reclass "Chờ BA" (5 TC)

Các TC này kỳ vọng cơ chế **không tồn tại trong SRS v3.5**. Theo nguyên tắc CLAUDE.md *"describe requirement, NOT prescribe implementation"* + *"không log FAIL khi SRS không quy định"*, đánh FAIL là **không đúng** — phải reclass sang **🚫 Chờ BA confirm (nhóm C)**.

| TC ID | Kỳ vọng TC | SRS nói gì | Vì sao reclass |
|---|---|---|---|
| TC-CTDT-E-030 | Optimistic lock `updated_at` → ERR-SYS-02 "Bản ghi đã bị thay đổi…" | SRS chỉ có **EC-03 `:510`**: import KQ đồng thời → row-lock → **ERR-DK-DT-04** (KHÁC cơ chế, KHÁC mã). Không có optimistic-lock generic cho sửa CTĐT. | SRS không quy định ERR-SYS-02/optimistic-lock cho CTĐT |
| TC-KH-E-038 | Optimistic lock sửa KH → ERR-SYS-02 | như trên | SRS không quy định |
| TC-GV-022 | Optimistic lock rename GV → ERR-SYS-02 | như trên | SRS không quy định |
| TC-DEXUAT-E-015 | DN double-click → debounce/idempotency, chỉ 1 record + 1 notif | SRS FR-III-13 không quy định idempotency/debounce | SRS không quy định |
| TC-NHCH-008 | Sửa câu hỏi đã DA_PHAN_PHOI → cảnh báo | WRN-NHCH-01 `:889` chỉ áp cho **XÓA** câu hỏi, KHÔNG cho UPDATE | SRS không quy định cảnh báo khi sửa |

→ Các TC nhóm C: đề xuất **đổi Kết quả `FAIL` → `🚫 Chờ BA`** + cột Lý do nhóm C "Chờ BA confirm: SRS không quy định [optimistic-lock / idempotency / cảnh báo sửa câu hỏi]". Ghi vào `tasks/srs-contradictions.md` nếu chưa có.

---

## Tóm tắt hành động

1. **5 TC nhóm A** → re-test live as-is.
2. **5 TC nhóm B** → sửa kỳ vọng TC trong xlsx (3 ký số + 2 tên state) → re-test live.
3. **5 TC nhóm C** → đổi FAIL → 🚫 Chờ BA (không re-test, escalate BA).

---

## Cập nhật sau khi CHẠY LIVE (2026-06-26 17:30)

Quan trọng — live test chỉnh lại 2 giả thuyết đối chiếu:

- **Nhóm B (ký số XUAT-H-003/004/006):** giả thuyết ban đầu "false-FAIL do over-spec ký số, sửa TC → PASS" **SAI**. Live: trang chi tiết CTĐT **không có nút Xuất DOCX/PDF nào** (FR-III-20 chưa build UI) → FAIL thật dù theo kỳ vọng đã sửa. Đã log **BUG-DT-RR-002**.
- **Nhóm B (hủy KH-H-015/S-026):** ngoài lỗi enum `HUY`/`DA_HUY`, live phát hiện khóa DU_THAO **không có hành động Hủy** (chỉ "Trình phê duyệt" + "Xóa" hard-delete). FAIL thật. Đã log **BUG-DT-RR-001**.
- **Nhóm C** xác nhận đúng: 6 TC reclass Chờ BA (gồm cả TC-GV-002 — live xác nhận UI bỏ filter vai_tro theo STT26).
- **Nhóm A:** TC-KH-NAM-N-007 → PASS (validation đúng). Còn TC-KQ-N-001/002 + TC-DK-H-006 **không re-test được** vì DB không có học viên (DANG_KY_DAO_TAO = 0 mọi khóa) → reclass CHƯA CHẠY (nhóm A thiếu seed), TC vẫn đúng SRS.

**Bài học:** đối chiếu SRS trên giấy chỉ ra TC sai/đúng, nhưng phải CHẠY LIVE mới biết FAIL là false-fail hay gap thật. 2/5 nhóm B hóa ra là gap chức năng thật, không phải lỗi TC.
