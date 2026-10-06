# Phép đo — LBCKQTHCT_06 (dòng 339) · 2026-08-07 — Khối **truy vết Chương trình HTPL liên quan**

**Verdict logic: CẦN BA** — vế chấm được (**C1 chọn được** + **C3 lưu/đọc lại được**) **ĐẠT đầy đủ**.
Nhưng khối **không hiện** khi làm đúng 2 bước phiếu mô tả, và đặc tả **im lặng** ở đúng điểm đó
⇒ Flow 04 cấm Pass lẫn Reopen. **Cùng một câu hỏi BA với phiếu LBCKQTHCT_05** — xem §5.

Chuẩn chấm: [`../chuan/LBCKQTHCT_06.md`](../chuan/LBCKQTHCT_06.md)

---

## 1. Điều kiện đo

| Mục | Giá trị |
|---|---|
| Env / bản dựng | `18.143.165.120.nip.io` · **`assets/index-D4Buvu4S.js`** (07/08/2026 02:23 VN), đọc lại tên bó mã trong tab |
| Tài khoản | **`cbnv_hn`** — `CB_NV_DP`, cấp ĐP, Sở Tư pháp Hà Nội (đúng tác nhân `:712`) |
| Đợt đo | `DOT-TRON_NAM-2026-1` (`a63a3214…`), đơn vị `DANG_LAP`, `baoCaoId 1b3085b8…` |

---

## 2. Gỡ blocker "không có chương trình để chọn" — khai đầy đủ

Lượt quét đầu: ô chọn **mở ra nhưng hiện `Trống`, 0 lựa chọn**. Chuẩn chấm §7 xếp đây là
**🚫 KHÔNG ĐO ĐƯỢC — nhóm A (thiếu seed)**, cấm chấm FAIL. Đã **phân loại trước khi seed**, không đoán:

| Bước phân loại | Kết quả |
|---|---|
| Ô chọn gọi endpoint nào? (cài bộ bắt **trước khi trang chạy**) | `GET /api/v1/chuong-trinh-htpls?page=1&pageSize=100` → **200**, **0 bản ghi** ⇒ FE gọi **đúng chỗ**, không phải lỗi giao diện |
| Hệ thống có chương trình nào không? (đối chứng ở phạm vi TW) | **14 chương trình**, nhưng **toàn bộ thuộc `Cục Bổ trợ tư pháp` (TW)** |
| Đơn vị đang đo sở hữu bao nhiêu? | **0** |

⇒ `Trống` là **phân quyền dữ liệu đúng** (`:732` — *"các CT **đơn vị** đã triển khai trong kỳ"*), **không phải lỗi**.
Nếu chấm FAIL ở đây là **Reopen oan**; nếu bỏ trống thì mất luôn kết luận về vế chính ⇒ **seed để gỡ**.

**Seed đã tạo (khai rõ vì thay đổi môi trường chung):**

| Mục | Giá trị |
|---|---|
| Người tạo | **`cbnv_hn`** (chính tài khoản đo — hợp lệ, CT thuộc đơn vị mình) |
| Endpoint | `POST /api/v1/chuong-trinh-htpls` — schema đọc từ `/api/docs-json`, không đoán tên trường |
| Bản ghi | **`CT-20260807-0001`** · id `99377050-220e-4111-8864-9098cb116367` · trạng thái `DU_THAO` |
| Chủ sở hữu | `donViId 00000000-0000-4000-8002-000000000001` = **Sở Tư pháp Hà Nội** ✅ |
| Ghi chú lưu trong bản ghi | *"Du lieu QA dung de kiem thu, co the xoa sau khi doi tac doc ket qua"* |

---

## 3. Kết quả — vế chấm được ĐẠT

### 3.1 C1 — khối tồn tại và chọn được

| Đo | Kết quả | SRS |
|---|---|---|
| Nhãn khối | **`Chương trình HTPL liên quan trong kỳ`** | `:732` |
| Dòng mô tả trên màn | *"Tùy chọn — dùng để truy vết các chương trình đơn vị đã triển khai trong kỳ báo cáo."* | gần **nguyên văn** `:732` (*"truy vết các CT đơn vị đã triển khai trong kỳ (tham khảo, không bắt buộc)"*) |
| Kiểu điều khiển | ô **chọn nhiều giá trị** có tìm kiếm (`ant-select-multiple`) | `:732` *"Multi-select FK → CHUONG_TRINH_HTPL"*, cột Nguồn = **"Chọn"** |
| Gợi ý trong ô | *"Chọn chương trình HTPL đã triển khai trong kỳ"* | — |
| Sau khi seed | dropdown hiện **đúng 1 lựa chọn** `CT-20260807-0001 — QA F5 seed CT…`, **chọn được** | ✅ |

### 3.2 C3 — lưu và đọc lại được

| Bước | Kết quả |
|---|---|
| Chọn chương trình → bấm [Lưu nháp] của thẻ Nhận xét | máy chủ nhận: `ctHtplIdsLienQuan = ["99377050-220e-4111-8864-9098cb116367"]` |
| **Tải lại trang bằng địa chỉ** | giao diện giữ **1 thẻ đã chọn**: `CT-20260807-0001 — QA F5 seed CT de do khoi truy vet (LBCKQTHCT_06)` |
| Đối chứng máy chủ sau tải lại | `ctHtplIdsLienQuan` = **đúng id của chương trình vừa chọn** |

⇒ **Hai đường khớp.** Không phải "khối chỉ có vỏ".
Ảnh: [`../image/LBCKQTHCT_06-khoi-truyvet-chon-va-doc-lai.png`](../image/LBCKQTHCT_06-khoi-truyvet-chon-va-doc-lai.png)

> ⚠️ **Hai lần suýt đo sai, ghi lại để không lặp:**
> 1. **Đếm gộp thẻ bọc với thẻ con.** Selector ban đầu khớp cả `.ant-select-selection-item` lẫn
>    `.ant-select-content-item` ⇒ trả về **2 dòng giống hệt** cho **1** lựa chọn. Đã đếm lại bằng node lá:
>    **1 chip**, không phải 2.
> 2. **Bộ đo thiếu, suýt kết luận "lưu im lặng".** Lượt bấm [Lưu nháp] cho ra *0 yêu cầu mạng* —
>    nhưng vì lượt đó tôi **chỉ vá `fetch`, chưa vá `XHR`**. Đã kiểm dữ liệu máy chủ: **đã lưu thật**.
>    ⇒ Đó là **dụng cụ thiếu**, KHÔNG phải hệ thống im lặng. Không log thành bug.

---

## 4. 🔴 Quan sát tái hiện được đúng bước phiếu mô tả

Phiếu chỉ ghi 2 bước: **1. Chọn menu "Đợt báo cáo" · 2. Mở Trang Chi tiết đợt báo cáo.**
Làm đúng 2 bước đó trên đợt mà đơn vị **chưa bắt đầu lập** (`trangThaiNop = CHUA_NOP`):

- Màn **chỉ có thẻ `Biểu mẫu 21a/TP/HTPLDN`**; **không** có thẻ `Nhận xét, kiến nghị` —
  mà **khối truy vết nằm BÊN TRONG thẻ đó** ⇒ khối truy vết **cũng không hiện**.
- Toàn màn **0 ô soạn**, **0 ô chọn**.

⇒ **Khiếu nại của đối tác không phải quan sát sai.** Khối chỉ xuất hiện **sau khi bấm [Lập báo cáo]**.
Ảnh dùng chung với phiếu 05:
[`../image/LBCKQTHCT_05-truoc-khi-lap-bc-khong-co-khoi-nhanxet.png`](../image/LBCKQTHCT_05-truoc-khi-lap-bc-khong-co-khoi-nhanxet.png)

**Nhưng cũng KHÔNG được Reopen:** bảng thành phần màn hình `:1163–1175` (11 dòng #35→#45) **hoàn toàn
im lặng** về khối này — không có dòng nào khai nó, nên **cũng không có** quy định nó phải là khối riêng,
đặt ở đâu, hay hiện ở trạng thái nào. Chuẩn chấm §7 ghi thẳng: *"KHÔNG chấm FAIL cho vế C2/C4… KHÔNG
Reopen vì lý do 'phải là một khối riêng'."*

---

## 5. CẦN BA CONFIRM — **cùng một câu hỏi với phiếu LBCKQTHCT_05**

> **CẦN BA CONFIRM:** đối tác kỳ vọng màn Chi tiết đợt báo cáo **có sẵn** khối truy vết *Chương trình HTPL
> liên quan* ngay khi mở màn.
> **SRS:** `srs-fr-15-ct-htpldn.md:732` khai đích danh `ct_htpl_ids_lien_quan[]` là **Input #9** của FR-XI-06,
> nguồn nhập **"Chọn"**, mô tả *"Multi-select FK → CHUONG_TRINH_HTPL — truy vết các CT đơn vị đã triển khai
> trong kỳ (tham khảo, không bắt buộc)"*; `:744` bước 6 khai đây là thao tác của cán bộ khi lập BC; `:745`
> + `:1417` khai lưu vào bản ghi báo cáo. **NHƯNG bảng thành phần màn hình `:1163–1175` KHÔNG có dòng nào
> cho khối này** ⇒ đặc tả **im lặng** về hình dạng, vị trí và điều kiện hiển thị của nó.
> **Web/dev hiện tại:** khối **có đủ và hoạt động đúng** (chọn được nhiều chương trình, lưu và đọc lại
> được sau khi tải lại trang); khối nằm **bên trong thẻ "Nhận xét, kiến nghị"**, và **chỉ hiện sau khi cán bộ
> bấm [Lập báo cáo]**.
>
> **Câu hỏi BA (chung cho cả LBCKQTHCT_05 và LBCKQTHCT_06 — chỉ cần trả lời một lần):**
> (1) Khi đơn vị **chưa vào pha lập báo cáo**, màn Chi tiết có phải hiển thị phần lập báo cáo
> (khối *Nhận xét, kiến nghị* **và** khối *Chương trình HTPL liên quan*) ở **dạng chỉ đọc** không,
> hay đúng là chỉ hiện khi bắt đầu lập?
> (2) Đề nghị **bổ sung một dòng cho khối truy vết chương trình liên quan** vào bảng thành phần màn hình
> Chi tiết đợt BC (hiện dừng ở dòng #45), ghi rõ kiểu điều khiển + vị trí + điều kiện hiển thị — để lần sau
> có căn cứ chấm thay vì phải suy từ phần Input của FR.
> (3) Khối này đặt **lồng trong thẻ "Nhận xét, kiến nghị"** có đúng ý đồ thiết kế không, hay phải tách thành
> khối riêng?
>
> ⚠️ Mục đích: **bổ sung/làm rõ đặc tả màn hình — KHÔNG chặn bàn giao.** Chức năng truy vết đã dùng được.

---

## 6. Quan sát ngoài vế — ghi nhận, không chấm

| # | Quan sát | Xử lý |
|---|---|---|
| 1 | Danh sách chương trình đổ vào ô chọn **không lọc theo trạng thái** — chương trình vừa tạo còn `DU_THAO` đã xuất hiện ngay | `:732` chỉ nói *"CT đơn vị đã triển khai trong kỳ"*, **không** khai bộ lọc trạng thái ⇒ SRS im lặng, ghi candidate. Có thể đáng hỏi BA cùng câu (2) nếu muốn siết |
| 2 | Danh sách **không lọc theo kỳ báo cáo** (đợt kỳ *Tròn năm* 2026 hiện CT bất kỳ của đơn vị) | Cùng lý do trên — ghi candidate |

---

## 7. Giới hạn hiệu lực

Chỉ có hiệu lực cho `18.143.165.120.nip.io` + bó mã `index-D4Buvu4S.js` (07/08/2026 02:23 VN).
Bằng chứng `LBCKQTHCT_06.jpg` **trùng md5 với `LBCKQTHCT_05.jpg`** (`c0fb9837447ee90ac8c8f975a298aaef`)
— một ảnh dùng cho hai khiếu nại về hai khối khác nhau, và ảnh chỉ bắt phần dưới trang. Vì vậy QA
**không** dựa vào ảnh mà tự tái hiện đúng các bước phiếu mô tả.

**Dữ liệu QA để lại trên môi trường:** đợt `DOT-TRON_NAM-2026-1` + chương trình `CT-20260807-0001`
— xoá được sau khi đối tác đọc xong kết quả.
