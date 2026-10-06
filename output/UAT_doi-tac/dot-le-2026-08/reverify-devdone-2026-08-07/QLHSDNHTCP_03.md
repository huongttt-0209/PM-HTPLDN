# QLHSDNHTCP_03 — Re-verify sau dev fix (dòng 72, tab `bug`)

**Ngày đo:** 2026-08-07 · **Verdict:** ✅ PASS (vế dev fix) — **còn 1 câu hỏi BA chưa được trả lời**
**Môi trường:** https://18.143.165.120.nip.io — ứng dụng `HTPLDN · V1.0.10`, bó mã giao diện `index-BbPPdate.js`
(tải lại trang và đọc lại tên bó mã trong tab trước khi đo; mới hơn bản QA đo lượt trước lúc 10:42–10:58 cùng ngày).
**Vai trò đo:** `cbnv_tw_02` (CB Nghiệp vụ - Trung ương) và `cbpd_tw_02` (CB Phê duyệt - Trung ương) — bộ tài khoản 02.

---

## Phạm vi lượt này

Chỉ kiểm **yêu cầu sắp xếp mặc định theo ngày cập nhật giảm dần** — đúng phạm vi mà lượt trước đã khoanh.
Hai vế SLA đã đạt ở lượt trước (đủ 4 mức cảnh báo · không tràn/đè sang cột Ngày nộp) không đo lại.

Chuẩn chấm: ô "Kết quả mong đợi" của phiếu — *"Mặc định: hệ thống sắp xếp theo ngày cập nhật mới nhất trước,
20 bản ghi mỗi trang"* — và `srs-fr-06-chi-tra.md:1081` *"Sắp xếp mặc định: ngày cập nhật DESC"*.

---

## Vế ĐÃ HẾT LỖI — thứ tự mặc định đã đúng

Mở màn Chi trả chi phí, tab "Tất cả", **không nhập từ khóa, không bật bộ lọc, không bấm vào tiêu đề cột nào**.
Yêu cầu danh sách mà màn hình tự gửi **không kèm bất kỳ tham số sắp xếp nào** → thứ tự đang thấy chính là
thứ tự mặc định của máy chủ.

**Thứ tự trang 1 (giống hệt ở cả 2 vai trò) và ngày cập nhật tương ứng:**

| # | Mã hồ sơ | Ngày cập nhật | Ngày tạo |
|---:|---|---|---|
| 1 | CT-SEED-102 | 07/08/2026 00:00 | 20/07/2026 |
| 2 | CT-QA-QLHSDNHTCP-15-120 | 05/08/2026 03:47 | 05/08/2026 |
| 3 | CT-SEED-104 | 05/08/2026 00:00 | 20/07/2026 |
| 4 | CT-SEED-106 | 04/08/2026 01:53 | 20/07/2026 |
| 5 | CT-QAW7-NORMAL | 03/08/2026 12:00 | 25/07/2026 |
| 6 | CT-SEED-105 | 31/07/2026 00:00 | 20/07/2026 |
| 7 | CT-SEED-101 | 29/07/2026 00:00.180 | 20/07/2026 |
| 8 | CT-SEED-103 | 29/07/2026 00:00.114 | 20/07/2026 |
| 9 | CT-QAW7-OVERDUE | 25/07/2026 03:30 | 25/07/2026 |
| 10 | CT-QAW7-CLOSED | 25/07/2026 03:23 | 25/07/2026 |
| 11 | CT-SEED-107 | 20/07/2026 11:00 | 20/07/2026 |
| 12–14 | CT-SEED-108 · CT-SEED-110 · CT-SEED-109 | 20/07/2026 10:33 (bằng nhau) | 20/07/2026 |

**Kết luận đo:** ngày cập nhật **giảm dần liên tục từ dòng 1 tới dòng 14**, không có cặp nào hồ sơ cập nhật
mới hơn lại đứng dưới hồ sơ cập nhật cũ hơn.

**Hai phép thử phân biệt được "ngày cập nhật" với "ngày tạo"** (nên kết quả không phải trùng hợp):

- `CT-SEED-102` có ngày tạo **cũ nhất** (20/07) nhưng ngày cập nhật **mới nhất** (07/08) → đứng **dòng 1**.
  Chính hồ sơ này ở lượt đo trước nằm **dòng 11**.
- `CT-QA-QLHSDNHTCP-15-120` có ngày tạo mới nhất (05/08) nhưng vẫn xếp **sau** `CT-SEED-102`.

Nếu danh sách còn sắp theo ngày tạo thì thứ tự đầu trang phải là `CT-QA-QLHSDNHTCP-15-120` → `CT-QAW7-NORMAL`
→ nhóm `CT-QAW7-*`; thực tế không phải vậy.

**Đối chứng độc lập:** đọc lại ngày cập nhật của đúng các mã đang hiển thị từ phản hồi danh sách rồi so theo
đúng thứ tự trên màn — trùng khít ở cả 2 vai trò, không có sai lệch.

![Vai trò CB Nghiệp vụ TW](image/QLHSDNHTCP_03-01-cbnv-tw-02-sap-xep-mac-dinh.png)
![Vai trò CB Phê duyệt TW](image/QLHSDNHTCP_03-02-cbpd-tw-02-sap-xep-mac-dinh.png)

> Ghi chú thao tác: với vai trò phê duyệt, màn tự mở vào tab "Chờ phê duyệt" (đang rỗng — đúng, vì không có hồ sơ
> nào ở trạng thái đó). Phải bấm sang tab "Tất cả" mới đo được thứ tự mặc định. Đây là hành vi theo vai trò,
> không phải lỗi.

---

## Vẫn CHƯA ĐƯỢC CHẤM — câu hỏi BA từ lượt trước chưa có trả lời

Cột SLA vẫn hiển thị nhãn thứ 5 **"Đã hoàn thành"** cho 4 hồ sơ đã kết thúc: `CT-QAW7-CLOSED` và `CT-SEED-108`
(Đã thanh toán), `CT-SEED-110` (Hủy), `CT-SEED-109` (Từ chối).

Đặc tả chỉ quy định **4 mức** cảnh báo SLA — `srs-fr-06-chi-tra.md:1058` (cột SLA: Bình thường / Sắp hết hạn /
Quá hạn / Quá hạn nghiêm trọng, điều kiện hiển thị ghi **"Luôn"**) và `:1523` (quy tắc ưu tiên mức, *"nếu không
thỏa điều kiện nào thì hiển thị Bình thường"*). Đã rà toàn bộ tài liệu Chi trả: **không có dòng nào** nói cách
hiển thị SLA với hồ sơ đã kết thúc, và bảng quy tắc gốc BR-SLA-02 để cột "Ngoại lệ" trống.

**BA cần chốt:** với hồ sơ đã kết thúc — giữ nhãn "Đã hoàn thành", hiển thị một trong 4 mức, hay không hiển thị SLA?
Trước khi có trả lời, điểm này **không được chấm là đạt cũng không được chấm là lỗi**.

---

## Phạm vi đã đo

2 vai trò (nghiệp vụ TW, phê duyệt TW) · 14 hồ sơ trang 1 · mỗi vai trò đo cả trên màn và bằng đối chứng dữ liệu
danh sách · không bấm tiêu đề cột, không đặt bộ lọc.
