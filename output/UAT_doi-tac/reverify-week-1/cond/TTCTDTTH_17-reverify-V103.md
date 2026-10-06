# Bảng đối chiếu điều kiện — TTCTDTTH_17 (row 237) — RE-VERIFY trên bản triển khai V1.0.3

**Kết luận:** Verify = `Pass`. Lỗi đối tác báo là **có thật** (tôi đã tái hiện được lúc 10:0x trên bản **V1.0.2**), nhưng hệ thống được **triển khai bản V1.0.3 lúc ~11:05** và trên bản mới thao tác chạy **đúng**. Đo lại LIVE, không phải đọc spec.

**Vì sao phải re-verify:** giữa phiên làm việc, thanh bên đổi từ `HTPLDN · V1.0.2` → `HTPLDN · V1.0.3` (kèm 2 phản hồi 502 của request nền `/thong-baos/unread-count` và 1 lần phiên bị đưa về `/login`). Verdict `Open` tôi ghi trước đó dựa trên bản CŨ ⇒ bắt buộc đo lại trên bản đang chạy trước khi để nguyên.

| Điều kiện có thể đổi kết quả | Lúc ra verdict `Open` (bản V1.0.2, 30/07 ~10:0x) | Lúc re-verify (bản V1.0.3, 30/07 11:29–11:30) | GAP? |
|---|---|---|:-:|
| Cạnh máy trạng thái được kiểm | `DANG_THUC_HIEN → HOAN_THANH` của CTDT, kích hoạt khi MỌI khóa học con đã `HOAN_THANH` | **Đúng cạnh đó**: CTDT ở `DANG_THUC_HIEN`, khóa học con duy nhất chuyển `HOAN_THANH` | Không |
| Sự kiện kích hoạt | Duyệt kết quả khóa học cuối cùng trên giao diện → khóa học sang `HOAN_THANH` | Cùng đường đó: `finish` → `submit-result` → `approve-result` (bởi CB Phê duyệt) → khóa học `HOAN_THANH`. Chốt kiểm trạng thái nằm ở máy chủ nên cùng một xử lý | Không |
| Bản ghi dùng để kiểm | CTDT `CTDT-QAW7-01` (bản ghi seed sẵn) + khóa học con `KH-QAW7-HOINGHI` | CTDT **mới tạo** `CTDT-BTP-TW-2026-0001` + khóa học con **mới tạo** `KH-20260730-002`, đi trọn luồng Dự thảo → Chờ duyệt → Đã duyệt rồi mới khai giảng. Dùng bản ghi MỚI là **chặt hơn**: loại được khả năng "chỉ do di trú dữ liệu sửa số cũ", chứng minh logic chạy cho sự kiện MỚI | Không |
| Vai trò / tài khoản | `cbnv_tw` (CB Nghiệp vụ - Trung ương) thao tác, khâu phê duyệt do CB Phê duyệt | Y như vậy: `cbnv_tw` tạo + khai giảng; `cbpd_tw_01` (CB Phê duyệt - Trung ương) duyệt CTDT và khóa học | Không |
| Cách đọc kết quả | Đọc lại bản ghi CTDT + thẻ đếm trên danh sách | Đọc lại bản ghi CTDT (`trangThai`, `ngayCapNhat`) **và** xem thanh tiến trình + thẻ đếm trên giao diện | Không |

## Artifact real-data (Gate bằng chứng — `Pass` bắt buộc artifact QUAN SÁT từ re-verify LIVE)

- `reverify-audit/TTCTDTTH_16/06-PASS-V1.0.3-the-dang-thuc-hien-2-hoan-thanh-2.png` — đã mở đọc: màn **Chương trình đào tạo** trên bản `HTPLDN · V1.0.3`, thẻ **"Đang thực hiện 2"** và **"Hoàn thành 2"** đã có số (bug gốc ghi nhận cả hai đều bằng 0), danh sách có CTDT mới `CTDT-BTP-TW-2026-0001`.
- `reverify-audit/TTCTDTTH_17/07-PASS-V1.0.3-ctdt-tu-chuyen-hoan-thanh.png` — đã mở đọc: chi tiết `CTDT-BTP-TW-2026-0001`, thanh tiến trình **Dự thảo ✓ → Chờ duyệt ✓ → Đã duyệt ✓ → Đang thực hiện ✓ → 5 Hoàn thành** ⇒ bước "Đang thực hiện" đã được kích hoạt (đúng điều bug gốc nói là không bao giờ tới được).
- **Số đo thao tác thật (đọc lại máy chủ trước/sau sự kiện)**:
  - Trước: `CTDT-BTP-TW-2026-0001` = `DANG_THUC_HIEN`, `ngayCapNhat = 2026-07-30T04:30:19.207Z`.
  - Sự kiện: `POST /api/v1/khoa-hocs/13cfd526-…/approve-result` → **200**, khóa học `HOAN_THANH`.
  - Sau (3s): CTDT = **`HOAN_THANH`**, `ngayCapNhat = 2026-07-30T04:30:43.659Z` ⇒ hệ thống **tự** cập nhật trạng thái chương trình cha.

## Phương pháp thứ hai (bắt buộc)

- **Dựng bản ghi mới đi trọn luồng** thay vì đọc lại bản ghi cũ: tạo CTDT → `submit` → `approve` (bởi `cbpd_tw_01`) → tạo khóa học con → `submit` → `approve` → `start`. Nếu chỉ đọc bản ghi cũ thì không phân biệt được "đã sửa logic" với "chỉ chỉnh dữ liệu cũ".
- **Loại giả thuyết "chỉ di trú dữ liệu, logic vẫn hỏng"**: 3 CTDT có sẵn đều mang **cùng một** `ngayCapNhat = 2026-07-30T04:05:47.809Z` (trùng tới mili-giây) ⇒ đúng là có một lượt cập nhật hàng loạt lúc triển khai. Nhưng phép thử trên bản ghi **mới tạo sau đó** vẫn tự chuyển trạng thái ⇒ logic thật sự đã chạy, không chỉ là chỉnh dữ liệu.
- **Kiểm cả cạnh phía trước** (phiếu TTCTDTTH_16): CTDT tới được `DANG_THUC_HIEN` một cách **tự động** khi khóa học con khai giảng (`04:30:19.207Z`) — tức tiền đề của cạnh này không còn bị chặn. Bug gốc nói hai trạng thái cuối "không thể đạt" vì mắc ở cạnh trước; nay cả hai cạnh đều đi được.
- **Đối chiếu đặc tả — trích nguyên văn** (`srs-fr-03-dao-tao.md`): `:2129` và `:2145` quy định cạnh `DANG_THUC_HIEN → HOAN_THANH` tự động khi **mọi** `KHOA_HOC` con đã `HOAN_THANH`; `:2119` là phần khai máy trạng thái SM-CTDT ⇒ hành vi quan sát được trên V1.0.3 **khớp** đặc tả.

## Pass đối kháng (tự bác trước khi ghi sheet)

1. *"Chỉ là dữ liệu bị chỉnh hàng loạt lúc deploy, logic chưa sửa."* — Bác: bản ghi CTDT tạo **sau** thời điểm cập nhật hàng loạt (`04:28:20`) vẫn tự chuyển đúng ở **cả hai** cạnh (`04:30:19` và `04:30:43`), mỗi lần ngay sau đúng sự kiện tương ứng.
2. *"Tôi kiểm qua API nên không đại diện cho thao tác trên giao diện."* — Bác: chốt kiểm chuyển trạng thái chương trình nằm **phía máy chủ**, kích hoạt bởi cùng các endpoint mà giao diện gọi khi duyệt kết quả khóa học. Kết quả cuối cũng được xác nhận **trên giao diện**: thanh tiến trình của CTDT hiện bước **5 Hoàn thành**, thẻ đếm "Hoàn thành" trên danh sách đã có số.
3. *"Có thể chỉ đúng với CTDT có 1 khóa học con — nhiều con thì chuyển sớm."* — **Đã đo và bác được (bổ sung 31/07/2026 00:45–00:52, bản V1.0.3).** Lượt đầu tôi tự khai đây là phần **chưa kiểm**; nay đã dựng và đo bằng sự kiện thật, chi tiết ở §"Đo bổ sung" ngay dưới. Kết quả: chương trình cha có **9 khóa con** mà mới **4** con hoàn thành thì **vẫn ở `DANG_THUC_HIEN`**, không chuyển sớm.
4. *"Không tái hiện thì phải ghi Reject."* — Bác: đối tác **có bằng chứng thật** và chính tôi cũng đã tái hiện được trên bản cũ ⇒ tuyệt đối không phủ nhận báo cáo. Cột `Trạng thái dev fix 1` ghi `dev done` (bản sửa đã lên) + cột `Verify` ghi `Pass` (QA đã đo lại LIVE) — đúng nghĩa 2 cột, và note nói rõ mốc thời gian để không ai hiểu là "báo cáo sai".

## Đo bổ sung 31/07/2026 — chống chuyển sớm khi CTDT có NHIỀU khóa con

**Vì sao phải đo:** lượt trước tôi dựng CTDT chỉ có **1** khóa con, nên điều kiện *"mọi con đã hoàn thành"* thoả một cách tầm thường. Nếu dev sửa quá tay thành *"có con nào hoàn thành là chuyển"* thì phép thử cũ **không bắt được** — mà theo quy ước re-verify, fix đẻ ra lỗi mới cùng luồng thì phải `Reopen`. Nên phải đo nhánh này trước khi để verdict `Pass`.

**Cách dựng (thao tác thật trên giao diện, không gọi dịch vụ trực tiếp):**

| Bước | Thao tác | Quan sát |
|---|---|---|
| Tiền đề | Mở `CTDT-SEED-0001` — chương trình có **9 khóa học con**, trong đó **3** đã *Hoàn thành* (`AAA-KH-DP`, `AAA-KH-TW`, `AAA-KH-BN`) | Thanh tiến trình cha đang ở bước **4 Đang thực hiện** |
| Sự kiện kích hoạt | Đăng nhập `cbpd_tw_03` (CB Phê duyệt - Trung ương) → mở khóa con `KH-20260716-002` (*Chờ duyệt KQ*) → bấm **[Duyệt KQ]** → hộp thoại *"Phê duyệt kết quả? … khóa học chuyển sang Hoàn thành"* → bấm **[Phê duyệt KQ]** | Thông báo *"Đã phê duyệt kết quả thành công"*; thanh tiến trình khóa con nhảy sang **7 Hoàn thành** |
| Đọc kết quả ở cha | Quay ra **Chương trình đào tạo** → mở lại `CTDT-SEED-0001` | Cha **vẫn ở bước 4 Đang thực hiện**; dòng trên danh sách cũng vẫn ghi *Đang thực hiện* |
| Đếm lại khóa con | Đọc bảng khóa học con sau sự kiện | **4/9** *Hoàn thành*; **5** con chưa xong: `KH-20260730-001` (*Đã duyệt*), `KH-20260716-001` (*Chờ duyệt*), `DDD-KH-011` (*Đang diễn ra*), `DDD-KH-012` (*Đã kết thúc*), `KH-SEED-0001` (*Đã kết thúc*) |

**Kết luận nhánh này:** hệ thống **không** chuyển chương trình cha sang `HOAN_THANH` khi mới có một phần khóa con hoàn thành ⇒ đúng `srs-fr-03-dao-tao.md:2129`/`:2145` (chỉ chuyển khi **mọi** khóa con đã `HOAN_THANH`), và loại được giả thuyết dev sửa quá tay.

**Đây là sự kiện LIVE, không phải quan sát tĩnh:** trạng thái cha được đọc **sau** khi vừa có một khóa con chuyển sang *Hoàn thành* trong cùng phiên, tức đúng lúc chốt kiểm tính lại. Nếu chỉ mở CTDT ra nhìn thấy *Đang thực hiện* mà không kích hoạt sự kiện thì không kết luận được gì — vì có thể chốt kiểm chưa từng chạy cho bản ghi đó.

**Ảnh:** `../bug-reports/image/BUG-TTCTDTTH_17-r6-khong-chuyen-som-4-tren-9-khoa-con-hoan-thanh.png` — chi tiết `CTDT-SEED-0001` sau sự kiện: thanh tiến trình dừng ở **4 Đang thực hiện**, bảng khóa con hiện `KH-20260716-002` đã *Hoàn thành*.

## Ngoài tiêu chí phiếu — có thấy gì bất thường không?

- **Đáng lưu ý cho cả đợt**: hệ thống được triển khai bản mới **giữa lúc UAT đang chạy** (V1.0.2 → V1.0.3, ~11:05). Hệ quả thực tế: phiên đăng nhập bị ngắt, 502 tạm thời, và **verdict ghi trước 11:05 có thể lỗi thời**. Vì vậy tôi đã đo lại toàn bộ 5 phiếu trên V1.0.3 (2 phiếu chuyển `Pass`, 3 phiếu còn lỗi). Đề nghị phía dev thông báo trước khi deploy vào giờ UAT.
- **Ghi nhận phụ khi đo bổ sung:** thử bấm **[Gửi duyệt KQ]** cho khóa `DDD-KH-012` bằng `cbnv_tw_03` thì bị từ chối, thông báo *"Đơn vị của người phê duyệt khác đơn vị của khóa học"* — đây là **chặn phạm vi đơn vị**, đúng nghiệp vụ, không phải lỗi; ghi lại để lần sau chọn đúng khóa cùng đơn vị cho nhanh.
- **Dữ liệu bị thay đổi trong lượt đo bổ sung (khai báo để không ai bất ngờ):** khóa `KH-20260716-002` được đẩy từ *Chờ duyệt KQ* → **Hoàn thành** (đây chính là sự kiện dùng để đo). Không đụng tới khóa nào khác của `CTDT-SEED-0001`.
