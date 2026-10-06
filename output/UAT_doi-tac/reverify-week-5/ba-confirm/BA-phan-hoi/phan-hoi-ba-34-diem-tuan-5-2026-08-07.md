# Phiếu chốt BA — 34 điểm treo tuần 5 (F5 · F6 · QLHSPLDN_15 · tổng hợp 06/08)

**Ngày:** 07/08/2026 · Gom từ 4 phiếu hỏi trong `Week5/Yêu cầu/`:
[`ba-confirm-lo-F5.md`](../Yêu%20cầu/ba-confirm-lo-F5.md) (7) ·
[`ba-confirmation-needed-F6-QLTLPLCVV-DKTGMLTVV-2026-08-07.md`](../Yêu%20cầu/ba-confirmation-needed-F6-QLTLPLCVV-DKTGMLTVV-2026-08-07.md) (5) ·
[`ba-confirmation-needed-QLHSPLDN_15-2026-08-07.md`](../Yêu%20cầu/ba-confirmation-needed-QLHSPLDN_15-2026-08-07.md) (1) ·
[`cau-hoi-BA-tong-hop-2026-08-06.md`](../Yêu%20cầu/cau-hoi-BA-tong-hop-2026-08-06.md) (21).

## Thay đổi kể từ lượt duyệt gần nhất

Lượt duyệt **đầu tiên** của phiếu — chưa có lượt trước để so. Bảng dưới ghi mức đọc cho từng phần.

| Phần | Nội dung | Kết luận có đổi không | Mức đọc |
|---|---|---|---|
| I — lô F5 (mục 1–7) | Đăng ký DN · mốc ký tự · phiên làm việc · lọc trạng thái TC TV | **ĐÃ KHÉP TRỌN.** Mục 2 duyệt 08/08 (5.000 ký tự) · mục 1, 5, 6 duyệt 09/08 · mục 3, 4, 7 tự khép | (a) đọc kỹ mục 1 · 2 |
| II — lô F6 (mục 8–12) | Loại hồ sơ TVV · điều hướng sau lưu · tìm kiếm tư liệu · thông báo kèm mã | Mới chốt — **mục 12 đảo kết luận của QA: Loại 4, không phải "expected sai"** | (a) đọc kỹ mục 12 |
| III — QLHSPLDN_15 (mục 13) | Xuất Excel khi bộ lọc rỗng | Mới chốt | (b) đọc phần phương án |
| IV — tổng hợp (mục 14–34) | 21 điểm rải nhiều nhóm | Mới chốt — **mục 27 đảo kết luận của QA** (đặc tả KHÔNG im lặng, có `DG-06`) rồi bị lớp soi độc lập hạ xuống *cần BA*; **mục 20 bị chính lượt kiểm định đảo lại** từ `SAP_HET` sang `SAP_HET_HAN`; **mục 19 xếp lại thành Loại 4** | (a) đọc kỹ mục 19 · 20 · 27 · 28 |

**Trạng thái chốt:** 16 mục **tự khép theo cây trọng tài** (đánh dấu `[tự khép]`) · **20 mục đã BA duyệt** (mục 2 — 08/08 · 19 mục — 09/08) · **0 mục cần BA quyết — PHIẾU ĐÃ KHÉP TRỌN 35/35**. **Lô F5 khép trọn 7/7 · Phần III khép trọn.** (đánh dấu `[CẦN BA CHỐT]`, đều đã kèm khuyến nghị). Không mục nào chặn bàn giao. **16 mục có việc cho Dev**, cao nhất mức Major đúng 1 mục.

## Bối cảnh chung

- **Bản bàn giao đối chiếu:** `docs/Reference/HTPLDN-PTYC-CT-v3.5.docx` — **bản sửa mới nhất, mốc tệp 08/08/2026 10:20**, `md5 adf292cce15a…`, 17,3 MB. Mốc đối chiếu duy nhất `[BA chốt 2026-08-06]`, kế thừa từ phiếu [`phan-hoi-ba-7-diem-can-chot-2026-08-06.md`](phan-hoi-ba-7-diem-can-chot-2026-08-06.md). **Chưa ghi nhận được ngày bàn giao và kênh gửi** — vẫn là điểm treo.
  - Bản này đã áp 7 quyết định của phiếu chốt trước (thêm ô *Cơ quan được đánh giá* + *Tài liệu đính kèm*, ghi lý do từ chối vào lịch sử, câu *"Đã lưu hợp đồng"*, bỏ chức năng in báo cáo, siết vai trò Quản trị hệ thống ở nhóm Báo cáo thống kê…). Đã đối chiếu: **bản gốc `.md` cũng đã được sửa đồng bộ** (`srs-fr-11-bao-cao.md:79` và `:1273`) ⇒ không sinh lệch tài liệu mới.
  - **Toàn bộ 13 đoạn phiếu này trích dẫn từ `.docx` đã được kiểm lại trên bản 08/08 — còn nguyên văn, không mục nào đổi kết luận.**
- **Môi trường đo:** env nội bộ `18.143.165.120.nip.io`, bản dựng V1.0.8 → V1.0.9. Đối tác đo trên `htpldn-uat.ospgroup.vn` bản V1.0–V1.0.3 — **hai bản dựng khác nhau thật**, mọi kết luận "web đúng" dưới đây chỉ có hiệu lực cho bản nội bộ và phải đo lại sau khi lên môi trường nghiệm thu.
- **Nguồn `.md`:** `_bmad-output/planning-artifacts/srs-v3.5/`. Mọi `file:dòng` trong phiếu đã tự mở đọc trong lượt này.

**Ghi chú phương pháp:**

- Câu `(1b)` của mọi mục đối tác có nêu kỳ vọng đều đã tra bản `.docx` bàn giao, không chỉ tra `.md` — đây là chỗ **lật một kết luận của QA** (mục 12).
- Ba cụm gom chung một phương án: **mục 21 + 30** (thanh lọc) · **mục 22 + 28** (mức cảnh báo ngoài vòng đời hồ sơ) · **mục 20 + 28** (mã mức "Sắp hết hạn").
- **Mục nào có phản hồi gửi đối tác, mục nào không** — quy tắc áp thống nhất, ghi ra để người duyệt kiểm được:

| Trường hợp | Có phản hồi? | Mục |
|---|:--:|---|
| Đối tác nêu, phần mềm đúng, đề nghị họ cập nhật Kết quả mong đợi | **Có** | 1 · 8 · 9 · 14 · 27 |
| Đối tác nêu, ta **chấp thuận** yêu cầu và sửa theo | **Có** | 2 |
| Đối tác báo Fail trên bản cũ, **bản mới đã hết lỗi** → đề nghị đo lại | **Có** | 10 · 11 · 13 · 28 |
| Đối tác nêu, kỳ vọng của họ **trùng khớp** thứ phần mềm đang làm | Không | 3 · 4 · 5 · 7 |
| Bug thật, Dev sửa **toàn bộ** — không có gì để giải trình | Không | 6 · 12 · 19 · 25 |
| Điểm **QA tự phát hiện**, đối tác không nêu — chưa có dòng phiếu để trả lời | Không | 15–18 · 20–24 · 26 · 29–34 |

> Nhóm cuối sẽ cần phản hồi **khi QA mở dòng mới** ở đợt kế tiếp, không phải ở phiếu này.
- Giá trị cột trạng thái ghi trong phiếu là **tên khái niệm**. Trước khi ghi lên sổ phải đọc tập giá trị đang dùng của tab `bug` và ghi đúng chuỗi đó, kể cả khi sai chính tả (sổ hiện dùng `Resoved`).

---

# PHẦN I — Lô F5 (7 mục)

## 1. Doanh nghiệp đặt mật khẩu ở biểu mẫu đăng ký, không phải ở màn kích hoạt  **✅ BA duyệt 09/08/2026**

**Vấn đề:** Doanh nghiệp tự mở tài khoản trên trang đăng nhập. Đối tác cho rằng doanh nghiệp phải gõ mật khẩu ở trang mở ra sau khi bấm liên kết trong thư kích hoạt; phần mềm lại bắt gõ mật khẩu ngay trong biểu mẫu đăng ký, còn trang kích hoạt chỉ báo thành công. Nếu chốt sai hướng thì toàn bộ luồng mở tài khoản của doanh nghiệp phải làm lại.

**(1)** `.md` **tự mâu thuẫn**: hướng "biểu mẫu đăng ký" có căn cứ ở **5 mục** của chính FR-VIII-22 (Inputs · Processing · Error Handling · Acceptance Criteria · bảng thành phần màn hình); hướng "màn kích hoạt" có **5 chỗ**, trong đó có **bảng chuyển trạng thái SM-TAIKHOAN**. Số chỗ ngang nhau nên không phân xử được bằng đếm — phép thử quyết định là *"dòng nào chết nếu chọn hướng kia"*, xem `#### Căn cứ chi tiết`.

**(1b)** **`.docx` mang cùng mâu thuẫn**, nhưng lệch **3–1** về phía biểu mẫu đăng ký:
- Theo biểu mẫu: mục 3.10 bước 1 — *"…đặt mật khẩu đủ mạnh và xác nhận lại…"*; mục 3.10 bước 3 — *"nhấn liên kết kích hoạt; hệ thống kiểm tra tính hợp lệ…; **hiển thị trang thông báo kích hoạt thành công**"* (không có bước đặt mật khẩu); mục 4.10.21.2.2 — bảng trường có đủ *Mật khẩu* + *Xác nhận mật khẩu*.
- Theo màn kích hoạt: mục 4.10.21.2.3 Trường hợp 1 — *"doanh nghiệp bấm đường dẫn kích hoạt **và đặt mật khẩu lần đầu**, tài khoản chuyển sang trạng thái hoạt động"*.

⇒ Không dùng `.docx` để phân xử được; nó chỉ cho biết **đối tác được giao một tài liệu cũng lệch**, nên kỳ vọng của họ không phải bịa.

**(2)** Đối tác đòi một bước không có ở cả hai bản tài liệu. Kết quả cuối của phiếu thì đã đạt: tài khoản về *Đang hoạt động*, đăng nhập được bằng mã số thuế.

**(3)** Không bắt buộc — mật khẩu vẫn do chính doanh nghiệp đặt, quyền sở hữu hộp thư vẫn được xác minh bằng liên kết kích hoạt. Đổi sang hướng kia chỉ dời chỗ nhập, không thêm giá trị nghiệp vụ nào.

#### Căn cứ chi tiết

**(1)** Hướng biểu mẫu đăng ký — 5 mục, 9 dòng:
- `srs-fr-10-quan-tri.md:1070-1071` — *"| 25 | mat_khau | text | Y | Ít nhất 8 ký tự… | 26 | mat_khau_xac_nhan | text | Y | Phải khớp mat_khau |"*
- `srs-fr-10-quan-tri.md:1081` — *"| 4 | Kiểm tra mật khẩu đủ độ mạnh + khớp xác nhận | BR-AUTH-01 |"* · `:1083` — *"| 6 | Mã hóa mật khẩu (hash 1 chiều) |"*
- `srs-fr-10-quan-tri.md:1098-1099` — `ERR-REG-04` *"Mật khẩu chưa đủ mạnh"* · `ERR-REG-05` *"Mật khẩu xác nhận không khớp"*
- `srs-fr-10-quan-tri.md:1112` — *"form đăng ký mở với 27 trường nhập gồm: 24 trường thông tin DN…, **2 trường mật khẩu**, và 1 ô cam kết"*
- `srs-fr-10-quan-tri.md:1934-1935` — SCR-VIII-08 hàng 26 *"Mật khẩu | password | Bắt buộc…"*, hàng 27 *"Xác nhận mật khẩu"*

Hướng màn kích hoạt — **5 chỗ** (lớp soi độc lập bổ sung 3 chỗ mà lượt soạn phiếu bỏ sót):
- `srs-fr-10-quan-tri.md:1109` — *"DN bấm link kích hoạt + đặt mật khẩu lần đầu (qua **FR-VIII-XX** Quên mật khẩu / Kích hoạt)…"* — số hiệu FR còn để trống, `CHANGELOG-v3-to-v3.5.md:2684` đã ghi nhận đây là chỗ chưa giải.
- `srs-fr-10-quan-tri.md:1116` — AC cùng nội dung.
- **`srs-fr-10-quan-tri.md:2299` — bảng chuyển trạng thái SM-TAIKHOAN**: *"| CHO_KICH_HOAT | HOAT_DONG | User kích hoạt qua email + **đặt mật khẩu lần đầu** | Token hợp lệ + **MK đủ độ mạnh** | Cho phép đăng nhập | **FR-VIII-15, FR-VIII-22, FR-VIII-26** |"* — có nêu đích danh FR-VIII-22.
- **`srs-v3.5.md:6390`** — bản sao của chính dòng đó ở Phụ lục C baseline, câu chữ y hệt.
- `srs-fr-10-quan-tri.md:1947` — ghi chú màn đã bỏ: *"…TK đi thẳng từ CHO_KICH_HOAT → HOAT_DONG khi user kích hoạt qua email + đặt mật khẩu lần đầu (FR-VIII-26)… FR-VIII-22 cho DN"*.

**Phép thử quyết định — dòng nào chết nếu chọn hướng kia.** Nếu chốt "đặt mật khẩu ở màn kích hoạt" thì **9 dòng đặc tả của FR-VIII-22 thành vô nghĩa**: hai ô nhập bắt buộc `:1070-1071`, hai bước xử lý `:1081`/`:1083`, hai mã lỗi `:1098-1099`, câu AC *"27 trường… 2 trường mật khẩu"* `:1112`, hai hàng màn hình `:1934-1935`. Ngược lại, nếu chốt "đặt ở biểu mẫu" thì **không dòng nào chết** — ba chỗ ở phía kia chỉ cần sửa lời cho đúng, vì bản thân bước kích hoạt vẫn tồn tại, chỉ là nó không đặt lại mật khẩu.

**Hai điểm yếu của phía màn kích hoạt:**
- Hàng SM-TAIKHOAN là **hàng dùng chung cho 3 FR**. Câu *"đặt mật khẩu lần đầu"* đúng cho FR-VIII-15 (quản trị tạo TK, `[STT80 UAT 2026-06-02]` đã bỏ hẳn ô mật khẩu khỏi form quản trị) và đúng cho FR-VIII-26 (TVV/NHT), nhưng bị gộp luôn FR-VIII-22 vào.
- FR mà `:1109` trỏ tới (`FR-VIII-26`) **không phủ trường hợp này** — đã đọc trọn `:1275-1362`, §Mô tả nêu đúng 3 trường hợp và §Acceptance nêu đúng 8 tiêu chí, không cái nào là DN vừa tự đăng ký.

Chứng minh ngược khẳng định *"FR-VIII-26 không phủ trường hợp doanh nghiệp tự đăng ký"*: đã đọc trọn FR-VIII-26 `:1275-1362`. §Mô tả `:1282-1285` liệt kê **3 trường hợp** — tài khoản TVV/CG do cán bộ duyệt, tài khoản NHT do cán bộ tạo, và Claim Flow (doanh nghiệp đã có hồ sơ, chưa có tài khoản). §Acceptance `:1353-1361` cũng đúng 3 nhóm đó. Không có trường hợp nào là doanh nghiệp tự đăng ký. Biến thể đã thử: `tự đăng ký`, `SELF_REGISTER`, `FR-VIII-22`, `kích hoạt`, `đặt mật khẩu lần đầu`.

**→ Kết luận: Loại 2 — chốt hướng **biểu mẫu đăng ký** `[BA duyệt 2026-08-09]`: doanh nghiệp đặt mật khẩu khi khai biểu mẫu; liên kết trong thư chỉ kích hoạt tài khoản, KHÔNG đặt lại mật khẩu. Phần mềm đang chạy **đúng** hướng này. Dev action: Không · Sửa đặc tả: Có (5 chỗ, gồm 2 bản sao máy trạng thái) · Doc action: Có → Sheet: KHÔNG đổi trạng thái.

> **Phản hồi gửi đối tác:**
> **[Lý do]** Theo thiết kế đã bàn giao, doanh nghiệp đặt mật khẩu ngay khi khai biểu mẫu đăng ký; liên kết trong thư điện tử chỉ dùng để xác nhận quyền sở hữu hộp thư và kích hoạt tài khoản, không yêu cầu đặt lại mật khẩu. Kết quả cuối cùng vẫn đúng: sau khi bấm liên kết, tài khoản chuyển sang trạng thái đang hoạt động và doanh nghiệp đăng nhập được bằng mã số thuế.
> **[Nhận định]** Đề nghị Quý đơn vị cập nhật bước 2 của kịch bản kiểm thử thành *"Doanh nghiệp bấm liên kết kích hoạt, hệ thống báo kích hoạt thành công"*. Nếu Quý đơn vị vẫn thấy cần để doanh nghiệp đặt mật khẩu tại màn kích hoạt, đề nghị đưa nội dung này vào danh sách yêu cầu cải tiến để xem xét.

### Phương án xử lý (cập nhật SRS)

1. `srs-fr-10-quan-tri.md:1109` — viết lại Hậu điều kiện: *"Doanh nghiệp bấm liên kết kích hoạt → hệ thống kiểm tra mã kích hoạt hợp lệ, chưa dùng → TAI_KHOAN chuyển HOAT_DONG (mật khẩu đã đặt từ bước đăng ký, KHÔNG đặt lại) → doanh nghiệp đăng nhập bằng mã số thuế + mật khẩu đã đặt."*
2. `srs-fr-10-quan-tri.md:1116` — sửa AC tương ứng: *"Given doanh nghiệp bấm liên kết kích hoạt When mã kích hoạt hợp lệ Then TAI_KHOAN chuyển HOAT_DONG, doanh nghiệp đăng nhập bằng MST + mật khẩu đã đặt khi đăng ký."*
3. `srs-fr-10-quan-tri.md` FR-VIII-22 §Processing — thêm bước **12**: *"Doanh nghiệp bấm liên kết kích hoạt: kiểm tra mã kích hoạt hợp lệ và chưa dùng → chuyển TAI_KHOAN sang HOAT_DONG → hủy mã kích hoạt → hiển thị trang báo kích hoạt thành công kèm đường dẫn về trang đăng nhập."* Kèm 2 mã lỗi cho mã kích hoạt sai và mã kích hoạt đã dùng (đặt theo tiền tố `ERR-REG-` đang dùng của FR này — `[BA chốt 2026-05-10]`).
4. `srs-fr-10-quan-tri.md:1282-1285` — FR-VIII-26 §Mô tả: thêm một câu khoanh phạm vi *"Không áp cho tài khoản doanh nghiệp tự đăng ký qua FR-VIII-22 — tài khoản đó đã có mật khẩu từ bước đăng ký, liên kết trong thư chỉ để kích hoạt."*
5. **Sửa 2 bản sao của bảng chuyển trạng thái SM-TAIKHOAN** — `srs-fr-10-quan-tri.md:2299` và `srs-v3.5.md:6390`. Hàng hiện tại gộp 3 FR vào một điều kiện; phải tách: với **FR-VIII-15 / FR-VIII-26** giữ nguyên *"kích hoạt qua email + đặt mật khẩu lần đầu · Token hợp lệ + MK đủ độ mạnh"*; với **FR-VIII-22** ghi riêng *"bấm liên kết kích hoạt · Token hợp lệ (mật khẩu đã đặt khi đăng ký)"*. Kèm sửa ghi chú `:1947`. *(Ba chỗ này lượt soạn phiếu bỏ sót, lớp soi độc lập bắt được.)*
6. **Doc action:** `.docx` mục 3.10 bước 2 và bước 3 ghi liên kết kích hoạt **"có hiệu lực 7 ngày"**, trong khi `.md:1088`, `:1938` và FR-VIII-26 `:1317` đều ghi **vĩnh viễn, dùng một lần** — và chính `.docx` mục 4.10.25.2.3 cũng ghi *"vĩnh viễn và chỉ dùng được một lần"*, tức **`.docx` tự mâu thuẫn với chính nó**. Nguồn của con số 7 ngày đã truy được: `srs-fr-10-quan-tri.md:2306` — *"| CHO_KICH_HOAT | VO_HIEU_HOA | **Auto: quá 7 ngày** | activation_token_expired |"* — đó là mốc **vô hiệu hoá tài khoản**, không phải hạn của liên kết. Bên soạn tài liệu sửa `.docx` theo `.md`, và chép bổ sung quy tắc 7 ngày vô hiệu hoá (hiện `.docx` **không có**). *(Phát sinh trong lượt này, không có trong phiếu hỏi gốc.)*

---

## 2. Mốc tối đa của ô "Lý do thay đổi trạng thái" — chốt 5.000 ký tự  **✅ BA duyệt 08/08/2026**

**Vấn đề:** Khi cán bộ tạm dừng hoặc vô hiệu hóa một tổ chức tư vấn, hệ thống bắt nhập lý do. Ô này hiện nhận tối đa 1.000 ký tự và **cắt phần thừa mà không báo gì** — cán bộ gõ dài rồi lưu, phần cuối biến mất mà không ai biết. Đối tác kỳ vọng 5.000 ký tự.

| Người dùng nhập | Hiện tại (V1.0.9) | Sau khi sửa |
|---|---|---|
| 9 ký tự | Chặn, báo lỗi | Chặn, báo lỗi *(không đổi)* |
| 999 ký tự | Nhận | Nhận |
| 1.001 ký tự | **Cắt còn 1.000, im lặng** | Nhận |
| Đúng 5.000 ký tự | **Cắt còn 1.000, im lặng** | Nhận, bộ đếm hiện `5000/5000` |
| Gõ tới 5.001 ký tự | **Cắt còn 1.000, im lặng** | **Không cắt** — giữ nguyên nội dung, báo vượt mốc, nút Lưu bị chặn |
| Dán một đoạn 8.000 ký tự | **Cắt còn 1.000, im lặng** | **Không cắt** — giữ nguyên 8.000 ký tự trong ô, báo vượt mốc, nút Lưu bị chặn |

**(1)** Đặc tả **thiếu mốc tối đa**: `srs-fr-04-chuyen-gia-tvv.md:984` — *"| 3 | ly_do | text (long) | Y | Min 10 ký tự |"*. Kiểu `text (long)` ở `srs-v3.5.md:805` cũng không kèm mốc mặc định. **Bản sao:** `srs-fr-04-chuyen-gia-tvv.md:892` (cùng ô, màn Tư vấn viên) cũng chỉ có Min 10.

**(1b)** `.docx` **cũng im lặng ở đúng ô này** (mục 4.4.12.2.2 và 4.4.14.2.2: *"Bắt buộc nhập tối thiểu 10 ký tự"*), **nhưng dùng 5.000 làm mốc mặc định cho ô văn bản nhiều dòng** ở 15 chỗ khác. Kỳ vọng của đối tác đến từ khuôn đó, không phải tự nghĩ ra.

**(2)** Đếm lại toàn bộ mốc ký tự trong `.md`: **5.000 là mốc được dùng nhiều nhất — 21 lần**, hơn 2.000 (17) và 1.000 (9). Chốt 5.000 vì vậy không phải ngoại lệ mà là **về đúng khuôn phổ biến nhất của hệ thống**, đồng thời khớp bản bàn giao nên `.docx` không phải sửa mốc.

**(3)** Việc **bỏ cắt âm thầm** thì bắt buộc bất kể con số: cắt lặng làm mất nội dung cán bộ đã gõ, mà lý do thay đổi trạng thái là dữ liệu lưu vết. Khuôn có sẵn: `.docx` *"có bộ đếm ký tự"*, `.md srs-fr-02-hoi-dap.md:1118` bộ đếm `{n}/1000`.

**→ Kết luận: Loại 2 `[BA duyệt 2026-08-09]` — chấp thuận mốc **5.000 ký tự** theo đúng kỳ vọng đối tác; phần mềm đang chặn ở 1.000 và cắt âm thầm nên phải sửa. Dev action: Có · Sửa đặc tả: Có · Doc action: Không (`.docx` đã dùng khuôn 5.000) → Sheet: KHÔNG đổi trạng thái — để QA/Dev chuyển sang *Giữ xử lý* khi bắt đầu làm.**

> **Phản hồi gửi đối tác:**
> **[Lý do]** Chấp thuận đề nghị của Quý đơn vị: giới hạn ô Lý do thay đổi trạng thái được chốt là **5.000 ký tự**, đúng bằng mốc Quý đơn vị nêu và thống nhất với các ô văn bản dài khác trong tài liệu bàn giao. Đặc tả đã được cập nhật theo hướng này.
> **[Nhận định]** Phần mềm sẽ được chỉnh cho đúng: nâng giới hạn lên 5.000 ký tự, hiển thị bộ đếm ký tự và báo khi vượt mốc, **không cắt bớt nội dung đã nhập** như hiện nay. Kết quả mong đợi của phiếu giữ nguyên, không cần sửa.

### Việc Dev cần làm

Mô tả theo **hành vi quan sát được**, áp cho ô *Lý do thay đổi trạng thái* ở **cả hai màn**: Chi tiết Tư vấn viên (`SCR-IV-03`) và Chi tiết Tổ chức tư vấn (`SCR-IV-NEW-03`).

| # | Việc | Nghiệm thu bằng |
|---|---|---|
| 1 | Nâng giới hạn ô lý do từ 1.000 lên **5.000 ký tự** | Nhập đúng 5.000 ký tự → lưu thành công, mở lại thấy đủ 5.000 |
| 2 | **Bỏ hẳn cơ chế cắt bớt nội dung.** Khi nội dung vượt mốc, ô phải **giữ nguyên** thứ người dùng đã nhập hoặc dán vào, không tự xóa phần thừa | Dán 8.000 ký tự → đếm lại trong ô vẫn đủ 8.000, không còn 5.000 |
| 3 | Hiện **bộ đếm ký tự** ngay dưới ô, dạng `{n}/5000`, cập nhật khi gõ; khi vượt mốc thì bộ đếm chuyển sang trạng thái cảnh báo | Gõ tới 5.001 → bộ đếm hiện `5001/5000` ở trạng thái cảnh báo |
| 4 | **Chặn nút Lưu** ở hai đầu: dưới 10 ký tự và trên 5.000 ký tự, kèm câu báo ngay tại ô | Ở 9 ký tự và ở 5.001 ký tự đều không lưu được, có câu báo |
| 5 | Câu báo dùng đúng chữ: dưới mốc → *"Lý do thay đổi là bắt buộc (≥ 10 ký tự)"*; vượt mốc → *"Lý do thay đổi tối đa 5.000 ký tự"* | So từng ký tự với hai câu trên |
| 6 | **Máy chủ kiểm cùng hai mốc**, không để giao diện là lớp duy nhất; khi từ chối thì trả đúng mã lỗi đã khai (`ERR-TT-03` cho Tư vấn viên, `ERR-TT-TC-03` cho Tổ chức tư vấn), không dùng mã hệ thống chung | Gọi thẳng máy chủ với 5.001 ký tự → bị từ chối, phản hồi mang đúng mã lỗi |

> Việc số 6 là hệ quả của quy ước chốt ở **mục 15** (*mã lỗi áp cho mọi lớp, câu chữ đo ở lớp giao diện*). Nếu BA không chốt mục 15 thì việc số 6 vẫn nên làm, vì đây là ràng buộc dữ liệu chứ không phải chuyện hiển thị.

### Phương án xử lý (cập nhật SRS)

**Phạm vi đã đếm — 41 chỗ khai trường lý do chưa có mốc tối đa, chia hai loại xử lý khác nhau:**

| Nhóm trường | Số chỗ chưa có mốc | Mốc đã có sẵn ở nơi khác | Xử lý |
|---|--:|---|---|
| `ly_do` (lý do hành động, lý do thay đổi trạng thái) + `ly_do_rut` | **15** | — chưa có khuôn nào — | **Gán mốc mới 5.000** |
| `ly_do_tu_choi` | 22 | **2.000** (5 chỗ, *Common Approval Field*) · 1.000 (1 chỗ, nhóm Hỏi đáp) | **Đồng bộ về 2.000** — KHÔNG gán 5.000 |
| `ly_do_huy` | 2 | 1.000 (3 chỗ) | Đồng bộ về 1.000 |
| `ly_do_uu_tien` | 2 | 500 (1 chỗ) | Đồng bộ về 500 |

**Vì sao không gán 5.000 cho cả 41 chỗ:** 26 trong số đó là **bản sao của trường đã có khuôn riêng** — đặc biệt `ly_do_tu_choi` đã được chuẩn hoá ở *Common Approval Field* là 2.000, và mốc đó vừa được BA chốt lại ngày 2026-07-24 (`PDHSVV_04`). Gán 5.000 đè lên sẽ vừa lật một quyết định mới hai tuần, vừa tạo hai mốc chọi nhau cho cùng một khái niệm.

**Các việc cụ thể:**

1. `srs-fr-04-chuyen-gia-tvv.md:984` và `:892` — *"Min 10 ký tự"* → *"Min 10 ký tự, max 5.000 ký tự"*.
2. `srs-fr-04-chuyen-gia-tvv.md:1016` `ERR-TT-TC-03` và `:922` `ERR-TT-03` — đổi câu thành *"Lý do thay đổi phải từ 10 đến 5.000 ký tự"*.
3. `srs-fr-04-chuyen-gia-tvv.md:1554` và `:1721` — mô tả nút *Cập nhật trạng thái*: *"lý do (từ 10 đến 5.000 ký tự, có bộ đếm `{n}/5000`)"*.
4. **13 chỗ `ly_do` / `ly_do_rut` còn lại** — bổ sung *"max 5.000 ký tự"*. Danh sách: `srs-fr-03-dao-tao.md:1403` · `srs-fr-04-chuyen-gia-tvv.md:511` · `:609` · `:913` · `:1181` · `:2155` · `srs-fr-05-vu-viec.md:523` · `:988` · `:2142` · `srs-fr-06-chi-tra.md:256` · `srs-v3.5.md:1667` · `:2237` · `:2765`. Mở từng chỗ đọc trước khi sửa — một số là bảng thực thể, một số là bảng Inputs, câu chữ khác nhau.
5. **26 chỗ nhóm đã có khuôn** — đồng bộ về mốc sẵn có (2.000 / 1.000 / 500) theo bảng trên. Việc này **tách khỏi quyết định 5.000**, chỉ là dọn bản sao thiếu mốc.
6. **Điểm cần BA xác nhận kèm theo:** `ly_do_tu_choi` hiện có **hai** mốc — 2.000 ở 5 chỗ và **1.000 ở `srs-fr-02-hoi-dap.md:677`** (nhóm Hỏi đáp). Giữ 1.000 làm ngoại lệ có lý do, hay đồng bộ luôn về 2.000?
7. **Doc action: không có.** `.docx` đã dùng khuôn 5.000 cho ô văn bản nhiều dòng nên không phải sửa mốc; chỉ cần bổ sung dòng bộ đếm nếu bản kế tiếp muốn ghi rõ.

---

## 3. Hộp thoại cảnh báo phiên hiện ở phút thứ 25, không phải phút 30 `[tự khép]`

**Vấn đề:** Khi người dùng để máy không thao tác, hệ thống hiện hộp thoại báo phiên sắp hết hạn rồi mới tự đăng xuất. Hai chỗ trong đặc tả ghi hai mốc khác nhau cho thời điểm hiện hộp thoại.

**(1)** `srs-fr-10-quan-tri.md:1891` (SCR-VIII-07 hàng 12) ghi điều kiện hiển thị *"30 phut idle"*; `srs-fr-10-quan-tri.md:1959` (SCR-VIII-09) ghi *"25 phut idle → Modal canh bao → 30 phut → Auto invalidate"*. Hai số không thể cùng đúng: ở phút 30 phiên đã bị hủy nên không thể hiện hộp thoại báo *"sắp hết hạn trong 5 phút"*.

**(1b)** Không phải tranh chấp tài liệu — đối tác chấm đúng theo hành vi 25 phút, trùng `:1959`.

**(2)** Web đo được đúng 25,0 phút — khớp `:1959` và khớp kỳ vọng đối tác.

**(3)** Không có gì phải sửa ở phần mềm. `CHANGELOG-v3-to-v3.5.md:1212` và `:1240` cho thấy bảng SCR-VIII-07 mới chỉ được soát lại ở hàng 2 và hàng 11, chưa soát hàng 12 ⇒ `:1891` là chỗ sót.

**→ Kết luận: Loại 2 — đặc tả tự mâu thuẫn, phần mềm đã đúng. Dev action: Không · Sửa đặc tả: Có → Sheet: KHÔNG đổi trạng thái.**

### Phương án xử lý (cập nhật SRS)

`srs-fr-10-quan-tri.md:1891` — cột Điều kiện hiển thị: *"30 phut idle"* → *"25 phút không thao tác"*.

---

## 4. Câu chữ và nhãn nút của hộp thoại cảnh báo phiên `[tự khép]`

**Vấn đề:** Hộp thoại báo phiên sắp hết hạn đang hiện đầy đủ tiêu đề, nội dung, đồng hồ đếm ngược và hai nút — nhưng đặc tả chỉ ghi một chuỗi rút gọn không dấu, nên vòng kiểm thử sau lại có thể chấm sai.

**(1)** `srs-fr-10-quan-tri.md:1891` ghi đúng một chuỗi: *"Phien sap het han trong 5 phut. [Gia han] [Dang xuat]"*.

**(1b)** Không phải tranh chấp tài liệu — web trùng **từng ký tự** với kỳ vọng đối tác.

**(2)** Web hiện: tiêu đề *"Phiên làm việc sắp hết hạn"*; nội dung *"Phiên làm việc sắp hết hạn trong 5 phút do không có thao tác. Vui lòng gia hạn để tiếp tục làm việc."*; dòng đếm ngược *"Phiên sẽ tự đăng xuất sau m:ss"*; hai nút `[Đăng xuất]` `[Gia hạn phiên]`.

**(3)** Chứng minh ngược khẳng định *"đặc tả chưa có đồng hồ đếm ngược"*: grep `đếm ngược` / `countdown` / `dem nguoc` toàn thư mục `srs-v3.5/` ra **đúng 1 kết quả**, tại `srs-fr-10-quan-tri.md:1887` — thuộc nút *Gửi lại* mã OTP, không phải hộp thoại phiên. ⇒ đúng là chưa có.

**→ Kết luận: Loại 2 — đặc tả ghi thiếu, phần mềm đã đúng. Dev action: Không · Sửa đặc tả: Có → Sheet: KHÔNG đổi trạng thái.**

### Phương án xử lý (cập nhật SRS)

`srs-fr-10-quan-tri.md:1891` — chép nguyên câu chữ và hai nhãn nút đang chạy vào cột Dữ liệu / Nội dung, kèm dòng đồng hồ đếm ngược *"Phiên sẽ tự đăng xuất sau m:ss"*. Giữ đúng thứ tự nút đang chạy: `[Đăng xuất]` (phụ) trước, `[Gia hạn phiên]` (chính) sau.

---

## 5. Hành vi của nút "Gia hạn phiên" — không giới hạn số lần  **✅ BA duyệt 09/08/2026**

**Vấn đề:** Hộp thoại cảnh báo có nút *Gia hạn phiên*, nhưng đặc tả để trống ô mô tả nút này làm gì. Kèm theo là câu hỏi chưa ai trả lời: một người có được bấm gia hạn liên tục không giới hạn để giữ phiên mở cả ngày không.

**(1)** `srs-fr-10-quan-tri.md:1891` khai nút `[Gia han]` nhưng ô Hành vi của chính hàng đó **để trống** (`—`). Hành vi suy ra được từ `BR-AUTH-06` (`srs-v3.5.md:5527`, `srs-fr-10-quan-tri.md:2369` — *"Session CMS: 30 phút idle timeout"*) nhưng chưa được viết thành câu.

**(1b)** `.docx` cũng không mô tả hành vi nút này.

**(2)** Web đo được: bấm → hộp thoại đóng dưới 0,4 giây, mốc không-thao-tác đặt lại về thời điểm bấm, vượt mốc tự đăng xuất cũ mà phiên vẫn còn hiệu lực. Đúng nghĩa "gia hạn".

**(3)** Phần hành vi: bắt buộc phải viết ra, nếu không thì không có thước đo. Phần giới hạn số lần: đặc tả im lặng hoàn toàn, không có khuôn nào để suy ra — **BA chốt 09/08/2026: không đặt giới hạn**. Mỗi lần gia hạn là một thao tác thật của người dùng, nên nó đúng nghĩa "có thao tác"; đặt trần sẽ đá người đang làm việc ra khỏi hệ thống giữa chừng.

**→ Kết luận: Loại 2 `[BA duyệt 2026-08-09]` — đặc tả để trống ô hành vi; phần mềm đã đúng và **không cần sửa** vì bản đang chạy vốn không giới hạn số lần gia hạn. Dev action: Không · Sửa đặc tả: Có → Sheet: KHÔNG đổi trạng thái.**

### Phương án xử lý (cập nhật SRS)

1. `srs-fr-10-quan-tri.md:1891` — điền ô Hành vi: *"Bấm → đóng hộp thoại, đặt lại mốc không-thao-tác về thời điểm bấm, phiên tiếp tục hiệu lực thêm trọn 30 phút. **Không giới hạn số lần gia hạn liên tiếp.**"*
2. `srs-v3.5.md:5527` và `srs-fr-10-quan-tri.md:2369` (`BR-AUTH-06`) — bổ sung một câu để lượt kiểm thử sau không phải đi tìm: *"Phiên chỉ kết thúc bởi một trong hai: đủ 30 phút không thao tác, hoặc người dùng chủ động đăng xuất. **Không có trần thời lượng tuyệt đối cho một phiên và không giới hạn số lần gia hạn** `[BA chốt 2026-08-09]`."*

> **Hệ quả đã cân nhắc:** không có trần tuyệt đối nghĩa là một người thao tác liên tục có thể giữ phiên mở suốt ngày làm việc. Đây là hành vi **đúng ý** với phần mềm nội bộ dùng qua mạng kín — cán bộ làm việc cả ngày trên cùng một phiên. Nếu sau này yêu cầu an toàn thông tin đòi trần tuyệt đối thì đó là **một quy tắc mới ở `BR-AUTH-06`**, không phải sửa nút này.

---

## 6. Câu thông báo hết phiên đang tồn tại 4 dạng khác nhau  **✅ BA duyệt 09/08/2026**

**Vấn đề:** Khi phiên hết hạn, người dùng bị đưa về trang đăng nhập kèm một câu thông báo. Bốn chỗ trong đặc tả viết bốn câu khác nhau, nên mỗi màn có thể hiện một kiểu và mỗi vòng kiểm thử lại chấm theo một câu.

**(1)** Bốn dạng, đã mở đọc từng dòng:
- `srs-fr-10-quan-tri.md:964` — `ERR-DN-07`: *"Redirect về trang đăng nhập + 'Phiên làm việc hết hạn'"*
- `srs-fr-10-quan-tri.md:1011` — Outputs FR-VIII-21: *"'Đăng xuất thành công' / 'Phiên hết hạn'"*
- `srs-fr-05-vu-viec.md:1593` — *"'Phiên làm việc đã hết hạn. Vui lòng đăng nhập lại.' + nút [Đăng nhập]"*
- `srs-fr-02-hoi-dap.md:1135` — *"'Phiên đăng nhập đã hết hạn'"* + phần mô tả giữ bản nháp + 2 nút

**(1b)** Không phải tranh chấp tài liệu.

**(2)** Web và phiếu đối tác đều dùng cụm *"do không có thao tác"* — grep toàn thư mục `srs-v3.5/`: **0 kết quả** ⇒ cụm này chưa có trong bất kỳ dạng nào.

**(3)** Cần chốt một câu chuẩn: đây là câu người dùng cuối gặp ở mọi màn, bốn dạng khác nhau là lỗi nhất quán thật.

**→ Kết luận: Loại 2 — đặc tả có 4 dạng lệch nhau; chốt một câu chuẩn dùng chung `[BA duyệt 2026-08-09]`. Dev action: Có (thống nhất câu hiển thị ở mọi màn) · Sửa đặc tả: Có → Sheet: KHÔNG đổi trạng thái.**

**Việc Dev:** Thống nhất một câu thông báo hết phiên hiển thị ở **mọi** màn theo câu chuẩn đã chốt. *Nghiệm thu:* để phiên hết ở vài màn khác nhau → đều hiện đúng một câu.

> **Chốt chặn khi thi hành:** câu này hiện ra ở **mọi** màn, nên trước khi Dev đổi, QA phải rà xem có phiếu kiểm thử nào đang lấy câu cũ làm Kết quả mong đợi không. Đổi trước rồi mới rà là đẩy đối tác vào một lô Fail mới.

### Phương án xử lý (cập nhật SRS)

1. **Câu chuẩn khuyến nghị**, ghi một lần vào quy ước chung `srs-v3.5.md` §Thông báo hệ thống: tiêu đề *"Phiên làm việc đã hết hạn"*, nội dung *"Phiên làm việc đã hết hạn do không có thao tác. Vui lòng đăng nhập lại để tiếp tục."*, một nút *[Đăng nhập lại]*.
2. Bốn chỗ trên trỏ về câu chuẩn thay vì viết lại. `srs-fr-02-hoi-dap.md:1135` **giữ phần bổ sung về bản nháp** (khôi phục nội dung đang soạn) như một ngoại lệ có lý do nghiệp vụ, nhưng dùng đúng tiêu đề chuẩn.
3. `srs-fr-10-quan-tri.md:1011` giữ nguyên hai giá trị vì đó là **hai nhánh khác nhau**, không phải hai cách viết một câu — xem xác nhận dưới.

> **Xác nhận cách chấm `QLDX_06`:** người dùng chủ động bấm *Đăng xuất* ở phút thứ 25 thì phiên **chưa** hết hạn, nên câu đúng là *"Đăng xuất thành công"* theo `:1011`. Câu hết phiên chỉ dành cho nhánh để tới phút 30. Cách QA đã chấm là đúng. Nếu nghiệp vụ muốn hiện câu hết phiên ở **cả hai** nhánh thì phải sửa `:1011` trước — nhưng khuyến nghị **không** đổi, vì hai nhánh mang hai nghĩa khác nhau với người dùng.

---

## 7. Danh sách trạng thái ở màn Tổ chức tư vấn phải lọc theo trạng thái hiện tại `[tự khép]`

**Vấn đề:** Khi cán bộ đổi trạng thái một tổ chức tư vấn, hộp thoại chỉ nên đưa ra những trạng thái chuyển được từ trạng thái hiện tại. Màn Tư vấn viên đã viết rõ quy tắc này, màn Tổ chức tư vấn thì chỉ liệt kê phẳng cả ba lựa chọn.

**(1)** `srs-fr-04-chuyen-gia-tvv.md:1554` (SCR-IV-03, màn Tư vấn viên) ghi rõ *"Tùy chọn trạng thái mới hiển thị theo trạng thái hiện tại"* kèm 4 nhánh (a)–(d). `srs-fr-04-chuyen-gia-tvv.md:1721` (SCR-IV-NEW-03, màn Tổ chức tư vấn) chỉ ghi *"chọn trạng thái mới (Tạm dừng / Khôi phục / Vô hiệu hóa)"*; chốt kiểm tra chuyển trạng thái nằm ở phía xử lý `:991`.

**(1b)** Không phải tranh chấp tài liệu.

**(2)** Web đang lọc đúng theo SM-TCTV (`:2392-2395`) — tức làm **nhiều hơn** `:1721` yêu cầu và khớp kỳ vọng đối tác.

**(3)** Không sửa phần mềm. Đặc tả bị thiếu một câu; để nguyên thì vòng sau lại tranh chấp đúng chỗ này.

**→ Kết luận: Loại 2 — đặc tả thiếu, phần mềm đã đúng. Dev action: Không · Sửa đặc tả: Có → Sheet: KHÔNG đổi trạng thái.**

### Phương án xử lý (cập nhật SRS)

`srs-fr-04-chuyen-gia-tvv.md:1721` — bổ sung câu lọc theo SM-TCTV, viết theo đúng khuôn `:1554`: *"Tùy chọn trạng thái mới hiển thị theo trạng thái hiện tại: (a) Đang hoạt động → 'Tạm dừng' + 'Vô hiệu hóa'; (b) Tạm dừng → 'Kích hoạt lại (Đang hoạt động)' + 'Vô hiệu hóa'; (c) Vô hiệu hóa → 'Khôi phục (Đang hoạt động)'."*

---

# PHẦN II — Lô F6 (5 mục)

> **Bốn** mục 8 · 9 · 12 · 12b thuộc **cùng một dòng phiếu** `DKTGMLTVV_13` (dòng 35). Đây là **case lai**: hai vế đối tác ghi sai kỳ vọng, một vế là lỗi thật do đặc tả gốc bị sót. Trạng thái sổ của dòng 35 theo **phần Dev** — xem mục 12.
>
> **Cách gửi cho dòng 35 — dòng này có 4 vế:** ghép phản hồi của **mục 8**, **mục 9** và **mục 12b** thành một đoạn, rồi thêm một câu cho vế còn lại: *"Riêng nội dung thông báo sau khi đăng ký thành công, phần mềm sẽ được bổ sung mã hồ sơ vừa tạo theo đúng tài liệu bàn giao."* Mục 12 không có phản hồi riêng vì Dev sửa toàn bộ.

**Bóc ý con Kết quả mong đợi của `DKTGMLTVV_13`:**

| Ý con trong Kết quả mong đợi | Bản gốc có không | Phiếu xử ở đâu |
|---|---|---|
| Hồ sơ mang loại **"Người hỗ trợ"** | Không — chỉ `TVV` / `CG` | Mục 8 — đề nghị sửa Kết quả mong đợi |
| Trạng thái **"Mới đăng ký"** | Có | Không tranh chấp — đã đo ĐẠT |
| Thông báo **"Đăng ký thành công, chờ thẩm định"** | Có, nguyên văn | Không tranh chấp — đã đo ĐẠT |
| Thông báo kèm **mã hồ sơ đã tạo** | `.md` không có · **`.docx` có** | Mục 12 — Loại 4 hướng B, Dev sửa |
| Chuyển sang **trang theo dõi tiến độ** | Không — quy ước §H7 buộc về Danh sách | Mục 9 — đề nghị sửa Kết quả mong đợi |
| Nút tên **"Gửi đăng ký"** thay vì "Lưu" | Không — §H4 buộc "Lưu" | **Mục 12b** — khuyến nghị giữ nguyên, có phản hồi |

## 8. Hồ sơ tạo ở màn Thêm mới Tư vấn viên không mang loại "Người hỗ trợ" `[tự khép]`

**Vấn đề:** Người hỗ trợ pháp lý đăng ký hộ một ứng viên tư vấn viên. Đối tác kỳ vọng hồ sơ tạo ra mang loại *"Người hỗ trợ"*. Thực tế ô Loại chỉ có hai lựa chọn *Tư vấn viên* và *Chuyên gia* — vì "Người hỗ trợ" là **vai trò của người đi đăng ký hộ**, không phải loại của hồ sơ được đăng ký.

**(1)** Phần mềm **đúng** `.md`: `srs-fr-04-chuyen-gia-tvv.md:296` — *"| 0 | loai_tvv | text | Y | CHECK IN ('TVV','CG') | 'TVV' | NHT chọn (radio) |"*; `:1490` — *"| 2.2 | nhóm 1 | Loại * | dropdown 2 lựa chọn | 'Tư vấn viên' / 'Chuyên gia'…"*. Người hỗ trợ là thực thể riêng `NGUOI_HO_TRO`, tạo ở màn khác `:1799`, trạng thái khởi tạo khác `:2073`. Đây là thay đổi **có chủ đích**: `:18` ghi lịch sử 2026-05-03 *"bỏ NHT khỏi loai_tvv enum + tạo entity NGUOI_HO_TRO"*.

**(1b)** `.docx` **cùng hướng**: mục 4.4.1.2.2, trường *Loại* — *"Bắt buộc chọn: 'Tư vấn viên' hoặc 'Chuyên gia'. Đây là cá nhân hành nghề tư vấn bên ngoài; cán bộ hỗ trợ pháp lý của cơ quan nhà nước được quản lý ở hồ sơ Người hỗ trợ pháp lý riêng (mục 4.4.17)."*

**(2)** Đối tác gán vai trò của người thao tác thành giá trị của trường Loại — hai khái niệm đã tách bạch ở cả hai bản tài liệu, **và tách sẵn từ Danh sách UC + Transaction** (baseline chính thức, cao hơn cả `.md` lẫn `.docx` khi xét phạm vi và tách vai):

- `docs/Reference/Danh-sach-transaction_v1.1_2026-03-27.md:763-766` — **UC 41 "Quản lý đăng ký tham gia mạng lưới tư vấn viên"**, đúng chức năng của màn đang xét: *"**Tác nhân:** Người hỗ trợ"* · *"**Mô tả:** Quản lý các hồ sơ đăng ký tham gia mạng lưới **tư vấn viên** từ các **ứng viên**."* ⇒ ngay trong một dòng, *Người hỗ trợ* nằm ở ô **Tác nhân**, còn thứ được tạo ra là hồ sơ **tư vấn viên**.
- Quét toàn bộ Danh sách UC + Transaction: chuỗi *"Người hỗ trợ"* xuất hiện **15 lần và cả 15 đều ở ô Tác nhân** (UC 23 · 32 · 41 · 42 · 49 · 60 · 65 · 118 · 119 · 120 · 123 · 148 · 150 · 161 và UC 21). **Không có UC nào** coi *Người hỗ trợ* là một loại hồ sơ hay một giá trị của trường dữ liệu.
- Cả cụm UC về hồ sơ tư vấn viên — UC 39 *Quản lý tư vấn viên* · UC 43 *Quản lý hồ sơ tư vấn viên* · UC 44 *Thẩm định hồ sơ tư vấn viên* · UC 45 *Phê duyệt hồ sơ tư vấn viên* — đều mang tên **tư vấn viên**, không mục nào là *người hỗ trợ*.

#### Căn cứ chi tiết

**(2) — hồ sơ Người hỗ trợ được quản lý ở đâu trong phần mềm.** Có hẳn **một nhánh riêng**, không dùng chung màn nào với tư vấn viên:

| Thành phần | Vị trí |
|---|---|
| Nhánh menu | *Mạng lưới Tư vấn viên → **Người hỗ trợ pháp lý*** — `srs-fr-04-chuyen-gia-tvv.md:1336-1339` |
| 3 chức năng | `FR-IV-NHT-01` Quản lý (`:1206`) · `FR-IV-NHT-02` Tìm kiếm (`:1271`) · `FR-IV-NHT-03` Xem hồ sơ (`:1300`) |
| 3 màn hình | `SCR-IV-NHT-01` Danh sách (`:1751`, đường dẫn `/chuyen-gia-tvv/nguoi-ho-tro`) · `SCR-IV-NHT-02` Thêm/Sửa (`:1795`) · `SCR-IV-NHT-03` Chi tiết 3 thẻ — Thông tin · Bồi dưỡng · Vụ việc đã hỗ trợ (`:1827`, `:1303`) |
| Thực thể | `NGUOI_HO_TRO` riêng, 1:1 với tài khoản, kèm bảng nối lĩnh vực chuyên môn — `srs-fr-04-chuyen-gia-tvv.md:2056` · baseline `srs-v3.5.md:1895` và `:1938` |
| Ai lập hồ sơ | **Quản trị hệ thống** (toàn hệ thống) hoặc **Cán bộ Nghiệp vụ** (quản lý NHT cùng đơn vị) — `:1215`. **Không** phải người hỗ trợ tự đăng ký |
| Lập xong thì | Đồng thời tạo tài khoản ở trạng thái chờ kích hoạt, gán vai trò, gửi thư kích hoạt — `:1236-1240` |
| Căn cứ | **NĐ 55/2019/NĐ-CP Điều 7** (`:1209`, `srs-v3.5.md:1897`) — khác căn cứ của tư vấn viên là **NĐ 77/2008** (`:137`) |

⇒ Hai nhóm đối tượng khác nhau về **pháp lý**, không chỉ khác về nhãn: người hỗ trợ là **cán bộ ở Sở Tư pháp / Bộ ngành / UBND / tổ chức đại diện doanh nghiệp**; tư vấn viên là **cá nhân hành nghề tư vấn bên ngoài**. Gộp vào một trường sẽ phá vòng đời thẩm định 4 nhóm tiêu chí vốn chỉ áp cho tư vấn viên.

> **Ghi nhận kèm theo, không ảnh hưởng kết luận:** nhánh quản lý này mang cờ `[GAP-IV-11]` (`:106`) — tức là **bổ sung ngoài Danh sách UC + Transaction**, có chủ đích, `[BA chốt 2026-05-03]`, căn cứ NĐ 55/2019 Đ.7. Nêu ra để lượt đối chiếu độ phủ UC sau không hiểu nhầm là thiếu sót.

**(3)** Không bắt buộc và cũng không đúng nghiệp vụ: người hỗ trợ là cán bộ nhà nước, tư vấn viên là cá nhân hành nghề bên ngoài; gộp hai loại vào một hồ sơ sẽ phá vòng đời thẩm định của tư vấn viên.

**→ Kết luận: Loại 3 — phần mềm đúng cả hai bản tài liệu, kỳ vọng của đối tác đặt sai khái niệm. Dev action: Không · Sửa đặc tả: Không · Sheet: theo mục 12 (case lai, cùng dòng 35).**

> **Phản hồi gửi đối tác:**
> **[Lý do]** Theo Danh sách UC + Transaction, mục **UC 41 "Quản lý đăng ký tham gia mạng lưới tư vấn viên"** — đúng chức năng của màn hình này — *Người hỗ trợ* nằm ở ô **Tác nhân**, tức người thực hiện thao tác; còn thứ được tạo ra là *"hồ sơ đăng ký tham gia mạng lưới **tư vấn viên** từ các **ứng viên**"*.
> **[Hồ sơ Người hỗ trợ quản lý ở đâu]** Ở nhánh riêng: *Mạng lưới Tư vấn viên → **Người hỗ trợ pháp lý*** (Danh sách · Thêm mới / Chỉnh sửa · Chi tiết), do Quản trị hệ thống hoặc Cán bộ Nghiệp vụ trong đơn vị lập.
> **[Nhận định]** Đề nghị Quý đơn vị cập nhật kết quả mong đợi thành *"…với loại Tư vấn viên hoặc Chuyên gia theo lựa chọn khi nhập"*. Nếu nghiệp vụ thực sự cần thêm loại *Người hỗ trợ*, đề nghị đưa vào danh sách yêu cầu cải tiến.

---

## 9. Sau khi lưu hồ sơ, hệ thống quay về trang danh sách `[tự khép]`

**Vấn đề:** Đối tác kỳ vọng sau khi lưu hồ sơ thành công thì hệ thống chuyển sang một "trang theo dõi tiến độ". Phần mềm quay về trang danh sách tư vấn viên.

**(1)** Phần mềm **đúng** quy ước mức **BẮT BUỘC**: `srs-v3.5.md:6759` §H7 — *"Sau khi thực hiện thành công thao tác Thêm mới một bản ghi, hệ thống chuyển hướng về trang Danh sách (SCR-XX-01) kèm toast thông báo. Trừ trường hợp… **phải có ghi chú riêng tại FR cụ thể**."* Đã đọc trọn FR-IV-03 (`:280-363`) và trọn SCR-IV-02 (`:1470-1529`): **không có ghi chú ngoại lệ nào**.

**(1b)** `.docx` **không mô tả** bước điều hướng sau khi lưu ở màn này ⇒ không có căn cứ tài liệu cho kỳ vọng của đối tác.

**(2)** Cụm *"trang theo dõi tiến độ"* xuất hiện **đúng 1 lần** trong cả thư mục `srs-v3.5/`, tại `srs-fr-15-ct-htpldn.md:621`, thuộc nghiệp vụ khác hẳn (cán bộ TW theo dõi tiến độ nộp báo cáo của các đơn vị). Màn đó **không tồn tại** cho luồng đăng ký tư vấn viên.

**(3)** Không bắt buộc, vì **trang danh sách chính là nơi theo dõi tiến độ** — đã tra và xác nhận có đủ ba đường:
- `srs-fr-04-chuyen-gia-tvv.md:1414` — SCR-IV-01 là *"Danh sách **7 tab** phân loại theo trạng thái lifecycle"*, mỗi tab có **số đếm**; hồ sơ vừa nộp nằm ở tab *"Mới đăng ký / Chờ thẩm định"* (`:1434`, có **chấm đỏ khi > 0**), sau đó chạy tiếp qua *"Đang thẩm định"* (`:1435`) và *"Yêu cầu bổ sung"* (`:1436`).
- `srs-fr-04-chuyen-gia-tvv.md:1551` — trang chi tiết hồ sơ có **badge trạng thái lớn** ngay ở thẻ thông tin chính.
- Người hỗ trợ đã nộp hồ sơ **nhận thông báo trong phần mềm + thư điện tử** ở mọi mốc kết quả: yêu cầu bổ sung (`:524`), không đạt (`:525`), phê duyệt hoặc từ chối (`:625`, `:634`) — `[BA chốt 2026-07-30 — TDHSTVV_14]`.

> **Chỗ hở phát hiện khi tra câu này:** khối **Quyền truy cập** của SCR-IV-01 (`:1419-1422`) và SCR-IV-03 (`:1538-1541`) **không liệt kê Người hỗ trợ**, dù chính các tab của màn danh sách mô tả công việc của họ (`:1434`, `:1436`), dù §H7 trả họ về đúng màn này sau khi lưu, và dù trang chi tiết có nút *Sửa hồ sơ* ghi rõ *"Vai trò = **Người hỗ trợ**"* (`:1552`). Phải vá — xem phương án.

**→ Kết luận: Loại 3 — phần mềm đúng quy ước bắt buộc §H7, kỳ vọng của đối tác dẫn một màn không tồn tại; việc theo dõi tiến độ đã có sẵn ba đường. Dev action: Không · Sửa đặc tả: **Có** (vá khối Quyền truy cập thiếu Người hỗ trợ — chỗ hở phát hiện khi tra câu hỏi này) · Sheet: theo mục 12 (case lai).**

### Phương án xử lý (cập nhật SRS)

`srs-fr-04-chuyen-gia-tvv.md:1419-1422` (SCR-IV-01) và `:1538-1541` (SCR-IV-03) — bổ sung vào khối **Quyền truy cập** một dòng: *"Người hỗ trợ pháp lý: xem danh sách và chi tiết hồ sơ tư vấn viên thuộc đơn vị mình để theo dõi tiến độ thẩm định; sửa và nộp lại hồ sơ do mình nộp."* Viết theo đúng khuôn đã dùng ở SCR-IV-02 (`:1476`), nơi Người hỗ trợ **đã** được liệt kê.

Không vá thì đặc tả tự chọi: các tab của màn danh sách mô tả công việc của Người hỗ trợ, §H7 trả họ về đúng màn đó sau khi lưu, nhưng khối quyền lại không cho họ vào.

> **Phản hồi gửi đối tác:**
> **[Lý do]** Theo quy ước áp cho toàn bộ phần mềm, sau khi thêm mới một bản ghi thành công thì hệ thống quay về trang danh sách kèm thông báo. Phần mềm không có màn riêng mang tên *trang theo dõi tiến độ* cho luồng đăng ký tư vấn viên.
> **[Theo dõi tiến độ ở đâu]** Chính trang danh sách: có các thẻ phân loại theo trạng thái kèm số đếm, hồ sơ vừa nộp nằm ở thẻ *Mới đăng ký / Chờ thẩm định* rồi tự chuyển sang *Đang thẩm định* và *Yêu cầu bổ sung* theo tiến trình; mở hồ sơ ra thì trạng thái hiện ngay đầu trang. Người nộp hồ sơ còn nhận thông báo trong phần mềm và qua thư điện tử ở từng mốc kết quả.
> **[Nhận định]** Đề nghị Quý đơn vị cập nhật kết quả mong đợi thành *"…và quay lại trang danh sách tư vấn viên"*. Nếu vẫn cần một màn theo dõi riêng ngoài các đường trên, đề nghị đưa vào danh sách yêu cầu cải tiến.

---

## 10. Nhóm "Tư liệu pháp lý liên kết" phải có ô tìm kiếm và bộ lọc `[tự khép]`

**Vấn đề:** Trong màn chi tiết một nội dung tư vấn chuyên sâu có nhóm *Tư liệu pháp lý liên kết*. Đối tác kỳ vọng tìm được tư liệu ngay tại đó; bản đối tác đo (V1.0) chưa có ô tìm kiếm nào. Bản nội bộ V1.0.9 đã có ô từ khóa và ba bộ lọc, nhưng bảng thành phần màn hình trong đặc tả lại không khai bốn ô đó — nên chưa có căn cứ để chấm.

**(1)** Đặc tả **tự mâu thuẫn** giữa hai phần của cùng một chức năng:
- §Processing FR-X.1-06 đòi tìm kiếm là bắt buộc: `srs-fr-12-tv-chuyen-sau.md:947` — *"Nhận tiêu chí: keyword (tên tư liệu, mô tả), lĩnh vực, loại tư liệu, trạng thái"*; `:948` toàn văn có bỏ dấu; `:950` AND logic; `:951` phân trang 20/trang.
- §Thành phần màn hình SCR-X1-02 `:1171` chỉ khai bảng 9 cột + nút `[+ Thêm tư liệu]`, không có ô lọc nào. §Acceptance của FR-X.1-06 (`:986-996`) đếm được **0** tiêu chí về tìm kiếm.
- Màn riêng của chức năng này đã bị khai tử: `:828` và `:1227-1229` — SCR-X1-07 gộp vào SCR-X1-02 ⇒ nếu bảng thành phần không có ô tìm kiếm thì FR-X.1-06 **không còn màn nào để thực hiện**.

**(1b)** `.docx` **đứng về phía §Processing**: mục **4.12.6.2.3, chức năng số 10 "Tìm kiếm tư liệu pháp lý"** — *"Người sử dụng nhập từ khóa theo tên tư liệu hoặc mô tả, chọn lĩnh vực, loại tư liệu, trạng thái rồi tìm kiếm, hệ thống… tìm toàn văn có bỏ dấu tiếng Việt trên tên tư liệu và mô tả, áp dụng đồng thời tất cả điều kiện, phân trang 20 dòng mỗi trang."* ⇒ đối tác được giao một tài liệu **có** yêu cầu này; kỳ vọng của họ đúng.

**(2)** Không khác — đối tác đòi đúng thứ cả `.md` §Processing lẫn `.docx` đều yêu cầu.

**(3)** Bắt buộc, và **đã có quy ước chung phân xử sẵn**: `srs-v3.5.md:584` `UI-12` `[BA chốt 2026-07-30]` — *"Khi màn hình có mục không nằm trong bảng: nếu mục đó **có căn cứ** ở §Inputs / §Processing / §Outputs / mô hình dữ liệu của chính FR đang xét thì **bảng bị sót — phần mềm đúng**, BA bổ sung vào bảng; nếu **không có căn cứ** ở bất kỳ đâu trong SRS thì **phần mềm thừa**, đội phát triển gỡ."* Ô tìm kiếm và 3 bộ lọc **có căn cứ** ở §Processing của chính FR-X.1-06 (`:947-951`) ⇒ theo `UI-12` đây là **bảng bị sót, phần mềm đúng**, không phải phần dev làm thừa. Ngoài ra nhóm tư liệu phân trang 20 dòng, không có tìm kiếm thì cán bộ không tra được ở vụ việc nhiều tài liệu.

**→ Kết luận: Loại 2 — bảng thành phần màn hình bị sót, phần mềm bản V1.0.9 đã đúng. Dev action: Không · Sửa đặc tả: Có → Sheet: KHÔNG đổi trạng thái; phải đo lại trên môi trường nghiệm thu sau khi V1.0.9 lên.**

> **Phản hồi gửi đối tác:**
> **[Lý do]** Nhóm *Tư liệu pháp lý liên kết* trên bản dựng mới đã có ô nhập từ khóa và ba ô lọc theo loại tư liệu, lĩnh vực và trạng thái, kèm nút Tìm kiếm và Xóa bộ lọc; tìm kiếm chạy đúng. Ghi nhận *"màn hình không có chức năng"* của Quý đơn vị thực hiện trên bản dựng trước đó nên hiện tượng không còn tái hiện.
> **[Nhận định]** Đề nghị Quý đơn vị kiểm thử lại phiếu này sau khi bản dựng mới được triển khai lên môi trường nghiệm thu. Kết quả mong đợi giữ nguyên, không cần sửa.

### Phương án xử lý (cập nhật SRS)

1. `srs-fr-12-tv-chuyen-sau.md:1171` — bổ sung vào cột Dữ liệu / Nội dung: ô từ khóa (gợi ý *"Tìm theo tên hoặc mô tả tư liệu"*) + ba ô lọc *Loại tư liệu* / *Lĩnh vực* / *Trạng thái* + nút `[Tìm kiếm]` và `[Xóa bộ lọc]`, đặt trước bảng tư liệu.
2. `srs-fr-12-tv-chuyen-sau.md:986-996` — thêm 2 tiêu chí nghiệm thu cho FR-X.1-06: tìm theo từ khóa ra đúng tập bản ghi khớp tên hoặc mô tả; kết hợp đồng thời từ khóa và ba bộ lọc theo phép AND.
3. `srs-fr-12-tv-chuyen-sau.md:1198` — phần mô tả bổ sung hiện chỉ nói *"CRUD tư liệu inline"*, thêm vế tra cứu.
4. Hành vi kích hoạt lọc theo quy ước chung chốt ở **mục 21** (bấm `[Tìm kiếm]` mới lọc).

---

## 11. Tìm kiếm tư liệu bắt buộc hỗ trợ tiếng Việt không dấu `[tự khép]`

**Vấn đề:** Gõ từ khóa không dấu phải ra được bản ghi có tên viết có dấu. Phần mềm làm được, nhưng quy tắc gốc về tìm kiếm toàn văn lại không liệt kê chức năng này trong phạm vi áp dụng.

**(1)** Đặc tả **tự mâu thuẫn**:
- `srs-fr-12-tv-chuyen-sau.md:948` — *"| 3 | Full-text search trên ten_tu_lieu + mo_ta (hỗ trợ tiếng Việt unaccent) | BR-DATA-08 |"* ⇒ có yêu cầu.
- `srs-v3.5.md:5572` — `BR-DATA-08` chỉ liệt kê phạm vi *"FR-II-02, FR-X.1-02, FR-X.2-04"*, **không có FR-X.1-06**; hai bảng tham chiếu trong chính FR-12 (`:1579`, `:1635`) cũng chỉ gán cho FR-X.1-02.

**(1b)** `.docx` mục **4.12.6.2.3 chức năng 10** ghi thẳng *"tìm toàn văn **có bỏ dấu tiếng Việt**"* ⇒ đứng về phía `:948`.

**(2)** Không khác — đối tác đòi đúng thứ hai bản tài liệu yêu cầu.

**(3)** Bắt buộc: tên tư liệu pháp lý là tiếng Việt có dấu; cán bộ gõ nhanh thường bỏ dấu.

**→ Kết luận: Loại 2 — phần mềm đúng, phạm vi `BR-DATA-08` ghi sót. Dev action: Không · Sửa đặc tả: Có → Sheet: KHÔNG đổi trạng thái; đo lại trên môi trường nghiệm thu sau khi V1.0.9 lên.**

> **Phản hồi gửi đối tác:**
> **[Lý do]** Trên bản dựng mới, tìm kiếm tư liệu đã hỗ trợ tiếng Việt không dấu: gõ từ khóa không dấu vẫn ra đúng bản ghi có tên viết có dấu. Ghi nhận của Quý đơn vị thực hiện trên bản dựng trước đó nên hiện tượng không còn tái hiện.
> **[Nhận định]** Đề nghị Quý đơn vị kiểm thử lại phiếu này sau khi bản dựng mới được triển khai lên môi trường nghiệm thu. Kết quả mong đợi giữ nguyên, không cần sửa.

### Phương án xử lý (cập nhật SRS)

Bổ sung `FR-X.1-06` vào phạm vi áp dụng của `BR-DATA-08` ở **cả ba chỗ**: `srs-v3.5.md:5572` (bản gốc quy tắc) · `srs-fr-12-tv-chuyen-sau.md:1579` · `:1635` (hai bảng tham chiếu trong FR-12). Sửa một chỗ là để lại mâu thuẫn ở hai chỗ còn lại.

---

## 12. Thông báo đăng ký thành công phải kèm mã hồ sơ — Loại 4, hướng B `[tự khép]`

**Vấn đề:** Người hỗ trợ nộp hồ sơ tư vấn viên xong, hệ thống báo *"Đăng ký thành công, chờ thẩm định"*. Đối tác kỳ vọng câu này kèm luôn mã hồ sơ vừa sinh, để họ ghi lại và tra cứu về sau. Phần mềm sinh mã nhưng không ghép vào câu thông báo.

**(1)** `.md` **im lặng ở đúng điểm đang xét**. `srs-fr-04-chuyen-gia-tvv.md:351` — *"| 4 | thong_bao | text | — | 'Đăng ký thành công, chờ thẩm định' |"*; `:348` khai `ma_tvv` là một đầu ra **riêng**, không nói ghép vào câu thông báo. Mô tả nút Lưu `:1522` và trọn §Hậu điều kiện `:353-357` cũng không nhắc. Web khớp **nguyên văn** `:351`.

**(1b)** **`.docx` NÓI KHÁC.** Mục **4.4.3.2.3**, chức năng *"Nộp hồ sơ ứng viên tư vấn viên"*, Trường hợp 1: *"nộp thành công, hệ thống báo 'Đăng ký thành công, chờ thẩm định' **kèm mã tư vấn viên vừa sinh**."* ⇒ đối tác chấm **đúng theo văn bản được giao**. Đây là **Loại 4**, không phải "đối tác ghi kỳ vọng sai" như phiếu hỏi của QA kết luận.

**(2)** Khác đúng một vế: có kèm mã hay không.

**(3)** Bắt buộc theo hướng B — xem phân định dưới.

#### Căn cứ chi tiết

**(1b) — phân định hướng A hay B theo cây trọng tài.** Câu hỏi: khi lên bản `.md` hiện hành, vế "kèm mã" bị **bỏ có chủ đích** hay bị **sót**?

- **Tín hiệu mở đầu:** `.md` **có** dùng đúng cách làm này ở nhóm FR khác — `srs-fr-04-chuyen-gia-tvv.md:597`: *"…gửi mail link kích hoạt vĩnh viễn (1 lần dùng) **kèm mã số TVV**"*, là quyết định `[chốt UAT tuần 2, 2026-07-16]` ghi ở `:24`. ⇒ nghi **bị sót**.
- **Tầng 1 cây trọng tài** — quyết định BA gần nhất chạm tới điểm này: `:24` (2026-07-16) chỉ thêm mã vào **thư điện tử**, không có câu nào **loại bỏ** mã khỏi thông báo trên màn. Không có dấu bỏ có chủ đích.
- **Tầng 2** — mô hình dữ liệu: `ma_tvv` đã là đầu ra khai sẵn ở `:348`, máy chủ đã trả `maTvv` trong chính phản hồi của lượt tạo ⇒ dữ liệu có sẵn, không phát sinh nguồn mới.
- ⇒ **Hướng B — `.md` bị sót.**

**Giá trị nghiệp vụ:** người hỗ trợ đăng ký hộ nhiều hồ sơ liên tiếp; không có mã trên thông báo thì phải mở lại danh sách dò theo tên để biết hồ sơ nào vừa nộp.

**→ Kết luận: Loại 4 hướng B — bản gốc bị sót, bổ sung đặc tả rồi Dev chỉnh câu thông báo. Dev action: Có · Sửa đặc tả: Có · Doc action: Không cần gỡ, chỉ chuẩn hoá nguyên văn ở bản `.docx` kế tiếp → Sheet: Giữ xử lý (dòng 35).**

**Việc Dev:** Ghép mã hồ sơ vào thông báo sau khi đăng ký: "Đăng ký thành công, chờ thẩm định. Mã hồ sơ: {ma_tvv}". *Nghiệm thu:* nộp hồ sơ → thông báo có mã vừa sinh.

Theo khuôn Loại 4:

| Trường | Nội dung |
|---|---|
| Bản `.docx` đối chiếu | `HTPLDN-PTYC-CT-v3.5.docx`, tệp ngày 01/08/2026; chưa ghi nhận được ngày bàn giao và kênh gửi |
| Trích `.docx` | Mục 4.4.3.2.3, chức năng *"Nộp hồ sơ ứng viên tư vấn viên"*, Trường hợp 1 — *"…báo 'Đăng ký thành công, chờ thẩm định' kèm mã tư vấn viên vừa sinh."* |
| Trích `.md` | `srs-fr-04-chuyen-gia-tvv.md:351` — chỉ *"Đăng ký thành công, chờ thẩm định"*, không có vế kèm mã |
| Hướng | **B** — `.md` bị sót (căn cứ ở `#### Căn cứ chi tiết`) |
| Dev action | Có |
| Doc action | Bên soạn tài liệu chuẩn hoá nguyên văn câu thông báo ở bản `.docx` kế tiếp cho khớp câu chốt dưới đây |
| Sheet | Giữ xử lý |

### Phương án xử lý (cập nhật SRS)

1. `srs-fr-04-chuyen-gia-tvv.md:351` — *"Đăng ký thành công, chờ thẩm định"* → *"Đăng ký thành công, chờ thẩm định. Mã hồ sơ: {ma_tvv}"*.
2. `srs-fr-04-chuyen-gia-tvv.md:1522` — mô tả nút *Lưu*: thêm vế thông báo có kèm mã hồ sơ, để bảng thành phần màn hình không lệch §Outputs.
3. Kiểm chéo trước khi sửa: không đụng câu thông báo của luồng phê duyệt (*"Đã công nhận tư vấn viên"*, `:24`) và không đụng nội dung thư kích hoạt (`:597` đã có mã).

**Không có phản hồi cho vế này** — Dev sửa toàn bộ nên không có gì phải giải trình với đối tác. Cách gửi cho cả dòng 35 ghi ở đầu Phần II.

---

## 12b. Nhãn nút ở màn Thêm mới Tư vấn viên — giữ "Lưu"  **✅ BA duyệt 09/08/2026**

> **Vế thứ tư của cùng dòng 35 `DKTGMLTVV_13`.** Phiếu hỏi của QA xếp điểm này là "ghi nhận, không cần BA quyết"; nhưng đối tác **hỏi thẳng** trong ô phản hồi nên phải có câu trả lời gửi lại. Đánh số `12b` để không xô lệch 34 mục đã đánh.

**Vấn đề:** Ở màn Thêm mới Tư vấn viên, nút lưu hồ sơ mang nhãn *"Lưu"*. Đối tác hỏi lại trong ô phản hồi: *"Màn hình chức năng không có button Gửi đăng ký, chỉ có button Lưu — là do tên button sai hay thiếu nút chức năng vậy ạ"*, kèm ghi chú *"BA xác nhận tên button sai"*. Chưa ai trả lời câu hỏi này.

**(1)** Đặc tả nói **"Lưu"**, ở mức bắt buộc: `srs-v3.5.md:6756` §H4 — *"Nút lưu luôn **"Lưu"** (không "Lưu lại", "Cập nhật", "Hoàn tất"…)"*, mức **BẮT BUỘC** áp cho **mọi** màn; `srs-fr-04-chuyen-gia-tvv.md:1522` cũng ghi *"Hủy" (phụ) / "Lưu" (chính)"*.

**(1b)** `.docx` **cùng hướng**: mục 4.4.3.2.3 mô tả thao tác là *"bấm 'Lưu'"*. Chuỗi *"Gửi đăng ký"*: **0 kết quả** trên toàn bộ 18 tệp `srs-v3.5/` và **0 kết quả** trong `.docx`.

**(2)** Đối tác không đòi thêm chức năng — họ hỏi để làm rõ. Bước thao tác của **chính phiếu** cũng ghi *"Dữ liệu hợp lệ và nhấn **Lưu**"* ⇒ nút *Lưu* là tiền đề thao tác họ đã dùng, không phải kết quả mong đợi bị lệch.

**(3)** Điểm mấu chốt: ghi chú *"BA xác nhận tên button sai"* **chưa từng được nhập vào đặc tả** — không có dấu thay đổi nào (`[STT…]` / `[CR-…]` / `[BA chốt …]`) chạm tới nhãn nút của SCR-IV-02, và 3 đợt áp UAT gần nhất vào FR-04 (`:24` ngày 2026-07-16 · `:26` ngày 2026-07-30 · `:27` ngày 2026-07-31) đều không đổi nhãn nút, dù đợt 2026-07-30 có xử đúng nhóm mã `DKTGMLTVV_02` / `DKTGMLTVV_03`. ⇒ **Cần BA xác nhận lại**: giữ nguyên, hay đúng là đã có ý định đổi mà chưa nhập đặc tả.

**→ Kết luận: Loại 3 — **giữ nhãn "Lưu"** `[BA duyệt 2026-08-09]`. Phần mềm đúng cả `.md` lẫn `.docx`. Căn cứ bạn chốt: **tên màn "Thêm mới Tư vấn viên" đã mang ngữ nghĩa**, nút chỉ cần mang hành động chung — đúng triết lý §H4 (tiêu đề gánh nghĩa, nút gánh hành động, thống nhất mọi màn). Dev action: Không · Sửa đặc tả: Không → Sheet: theo mục 12 (case lai, cùng dòng 35).**

> **Phản hồi gửi đối tác:** *(gửi sau khi BA xác nhận giữ nhãn)*
> **[Lý do]** Màn hình **không thiếu nút chức năng**. Theo quy ước đặt tên áp cho toàn bộ phần mềm, nút lưu bản ghi luôn mang nhãn *"Lưu"*; tài liệu bàn giao cũng mô tả thao tác nộp hồ sơ là bấm *"Lưu"*. Phần mềm không có nút nào tên *"Gửi đăng ký"*, và bấm *"Lưu"* chính là hoàn tất việc nộp hồ sơ ứng viên.
> **[Nhận định]** Không cần sửa kết quả mong đợi — bước thao tác của phiếu vốn đã ghi *"nhấn Lưu"*. Tên màn *Thêm mới Tư vấn viên* đã cho biết đang tạo hồ sơ tư vấn viên; nút *Lưu* là hành động chung áp thống nhất cho mọi màn của phần mềm, giúp người dùng thao tác nhất quán. Nếu Quý đơn vị vẫn thấy cần đổi tên nút cho sát nghiệp vụ, đề nghị đưa vào danh sách yêu cầu cải tiến.

# PHẦN III — QLHSPLDN_15 (1 mục)

## 13. Xuất Excel khi bộ lọc không ra bản ghi nào  **✅ BA duyệt 09/08/2026**

**Vấn đề:** Ở tab Hồ sơ pháp lý của một doanh nghiệp, cán bộ lọc ra 0 dòng rồi bấm *Xuất Excel*. Phần mềm chặn và báo *"Không có dữ liệu để xuất"*, không tạo tệp. Đặc tả không có dòng nào cho tình huống này nên chưa có căn cứ chấm, và dòng phiếu đang treo.

**(1)** Đặc tả **im lặng**: `srs-fr-12-tv-chuyen-sau.md:657-665` (§Processing Xuất Excel của FR-X.1-04) mô tả đủ 5 bước — áp bộ lọc, giới hạn 10.000 dòng, 8 cột, trả tệp — **không nói gì** về bộ lọc rỗng. Bảng Error Handling của chính chức năng đó (`:693-701`) liệt kê đủ E1→E7, trong đó `E7 / INF-HSPL-01` là *"Không có kết quả tìm kiếm"* cho thao tác **tra cứu**, không có mã nào cho thao tác **xuất tệp**. `srs-v3.5.md:5570` `BR-DATA-06` chỉ đặt giới hạn trên 10.000 dòng.

**(1b)** `.docx` **cũng im lặng**: mục 4.12.4, chức năng *"Xuất tệp bảng tính danh sách hồ sơ"* chỉ mô tả áp bộ lọc, 10.000 dòng và các cột. ⇒ không phải tranh chấp tài liệu.

**(2)** Đối tác kỳ vọng đúng câu phần mềm đang hiện. Nhưng đối tác báo *"màn hình không có nút chức năng"* ở môi trường nghiệm thu ngày 17/07 nên **chưa từng chạy tới bước này**.

**(3)** Bắt buộc phải chốt: hai chức năng khác đã có quy định cho đúng tình huống này, với **hai câu chữ khác nhau** — `srs-fr-13-tv-nhanh.md:155` `INF-KHO-XL-01` *"Không có dữ liệu để xuất"* `[BA-07 tuần 4]` và `srs-fr-15-ct-htpldn.md:403` `INF-XI-02-XL-01` *"Không có chương trình nào để xuất"*. Không chốt thì màn thứ tư lại đẻ ra câu thứ ba.

**→ Kết luận: Loại 2 — đặc tả im lặng ở cả hai bản; chốt **quy ước dùng chung: chặn xuất, không tạo tệp rỗng, báo "Không có dữ liệu để xuất"** `[BA duyệt 2026-08-09]`. Phần mềm đang chạy đúng thứ này. Dev action: **Không** · Sửa đặc tả: Có → Sheet: KHÔNG đổi trạng thái (dòng 297 giữ nguyên, QA chấm lại sau khi đặc tả xong và bản mới lên môi trường nghiệm thu).**

### Phương án xử lý (cập nhật SRS)

**Chốt mức có quy ước** `[BA duyệt 2026-08-09]` — thêm một dòng vào Phụ lục E của `srs-v3.5.md`, mức BẮT BUỘC:

> *"Mọi nút Xuất Excel: nếu bộ lọc hiện hành không ra bản ghi nào thì **chặn xuất, không tạo tệp rỗng**, và báo câu chuẩn **"Không có dữ liệu để xuất"**. Chức năng nào cần câu riêng theo đối tượng thì phải ghi rõ tại FR đó."*

Kèm theo:

1. `srs-fr-12-tv-chuyen-sau.md:693-701` — thêm một dòng Error Handling cho `FR-X.1-04` với câu chuẩn trên, mức INFO. Mã lỗi đặt theo tiền tố đang dùng của nhóm; **grep kiểm không trùng toàn thư mục trước khi đặt**.
2. `srs-fr-13-tv-nhanh.md:155` (`INF-KHO-XL-01`) — đã đúng câu chuẩn, giữ nguyên, chỉ thêm dẫn chiếu về quy ước mới.
3. `srs-fr-15-ct-htpldn.md:403` (`INF-XI-02-XL-01`, *"Không có chương trình nào để xuất"*) — **giữ nguyên như ngoại lệ đã ghi rõ tại FR**, đúng vế thứ hai của quy ước. **Không phát sinh việc cho Dev.**
4. **Số hiệu §H cấp khi thi hành**, theo thứ tự các quy ước được duyệt — không đặt cứng trong phiếu này vì còn vài quy ước khác đang chờ chốt (mục 15 · 21 · 29 · 33 · 34).

> **Điểm liền kề chưa chốt:** cùng hai chức năng đối chứng còn xử lý **khác nhau khi vượt 10.000 dòng** — kho câu hỏi **chặn xuất**, chương trình **xuất 10.000 dòng đầu**. Quy ước vừa chốt chỉ phủ trường hợp **rỗng**. Đã ghi ở bảng điểm treo; nên chốt cùng lượt để khỏi mở lại Phụ lục E hai lần.

> **Phản hồi gửi đối tác:**
> **[Lý do]** Màn *Hồ sơ pháp lý* của doanh nghiệp trên bản dựng mới đã có đầy đủ nút chức năng, trong đó có xuất tệp bảng tính. Khi bộ lọc không ra bản ghi nào, hệ thống báo đúng câu *"Không có dữ liệu để xuất"* và không tạo tệp rỗng — trùng với kết quả Quý đơn vị mong đợi. Ghi nhận *"màn hình không có nút chức năng"* ngày 17/07 thực hiện trên bản dựng trước đó.
> **[Nhận định]** Đề nghị Quý đơn vị kiểm thử lại phiếu này sau khi bản dựng mới được triển khai lên môi trường nghiệm thu. Kết quả mong đợi giữ nguyên, không cần sửa.

---

# PHẦN IV — Tệp tổng hợp 06/08 (21 mục)

> **18/21 mục không treo verdict phiếu nào** — trả lời để lượt kiểm thử sau không chấm sai và Dev không dọn nhầm. Ba mục đang treo verdict: **14 · 27 · 28**.

## 14. Báo cáo Vụ việc đã tiếp nhận không có biểu đồ tròn theo lĩnh vực `[tự khép]`

**Vấn đề:** Đối tác mở báo cáo *Vụ việc đã tiếp nhận* và kỳ vọng thấy biểu đồ tròn chia theo lĩnh vực pháp luật, kèm hai cột *Theo kênh* và *Theo lĩnh vực* trong bảng tổng hợp. Màn chỉ có biểu đồ cột theo kênh và biểu đồ đường theo thời gian; chiều lĩnh vực được trình bày bằng bảng.

**(1)** Phần mềm **đúng**. `srs-fr-11-bao-cao.md:1070` — *"| **Vụ việc** | UC125 | BC Vụ việc đã tiếp nhận | Kênh tiếp nhận, Lĩnh vực PL | **Bar + Trend** |"*. Cùng bảng đó gán `Donut + Trend` cho UC124 (`:1069`) và `Bar + Donut` cho UC127 (`:1072`) ⇒ biểu đồ tròn là khái niệm **có** trong đặc tả và **cố ý không** gán cho UC125.

**(1b)** `.docx` **cùng hướng**: mục **4.11.2.2.2** (Báo cáo vụ việc đã tiếp nhận) — *"gồm biểu đồ cột theo kênh tiếp nhận và biểu đồ diễn biến theo thời gian"*. Đối chứng: `.docx` **có** dùng biểu đồ tròn ở ba báo cáo khác (mục 4.11.1, 4.11.4, 4.11.8) ⇒ việc không có ở 4.11.2 là chủ ý, không phải sót.

**Bóc ý con Kết quả mong đợi của `VVDTN_04`:**

| Ý con trong Kết quả mong đợi | Bản gốc có không | Phiếu xử ở đâu |
|---|---|---|
| (a) Biểu đồ **tròn** theo lĩnh vực | Không — `.md` và `.docx` đều gán Bar + Trend | Mục này — Reject, đề nghị đưa vào yêu cầu cải tiến |
| (b) Bảng tổng hợp có chiều **Theo kênh** và **Theo lĩnh vực** | Có | Mục này — **đã hết lỗi** trên V1.0.8 |

**(2)** Vế (b) — hai chiều *theo kênh* và *theo lĩnh vực* — **đã hết lỗi** trên bản V1.0.8: cả hai bảng đều hiện, số liệu cộng khớp tổng và khớp đường đo độc lập. Chỉ còn vế (a) là đòi thêm ngoài đặc tả.

**(3)** Không bắt buộc: chiều lĩnh vực đã có đủ số liệu kèm cột tỷ lệ ở dạng bảng, đọc được chính xác hơn biểu đồ tròn khi có nhiều lĩnh vực.

**→ Kết luận: Loại 3 — phần mềm đúng cả hai bản tài liệu; phần đối tác đòi thêm không bắt buộc. Dev action: Không · Sửa đặc tả: Không → Sheet: Reject** (đã kiểm đủ hai vế: phần mềm không phải sửa, đặc tả không phải sửa).

> **Phản hồi gửi đối tác:**
> **[Lý do]** Theo thiết kế đã bàn giao, báo cáo *Vụ việc đã tiếp nhận* gồm biểu đồ cột theo kênh tiếp nhận và biểu đồ diễn biến theo thời gian; số liệu theo lĩnh vực pháp luật được trình bày bằng bảng có cột tỷ lệ. Biểu đồ tròn được dùng ở một số báo cáo khác, không áp dụng cho báo cáo này. Hai chiều *theo kênh* và *theo lĩnh vực* mà Quý đơn vị nêu hiện đã hiển thị đầy đủ và số liệu cộng khớp tổng.
> **[Nhận định]** Đề nghị Quý đơn vị cập nhật kết quả mong đợi; nếu vẫn cần biểu đồ tròn theo lĩnh vực, đề nghị đưa vào danh sách yêu cầu cải tiến.

---

## 15. Phản hồi của máy chủ khi tệp vượt 20MB không mang đúng mã lỗi đã khai  **✅ BA duyệt 09/08/2026**

**Vấn đề:** Đính tệp vượt 20MB vào tư liệu pháp lý. Giao diện chặn ngay và báo tiếng Việt đúng nghĩa. Nhưng nếu gọi thẳng máy chủ thì nhận về câu tiếng Anh *"File too large"* kèm mã lỗi hệ thống chung, không nêu ngưỡng. Đối tác không nêu điểm này.

**(1)** Đặc tả **có** quy định riêng: `srs-fr-12-tv-chuyen-sau.md:884` — *"| 2 | Kiểm tra file: max 20MB, định dạng cho phép | EC-FILE-01 |"*; `:981` — *"| E3 | File vượt 20MB | ERR-TLPL-03 | 'File tối đa 20MB' | ERROR |"*. Đặc tả **im lặng** ở chỗ khác: không nói bảng Error Handling đo ở lớp nào.

**(1b)** Không phải tranh chấp tài liệu.

**(2)** Đối chứng loại trừ: cùng endpoint đó, tệp chứa mã độc **trả đúng** mã riêng `ERR-TLPL-04` kèm câu tiếng Việt ⇒ cơ chế trả mã lỗi theo tình huống vẫn chạy được, đây là chỗ sót chứ không phải giới hạn kỹ thuật.

**(3)** Bắt buộc ở mức mã lỗi, không bắt buộc ở mức câu chữ — xem phân định dưới.

**→ Kết luận: Loại 1 phần mã lỗi — phần mềm trả sai mã đã khai; chốt quy ước **mã lỗi áp mọi lớp, câu chữ đo ở lớp giao diện** `[BA duyệt 2026-08-09]`. Dev action: Có (mức Minor, đúng một chỗ) · Sửa đặc tả: Có (một dòng quy ước phạm vi) → Sheet: chưa có dòng phiếu; QA mở dòng mới `QLTLPLCVV_QA01` ở đợt kế tiếp.**

### Phương án xử lý (cập nhật SRS)

**Chốt phạm vi bảng Error Handling** `[BA duyệt 2026-08-09]` — ghi **một lần** vào quy ước chung của `srs-v3.5.md`, không lặp ở từng FR:

> *"**Mã lỗi** khai trong bảng Error Handling áp cho **mọi lớp** của hệ thống: khi máy chủ từ chối vì đúng điều kiện đã khai, phản hồi phải mang đúng mã lỗi đó, không dùng mã hệ thống chung.
> **Câu chữ hiển thị** trong bảng Error Handling đo ở **lớp người dùng cuối nhìn thấy** — tức giao diện. Máy chủ không bắt buộc trả nguyên văn câu tiếng Việt."*

Cách này khép cả hai lo ngại: người dùng cuối vẫn được lớp giao diện bảo vệ, còn mã lỗi thì đủ chính xác để lần vết và để bên tích hợp xử lý.

**Việc Dev — đúng một chỗ:** máy chủ trả `ERR-TLPL-03` (`srs-fr-12-tv-chuyen-sau.md:981`) thay cho mã hệ thống chung khi tệp vượt 20MB. Mức **Minor**. Cơ chế đã sẵn sàng — cùng endpoint đó, tệp chứa mã độc đã trả đúng `ERR-TLPL-04`.

**Hệ quả cần rà khi thi hành:** quy ước này áp cho **mọi** bảng Error Handling trong đặc tả, nên sau khi chốt phải rà xem còn chỗ nào máy chủ đang trả mã hệ thống chung cho một điều kiện đã khai mã riêng. Lượt này mới đo được đúng một ca (tệp vượt 20MB); các ca khác chưa đo. Ghi vào điểm treo, **không** mở rộng phạm vi Dev ngoài một chỗ trên khi chưa có bằng chứng đo.

**Số hiệu §H cấp khi thi hành**, cùng lượt với các quy ước khác đang chờ chốt.

## 16. Bộ lọc "Trạng thái chương trình" phải có đủ 3 giá trị `[tự khép]`

**Vấn đề:** Báo cáo *Số lượng chương trình hỗ trợ* có ô lọc trạng thái với ba lựa chọn *Đã phê duyệt · Đang thực hiện · Hoàn thành*, còn đặc tả chỉ liệt kê hai. Nếu bỏ bớt một giá trị thì tổng số chương trình sẽ không bằng tổng các nhóm lọc ra.

**(1)** Đặc tả **tự mâu thuẫn**: `srs-fr-11-bao-cao.md:900` — *"| 1 | trang_thai_ct | text | N | DANG_THUC_HIEN / HOAN_THANH |"* (2 giá trị), trong khi `:82` (Processing chung) — *"Truy vấn dữ liệu: CHỈ bản ghi đã duyệt (trạng thái đã duyệt / hoàn thành / đã thanh toán)"* ⇒ tập dữ liệu vào báo cáo **có** nhóm *đã duyệt*, và `:910` đòi `tong_ct` là tổng số chương trình.

**(1b)** Không phải tranh chấp tài liệu — đối tác không nêu.

**(2)** Đo được: không lọc thì *Đã phê duyệt 5 · Đang thực hiện 1 · Hoàn thành 1*, cộng bằng tổng 7. Bỏ nhóm *Đã phê duyệt* thì hai nhóm còn lại cộng được 2, lệch tổng 7.

**(3)** Bắt buộc: bộ lọc phải phủ đúng tập trạng thái mà báo cáo thống kê, nếu không thì người dùng lọc lần lượt từng giá trị vẫn không ra được tổng.

**→ Kết luận: Loại 2 — đặc tả liệt kê thiếu, phần mềm đã đúng. Dev action: Không · Sửa đặc tả: Có → Sheet: không có dòng phiếu riêng (verdict `SLCTHT_06` đang Reopen vì lý do khác, không liên quan mục này).**

### Phương án xử lý (cập nhật SRS)

1. `srs-fr-11-bao-cao.md:900` — ràng buộc: `DA_DUYET / DANG_THUC_HIEN / HOAN_THANH`.
2. Thêm một câu nguyên tắc ngay dưới `:82`: *"Tập giá trị của ô lọc trạng thái phải phủ đúng tập trạng thái mà báo cáo thống kê, để tổng các nhóm lọc bằng tổng chung."*
3. **Điểm treo kèm theo:** entity `CHUONG_TRINH` có 8 trạng thái (`srs-fr-15-ct-htpldn.md:1342`), trong đó **`DA_CONG_BO`** và **`TAM_DUNG`** chưa rõ có nằm trong tập báo cáo thống kê hay không. Cần BA xác nhận ở lượt sau — không chặn mục này.

---

## 17. Nhãn kỳ báo cáo trong tệp xuất phải là chữ tiếng Việt `[tự khép]`

**Vấn đề:** Tệp Excel xuất từ báo cáo có dòng ghi kỳ báo cáo. Chọn kỳ *Năm* thì tệp in *"Năm"*; chọn kỳ *Khoảng* thì tệp in *"KHOANG"* — mã nội bộ viết hoa không dấu. Tệp này là bản người dùng gửi ra ngoài, đính kèm báo cáo lên cấp trên.

**(1)** Đặc tả **im lặng ở câu chữ nhưng đủ nghĩa**: `srs-fr-11-bao-cao.md:1097` chỉ đòi *"chèn tiêu đề BC + thông tin kỳ + đơn vị + ngày tạo vào header file"*; `:95` — *"| 2 | ky_bao_cao | text | Luôn | **Kỳ đã chọn** |"*. *"Kỳ đã chọn"* là cái người dùng chọn trên màn, tức chữ *Khoảng*, không phải mã nội bộ.

**(1b)** Không phải tranh chấp tài liệu — đối tác không nêu.

**(2)** Cùng một tệp, cùng một chỗ, khi thì in nhãn tiếng Việt khi thì in mã nội bộ ⇒ không nhất quán ngay trong chính phần mềm.

**(3)** Bắt buộc: tệp kết xuất là văn bản đối ngoại; mã nội bộ viết hoa không dấu không đọc được với người nhận.

**→ Kết luận: Loại 1 — phần mềm in không nhất quán, không có cách đọc nào của đặc tả cho phép in mã nội bộ. Dev action: Có (mức Minor) · Sửa đặc tả: Có (ghi rõ để khỏi tranh chấp lại) → Sheet: chưa có dòng phiếu; QA mở dòng mới `CTTDVQL_QA01` ở đợt kế tiếp.**

**Việc Dev:** Tệp xuất in nhãn kỳ bằng **chữ tiếng Việt** (Năm/Quý/Tháng/Khoảng), không in mã nội bộ. *Nghiệm thu:* xuất kỳ "Khoảng" → dòng kỳ trong tệp ghi "Khoảng", không phải "KHOANG".

### Phương án xử lý (cập nhật SRS)

`srs-fr-11-bao-cao.md:1097` — bổ sung: *"Nhãn kỳ báo cáo in trong tệp kết xuất dùng đúng chữ tiếng Việt hiển thị trên màn (Năm · Quý · Tháng · Khoảng), không in mã nội bộ."* Áp cho **mọi** loại báo cáo dùng chung chức năng xuất, vì `:1097` nằm ở phần dùng chung.

---

## 18. Báo cáo Chương trình theo thời gian giữ phần thống kê ngân sách  **✅ BA duyệt 09/08/2026**

**Vấn đề:** Báo cáo *Chương trình theo thời gian* đang hiện thêm thẻ *Tổng ngân sách toàn kỳ*, một đường ngân sách trên biểu đồ, một cột ngân sách trong bảng và trong tệp xuất. Danh sách đầu ra trong đặc tả không liệt kê mục ngân sách nào.

**(1)** Đặc tả **im lặng**: `srs-fr-11-bao-cao.md:1021-1023` liệt kê đúng 3 mục đầu ra (`trend_data[]`, `chart_type = LINE`, `tong_ct`), không có ngân sách — nhưng cũng **không có câu bỏ**. Đối chứng: khi BA muốn bỏ một mục thì có ghi rõ, ngay tại `:1021` — *"[CTTLV_04 chốt 2026-07-24: **bỏ so_dn**…]"*.

**(1b)** Không phải tranh chấp tài liệu — đối tác không nêu.

**(2)** Báo cáo anh em `FR-IX-21` (*Chương trình theo đơn vị*) **có** `tong_ngan_sach` trong danh sách đầu ra (`:948`) ⇒ chiều ngân sách đã là dữ liệu chính thức của nhóm báo cáo chương trình.

**(3)** Không bắt buộc, nhưng có giá trị quản lý: theo dõi ngân sách theo kỳ là thông tin điều hành, dữ liệu đã có sẵn, và đã có tiền lệ giữ phần vượt độ phủ khi nó phục vụ nghiệp vụ.

**→ Kết luận: Loại 2 — chốt **giữ** phần thống kê ngân sách; đặc tả liệt kê thiếu, phần mềm đang đúng `[BA duyệt 2026-08-09]`. Dev action: Không · Sửa đặc tả: Có · Doc action: Có → Sheet: không có dòng phiếu riêng.**

### Phương án xử lý (cập nhật SRS)

**Chốt giữ phần ngân sách** `[BA duyệt 2026-08-09]` — phần mềm đang hiển thị đúng, chỉ bổ sung đặc tả cho khớp.

1. `srs-fr-11-bao-cao.md:1021-1023` — bổ sung vào danh sách đầu ra của `FR-IX-23`: **`tong_ngan_sach`** (tổng toàn kỳ) và **cột ngân sách theo từng kỳ** trong `trend_data[]`. Viết theo đúng khuôn đã dùng ở `FR-IX-21` (`:948` — *"| 5 | tong_ngan_sach | money | Luôn | Tổng ngân sách |"*).
2. `srs-fr-11-bao-cao.md` §Acceptance của `FR-IX-23` — bổ sung một tiêu chí nghiệm thu cho chiều ngân sách, để lượt kiểm thử sau có thước đo.
3. **Doc action:** bổ sung khối *Tổng ngân sách toàn kỳ* và cột ngân sách vào mục tương ứng của `.docx` ở bản kế tiếp — phần mềm đã hiển thị nhưng bản bàn giao chưa mô tả.

> **Không đụng `so_dn`.** Dòng `:1021` đã chốt **bỏ** `so_dn` `[CTTLV_04 chốt 2026-07-24]`; việc báo cáo vẫn đang thống kê *Số DN* là **lỗi riêng, đã đủ căn cứ**, QA mở phiếu riêng — không gộp vào mục này.

## 19. Nhãn lựa chọn kết luận kiểm tra hồ sơ — Loại 4, hướng B `[tự khép]`

**Vấn đề:** Cán bộ kiểm tra hồ sơ vụ việc, ô Kết luận có lựa chọn *"Đạt — chuyển sang phân công"*. Chọn xong thì vụ việc **vẫn giữ** trạng thái *Đang kiểm tra* — đúng thiết kế, và chính câu thông báo hệ thống hiện ra cũng nói đúng: *"Kiểm tra hồ sơ đạt — sẵn sàng phân công"*. Chỉ nhãn trong ô chọn là nói sai việc.

**(1)** `.md` quy định **giá trị** của trường (`DAT` / `KHONG_DAT` / `YEU_CAU_BO_SUNG` — `srs-fr-05-vu-viec.md:522`) nhưng **im lặng về chữ hiển thị**. Hành vi thì rõ: `:541` — *"Nếu DAT: vụ việc sẵn sàng phân công, **giữ trạng thái DANG_KIEM_TRA** — chỉ chuyển DA_PHAN_CONG khi CB NV phân công người/tổ chức xử lý qua FR-V.I-09"*.

**(1b)** **`.docx` KHÔNG im lặng** — mục **4.5.6**, bảng *Mô tả thông tin trên màn hình*, trường *Kết luận kiểm tra*: *"Bắt buộc chọn một trong ba: **'Đạt', 'Không đạt', 'Yêu cầu bổ sung'**."* Ba nhãn **trần**, không hậu tố. Cùng mục đó, bảng *Chức năng trên màn hình* còn mô tả đúng hành vi: *"Trường hợp 1: kết luận 'Đạt', vụ việc sẵn sàng phân công và **vẫn giữ trạng thái 'Đang kiểm tra'**; chỉ chuyển sang 'Đã phân công' khi cán bộ thực hiện phân công…"* ⇒ **`.md` bị sót ba nhãn mà `.docx` đã có**, còn phần mềm thì tự thêm hậu tố ngoài cả hai bản.

**(2)** Đây đúng là chỗ đối tác đã hiểu nhầm: kỳ vọng ghi trong phiếu `KTHSYCHTPL_11` là *"chuyển Đang kiểm tra → Đã phân công"*, và BA đã bác kỳ vọng đó ngày **2026-07-16** (`srs-fr-05-vu-viec.md:22`). Nhãn hiện tại đang nói y như kỳ vọng đã bị bác.

**(3)** Bắt buộc đổi: nhãn hiện tại hứa một việc hệ thống cố ý không làm, để nguyên thì mỗi vòng kiểm thử lại sinh đúng một phiếu lỗi ở chỗ này. Và vì `.docx` đã chốt sẵn ba nhãn trần nên **không cần nghĩ chữ mới** — chỉ cần gỡ hậu tố cho khớp bản bàn giao.

**→ Kết luận: Loại 4 hướng B — `.md` bị sót ba nhãn mà `.docx` đã chốt; phần mềm tự thêm hậu tố ngoài cả hai bản. Chốt ba nhãn trần **"Đạt" / "Không đạt" / "Yêu cầu bổ sung"** theo `.docx`. Dev action: Có (mức Trivial, gỡ hậu tố ở cả ba nhãn, không đụng hành vi) · Sửa đặc tả: Có · Doc action: **Không** — `.docx` đã đúng → Sheet: verdict `KTHSYCHTPL_11` giữ **Pass**; QA mở dòng mới ở đợt kế tiếp cho việc sửa chữ.**

**Việc Dev:** Gỡ hậu tố ở ba nhãn kết luận kiểm tra, còn **"Đạt" / "Không đạt" / "Yêu cầu bổ sung"**. *Nghiệm thu:* mở ô Kết luận → ba nhãn trần, không còn "— chuyển sang phân công".

Theo khuôn Loại 4:

| Trường | Nội dung |
|---|---|
| Bản `.docx` đối chiếu | `HTPLDN-PTYC-CT-v3.5.docx`, tệp ngày 01/08/2026; chưa ghi nhận được ngày bàn giao và kênh gửi |
| Trích `.docx` | Mục 4.5.6, trường *Kết luận kiểm tra* — *"Bắt buộc chọn một trong ba: 'Đạt', 'Không đạt', 'Yêu cầu bổ sung'."* |
| Trích `.md` | `srs-fr-05-vu-viec.md:522` — chỉ có mã giá trị `DAT / KHONG_DAT / YEU_CAU_BO_SUNG`, **không có** cột nhãn hiển thị |
| Hướng | **B** — `.md` bị sót. Tín hiệu: nhãn hiển thị là thứ `.md` **có** khai ở nhóm FR khác (ví dụ bảng ánh xạ nhãn mức cảnh báo `srs-fr-05-vu-viec.md:1516`), thiếu đúng ở chỗ đang xét |
| Dev action | Có — gỡ hậu tố ở cả ba nhãn |
| Doc action | Không — `.docx` đã đúng, không có gì phải gỡ hay bổ sung |
| Sheet | `KTHSYCHTPL_11` giữ Pass |

### Phương án xử lý (cập nhật SRS)

`srs-fr-05-vu-viec.md:522` — bổ sung cột nhãn hiển thị cho ba giá trị, **chép đúng chữ của `.docx`**: `DAT` → *"Đạt"* · `KHONG_DAT` → *"Không đạt"* · `YEU_CAU_BO_SUNG` → *"Yêu cầu bổ sung"*.

> **Vì sao chọn nhãn trần thay vì nhãn có hậu tố gợi ý:** hậu tố phải áp đồng đều cả ba nhãn mới nhất quán, mà `.docx` đã chốt cả ba là chữ trần. Đặt ra bộ nhãn thứ ba (không giống `.docx`, không giống phần mềm) là tự sinh thêm một điểm lệch tài liệu nữa. Phần "sẵn sàng phân công" vẫn được nói đúng chỗ — ở câu thông báo sau khi lưu, thứ phần mềm đang hiện đúng.

---

## 20. Mã của mức "Sắp hết hạn" chốt là `SAP_HET_HAN`  **✅ BA duyệt 09/08/2026**

**Vấn đề:** Cùng một mức cảnh báo thời hạn đang mang hai mã khác nhau ở các nhóm chức năng khác nhau. Nhóm Vụ việc dùng `SAP_HET` và máy chủ của nhóm đó **từ chối** mã còn lại; nhóm Báo cáo, Hỏi đáp và dữ liệu chạy thật của nhóm Chi trả dùng `SAP_HET_HAN`. Không chốt một mã thì mỗi nhóm lọc ra một tập khác nhau và không nhóm nào thống kê chung được.

**(1)** Đếm toàn thư mục `srs-v3.5/` (lượt đếm 07/08): **`SAP_HET` 15 lần** · **`SAP_HET_HAN` 9 lần**. Tỷ lệ không áp đảo ⇒ **không lấy số đếm làm căn cứ** — phải đi cây trọng tài.

**(1b)** Không phải tranh chấp tài liệu — đối tác không nêu mã.

**(2)** **Tầng 1 — quy ước dùng chung và quyết định BA — quyết định.** Phụ lục B của baseline **tự khai là nguồn chuẩn**: `srs-v3.5.md:5510` — *"**SOURCE OF TRUTH (v3.1):** Đây là bản gốc cho tất cả business rules. Mỗi FR group file chứa bản trích BR liên quan (Section 6). Khi thay đổi BR, cập nhật ở đây trước, sau đó sync sang FR files."* Và **bản định nghĩa gốc `BR-SLA-02` ở đó ghi `SAP_HET_HAN`** — `srs-v3.5.md:5626`; bản registry `srs-fr-10-quan-tri.md:2441` cũng vậy. Bản ở `srs-fr-06-chi-tra.md:1514-1523` ghi `SAP_HET` nhưng **tự dẫn chiếu về registry** — *"xem định nghĩa BR-SLA-02 (registry BR ở srs-fr-10 §6)"* ⇒ đó là bản chép, không phải bản định nghĩa. `CHANGELOG-v3-to-v3.5.md:1317` cite **BA chốt 2026-05-04** cũng ghi `SAP_HET_HAN`, và **không có quyết định nào sau đó lật lại**.

**(3)** Tầng 2 (**toàn bộ 6 bản khai ràng buộc thực thể** đều ghi `SAP_HET`: `srs-v3.5.md:1509` · `:1564` · `:2001` · `srs-fr-02-hoi-dap.md:1354` · `srs-fr-05-vu-viec.md:2031` · `srs-fr-06-chi-tra.md:1311`) đứng **sau** tầng 1 trong cây trọng tài, nên không đè được — dù đây đúng là chỗ lệch rộng nhất và là lý do phải sửa nhiều. Chốt theo `SAP_HET` sẽ là lật một quyết định BA đã ghi mà không có văn bản nào lật nó.

#### Căn cứ chi tiết

**(3) — rủi ro chuyển đổi dữ liệu: thấp.** Phần sửa nằm ở nhóm Vụ việc (ràng buộc thực thể, ô lọc, bảng ánh xạ nhãn, giá trị đang lưu), nhưng mức cảnh báo là trường **được tính lại**, không phải trường người dùng nhập — `srs-fr-05-vu-viec.md:1436` khai công việc tự động quét và tính lại mức cho vụ việc đang hoạt động. Đổi mã xong chạy lại công việc đó là đủ, không phải chuyển đổi dữ liệu thủ công.

**→ Kết luận: Loại 2 — chốt mã chuẩn toàn hệ thống là **`SAP_HET_HAN`** `[BA duyệt 2026-08-09]`, theo bản định nghĩa gốc của `BR-SLA-02` ở Phụ lục B (nơi tự khai là *SOURCE OF TRUTH* cho mọi quy tắc nghiệp vụ) và quyết định BA 2026-05-04. Dev action: Có (nhóm Vụ việc — mức Minor, đổi mã + chạy lại công việc tính mức) · Sửa đặc tả: Có (15 chỗ dùng `SAP_HET`) → Sheet: verdict `TKHSYCHTPL_03` giữ **Pass**; QA mở dòng mới cho phần đổi mã ở đợt kế tiếp.**

**Việc Dev:** Nhóm Vụ việc đổi mã mức *Sắp hết hạn* SAP_HET → SAP_HET_HAN (ràng buộc thực thể + ô lọc + giá trị đang lưu) rồi chạy lại công việc tính mức. *Nghiệm thu:* lọc *Sắp hết hạn* → máy chủ nhận SAP_HET_HAN, không trả 422.

### Phương án xử lý (cập nhật SRS)

1. Sửa **15** chỗ đang ghi `SAP_HET` về `SAP_HET_HAN`, trong đó có **ràng buộc thực thể ở 2 nơi**: `srs-v3.5.md:2001` và `srs-fr-05-vu-viec.md:2031`; các chỗ còn lại nằm ở `srs-fr-02-hoi-dap.md` (4) · `srs-fr-05-vu-viec.md` (`:1516` bảng ánh xạ nhãn, `:1644` ô lọc, và 2 chỗ khác) · `srs-fr-06-chi-tra.md` (3, gồm bảng ở `:1514-1523`) · `srs-v3.5.md` (2 chỗ còn lại).
2. **Grep lại đủ 15 vị trí ngay trước khi sửa** — số đếm trên lấy từ lượt đếm ngày 07/08, các lượt sửa xen giữa có thể làm lệch. Mẫu tìm phải loại trừ `SAP_HET_HAN` để không đếm chồng.
3. `srs-fr-06-chi-tra.md:1514-1523` — sau khi sửa, giữ nguyên câu dẫn chiếu về registry để lần sau không ai sửa lệch bản chép nữa.
4. Đồng bộ cùng lượt với mục 28 (hai việc chạm cùng một trường `muc_do_canh_bao`).

---

## 21. Thanh lọc chỉ chạy khi bấm [Tìm kiếm] — chốt thành quy ước chung `[tự khép]`

> **Gộp cụm:** mục này và **mục 30** (màn Biểu mẫu) là **cùng một quyết định thiết kế**, khác màn. Phân tích và chốt phương án một lần ở đây; mục 30 dẫn về.

**Vấn đề:** Trên các màn danh sách, người dùng chọn giá trị ở một ô lọc thì danh sách chưa đổi; phải bấm nút *Tìm kiếm* mới lọc. Đặc tả lại ghi hành vi của các ô lọc là "đổi giá trị → lọc ngay", đồng thời vẫn khai nút *Tìm kiếm* trong cùng bảng — hai câu không thể cùng đúng.

**(1)** Đặc tả **tự mâu thuẫn** ở cùng một bảng: `srs-fr-05-vu-viec.md:1644` (và 7 hàng ô lọc `:1639`→`:1645`) ghi `change → filter`, trong khi `:1646` khai *"Nút Tìm kiếm / Xóa bộ lọc — click → query / reset"*, điều kiện hiển thị *"Luôn"*. Nếu mọi ô đã lọc ngay thì nút này không còn việc.

**(1b)** Không phải tranh chấp tài liệu — đối tác không nêu, và chính đối tác cũng thao tác theo cách bấm nút.

**(2)** Hiện tượng không của riêng một màn, và **rộng hơn con số ở lượt đếm đầu**:
- `change → filter` (mũi tên Unicode): **47 lần** ở 8 tệp — `srs-fr-10` 12 · `srs-fr-05` 7 · `srs-fr-07` 6 · `srs-fr-09` 6 · `srs-fr-02` 5 · `srs-fr-08` 5 · `srs-fr-06` 4 · `srs-fr-11` 2.
- `change -> filter` (mũi tên ASCII, **cùng nghĩa, khác cách gõ** — lượt đếm đầu bỏ sót): **13 lần** — `srs-fr-12` 6 · `srs-fr-15` 4 · `srs-fr-13` 2 · `srs-fr-14` 1.
- **Tổng 60 lần**, cộng thêm các biến thể tiếng Việt cùng nghĩa (`gõ → lọc tự động`, `chọn → lọc`) ở `srs-fr-05-vu-viec.md:1831-1833` và `:1869-1871`.
- Phía đối lập: **9 màn** khai nút `[Tìm kiếm]` và **10 màn** khai `[Xóa bộ lọc]` ngay trong bảng thành phần màn hình. Riêng 3 màn nhóm IV (`srs-fr-04:1444` · `:1635` · `:1775`) **chỉ có nút, 0 lần `change → filter`** — tức đã nhất quán sẵn theo hướng khuyến nghị.

**(3)** Bắt buộc chốt một hướng. **Khuyến nghị giữ nút [Tìm kiếm]**: các màn danh sách có 4–8 ô lọc, lọc ngay mỗi lần đổi một ô sẽ bắn nhiều lượt truy vấn liên tiếp trong khi người dùng còn đang đặt điều kiện; đây cũng là cách phần mềm đang chạy ở mọi màn đã đo và là cách đối tác đang thao tác.

**→ Kết luận: Loại 2 — chốt quy ước "bấm [Tìm kiếm] mới lọc", phần mềm đã đúng. Dev action: Không · Sửa đặc tả: Có (phạm vi rộng, xem phương án) → Sheet: verdict `TKHSYCHTPL_03` và `QLBMHD_02` giữ **Pass**.**

### Phương án xử lý (cập nhật SRS)

1. **Thêm một dòng quy ước vào Phụ lục E của `srs-v3.5.md`** (đánh số tiếp sau §H8), mức BẮT BUỘC: *"Thanh lọc của màn danh sách có nút **[Tìm kiếm]** và **[Xóa bộ lọc]**. Đổi giá trị một ô lọc **không** tự lọc; danh sách chỉ đổi khi bấm [Tìm kiếm]. Màn nào cần lọc ngay khi đổi giá trị phải ghi rõ lý do tại FR đó."*
2. **Rà đủ 60 chỗ** — cả `change → filter` (47, mũi tên Unicode) lẫn `change -> filter` (13, mũi tên ASCII ở `srs-fr-12/13/14/15`) `[Codex review 2026-08-09 bắt: bản trước chỉ ghi 47, sót 13]`. Mỗi chỗ xử theo màn: màn **có** nút Tìm kiếm trong bảng thành phần → đổi hành vi thành *"bấm [Tìm kiếm] → lọc"*; màn **không có** nút → bổ sung 2 hàng nút vào bảng thành phần rồi đổi hành vi. Không được đổi hàng loạt bằng thay chuỗi: một số hàng `change → filter` là ô chuyển tab hoặc ô ngoài thanh lọc, phải mở từng chỗ đọc.
3. `srs-fr-09-bieu-mau.md:650-673` — bổ sung 2 hàng nút `[Tìm kiếm]` và `[Xóa bộ lọc]` (bảng này hiện **không khai** hai nút mà phần mềm đang có) — xem mục 30.
4. **Rào chắn với quy ước `UI-09` (giữ bộ lọc khi quay lại) — phát hiện ở lượt soi vòng 2.** `srs-v3.5.md:581` `UI-09` buộc giữ nguyên bộ lọc khi người dùng từ màn chi tiết quay về danh sách. Ghép mù với quy ước mới thì người dùng quay lại sẽ thấy bộ lọc còn nguyên mà danh sách không lọc, phải bấm `[Tìm kiếm]` lần nữa. Phải ghi kèm: *"Khi quay lại danh sách theo `UI-09`, hệ thống **tự chạy lại truy vấn** với bộ lọc đã giữ — không đòi bấm [Tìm kiếm] lại. Quy ước 'bấm mới lọc' chỉ áp cho thao tác đổi giá trị ô lọc."*
5. **Ngưỡng tách phương án:** đây là lượt sửa chạm 8 tệp; đề nghị làm thành **một đợt sửa đặc tả riêng**, không gộp vào đợt sửa của các mục còn lại.

---

## 22. Hồ sơ chưa có thời hạn xử lý không thuộc mức cảnh báo nào  **✅ BA duyệt 09/08/2026**

> **Nguyên tắc đã chốt** `[BA duyệt 2026-08-09]` — **mức cảnh báo thời hạn chỉ có nghĩa trong khoảng hồ sơ đang chạy.** Trước khi có thời hạn và sau khi hồ sơ kết thúc thì **không mang mức**: trường để trống, cột hiển thị `—`, và không lọt bất kỳ giá trị nào của ô lọc mức.
>
> Đây **không phải quy ước mới sáng tác** — nhóm Hỏi đáp đã làm đúng như vậy từ trước (`srs-fr-02-hoi-dap.md:1043`). Mục này áp nó cho nhóm **Vụ việc**; **mục 28** áp cho nhóm **Chi trả** và xử tiếp nhãn thứ 5.

**Vấn đề:** Lọc danh sách vụ việc theo mức *Bình thường* thì lọt vào cả những hồ sơ **Mới tạo** — chưa tiếp nhận nên chưa có thời hạn xử lý. Cột cảnh báo của chính những dòng đó hiện dấu `—`. Người dùng lọc ra một nhóm rồi thấy dòng không mang nhãn nhóm đó.

**(1)** Đặc tả **im lặng**: `srs-fr-05-vu-viec.md:2031` khai trường mức cảnh báo là **không bắt buộc**, mặc định `'BINH_THUONG'` ⇒ cho phép bản ghi chưa được tính mức và tự xếp vào nhóm Bình thường. `:1436` — công việc tự động **chỉ quét vụ việc đang hoạt động**, không quét hồ sơ Mới tạo. `:1656` mô tả cột chỉ có 4 mức, không nói hồ sơ chưa tính được mức thì hiện gì và thuộc nhóm lọc nào.

**(1b)** Không phải tranh chấp tài liệu — đối tác không nêu.

**(2)** Giao diện và dữ liệu **khớp nhau** (`mucDoCanhBao = BINH_THUONG`, `deadline = null`) ⇒ không phải lỗi hiển thị, mà là giá trị mặc định đang được dùng cho một trạng thái nó không mô tả.

**(3)** Nên sửa: hiển thị đã nói đúng (`—`), chỉ bộ lọc là nói sai. Để nguyên thì mọi thống kê theo mức đều cộng nhầm nhóm hồ sơ chưa chạy.

**→ Kết luận: Loại 2 — chốt nguyên tắc *mức cảnh báo chỉ có nghĩa trong vòng đời hồ sơ* `[BA duyệt 2026-08-09]`. Dev action: Có (mức Minor, 3 việc — đều ở máy chủ) · Sửa đặc tả: Có — **4 chỗ ở nhóm Vụ việc + 2 chỗ đồng bộ nhóm Hỏi đáp**, liệt kê ngay dưới → Sheet: verdict `TKHSYCHTPL_03` giữ **Pass**; QA mở dòng mới ở đợt kế tiếp.**

### Việc Dev cần làm

Hiện trạng đo được: lọc *Mức SLA = "Bình thường"* trả **38** bản ghi, trong đó **2** bản ghi ở trạng thái *Mới tạo* — chưa tiếp nhận nên **chưa có thời hạn xử lý** — vẫn lọt vào. Cột *Cảnh báo thời hạn* của chính 2 dòng đó lại hiện `—`. Tức **giao diện nói một đằng, bộ lọc nói một nẻo**.

| # | Việc | Bên | Nghiệm thu bằng |
|---|---|---|---|
| 1 | Khi tính mức cảnh báo: hồ sơ **chưa có thời hạn xử lý** thì **để trống** mức, không gán `BINH_THUONG` như hiện nay | BE | Đọc lại 2 bản ghi `VV-BTP-TW-20260731-002` và `VV-BTP-TW-20260712-002` → mức để trống, không còn `BINH_THUONG` |
| 2 | Ô lọc *Mức SLA*: hồ sơ **không có mức** không lọt vào bất kỳ giá trị nào của ô lọc | BE | Lọc *"Bình thường"* → còn **36** bản ghi, 2 dòng kia biến mất |
| 3 | **Dọn dữ liệu đang lưu:** chạy lại công việc tính mức để xoá giá trị cũ đã gán sai | BE | Không còn bản ghi nào có mức mà không có thời hạn |

**Không phải làm:** cột *Cảnh báo thời hạn* trên giao diện — nó **đã** hiện `—` đúng cho nhóm này. Phần sai chỉ nằm ở giá trị lưu và ở bộ lọc.

> **Gộp một lượt với mục 20 và 28.** Cả ba chạm cùng trường `muc_do_canh_bao`: mục 20 đổi mã `SAP_HET` → `SAP_HET_HAN`, mục 22 và 28 bỏ mặc định + sửa bộ lọc. Làm rời ba lượt là chạy lại công việc tính mức ba lần.

### Phương án xử lý (cập nhật SRS)

Nguyên tắc chốt ở **mục 28**; đây là phần áp riêng cho nhóm Vụ việc — **4 chỗ**, đều đã mở đọc:

| # | Vị trí | Sửa gì |
|---|---|---|
| 1 | `srs-fr-05-vu-viec.md:2031` — ràng buộc thực thể `VU_VIEC.muc_do_canh_bao` | Bỏ giá trị mặc định `'BINH_THUONG'`, cho phép **để trống** khi hồ sơ chưa có thời hạn hoặc đã kết thúc |
| 2 | `srs-v3.5.md:1564` — **bản sao ở baseline** của chính trường đó | Sửa y hệt. Sửa một bản là để lại lệch |
| 3 | `srs-fr-05-vu-viec.md:1656` — cột *Cảnh báo thời hạn* (hiện khai đúng 4 mức) | Bổ sung: hồ sơ **không có mức** thì hiển thị `—` |
| 4 | `srs-fr-05-vu-viec.md:1644` — ô lọc *Mức SLA* | Ghi rõ: hồ sơ không có mức **không lọt** bất kỳ giá trị nào của ô lọc |

`srs-fr-05-vu-viec.md:1436` (công việc tự động chỉ quét vụ việc đang hoạt động) **không phải sửa** — chính dòng này là căn cứ cho nguyên tắc: hồ sơ ngoài diện đang hoạt động vốn đã không được tính mức.

**Đồng bộ nhóm Hỏi đáp — 2 chỗ, chỉ ở tầng đặc tả** `[BA đồng ý mở rộng 2026-08-09]`:

| # | Vị trí | Sửa gì |
|---|---|---|
| 5 | `srs-fr-02-hoi-dap.md:1354` — ràng buộc thực thể `HOI_DAP.muc_do_canh_bao` | Bỏ mặc định `'BINH_THUONG'`, cho phép để trống |
| 6 | `srs-v3.5.md:1509` — bản sao ở baseline | Sửa y hệt |

**Không có việc Dev cho nhóm Hỏi đáp** — đã đo: màn danh sách không có ô lọc Mức SLA, và cột cảnh báo đã xử `han_xu_ly = NULL → "—"` sẵn. Chỉ ngừng gán mặc định lúc tạo bản ghi, không đổi hiển thị, không đổi bộ lọc.

> **Phạm vi nguyên tắc — đã đo nhóm Hỏi đáp `[BA yêu cầu đo 2026-08-09]`.** Trường `muc_do_canh_bao` tồn tại ở **ba** thực thể, cả ba đều mặc định `'BINH_THUONG'`: `VU_VIEC` (`srs-v3.5.md:1564`) · `HO_SO_CHI_TRA` (`:2001`) · `HOI_DAP` (`:1509`, `srs-fr-02-hoi-dap.md:1354`). Kết quả đo nhóm Hỏi đáp:
>
> | Điểm đo | Vụ việc / Chi trả | **Hỏi đáp** |
> |---|---|---|
> | Công việc tự động quét trạng thái nào | Chỉ trạng thái đang hoạt động ⇒ hồ sơ chưa tiếp nhận và đã kết thúc **không** được tính mức | **Giống** — `srs-fr-02-hoi-dap.md:967` chỉ quét `TIEP_NHAN`, `DANG_XU_LY`; `MOI` và 6 trạng thái sau đó đều ngoài diện |
> | Cột hiển thị khi chưa có thời hạn | **Chưa đặc tả** → đây là chỗ mục 22 và 28 phải bổ sung | **ĐÃ CÓ** — `srs-fr-02-hoi-dap.md:1043` ghi rõ *"Nếu `han_xu_ly = NULL` → **"—"**"*, điều kiện hiển thị *"khi có thời hạn xử lý"* |
> | Ô lọc theo Mức SLA | **Có** ⇒ hồ sơ không có mức lọt nhầm vào nhóm *Bình thường* — chính là lỗi của mục 22 | **KHÔNG CÓ** — thanh lọc `SCR-II-01` (`:1027-1034`) có 7 ô: từ khóa · lĩnh vực · trạng thái · kênh tiếp nhận · mức độ phức tạp · khoảng ngày · 2 nút. **Không có ô Mức SLA** ⇒ không có chỗ để lọt sai |
>
> ⇒ **Nhóm Hỏi đáp không có lỗi cần sửa.** Chỗ duy nhất còn giống là **giá trị mặc định `'BINH_THUONG'` ở entity** — nhưng vì không có ô lọc và cột đã xử `NULL`, giá trị đó **không lộ ra đâu cả**.
>
> **Đề xuất phạm vi:** áp nguyên tắc cho **cả ba** thực thể nhưng **chỉ ở tầng đặc tả** với Hỏi đáp — bỏ mặc định `'BINH_THUONG'` ở `srs-v3.5.md:1509` và `srs-fr-02-hoi-dap.md:1354`, để ba thực thể nhất quán. **Không phát sinh việc Dev cho nhóm Hỏi đáp** (chỉ ngừng gán mặc định lúc tạo, không đổi hiển thị, không đổi bộ lọc vì không có).
>
> **Phát hiện đáng chú ý hơn:** cách Hỏi đáp xử lý (`:1043`) **chính là nguyên tắc** mà mục 22 và 28 đang đề xuất. Vậy đây **không phải quy ước mới** — nó là **khuôn đã có sẵn ở một nhóm, nay áp cho hai nhóm còn lại**. Điều này hạ rủi ro của mục 22 + 28 xuống đáng kể: không phải sáng tác quy tắc, chỉ đồng bộ theo chỗ đã làm đúng.

---

## 23. Câu thông báo sau khi cập nhật kết quả hỗ trợ  **✅ BA duyệt 09/08/2026**

**Vấn đề:** Người được phân công cập nhật kết quả hỗ trợ, hệ thống báo *"Đã cập nhật kết quả"*. Phiếu kiểm thử ghi kỳ vọng *"Đã cập nhật kết quả hỗ trợ"* — lệch một chữ.

**(1)** Đặc tả **im lặng**: `srs-fr-05-vu-viec.md:1100-1114` (§Processing và §Hậu điều kiện của FR-V.I-15) không có dòng nào quy định chữ hiển thị sau khi lưu; bảng thông báo riêng của màn `:1773-1785` không có dòng cho thao tác này.

**(1b)** Không phải tranh chấp tài liệu — đối tác chỉ phản ánh vế thông báo cho cán bộ nghiệp vụ, chữ trên màn là vế đối tác không nêu.

**(2)** Lệch đúng một chữ so với phiếu, và cũng lệch với tên hộp thoại của chính chức năng — hộp thoại tên *"Cập nhật kết quả hỗ trợ"*.

**(3)** Không bắt buộc, nhưng **khuyến nghị đổi theo phiếu**: sửa một chuỗi hiển thị thì rẻ hơn nhiều so với đề nghị đối tác sửa kỳ vọng, và câu mới khớp luôn tên hộp thoại.

**→ Kết luận: Loại 2 — chốt câu **"Đã cập nhật kết quả hỗ trợ"** `[BA duyệt 2026-08-09]`, khớp tên hộp thoại của chính chức năng và khớp phiếu kiểm thử. Dev action: Có (mức Trivial — sửa một chuỗi hiển thị) · Sửa đặc tả: Có → Sheet: verdict `CNKQHT_07` giữ **Pass**; QA mở dòng mới ở đợt kế tiếp.**

**Việc Dev:** Đổi chuỗi hiển thị "Đã cập nhật kết quả" → "Đã cập nhật kết quả hỗ trợ". *Nghiệm thu:* bấm Cập nhật kết quả → toast đúng câu mới.

### Phương án xử lý (cập nhật SRS)

`srs-fr-05-vu-viec.md:1773-1785` (bảng *Thông báo riêng `SCR-V.I-03`*) — thêm một hàng: *"| Cập nhật kết quả hỗ trợ | Toast success | **"Đã cập nhật kết quả hỗ trợ"** |"*. Đây là bảng đang thiếu hẳn dòng cho thao tác này, nên bổ sung chứ không sửa dòng cũ.

**Không phải rà lại phiếu kiểm thử.** Khác mục 6 (câu hết phiên hiện ở mọi màn, đổi thì phải soát các phiếu đang lấy câu cũ làm chuẩn), câu này chỉ thuộc **một** thao tác, và câu mới **trùng đúng thứ phiếu `CNKQHT_07` đang ghi** — sửa xong là phiếu khớp hơn chứ không lệch đi.

---

## 24. Tệp của lần cập nhật kết quả trước được giữ lại  **✅ BA duyệt 09/08/2026**

**Vấn đề:** Cập nhật kết quả hỗ trợ lần thứ hai mà không đính tệp mới thì tệp của lần đầu vẫn còn. Đặc tả không nói tệp cũ được giữ, bị thay hay bị xóa, nên chưa có thước đo.

**(1)** Đặc tả **im lặng**: `srs-fr-05-vu-viec.md:1094-1096` chỉ khai tệp kết quả là đầu vào **tùy chọn**; `:1104-1105` (*"Tạo/cập nhật KET_QUA_VU_VIEC"*, *"Lưu tài liệu kết quả"*) không mô tả nhánh "không có tệp mới".

**(1b)** Không phải tranh chấp tài liệu — đối tác không nêu.

**(2)** Hiện trạng là **tích lũy**: nội dung được thay bằng bản mới, tệp thì cộng dồn qua các lần.

**(3)** **Khuyến nghị giữ hiện trạng.** Tệp kết quả là chứng cứ đã nộp; xóa tự động khi người dùng chỉ sửa chữ là mất dữ liệu ngoài ý muốn. Cách này cũng khớp cách lưu vết của các nhóm chức năng khác.

**→ Kết luận: Loại 2 — chốt **tệp kết quả tích lũy qua các lần cập nhật** `[BA duyệt 2026-08-09]`. Kèm theo: đã đo và xác nhận **đặc tả chưa có đường xóa tệp kết quả**, nên phải bổ sung — nếu không, "tích lũy" thành "không bao giờ gỡ được". Dev action: **Có** (bổ sung đường xóa tệp ở Nhóm 6, trừ khi phép đo xác nhận màn đã có) · Sửa đặc tả: Có → Sheet: verdict `CNKQHT_07` giữ **Pass**; QA mở dòng mới ở đợt kế tiếp.**

**Việc Dev:** Bổ sung đường **xóa từng tệp kết quả** ở Nhóm 6 (nếu phép đo tay xác nhận màn chưa có). *Nghiệm thu:* vụ đang xử lý có tệp cũ → mở form Cập nhật, tệp cũ hiện kèm nút xóa.

### Phương án xử lý (cập nhật SRS)

1. `srs-fr-05-vu-viec.md:1104-1105` — bổ sung: *"Tệp kết quả **tích lũy** qua các lần cập nhật. Lần cập nhật sau không đính tệp mới thì các tệp đã nộp trước đó được giữ nguyên; muốn bỏ một tệp thì xóa đúng tệp đó."*

**Đã đo đường xóa tệp `[BA yêu cầu đo 2026-08-09]` — đặc tả CHƯA CÓ, nhưng khuôn thì có sẵn ngay trong cùng màn:**

| Nơi | Có đường xóa tệp không |
|---|---|
| `srs-fr-05-vu-viec.md:1695` — **Accordion 3** (hồ sơ đính kèm của vụ việc), cùng màn `SCR-V.I-03` | **CÓ** — *"| 16 | accordion-3 | Danh sách file đã upload | Table nhỏ | Tên file, Kích thước, Ngày upload, **Nút [Xóa]** | — | Khi có file |"* |
| `srs-fr-05-vu-viec.md:1732` — **Accordion 6** (Kết quả Hỗ trợ) | **KHÔNG** — chỉ liệt kê `file_ket_qua`, không khai bảng tệp, không khai nút Xóa |
| `srs-fr-05-vu-viec.md:1094-1114` — FR-V.I-15 §Inputs + §Processing | **KHÔNG** — 7 bước, chỉ có bước 4 *"Lưu tài liệu kết quả"*, không có bước xóa |

Grep toàn nhóm Vụ việc chuỗi *"xóa tệp / xóa file"*: **đúng 1 kết quả**, chính là `:1695` của Accordion 3.

2. `srs-fr-05-vu-viec.md:1732` — Accordion 6: bổ sung bảng tệp kết quả kèm **nút [Xóa]**, **chép đúng khuôn Accordion 3** ở `:1695` (Tên file · Kích thước · Ngày upload · Nút [Xóa], hiện khi có file). Không cần sáng tác mẫu mới.
3. `srs-fr-05-vu-viec.md:1104-1114` — FR-V.I-15 §Processing: thêm khối *"Xóa tệp kết quả"*, chép khuôn đã có ở `srs-fr-12-tv-chuyen-sau.md:931-937`: kiểm quyền → kiểm tệp thuộc đúng bản ghi → xóa khỏi kho → cập nhật danh sách tệp → ghi nhật ký. Quyền xóa theo đúng quyền cập nhật kết quả (người được phân công).

### Kết quả đo phần mềm `[đo 2026-08-09, bản dựng V1.0.10, tài khoản cbnv_tw]`

Mở màn chi tiết vụ việc thật, đo hai chế độ:

| Chế độ | Vụ đo | Nhóm 6 "Kết quả hỗ trợ" hiển thị gì |
|---|---|---|
| **Đọc** (vụ đã đóng — *Đã đánh giá*) | `VV-BTP-TW-20260806-003` (có 1 tệp kết quả đã lưu) | Tệp `qa-cnkqht07-ket-qua.pdf` **chỉ có nút "Xem"** — KHÔNG có nút Xóa, KHÔNG có nút Tải. Không có nút *Cập nhật kết quả* (vụ đã đóng) |
| **Nhập** (vụ đang xử lý) | `DDD-VV-002`, `DDD-VV-003` | Có nút *Cập nhật kết quả* → form gồm ô *Nội dung*, **vùng tải tệp kiểu kéo-thả (Ant Upload)**, ô *Ghi chú*. Cả hai vụ **chưa có tệp kết quả nào** |

**Chưa dựng được đúng tình huống của câu hỏi.** Câu hỏi cần: **vụ đang xử lý + đã có tệp kết quả từ lần trước** → mở form Cập nhật xem tệp cũ có hiện lại kèm nút xóa không. Seed data không có vụ nào như vậy (vụ có tệp thì đã đóng; vụ đang xử lý thì chưa có tệp), và không tự tạo được vì `Ant Upload` chặn thao tác đính tệp qua automation (báo uploaded nhưng không nhận — có `beforeUpload` validate). Không mutate dữ liệu nào (chỉ mở form, không bấm Xác nhận).

**Kết luận đo:**
- **Chế độ đọc: KHÔNG có đường xóa tệp kết quả** — khớp đặc tả (Accordion 6 không khai nút Xóa). Nhưng đây là chế độ đọc, đúng ra không cho xóa.
- **Chế độ nhập:** form dùng Ant Upload chuẩn. Tệp *vừa chọn trong phiên soạn* thì Ant Upload luôn cho gỡ; nhưng **tệp đã lưu từ lần trước có hiện lại để xóa hay không thì chưa xác nhận được** — chính là điểm mấu chốt của phiếu.

**→ Dev action giữ "Có" (việc 2 + 3).** Chưa có bằng chứng nào cho thấy form Cập nhật hiện lại tệp đã lưu kèm nút xóa; chế độ đọc thì chắc chắn không có đường xóa. Nếu QA đo tay (đính tệp thật rồi mở lại form) xác nhận **đã** cho xóa tệp cũ thì Dev action về **Không**, chỉ còn sửa đặc tả.

> **Điểm treo thu hẹp còn một câu:** trên vụ **đang xử lý đã có tệp kết quả**, form *Cập nhật kết quả* có hiện lại tệp cũ kèm nút xóa không. Cần QA đính tệp thật (automation không làm được) rồi mở lại form. Đã ghi ở bảng điểm treo.

---

## 25. Cán bộ nghiệp vụ vẫn được chấm khi vụ việc đã ở "Đã đánh giá"  **✅ BA duyệt 09/08/2026 — Hướng A**

**Vấn đề:** Một vụ việc có thể được chấm bởi hai bên độc lập — cán bộ nghiệp vụ và doanh nghiệp, mỗi bên đúng một lần. Lần chấm đầu tiên đẩy vụ việc sang *Đã đánh giá*. Nếu doanh nghiệp chấm trước thì cán bộ **mất đường vào**, không còn nút nào để mở phần đánh giá — dù ràng buộc dữ liệu vẫn còn chỗ trống cho đánh giá của cán bộ.

**(1)** Đặc tả **tự mâu thuẫn**, và mâu thuẫn nằm gọn trong chế độ cán bộ:
- Cho phép: `srs-fr-05-vu-viec.md:1197` — *"| PRE-02 | VV ở trạng thái HOAN_THANH hoặc DA_DANH_GIA |"*; `:1198` — *"Role ∈ {CB_NV, DN}"*; `:1734` — Accordion 8 hiện *"Khi VV ở HOAN_THANH hoặc DA_DANH_GIA"*; và **§Processing đã lường sẵn ca đánh giá thứ hai** — `:1222` *"| 8 | Chuyển VV → DA_DANH_GIA (**chỉ lần đánh giá đầu tiên; nếu VV đã DA_DANH_GIA thì giữ nguyên**) |"*.
- Chặn trùng đã có sẵn, **không cần đặt ra điều kiện mới**: `:1219` — *"| 5 | Check duplicate: nếu đã tồn tại bản ghi DANH_GIA_VU_VIEC cho cùng VV và cùng loại người đánh giá → ERR-DG-VV-03 |"*; `:1241` — *"| E3 | Đã đánh giá | ERR-DG-VV-03 | 'Bạn đã đánh giá vụ việc này rồi' |"*.
- Chặn: `:1751` — bảng nút theo trạng thái chỉ có **một** dòng cho chức năng đánh giá, *"| HOAN_THANH | [Đánh giá]… |"*, **không có** dòng nào cho `DA_DANH_GIA` ⇒ accordion phải hiện nhưng không có nút nào mở nó.
- Đối chứng: phía doanh nghiệp **không** mâu thuẫn — `:1809` và `:1811` đều nói cả hai trạng thái.
- Ràng buộc dữ liệu dự trù đủ 2 đánh giá: `:2108` — *"UNIQUE (vu_viec_id, loai_nguoi_danh_gia)"*.

**(1b)** Không phải tranh chấp tài liệu.

**(2)** Kịch bản hỏng cụ thể: doanh nghiệp chấm trước → vụ việc sang *Đã đánh giá* → cán bộ mất đường vào. Chiều ngược lại thì doanh nghiệp vẫn vào được.

**(3)** Bắt buộc: một trong hai đánh giá bị mất hẳn tùy vào ai bấm trước — đây là mất dữ liệu nghiệp vụ, không phải bất tiện giao diện.

**→ Kết luận: Loại 2 — chốt **Hướng A: hai bên (CB NV và DN) đánh giá độc lập, mỗi bên một lần, thứ tự bất kỳ; `DA_DANH_GIA` chỉ đánh dấu "đã có ít nhất một đánh giá"** `[BA duyệt 2026-08-09]`. Bảng nút + máy trạng thái thiếu nhánh cho bên chấm sau, cần bổ sung rồi Dev mở đường vào. Dev action: Có (mức Major, ghép cùng lần sửa `BUG-VV-DGKQHTVV-01`) · Sửa đặc tả: Có → Sheet: verdict `DGKQHTVV_01` giữ **Reopen** (đang Reopen vì nhánh doanh nghiệp, mục này không đổi verdict đó).**

**Việc Dev:** Mở nút **Đánh giá** khi vụ việc ở DA_DANH_GIA và người đang xem **chưa** chấm. *Nghiệm thu:* DN chấm trước → CB NV vẫn vào chấm được; CB NV đã chấm rồi thì bị chặn (ERR-DG-VV-03).

### Phương án xử lý (cập nhật SRS)

**Máy trạng thái thiếu HAI nhánh, không phải một — phát hiện khi BA hỏi lại nghiệp vụ 09/08.** Cả ba bản (mermaid + bảng ở FR-05, và bản sao baseline) hiện chỉ ghi đúng một mũi tên *"HOAN_THANH → DA_DANH_GIA : **CB NV** đánh giá"*, tức mô tả thiên một chiều. Theo Hướng A phải sửa:

1. **Bảng nút hành động** `srs-fr-05-vu-viec.md:1751` — thêm dòng: *"| DA_DANH_GIA | [Đánh giá] | CB NV/DN | Mở Accordion 8. Chỉ hiện khi người đang xem **chưa** đánh giá vụ việc này (theo `loai_nguoi_danh_gia`). Gửi → giữ nguyên DA_DANH_GIA |"*. Điều kiện "chưa đánh giá" không phải quy tắc mới — chép lại chốt chặn đã có ở `:1219` / `:1241`.
2. **Nhánh 1 — sửa transition hiện có** cho khỏi thiên một chiều: *"HOAN_THANH → DA_DANH_GIA : **CB NV hoặc DN** đánh giá (lần đầu)"*. Hiện chỉ ghi *"CB NV đánh giá"* — nếu DN chấm trước thì transition này không mô tả được.
3. **Nhánh 2 — thêm transition tự lặp** cho bên chấm sau: *"DA_DANH_GIA → DA_DANH_GIA : bên còn lại đánh giá (UC67), điều kiện `loai_nguoi_danh_gia` chưa có bản ghi; lưu đánh giá + audit, **giữ nguyên trạng thái**"*.
4. **Chú thích badge** `srs-fr-05-vu-viec.md:2277` — hiện ghi *"CB NV đã đánh giá chất lượng HTPL"*, nới thành *"đã có ít nhất một đánh giá (CB NV hoặc DN); có thể còn chờ bên kia đánh giá"* — để tên trạng thái không bị hiểu là "cả hai đã xong".
5. **Đồng bộ đủ 4 vị trí máy trạng thái:** sơ đồ mermaid `srs-fr-05-vu-viec.md:2255` · bảng `:2297` · bản sao baseline mermaid `srs-v3.5.md:6044` · bảng `:6065`. Áp cả nhánh 1 và nhánh 2 vào mỗi vị trí. Sửa một bản là để lại lệch ở ba bản kia.

> **Ghi rõ để lượt sau không hiểu nhầm:** `DA_DANH_GIA` = *"đã có **ít nhất một** đánh giá"*, KHÔNG phải "cả hai đã xong". Tên trạng thái này là nguồn gốc của chính hiểu nhầm mà đối tác và người soạn phiếu đều mắc.

---

## 26. Đánh giá một vụ việc không làm đổi điểm trung bình của tư vấn viên `[tự khép]`

**Vấn đề:** Hai dòng trong cùng một chức năng nói ngược nhau về việc chấm một vụ việc có kéo theo cập nhật điểm trung bình của tư vấn viên hay không, nên không có thước đo để chấm.

**(1)** Đặc tả **tự mâu thuẫn**: `srs-fr-05-vu-viec.md:1233` (§Hậu điều kiện) — *"Điểm TVV được cập nhật"*; `:1223` (§Processing bước 9) — *"…nguồn dữ liệu là `DANH_GIA_SAU_VU_VIEC`…, **không phải** `DANH_GIA_VU_VIEC`. UC67 chỉ tạo `DANH_GIA_VU_VIEC`; trigger cập nhật điểm TVV nằm ở module FR-IV"*.

**(1b)** Không phải tranh chấp tài liệu.

**(2)** **Bên thứ ba phân xử:** đã mở trọn `FR-IV-CROSS-01` (`srs-fr-04-chuyen-gia-tvv.md:940-965`) — bước 1: *"Trigger sau khi tạo **DANH_GIA_SAU_VU_VIEC** mới (nguồn đánh giá DN…)"*; bước 2 tính trung bình *"từ tất cả DANH_GIA_SAU_VU_VIEC của TVV"*. ⇒ `:1223` đúng, `:1233` là câu hậu điều kiện chép khuôn.

**(3)** Không phải chọn theo ý muốn: cơ chế tính điểm đã được đặc tả đầy đủ ở một FR khác và không lấy nguồn từ `DANH_GIA_VU_VIEC`.

**→ Kết luận: Loại 2 — bỏ dòng hậu điều kiện sai. Dev action: Không · Sửa đặc tả: Có → Sheet: verdict `DGKQHTVV_01` không đổi.**

### Phương án xử lý (cập nhật SRS)

1. `srs-fr-05-vu-viec.md:1233` — bỏ dòng *"Điểm TVV được cập nhật"*, thay bằng một câu dẫn chiếu: *"Điểm trung bình của tư vấn viên KHÔNG đổi ở chức năng này — xem FR-IV-CROSS-01, nguồn `DANH_GIA_SAU_VU_VIEC`."*
2. **Điểm treo:** hệ thống đang có **hai** thực thể đánh giá (`DANH_GIA_VU_VIEC` và `DANH_GIA_SAU_VU_VIEC`) với hai luồng nhập khác nhau. Đề nghị BA rà lại ở một lượt riêng xem có thực sự cần cả hai không — không chặn mục này.

---

## 27. Thứ tự sắp xếp mặc định của danh sách Tư vấn viên  **✅ BA duyệt 09/08/2026 — DG-06 (ngày cập nhật)**

**Vấn đề:** Đối tác kỳ vọng danh sách tư vấn viên mặc định sắp theo *ngày công nhận* mới nhất trước. Phần mềm đang sắp theo *ngày tạo bản ghi*. Phiếu hỏi kết luận "đặc tả im lặng" — **kết luận đó sai**.

**Bóc ý con `QLTVV_02` — case gộp 5 vế:** 4 vế *(không tràn/đè · hiển thị điểm đồng nhất · nút thao tác không xuống dòng · mặc định 20 mục/trang)* **đã hết lỗi** trên lượt đo 06/08, không tranh chấp. Mục này xử vế thứ 5 — thứ đang giữ verdict của cả phiếu.

**(1)** Đặc tả **KHÔNG im lặng**. Có quy ước dùng chung ở baseline: `srs-v3.5.md:960` — *"| DG-06 | Sắp xếp mặc định | **Theo thời gian cập nhật mới nhất** |"*, nằm trong bảng *Quy tắc dữ liệu chung* (DG-01…DG-08) áp cho toàn hệ thống. Phiếu hỏi chỉ tra trong `srs-fr-04-chuyen-gia-tvv.md` nên không thấy — đúng loại lỗi mà quy trình đã cảnh báo: quy ước chung nằm ở `srs-v3.5.md`, không nằm ở tệp FR module.

**(1b)** `.docx` không mô tả thứ tự mặc định của danh sách này ⇒ kỳ vọng "ngày công nhận" không có căn cứ tài liệu.

**(2)** **Nhưng số đếm KHÔNG áp đảo** — lượt đếm lại đầy đủ (lớp soi độc lập bổ sung 2 chỗ mà lượt đầu bỏ sót): **ngày cập nhật 3 chỗ** (`srs-fr-05-vu-viec.md:1665` · `srs-fr-06-chi-tra.md:1081` · `srs-fr-07-doanh-nghiep.md:448`) · **ngày tạo 3 chỗ** (`srs-fr-08-danh-gia.md:908` · `srs-fr-12-tv-chuyen-sau.md:1145` · `srs-fr-02-hoi-dap.md:1044`) · ngày đăng ký 1 · thứ tự/tên 2 · **ngày công nhận 0**. Tỷ lệ 3–3 ⇒ theo quy trình, số đếm này **không đủ làm căn cứ**.

**(3)** Và bản thân `DG-06` có **ba điểm yếu** phải vá cùng lượt — xem `#### Căn cứ chi tiết`. Điều duy nhất chắc chắn: **kỳ vọng của đối tác (ngày công nhận) không có căn cứ ở bất kỳ đâu** — 0 chỗ trong toàn bộ đặc tả, và `.docx` cũng không mô tả thứ tự cho danh sách này.

#### Căn cứ chi tiết

**(3) — ba điểm yếu của `DG-06`, đều phải vá:**
1. **Không có mệnh đề phạm vi.** Các quy ước cùng bảng thì có: `UI-09` ghi *"Áp cho mọi màn danh sách"*, `DG-08` ghi *"Áp cho mọi trường số điện thoại toàn hệ thống"*. Riêng `DG-06` không ghi gì.
2. **Chưa tệp FR nào dẫn chiếu.** Grep `DG-06` toàn bộ 18 tệp ra **đúng 1 kết quả** — chính dòng `srs-v3.5.md:960`.
3. **Có một dòng baseline nói ngược.** `srs-v3.5.md:721` — *"Danh sách sắp xếp **mới nhất trước theo thời điểm tạo** (BR-DATA-07)"*. **Nhưng dòng này viện dẫn sai**: `BR-DATA-07` ở `srs-v3.5.md:5571` chỉ nói về **phân trang** (*"Mọi danh sách sử dụng phân trang. Default: 20 rows/page…"*), không có chữ nào về thứ tự. ⇒ `:721` là một khẳng định không có nguồn, yếu hơn `DG-06` vốn là quy ước có mã định danh.

**→ Kết luận: Loại 2 — chốt **ngày cập nhật mới nhất trước theo `DG-06`** `[BA duyệt 2026-08-09]`. Phần mềm hiện sắp theo ngày tạo nên phải sửa. Dev action: **Có** (mức Minor) · Sửa đặc tả: Có → Sheet: KHÔNG đổi trạng thái (đang treo verdict; QA chấm lại sau khi Dev sửa).**

**Việc Dev:** Danh sách Tư vấn viên sắp theo **ngày cập nhật giảm dần** (hiện đang theo ngày tạo). *Nghiệm thu:* mở danh sách chưa đụng bộ lọc → thứ tự theo ngày cập nhật mới nhất trước.

> **Lịch sử:** QA đề xuất *im lặng* → phiếu đảo thành *DG-06 (ngày cập nhật)* → BA cân nhắc *ngày công nhận theo đối tác* 09/08 → BA quay lại *DG-06* 09/08. Chốt cuối: **ngày cập nhật**.

> Chốt theo `DG-06` nên **không** phải ghi ngoại lệ tại FR — màn này theo đúng quy ước chung. Vẫn phải vá ba điểm yếu của chính `DG-06` ở trên (thiếu phạm vi, chưa FR nào dẫn chiếu, dòng `:721` nói ngược), nếu không vòng UAT sau lại mở đúng chỗ này.

> **Phản hồi gửi đối tác:**
> **[Lý do]** Theo quy ước dữ liệu chung của phần mềm, mọi danh sách mặc định sắp theo thời gian cập nhật mới nhất trước, không phải theo ngày công nhận. Danh sách tư vấn viên hiện đang sắp theo một tiêu chí khác với quy ước này và sẽ được chỉnh lại.
> **[Nhận định]** Đề nghị Quý đơn vị cập nhật kết quả mong đợi thành *"mặc định sắp theo thời gian cập nhật mới nhất trước, 20 bản ghi mỗi trang"*.

### Phương án xử lý (cập nhật SRS)

1. `srs-v3.5.md:960` — bổ sung mệnh đề phạm vi cho `DG-06`, viết theo đúng khuôn của `UI-09` / `DG-08`: *"Áp cho mọi màn danh sách, trừ màn có quy định riêng ghi tại FR."*
2. `srs-v3.5.md:721` — sửa hoặc bỏ: câu này nói *"theo thời điểm tạo"* và viện `BR-DATA-07`, trong khi `BR-DATA-07` (`:5571`) chỉ nói về phân trang. Để nguyên là giữ một dòng chọi thẳng `DG-06`.
3. `srs-fr-04-chuyen-gia-tvv.md:243-247` (FR-IV-02 §Processing) — bổ sung một bước: *"Sắp xếp mặc định theo `DG-06`. Bản ghi chưa từng cập nhật lấy theo thời gian tạo."* Câu sau là cần thiết: trên màn hiện có bản ghi bỏ trống ngày công nhận, không chốt chỗ đứng của nhóm trống thì vòng sau vẫn tranh chấp.
4. **Rà 3 chỗ đang ghi "ngày tạo"** (`srs-fr-08-danh-gia.md:908` · `srs-fr-12-tv-chuyen-sau.md:1145` · `srs-fr-02-hoi-dap.md:1044`): mỗi chỗ hoặc sửa theo `DG-06`, hoặc ghi rõ là ngoại lệ có lý do. Không để lửng — đó chính là thứ tạo ra tỷ lệ 3–3 hiện nay.

---

## 28. Hồ sơ đã kết thúc không hiển thị mức cảnh báo thời hạn  **✅ BA duyệt 09/08/2026 — theo nguyên tắc mục 22**

> **Không phải quyết định riêng** — cùng nguyên tắc *mức cảnh báo chỉ có nghĩa trong vòng đời hồ sơ* đã duyệt ở **mục 22** `[BA duyệt 2026-08-09]`. Mục này chỉ áp nguyên tắc đó cho nhóm **Chi trả** (hồ sơ đã kết thúc) và bỏ nhãn thứ 5; cả hai đều là hệ quả trực tiếp, không mở lại quyết định.

**Vấn đề:** Cột *SLA* trên danh sách chi trả chi phí đang hiện **5 loại nhãn**, trong khi mô hình cảnh báo chỉ có 4 mức. Nhãn thứ 5 là *"Đã hoàn thành"*, gán cho 4 hồ sơ ở trạng thái **Đã thanh toán, Từ chối, Hủy** — trong đó gọi một hồ sơ **đã Hủy** là *"Đã hoàn thành"* là sai nghĩa. Dữ liệu của chính 4 hồ sơ đó lại đang lưu mức *Bình thường*, tức giao diện không hiện thứ dữ liệu đang mang.

| Trạng thái hồ sơ | Cột SLA đang hiện | Dữ liệu đang lưu | Khuyến nghị |
|---|---|---|---|
| Đang kiểm tra, còn hạn | "Bình thường · còn 10 ngày LV" | `BINH_THUONG` | giữ nguyên |
| Đang kiểm tra, trễ | "Quá hạn nghiêm trọng · 11 ngày LV" | `QUA_HAN_NGHIEM_TRONG` | giữ nguyên |
| **Mới tạo, chưa có thời hạn** (mục 22) | "Bình thường" khi lọc, `—` ở cột | `BINH_THUONG` | `—`, không lọt mức nào |
| **Đã thanh toán / Từ chối / Hủy** | **"Đã hoàn thành"** | `BINH_THUONG` | `—`, không lọt mức nào |

**(1)** Đặc tả **im lặng**: `BR-SLA-02` (`srs-fr-06-chi-tra.md:1514-1523`) định nghĩa đúng **4 mức** và kết bằng *"Nếu không thỏa điều kiện nào thì hiển thị 'Bình thường'"*; `:1058` (thành phần #16 của SCR-V.II-01) khai đúng 4 mức, điều kiện hiển thị *"Luôn"*; `:1311` ràng buộc trường chỉ nhận 4 giá trị. **Không dòng nào** nói cột này hiện gì khi hồ sơ đã kết thúc.

**(1b)** Không phải tranh chấp tài liệu — đối tác không nêu điểm này; hai vế đối tác nêu (cột không giống thiết kế, dữ liệu tràn cột) **đều đã hết lỗi** trên V1.0.8.

**(2)** Quyết định BA ngày **2026-07-24** cho chính mã phiếu này chỉ chốt tên cột *SLA* và bốn nhãn rời kèm số ngày, **không nhắc** hồ sơ đã kết thúc.

**(3)** Bắt buộc chốt: cột đang có một nhãn nằm ngoài đặc tả nên QA không chấm Pass được, và dòng phiếu đang treo.

**→ Kết luận: Loại 2 — áp nguyên tắc đã duyệt ở mục 22 cho nhóm Chi trả + bỏ nhãn *"Đã hoàn thành"* `[BA duyệt 2026-08-09]`. Dev action: Có (mức Minor) · Sửa đặc tả: Có → Sheet: KHÔNG đổi trạng thái. **Gộp một lượt Dev với mục 20 + 22** — cùng chạm trường `muc_do_canh_bao`.**

**Việc Dev:** Nhóm Chi trả: bỏ mặc định BINH_THUONG cho hồ sơ **đã kết thúc**, bỏ nhãn thứ 5 "Đã hoàn thành" khỏi cột SLA, dọn 4 hồ sơ đang mang giá trị sai. *Nghiệm thu:* hồ sơ đã Hủy → cột SLA hiện "—". **Gộp một lượt với mục 20 + 22.**

> **Phản hồi gửi đối tác:**
> **[Lý do]** Hai điểm Quý đơn vị phản ánh ở phiếu này — cột hiển thị không giống thiết kế và dữ liệu tràn sang cột Ngày nộp — **đều đã được xử lý** trên bản dựng mới. Phần mềm hiện còn một điểm khác đang được rà soát nội bộ về cách hiển thị cột cảnh báo thời hạn với hồ sơ đã kết thúc; điểm này không thuộc nội dung Quý đơn vị nêu.
> **[Nhận định]** Đề nghị Quý đơn vị kiểm thử lại hai điểm đã nêu sau khi bản dựng mới được triển khai lên môi trường nghiệm thu. Kết quả mong đợi giữ nguyên, không cần sửa.

### Phương án xử lý (cập nhật SRS)

**Nguyên tắc khuyến nghị — mức cảnh báo thời hạn chỉ có nghĩa trong khoảng hồ sơ đang chạy:**

1. Hồ sơ **chưa có thời hạn xử lý** (chưa tiếp nhận) và hồ sơ **đã kết thúc** (Đã thanh toán / Từ chối / Hủy, và tương ứng ở nhóm Vụ việc) đều **không mang mức cảnh báo**: trường để trống, cột hiển thị `—`, và **không lọt** bất kỳ giá trị nào của bộ lọc mức.
2. Bỏ nhãn thứ 5 *"Đã hoàn thành"* khỏi cột SLA — trạng thái hồ sơ đã có cột riêng, không cần nhắc lại ở cột cảnh báo, và nhãn đó sai nghĩa với hồ sơ Từ chối / Hủy.
3. Ghi nguyên tắc trên vào `BR-SLA-02` (`srs-fr-06-chi-tra.md:1514-1523`) — thay câu *"Nếu không thỏa điều kiện nào thì hiển thị 'Bình thường'"* bằng *"Chỉ tính mức khi hồ sơ đã có thời hạn xử lý và chưa kết thúc; ngoài khoảng đó thì không có mức"*.
4. Đồng bộ **3 bản sao**: `srs-fr-06-chi-tra.md:1058` (thành phần #16) · `:1311` (ràng buộc trường) · `srs-fr-05-vu-viec.md:2031` + `:1656` (nhóm Vụ việc — mục 22). Trường `muc_do_canh_bao` bỏ giá trị mặc định `'BINH_THUONG'`, để trống khi chưa tính.
5. **Câu hỏi liên đới đã có lời giải:** 4 hồ sơ đã kết thúc đang mang `BINH_THUONG` trong dữ liệu — theo nguyên tắc trên thì giá trị đó **sai**, phải để trống. Dev xử cùng lượt.
6. **Bổ sung độ phủ nhóm Vụ việc — Codex review 2026-08-09 bắt:** nguyên tắc phủ cả *chưa có hạn* lẫn *đã kết thúc*, nhưng phần áp cho nhóm Vụ việc (mục 22) mới xử ca *chưa có hạn*. Phải thêm: **hồ sơ Vụ việc ở trạng thái kết thúc (`HOAN_THANH`, `DA_DANH_GIA`, `TU_CHOI`, `HUY`) cũng để trống mức** — công việc tự động `srs-fr-05-vu-viec.md:1436` vốn không quét các trạng thái này nên chúng đang giữ mức cũ (ví dụ *Quá hạn* cho vụ đã hoàn thành, vô nghĩa). Áp cùng chỗ với ca chưa-có-hạn ở bốn vị trí đã liệt kê.

> **Rào chắn với `BR-SLA-03` (thông báo khi chuyển mức) — phát hiện ở lượt soi vòng 2.** `srs-v3.5.md:5627`, `srs-fr-05-vu-viec.md:2444` và `srs-fr-02-hoi-dap.md:1652` đều quy định *"khi chuyển mức cảnh báo thì gửi thông báo"*. Nếu áp nguyên tắc trên mà không rào, thì mỗi hồ sơ **kết thúc** đều là một lần "chuyển mức" (từ một mức về trống) và sẽ bắn thông báo cảnh báo thời hạn cho cán bộ ngay lúc hồ sơ vừa đóng — đúng lúc không còn gì để cảnh báo. Phải ghi kèm vào `BR-SLA-03`: *"Việc xoá mức khi hồ sơ chưa có thời hạn hoặc đã kết thúc **không** tính là chuyển mức, không gửi thông báo."*
7. **Kết hợp với mục 20:** mã chuẩn chốt là `SAP_HET_HAN` — nhóm Chi trả đang chạy đúng mã đó, nhóm Vụ việc phải đổi. Hai việc chạm cùng một trường `muc_do_canh_bao`, đề nghị Dev làm chung một lượt.

---

## 29. Bốn ô lọc trên màn Biểu mẫu đều chỉ hiện chữ "Tất cả"  **✅ BA duyệt 09/08/2026**

**Vấn đề:** Thanh lọc màn Biểu mẫu có 4 ô, cả 4 đều hiện đúng chữ *Tất cả*, không ô nào có nhãn. Người dùng phải mở từng ô mới biết ô nào lọc theo thư mục, lĩnh vực, loại hình hay định dạng.

**(1)** Đặc tả **im lặng**: `srs-fr-09-bieu-mau.md:654` khai thành phần *"Lọc lĩnh vực / loại hình / thư mục / định dạng"* kiểu `select`, không nói nhãn hiển thị của từng ô.

**(1b)** Không phải tranh chấp tài liệu — đối tác không nêu.

**(2)** Bốn ô giống hệt nhau về mặt thị giác ⇒ người dùng không phân biệt được ô nào là ô nào nếu chưa mở.

**(3)** **Khuyến nghị chốt là bắt buộc.** Đây là khiếm khuyết dùng được thật, không phải sở thích trình bày: bốn ô không nhãn nằm cạnh nhau thì không thao tác được nếu chưa quen màn.

**→ Kết luận: Loại 2 — chốt quy ước *mỗi ô lọc phải tự nhận diện được* `[BA duyệt 2026-08-09]`. Dev action: Có (mức Minor) · Sửa đặc tả: Có → Sheet: verdict `QLBMHD_02` giữ **Pass**; QA mở dòng mới `QLBMHD_QA01` ở đợt kế tiếp.**

### Việc Dev cần làm

| # | Việc | Bên | Nghiệm thu bằng |
|---|---|---|---|
| 1 | Bốn ô lọc trên màn Biểu mẫu (`SCR-VII-02`) mỗi ô có **nhãn chữ phía trên** hoặc chữ gợi ý mang tên bộ lọc (*Thư mục · Lĩnh vực · Loại hình · Định dạng*), thay vì cả 4 cùng hiện "Tất cả" | FE | Nhìn thanh lọc đọc được ngay ô nào lọc theo gì mà không cần mở |
| 2 | **KHÔNG** đổi mục *"Tất cả"* **bên trong** danh sách lựa chọn của mỗi ô — mục đó phải giữ theo `UI-11` | FE | Mở từng ô: vẫn có mục "Tất cả" đầu danh sách |

> **Rào chắn `UI-11` — bắt buộc đọc trước khi sửa.** `srs-v3.5.md:583` `UI-11` buộc **mục "Tất cả" nằm trong danh sách lựa chọn** của ô lọc chọn nhiều. Quy ước mới chỉ nói về **nhãn của chính ô lọc**, không đụng mục "Tất cả" bên trong. Nếu Dev hiểu nhầm thành "đổi tên mục Tất cả" là làm hỏng `UI-11`.

### Phương án xử lý (cập nhật SRS)

Thêm một dòng vào Phụ lục E của `srs-v3.5.md`, cùng chỗ với quy ước thanh lọc ở mục 21: *"Mỗi ô lọc phải tự nhận diện được — có **nhãn chữ phía trên ô**, hoặc chữ gợi ý của ô mang tên bộ lọc. Không để nhiều ô lọc cùng hiện một chuỗi giống nhau."* Ghi ở quy ước chung thay vì riêng màn Biểu mẫu, vì hiện tượng này lặp được ở mọi thanh lọc.

---

## 30. Bộ lọc màn Biểu mẫu chỉ chạy khi bấm [Tìm kiếm] `[tự khép]`

**Vấn đề:** Giống hệt mục 21, khác màn: đặc tả màn Biểu mẫu ghi các ô lọc "đổi giá trị → lọc ngay" và **không khai** hai nút mà phần mềm đang có.

**(1)** `srs-fr-09-bieu-mau.md:653` và `:654` đều ghi `change → filter`; bảng thành phần `:650-673` **không khai** nút `[Tìm kiếm]` / `[Xóa bộ lọc]` ⇒ đặc tả vừa đòi lọc ngay, vừa không cho phép tồn tại hai nút đang có.

**(1b)** Không phải tranh chấp tài liệu — đối tác không nêu.

**(2)** Đo được: chọn giá trị không tự lọc, danh sách giữ nguyên 27 kết quả cho tới khi bấm `[Tìm kiếm]`.

**(3)** Hai việc, hai quy ước:
- *Hành vi kích hoạt lọc* → chốt theo quy ước chung ở **mục 21** (giữ nút).
- *Hai nút không được khai trong bảng thành phần* → `srs-v3.5.md:584` `UI-12` phân xử: nút `[Tìm kiếm]` / `[Xóa bộ lọc]` **có căn cứ** ở §Processing của chức năng tra cứu biểu mẫu ⇒ **bảng bị sót, phần mềm đúng**, BA bổ sung hai hàng nút vào bảng.

**→ Kết luận: Loại 2 — phần mềm đúng, đặc tả màn này phải sửa theo quy ước chung. Dev action: Không · Sửa đặc tả: Có (nằm trong phương án mục 21, việc 3) → Sheet: verdict `QLBMHD_02` giữ **Pass**.**

---

## 31. Ô chọn Thư mục ở form Thêm biểu mẫu phải lọc theo đơn vị  **✅ BA duyệt 09/08/2026**

**Vấn đề:** Form Thêm biểu mẫu cho chọn cả thư mục của đơn vị khác; chọn xong bấm lưu thì máy chủ từ chối. Người dùng chọn được một thứ mà chắc chắn sẽ bị từ chối.

**(1)** Đặc tả **im lặng**: `srs-fr-09-bieu-mau.md:357` — *"| E5 | Thư mục không tồn tại | ERR-BM-05 | 'Thư mục đích không tồn tại' |"* chỉ lường tình huống thư mục không tồn tại; **không dòng nào** nói ô chọn phải lọc sẵn theo đơn vị người đăng nhập.

**(1b)** Không phải tranh chấp tài liệu — đối tác không nêu.

**(2)** Phần bảo vệ dữ liệu **đã đúng**: máy chủ chặn và hiện thông báo, không nuốt lỗi, đúng `BR-AUTH-08`.

**(3)** **Khuyến nghị lọc sẵn.** Nguyên tắc phạm vi đơn vị đã áp cho danh sách và cho thao tác; để ô chọn bày ra thứ ngoài phạm vi vừa lộ tên thư mục của đơn vị khác, vừa đẩy người dùng vào một lỗi chắc chắn xảy ra.

**→ Kết luận: Loại 2 `[BA duyệt 2026-08-09]` — chốt lọc sẵn theo đơn vị. Dev action: Có (mức Minor, lọc ở đường trả danh sách thư mục) · Sửa đặc tả: Có → Sheet: verdict `QLBMHD_02` giữ **Pass**.**

**Việc Dev:** Ô chọn Thư mục ở form Thêm/Sửa biểu mẫu **lọc sẵn theo đơn vị** người đăng nhập. *Nghiệm thu:* mở ô Thư mục → chỉ thấy thư mục của đơn vị mình.

### Phương án xử lý (cập nhật SRS)

1. `srs-fr-09-bieu-mau.md` — hàng ô chọn Thư mục của form Thêm/Sửa biểu mẫu: bổ sung *"chỉ liệt kê thư mục thuộc đơn vị của người đăng nhập (BR-AUTH-08)"*.
2. `srs-fr-09-bieu-mau.md:357` — `ERR-BM-05` giữ nguyên vai trò chốt chặn phía máy chủ, sửa câu thành *"Thư mục đích không tồn tại hoặc không thuộc đơn vị của bạn"* cho khớp phần mềm.

---

## 32. Nhật ký hệ thống xếp Hồ sơ pháp lý DN vào nhóm "Tư vấn" là đúng  **✅ BA duyệt 09/08/2026**

**Vấn đề:** Trong Nhật ký hệ thống, thao tác trên *Hồ sơ pháp lý doanh nghiệp* hiện Module = *Tư vấn*, trong khi bộ giá trị của ô lọc có cả nhóm *DN* riêng. Người đi tra dấu vết dễ chọn nhầm nhóm.

**(1)** Đặc tả **KHÔNG im lặng — có bảng ánh xạ, và nó xác nhận phần mềm đúng** `[Codex review 2026-08-09 bắt lỗi lập luận cũ]`: `srs-v3.5.md:1197` là bảng *Entity Name | Module*, dòng `:1263` ghi thẳng *"| 41 | HO_SO_PHAP_LY_DN | **tu-van** | Hồ sơ pháp lý doanh nghiệp (UC150-151) |"*; entity `HO_SO_PHAP_LY_DN` cũng khai *"Module: Nhóm X.1 — Quản lý Tư vấn pháp luật chuyên sâu"* (`srs-fr-12-tv-chuyen-sau.md`). ⇒ nhật ký gán thao tác trên hồ sơ này vào nhóm **Tư vấn** là **đúng theo bảng ánh xạ đã có**, không phải chỗ đặc tả bỏ trống. *(Lập luận cũ ghi "đặc tả im lặng, không có bảng ánh xạ" — sai; Codex bắt được.)*

**(1b)** Không phải tranh chấp tài liệu — đối tác không nêu.

**(2)** Thực thể `HO_SO_PHAP_LY_DN` được đặc tả trong `srs-fr-12-tv-chuyen-sau.md` (nhóm Tư vấn chuyên sâu, `FR-X.1-04`), không thuộc nhóm chức năng Doanh nghiệp ⇒ phần mềm đang gán theo **nhóm chức năng sở hữu chức năng sinh ra thao tác**.

**(3)** **Khuyến nghị giữ "Tư vấn"** và viết nguyên tắc ra: gán theo nhóm chức năng sở hữu thì mọi thực thể đều có đúng một nhóm, không phải phán đoán theo tên.

**→ Kết luận: Loại 3 `[BA duyệt 2026-08-09]` — phần mềm đúng **có căn cứ ở bảng ánh xạ** `srs-v3.5.md:1263` (`HO_SO_PHAP_LY_DN → tu-van`); không phải đặc tả thiếu. Dev action: Không · Sửa đặc tả: Không (bảng đã có; chỉ nên bổ sung một câu trỏ để lượt sau khỏi tra lại) → Sheet: verdict `QLHSPLDN_06` giữ **Pass**.**

### Phương án xử lý (cập nhật SRS)

`srs-fr-10-quan-tri.md:1387` — thêm một câu trỏ tới bảng ánh xạ đã có: *"Giá trị Module của một dòng nhật ký lấy theo bảng ánh xạ Entity → Module (`srs-v3.5.md:1197`+), không lấy theo tên thực thể. Ví dụ `HO_SO_PHAP_LY_DN → tu-van` (`:1263`)."* Đây chỉ là dẫn chiếu cho dễ tra, không phải bổ sung quy tắc mới.

---

## 33. Thêm tệp đính kèm phải đẩy mốc "ngày cập nhật" của hồ sơ  **✅ BA duyệt 09/08/2026**

**Vấn đề:** Sửa hồ sơ pháp lý mà chỉ đính thêm tệp thì tệp vào đủ, nhưng mốc *ngày cập nhật* và số phiên bản của hồ sơ giữ nguyên. Người xem danh sách không thấy hồ sơ vừa được đụng tới.

**(1)** Đặc tả **im lặng**: không có dòng nào định nghĩa thay đổi tệp đính kèm có tính là *cập nhật bản ghi* hay không. Chứng minh ngược: đã tra `ngay_cap_nhat`, `updated_at`, `version`, `tệp đính kèm` ở cả tệp FR và baseline — không có dòng nào phủ trường hợp này.

**(1b)** Không phải tranh chấp tài liệu — đối tác không nêu.

**(2)** Vế quan trọng nhất **đã đóng**: Nhật ký hệ thống có dòng đúng giây bấm ⇒ không mất dấu thao tác.

**(3)** **Khuyến nghị (chỉ chốt hành vi nghiệp vụ, không chỉ định cơ chế kỹ thuật):** thêm hoặc xóa tệp đính kèm **là một lần cập nhật bản ghi** — nên **ngày cập nhật (`ngay_cap_nhat`) phải đổi**, để người dùng thấy hồ sơ vừa được đụng tới trên danh sách.

> **Đã gỡ lập luận kỹ thuật sai `[Codex review 2026-08-09]`.** Bản trước nói *"không tăng `version` để tránh xung đột giả"* — sai cơ chế: hệ này khóa lạc quan bằng **`updated_at`** cho UPDATE thường (`BR-EC-01`, `srs-v3.5.md:5699`) và bằng **`version`** riêng cho chuyển trạng thái (`:5844`); mà `ngay_cap_nhat` **chính là** `updated_at` (`srs-fr-16-api.md:143`). Việc đính tệp đi qua khóa lạc quan hay không là chi tiết **HOW** — thuộc Dev, không phải nội dung phiếu (WHAT-not-HOW). Phiếu chỉ chốt: đính/xóa tệp làm ngày cập nhật đổi.

**→ Kết luận: Loại 2 `[BA duyệt 2026-08-09]` — đặc tả thiếu định nghĩa; chốt *đính/xóa tệp = bản ghi được cập nhật → ngày cập nhật đổi*. Dev action: Có (mức Minor) · Sửa đặc tả: Có → Sheet: verdict `QLHSPLDN_07` giữ **Pass**.**

**Việc Dev:** Thêm hoặc xóa tệp đính kèm làm **đổi ngày cập nhật** của bản ghi (để hồ sơ nổi lên danh sách). Cơ chế khóa lạc quan giữ theo quy ước sẵn có (`BR-EC-01` / chuyển trạng thái) — Dev tự chọn, phiếu không chỉ định. *Nghiệm thu:* sửa hồ sơ chỉ thêm 1 tệp → ngày cập nhật nhảy.

### Phương án xử lý (cập nhật SRS)

Ghi một dòng định nghĩa vào quy ước dữ liệu chung của `srs-v3.5.md` (cạnh bảng DG-01…DG-08), áp cho **mọi** thực thể có tệp đính kèm: *"Thêm hoặc xóa tệp đính kèm của một bản ghi được coi là một lần cập nhật bản ghi đó — `ngay_cap_nhat` đổi theo. Cơ chế khóa lạc quan áp theo quy ước sẵn có (`BR-EC-01` / chuyển trạng thái), không quy định riêng ở đây."*

**Hệ quả phải nói trước với BA — phát hiện ở lượt soi vòng 2:** `DG-06` (`srs-v3.5.md:960`) sắp danh sách theo thời gian cập nhật mới nhất, nên chỉ đính thêm một tệp là bản ghi nhảy lên đầu danh sách. Đây là hệ quả **đúng ý** (bản ghi vừa được đụng tới thì nổi lên trên), nhưng phải nêu ra để lượt kiểm thử sau không log thành lỗi "thứ tự danh sách tự đổi".

---

## 34. Biểu tượng ở cột dữ liệu phải có nhãn tiếng Việt đọc được  **✅ BA duyệt 09/08/2026**

**Vấn đề:** Cột *Loại TL* trên màn Biểu mẫu phân biệt tệp Excel với tệp Word **chỉ bằng biểu tượng**, ô không có chữ, không có nhãn trợ năng, không có chú thích khi rê chuột. Người dùng đọc màn hình bằng phần mềm hỗ trợ chỉ nghe được chuỗi kỹ thuật tiếng Anh.

**(1)** Đặc tả **im lặng ở đúng phạm vi này**: `srs-v3.5.md:6758` §H6 bắt buộc biểu tượng có nhãn trợ năng và chú thích — nhưng phạm vi câu chữ **chỉ là cột Hành động**. Grep toàn bộ `srs-v3.5/`: `aria-label` xuất hiện **3 lần** (`srs-v3.5.md:6758` chính quy ước · `srs-fr-02-hoi-dap.md:1046` một cột Hành động áp quy ước đó · `srs-fr-02-hoi-dap.md:19` dòng lịch sử sửa đổi) — **cả 3 đều thuộc cột Hành động**. Không có dòng nào phủ biểu tượng ở cột dữ liệu.
*(Đính chính bản ghi gốc: §H6 **không** tự mâu thuẫn — nó chỉ không phủ trường hợp này.)*

**(1b)** Không phải tranh chấp tài liệu — đối tác không nêu.

**(2)** Lý do §H6 tồn tại — WCAG 4.1.2, không để thông tin chỉ nằm ở hình ảnh — áp y hệt cho cột dữ liệu: ở đây biểu tượng là **thông tin duy nhất** phân biệt hai định dạng tệp, còn ở cột Hành động thì ít nhất còn vị trí nút để đoán.

**(3)** **Khuyến nghị mở rộng phạm vi §H6.** Đây là phần mềm của cơ quan nhà nước, và yêu cầu tiếp cận đã là ràng buộc đã văn bản hoá chứ không phải tùy chọn: `srs-v3.5.md:577` `UI-05` — *"Accessibility | WCAG 2.1 Level A…"*.

**→ Kết luận: Loại 2 `[BA duyệt 2026-08-09]` — mở rộng phạm vi quy ước. Dev action: Có (mức Minor) · Sửa đặc tả: Có → Sheet: verdict `QLBMHD_02` giữ **Pass**.**

### Phương án xử lý (cập nhật SRS)

`srs-v3.5.md:6758` §H6 — mở rộng câu phạm vi: *"Áp cho **mọi biểu tượng THAY THẾ chữ** trong bảng, không riêng cột Hành động. Biểu tượng đứng thay một giá trị dữ liệu (ví dụ cột Loại tài liệu) phải có nhãn trợ năng và chú thích hover bằng **tiếng Việt** mô tả đúng giá trị đó (ví dụ 'Tệp Excel' / 'Tệp Word'). **Không áp** cho biểu tượng đi **kèm** chữ — ví dụ badge mức cảnh báo 🟡 *Sắp hết hạn* (`srs-fr-05-vu-viec.md:1516`) đã có chữ nên không cần thêm nhãn."*

**Khoanh phạm vi này là bắt buộc — phát hiện ở lượt soi vòng 2.** Viết "mọi biểu tượng mang thông tin" sẽ kéo theo cả các badge trạng thái vốn đã có chữ, biến một việc nhỏ thành lượt rà toàn hệ thống không cần thiết.

Sau khi chốt phải rà **mọi** bảng có biểu tượng đứng thay chữ ở cột dữ liệu, không riêng màn Biểu mẫu.

---

# Kiểm định phiếu — 3 vòng, chế độ Khám phá

## Vòng 1 — khẳng định phủ định và trích dẫn

Rút cơ học mọi câu trong phiếu mà *"nếu thứ này đã tồn tại sẵn thì câu này còn đứng được không"* trả lời **không**, rồi tra ngược từng câu. Bắt được **3 lỗi trong chính phiếu**, hai trong đó do chép trích dẫn của phiếu hỏi mà chưa tự mở kiểm:

| Lỗi | Sai thành | Đã sửa |
|---|---|---|
| Mục 34 — vị trí §H6 | `srs-v3.5.md:6714` (chép từ phiếu hỏi) | `:6758` |
| Mục 34 — *"`aria-label` xuất hiện đúng 1 lần"* | Thực tế **3 lần** — nhưng cả 3 đều thuộc cột Hành động, nên **kết luận không đổi** | Sửa số, giữ kết luận |
| Mục 1 — *"7 neo"* | Không khớp cả số mục lẫn số dòng | Đổi thành "5 mục, 9 dòng" |

Ngoài ra, đối chiếu lại **9 trích dẫn** của phiếu hỏi ở nhóm Báo cáo và Tư vấn chuyên sâu thì **5 trích dẫn trỏ vào dòng trống hoặc dòng khác** — đã dò lại vị trí thật và sửa trong phiếu:

| Phiếu hỏi ghi | Vị trí thật | Thuộc mục |
|---|---|---|
| `srs-fr-12-tv-chuyen-sau.md:871` | `:884` | 15 |
| `srs-fr-12-tv-chuyen-sau.md:968` | `:981` | 15 |
| `srs-fr-11-bao-cao.md:1092` | `:1097` | 17 |
| `srs-fr-11-bao-cao.md:944` | `:948` | 18 |
| `srs-fr-11-bao-cao.md:1016-1020` · `:1018` | `:1021-1023` · `:1021` | 18 |

## Vòng 2 — hệ quả ngược (áp quy ước mới vào thì có chỗ nào đang đúng thành sai không)

Ra **3 điểm**, đều đã vá thẳng vào phương án của mục tương ứng:

| Điểm | Chọi với | Rào chắn đã thêm |
|---|---|---|
| Quy ước *"bấm [Tìm kiếm] mới lọc"* (mục 21) | `UI-09` giữ bộ lọc khi quay lại (`srs-v3.5.md:581`) | Quay lại danh sách thì **tự chạy lại truy vấn** với bộ lọc đã giữ, không đòi bấm lại |
| Quy ước *"xoá mức cảnh báo khi hồ sơ kết thúc"* (mục 22 + 28) | `BR-SLA-03` gửi thông báo khi chuyển mức (`srs-v3.5.md:5627` · `srs-fr-05-vu-viec.md:2444` · `srs-fr-02-hoi-dap.md:1652`) | Xoá mức **không** tính là chuyển mức, không gửi thông báo |
| Mở rộng §H6 sang *"mọi biểu tượng mang thông tin"* (mục 34) | Badge mức cảnh báo đã có chữ (`srs-fr-05-vu-viec.md:1516`) | Khoanh lại: chỉ áp cho biểu tượng **thay thế** chữ, không áp cho biểu tượng **đi kèm** chữ |

Kèm một hệ quả **đúng ý nhưng phải nói trước**: mục 33 đẩy `ngay_cap_nhat` khi đính tệp, mà `DG-06` sắp theo ngày cập nhật ⇒ đính một tệp là bản ghi nhảy lên đầu danh sách.

## Vòng 3 — độ phủ bản sao (mỗi phương án đã liệt kê hết các bản sao chưa)

Ra **0 điểm** ⇒ hội tụ, dừng soi.

| Phương án | Lệnh tra | Kết quả |
|---|---|---|
| Mục 6 — câu hết phiên | grep *"hết hạn.*đăng nhập lại"* · *"session expired"* · *"phiên.*hết hạn"* toàn thư mục | Đúng **4** dạng đã liệt kê, không sót bản sao thứ 5 |
| Mục 12 — câu *"Đăng ký thành công, chờ thẩm định"* | grep chuỗi nguyên văn | **1** nơi duy nhất (`srs-fr-04-chuyen-gia-tvv.md:351`) ⇒ sửa một chỗ là đủ |
| Mục 23 — câu *"Đã cập nhật kết quả"* | grep chuỗi nguyên văn | **0** nơi ⇒ đúng là đặc tả im lặng, phương án thêm mới là chỗ duy nhất |
| Mục 27 — chỗ đặt dòng sắp xếp | đọc trọn bảng `SCR-IV-01` (`srs-fr-04-chuyen-gia-tvv.md:1440-1457`) | Chỉ có hàng phân trang, không có hàng sắp xếp ⇒ dòng mới đặt ở `FR-IV-02 §Processing` là đúng chỗ |

## Lớp soi độc lập — hỏi mù, 3 cụm / 16 câu

Đề bài là **câu hỏi trần** (*"đặc tả nói gì về X"*), **không** đưa kết luận của phiếu vào — so với phiếu chỉ sau khi có câu trả lời. Mọi điểm lớp soi nêu đều đã tự mở tệp kiểm lại trước khi nhận.

**Xác nhận đúng 11 kết luận** của phiếu, trong đó 3 kết luận được củng cố bằng chứng cứ phiếu chưa dẫn: mục 20 (`srs-v3.5.md:5510` tự khai Phụ lục B là *SOURCE OF TRUTH* cho mọi quy tắc nghiệp vụ) · mục 26 (thêm 4 chứng cứ: `BR-CALC-06` `:5604`, mô hình dữ liệu `:1646`, `:1805`, `srs-fr-05:2462`) · mục 14 (rà trọn 23 báo cáo: đúng 3 báo cáo có biểu đồ tròn ở cả hai bản, không thừa không thiếu).

**Lật hoặc sửa 7 điểm:**

| # | Điểm | Phiếu ghi | Thực tế | Xử lý |
|--:|---|---|---|---|
| 1 | Mục 1 — `.docx` | *"cùng hướng với phần mềm"* | `.docx` **cũng tự mâu thuẫn**: mục 4.10.21.2.3 Trường hợp 1 nói *"bấm đường dẫn kích hoạt và đặt mật khẩu lần đầu"*. Lệch 3–1 nghiêng về biểu mẫu | Sửa (1b); **hạ mục 1 xuống `[CẦN BA CHỐT]`** |
| 2 | Mục 1 — số chỗ phía màn kích hoạt | *"2 câu"* | **5 chỗ**, gồm bảng chuyển trạng thái SM-TAIKHOAN `srs-fr-10:2299` + bản sao baseline `srs-v3.5.md:6390` **nêu đích danh FR-VIII-22** | Sửa (1); thêm phép thử *dòng nào chết*; thêm 3 chỗ vào phương án |
| 3 | Mục 27 — số đếm khuôn sắp xếp | *"ngày cập nhật 3 · ngày tạo 1"* | **3–3** (bổ sung `srs-fr-12:1145`, `srs-fr-02:1044`); `DG-06` còn thiếu mệnh đề phạm vi, chưa FR nào dẫn chiếu, và `srs-v3.5.md:721` nói ngược | **Hạ xuống `[CẦN BA CHỐT]`**; phương án từ 1 việc lên 4 việc |
| 4 | Mục 21 — độ rộng lượt sửa | *"47 chỗ"* | **60** — lượt đếm đầu bỏ sót 13 chỗ dùng mũi tên ASCII `change -> filter` ở 4 tệp khác; cộng biến thể tiếng Việt | Sửa số; sửa *"ít nhất 5 màn"* → **9 màn** có nút Tìm kiếm, **10 màn** có Xóa bộ lọc |
| 5 | Mục 10 · 30 — căn cứ | Lập luận riêng | Đã có **quy ước `UI-12`** (`srs-v3.5.md:584`, BA chốt 2026-07-30) phân xử đúng tình huống này | Dẫn thẳng `UI-12`; kết luận không đổi |
| 6 | Mục 25 — độ phủ chỗ sửa | Chỉ vá bảng nút `:1751` | **Bảng chuyển trạng thái SM-VUVIEC `:2297` cũng thiếu**, cùng 2 bản sao ở baseline | Phương án từ 1 việc lên 3 việc |
| 7 | Mục 29 — quy ước mới | *"'Tất cả lĩnh vực' thay vì 'Tất cả'"* | Cách viết đó có thể bị hiểu thành đổi mục *"Tất cả"* trong danh sách, phá `UI-11` (`srs-v3.5.md:583`) | Khoanh lại phạm vi: chỉ nói về **nhãn của ô lọc** |

**Bốn điểm treo mới** do lớp soi phát hiện, đều nằm ngoài phạm vi 34 mục — đã ghi ở bảng cuối phiếu: `FR-V.I-04` redirect lệch §H7 · §Outputs nhóm Hỏi đáp chỉ liệt kê 3/4 mức cảnh báo · ô Loại khai *radio* ở một chỗ và *dropdown* ở chỗ khác · hai chức năng xuất tệp xử lý khác nhau khi vượt 10.000 dòng.

**Đánh giá độ tin của lớp soi:** không nhận nguyên si. Một điểm nó nêu đã bị bác sau khi tự kiểm — nó xếp `srs-fr-04-chuyen-gia-tvv.md:984` thuộc *FR-IV-14*, trong khi heading thật ở `:966` là **FR-IV-NEW-02**; phiếu giữ theo heading.

## Vòng 4 — đối chiếu lại sau khi bản bàn giao được cập nhật

Bản `.docx` bị sửa **giữa lượt kiểm định** (bản trích lấy lúc 07/08 15:46, tệp được lưu lại lúc 08/08 10:20). Toàn bộ câu `(1b)` của phiếu đang dựa trên bản cũ nên phải trích lại và so.

- **62 dòng khác nhau** giữa hai bản trích. Đọc hết: đều là nội dung áp 7 quyết định của phiếu chốt trước, **không chạm** vào 13 đoạn phiếu này đang dẫn.
- Kiểm từng đoạn trong 13 đoạn đó trên bản mới: **còn nguyên 13/13** ⇒ không mục nào đổi kết luận.
- Kiểm chiều ngược (câu 6 của rà phạm vi ảnh hưởng): quyết định *"Quản trị hệ thống không phải tác nhân nhóm Báo cáo thống kê"* đã được áp ở **cả hai** bản — `.docx` mục 4.10.30.2.3 và `.md` `srs-fr-11-bao-cao.md:79` + `:1273`. Không sinh lệch mới.

**Kiểm toàn vẹn bản trích** (phòng lỗi bóc `.docx` sai cách làm mất ô bảng / số mục):

| Phép đo | Kết quả |
|---|---|
| Số mục `N.N…` trong `.docx` gốc | **1.169**, từ `1.1` đến `5.1.1` |
| Số mục không có ở bản trích | **0** |
| 13 số mục phiếu đang dẫn | có đủ ở cả tệp gốc lẫn bản trích |
| Độ phủ đoạn văn (>40 ký tự) | 1.892/1.894 — 2 chỗ còn lại đã mở kiểm, **có** trong bản trích, là lỗi phép khớp |
| Độ phủ ô bảng (>40 ký tự) | 1.808/1.818 — spot-check 4 chỗ báo thiếu thì 3 chỗ **có**, chỗ còn lại là ô gộp bị đếm trùng |

**Soát lại toàn bộ trích dẫn `file:dòng` của phiếu — 122 tham chiếu:**

| Phép đo | Kết quả |
|---|---|
| Trỏ ra ngoài tệp | 0 |
| Trỏ vào dòng trống | 0 *(2 chỗ còn số cũ là cố ý — nằm trong bảng ghi nhận độ lệch ở Vòng 1)* |
| **Sai dòng, đã sửa** | **6** — xem dưới |

| Phiếu ghi | Vị trí thật | Thuộc mục |
|---|---|---|
| `srs-fr-11-bao-cao.md:1064` · `:1065` · `:1067` (bảng ánh xạ 23 loại báo cáo) | `:1069` · `:1070` · `:1072` | 14 |
| `srs-fr-11-bao-cao.md:897` (ô lọc `trang_thai_ct`) | `:900` | 16 |
| `srs-fr-11-bao-cao.md:907` (`tong_ct`) | `:910` | 16 |

Sáu chỗ này đều là số dòng **chép từ phiếu hỏi của QA mà lượt soạn chưa tự mở kiểm** — đúng loại lỗi mà Vòng 1 đã bắt được 5 lần ở cùng hai tệp `srs-fr-11` và `srs-fr-12`. Nội dung trích dẫn không sai, chỉ sai toạ độ.

## Cảnh báo ngưỡng — lượt này sinh 12 thứ mới, vượt ngưỡng 10

Quy trình đặt ngưỡng **10 thứ mới trong một lượt**; quá thì dừng và tách phương án, vì số cặp phải đối chiếu bùng theo bình phương. Lượt này sinh **12** thứ mới:

> 6 quy ước mới (mục 13 · 15 · 21 · 29 · 33 · 34) · 3 nguyên tắc mới (mục 16 · 22+28 · 32) · 1 mã chuẩn đổi (mục 20) · 1 câu chuẩn mới (mục 6) · 1 ràng buộc mới về nhãn kỳ tệp xuất (mục 17) → **66 cặp** nếu đối chiếu trọn.

**Vì vậy phiếu đã tách sẵn 3 đợt sửa đặc tả ở mục B dưới đây.** Đợt lớn nhất (Đ2) gom 6 quy ước = **15 cặp**, nằm dưới ngưỡng và đối chiếu được trong một lượt. Đề nghị BA **không gộp ba đợt làm một** — gộp lại là quay về đúng 66 cặp mà ngưỡng này sinh ra để phòng.

---

# Việc phải thi hành sau khi BA duyệt

## A. Việc của Dev — 17 mục, gộp thành 16 dòng việc  ·  *mỗi mục cũng có dòng **Việc Dev** riêng tại thân mục*

| Mục | Việc | Mức | Bên |
|---|---|---|---|
| 2 | Nâng mốc ô Lý do lên **5.000** ký tự · bỏ hẳn cắt bớt nội dung · thêm bộ đếm `{n}/5000` · chặn Lưu ở hai đầu kèm câu báo · máy chủ kiểm cùng hai mốc và trả đúng mã lỗi — **6 việc, chi tiết ở mục 2 §Việc Dev cần làm** | Minor | FE + BE |
| 6 | Thống nhất câu thông báo hết phiên theo câu chuẩn | Minor | FE |
| 12 | Ghép mã hồ sơ vào thông báo đăng ký thành công | Minor | FE |
| 15 | Máy chủ trả `ERR-TLPL-03` thay cho mã hệ thống chung khi tệp vượt 20MB | Minor | BE |
| 17 | Tệp xuất in nhãn kỳ bằng chữ tiếng Việt, mọi loại báo cáo | Minor | BE |
| 19 | Gỡ hậu tố ở ba nhãn kết luận kiểm tra, còn *"Đạt" / "Không đạt" / "Yêu cầu bổ sung"* theo bản bàn giao | Trivial | FE |
| 20 | Nhóm Vụ việc đổi mã mức sang `SAP_HET_HAN` (ràng buộc, ô lọc, giá trị đang lưu) rồi chạy lại công việc tính mức | Minor | BE |
| 22 + 28 | Mức cảnh báo chỉ tính khi hồ sơ đã có thời hạn và chưa kết thúc → để trống ngoài khoảng đó · bộ lọc Mức SLA loại hồ sơ không có mức · bỏ nhãn *"Đã hoàn thành"* khỏi cột SLA · chạy lại công việc tính mức để dọn dữ liệu cũ (2 hồ sơ ở nhóm Vụ việc + 4 hồ sơ ở nhóm Chi trả) — **gộp một lượt với mục 20** | Minor | BE (+ FE chỉ ở phần gỡ nhãn) |
| 23 | Đổi chuỗi hiển thị sau khi lưu kết quả: *"Đã cập nhật kết quả"* → *"Đã cập nhật kết quả hỗ trợ"* | Trivial | FE |
| 24 | Bổ sung đường **xóa từng tệp kết quả** ở Nhóm 6 màn chi tiết vụ việc — chép khuôn Accordion 3 đã có cùng màn *(bỏ nếu phép đo cho thấy màn đã có nút Xóa)* | Minor | BE + FE |
| 25 | Mở nút Đánh giá khi vụ việc ở *Đã đánh giá* và người xem chưa chấm | Major | BE + FE |
| 27 | Danh sách Tư vấn viên sắp theo **ngày cập nhật** giảm dần (DG-06) — hiện đang theo ngày tạo | Minor | BE |
| 29 | Ô lọc phải tự nhận diện được (nhãn hoặc chữ gợi ý mang tên bộ lọc) | Minor | FE |
| 31 | Ô chọn Thư mục lọc sẵn theo đơn vị người đăng nhập | Minor | BE |
| 33 | Thêm/xóa tệp đính kèm đẩy `ngay_cap_nhat`, không tăng `version` | Minor | BE |
| 34 | Biểu tượng ở cột dữ liệu có nhãn trợ năng + chú thích tiếng Việt | Minor | FE |

**Không mục nào chặn bàn giao.** Mục 25 là mục duy nhất mức Major, đề nghị ghép cùng lần sửa `BUG-VV-DGKQHTVV-01`.

## B. Việc sửa đặc tả — tách thành đợt riêng

Theo nguyên tắc nền của quy trình, **sửa SRS là pha riêng, chỉ chạy khi BA yêu cầu rõ**. Phiếu này chỉ chốt nội dung. Đề nghị chia **3 đợt**, không gộp:

| Đợt | Phạm vi | Số tệp chạm | Lý do tách |
|---|---|---|---|
| **Đ1 — điểm lẻ** | Mục 1 · 2 · 3 · 4 · 5 · 7 · 10 · 11 · 12 · 16 · 17 · 18 · 19 · 23 · 24 · 25 · 26 · 31 · 32 | 8 | Mỗi mục sửa 1–4 chỗ, độc lập nhau |
| **Đ2 — quy ước mới ở Phụ lục E** | Mục 13 (chặn xuất khi rỗng) · 15 (phạm vi bảng Error Handling) · 21 (thanh lọc) · 29 (nhãn ô lọc) · 33 (tệp đính kèm và `ngay_cap_nhat`) · 34 (mở rộng §H6) | 1 + rà toàn bộ | Sáu quy ước mới trong một lượt — phải rà chéo từng cặp xem có chọi nhau không trước khi áp |
| **Đ3 — sửa hàng loạt** | Mục 20 (15 chỗ `SAP_HET`) · 21 việc 2 (47 chỗ `change → filter`) · 22 + 28 (4 bản sao mức cảnh báo) | 8 | Sửa hàng loạt, mỗi chỗ phải mở đọc chứ không thay chuỗi máy móc |

**Chốt chặn cho Đ2:** sáu quy ước mới sinh **15 cặp** phải đối chiếu xem có loại trừ nhau không. Dưới ngưỡng 10 thứ mới nên vẫn làm được trong một lượt, nhưng phải in ra bảng đối chiếu đủ 15 cặp, không rà bằng cảm giác.

## C. Việc của bên soạn tài liệu bàn giao — Doc action

| Mục | Việc |
|---|---|
| 1 | `.docx` mục 3.10 bước 2 ghi liên kết kích hoạt *"có hiệu lực 7 ngày"* — sửa theo bản gốc: **vĩnh viễn, dùng một lần** |
| 2 | Bổ sung mốc 2.000 ký tự + bộ đếm vào hai bảng ô *Lý do thay đổi trạng thái* |
| 10 | Bổ sung ô tìm kiếm + 3 bộ lọc vào bảng *Mô tả thông tin trên màn hình* mục 4.12.6.2.2 (mục 4.12.6.2.3 đã có chức năng số 10, chỉ thiếu ở bảng thành phần) |
| 12 | Chuẩn hoá nguyên văn câu thông báo ở mục 4.4.3.2.3 theo câu chốt *"Đăng ký thành công, chờ thẩm định. Mã hồ sơ: {ma_tvv}"* |
| Chung | Mỗi chỗ sửa bản gốc ở đợt Đ1–Đ3 phải sinh đúng một dòng đối ứng trong `.docx` — rà cả chiều *"`.docx` thừa thì gỡ"* lẫn chiều *"`.docx` phải theo bản gốc mới"* |

## D. Việc ghi sổ theo dõi — trước khi ghi phải làm đủ

1. **Đọc tập giá trị đang dùng** của cột trạng thái tab `bug` và đếm tần suất. Ghi đúng chuỗi của sổ **kể cả khi sai chính tả** (sổ hiện dùng `Resoved`). Phiếu này ghi theo tên khái niệm, không phải chuỗi ghi lên sổ.
2. **Xác định dòng theo Mã TC ngay trước khi ghi**, không dùng số dòng nhớ từ lượt đọc trước. Số dòng nêu trong các phiếu hỏi (35 · 50 · 62 · 64 · 72 · 138 · 178 · 267 · 272 · 281 · 297 · 299 · 301 · 302) là **toạ độ chép từ tài liệu dẫn xuất** — chỉ dùng để định hướng, không dùng để ghi.
3. **Verify ngay sau khi ghi:** đúng số ô đã đổi, và tại mỗi dòng vừa ghi Mã TC vẫn là mã dự kiến.
4. Dòng nào chỉ đổi trạng thái được sau khi đặc tả sửa xong thì **để QA/Dev đổi**, người phân tích không đổi thay.

# Điểm treo chuyển đợt sau

| Nội dung | Phát hiện ở mục | Thuộc bên | Trạng thái |
|---|---|---|---|
| `ly_do_tu_choi` đang có **hai** mốc — 2.000 ở 5 chỗ và 1.000 ở `srs-fr-02-hoi-dap.md:677` (nhóm Hỏi đáp). Giữ 1.000 làm ngoại lệ hay đồng bộ về 2.000? | 2 | BA | CHỜ BA CHỐT |
| Trạng thái `DA_CONG_BO` và `TAM_DUNG` của chương trình có nằm trong tập báo cáo thống kê không | 16 | BA | CHỜ BA CHỐT |
| Trên vụ **đang xử lý đã có tệp kết quả**, form *Cập nhật kết quả* có hiện lại tệp cũ kèm nút xóa không — đã đo 09/08 nhưng seed không có vụ đúng diện + automation không đính được tệp (Ant Upload chặn); cần QA đo tay | 24 | QA đo tay | CHỜ BẰNG CHỨNG |
| Hệ thống có cần **cả hai** thực thể đánh giá (`DANH_GIA_VU_VIEC` và `DANH_GIA_SAU_VU_VIEC`) không | 26 | BA | CHỜ BA CHỐT |
| Ngày bàn giao và kênh gửi của `HTPLDN-PTYC-CT-v3.5.docx` — chưa ghi nhận được | Bối cảnh chung | Bên soạn tài liệu | Chưa xử |
| Mọi kết luận "web đúng" trong phiếu đo trên env nội bộ V1.0.8/V1.0.9; **phải đo lại** sau khi bản này lên môi trường nghiệm thu | Toàn phiếu | QA | Chưa xử |
| Khi gửi bản `.docx` mới cho đối tác, **gửi kèm danh sách mã test case cần sửa Kết quả mong đợi** — hiện gồm `QLDKTK_10` · `QLDMTCTV_12` · `DKTGMLTVV_13` · `VVDTN_04` · `QLTVV_02` | 1 · 2 · 8 · 9 · 14 · 27 | Bên soạn tài liệu | Chưa xử |
| §Outputs của nhóm Hỏi đáp (`srs-fr-02-hoi-dap.md:182` · `:256` · `:403`) và ô lọc `srs-fr-05-vu-viec.md:114` chỉ liệt kê **3/4** mức cảnh báo (thiếu `QUA_HAN_NGHIEM_TRONG`) | Lớp soi độc lập | BA | Chưa xử — gộp vào lượt sửa mã mức ở mục 20 |
| `srs-fr-04-chuyen-gia-tvv.md:296` khai ô Loại là **radio**, `:1490` khai là **dropdown 2 lựa chọn** — mâu thuẫn nội tại, phần mềm đang làm dropdown | Lớp soi độc lập | BA | Chưa xử |
| Hai chức năng xuất tệp xử lý **khác nhau** khi vượt 10.000 dòng: kho câu hỏi **chặn xuất**, chương trình **xuất 10.000 dòng đầu**. Liên quan trực tiếp tới quy ước đang chốt ở mục 13 | Lớp soi độc lập | BA | Chưa xử — nên chốt cùng lượt với mục 13 |
| Quy ước *mã lỗi áp mọi lớp* (mục 15) áp cho **mọi** bảng Error Handling — lượt này mới đo được 1 ca (tệp vượt 20MB); phải rà các ca còn lại khi thi hành | 15 | QA đo lượt sau | CHỜ BẰNG CHỨNG |
| `FR-V.I-04` (nhập hồ sơ yêu cầu thủ công) ghi *"redirect chi tiết VV"* (`srs-fr-05-vu-viec.md:347`) — lệch quy ước §H7 mà **không có ghi chú ngoại lệ**, đúng loại lỗi mà mục 9 đang xử ở FR khác | Lớp soi độc lập | BA | Chưa xử — ngoài phạm vi phiếu này |
| Bản tải trùng `cau-hoi-BA-tong-hop-2026-08-06 (1).md` cũ hơn bản chính (thiếu khối trỏ sang `QLHSPLDN_15`) — nên xoá cho khỏi lẫn | Bối cảnh | QA | Chưa xử |
