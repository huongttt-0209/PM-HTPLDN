# Bảng đối chiếu điều kiện — TKHDVMTH_07 (re-verify sau khi dev báo fix, 27/07/2026)

**Mode:** `reverify2` — cột tham chiếu là **điều kiện của BUG GỐC** (`BUG-TKHDVMTH_07`, [`Pass-bug-report-hoi-dap-r2.md`](../bug-reports/hoi-dap/Pass-bug-report-hoi-dap-r2.md) §Bước tái hiện), không phải evidence đối tác.

**Bug gốc:** ô lọc "Trạng thái" không kết hợp AND với điều kiện cứng của thẻ — hệ thống trả nguyên tập của thẻ. Chọn "Tiếp nhận" ở thẻ "Đang xử lý" ra 22 bản ghi (4 Tiếp nhận + 18 Đang xử lý); chọn "Hủy" ở thẻ "Hoàn thành" ra 10 bản ghi (4 Hủy + 6 Hoàn thành).

> ⚠️ **GIỚI HẠN PHẠM VI RE-VERIFY (đọc trước khi dùng kết luận này):** bug gốc đo trên env đối tác `htpldn-uat.ospgroup.vn`, còn lần re-verify này **chỉ đo trên env được giao `18.143.165.120.nip.io`** — phạm vi do người phụ trách chốt ngày 27/07/2026. Kết luận vì vậy chứng minh **mã nguồn đã được sửa**, **chưa** chứng minh bản sửa đã được triển khai lên env đối tác. Dev phải tự xác nhận việc triển khai. Dòng "Môi trường" dưới đây ghi GAP = "Không" theo đúng phạm vi đã chốt đó, không phải khẳng định 2 env giống nhau.

| Điều kiện có thể đổi kết quả | Bug gốc (bug-report §Bước tái hiện) | Mình test (27/07/2026 17:26–17:33) | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | `cbnv_tw` — Cán bộ NV Trung ương (`CB_NV_TW`), đơn vị Cục Bổ trợ tư pháp — BTP · TW | Đúng `cbnv_tw`, đúng vai trò `CB_NV_TW`, đúng đơn vị BTP · TW | Không |
| Môi trường | Env đối tác `htpldn-uat.ospgroup.vn` | Env được giao `18.143.165.120.nip.io` — **phạm vi re-verify đã được chốt là env này**, xem khối cảnh báo phía trên | Không |
| Màn hình | Màn "Quản lý hỏi đáp, vướng mắc pháp lý" (`/hoi-dap`) | Đúng màn đó | Không |
| Thẻ (tab) đang đứng + giá trị ô lọc | Thẻ gộp 2 trạng thái + ô lọc chọn 1 trong 2 trạng thái đó: thẻ "Đang xử lý" + lọc "Tiếp nhận"; thẻ "Hoàn thành" + lọc "Hủy" | Đúng cả 2 tổ hợp, cộng thêm tổ hợp thứ 3 để đối chứng: thẻ "Hoàn thành" + lọc "Hoàn thành" | Không |
| Tiền đề dữ liệu (quyết định lỗi có lộ ra hay không) | Thẻ gộp 2 trạng thái **phải chứa bản ghi của CẢ HAI** trạng thái — nếu thẻ chỉ có 1 trạng thái thì kết quả tình cờ vẫn đúng và lỗi bị che | Đã dựng đủ: thẻ "Hoàn thành" sẵn có 1 `HOAN_THANH` + 1 `HUY`. Thẻ "Đang xử lý" ban đầu chỉ có 1 `DANG_XU_LY` → **đã seed 1 bản ghi `TIEP_NHAN`** (`HD-20260727-001`, tạo qua luồng chuẩn: tạo hỏi đáp → tiếp nhận) để thẻ có đủ 2 trạng thái đúng như điều kiện bug gốc | Không |

**Kết luận:** 0 GAP trong phạm vi đã chốt. Tiền đề dữ liệu — điều kiện duy nhất có thể che lỗi — đã được **tự tạo** thay vì bỏ qua (§Nguyên tắc 4).

## Kết quả đo

**Phép đo quyết định** (chính là phép đo mà bug gốc dùng để chứng minh lỗi): so `tab=Y` đứng một mình với `trangThai=X` **cộng** `tab=Y`. Bug gốc: hai truy vấn **trùng khít** ⇒ tham số trạng thái bị bỏ qua hoàn toàn. Nay: hai truy vấn **khác nhau** ⇒ đã kết hợp AND.

- Thẻ "Đang xử lý" đứng một mình → **2** bản ghi (1 Tiếp nhận + 1 Đang xử lý)
- Thẻ "Đang xử lý" + lọc "Tiếp nhận" → **1** bản ghi, đúng `HD-20260727-001` trạng thái "Tiếp nhận" ✅ *(bug gốc: trả nguyên 22 bản ghi của thẻ)*
- Thẻ "Đang xử lý" + lọc "Đang xử lý" → **1** bản ghi, đúng `HD-20260708-001` trạng thái "Đang xử lý" ✅
- Thẻ "Hoàn thành" đứng một mình → **2** bản ghi (1 Hoàn thành + 1 Đã hủy)
- Thẻ "Hoàn thành" + lọc "Đã hủy" → **1** bản ghi, đúng `HD-20260708-002` trạng thái "Đã hủy" ✅ *(bug gốc: trả 10 bản ghi lẫn cả Hoàn thành)*
- Thẻ "Hoàn thành" + lọc "Hoàn thành" → **1** bản ghi, đúng `HD-20260707-005` trạng thái "Hoàn thành" ✅ *(bug gốc: hai lựa chọn này ra CÙNG một tập 10 bản ghi; nay ra hai bản ghi khác nhau)*

**Đo bằng 2 phương pháp độc lập, kết quả khớp nhau:** đọc bảng hiển thị trên giao diện, và đối chiếu tham số + số bản ghi của chính lần bấm Tìm kiếm đó (`/api/v1/hoi-daps?trangThai=HUY&tab=HOAN_THANH...` trả đúng 1 bản ghi).

**Ghi nhận kèm — lỗi phụ trong bug gốc cũng đã sửa:** nhãn của trạng thái `HUY` trong ô lọc nay là **"Đã hủy"**, đúng quy định `srs-fr-02-hoi-dap.md:1028`; bug gốc ghi nhận web đang hiển thị "Hủy".

**Bằng chứng:**
- [`BUG-TKHDVMTH_07-r3-nipio-PASS-the-dangxuly2-loc-tiepnhan-tra-1.png`](../bug-reports/hoi-dap/image/BUG-TKHDVMTH_07-r3-nipio-PASS-the-dangxuly2-loc-tiepnhan-tra-1.png)
- [`BUG-TKHDVMTH_07-r3-nipio-PASS-the-hoanthanh-loc-dahuy-tra-1.png`](../bug-reports/hoi-dap/image/BUG-TKHDVMTH_07-r3-nipio-PASS-the-hoanthanh-loc-dahuy-tra-1.png)
