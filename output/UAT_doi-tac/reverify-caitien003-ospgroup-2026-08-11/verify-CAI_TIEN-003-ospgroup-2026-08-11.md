# Verify CAI_TIEN-003 — Tải lên văn bản kết quả, nhóm Chi trả chi phí

| | |
|---|---|
| **Mã phiếu** | CAI_TIEN-003 (tab `Task-cải tiến`, dòng 4) |
| **Nhóm chức năng** | V.II — Chi trả chi phí tư vấn pháp luật (UC 68–80) |
| **Ngày đo** | 11/08/2026, 09:15–10:20 |
| **Môi trường** | **Môi trường nghiệm thu của đối tác** — `https://htpldn-uat.ospgroup.vn` · bản dựng giao diện `index-d6TXdPN4.js` · nhãn phiên bản hiển thị trên giao diện **HTPLDN · V1.0.11** |
| **Chuẩn chấm** | Phiếu chốt BA 09/08/2026 — [`phan-hoi-CR-upload-van-ban-chi-tra-2026-08-09.md`](../reverify-week-5/ba-confirm/phan-hoi-CR-upload-van-ban-chi-tra-2026-08-09.md), 16 mục · đối chiếu đặc tả `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-06-chi-tra.md` |
| **Kết luận** | **PASS** — 12 mục ĐẠT · 0 lỗi · 2 mục **không kiểm chứng được trên môi trường này** (mục 4, mục 16) · 2 mục thuộc tài liệu/treo BA (mục 7, mục 12) |

> **Lượt đo này bỏ toàn bộ kết quả cũ, đo lại từ đầu.** Lượt trước (10/08) đo trên môi trường phát triển
> `18.143.165.120.nip.io`; lượt này đo **trên chính môi trường nghiệm thu của đối tác**, dùng dữ liệu và
> tài khoản của môi trường đó. Không kế thừa bất kỳ kết luận nào của lượt trước.

---

## 1. Bảng trạng thái 16 mục BA đã chốt

| # | Nội dung BA chốt | Kết quả | Bằng chứng gọn |
|---|---|---|---|
| 1 | Ô tải đặt ở **đúng 2 chỗ**: Kiểm tra khi **Không đạt** và bước **Phê duyệt**. Thẩm định và Từ chối thanh toán giữ nguyên | ✅ Đạt | Kiểm tra: chọn **Đạt** → 0 ô tải · **Yêu cầu bổ sung** → 0 ô tải · **Không đạt** → 1 ô tải. Thẩm định: cả 2 nhánh Đạt/Không đạt đều 0 ô tải. Từ chối thanh toán: 0 ô tải. `osp-01`, `osp-05`, `osp-06`, `osp-07` |
| 2 | Tệp **bắt buộc** — chặn nút xác nhận khi chưa đính kèm | ✅ Đạt | Chặn ở **cả giao diện lẫn máy chủ**. Kiểm tra/Không đạt: `HTTP 400 · ERR-CT-KT-03 "Văn bản thông báo từ chối là bắt buộc khi kết quả Không đạt"`. Phê duyệt: giao diện báo *"Bản quyết định hỗ trợ là bắt buộc khi phê duyệt"*, gọi thẳng máy chủ bỏ tệp → `HTTP 422 · ERR-CT-PD-04` cùng câu chữ, hồ sơ **giữ nguyên** Chờ phê duyệt |
| 3 | **Không thêm** ô số và ngày văn bản | ✅ Đạt | Biểu mẫu Kiểm tra chỉ có: Kết quả kiểm tra · Lý do · ô tải. Biểu mẫu Phê duyệt chỉ có: Số tiền duyệt · Ghi chú phê duyệt · ô tải. Không có trường số/ngày ở cả hai |
| 4 | **Gửi văn bản kèm sang Cổng Dịch vụ công** cho doanh nghiệp | 🚫 **Không kiểm chứng được** | Kênh tích hợp chưa mở trên môi trường nghiệm thu: 3 đầu mối vào của Cổng (`/tiep-nhan-dvc`, `/bo-sung-dvc`, `/de-nghi-thanh-toan-dvc`) đều trả `HTTP 401 · ERR-CT-AUTH-01`; hai sổ tích hợp `nhat-ky-tich-hops` và `ho-so-lgsp` **đều 0 bản ghi**. Xem §3 |
| 5 | **Không** kiểm chữ ký số — chỉ quét mã độc | ✅ Đạt | Tệp PDF **không ký số** vẫn nhận bình thường (đã ban hành được quyết định HSCT000019). Tệp nhiễm mã độc bị chặn ở **cả 2 nhánh**: *"Tệp chứa mã độc, không thể upload"* (`ERR-FILE-02`). `osp-02`, `osp-10` |
| 6 | Nhánh **hệ thống tự từ chối khi quá hạn bổ sung** → không cần văn bản | ✅ Đạt (xem ghi chú §3.3) | Hai lớp bằng chứng. **(a) Ở mức bản dựng:** toàn bộ giao diện lập trình của bản đang chạy chỉ có **đúng 2** lối tải văn bản kết quả — `…/{id}/kiem-tra/van-ban-ket-qua` và `…/{id}/phe-duyet/van-ban-ket-qua` (lối thứ ba duy nhất là tải **xuống**: `…/{id}/van-ban-ket-qua/{fileId}/download`); không có lối tải nào gắn vào nhánh từ chối/quá hạn, nên nhánh này không thể đòi văn bản. **(b) Ở mức dữ liệu:** hồ sơ `HSCT-HDSD-001` đang ở Từ chối, lý do *"Quá hạn bổ sung hồ sơ (5 ngày làm việc)"*, hạn bổ sung tính từ `13/05/2026` (quá hạn thật), người từ chối = tài khoản hệ thống `00000000-0000-0000-0000-000000000000`, **0 tệp đính kèm** |
| 7 | Sửa câu quy tắc *"cán bộ không nhập tay hồ sơ chi trả"* | 📄 Thuộc tài liệu | Việc sửa đặc tả, không đo được trên phần mềm. BA ghi đã xong 10/08, commit `b067649` |
| 8 | **Không** gửi văn bản kèm cho tư vấn viên | ✅ Đạt | Tài khoản tư vấn viên `tvv_dp_ag_01` bị chặn **toàn bộ** nhóm chi trả: danh sách `403`, chi tiết hồ sơ **do chính họ đứng tên** `403`, tải văn bản kết quả `403` (`ERR-PERM-SYS-00-01`). Hộp thông báo của họ chỉ có tin nhắn chữ, không đính kèm tệp nào. **Đã soát cả hòm thư:** tư vấn viên này nhận đúng 3 thư, trong đó có 1 thư nghiệp vụ chi trả thật *"Hồ sơ chi trả HSCT-HDSD-TVV-001 đã được thẩm định"* (sinh ra lúc 10:09 khi thẩm định hồ sơ họ đứng tên) — nội dung vỏn vẹn một dòng *"Hồ sơ HSCT-HDSD-TVV-001 đã được thẩm định: Đạt."*, **0 tệp đính kèm, 0 đường dẫn**, không nhắc tới văn bản kết quả; 2 thư còn lại là mã đăng nhập và đặt lại mật khẩu |
| 9 | **Không** có ô tải ở bước từ chối thanh toán sau khi đã duyệt | ✅ Đạt | Hồ sơ `HSCT000064` (Đã duyệt): chọn *Từ chối thanh toán* chỉ hiện ô **Lý do từ chối thanh toán**, 0 ô tải. Dữ liệu gửi lên của thao tác này cũng không có trường tệp. `osp-07` |
| 10 | Xem/tải văn bản · **tách nhóm hiển thị** · ai được xem | ✅ Đạt (phần doanh nghiệp: xem §3) | Vùng đính kèm tách rõ **"Văn bản của cơ quan"** riêng khỏi giấy tờ doanh nghiệp nộp, kèm chú thích người tải + thời điểm tải (đúng thành phần #39 của màn chi tiết). Cán bộ nghiệp vụ **và** cán bộ phê duyệt **cùng đơn vị** tải được (`200`); cán bộ **đơn vị khác** không thấy hồ sơ (`404`); tư vấn viên `403`. Tệp tải về **khớp nguyên vẹn** bản gốc: 320 byte, mã kiểm tra `SHA-256 = fb7edbff…e26cd24` trùng đúng với tệp gốc trên máy, dung lượng máy chủ khai báo cũng 320 byte. `osp-03`, `osp-04`, `osp-09` |
| 11 | **Khoá** sửa/xoá tệp sau khi đã gửi | ✅ Đạt | Nhánh Kiểm tra (`HSCT_TEST_1`, đã Từ chối): tải đè `409 · ERR-CT-KT-01`, xoá `403 · ERR-PERM-FILE-01`. Nhánh Phê duyệt (`HSCT000019`, đã Duyệt): tải đè `409 · ERR-CT-PD-01`, xoá `403 · ERR-PERM-FILE-01`; tệp giữ nguyên. Giao diện ghi rõ *"Văn bản do cơ quan ban hành: chỉ xem và tải, không sửa và không xoá."* |
| 12 | Rà lại nhóm chi trả theo Điều 9 hiện hành | 📄 BA treo lại | Ngoài phạm vi lượt đo |
| 13 | **1 tệp · PDF/DOC/DOCX/JPG/PNG · ≤ 20 MB** | ✅ Đạt | Dòng hướng dẫn ghi đúng *"Đúng 1 tệp, định dạng PDF/DOC/DOCX/JPG/PNG, tối đa 20MB."* Thử `.xlsx` → *"Tệp không đúng định dạng…"*; thử PDF **22.020.417 byte (≈21 MB)** → *"Tệp vượt dung lượng cho phép…"*; PDF hợp lệ 320 byte → nhận. Ô tải chỉ giữ **một** vị trí (nút đổi thành **Thay tệp**) |
| 14 | Nhánh **"Từ chối — trả về thẩm định"** không bắt buộc tệp | ✅ Đạt | `HSCT000051`: hộp thoại *Trả về thẩm định* **0 ô tải**, chỉ đòi lý do ≥10 ký tự; xác nhận thành công, hồ sơ về Đang thẩm định, danh sách tệp trống |
| 15 | Nhánh **"Cần bổ sung"** không bắt buộc tệp | ✅ Đạt | `HSCT000062`: chọn *Yêu cầu bổ sung* → **0 ô tải**; xác nhận thành công → hồ sơ sang **Yêu cầu bổ sung**, số lần bổ sung 0 → 1, **0 tệp**. `osp-06` |
| 16 | Nhánh **"bổ sung 3 lần không đạt"** miễn tệp | 🚫 **Không kiểm chứng được** | Không dựng được tình huống: hồ sơ đã đủ 3 lần bổ sung (`HSCT200008`, `HSCT000011`, `HSCT000014`) đều đang ở *Yêu cầu bổ sung*, mà đường duy nhất đưa hồ sơ trở lại *Đang kiểm tra* là doanh nghiệp nộp bổ sung qua Cổng Dịch vụ công — kênh này trả `401 · ERR-CT-AUTH-01`. Xem §3 |

**Tổng:** 12 ✅ đạt · 0 lỗi · 2 🚫 không kiểm chứng được · 2 📄 ngoài phần mềm.

---

## 2. Cách đo và dữ liệu đã dùng

| Hồ sơ | Đơn vị | Dùng cho mục | Đường đi đã chạy |
|---|---|---|---|
| `HSCT_TEST_1` | Cục Bổ trợ tư pháp · TW | 2, 5, 10, 11 | Chờ tiếp nhận → Đang kiểm tra → **Không đạt** kèm văn bản `vb-tu-choi-hop-le.pdf` |
| `HSCT000051` | Bộ Kế hoạch và Đầu tư | 14 | Thẩm định Đạt → Trình phê duyệt → **Trả về thẩm định** (không tệp) |
| `HSCT000062` | Bộ Công Thương | 1, 15 | Đang kiểm tra → **Yêu cầu bổ sung** (không tệp) |
| `HSCT000063` | Bộ Công Thương | 1, 2, 5, 13 | Chờ phê duyệt — thử chặn thiếu tệp, tệp mã độc |
| `HSCT000064` | Bộ Công Thương | 9 | Đã duyệt — mở ô *Từ chối thanh toán* |
| `HSCT000019` | Sở Tư pháp Bắc Ninh | 2, 10, 11, 13 | Đang đánh giá → Đánh giá → Thẩm định Đạt (3.000.000 đ) → Trình phê duyệt → **Phê duyệt kèm quyết định** `qd-ho-tro-hop-le.pdf` |
| `HSCT-HDSD-001` | Sở Tư pháp An Giang | 6 | Chỉ đọc — hồ sơ do hệ thống tự từ chối vì quá hạn bổ sung |

**Tài khoản đã dùng** (đều của môi trường nghiệm thu): `cb_nv_tw_03` (CB NV · TW) · `cbnv_bn`, `cbpd_bn` (Bộ KH&ĐT) · `cb_nv_bn_09`, `cb_pd_bn_09` (Bộ Công Thương) · `cb_nv_dp_09`, `cb_pd_dp_09` (Sở Tư pháp Bắc Ninh) · `cb_nv_dp_10`, `cb_pd_dp_10` (Sở Tư pháp An Giang) · `tvv_dp_ag_01` (Tư vấn viên) · `admin`.

**Vì sao mục 2 phải chạy tới hồ sơ Bắc Ninh:** trên các hồ sơ cấp Bộ, thao tác phê duyệt bị chặn trước
bởi luật trần hỗ trợ (`ERR-CT-TD-03` — mức được duyệt bằng 0 vì hồ sơ mẫu chưa qua bước Đánh giá), nên
không chạm được tới bước kiểm tệp. Phải dựng một hồ sơ đi đủ Đánh giá → Thẩm định để mức được duyệt
lớn hơn 0, mới đo được đúng câu trả lời của máy chủ khi thiếu tệp.

---

## 3. Hai mục không kiểm chứng được — vì sao và cần gì để đo (kèm một giới hạn của mục 6)

### 3.1 Mục 4 — gửi văn bản kèm sang Cổng Dịch vụ công

- Ba đầu mối tích hợp với Cổng trên môi trường nghiệm thu đều trả `HTTP 401` với mã `ERR-CT-AUTH-01`
  (kênh này yêu cầu chứng thư hai chiều, chưa được cấp cho bên kiểm thử).
- Sổ nhật ký tích hợp `nhat-ky-tich-hops` và sổ hồ sơ gửi qua trục `ho-so-lgsp` **đều rỗng (0 bản ghi)**
  — kể cả sau khi ban hành quyết định cho `HSCT000019` lúc 10:04.
- Khi phê duyệt kèm tệp, giao diện chỉ báo *"Phê duyệt hồ sơ thành công"*, **không** có cảnh báo gửi
  Cổng thất bại. Đặc tả quy định khi gửi thất bại thì **ghi log + cảnh báo cán bộ nghiệp vụ** — ở đây
  không thấy cả hai, nên **không kết luận được** là chưa gửi hay gửi im lặng.

  **Cần để đo:** mở kênh Cổng Dịch vụ công trên môi trường nghiệm thu (cấp chứng thư), hoặc dev cho xem
  nhật ký gửi phía máy chủ của giao dịch `HSCT000019` lúc 11/08/2026 10:04.

### 3.2 Mục 16 — nhánh "bổ sung 3 lần không đạt"

- Tình huống cần: hồ sơ đang **Đang kiểm tra** với số lần bổ sung đã là **3/3**, rồi cán bộ chọn
  *Yêu cầu bổ sung* lần nữa → hệ thống phải tự lật sang Từ chối mà **không** đòi văn bản.
- Trên môi trường đang có 3 hồ sơ đủ 3/3 lần bổ sung (`HSCT200008`, `HSCT000011`, `HSCT000014`) nhưng
  cả 3 đều đứng ở **Yêu cầu bổ sung**. Màn chi tiết ở trạng thái này **không có thao tác nào cho cán bộ**
  — đúng thiết kế, vì phải chờ doanh nghiệp nộp bổ sung.
- Đường đưa hồ sơ trở lại *Đang kiểm tra* chỉ có một: doanh nghiệp nộp bổ sung qua Cổng Dịch vụ công —
  cùng kênh đang trả `401` như mục 4.

  **Cần để đo:** một hồ sơ được đặt sẵn ở **Đang kiểm tra** với số lần bổ sung = 3, hoặc mở kênh Cổng.

### 3.3 Giới hạn của mục 6 — nêu rõ để không hiểu quá bằng chứng

Mục 6 vẫn **Đạt**, nhưng cần phân biệt hai câu hỏi khác nhau:

| Câu hỏi | Trên môi trường nghiệm thu |
|---|---|
| Nhánh tự từ chối do quá hạn có **đòi/cho phép** văn bản kết quả không? | **Đã trả lời — Không.** Bản đang chạy chỉ mở đúng 2 lối tải văn bản (bước *Kiểm tra* và bước *Phê duyệt*); không có lối tải nào ở nhánh từ chối. Đây là bằng chứng ở mức bản dựng, không phụ thuộc dữ liệu mẫu |
| Tác vụ nền tự từ chối có **thực sự chạy** trên bản này không? | **Chưa dựng lại được.** Không có đầu mối kích hoạt tác vụ nền, không có quyền chỉnh cơ sở dữ liệu để lùi hạn bổ sung. Chỉ quan sát được kết quả sẵn có: `HSCT-HDSD-001` (hạn bổ sung từ `13/05/2026`, đã bị hệ thống từ chối) |

Nhật ký thao tác **không dùng để đối chứng được** cho hồ sơ này: sổ nhật ký chỉ còn dữ liệu từ
`04/08/2026` trở lại đây (2 173 bản ghi, bản ghi cũ nhất `04/08/2026 03:45`), trong khi mốc quá hạn của
hồ sơ là `13/05/2026` — nằm ngoài phạm vi lưu trữ. Việc tra ra 0 bản ghi cho hồ sơ này **không** nói lên
điều gì theo cả hai hướng.

Câu hỏi thứ hai (tác vụ nền có chạy không) nằm ngoài phạm vi CAI_TIEN-003 — cải tiến này nói về văn bản
kết quả chi trả, không phải về tác vụ tự từ chối. Ghi ở đây để bên nghiệm thu tự quyết có cần đo thêm.

---

## 4. Ghi chú về bằng chứng

- Ảnh `osp-10` (tệp mã độc ở bước Phê duyệt): thông báo của giao diện chỉ hiện khoảng 3 giây nên đã
  **giữ lại đúng thẻ thông báo thật** trên trang để chụp kịp — nội dung, thời điểm và thao tác sinh ra
  nó là thật, chỉ can thiệp để nó không tự biến mất. Cùng thông báo đó đã được ghi nhận độc lập bằng
  bộ bắt sự kiện của trang: *"Tệp chứa mã độc, không thể upload"*.
- Các kết quả gọi thẳng máy chủ (mã lỗi, mã HTTP) đều lấy từ chính phiên đăng nhập của tài khoản tương
  ứng, không dùng đường tắt quản trị.

---

## 5. Dữ liệu đã thay đổi trên môi trường nghiệm thu (bàn giao lại)

Các thao tác dưới đây là **bắt buộc** để dựng được tình huống đo; ghi lại đầy đủ để bên quản trị nắm.

| Đối tượng | Thay đổi | Khôi phục |
|---|---|---|
| `HSCT_TEST_1` | Chờ tiếp nhận → **Từ chối**, đính kèm `vb-tu-choi-hop-le.pdf` | Không lùi được (trạng thái kết thúc) |
| `HSCT000051` | Đang thẩm định → Chờ phê duyệt → **Đang thẩm định** | ✅ đã về trạng thái ban đầu |
| `HSCT000061` | Chờ tiếp nhận → Đang kiểm tra → **Đang đánh giá** | Không lùi được |
| `HSCT000062` | Đang kiểm tra → **Yêu cầu bổ sung**, số lần bổ sung 0 → 1 | Không lùi được |
| `HSCT000019` | Đang đánh giá → **Đã duyệt** 2.845.677 đ, đính kèm `qd-ho-tro-hop-le.pdf` | Không lùi được |
| `HSCT-HDSD-TVV-001` | Đang thẩm định → **Chờ phê duyệt** | Không lùi được |
| Mật khẩu đặt lại thành `Test@1234` | `cb_nv_bn_09`, `cb_pd_bn_09`, `cb_nv_dp_09`, `cb_pd_dp_09`, `cb_nv_dp_10`, `cb_pd_dp_10`, `tvv_dp_ag_01` | Ghi vào `input/input.md` để lượt sau khỏi dò |
| Số căn cước (hệ thống bắt nhập bắt buộc khi đăng nhập lần đầu) | `cb_nv_tw_03` `000000000003` · `cbnv_bn` `000000000011` · `cb_nv_bn_09` `000000000009` · `cb_pd_bn_09` `000000000019` · `cb_nv_dp_09` `000000000029` · `cb_pd_dp_09` `000000000039` · `cb_nv_dp_10` `000000000049` | Giá trị kiểm thử, không có ý nghĩa nghiệp vụ |

> **Lưu ý môi trường:** hệ thống chỉ cho **một phiên đăng nhập cho mỗi tài khoản**; trong lúc đo có
> người khác cùng đăng nhập `cbnv_tw`, `cbpd_tw`, `cbnv_dp`, `admin` nên các phiên đó bị đá ra nhiều lần.
> Đây là hành vi đúng của hệ thống, không phải lỗi.

---

## 6. Danh mục ảnh

| Tệp | Nội dung |
|---|---|
| `osp-01-kiemtra-khongdat-o-tai-bat-buoc.png` | Kiểm tra / Không đạt — ô tải **Văn bản thông báo từ chối (đã ký)** có dấu bắt buộc + dòng ràng buộc tệp |
| `osp-02-kiemtra-tep-ma-doc-bao-loi.png` | Kiểm tra — thao tác tải tệp nhiễm mã độc |
| `osp-03-tach-nhom-van-ban-co-quan-khoa-sua-xoa.png` | Vùng đính kèm tách 2 nhóm + câu *"chỉ xem và tải, không sửa và không xoá"* |
| `osp-04-tooltip-nguoi-tai-thoi-diem-tai.png` | Chú thích hiện **người tải** và **thời điểm tải** cho văn bản của cơ quan |
| `osp-05-pheduyet-o-tai-quyet-dinh-bat-buoc.png` | Phê duyệt — ô tải **Bản quyết định hỗ trợ (đã ký)**, bắt buộc |
| `osp-06-kiemtra-yeucaubosung-khong-co-o-tai.png` | Kiểm tra / **Yêu cầu bổ sung** — không có ô tải nào |
| `osp-07-tuchoi-thanhtoan-khong-co-o-tai.png` | Đã duyệt → **Từ chối thanh toán** — chỉ có ô lý do, không có ô tải |
| `osp-08-pheduyet-rang-buoc-tep-va-tep-da-chon.png` | Phê duyệt — dòng ràng buộc *đúng 1 tệp · PDF/DOC/DOCX/JPG/PNG · ≤ 20MB* và tệp hợp lệ đã chọn |
| `osp-09-da-duyet-van-ban-co-quan-khoa-sua-xoa.png` | Sau khi duyệt — quyết định nằm trong nhóm **Văn bản của cơ quan**, đã khoá sửa/xoá |
| `osp-10-pheduyet-tep-ma-doc-bao-loi.png` | Phê duyệt — thông báo **"Tệp chứa mã độc, không thể upload"** |
