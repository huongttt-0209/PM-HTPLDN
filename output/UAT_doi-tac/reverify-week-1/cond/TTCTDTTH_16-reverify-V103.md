# Bảng đối chiếu điều kiện — TTCTDTTH_16 (row 236) — RE-VERIFY trên bản triển khai V1.0.3

**Kết luận:** Verify = `Pass`. Lỗi đối tác báo là **có thật** (tôi đã tái hiện được lúc 10:0x trên bản **V1.0.2**), nhưng hệ thống được **triển khai bản V1.0.3 lúc ~11:05** và trên bản mới thao tác chạy **đúng**. Đo lại LIVE, không phải đọc spec.

**Vì sao phải re-verify:** giữa phiên làm việc, thanh bên đổi từ `HTPLDN · V1.0.2` → `HTPLDN · V1.0.3` (kèm 2 phản hồi 502 của request nền `/thong-baos/unread-count` và 1 lần phiên bị đưa về `/login`). Verdict `Open` tôi ghi trước đó dựa trên bản CŨ ⇒ bắt buộc đo lại trên bản đang chạy trước khi để nguyên.

| Điều kiện có thể đổi kết quả | Lúc ra verdict `Open` (bản V1.0.2, 30/07 ~10:0x) | Lúc re-verify (bản V1.0.3, 30/07 11:29–11:30) | GAP? |
|---|---|---|:-:|
| Cạnh máy trạng thái được kiểm | `DA_DUYET → DANG_THUC_HIEN` của CTDT, kích hoạt bởi khóa học con sang `DANG_DIEN_RA` | **Đúng cạnh đó**: CTDT ở `DA_DUYET`, khóa học con chuyển `DANG_DIEN_RA` | Không |
| Sự kiện kích hoạt | Bấm **[Khai giảng]** trên giao diện → `POST /api/v1/khoa-hocs/{id}/start` | Cùng **một endpoint** `POST /api/v1/khoa-hocs/{id}/start` (chính là request mà nút [Khai giảng] gọi — đã ghi nhận trong bug entry gốc) ⇒ cùng đường xử lý phía máy chủ | Không |
| Bản ghi dùng để kiểm | CTDT `CTDT-QAW7-01` (bản ghi seed sẵn) + khóa học con `KH-QAW7-HOINGHI` | CTDT **mới tạo** `CTDT-BTP-TW-2026-0001` + khóa học con **mới tạo** `KH-20260730-002`, đi trọn luồng Dự thảo → Chờ duyệt → Đã duyệt rồi mới khai giảng. Dùng bản ghi MỚI là **chặt hơn**: loại được khả năng "chỉ do di trú dữ liệu sửa số cũ", chứng minh logic chạy cho sự kiện MỚI | Không |
| Vai trò / tài khoản | `cbnv_tw` (CB Nghiệp vụ - Trung ương) thao tác, khâu phê duyệt do CB Phê duyệt | Y như vậy: `cbnv_tw` tạo + khai giảng; `cbpd_tw_01` (CB Phê duyệt - Trung ương) duyệt CTDT và khóa học | Không |
| Cách đọc kết quả | Đọc lại bản ghi CTDT + thẻ đếm trên danh sách | Đọc lại bản ghi CTDT (`trangThai`, `ngayCapNhat`) **và** xem thanh tiến trình + thẻ đếm trên giao diện | Không |

## Artifact real-data (Gate bằng chứng — `Pass` bắt buộc artifact QUAN SÁT từ re-verify LIVE)

- `reverify-audit/TTCTDTTH_16/06-PASS-V1.0.3-the-dang-thuc-hien-2-hoan-thanh-2.png` — đã mở đọc: màn **Chương trình đào tạo** trên bản `HTPLDN · V1.0.3`, thẻ **"Đang thực hiện 2"** và **"Hoàn thành 2"** đã có số (bug gốc ghi nhận cả hai đều bằng 0), danh sách có CTDT mới `CTDT-BTP-TW-2026-0001`.
- `reverify-audit/TTCTDTTH_17/07-PASS-V1.0.3-ctdt-tu-chuyen-hoan-thanh.png` — đã mở đọc: chi tiết `CTDT-BTP-TW-2026-0001`, thanh tiến trình **Dự thảo ✓ → Chờ duyệt ✓ → Đã duyệt ✓ → Đang thực hiện ✓ → 5 Hoàn thành** ⇒ bước "Đang thực hiện" đã được kích hoạt (đúng điều bug gốc nói là không bao giờ tới được).
- **Số đo thao tác thật (đọc lại máy chủ trước/sau sự kiện)**:
  - Trước: `CTDT-BTP-TW-2026-0001` = `DA_DUYET`, `ngayCapNhat = 2026-07-30T04:28:57.365Z`.
  - Sự kiện: `POST /api/v1/khoa-hocs/13cfd526-…/start` → **200**, khóa học `DANG_DIEN_RA`.
  - Sau (2,5s): CTDT = **`DANG_THUC_HIEN`**, `ngayCapNhat = 2026-07-30T04:30:19.207Z` ⇒ hệ thống **tự** cập nhật trạng thái chương trình cha.

## Phương pháp thứ hai (bắt buộc)

- **Dựng bản ghi mới đi trọn luồng** thay vì đọc lại bản ghi cũ: tạo CTDT → `submit` → `approve` (bởi `cbpd_tw_01`) → tạo khóa học con → `submit` → `approve` → `start`. Nếu chỉ đọc bản ghi cũ thì không phân biệt được "đã sửa logic" với "chỉ chỉnh dữ liệu cũ".
- **Loại giả thuyết "chỉ di trú dữ liệu, logic vẫn hỏng"**: 3 CTDT có sẵn đều mang **cùng một** `ngayCapNhat = 2026-07-30T04:05:47.809Z` (trùng tới mili-giây) ⇒ đúng là có một lượt cập nhật hàng loạt lúc triển khai. Nhưng phép thử trên bản ghi **mới tạo sau đó** vẫn tự chuyển trạng thái ⇒ logic thật sự đã chạy, không chỉ là chỉnh dữ liệu.
- **Kiểm cả cạnh kế tiếp** (phiếu TTCTDTTH_17): hoàn thành khóa học con duy nhất (`finish` → `submit-result` → `approve-result` → `HOAN_THANH`) thì CTDT **tự** chuyển `DANG_THUC_HIEN` → **`HOAN_THANH`** (`ngayCapNhat 04:30:43.659Z`). Hai cạnh cuối của máy trạng thái SM-CTDT đều đạt được ⇒ đúng phần bug gốc nói là "không thể đạt".
- **Đối chiếu đặc tả — trích nguyên văn** (`srs-fr-03-dao-tao.md`): `:2128` — *"DA_DUYET --> DANG_THUC_HIEN : Có ≥1 KHOA_HOC con DA_CONG_KHAI / DANG_DIEN_RA"*; `:2144` — *"| DA_DUYET | DANG_THUC_HIEN | Auto khi có ≥1 KHOA_HOC con DA_CONG_KHAI / DANG_DIEN_RA | — | (auto) |"* ⇒ hành vi quan sát được trên V1.0.3 **khớp** đặc tả.

## Pass đối kháng (tự bác trước khi ghi sheet)

1. *"Chỉ là dữ liệu bị chỉnh hàng loạt lúc deploy, logic chưa sửa."* — Bác: bản ghi CTDT tạo **sau** thời điểm cập nhật hàng loạt (`04:28:20`) vẫn tự chuyển đúng ở **cả hai** cạnh (`04:30:19` và `04:30:43`), mỗi lần ngay sau đúng sự kiện tương ứng.
2. *"Tôi kiểm qua API nên không đại diện cho thao tác trên giao diện."* — Bác: endpoint `POST /khoa-hocs/{id}/start` chính là request mà nút **[Khai giảng]** gọi — đã ghi nhận trong bug entry gốc (`"thao_tac": "POST /api/v1/khoa-hocs/…/start"`). Chốt kiểm trạng thái nằm ở máy chủ nên hai đường vào cùng một xử lý. Ngoài ra kết quả cuối được xác nhận **trên giao diện** (thanh tiến trình + thẻ đếm).
3. *"Có thể chỉ đúng với CTDT có 1 khóa học con."* — Ghi nhận là giới hạn của phép thử: CTDT tôi dựng có 1 khóa học con. Nhưng cạnh `DA_DUYET → DANG_THUC_HIEN` theo đặc tả chỉ cần **≥1** con `DA_CONG_KHAI/DANG_DIEN_RA` nên 1 con là đủ để kiểm đúng điều kiện. Riêng cạnh sang `HOAN_THANH` đòi **mọi** con hoàn thành — với 1 con thì điều kiện "mọi con" thoả, chưa kiểm được trường hợp nhiều con hoàn thành một phần. Phần đó **nay đã đo xong** (bổ sung 31/07/2026 00:52): xem [TTCTDTTH_17-reverify-V103.md](TTCTDTTH_17-reverify-V103.md) §Đo bổ sung — `CTDT-SEED-0001` có 9 khóa con, sau khi 1 con nữa chuyển *Hoàn thành* (4/9) thì cha **vẫn** ở `DANG_THUC_HIEN`.
4. *"Không tái hiện thì phải ghi Reject."* — Bác: đối tác **có bằng chứng thật** và chính tôi cũng đã tái hiện được trên bản cũ ⇒ tuyệt đối không phủ nhận báo cáo. Cột `Trạng thái dev fix 1` ghi `dev done` (bản sửa đã lên) + cột `Verify` ghi `Pass` (QA đã đo lại LIVE) — đúng nghĩa 2 cột, và note nói rõ mốc thời gian để không ai hiểu là "báo cáo sai".

## Ngoài tiêu chí phiếu — có thấy gì bất thường không?

- **Đáng lưu ý cho cả đợt**: hệ thống được triển khai bản mới **giữa lúc UAT đang chạy** (V1.0.2 → V1.0.3, ~11:05). Hệ quả thực tế: phiên đăng nhập bị ngắt, 502 tạm thời, và **verdict ghi trước 11:05 có thể lỗi thời**. Vì vậy tôi đã đo lại toàn bộ 5 phiếu trên V1.0.3 (2 phiếu chuyển `Pass`, 3 phiếu còn lỗi). Đề nghị phía dev thông báo trước khi deploy vào giờ UAT.
- **Phần trước đây chưa kiểm — nay đã kiểm** (xem Pass đối kháng #3): trường hợp CTDT có **nhiều** khóa học con mà chỉ một phần hoàn thành thì CTDT phải KHÔNG chuyển sang `HOAN_THANH`. Đã dựng và đo bằng sự kiện thật ngày 31/07/2026 00:52 trên `CTDT-SEED-0001` (9 khóa con, 4 con hoàn thành) → cha **không** chuyển sớm. Chi tiết ở [TTCTDTTH_17-reverify-V103.md](TTCTDTTH_17-reverify-V103.md) §Đo bổ sung.
