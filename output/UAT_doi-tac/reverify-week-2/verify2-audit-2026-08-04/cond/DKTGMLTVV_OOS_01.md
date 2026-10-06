# DKTGMLTVV_OOS_01 — Bảng đối chiếu điều kiện (VÒNG SOÁT LẠI 2, 2026-08-04)

> Sheet `UAT_TGPL Doanh Nghiệp-tuần 2` row 138 · Verdict Verify 2: `Pass`
> **Bug gốc (2 ý):** trên biểu mẫu Thêm mới Tư vấn viên, khi Loại = Tư vấn viên thì ô *"Số thẻ hành nghề"*
> **(a)** không được báo hiệu là bắt buộc và **(b)** để trống vẫn **lưu thành công** — tạo ra hồ sơ `TVV-BTP-TW-0031`
> với Loại = Tư vấn viên và số thẻ rỗng (3 lệnh, 1 thông báo *"Tạo hồ sơ TVV thành công"*, không có thông báo cản nào).
> **Kết quả mong đợi:** hệ thống phải coi ô này là bắt buộc — cho người dùng biết đó là trường bắt buộc **và** từ chối
> lưu khi để trống. Chiếu `srs-fr-04-chuyen-gia-tvv.md:1507`: *"Số thẻ hành nghề | ô văn bản | **Bắt buộc nếu Loại =
> Tư vấn viên** (theo NĐ 77/2008 Đ.20)"*.
> Bug phụ thuộc **vai trò + giá trị ô Loại (điều kiện của ràng buộc) + thao tác lưu thật** ⇒ KHÔNG phải bug tĩnh ⇒
> bắt buộc điền bảng này.

**Môi trường soát lại 2:** `https://htpldn-uat.ospgroup.vn` · `HTPLDN · V1.0.5`.

| Điều kiện có thể đổi kết quả | Điều kiện bug gốc | Mình test (soát lại 2, 04/08/2026) | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | *"Người hỗ trợ pháp lý cấp Trung ương, đơn vị Cục Bổ trợ tư pháp - Bộ Tư pháp"*; lần đo trước dùng `nht_qa_tw` | **`nht_tc001_btp_tw`** — `GET /api/v1/auth/me` trả `vaiTro ["NHT"]`, `capDonVi "TW"`, `donViId 00000000-0000-4000-8000-000000000001` (= Cục Bổ trợ tư pháp - Bộ Tư pháp), thanh trên hiện `BTP · TW` + `NHT TC001 Test BTP TW · NHT`. `nht_qa_tw` **không tồn tại** trên môi trường này nên dùng NHT **cùng vai trò + cùng cấp + cùng đơn vị** đúng Rule 7 (đã thử `nht_btp_tw_audit_r30` trước: máy chủ trả `ERR-AUTH-LOGIN-04` — tài khoản bị vô hiệu hóa). **KHÔNG** dùng vai trò cán bộ để ra verdict | Không |
| Màn hình + lối vào | *"Mạng lưới Tư vấn viên → Tư vấn viên / Chuyên gia → Thêm mới"* | Đúng lối vào đó (`/chuyen-gia-tvv/tao-moi`, tiêu đề *"Thêm mới Tư vấn viên"*), mở bằng nút **[+ Thêm mới]** trên màn danh sách | Không |
| **Giá trị ô "Loại"** — chính là điều kiện của ràng buộc | Phiếu chỉ đo nhánh **Loại = Tư vấn viên (TVV)** | Đo **cả hai nhánh** (đúng yêu cầu của lô): **(A) Tư vấn viên (TVV)** — phải chặn; **(B) Chuyên gia (CG)** — đặc tả KHÔNG bắt buộc nên phải **không** chặn. Chạy lưu thật ở cả hai nhánh | Không |
| Dữ liệu tiền đề | Hồ sơ *"QA OOS01 Khong So The Hanh Nghe"*: TVV, sinh 01/01/1988, Nam, CCCD `038119880501`, email/điện thoại riêng, Cử nhân, Luat kinh te, 5 năm, lĩnh vực Thương mại, **có** tệp PDF thẻ hành nghề, **riêng ô "Số thẻ hành nghề" để trống** | **Tự dựng lại đúng bộ dữ liệu đó**, chỉ đổi CCCD/email/điện thoại để không trùng bản ghi cũ: `038119880503` · `qa.v2.tvv.thehanhnghe@htpldn.test` · `0912340503`; vẫn Cử nhân + Luat kinh te + 5 năm + Thương mại, **có tải tệp PDF thẻ hành nghề thật** (`DKTGMLTVV_OOS_01-v2-the-hanh-nghe.pdf`), **ô "Số thẻ hành nghề" để trống**. Nhánh Chuyên gia dựng bộ tương đương (`038119880502`) | Không |
| Cách quan sát | *"Quan sát ô có báo hiệu bắt buộc không"* + *"bấm [Lưu] xem có từ chối lưu không"*; bug gốc đo **3 lệnh / 1 thông báo thành công / hồ sơ được tạo** | Đo cả 3 mặt, bằng máy: **(1)** cờ bắt buộc trên nhãn (`ant-form-item-required`) + dấu sao; **(2)** số **lệnh gửi đi** và số **khung thông báo** (bắt bằng `tools/toast-capture.js`, không lọc trùng, đọc `innerText`, tự kiểm `soObserverDangSong = 1`); **(3)** đọc lại **dữ liệu máy chủ trả về** của mọi hồ sơ tạo trong phiên để xem `soTheHanhNghe` thực sự lưu gì | Không |

## Kết quả đo

**Ý (a) — nay có báo hiệu bắt buộc, và báo hiệu theo đúng điều kiện.**
Loại = **Tư vấn viên** → nhãn *"Số thẻ hành nghề"* mang cờ bắt buộc + dấu sao đỏ, gợi ý trong ô là *"Số thẻ hành nghề"*.
Đổi Loại sang **Chuyên gia** → cờ bắt buộc **tự bỏ**, gợi ý đổi thành *"Số thẻ (nếu có)"*. Tức ràng buộc gắn đúng theo
điều kiện `:1507`, không phải bật cứng.

**Ý (b) — nay từ chối lưu.** Nhánh TVV, để trống ô đó rồi bấm **[Lưu]**: **0 lệnh gửi đi** · **0 khung thông báo** ·
vẫn ở `/chuyen-gia-tvv/tao-moi` · **đúng 1 dòng báo lỗi** gắn **đúng ô** *"Số thẻ hành nghề"*:
*"**Số thẻ hành nghề là bắt buộc đối với Tư vấn viên**"* (884×22 điểm ảnh, hiển hình thật). Ảnh `DKTGMLTVV_OOS_01-v2-01`.

**Phép thử dương tính — chặn là riêng ô đó, không phải biểu mẫu hỏng.** Điền `THN-QA-V2-0503` vào chính ô vừa bị chặn
rồi bấm [Lưu]: **4 lệnh** — **1 thông báo** *"Tạo hồ sơ TVV thành công"*, tạo `TVV-BTP-TW-0080`, đọc lại máy chủ:
`loaiTvv "TVV"`, `soTheHanhNghe "THN-QA-V2-0503"`.

**Nhánh Chuyên gia — không chặn nhầm.** Cùng biểu mẫu, Loại = Chuyên gia, **để trống** số thẻ → lưu **thành công**:
2 lệnh — 1 thông báo *"Tạo hồ sơ TVV thành công"*, tạo `TVV-BTP-TW-0079` (`loaiTvv "CG"`, `soTheHanhNghe null`).

## Đã cố BÁC BỎ kết luận `Pass` bằng những cách nào

1. **Nghi "chỉ thêm dấu sao cho đẹp, bấm Lưu vẫn lọt"** → **BÁC**: bấm [Lưu] thật, **0 lệnh** gửi đi, không có hồ sơ nào
   được tạo trong lần bấm đó.
2. **Nghi "chặn cứng mọi trường hợp nên Chuyên gia cũng bị chặn oan"** → **BÁC**: nhánh Chuyên gia lưu được với ô trống.
3. **Nghi "biểu mẫu hỏng nên bấm gì cũng không lưu được"** → **BÁC**: điền đúng ô đó vào là lưu ngay, hồ sơ
   `TVV-BTP-TW-0080` có thật trên máy chủ.
4. **Nghi "báo lỗi hiện sai chỗ / sai nội dung"** (lô yêu cầu: chặn được nhưng báo sai chỗ vẫn tính chưa đạt) → **BÁC**:
   dòng lỗi gắn **đúng** ô "Số thẻ hành nghề" và nội dung nêu **đúng điều kiện** *"đối với Tư vấn viên"* của `:1507`.
5. **Nghi "sửa ô này thì làm hỏng ràng buộc ô kề bên"** (`:1508` — File thẻ hành nghề cũng bắt buộc nếu Loại = TVV; bug
   gốc ghi nhận chỗ này **đang chặn được**) → **BÁC**: thử lưu TVV có số thẻ nhưng **thiếu tệp thẻ hành nghề** → vẫn bị
   chặn: **0 lệnh**, 1 khung thông báo *"File thẻ hành nghề là bắt buộc đối với Tư vấn viên"*.
6. **Nghi "đọc nhầm giữa cờ giao diện và dữ liệu thật"** → **BÁC**: mọi hồ sơ tạo trong phiên đều đọc lại bằng dữ liệu
   máy chủ trả về, khớp với những gì màn hình thể hiện.

**Đã ghi nhận, KHÔNG dùng để hạ verdict phiếu này:** gọi thẳng máy chủ `POST /api/v1/tu-van-viens` với `loaiTvv "TVV"`
mà bỏ `soTheHanhNghe` thì máy chủ vẫn **nhận (201)** và tạo `TVV-BTP-TW-0081` (`soTheHanhNghe null`) ⇒ ràng buộc hiện
chỉ nằm ở phía trình duyệt. Phiếu này mô tả thao tác **trên biểu mẫu** (*"bấm [Lưu]"*, *"ô này để trống"*) và cả hai ý
của phiếu đã được đáp ứng qua biểu mẫu, nên verdict giữ `Pass`; phần thiếu kiểm tra ở máy chủ được **mở dòng mới**
theo thông lệ "lỗi ngoài phạm vi dòng TC có sẵn".

**Đã cân nhắc, KHÔNG tính là lỗi:** nhãn *"File thẻ hành nghề (PDF)"* và *"File đính kèm (Bằng cấp / Chứng chỉ)"* không
mang dấu sao dù vẫn chặn — khớp quy ước đã chốt ở CHANGELOG 2026-07-30 mục (4) (*"dấu sao chỉ dùng cho trường người
dùng tự nhập"*), và cả hai đều báo rõ lý do khi chặn.

**Kết luận: 0 GAP** — đúng vai trò Người hỗ trợ pháp lý cấp TW cùng đơn vị, đúng màn hình + lối vào, dựng lại đúng bộ
dữ liệu của phiếu, đo **cả hai nhánh Loại**, và chạy thao tác lưu **tới cùng** ở cả nhánh bị chặn lẫn nhánh phải lưu được.
