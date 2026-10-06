# Câu hỏi cần BA xác nhận — đợt verify dev fix (FLOW 04) — 2026-08-06

> **⚠️ File này là bản ghi gốc của lô, KHÔNG phải bản gửi BA.**
> Bản gửi BA là [`cau-hoi-BA-tong-hop-2026-08-06.md`](../reverify-week-5/ba-confirm/cau-hoi-BA-tong-hop-2026-08-06.md) — `QLHSDNHTCP_03` → **Mục 15**.

**Môi trường quan sát:** https://18.143.165.120.nip.io (env dev) — bản dựng **HTPLDN · V1.0.8**
**Số mục cần BA:** 1

---

## §1 — `QLHSDNHTCP_03`: cột cảnh báo thời hạn hiển thị gì khi hồ sơ đã kết thúc?

**Bối cảnh:** màn **Chi trả chi phí → Danh sách** (`/chi-tra/danh-sach`, SCR-V.II-01), cột **"SLA"**
(thành phần #16). Dòng bảng 72, mã TC `QLHSDNHTCP_03`.

### Phần mềm đang thế nào

Cột "SLA" hiện **5 loại nhãn**, trong khi mô hình cảnh báo chỉ có **4 mức**:

| Nhãn đang hiện | Số dòng | Trạng thái hồ sơ | Giá trị mức cảnh báo trong dữ liệu |
|---|---|---|---|
| "Bình thường · còn 10 ngày LV" | 1 | Đang kiểm tra | `BINH_THUONG` |
| "Sắp hết hạn · còn 6 ngày LV" | 1 | Đang kiểm tra | `SAP_HET_HAN` |
| "Quá hạn · 6 / 9 ngày LV" | 2 | Chờ tiếp nhận, Đang kiểm tra | `QUA_HAN` |
| "Quá hạn nghiêm trọng · 11…53 ngày LV" | 6 | Đang kiểm tra, Yêu cầu bổ sung, Đang đánh giá, Đã duyệt, Đang thẩm định ×2 | `QUA_HAN_NGHIEM_TRONG` |
| **"Đã hoàn thành"** ← nhãn thứ 5 | **4** | **Đã thanh toán ×2, Từ chối, Hủy** | **`BINH_THUONG`** |

Điểm đáng chú ý: 4 dòng cuối mang nhãn **"Đã hoàn thành"** trên giao diện, nhưng dữ liệu của chính 4 bản ghi đó
lại là `BINH_THUONG` — tức **giao diện không hiển thị giá trị mà dữ liệu đang mang**.
Bản ghi: `CT-QAW7-CLOSED`, `CT-SEED-108` (Đã thanh toán), `CT-SEED-109` (Từ chối), `CT-SEED-110` (Hủy).

### Đối tác kỳ vọng gì

Đối tác **không** phản ánh điểm này. Cả 2 vòng của họ chỉ nói về (a) cột không giống thiết kế và (b) dữ liệu
tràn sang cột "Ngày nộp" — **cả hai vế nay đều đã hết lỗi** trên bản dựng V1.0.8. Đây là điểm QA gặp khi đo,
nằm trong đúng cột đang tranh chấp nên đưa ra để BA chốt, không phải phản ánh mới của đối tác.

### Đặc tả nói gì

- **BR-SLA-02** (`srs-fr-06-chi-tra.md:1514-1523`) định nghĩa **đúng 4 mức**: `BINH_THUONG` "Bình thường"
  (còn >50%) · `SAP_HET` "Sắp hết hạn" (còn <50%) · `QUA_HAN` "Quá hạn" (trễ >100%) ·
  `QUA_HAN_NGHIEM_TRONG` "Quá hạn nghiêm trọng" (trễ >200%). Câu cuối: *"Nếu không thỏa điều kiện nào thì hiển
  thị **'Bình thường'**"*.
- **SCR-V.II-01 #16** (`:1058`) — *"4 mức cảnh báo theo BR-SLA-02: Bình thường / Sắp hết hạn / Quá hạn /
  Quá hạn nghiêm trọng"*, điều kiện hiển thị **"Luôn"**.
- Ràng buộc của trường `muc_do_canh_bao` (`:1311`) chỉ nhận **4 giá trị** trên.
- **Đặc tả IM LẶNG** về việc cột này hiển thị gì khi hồ sơ đã ở trạng thái kết thúc (`DA_THANH_TOAN`,
  `TU_CHOI`, `HUY`) — không dòng nào nói tới. Đọc thẳng BR-SLA-02 thì 4 dòng đó phải ghi **"Bình thường"**,
  nhưng ghi "Bình thường" cho một hồ sơ **đã Từ chối** hoặc **đã Hủy** thì không có nghĩa về nghiệp vụ.
- Quyết định **BA ngày 2026-07-24** cho chính mã TC này chỉ chốt: tên cột "SLA" là đúng, và phần mềm phải hiện
  4 nhãn rời + số ngày. **Không nhắc tới hồ sơ đã kết thúc.**

### Câu hỏi cụ thể cho BA

1. Với hồ sơ đã ở trạng thái kết thúc (**Đã thanh toán / Từ chối / Hủy**), cột "SLA" nên hiển thị gì:
   (a) giữ nhãn **"Đã hoàn thành"** như phần mềm đang làm · (b) hiện đúng mức cảnh báo lưu trong dữ liệu
   (hiện là "Bình thường") · (c) để trống / dấu "—" vì cảnh báo thời hạn không còn ý nghĩa · (d) phương án khác?
2. Nếu chọn (a): xin bổ sung nhãn thứ 5 này vào BR-SLA-02 và vào thành phần #16 của SCR-V.II-01 để lần sau QA
   có căn cứ chấm, và nói rõ nhãn này áp cho **những trạng thái nào**.
3. Câu hỏi liên đới: 4 hồ sơ đã kết thúc đó đang mang `muc_do_canh_bao = BINH_THUONG` trong dữ liệu — giá trị
   này có **đúng** không, hay khi hồ sơ kết thúc thì mức cảnh báo cần được chốt lại / để trống? (Nếu BA chọn
   phương án (b) ở câu 1 thì giá trị trong dữ liệu sẽ hiện thẳng ra giao diện, nên cần đúng.)

### Đường dẫn ảnh

- `image/QLHSDNHTCP_03-danhsach-SLA-NgayNop-V108-2026-08-06.png` — 5 dòng đầu, thấy nhãn "Bình thường",
  "Sắp hết hạn", **"Đã hoàn thành"** (dòng `CT-QAW7-CLOSED`, trạng thái *Đã thanh toán*), "Quá hạn nghiêm trọng".
- `image/QLHSDNHTCP_03-vaitro-CBPD-SLA-NgayNop-V108-2026-08-06.png` — 9 dòng cuối, thấy **3 dòng
  "Đã hoàn thành"** ứng với `CT-SEED-108` (*Đã thanh toán*), `CT-SEED-109` (*Từ chối*), `CT-SEED-110` (*Hủy*).

### QA đề xuất tạm thời

Verdict `QLHSDNHTCP_03` = **cần BA**. Không chấm Pass vì cột đang tranh chấp có 1 nhãn nằm ngoài đặc tả;
không chấm Reopen vì **cả 2 vế đối tác phản ánh đều đã hết lỗi** và đặc tả không quy định điểm này —
chưa có việc gì để chuyển cho dev cho tới khi BA chốt.
