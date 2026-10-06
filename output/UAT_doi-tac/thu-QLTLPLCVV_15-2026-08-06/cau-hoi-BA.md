# BA confirmation needed — Verify bug dev fix QLTLPLCVV_15 — 2026-08-06

> **⚠️ File này là bản ghi gốc của lô, KHÔNG phải bản gửi BA.**
> Bản gửi BA là [`cau-hoi-BA-tong-hop-2026-08-06.md`](../reverify-week-5/ba-confirm/cau-hoi-BA-tong-hop-2026-08-06.md) — Mục 1 · 3 · 4 · 5 → **Mục 2 · 3 · 4 · 5**.
> **Đã xoá khỏi bản gộp vì trùng câu đã gửi:** Mục 2 (cùng câu hỏi quyền xuất tệp của vai trò QTHT) — BA trả lời một lần ở [`cau-hoi-BA.md`](../reverify-week-5/ba-confirm/cau-hoi-BA.md).

> **File này để làm gì:** ghi nhận **ngoài phạm vi** phát sinh trong lúc verify case `QLTLPLCVV_15`.
> Đối tác **không** phản ánh điểm này; nó **không** ảnh hưởng verdict của `QLTLPLCVV_15` (đã Pass).
> Chưa mở phiếu lỗi vì giao diện và máy chủ đang **lệch nhau** — cần BA chốt trước.

---

## Ghi nhận ngoài phạm vi — Thông báo khi tệp đính kèm vượt 20MB: giao diện đúng, máy chủ trả câu tiếng Anh không nêu ngưỡng

**Bối cảnh**

- Phát sinh khi verify `QLTLPLCVV_15` (tab `bug`, dòng 299) — cùng màn "Tư liệu pháp lý liên kết" của
  nội dung Tư vấn chuyên sâu, cùng widget "File đính kèm".
- **Không thuộc case nào của bảng theo dõi.** Đối tác không nêu điểm này.
- Vai trò đo: `cbnv_tw` (CB_NV_TW, cấp TW). Môi trường `https://18.143.165.120.nip.io`, bản dựng V1.0.8.

**Kết quả verify hiện tại — hai đường đo cho ra hai kết quả khác nhau**

| Đường đo | Quan sát |
|---|---|
| **Giao diện** — chọn tệp PDF sạch 23.069.772 B (≈22MB) qua widget "File đính kèm" | Bị chặn **ngay tại trình duyệt** (0 request gửi lên máy chủ). Thông báo tiếng Việt: `C-pdf-sach-vuot-20mb.pdf: Kích thước vượt quá giới hạn 20MB.` → **đúng nghĩa, người dùng hiểu được** |
| **Máy chủ** — gọi thẳng cùng hành động với tệp 22.000.099 B | HTTP **413**, `{"code":"ERR-SYS-00-00-01","message":"File too large"}` → **tiếng Anh**, mã lỗi hệ thống chung, **không nêu ngưỡng 20MB** |

- Đối chứng: cùng widget, tệp chứa mã độc trả đúng mã riêng `ERR-TLPL-04` với câu tiếng Việt đầy đủ
  ⇒ cơ chế "trả mã lỗi riêng theo tình huống" **vẫn chạy được ở chỗ khác** trên chính endpoint này
  ⇒ không phải lỗi môi trường.
- Bằng chứng: [`image/A-02-thong-bao-va-phan-hoi-may-chu.txt`](image/A-02-thong-bao-va-phan-hoi-may-chu.txt) mục 3 và mục 4.

**Đối chiếu SRS v3.5**

- Luồng "Tải lên file" tách bước 2 (kiểm dung lượng/định dạng) và bước 3 (quét virus).
- Bảng Error Handling quy định tình huống **tệp vượt 20MB** có phản hồi riêng, nêu rõ ngưỡng 20MB —
  khác với lỗi hệ thống chung.

**Citation**

- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-12-tv-chuyen-sau.md:871`
  — `| 2 | Kiểm tra file: max 20MB, định dạng cho phép | EC-FILE-01 |`
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-12-tv-chuyen-sau.md:968`
  — `| E3 | File vượt 20MB | ERR-TLPL-03 | "File tối đa 20MB" | ERROR |`

**Điểm cần BA chốt**

Bảng Error Handling của đặc tả áp dụng cho **cả hai lớp** (giao diện *và* máy chủ), hay chỉ cần **lớp mà
người dùng cuối nhìn thấy**?

1. **Nếu chỉ tính lớp người dùng nhìn thấy:** hiện trạng **đạt** — giao diện đã chặn và báo đúng nghĩa
   bằng tiếng Việt trước khi request rời trình duyệt; người dùng trên giao diện không bao giờ gặp câu
   tiếng Anh. ⇒ Không mở phiếu, đóng ghi nhận này.
2. **Nếu tính cả lớp máy chủ** (vì còn các bên tích hợp gọi thẳng API, không đi qua giao diện):
   hiện trạng **chưa đạt** — máy chủ cần trả phản hồi nêu rõ tệp vượt ngưỡng 20MB bằng tiếng Việt như
   các tình huống lỗi khác của cùng endpoint. ⇒ Mở phiếu mức **Minor**, owner **Dev BE**.

**Đề xuất QA tạm thời**

- **Chưa** mở phiếu lỗi và **chưa** thêm dòng mới trên bảng theo dõi cho tới khi BA chọn hướng — vì hai
  đường đo cho kết quả khác nhau và hướng (1) là kết luận "không phải lỗi".
- Verdict của `QLTLPLCVV_15` **không** phụ thuộc vào ghi nhận này (đã Pass theo đúng các vế đối tác nêu).
- Nếu BA chọn hướng (2), QA sẽ mở dòng mới trên tab `bug` theo quy tắc mã `QLTLPLCVV_QA01` ngay trong
  đợt kế tiếp.

---
---

# Bổ sung 2026-08-06 12:40 — phát sinh khi verify `SLCTHT_06` (tab `bug`, dòng 267)

> Hai mục dưới đây phát sinh trên màn **Báo cáo thống kê → BC Số lượng chương trình hỗ trợ**
> (FR-IX-20/UC143). Đối tác **không** nêu mục 3. Cả hai **không** kéo verdict của `SLCTHT_06`
> (đã Reopen theo đúng vế đối tác nêu).

## Mục 2 — Vai trò QTHT có được XUẤT báo cáo thống kê không? (đặc tả không nói rõ, lại có 2 chỗ nghiêng về 2 hướng)

**Web đang thế nào** (đo 2026-08-06 12:32, `18.143.165.120.nip.io`, bản dựng V1.0.8, tài khoản `admin`,
`vaiTro = ["QTHT"]`, cấp TW):

| Thao tác | Kết quả |
|---|---|
| [Xem báo cáo] | **Cho qua** — hiện đầy đủ Tổng chương trình 7 · Đang thực hiện 1 · Hoàn thành 1 + bảng theo đơn vị + biểu đồ |
| [Xuất Excel] | **Từ chối** — HTTP 403, chữ hiện ra cho người dùng là `Forbidden`, không có tệp |

**Đối tác kỳ vọng gì:** đối tác chạy đúng vai trò QTHT này ở cả 2 vòng nghiệm thu và coi việc không xuất
được tệp là lỗi (ô *Kết quả mong đợi*: *"Hệ thống xuất toàn bộ và tự động tải tệp về máy người dùng"*).

**Đặc tả nói gì** (`Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md`):

- `:62` — Preconditions chung: *"User đã đăng nhập, có role CB Nghiệp vụ hoặc CB Phê duyệt (TW/BN/ĐP)"*.
  `:889` — Tác nhân FR-IX-20: *"CB Nghiệp vụ / CB Phê duyệt (TW/BN/ĐP)"*.
  ⇒ **liệt kê** hai vai trò, nhưng **không có câu nào cấm** QTHT.
- `:1268` — BR-AUTH-08, cột *Ngoại lệ* ghi **"QTHT bypass"**, cột *Áp dụng* ghi **"Toàn bộ FR-IX"**.
  ⇒ nghiêng về hướng QTHT **có** chạm vào báo cáo.
- `:79` — Processing bước 1: *"Kiểm tra quyền truy cập báo cáo + phạm vi theo đơn vị"* — việc kiểm quyền
  nằm ở **đầu** luồng, nên dù chốt hướng nào thì bước Xem và bước Xuất cũng phải **nhất quán**.

**Câu hỏi cụ thể cho BA:**

1. Vai trò **QTHT** có được **xuất** báo cáo thống kê (Excel/PDF) không?
2. Nếu **có** → phần mềm đang chặn sai, Dev BE phải mở quyền xuất cho QTHT.
3. Nếu **không** → phần mềm đang **cho xem** nhưng **cấm xuất** là mâu thuẫn: theo `:79` thì phải chặn
   ngay từ bước [Xem báo cáo]. BA xác nhận giúp hướng xử lý là chặn từ bước Xem, hay chấp nhận cho xem
   và chỉ cấm xuất?
4. Dù chốt hướng nào: câu chữ hiện cho người dùng khi từ chối phải theo `:117` (*"Bạn không có quyền xem
   báo cáo này"*), **không** để lọt chuỗi `Forbidden` / mã `ERR-PERM-SYS-00-01` ra màn hình.

**Đường dẫn ảnh + bằng chứng:**
[`image/SLCTHT_06-B1-qtht-forbidden-khi-xuat-excel-V108.png`](image/SLCTHT_06-B1-qtht-forbidden-khi-xuat-excel-V108.png)
· nguyên văn phản hồi máy chủ ở
[`image/SLCTHT_06-thong-bao-va-phan-hoi-may-chu.txt`](image/SLCTHT_06-thong-bao-va-phan-hoi-may-chu.txt)
· phiếu lỗi: `bug-report.md` § BUG-SLCTHT-006.

> **Cùng câu hỏi này, đo thêm trên màn *BC Chương trình theo đơn vị*** (case `CTTDVQL_04`, tab `bug` dòng 272,
> đo 2026-08-06 13:05–13:06, cùng bản dựng V1.0.8, cùng tài khoản `admin`/`QTHT`): [Xem báo cáo] **cho qua**
> (7 chương trình · 350.000.000 ₫), [Xuất Excel] **từ chối** HTTP 403 `ERR-PERM-SYS-00-01`, chữ hiện ra vẫn là
> `Forbidden`, không có tệp. **Không mở mục hỏi mới** — đây đúng câu hỏi Mục 2, chỉ khác loại báo cáo. Ảnh:
> [`image/CTTDVQL_04-B4-qtht-thong-bao-Forbidden-khi-bam-xuat-excel-V108.png`](image/CTTDVQL_04-B4-qtht-thong-bao-Forbidden-khi-bam-xuat-excel-V108.png)
> · phiếu lỗi: `bug-report.md` § BUG-CTTDVQL-004. BA chốt một lần là đủ cho cả hai (và cả các loại báo cáo
> khác đang dùng chung `POST /api/v1/bao-cao/export`).

> **Cùng câu hỏi này, đo thêm trên màn *BC Chương trình theo lĩnh vực*** (case `CTTLV_05`, tab `bug` dòng 277,
> đo 2026-08-06 13:44–13:45, cùng bản dựng V1.0.8, cùng tài khoản `admin`/`QTHT`): [Xem báo cáo] **cho qua**
> (Tổng 7 chương trình, 5 nhóm lĩnh vực), [Xuất Excel] **từ chối** HTTP 403 `ERR-PERM-SYS-00-01`, chữ hiện ra
> vẫn là `Forbidden`, không có tệp. **Không mở mục hỏi mới** — đây đúng câu hỏi Mục 2, chỉ khác loại báo cáo.
> Ảnh: [`image/CTTLV_05-B1-qtht-xem-duoc-bao-cao-day-du-truoc-khi-bam-xuat-V108.png`](image/CTTLV_05-B1-qtht-xem-duoc-bao-cao-day-du-truoc-khi-bam-xuat-V108.png)
> · phiếu lỗi: `bug-report.md` § BUG-CTTLV-005.

> **Cùng câu hỏi này, đo thêm trên màn *BC Chương trình theo thời gian*** (case `CTTTG_04`, tab `bug` dòng 281,
> đo 2026-08-06 14:22–14:23, cùng bản dựng V1.0.8 — bó mã `assets/index-DIABnbIr.js`, cùng tài khoản
> `admin`/`QTHT`): [Xem báo cáo] **cho qua** (Tổng chương trình toàn kỳ 6 · 250.000.000 ₫), [Xuất Excel]
> **từ chối** HTTP 403 `ERR-PERM-SYS-00-01`, chữ hiện ra vẫn là `Forbidden`, không có tệp. **Không mở mục
> hỏi mới** — đây đúng câu hỏi Mục 2, chỉ khác loại báo cáo. Ảnh:
> [`image/CTTTG_04-B1-qtht-xem-duoc-bao-cao-day-du-truoc-khi-bam-xuat-V108.png`](image/CTTTG_04-B1-qtht-xem-duoc-bao-cao-day-du-truoc-khi-bam-xuat-V108.png)
> · phiếu lỗi: `bug-report.md` § BUG-CTTTG-004.

> **Cùng câu hỏi này, đo thêm trên màn *BC Số lượng CG/TVV*** (case `CGTVPL_06`, tab `bug` dòng 210, đo
> 2026-08-06 14:40–14:47, bó mã `assets/index-DIABnbIr.js`, cùng tài khoản `admin`/`QTHT` — `donViId …0001`,
> **trùng đơn vị** với tài khoản CB Nghiệp vụ dùng đối chứng): [Xem báo cáo] **cho qua** (Tổng Tư vấn viên 6 ·
> Số Tư vấn viên 4 · Số Chuyên gia 2), [Xuất Excel] **và** [Xuất PDF] đều **từ chối** HTTP 403
> `ERR-PERM-SYS-00-01`, chữ hiện ra vẫn là `Forbidden`, không có tệp — **4/4 lượt** (2 bấm chuột + 2 gọi
> thẳng máy chủ). **Không mở mục hỏi mới** — đây đúng câu hỏi Mục 2, chỉ khác loại báo cáo. Ảnh:
> [`image/CGTVPL_06-07-vaitro-QTHT-thong-bao-Forbidden-khi-xuat-excel-V108.png`](image/CGTVPL_06-07-vaitro-QTHT-thong-bao-Forbidden-khi-xuat-excel-V108.png)
> · phiếu lỗi: `bug-report.md` § BUG-CGTVPL-006.

> **Cùng câu hỏi này, đo thêm trên màn *BC Đánh giá hiệu quả HTPL*** (case `DGHQHTPL_06`, tab `bug` dòng 214,
> đo 2026-08-06 15:31–15:35, bó mã `assets/index-DIABnbIr.js`, cùng tài khoản `admin`/`QTHT` — `donViId …0001`,
> **trùng đơn vị** với tài khoản CB Nghiệp vụ dùng đối chứng): [Xem báo cáo] **cho qua** (Tổng đợt đánh giá 4 ·
> Tổng lượt đánh giá 8 · Tổng số vụ việc đã đánh giá 7 · Điểm trung bình chung 33), [Xuất Excel] **và**
> [Xuất PDF] đều **từ chối** HTTP 403 `ERR-PERM-SYS-00-01`, chữ hiện ra vẫn là `Forbidden`, không có tệp —
> **13/13 lượt** (11 bấm chuột + 2 gọi thẳng máy chủ). **Không mở mục hỏi mới** — đây đúng câu hỏi Mục 2, chỉ
> khác loại báo cáo. Ảnh:
> [`image/DGHQHTPL_06-07-vaitro-QTHT-thong-bao-Forbidden-khi-xuat-excel-V108.png`](image/DGHQHTPL_06-07-vaitro-QTHT-thong-bao-Forbidden-khi-xuat-excel-V108.png)
> · phiếu lỗi: `bug-report.md` § BUG-DGHQHTPL-006.

> **Cùng câu hỏi này, đo thêm trên màn *BC Chất lượng đào tạo*** (case `CLDTBDPL_06`, tab `bug` dòng 218,
> đo 2026-08-06 16:14–16:18, bó mã `assets/index-DIABnbIr.js`, cùng tài khoản `admin`/`QTHT` — `donViId …0001`,
> **trùng đơn vị** với tài khoản CB Nghiệp vụ dùng đối chứng): [Xem báo cáo] **cho qua** (Tổng khóa học 7 ·
> Tổng học viên 17 · Điểm trung bình 6 · Tỷ lệ đạt 28.6 %), [Xuất Excel] **và** [Xuất PDF] đều **từ chối**
> HTTP 403 `ERR-PERM-SYS-00-01`, chữ hiện ra vẫn là `Forbidden`, không có tệp — **19/19 lượt** (17 bấm chuột
> + 2 gọi thẳng máy chủ). **Không mở mục hỏi mới** — đây đúng câu hỏi Mục 2, chỉ khác loại báo cáo. Ảnh:
> [`image/CLDTBDPL_06-08-vaitro-QTHT-thong-bao-Forbidden-khi-xuat-excel-V108.png`](image/CLDTBDPL_06-08-vaitro-QTHT-thong-bao-Forbidden-khi-xuat-excel-V108.png)
> · phiếu lỗi: `bug-report.md` § BUG-CLDTBDPL-006.

---

## Mục 3 — Bộ lọc "Trạng thái chương trình" có 3 giá trị, đặc tả chỉ liệt kê 2 (đặc tả tự mâu thuẫn)

**Bối cảnh:** phát sinh khi verify `SLCTHT_06`. **Đối tác không nêu điểm này**, không thuộc case nào của
bảng theo dõi, **không** ảnh hưởng verdict.

**Web đang thế nào:** dropdown *Trạng thái chương trình* trên màn có **3** lựa chọn —
**Đã phê duyệt · Đang thực hiện · Hoàn thành**. Tệp xuất cũng có mục *Theo trạng thái* liệt kê đúng 3 nhóm
đó (ở dạng không lọc: Đã phê duyệt 5 · Đang thực hiện 1 · Hoàn thành 1, cộng bằng tổng 7).

**Đặc tả nói gì — hai chỗ không khớp nhau:**

- `srs-fr-11-bao-cao.md:897` — Input đặc thù FR-IX-20:
  `| 1 | trang_thai_ct | text | N | DANG_THUC_HIEN / HOAN_THANH | — | Chọn |` ⇒ chỉ **2** giá trị.
- `srs-fr-11-bao-cao.md:82` — Processing chung bước 4: *"Truy vấn dữ liệu: CHỈ bản ghi đã duyệt (trạng
  thái đã duyệt / hoàn thành / đã thanh toán)"* ⇒ tập dữ liệu vào báo cáo **có** nhóm *đã duyệt*, và
  `:907` đòi `tong_ct` là *"Tổng số CT"* — muốn tổng khớp thì phải đếm cả nhóm đã duyệt.

**Câu hỏi cụ thể cho BA:** bộ lọc *Trạng thái chương trình* của báo cáo này đúng ra có **2** hay **3**
giá trị? Nếu là 2 thì `tong_ct` (`:907`) có còn bao gồm các chương trình *Đã phê duyệt* không — vì hiện
tổng 7 lớn hơn hẳn tổng của 2 nhóm còn lại (1 + 1)?

**Đề xuất QA tạm thời:** **chưa** mở phiếu lỗi và **chưa** thêm dòng mới trên bảng theo dõi, vì đây là hai
chỗ trong chính đặc tả nói khác nhau chứ không phải phần mềm làm sai một quy định rõ ràng. Nếu BA chốt là
lỗi phần mềm, QA sẽ mở dòng mới trên tab `bug` theo quy tắc mã `SLCTHT_QA01` trong đợt kế tiếp.

---

# Bổ sung 2026-08-06 13:10 — phát sinh khi verify `CTTDVQL_04` (tab `bug`, dòng 272)

## Mục 4 — Nhãn kỳ báo cáo trong tệp Excel đang in mã nội bộ (`KHOANG`) thay vì chữ tiếng Việt như trên màn

**Bối cảnh:** phát sinh trên màn *Báo cáo thống kê → **BC Chương trình theo đơn vị*** (FR-IX-21/UC144), khi
đang kiểm chức năng Xuất Excel. **Đối tác không nêu điểm này**, không thuộc case nào của bảng theo dõi,
**không** kéo verdict của `CTTDVQL_04`.

**Web đang thế nào** (đo 2026-08-06 13:02–13:03, `18.143.165.120.nip.io`, bản dựng V1.0.8, tài khoản
`cbnv_tw_04`) — dòng thứ hai trong tệp Excel xuất ra:

| Kỳ báo cáo chọn trên màn | Màn hiển thị | Dòng thứ hai trong tệp Excel |
|---|---|---|
| Năm | *Kỳ: Năm* | *Kỳ báo cáo: **Năm** (từ 01/01/2026 đến 31/12/2026)* ✔ |
| Khoảng tùy chọn | *Kỳ: Khoảng* | *Kỳ báo cáo: **KHOANG** (từ 01/02/2026 đến 31/12/2026)* ✖ |

Tức cùng một tệp, cùng một chỗ, khi thì in nhãn tiếng Việt khi thì in **mã nội bộ viết hoa không dấu**.
Tệp này là bản người dùng gửi ra ngoài (đính kèm báo cáo, nộp lên cấp trên), nên chữ trong đó là chữ đối
ngoại.

**Đặc tả nói gì** (`Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md`):

- `:1092` — nội dung phần đầu tệp xuất: chỉ đòi *"chèn… thông tin kỳ"*, **không** nói nhãn kỳ phải là nhãn
  tiếng Việt hay mã.
- `:95` — Output chung, dòng kỳ báo cáo ghi format *"Kỳ đã chọn"* — đọc theo nghĩa thường thì là **cái người
  dùng đã chọn trên màn** (tức *"Khoảng"*), nhưng câu chữ không đủ dứt khoát để chấm phần mềm sai.

⇒ Đặc tả **im lặng**, không đủ căn cứ kết luận phần mềm vi phạm một quy định rõ ràng.

**Câu hỏi cụ thể cho BA:** nhãn kỳ báo cáo in trong tệp Excel/PDF phải là **nhãn tiếng Việt như trên màn**
(*Năm · Quý · Tháng · Khoảng*) hay chấp nhận in **mã nội bộ** (`NAM` · `QUY` · `THANG` · `KHOANG`)? Nếu chốt
là nhãn tiếng Việt thì cần áp cho **mọi** loại báo cáo dùng chung chức năng xuất, không riêng màn này.

**Đề xuất QA tạm thời:** **chưa** mở phiếu lỗi và **chưa** thêm dòng mới trên bảng theo dõi của đối tác. Nếu
BA chốt phải là nhãn tiếng Việt, QA sẽ mở dòng mới trên tab `bug` theo quy tắc mã `CTTDVQL_QA01` trong đợt
kế tiếp.

**Đường dẫn bằng chứng:** nội dung đầy đủ 3 tệp xuất (cả dòng nhãn kỳ của từng lượt) ở
[`image/CTTDVQL_04-thong-bao-va-phan-hoi-may-chu.txt`](image/CTTDVQL_04-thong-bao-va-phan-hoi-may-chu.txt)
· tệp gốc [`testfiles/BaoCaoCtTheoDonVi_20260806_1303.xlsx`](testfiles/BaoCaoCtTheoDonVi_20260806_1303.xlsx)
(kỳ Khoảng) và [`testfiles/BaoCaoCtTheoDonVi_20260806_1257.xlsx`](testfiles/BaoCaoCtTheoDonVi_20260806_1257.xlsx)
(kỳ Năm) · ảnh màn lúc chọn kỳ Khoảng:
[`image/CTTDVQL_04-A5-dang3-ky-Khoang-01.02-31.12-man-hinh-truoc-khi-xuat-V108.png`](image/CTTDVQL_04-A5-dang3-ky-Khoang-01.02-31.12-man-hinh-truoc-khi-xuat-V108.png).

---

# Bổ sung 2026-08-06 14:40 — phát sinh khi verify `CTTTG_04` (tab `bug`, dòng 281)

## Mục 5 — BC Chương trình theo thời gian có thống kê ngân sách không? (danh sách đầu ra của đặc tả không có, nhưng cũng không có câu bỏ)

**Bối cảnh:** phát sinh trên màn *Báo cáo thống kê → **BC Chương trình theo thời gian*** (FR-IX-23/UC146).
**Đối tác không nêu điểm này**, không thuộc case nào của bảng theo dõi, **không** kéo verdict của
`CTTTG_04`.

**Web đang thế nào** (đo 2026-08-06 14:30–14:36, `18.143.165.120.nip.io`, bản dựng V1.0.8 —
bó mã `assets/index-DIABnbIr.js`, tài khoản `cbnv_tw_04`): báo cáo hiện **3 thẻ** —
*Tổng chương trình toàn kỳ = 6* · *Tổng DN toàn kỳ = 0* · **Tổng ngân sách toàn kỳ = 250.000.000**;
biểu đồ có thêm đường *Tổng ngân sách*; bảng *Theo kỳ* có cột *Tổng ngân sách*; tệp Excel xuất ra cũng
có khối *Tổng ngân sách toàn kỳ* và cột *Tổng ngân sách (₫)*.

**Đặc tả nói gì** (`Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md`):

- `:1016`–`:1020` — Output đặc thù của FR-IX-23 chỉ liệt kê **3** mục: `trend_data[]` `{ky_label, so_ct}` ·
  `chart_type = LINE` · `tong_ct`. **Không** có mục ngân sách.
- `:1018` cho thấy khi BA muốn **bỏ** một mục thì có ghi rõ: *"[CTTLV_04 chốt 2026-07-24: **bỏ so_dn** …]"*.
  Với ngân sách thì **không có câu nào** như vậy.
- `:944` — loại BC anh em **FR-IX-21** (*BC Chương trình theo đơn vị*) **có** `tong_ngan_sach` trong danh
  sách đầu ra.

⇒ Đặc tả **im lặng** cho riêng loại BC này: không liệt kê, nhưng cũng không bỏ. Không đủ căn cứ kết luận
phần mềm vi phạm một quy định rõ ràng.

**Câu hỏi cụ thể cho BA:** *BC Chương trình theo thời gian* có thống kê **ngân sách** không?

1. Nếu **có** → bổ sung `tong_ngan_sach` (và cột ngân sách theo kỳ) vào danh sách đầu ra `:1016`–`:1020`
   để đặc tả khớp phần mềm.
2. Nếu **không** → phần mềm đang hiện thừa; cần ghi câu bỏ vào `:1016`–`:1020` giống cách đã làm với
   `so_dn` ở `:1018`, rồi dev gỡ khỏi thẻ + biểu đồ + bảng + tệp xuất.

**Đề xuất QA tạm thời:** **chưa** mở phiếu lỗi và **chưa** thêm dòng mới trên bảng theo dõi của đối tác.
Nếu BA chốt là hiện thừa, QA sẽ mở dòng mới trên tab `bug` theo quy tắc mã `CTTTG_QA01` trong đợt kế tiếp.

**Đường dẫn bằng chứng:** ảnh màn
[`image/CTTTG_04-A5-dang1-doluong-lai-tren-ban-dung-moi-truoc-khi-xuat.png`](image/CTTTG_04-A5-dang1-doluong-lai-tren-ban-dung-moi-truoc-khi-xuat.png)
· nội dung đầy đủ các tệp xuất ở
[`image/CTTTG_04-thong-bao-va-phan-hoi-may-chu.txt`](image/CTTTG_04-thong-bao-va-phan-hoi-may-chu.txt)
· tệp gốc [`testfiles/CTTTG_04-dang1-bandung-moi-DIABnbIr.xlsx`](testfiles/CTTTG_04-dang1-bandung-moi-DIABnbIr.xlsx).

> **Ghi chú:** trên cùng màn này còn **2 điểm khác** đã có đủ căn cứ đặc tả nên **không** đưa vào file hỏi
> BA mà xếp vào diện mở phiếu lỗi (đang chờ phiên chính duyệt mã dòng mới): (a) báo cáo vẫn thống kê
> *Số DN* dù `:1018` đã chốt bỏ `so_dn`; (b) không cấu hình nào trên màn cho ra biểu đồ trend nhiều điểm
> nên AC `:1023` (*"chọn 12 tháng → hiển thị biểu đồ trend"*) không với tới được bằng giao diện, dù máy
> chủ làm được. Chi tiết ở [`tieuchi/CTTTG_04.md`](tieuchi/CTTTG_04.md) mục 7.
