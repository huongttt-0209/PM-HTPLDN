# Bảng đối chiếu điều kiện — CNDSMLTVV_05

**Evidence đã xem:** `partner-evidence/CNDSMLTVV_05.webm` → frames `reverify-audit/CNDSMLTVV_05/frames/`
- f005 (00:13): vai trò **CB_NV_TW**, hồ sơ TVV "Đinh Văn Mười Bốn" (**Đang hoạt động**, chưa công khai) → hộp thoại "Công khai TVV ... lên Cổng PLQG" → đã nhập **Mô tả công khai** (67/5000) + đính kèm 1 tệp PDF.
- f017 (00:49) — **frame chứa LỖI**: cùng thao tác trên hồ sơ "TVV R12 A18 UI Walk" (Đang hoạt động), mô tả 69/5000 + 1 tệp PDF → bấm "Công khai" → hiện toast đỏ **"Không thể công khai. Vui lòng thử lại."** → hồ sơ KHÔNG được công khai.

**Đối tác phản ánh cụ thể:** bấm "Công khai lên Cổng pháp luật quốc gia" → hệ thống báo **"Không thể công khai. Vui lòng thử lại."**, không công khai được.

| Điều kiện có thể đổi kết quả | Đối tác (từ evidence, full-res) | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | Cán bộ NV Trung ương (CB_NV_TW) — đúng tác nhân FR-IV-08 | cbnv_tw (CB_NV_TW) | Không |
| Entity + trạng thái (state machine) | TVV cấp TW, trạng thái **Đang hoạt động**, **chưa công khai** | TVV-BTP-TW-0002 "QA TVV Seed28 Active" cấp TW, trạng thái **Đang hoạt động** (`HOAT_DONG`), **chưa công khai** (`laCongKhai=false`) | Không |
| Dữ liệu tiền đề / Input | Mô tả công khai đã nhập (67-69 ký tự) + **1 tệp PDF đính kèm** | Mô tả công khai 70 ký tự + **1 tệp PDF đính kèm** (`the-hanh-nghe-qa.pdf`) | Không |

**Kết quả verify trên web (cbnv_tw) — TÁI HIỆN:**
- Bấm "Công khai" → toast lỗi (MutationObserver bắt được): **"Lỗi kết nối Cổng PLQG khi công khai tư vấn viên"** (env đối tác hiện câu "Không thể công khai. Vui lòng thử lại." — cùng bản chất lỗi, khác câu chữ theo build).
- Network của **chính thao tác đó**: `POST /api/v1/tu-van-viens/{id}/cong-khai` → **502**, body `{"code":"ERR-SYS-IV-CK-02","message":"Lỗi kết nối Cổng PLQG khi công khai tư vấn viên"}`. (Tệp đính kèm upload OK — `POST .../cong-khai/files` trả 201.)
- **Cô lập nguyên nhân:** gọi lại đúng thao tác **KHÔNG kèm tệp đính kèm** → **vẫn 502, cùng mã lỗi** ⇒ lỗi **không phải** do tệp đính kèm, mà do backend **gọi ra Cổng PLQG** và kết nối thất bại.
- Hồ sơ **không đổi**: `laCongKhai=false`, `moTaCongKhai=null`, `thoiGianDangTai=null`; nút "Công khai lên Cổng PLQG" vẫn còn ⇒ **luồng nghiệp vụ hợp lệ bị chặn hoàn toàn**.
- Log đầy đủ: `reverify-audit/CNDSMLTVV_05/api-cong-khai-502.log`.

**Đối chiếu SRS v3.5 (`srs-fr-04-chuyen-gia-tvv.md`) — web làm SAI mô hình SRS:**
- FR-IV-08 §Mô tả (dòng 638) `[CR-02]`: *"Công khai … theo mô hình **KÉO (PULL)**: phần mềm **chỉ đặt cờ `cong_khai` + chuyển trạng thái CONG_KHAI / HUY_CONG_KHAI**; Cổng PLQG **tự kéo** dữ liệu công khai định kỳ qua API outbound (Cổng chủ động gọi sang). **Phần mềm KHÔNG đẩy trực tiếp, KHÔNG gọi API ra Cổng.**"*
- FR-IV-08 §Processing bước 2 (dòng 657): *"Công khai: lưu mo_ta_cong_khai + file_dinh_kem_cong_khai, **đặt cong_khai = 1, chuyển trạng thái CONG_KHAI**, auto fill thoi_gian_dang_tai. Cổng PLQG tự kéo dữ liệu ở lần đồng bộ định kỳ kế tiếp."*
- FR-IV-08 §Error Handling (dòng 674-675): chỉ có **ERR-CK-01** (sai trạng thái) và **ERR-CK-02** (thiếu mô tả công khai) — **KHÔNG có** lỗi "kết nối Cổng PLQG".
- ⇒ Theo SRS, thao tác công khai là **nội bộ hoàn toàn**, phải thành công ngay (đặt cờ + đổi trạng thái) mà **không phụ thuộc** kết nối tới Cổng PLQG. Thực tế backend lại gọi ra Cổng PLQG (mô hình ĐẨY) và khi kết nối lỗi thì **rollback toàn bộ**, chặn cán bộ công khai tư vấn viên đủ điều kiện.
- Hộp thoại trên giao diện cũng ghi *"Sau khi công khai, dữ liệu sẽ được đồng bộ tới Cổng PLQG. Nếu đồng bộ thất bại, hệ thống sẽ rollback…"* — xác nhận web đang cài theo mô hình **ĐẨY**, trái `[CR-02]`.

**Ghi chú về Kết quả mong đợi của test case:** đối tác kỳ vọng *"Gọi giao diện tích hợp **đẩy** dữ liệu lên Cổng PLQG"* + toast *"Đã đẩy tư vấn viên lên Cổng pháp luật quốc gia"* + *"Dữ liệu được tiếp nhận bởi Cổng PLQG trong lần gọi đầu tiên"* — mô tả này theo mô hình **ĐẨY**, **trái với SRS v3.5 `[CR-02]` (mô hình KÉO)**. Phần kỳ vọng này đã tách sang `ba-confirmation-needed-week-2.md`; **không ảnh hưởng verdict** vì lỗi chính là **luồng công khai bị chặn**.

**Verdict:** `Open` (hệ thống **chặn luồng hợp lệ dù đủ điều kiện** — đúng vai trò, đúng trạng thái, đủ mô tả công khai; trái FR-IV-08 §Processing bước 2 (dòng 657) và mô hình PULL (dòng 638)).

---

## RE-VERIFY 2026-07-15 (sau dev fix) — `Pass`

**Điều kiện re-test khớp bug gốc (0 GAP):** vai trò `cbnv_tw` (CB_NV_TW) · TVV-BTP-TW-0002 "QA TVV Seed28 Active" **Đang hoạt động + Chưa công khai** (đúng tiền đề) · nhập Mô tả công khai 68 ký tự (không kèm tệp — vòng 1 đã cô lập tệp không ảnh hưởng kết quả).

**Chạy hết luồng trên web (không tĩnh):** mở hộp thoại "Công khai lên Cổng PLQG" → điền mô tả → bấm **"Công khai"**.
- Toast (MutationObserver bắt được): **"Đã công khai lên Cổng PLQG"** (thành công).
- Nút đổi từ "Công khai lên Cổng PLQG" → **"Hủy công khai"**; hồ sơ hiện section **"Thông tin công khai"** (Mô tả + **Thời gian đăng tải 15/07/2026**) ⇒ trạng thái đã CÔNG KHAI.
- Network của chính thao tác: `POST /api/v1/tu-van-viens/98cfd963…/cong-khai` → **200** (vòng 1 là **502 ERR-SYS-IV-CK-02**). Thao tác nội bộ, không còn phụ thuộc kết nối ra Cổng.
- Hộp thoại nay ghi *"hồ sơ được đánh dấu công khai ngay. Cổng PLQG sẽ tự động **kéo** dữ liệu công khai định kỳ"* — đúng mô hình **KÉO (PULL)** theo `[CR-02]` (dòng 638).

**Evidence:** `bug-reports/image/BUG-CNDSMLTVV_05-reverify-pass-cong-khai-ok.png`.

**Kết luận:** luồng công khai hợp lệ nay **thành công đúng SRS** (mô hình KÉO, đặt cờ + đổi trạng thái nội bộ) → **Pass**.
