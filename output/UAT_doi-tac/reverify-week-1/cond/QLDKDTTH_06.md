# Bảng đối chiếu điều kiện — QLDKDTTH_06 (row 272) — Duyệt học viên khi khóa học đã đóng đăng ký

**Kết luận:** Open (Major). Tái hiện **2/2** bằng thao tác thật trên đúng vai trò + đúng tiền đề của đối tác.

Phiếu ghi kỳ vọng *"Hệ thống từ chối thao tác và hiển thị thông báo 'Khóa học đã đóng đăng ký'."*, thực tế *"Hệ thống hiển thị thông báo thành công"* → **TÁI HIỆN ĐÚNG**.

Tôi dựng lại đúng tiền đề của đối tác (khóa học **Đã duyệt**, cửa sổ đăng ký **01/07/2026 → 03/07/2026** đã đóng, hôm nay 30/07/2026 — trễ 27 ngày), thêm học viên nhập tay để có hồ sơ **Chờ duyệt**, rồi bấm **[Phê duyệt]**. Hệ thống **duyệt thành công**: thông báo xanh *"Đã phê duyệt đăng ký"*, hồ sơ chuyển **Đã duyệt**, máy chủ trả **201**. Không có bất kỳ chốt kiểm nào về cửa sổ đăng ký.

| Điều kiện có thể đổi kết quả | Đối tác (evidence `partner-evidence/QLDKDTTH_07.webm`, full-res) | Mình test (env nip.io, 30/07/2026 10:39–10:41) | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | Frame `t000.00s` góc phải: **Cán bộ NV Trung ương · CB_NV_TW**, phạm vi **BTP · TW** | `cbnv_tw` — CB Nghiệp vụ - Trung ương, BTP · TW (đúng vai trò + đúng cấp) | Không |
| Entity + **trạng thái** (state machine) | Hồ sơ đăng ký của *Hoàng Minh Đức* ở **Chờ duyệt** (frame `t000.00s`, cột Trạng thái + 2 hành động Phê duyệt/Từ chối); khóa học `KH-20260703-005` ở bước **3 Đã duyệt** | Hồ sơ *QA Verify QLDKDTTH_06* (và lần 2: *… lan2*) ở **Chờ duyệt**; khóa học `KH-20260730-001` ở bước **3 Đã duyệt** | Không |
| Dữ liệu tiền đề — **cửa sổ đăng ký đã đóng** | Frame `t003.03s` (đối tác tự bôi xanh ô để nhấn mạnh): **Mở đăng ký từ 01/07/2026 · Mở đăng ký đến 03/07/2026**; video quay **24/07/2026 16:24** ⇒ đã đóng 21 ngày. Sĩ số tối đa 2, Đã đăng ký 0 (còn chỗ ⇒ không phải lỗi "lớp đầy") | Ảnh `05-tien-de-cua-so-dang-ky-da-dong.png`: **Mở đăng ký từ 01/07/2026 · Mở đăng ký đến 03/07/2026** — trùng khít ngày của đối tác; hôm nay **30/07/2026** ⇒ đã đóng 27 ngày. Sĩ số tối đa 5, Đã đăng ký 0 lúc bắt đầu (còn chỗ) | Không |
| Nguồn đăng ký | Cột **Nguồn = "Nhập tay"** (frame `t000.00s`) | Cột **Nguồn = "Nhập tay"** (thêm qua **[Thêm học viên]** trên tab Học viên) | Không |
| Input / thao tác kích hoạt | Bước 4 của phiếu: bấm **Duyệt** trên dòng học viên (nhãn thực tế trên web là **[Phê duyệt]**) | Bấm **[Phê duyệt]** trên dòng học viên **Chờ duyệt** — 2 lần, trên 2 hồ sơ khác nhau | Không |

## Artifact real-data (Gate bằng chứng — loại claim: Absence "phải báo lỗi X nhưng không")

- `partner-evidence/QLDKDTTH_07.webm` — đã mở đọc frame full-res (crosswalk: tên file lệch mã TC, khóa chính là tên file cột *Ảnh/vieo 1*).
  - `t000.00s`: tab **Học viên**, học viên *Hoàng Minh Đức* — Nguồn *Nhập tay*, ngày đăng ký 24/07/2026 16:24:02, Trạng thái **Chờ duyệt**, hành động **Phê duyệt · Từ chối**. Stepper khóa học ở bước **3 Đã duyệt**.
  - `t003.03s` = **tiền đề**: tab **Thông tin** khóa học `KH-20260703-005 — test thêm mới khóa học`, **Mở đăng ký đến 03/07/2026** (ô đang được bôi xanh).
  - `t012.09s` = **khoảnh khắc lỗi**: thông báo xanh *"Đã phê duyệt đăng ký"* + cột Trạng thái đổi sang **Đã duyệt**, cột Hành động còn dấu **—**.
- `reverify-audit/QLDKDTTH_06/05-tien-de-cua-so-dang-ky-da-dong.png` — đã mở đọc: tiền đề của tôi (khóa học `KH-20260730-001`, Mở đăng ký 01/07 → 03/07/2026, stepper bước **3 Đã duyệt**). Bố cục trùng khít frame `t003.03s`.
- `reverify-audit/QLDKDTTH_06/01-seed-them-hoc-vien-cho-duyet.png` — đã mở đọc (bước seed): học viên vừa thêm ở **Chờ duyệt**, hành động **Phê duyệt · Từ chối** — đúng điểm khởi đầu của đối tác.
- `reverify-audit/QLDKDTTH_06/02-BUG-phe-duyet-thanh-cong-du-dong-dang-ky.png` — đã mở đọc: ngay sau khi bấm [Phê duyệt], cột Hành động của dòng đó thành **—** (không còn thao tác) ⇒ đã duyệt xong.
- `reverify-audit/QLDKDTTH_06/03-BUG-hoc-vien-da-duyet.png` — đã mở đọc: cuộn ngang sang cột **Trạng thái** → thẻ xanh **Đã duyệt**.
- `reverify-audit/QLDKDTTH_06/04-BUG-toast-da-phe-duyet-dang-ky.png` — đã mở đọc: **chụp được thông báo xanh *"Đã phê duyệt đăng ký"*** trong lần tái hiện thứ 2, cả 2 học viên đều **Đã duyệt**. Trùng khít frame `t012.09s` của đối tác.
- Bộ bắt thông báo (`tools/toast-capture.js`, tự kiểm `soObserverDangSong = 1`): mỗi lần bấm [Phê duyệt] = **1 request** `POST /api/v1/dang-ky-dao-taos/{id}/approve` ↔ **1 khung thông báo** *"Đã phê duyệt đăng ký"*. Không lặp, không gửi trùng.
- **Chứng minh "không có chốt kiểm nào chạy"** (đúng dạng claim *Absence*): `.ant-form-item-explain-error` **rỗng**; bảng điều khiển trình duyệt **0 dòng lỗi**; mạng chỉ có `POST …/approve` trả **201** (không có 4xx nào). Nghĩa là hệ thống không hề thử chặn — không phải chặn rồi báo sai chỗ.

## Phương pháp thứ hai (bắt buộc)

- **Đọc lại bản ghi sau thao tác** (không chỉ nhìn giao diện): `GET /api/v1/khoa-hocs/{id}/dang-ky-dao-taos` trả hồ sơ `913bca7d-…` với `trangThai = "DA_DUYET"` ⇒ trạng thái **đã ghi thật vào dữ liệu**, không phải lỗi hiển thị tạm.
- **Tái hiện lần 2 trên hồ sơ khác** (`6c7be07a-…`) cho kết quả y hệt: 201 + thông báo thành công ⇒ **2/2**, loại khả năng "một lần trùng hợp".
- **Loại giả thuyết "khóa học của tôi không thật sự đóng đăng ký"**: đọc lại bản ghi khóa học ngay trước lúc bấm — `moDangKyTuNgay = "2026-07-01"`, `moDangKyDenNgay = "2026-07-03"`, `trangThai = "DA_DUYET"`, hôm nay `2026-07-30`. Cả **hai** căn cứ để coi là "đang mở đăng ký" đều không thỏa: khóa chưa **Đã công khai/Đang diễn ra**, và mốc thời gian đã quá hạn.
- **Loại giả thuyết "lỗi nằm ở chỗ khác (lớp đầy / thiếu quyền)"**: sĩ số tối đa 5, đã đăng ký 0 lúc bắt đầu ⇒ không vướng sức chứa. Tài khoản `cbnv_tw` thao tác được cả thêm và duyệt ⇒ không vướng phân quyền. Chỉ còn đúng một chốt kiểm bị thiếu: **cửa sổ đăng ký**.
- **Đối chiếu đặc tả — trích nguyên văn** (`Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-03-dao-tao.md`):
  - `:371` — *"### FR-III-03: Quản lý đăng ký đào tạo (UC22)"* · `:373` — *"**UC Reference:** UC 22"*
  - `:385` — *"| PRE-02 | Khóa học tồn tại, đang mở đăng ký |"*
  - `:426` — *"| E1 | Khóa học đã đóng đăng ký | ERR-DKDT-01 | \"Khóa học đã đóng đăng ký\" | ERROR |"*
  - `:452` (FR-III-04, định nghĩa "đang nhận đăng ký") — *"Khóa học đang nhận đăng ký: trạng thái ∈ **{DA_CONG_KHAI, DANG_DIEN_RA}** VÀ (nếu có cửa sổ) `NOW ∈ [mo_dang_ky_tu, mo_dang_ky_den]`"*
  ⇒ Kỳ vọng của đối tác **trùng khớp đặc tả** (không phải kỳ vọng riêng) ⇒ đây là `Open`, không phải `BA confirm`.
- **Kiểm phần đã đúng để không quy kết quá phạm vi**: thao tác duyệt tự nó chạy đúng nghiệp vụ mô tả ở `:402` (*"Duyệt: cập nhật trạng thái = DA_DUYET, ghi nhật ký"*) — chuyển state đúng, thông báo rõ, 1 request ↔ 1 thông báo, phân quyền đúng vai trò. Lỗi khoanh đúng vào **thiếu chốt kiểm cửa sổ đăng ký / trạng thái khóa học trước khi cho duyệt**.

## Pass đối kháng (tự bác trước khi ghi sheet)

1. *"E1 có thể chỉ áp cho việc DN tự đăng ký, không áp cho khâu duyệt."* — Bác: E1 nằm trong **bảng Error Handling của chính FR-III-03**, cùng bảng với E2 *"Từ chối không có lý do"* (rõ ràng thuộc khâu duyệt/từ chối); Tác nhân của FR này là **CB NV / CB PD**; Inputs chỉ có `quyet_dinh = DUYET/TU_CHOI`. Việc DN tự đăng ký là FR-III-04 với **mã lỗi khác** (`ERR-DK-DT-01`). Vậy E1 thuộc khâu duyệt.
2. *"Chặn duyệt khi cửa sổ đã đóng là vô lý về nghiệp vụ — hồ sơ nộp lúc còn mở thì vẫn nên duyệt được."* — Đây là lập luận **nên sửa đặc tả**, không phải bằng chứng web đang đúng. Đặc tả hiện hành ghi rõ cả tiền đề (`:385`) và mã lỗi + câu thông báo (`:426`), và kỳ vọng đối tác trùng khớp. QA chấm theo đặc tả đang có; nếu BA thấy rule này cần nới thì đó là **thay đổi spec**, không phải bác phiếu. Đã ghi rõ ý này để dev/BA phản hồi có căn cứ.
3. *"Có thể web đã chặn nhưng thông báo lỗi bị mất."* — Bác bằng số đo: mạng chỉ có **201**, không có 4xx; `.ant-form-item-explain-error` rỗng; console 0 lỗi; và **trạng thái đã đổi thật trong dữ liệu** (`DA_DUYET` khi đọc lại). Chặn thì trạng thái phải giữ **CHO_DUYET**.
4. *"Môi trường khác (đối tác `htpldn-uat.ospgroup.vn` vs mình `nip.io`) nên không so được."* — Không cần suy luận: tôi **tự tái hiện được trên env được giao**, 2/2. Env khác chỉ là lý do phải tự dựng tiền đề, và tiền đề đã dựng trùng khít (cùng ngày cửa sổ 01/07→03/07, cùng vai trò, cùng state).

## Ngoài tiêu chí phiếu — có thấy gì bất thường không?

- **Đã soi 1 nghi vấn khác và LOẠI, không log:** ô **"Đã đăng ký"** ở tab Thông tin hiển thị **0** khi có 1 hồ sơ *Chờ duyệt* (khớp frame `t003.03s` của đối tác cũng là 0), và lên **2** sau khi duyệt ⇒ ô này đếm **chỉ hồ sơ đã duyệt**. Đặc tả không định nghĩa công thức của ô hiển thị này (chỉ `:509` EC-01 nói về **phép kiểm sức chứa** khi đăng ký: *"số đăng ký (trừ từ chối)"*). Chưa đủ căn cứ để nói ô hiển thị sai ⇒ **không log**.
- Ngoài ra không phát hiện thêm: bảng điều khiển trình duyệt sạch (0 lỗi), 4 thao tác đổi trạng thái đều **1 request ↔ 1 thông báo**, không lặp.
