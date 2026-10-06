# BA confirmation needed — `QLHSPLDN_15` — 2026-08-07

> **Dạng B′ — đặc tả IM LẶNG** (SRS không có dòng nào về điểm đang xét; khác với "hai chỗ nói ngược nhau").
> Bộ mục theo Dạng B, chỉ đổi tên mục thứ ba thành *Điểm đặc tả im lặng / chưa rõ*.

> **Quy tắc citation:** mọi khẳng định SRS đều trỏ `path/tới/file-srs.md:LINE`, đã mở file đọc từng dòng trong
> chính lượt này. Nguồn duy nhất: `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/`.

> **Quan hệ với file tổng hợp:** [`cau-hoi-BA-tong-hop-2026-08-06.md`](cau-hoi-BA-tong-hop-2026-08-06.md) có
> 1 dòng trỏ sang đây trong Mục lục; nội dung **không** lặp ở file đó.

---

## Bối cảnh testcase

- Dòng Excel: **297**, tab `bug` (gid 1714340219), mã TC `QLHSPLDN_15` — *"Xuất Excel Không có dữ liệu"*.
- Màn: *Chi tiết doanh nghiệp → tab **Hồ sơ pháp lý*** (`SCR-V.III-02`, `/doanh-nghiep/{id}?tab=ho-so-pl`),
  vai trò **CB_NV_TW**.
- Ô *Kết quả mong đợi* của đối tác: hệ thống hiển thị thông báo **"Không có dữ liệu để xuất"**.
- Đối tác báo *"Màn hình không có nút chức năng"* (env nghiệm thu, 17/07/2026) nên **chưa từng chạy tới bước này**.
- **Dòng 297 đang treo verdict** — QA không tự chốt được vì đặc tả im lặng đúng ở điểm đối tác kỳ vọng.
  Đã ghi `Trạng thái dev fix = BA confirm` chờ BA.

## Kết quả verify UI hiện tại

Đo 2026-08-07 00:11 · env nội bộ `https://18.143.165.120.nip.io` · bản dựng `HTPLDN · V1.0.9`, bó mã
`assets/index-CxS5qW_0.js`, `last-modified 06/08/2026 12:48:25 GMT` · tài khoản `cbnv_tw_02` · DN `DN-HNI-0001`.

- Lọc từ khóa không khớp bản ghi nào (`zzqqxx-khongtontai`) → bảng **0 dòng** → bấm **Xuất Excel**.
- Bắt được **đúng 1 thông báo**, nguyên văn **"Không có dữ liệu để xuất"** — **trùng khít** câu chữ đối tác kỳ
  vọng. Bấm lặp lần 2: vẫn đúng 1 thông báo, không nhân đôi.
- Đối chứng độc lập: **0 lượt gọi máy chủ**, **không tệp nào được tạo** ⇒ hệ thống **chặn xuất**, không trả tệp rỗng.
- Ảnh: [`../F4-pilot-QLHSPLDN-2026-08-07/image/QLHSPLDN_15-C5b-khong-co-du-lieu-de-xuat.png`](../F4-pilot-QLHSPLDN-2026-08-07/image/QLHSPLDN_15-C5b-khong-co-du-lieu-de-xuat.png)
- Chi tiết phép đo: [`../F4-pilot-QLHSPLDN-2026-08-07/bao-cao-lo-2026-08-07.md`](../F4-pilot-QLHSPLDN-2026-08-07/bao-cao-lo-2026-08-07.md)

> Vế còn lại của cùng phiếu — **chuỗi lọc rồi xuất** — đã đo và **đạt**: lọc còn 2 dòng thì tệp xuất ra đúng
> 2 dòng, `GET /api/v1/ho-so-phap-ly-dns/export?…&keyword=QA-W5` mang theo bộ lọc. Vế đó **không** cần BA.

## Điểm đặc tả im lặng / chưa rõ trong SRS v3.5

- `srs-fr-12-tv-chuyen-sau.md:657-665` — `FR-X.1-04` **§Processing — Xuất Excel** đặc tả đủ 5 bước (áp bộ lọc
  `:662` · giới hạn 10.000 dòng `:663` · 8 cột `:664` · trả tệp `:665`) nhưng **không nói gì** về trường hợp bộ
  lọc ra 0 bản ghi.
- `srs-fr-12-tv-chuyen-sau.md:693-701` — bảng **Error Handling** của chính `FR-X.1-04` liệt kê đủ **E1→E7**,
  trong đó `E7 / INF-HSPL-01` là *"Không có kết quả tìm kiếm"* → *"Không tìm thấy hồ sơ pháp lý phù hợp"*.
  **Không có mã nào** cho tình huống **xuất Excel** khi bộ lọc rỗng. Đây là **im lặng**, không phải mâu thuẫn.
- Module khác **đã có** quy định cho đúng tình huống này, với **câu chữ khác nhau**:
  - `srs-fr-13-tv-nhanh.md:155` — `E5 / INF-KHO-XL-01`: *"Không có dữ liệu để xuất"* — **chặn xuất, không tạo
    tệp rỗng** `[BA-07 tuần 4]` (Kho câu hỏi).
  - `srs-fr-15-ct-htpldn.md:403` — `E1 / INF-XI-02-XL-01`: *"Không có chương trình nào để xuất"* (CT HTPLDN).
- Đã soát cả `srs-v3.5.md:5570` (`BR-DATA-06` — *"Mọi danh sách có tính năng xuất Excel… không vượt quá 10.000
  rows/file"*): quy định **giới hạn trên**, không nói gì về tập rỗng.

## Câu hỏi cần BA xác nhận

Hồ sơ pháp lý DN (`FR-X.1-04`) có áp cùng hành vi **"chặn xuất, không tạo tệp rỗng"** như `INF-KHO-XL-01` không?

1. Nếu **có** → xin BA cấp **mã lỗi + câu chữ chính thức** cho `FR-X.1-04`: dùng lại đúng câu *"Không có dữ liệu
   để xuất"* (giống Kho câu hỏi), hay đặt câu riêng theo đối tượng như nhóm XI (*"Không có hồ sơ nào để xuất"*)?
   Bản dựng hiện tại đang dùng **đúng câu của Kho câu hỏi**.
2. Nếu **không áp** → xin BA xác nhận rõ hệ thống **được phép** trả tệp rỗng, để QA đóng vế này và ghi lại cho
   các lượt sau.

## Đề xuất QA tạm thời

- **Chưa** mở phiếu lỗi và **chưa** chấm Pass cho dòng 297: đặc tả không có dòng nào để chấm, nên kết quả web
  dù trùng khít kỳ vọng đối tác cũng **không** đủ tư cách làm chuẩn chấm.
- Nếu BA chọn (1) thì nên chốt luôn **quy ước dùng chung** cho mọi màn có nút Xuất Excel — hiện đã có **2 câu
  chữ khác nhau** ở 2 module (`INF-KHO-XL-01` và `INF-XI-02-XL-01`), dễ tiếp tục lệch ở màn thứ ba.
