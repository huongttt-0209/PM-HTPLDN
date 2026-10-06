# Báo cáo đợt verify dev fix — FLOW 04 — 2026-08-06

**Phạm vi:** 2 case theo yêu cầu — `LKHDG_12` (dòng 126) · `QLHSDNHTCP_03` (dòng 72), tab `bug`.
**Môi trường:** https://18.143.165.120.nip.io — **HTPLDN · V1.0.8**, gói mã `assets/index-DThrFe1_.js`.
**Tài khoản đã dùng:** `cbnv_tw` · `cbpd_tw_01` · `cbpd_bn`. **Khung nhìn:** 1440×741.

> **KHÔNG ghi gì lên bảng** theo yêu cầu đầu đợt. Ô kết quả QA + ô note để trống; ô "Trạng thái dev fix" và
> "Dopai" chỉ đọc. Verdict dưới đây nằm trong hồ sơ, chưa vào bảng.

---

## Kết quả

| Mã TC | Dòng | Verdict | Vì sao | Chủ việc |
|---|---|---|---|---|
| `LKHDG_12` | 126 | **Reopen** | Vế "xuất Excel không đúng tiêu chí lọc" **vẫn tái hiện** trên 2 bộ lọc khác cột nhau. 2 vế còn lại (thiếu cột · chữ không dấu) đã hết lỗi | **Dev BE** |
| `QLHSDNHTCP_03` | 72 | **Cần BA** | **Cả 2 vế đối tác phản ánh đều đã hết lỗi.** Nhưng cột đang tranh chấp hiện thêm nhãn thứ 5 "Đã hoàn thành" cho hồ sơ đã kết thúc — đặc tả im lặng, QA không tự chấm | **BA** |

Hồ sơ: [`bug-report.md`](bug-report.md) · [`cau-hoi-BA.md`](cau-hoi-BA.md) · tiêu chí:
[`tieuchi/LKHDG_12.md`](tieuchi/LKHDG_12.md) · [`tieuchi/QLHSDNHTCP_03.md`](tieuchi/QLHSDNHTCP_03.md)

🔴 **Hiệu lực:** mọi kết luận "đã hết lỗi" chỉ đúng cho **env dev + bản dựng V1.0.8**. Bằng chứng đối tác quay
trên env nghiệm thu `htpldn-uat.ospgroup.vn` (V1.0 và V1.0.2). Đối tác mở env của họ lên **chưa chắc đã hết lỗi**
cho tới khi V1.0.8 được đưa sang đó.

---

## 1. Lỗi phát hiện thêm ngoài phạm vi

**Không phát hiện thêm lỗi nào.** Câu này dựa trên ảnh đã mở đọc, không phải suy đoán. Hai điều bất thường có
gặp trong lúc đo, đã truy tới cùng và **đều không phải lỗi**:

| Quan sát ban đầu | Kiểm chứng | Kết luận |
|---|---|---|
| Bấm [Xuất Excel] → bộ theo dõi DOM bắt được **4 sự kiện thông báo** ⇒ nghi thông báo đúp | Cài bộ đếm chạy **trước** lúc bấm: số thẻ thông báo **cùng tồn tại** tối đa = **1**; số yêu cầu tới đường dẫn xuất = **1** | **Không phải lỗi.** 4 sự kiện là cặp *thẻ bọc + thẻ trong* bị dựng lại 2 lần trong cùng 1 mili-giây. Đếm theo số phần tử là ra "lỗi ma" |
| `cbpd_tw_01` mở Chi trả → bảng ghi "Không có hồ sơ nào phù hợp." trong khi tab đầu tiên đếm **14** | Đọc tab **đang được chọn**: là **"Chờ phê duyệt"** (0 hồ sơ), không phải "Tất cả" | **Không phải lỗi.** Vai trò CB Phê duyệt mặc định vào tab việc của mình. Tôi đọc nhầm tab đầu danh sách thành tab đang chọn |

Hai điểm khác **có thấy** nhưng **nằm ngoài 2 vế đối tác phản ánh** ở case này, nên chỉ ghi nhận, không log
thành lỗi và không dùng để chấm:
- Bảng Chi trả có cột **"Mức HT %"** không nằm trong danh sách thành phần của SCR-V.II-01.
- Nhãn thứ 5 **"Đã hoàn thành"** ở cột SLA — đã chuyển thành câu hỏi BA (`cau-hoi-BA.md` §1), không log lỗi.

**Vì chưa ghi bảng đợt này** nên chưa phát sinh dòng case mới nào cần thêm vào bảng theo dõi.

---

## 2. Dữ liệu đã seed / thay đổi

**1 bản ghi được tạo mới. Không sửa, không xoá bản ghi nào có sẵn.**

| Env | Bản ghi | Việc đã làm | Vì sao |
|---|---|---|---|
| `18.143.165.120.nip.io` (dev) | **`DG-20260806-0001`** — *"QA FLOW04 LKHDG_12 seed So bo 6 thang 20260806"* | **Tạo mới** qua giao diện ([+ Thêm mới] → [Lưu nháp]) bằng `cbnv_tw`. Tần suất *Sơ bộ 6 tháng* · Đối tượng *Đào tạo* · Kỳ 01/01/2026–30/06/2026 · Cơ quan được đánh giá *Bộ Công an* · trạng thái *Lập kế hoạch* | Cả **19 đợt sẵn có đều Tần suất "Tròn năm"** → bộ lọc mà đối tác dùng (`tanSuat=TRON_NAM`) **không cắt bớt được gì**, phép đo sẽ vô nghĩa. Đồng thời đóng luôn 2 dạng còn thiếu của M (Sơ bộ 6 tháng, Đào tạo) |

Ghi chú: ô "Cơ quan được đánh giá" chọn **Bộ Công an** chỉ vì đó là mục đầu danh sách thả xuống — trường này
không ảnh hưởng tới phép đo bộ lọc/cột. Xoá được bằng `cbnv_tw` (đợt ở trạng thái *Lập kế hoạch* có nút Xoá)
nếu cần trả env về nguyên trạng.

**Không seed gì cho `QLHSDNHTCP_03`** — env đã sẵn 14 hồ sơ phủ đủ 4/4 mức cảnh báo.

---

## 3. Case chưa chốt được

Không có case nào phải để **ô trống**. Cả 2 case đều đo được, 0 GAP điều kiện còn hở.

| Case | Trạng thái | Vì sao chưa xong | Cần ai làm gì |
|---|---|---|---|
| `QLHSDNHTCP_03` | **Cần BA** (đã đo đủ, không chấm) | Đặc tả không quy định cột "SLA" hiển thị gì khi hồ sơ đã kết thúc; BR-SLA-02 chỉ có 4 mức, phần mềm hiện nhãn thứ 5 "Đã hoàn thành" | **BA** trả lời 3 câu ở `cau-hoi-BA.md` §1 → QA chấm lại, không cần đo lại |
| `LKHDG_12` | **Reopen** (đã chốt là lỗi) | — | **Dev BE** áp bộ lọc vào truy vấn của đường dẫn xuất tệp → QA verify theo khối CÁCH VERIFY trong `bug-report.md` |

**Một hạn chế đã ghi rõ, không phải blocker:** không đóng được điều kiện vai trò bằng đúng `cbpd_bn` (vai trò
vòng 2 của đối tác) vì **cấp Bộ ngành có 0 hồ sơ chi trả** trên env này — blocker khách quan, không phải tiền đề
tôi tạo được mà không tạo. Đã đóng bằng cách thử **đủ nhánh vai trò có dữ liệu** (CB Nghiệp vụ và CB Phê duyệt),
**hai nhánh cho cùng một kết quả**.
