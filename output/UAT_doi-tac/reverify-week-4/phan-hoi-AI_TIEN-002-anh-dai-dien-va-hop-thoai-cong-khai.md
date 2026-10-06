# Phiếu phân tích — `AI_TIEN-002`: ô Ảnh đại diện và Hộp thoại công khai (nhóm III Đào tạo)

**Ngày lập:** 01/08/2026 · **Phạm vi:** 2 mục QA nêu "CẦN BA XÁC NHẬN"
**Yêu cầu gốc:** *"Màn thêm mới/chỉnh sửa kế hoạch đào tạo và khóa học/ Chương trình kế hoạch: Bổ sung trường Ảnh đại diện: Không bắt buộc, cho phép tải lên các định dạng ảnh"*
**Đầu ra:** chỉ phiếu phân tích. Chưa sửa SRS, chưa cập nhật sheet.

## Ghi chú phương pháp

- Cả 2 mục QA gắn nhãn "cần BA xác nhận" **đều không cần BA quyết** — tra đủ nguồn thì tài liệu đã tự trả lời. Chi tiết ở từng mục.
- Trích dẫn của QA (`CHANGELOG:3719`, `srs-fr-03:1777`, `:1783-1789`) **kiểm lại đều đúng**, không lệch dòng.
- **Bối cảnh chung — bản đồ CPF.** `srs-v3.5.md:1018` (`[TOIUU-112 chốt 2026-07-31]`) xếp 12 entity công khai thành 4 kiểu theo chỗ đặt ô nhập: (1) nhập ở form thêm/sửa — **CHUONG_TRINH_DAO_TAO** cùng 4 entity khác; (2) nhập ở hộp thoại công khai — **KE_HOACH_DAO_TAO** cùng 4 entity khác; (3) tách đôi — TU_VAN_VIEN; (4) nhập một phần — KHOA_HOC. Hai mục dưới đây rơi vào kiểu (1) và kiểu (2).

---

## Mục 1 — Form Chương trình đào tạo thiếu ô Ảnh đại diện

**Vấn đề:** Ô "Kết quả mong đợi" nhắc "Chương trình kế hoạch", nhưng form Chương trình đào tạo trên phần mềm không có ô Ảnh đại diện. QA hỏi phạm vi TOIUU-112 có bao gồm màn này không.

### (1) Phần mềm đúng SRS chưa? — **SAI**

- `srs-fr-03-dao-tao.md:1857` (SCR-III-01 Thành phần 6 — Form lập / chỉnh sửa CTDT) — *"| **Trường công khai chuyên trang (5 CPF)** | nhóm trường | Theo Thay đổi 5 — bật/tắt cong_khai + **ảnh đại diện** + thời gian đăng tải (auto) + mô tả công khai + file đính kèm công khai |"*
- `srs-fr-03-dao-tao.md:109` (FR-III-01 §Inputs #11) — *"anh_dai_dien | structured | N | jpg/png/gif, max 5MB **(Yêu cầu đối tác mục 01)** | Ảnh mặc định hệ thống"*
- `srs-v3.5.md:1018` — CHUONG_TRINH_DAO_TAO thuộc kiểu (1) *"nhập ngay ở form thêm/sửa"*.
- `srs-fr-03-dao-tao.md:2005` — *"CHUONG_TRINH_DAO_TAO | ✅ Đủ 5 CPF"*.

Bốn nguồn thống nhất: ô Ảnh đại diện **phải có** ở form CTDT. Phần mềm thiếu ⇒ sai.

### (1b) Bản `.docx` có nói khác không? — **Không xét**

Phần mềm sai `.md` nên Pha 1 dừng ở câu (1), không tới câu (1b).

### (2) Đối tác yêu cầu có khác SRS không? — **Không khác**

Kết quả mong đợi trùng đúng nội dung `:1857` và `:109`.

### (3) Có bắt buộc cho luồng nghiệp vụ không? — **CÓ**

Không có ô thì trường `anh_dai_dien` của CTDT vĩnh viễn rỗng, Cổng Pháp luật quốc gia chỉ hiển thị ảnh mặc định. Ghi chú kỹ thuật của QA xác nhận API tạo Chương trình đào tạo đã có sẵn trường `anhDaiDien` — chỉ thiếu ô nhập trên giao diện, khối lượng bổ sung nhỏ.

**→ Kết luận: Loại 1 — Lỗi phần mềm, Dev sửa theo SRS.** Bổ sung ô Ảnh đại diện vào form thêm mới / chỉnh sửa Chương trình đào tạo: không bắt buộc, nhận JPG/PNG/GIF ≤ 5MB, để trống hoặc tải lỗi thì tự dùng ảnh mặc định hệ thống. **Dev action: Có → Sheet: Giữ xử lý.** Không phản hồi đối tác, không sửa Kết quả mong đợi.

**Không cần BA xác nhận** — câu QA hỏi ("ý *Chương trình kế hoạch* có gồm màn Chương trình đào tạo không") không quyết định gì, vì SRS đã quy định ô này ở form CTDT **từ trước** TOIUU-112 (dòng `:1857` ghi *"Theo Thay đổi 5"*, thuộc đợt cổng duyệt 06/05/2026). Chốt TOIUU-112 *"10 entity công khai khác giữ nguyên cách bố trí"* nghĩa là **giữ** cách bố trí sẵn có của CTDT — mà cách bố trí đó chính là "ô ở form". Phạm vi hẹp của TOIUU-112 nói về việc **thêm ô ở chỗ đang thiếu**, không phải về việc gỡ ô đã đặc tả.

---

## Mục 2 — Hộp thoại Công khai của Kế hoạch đào tạo chỉ là hộp xác nhận

**Vấn đề:** Hộp thoại "Công khai" hiện chỉ có một câu hỏi + nút Hủy/Công khai, thiếu cả ba ô Mô tả công khai, Ảnh đại diện, File đính kèm công khai. Dev khai đây là chỗ "SRS lệch code" và cố ý chỉ đặt ô ảnh ở form lập; QA hỏi BA chọn sửa SRS theo code hay bổ sung ba ô.

### (1) Phần mềm đúng SRS chưa? — **SAI**

- `srs-fr-03-dao-tao.md:1782`–`:1790` (SCR-III-00 Thành phần 5 — Hộp thoại công khai) — ba ô *"Mô tả công khai"*, *"Ảnh đại diện"*, *"File đính kèm công khai"* cùng hai nút.
- `CHANGELOG-v3-to-v3.5.md:3719` (`[TOIUU-112 chốt 2026-07-31]`) — *"Bốn trường công khai còn lại của Kế hoạch đào tạo năm **giữ nguyên ở Hộp thoại công khai**"*.
- `srs-v3.5.md:1018` — KE_HOACH_DAO_TAO thuộc kiểu (2) *"nhập ở hộp thoại / accordion công khai khi bản ghi đạt trạng thái cuối"*.

### (2) Đối tác yêu cầu có khác SRS không? — **Không khác**

### (3) Có bắt buộc cho luồng nghiệp vụ không? — **CÓ, thiếu thì mất trường vĩnh viễn**

Đây là điểm quyết định, và nó bác hướng "sửa SRS theo hiện trạng code":

- Form lập kế hoạch năm (Thành phần 4, `:1761`–`:1778`) có 12 phần tử: Mã, Tên, Năm, Thời gian bắt đầu/kết thúc, Ngân sách, Nội dung, Nguồn lực, Ghi chú, File đính kèm, Ảnh đại diện, Thanh hành động. **Không có Mô tả công khai, không có File đính kèm công khai.**
- Gỡ hộp thoại thành hộp xác nhận trơn ⇒ `mo_ta_cong_khai` và `file_dinh_kem_cong_khai` **không có ô nhập ở bất kỳ màn nào**. Mô tả công khai chính là nội dung hiển thị của kế hoạch trên Cổng Pháp luật quốc gia.
- Riêng ô **Ảnh đại diện** thì lập luận của Dev đứng vững: `:1777` ghi rõ ô ảnh ở form *"**Dùng chung một trường `anh_dai_dien` với ô Ảnh đại diện tại Thành phần 5**"* — cùng một trường nên đặt ở form không mất dữ liệu.

**→ Kết luận: Loại 1 — Lỗi phần mềm, Dev sửa theo SRS.** Hộp thoại Công khai của Kế hoạch đào tạo năm phải có ô **Mô tả công khai** và **File đính kèm công khai** (bắt buộc phải có, vì không màn nào khác nhập được). Ô **Ảnh đại diện** giữ theo SRS ở cả form lẫn hộp thoại, dùng chung một trường. **Dev action: Có → Sheet: Giữ xử lý.** Không phản hồi đối tác.

**Không cần BA chọn hướng.** Hướng "sửa SRS theo hiện trạng code" bị loại bằng chính chốt BA ngày 31/07 (*"giữ nguyên ở Hộp thoại công khai"* — cây trọng tài tầng 1), và bằng hệ quả mất hai trường công khai không nhập lại được ở đâu.

### Phương án xử lý (cập nhật SRS)

Nhận định của Dev *"SRS lệch code"* đúng một nửa: SRS **có** lệch, nhưng lệch ở chỗ khác — phần đặc tả xử lý chưa bao giờ đỡ cho các ô đã vẽ trên màn. Ba điểm dọn đặc tả, BA làm, không phát sinh việc cho Dev ngoài phần đã nêu ở Kết luận.

**Điểm A — FR-III-16 §Inputs không có trường nào của hộp thoại.** Hiện chỉ *"ke_hoach_id (identifier, Y), hanh_dong (text, Y: CONG_KHAI/HUY_CONG_KHAI)"*; §Processing chỉ *"Kiểm tra trạng thái → đặt cờ công khai + chuyển trạng thái → Ghi nhật ký"*. Theo cây trọng tài tầng 3, ô nhập chỉ tồn tại nếu có bước xử lý dùng tới — ba ô ở Thành phần 5 đang không có chỗ bám. **Đặc tả phải thành:** FR-III-16 §Inputs bổ sung `mo_ta_cong_khai`, `anh_dai_dien`, `file_dinh_kem_cong_khai` (đều tùy chọn) và §Processing thêm bước ghi ba trường này trước khi đặt cờ công khai.

**Điểm B — FR-III-14 §Inputs thiếu `anh_dai_dien` mà BA vừa chốt thêm.** §Inputs Tạo/Sửa kế hoạch năm hiện có đúng 9 trường, không trường CPF nào. Đợt áp TOIUU-112 ngày 31/07 đã thêm ô Ảnh đại diện vào SCR-III-00 Thành phần 4 nhưng **không sửa §Inputs tương ứng** — cùng một kiểu sót với vụ `TDHSTVV_13` (sửa màn hình mà quên phần đặc tả xử lý). **Đặc tả phải thành:** FR-III-14 §Inputs bổ sung `anh_dai_dien` (tùy chọn, jpg/png/gif ≤ 5MB, mặc định ảnh hệ thống), ghi rõ dùng chung trường với hộp thoại công khai.

**Điểm C — bản đồ CPF xếp sai kiểu cho KE_HOACH_DAO_TAO.** `srs-v3.5.md:1018` xếp entity này vào kiểu (2) thuần "nhập ở hộp thoại". Nhưng sau TOIUU-112 nó đã thành **tách đôi** — ảnh ở form, bốn trường còn lại ở hộp thoại — tức cùng kiểu (3) với TU_VAN_VIEN. Bản đồ và chốt TOIUU-112 nằm cùng một lượt ngày 31/07 nhưng không khớp nhau. **Đặc tả phải thành:** chuyển KE_HOACH_DAO_TAO từ kiểu (2) sang kiểu (3), ghi rõ ranh giới ảnh ↔ bốn trường còn lại.

---

## Tổng hợp cho sheet

| Mục | Loại | Dev action | Sheet | Phản hồi đối tác |
|---|---|---|---|---|
| 1 — Ô Ảnh đại diện ở form Chương trình đào tạo | Loại 1 | Có | Giữ xử lý | Không |
| 2 — Hộp thoại Công khai Kế hoạch đào tạo | Loại 1 | Có | Giữ xử lý | Không |

Cả hai đều là bug thật, Dev sửa, nên không viết phản hồi gửi đối tác. **Không mục nào cần BA xác nhận** — QA gắn nhãn "cần BA" vì chưa tra tới `SCR-III-01:1857` (mục 1) và tới `CHANGELOG:3719` phần *"giữ nguyên ở Hộp thoại công khai"* cùng danh sách trường của form lập (mục 2).

Ba điểm A/B/C là dọn đặc tả cho SRS tự nhất quán, chờ BA bật đèn xanh cho đợt áp.
