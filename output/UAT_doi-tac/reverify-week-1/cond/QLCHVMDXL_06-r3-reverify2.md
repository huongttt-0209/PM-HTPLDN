# Bảng đối chiếu điều kiện — QLCHVMDXL_06 (re-verify sau khi dev báo fix, 27/07/2026)

**Mode:** `reverify2` — cột tham chiếu là **điều kiện của BUG GỐC** (`BUG-QLCHVMDXL-COT-NOIDUNG`, [`Pass-bug-report-hoi-dap-r2.md`](../bug-reports/hoi-dap/Pass-bug-report-hoi-dap-r2.md) §Bước tái hiện).

**Bug gốc:** cột "Nội dung" bị đặt bề rộng **0 px** ở đúng 3 thẻ "Đã duyệt" / "Công khai" / "Hoàn thành" — 3 thẻ có 13 cột (nhiều hơn 2 cột "Người duyệt" + "Ngày duyệt" bổ sung sau vòng 1). Tổng bề rộng 13 cột là 1632 px trong khi khung bảng chỉ 1128 px, phần dôi ra rơi đúng vào cột "Nội dung". Dữ liệu vẫn còn, chỉ là người dùng không nhìn thấy.

> ⚠️ **GIỚI HẠN PHẠM VI RE-VERIFY (đọc trước khi dùng kết luận này):** bug gốc đo trên env đối tác `htpldn-uat.ospgroup.vn`, còn lần re-verify này **chỉ đo trên env được giao `18.143.165.120.nip.io`** — phạm vi do người phụ trách chốt ngày 27/07/2026. Kết luận vì vậy chứng minh **mã nguồn đã được sửa**, **chưa** chứng minh bản sửa đã được triển khai lên env đối tác. Dev phải tự xác nhận việc triển khai. Dòng "Môi trường" dưới đây ghi GAP = "Không" theo đúng phạm vi đã chốt đó, không phải khẳng định 2 env giống nhau.

| Điều kiện có thể đổi kết quả | Bug gốc (bug-report §Bước tái hiện) | Mình test (27/07/2026 17:29–17:33) | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | `cbpd_tw` — Cán bộ PD Trung ương (`CB_PD_TW`), đơn vị Cục Bổ trợ tư pháp — BTP · TW (đúng vai trò đối tác dùng khi chụp bằng chứng). Bug gốc đã đo lặp bằng `CB_NV_TW` và ghi nhận kết quả y hệt | Đo bằng **cả hai** vai trò như bug gốc: `cbpd_tw` (`CB_PD_TW`) và `cbnv_tw` (`CB_NV_TW`), cùng đơn vị BTP · TW — số đo giống hệt nhau | Không |
| Môi trường | Env đối tác `htpldn-uat.ospgroup.vn` | Env được giao `18.143.165.120.nip.io` — **phạm vi re-verify đã được chốt là env này**, xem khối cảnh báo phía trên | Không |
| Màn hình | Màn "Quản lý hỏi đáp, vướng mắc pháp lý" (`/hoi-dap`) | Đúng màn đó | Không |
| Thẻ (tab) đang đứng | 3 thẻ hỏng: "Đã duyệt", "Công khai", "Hoàn thành"; 4 thẻ đối chứng bình thường: "Tất cả", "Mới", "Đang xử lý", "Chờ phê duyệt" | Quét **đủ cả 7 thẻ**, đo bề rộng từng cột ở từng thẻ | Không |
| Tiền đề dữ liệu | 3 thẻ hỏng phải là thẻ có **13 cột** (đã có đủ 2 cột "Người duyệt" + "Ngày duyệt" bổ sung sau vòng 1) — nếu 2 cột đó chưa có thì bảng chỉ 11 cột và lỗi không lộ ra | Đúng: 3 thẻ "Đã duyệt" / "Công khai" / "Hoàn thành" vẫn đang là **13 cột**, vẫn có đủ "Người duyệt" + "Ngày duyệt"; 4 thẻ còn lại vẫn 11 cột. Tiền đề gây lỗi **còn nguyên** | Không |

**Kết luận:** 0 GAP trong phạm vi đã chốt. Quan trọng: **tiền đề gây lỗi chưa hề bị gỡ** — 3 thẻ vẫn 13 cột, vẫn dôi bề rộng so với khung — nên việc cột "Nội dung" không còn bị bóp về 0 là do bố cục bảng đã được sửa, không phải do 2 cột bổ sung bị gỡ đi.

## Kết quả đo — bề rộng cột "Nội dung" trên cả 7 thẻ

- Thẻ **Tất cả** — 11 cột — cột "Nội dung" **303 px** ✅
- Thẻ **Mới** — 11 cột — **303 px** ✅
- Thẻ **Đang xử lý** — 11 cột — **303 px** ✅
- Thẻ **Chờ phê duyệt** — 11 cột — **303 px** ✅
- Thẻ **Đã duyệt** — 13 cột — **303 px** ✅ *(bug gốc: 0 px)*
- Thẻ **Công khai** — 13 cột — **303 px** ✅ *(bug gốc: 0 px)*
- Thẻ **Hoàn thành** — 13 cột — **303 px** ✅ *(bug gốc: 0 px)*

**Cách bố cục đã đổi:** ở 3 thẻ 13 cột, tổng bề rộng các cột là **1950 px** trong khi khung bảng rộng **1136 px** — bảng nay **cuộn ngang** để chứa phần dôi ra, thay vì bóp một cột về 0. Đúng yêu cầu nêu trong §Kết quả mong đợi của bug gốc: *"khi bổ sung thêm cột cho một số thẻ, tổng bề rộng các cột không được đẩy một cột về 0"*.

**Dữ liệu thật sự hiển thị** (không phải cột rỗng có bề rộng): thẻ "Đã duyệt" → `HD-20260707-004` hiện "Seed UI QLCKPHCHVM_02: câu hỏi batch phê duyệt thuộc TW 02"; thẻ "Công khai" → "Doanh nghiệp hỏi về thủ tục đăng ký kinh doanh…"; thẻ "Hoàn thành" → "Seed HUY verify BA confirm 2026-07-08…".

**Bằng chứng:**
- [`BUG-QLCHVMDXL-COT-NOIDUNG-r3-nipio-PASS-daduyet-cbpd_tw-dung-vaitro-doitac.png`](../bug-reports/hoi-dap/image/BUG-QLCHVMDXL-COT-NOIDUNG-r3-nipio-PASS-daduyet-cbpd_tw-dung-vaitro-doitac.png) — đúng vai trò đối tác
- [`BUG-QLCHVMDXL-COT-NOIDUNG-r3-nipio-PASS-daduyet-cbnv_tw-cot-noidung-303px.png`](../bug-reports/hoi-dap/image/BUG-QLCHVMDXL-COT-NOIDUNG-r3-nipio-PASS-daduyet-cbnv_tw-cot-noidung-303px.png) — vai trò thứ hai, cùng kết quả
