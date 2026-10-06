# Bảng đối chiếu điều kiện — QLDMTCTV_OOS_05 (re-verify vòng 1, 05/08/2026)

Loại bug: **danh sách cột của bảng + khả năng nhìn thấy cột cuối ở bề ngang chuẩn** → điền bảng đối chiếu, 0 GAP.
Tiêu chí lấy nguyên văn từ khối `── CÁCH VERIFY sau Dev fix ──` trong ô *DEV phản hồi lần 1* của chính dòng này.

| Điều kiện | Bug gốc (khối CÁCH VERIFY) | Mình test | GAP? |
|---|---|---|---|
| Môi trường | Môi trường bàn giao, bản dựng đang chạy | `https://18.143.165.120.nip.io` — bản dựng **HTPLDN · V1.0.6** (đọc ở thanh bên trái) | Không |
| Vai trò | `cbnv_tw` | `cbnv_tw` · CB_NV_TW · Cục Bổ trợ tư pháp - Bộ Tư pháp · cấp TW | Không |
| Màn hình | Mạng lưới Tư vấn viên → Tổ chức tư vấn | Mạng lưới Tư vấn viên → Tổ chức tư vấn (`/chuyen-gia-tvv/to-chuc`) | Không |
| Thẻ đang mở | Thẻ "Đang hoạt động" có ≥1 bản ghi | Thẻ **Đang hoạt động** — 3 bản ghi (TC-STP-AG-0001, TCTV-SEED-0001, TC-TW-DEMO-001) | Không |
| Bề ngang cửa sổ | 1440px | Khung nhìn đo được **1440 × 736** (đặt bằng lệnh đổi cỡ cửa sổ, không phóng to/thu nhỏ) | Không |
| Thanh menu bên trái | Trạng thái mặc định của màn | Để nguyên trạng thái mặc định (đang mở rộng, chiếm 280px) — không thu gọn để "ăn gian" bề ngang | Không |
| Bước 1 — đọc tiêu đề cột | Đọc lần lượt tiêu đề tất cả các cột từ trái sang phải | Đã đọc đủ 10 tiêu đề bằng cả ảnh chụp lẫn đọc trực tiếp cấu trúc bảng | Không |
| Bước 2 — không cuộn ngang | Kiểm 3 cột Trạng thái, Công khai, Hành động có nằm trong khung nhìn không | Đo ở vị trí cuộn = 0: bề rộng nội dung bảng 1466 so với khung chứa 1136 → **thừa 330 điểm ảnh** | Không |
| Bước 3 — bộ lọc đơn vị quản lý | Mở bộ lọc phía trên bảng, kiểm còn dùng được không | Đã mở, chọn **Sở Tư pháp An Giang**, bấm Tìm kiếm | Không |

**Kết luận: 0 GAP** — đúng bản dựng đang chạy, đúng vai trò, đúng màn hình, đúng thẻ, đúng bề ngang 1440, đã chạy hết cả 3 bước của khối CÁCH VERIFY (không chấm bằng quan sát tĩnh).

## Đo lường trực tiếp (05/08/2026, `18.143.165.120.nip.io`, bản dựng V1.0.6)

### Đối chiếu từng vế của khối "✅ PASS khi"

- ✅ **Vế 1 — bảng có đúng 10 cột, không còn cột "Đơn vị quản lý"** → đọc được đúng 10 tiêu đề: Ô chọn · STT · Mã tổ chức · Tên tổ chức · Loại hình · Lĩnh vực · Người đại diện · Trạng thái · Công khai · Hành động. Cột "Đơn vị quản lý" đã được gỡ khỏi bảng.
  Ảnh: [`../image/QLDMTCTV_OOS_05-bang-10-cot-1440px.png`](../image/QLDMTCTV_OOS_05-bang-10-cot-1440px.png)
- ❌ **Vế 2 — ở bề ngang 1440 nhìn thấy cả ba cột cuối mà không phải cuộn ngang** → KHÔNG đạt. Ở vị trí cuộn = 0, khung nhìn chỉ tới hết cột "Người đại diện" rồi nhảy thẳng sang "Hành động" (cột này được ghim cứng bên phải). Hai cột **"Trạng thái"** và **"Công khai"** nằm ngoài khung, chỉ hiện ra sau khi kéo thanh cuộn ngang hết cỡ (330 điểm ảnh).
  - Vị trí cột khi chưa cuộn: Trạng thái 1296→1456, Công khai 1456→1616, trong khi mép phải khung chứa chỉ ở 1416 và bị cột "Hành động" ghim (1286→1416) che nốt phần còn lại.
  - Ảnh minh chứng (đã cuộn hết sang phải mới đọc được 2 cột đó): [`../image/QLDMTCTV_OOS_05-phai-cuon-ngang-moi-thay-trangthai-congkhai.png`](../image/QLDMTCTV_OOS_05-phai-cuon-ngang-moi-thay-trangthai-congkhai.png)
- ✅ **Vế 3 — bộ lọc theo đơn vị quản lý vẫn còn và vẫn lọc đúng** → bộ lọc "Đơn vị quản lý" vẫn nằm trên thanh tìm kiếm, gõ tìm ra đủ danh sách đơn vị; chọn "Sở Tư pháp An Giang" → còn đúng 1 kết quả TC-STP-AG-0001 (đúng tổ chức thuộc đơn vị đó), thẻ "Đang hoạt động" đổi số từ 3 về 1.
  Ảnh: [`../image/QLDMTCTV_OOS_05-boloc-donviquanly-con-dung.png`](../image/QLDMTCTV_OOS_05-boloc-donviquanly-con-dung.png)

### Đối chiếu khối "❌ FAIL nếu"

- Cột "Đơn vị quản lý" vẫn còn trong bảng → **không xảy ra** (đã gỡ).
- Gỡ cột nhưng gỡ mất luôn bộ lọc theo đơn vị quản lý → **không xảy ra** (bộ lọc còn nguyên và còn đúng).

### Kết luận

Khối "✅ PASS khi" có 3 vế, phải đạt cả 3 mới được chấm Pass. Vế 1 và vế 3 đã đạt; **vế 2 chưa đạt** — hai cột "Trạng thái" và "Công khai" vẫn nằm ngoài khung nhìn ở bề ngang 1440, đúng phần hệ quả mà phiếu gốc nêu ("phải cuộn ngang mới thấy được 3 cột cuối"). Sửa được một phần (gỡ cột thừa + ghim lại cột Hành động) nhưng chưa hết → **Reopen**.

### Ghi nhận thêm (ngoài phạm vi phiếu — không tự thêm dòng mới vào sheet)

- Thứ tự cột trên bảng đang là *… Loại hình → Lĩnh vực → Người đại diện …*, trong khi danh sách cột của đặc tả xếp *Người đại diện* trước *Lĩnh vực*. Đây là thứ tự đã có từ trước, phiếu gốc không nêu và khối CÁCH VERIFY cũng không liệt vào điều kiện FAIL, nên KHÔNG dùng để chấm phiếu này — chỉ ghi lại để đối tác/BA biết.
