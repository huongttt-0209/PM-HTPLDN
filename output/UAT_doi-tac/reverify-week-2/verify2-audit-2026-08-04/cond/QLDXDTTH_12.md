# QLDXDTTH_12 — Bảng đối chiếu điều kiện (VÒNG SOÁT LẠI 2, 2026-08-04)

> Sheet `UAT_TGPL Doanh Nghiệp-tuần 2` row 136 · Verdict Verify 2: `Pass`
> Bug gốc: *"Màn gửi đề xuất và màn chi tiết đề xuất **lộ mã kỹ thuật** của lĩnh vực ra cho người dùng"* —
> ô chọn hiện `"DAN_SU - Dân sự"`, `"THUE - Thuế"`, `"SHTT - Sở hữu trí tuệ"`…, màn chi tiết hiện
> `"Lĩnh vực: DAN_SU - Dân sự"`, trong khi cột "Lĩnh vực" của bảng danh sách lại hiện đúng `"Dân sự"`.
> Kết quả mong đợi của phiếu: *"Người dùng **chỉ** nhìn thấy tên lĩnh vực bằng tiếng Việt"*.
> Dev khai lần 1: *"Đã fix: ô chọn Lĩnh vực + bộ lọc + chi tiết chỉ hiển thị tên tiếng Việt (bỏ prefix mã)"*.
> Bug phụ thuộc **vai trò + từng màn hình + từng giá trị lĩnh vực** ⇒ điền bảng này (không dùng `--static-bug`).

**Môi trường soát lại 2:** `https://htpldn-uat.ospgroup.vn` · `HTPLDN · V1.0.5` · gói giao diện **`index-DpIXRGaI.js`**.

| Điều kiện có thể đổi kết quả | Điều kiện bug gốc | Mình test (soát lại 2, 04/08/2026) | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | *"Đăng nhập tài khoản **Doanh nghiệp hoặc Cán bộ nghiệp vụ**"* (phiếu cho phép cả hai) | Đo bằng **cả hai**: (1) **`0311224477`** — `QA Kiem Chung`, vai trò **`DN`**, `BTP · DP`; (2) **`cbnv_tw`** — `Cán bộ NV Trung ương`, vai trò **`CB_NV_TW`**, `BTP · TW`. Mọi màn kiểm dưới đây đều chạy lại đủ ở cả 2 vai trò | Không |
| Chỗ 1 — **ô chọn "Lĩnh vực" khi gửi đề xuất mới** | *"Bấm 'Gửi đề xuất mới', mở ô chọn 'Lĩnh vực'"* → khi đó hiện `DAN_SU - Dân sự`… | Mở hộp thoại **"Gửi đề xuất đào tạo"** ở cả 2 vai trò, bung danh sách chọn: **10 lựa chọn, 100% chỉ có tên tiếng Việt** — `Thuế · Lao động · Đất đai · Dân sự · Thương mại · Hình sự · Hành chính · Sở hữu trí tuệ · Doanh nghiệp · Đầu tư`. Chọn thử **`Sở hữu trí tuệ`** (giá trị mà phiếu nêu đích danh là `SHTT - …`): ô sau khi chọn hiện đúng `Sở hữu trí tuệ`, thuộc tính chú thích khi rê chuột cũng là `Sở hữu trí tuệ` | Không |
| Chỗ 2 — **bộ lọc "Lĩnh vực" trên danh sách đề xuất** | Dev khai đã sửa cả bộ lọc; phiếu yêu cầu người dùng chỉ thấy tên tiếng Việt | Bung bộ lọc ở cả 2 vai trò: **10 lựa chọn, đều chỉ có tên tiếng Việt**. Lọc thật theo `Dân sự` (vai trò cán bộ): danh sách rút từ **16 → 5 bản ghi**, cả 5 đều đúng lĩnh vực `Dân sự`, **nhãn đã chọn trên ô lọc hiện `Dân sự`** (không kèm mã) | Không |
| Chỗ 3 — **màn chi tiết đề xuất** | *"Mở màn chi tiết của một đề xuất bất kỳ, xem dòng 'Lĩnh vực'"* → khi đó hiện `Lĩnh vực: DAN_SU - Dân sự` | Mở chi tiết ở cả 2 vai trò: bản ghi của chính đối tác *"TKM gửi đề xuất đào tạo cán bộ nghiệp vụ quý 3/2026"* (vai trò cán bộ) và bản ghi `QA-V2-0804` (vai trò doanh nghiệp) → dòng **"Lĩnh vực: Dân sự"**, không có mã | Không |
| Màn hình phát sinh thêm (kiểm rộng hơn phiếu) | Phiếu chỉ nêu 3 chỗ | Kiểm thêm **hộp thoại "Cập nhật đề xuất đào tạo"** (nút **Sửa** của doanh nghiệp) — chỗ ô chọn được **điền sẵn giá trị đã lưu**, dễ sót nhất khi sửa lỗi hiển thị: vẫn hiện đúng `Dân sự`. Và **cột "Lĩnh vực" của bảng danh sách** (chỗ vốn đã đúng từ đầu) vẫn đúng: `Sở hữu trí tuệ · Dân sự · Đất đai · Thuế · Lao động · Doanh nghiệp` | Không |
| Dữ liệu đầu vào — số giá trị của danh mục | *"Danh mục lĩnh vực pháp luật đang có **10 giá trị**"* | Đếm được **đúng 10** lựa chọn ở cả ô chọn khi tạo lẫn bộ lọc, ở cả 2 vai trò ⇒ không thiếu giá trị nào, không có giá trị nào bị bỏ sót khỏi phép kiểm | Không |
| Nguồn dữ liệu — mã kỹ thuật còn tồn tại hay không | Phiếu ngầm định mã kỹ thuật là thứ **có thật** trong dữ liệu và bị rò ra màn hình | Gọi thẳng dịch vụ dữ liệu của đúng phiên đăng nhập: mỗi bản ghi vẫn trả **cả mã lẫn tên** (`ma: "SHTT" / ten: "Sở hữu trí tuệ"`, `ma: "DAN_SU" / ten: "Dân sự"`) ⇒ mã **vẫn còn** trong dữ liệu, nhưng **không màn hình nào hiển thị nó** — tức là sửa thật ở phần hiển thị, không phải "may mà dữ liệu không có mã" | Không |

## Đo được

- Danh sách lựa chọn (ô tạo + bộ lọc, cả 2 vai trò), đọc bằng chữ **nhìn thấy** (`innerText`):
  `Thuế · Lao động · Đất đai · Dân sự · Thương mại · Hình sự · Hành chính · Sở hữu trí tuệ · Doanh nghiệp · Đầu tư` — **0/10** lựa chọn kèm mã.
- Quét toàn bộ chữ hiển thị của trang danh sách + trang chi tiết + hộp thoại tạo/sửa để tìm 10 mã kỹ thuật
  (`DAN_SU`, `THUE`, `LAO_DONG`, `SHTT`, `DAT_DAI`, `THUONG_MAI`, `HINH_SU`, `HANH_CHINH`, `DOANH_NGHIEP`, `DAU_TU`):
  **không khớp chỗ nào** — kể cả trong chú thích rê chuột (`title`) và chữ mờ gợi ý trong ô nhập (`placeholder`).
- Lọc theo `Dân sự`: **16 → 5 bản ghi**, đúng 5/5 bản ghi có lĩnh vực `Dân sự` ⇒ bộ lọc không chỉ hiển thị đúng mà còn **chạy đúng**.

## Đã cố BÁC BỎ kết luận `Pass` cũ bằng những cách nào

1. **Không chấm bằng nhìn lướt một màn.** Kiểm **đủ 3 chỗ phiếu nêu**, mỗi chỗ chạy lại ở **cả 2 vai trò** mà phiếu cho phép — tổng 6 lượt quan sát.
2. **Kiểm thêm chỗ phiếu không nêu** (hộp thoại **Cập nhật đề xuất**) — đây là chỗ ô chọn phải **hiển thị lại giá trị đã lưu**, khác đường mã với lúc bung danh sách, nên hay sót nhất khi dev chỉ sửa phần bung danh sách. Vẫn sạch.
3. **Chọn đúng giá trị mà phiếu réo tên** (`SHTT - Sở hữu trí tuệ`, `DAN_SU - Dân sự`) chứ không chọn giá trị dễ.
4. **Loại giả thuyết "sạch vì dữ liệu không còn mã"**: gọi thẳng dịch vụ dữ liệu, thấy **mã vẫn được trả về** kèm tên ⇒ nếu phần hiển thị chưa sửa thì mã đã phải hiện ra. Đây là phép thử quyết định.
5. **Loại khả năng mã bị giấu ở chỗ khó thấy**: quét cả chú thích rê chuột và chữ gợi ý trong ô nhập, không chỉ chữ hiển thị.
6. **Kiểm cả tính đúng của bộ lọc**, không chỉ cái nhãn — vì "bỏ mã" mà làm hỏng lọc thì cũng là `Reopen`; lọc vẫn ra đúng 5/5.

**Kết luận: 0 GAP.** Cả 3 chỗ phiếu nêu (và 1 chỗ kiểm thêm) đều **chỉ hiện tên tiếng Việt**, ở cả 2 vai trò, trên đủ 10 giá trị của danh mục, trong khi dữ liệu **vẫn còn mã kỹ thuật** ⇒ triệu chứng cũ **không tái hiện** ⇒ verdict `Pass`.
