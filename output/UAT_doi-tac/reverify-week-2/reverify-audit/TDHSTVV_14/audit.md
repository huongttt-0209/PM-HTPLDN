# Audit verify vòng 2 — TDHSTVV_14

| Mục | Nội dung |
|---|---|
| **Mã ca kiểm thử** | TDHSTVV_14 (dòng 68, tab `UAT_TGPL Doanh Nghiệp-tuần 2`) |
| **Mô tả ca** | Gửi kết quả thẩm định — Kết luận "Không đạt" |
| **Phản ánh vòng 2 của đối tác** | "Người hỗ trợ không nhận được thông báo kèm lý do" |
| **Bằng chứng đối tác** | `TDHSTVV_13_v2.webm` (số hiệu tệp lệch một bậc — đối chiếu theo nội dung) |
| **Môi trường QA kiểm lại** | https://18.143.165.120.nip.io — `nht_qa_tw` (NHT, Cục Bổ trợ tư pháp) + `cbnv_tw` (CB_NV_TW, cùng đơn vị) |
| **Thời điểm** | 2026-07-27 15:28–15:40 |
| **Bảng đối chiếu điều kiện** | [`../../cond/TDHSTVV_14-r2.md`](../../cond/TDHSTVV_14-r2.md) — **0 GAP** |
| **Kết luận** | **BA confirm** (ý chính) + **Open** (1 lỗi phụ phát hiện kèm) |

---

## Cổng 1 — Bằng chứng đọc được gì

| Dữ kiện | Giá trị đọc từ video |
|---|---|
| Vai trò thẩm định | CB_NV_TW, badge "BTP · TW" |
| Thao tác | Thẻ Thẩm định → chọn **KHÔNG ĐẠT** → ô **Lý do** có nội dung (32 ký tự) → bấm **"Gửi KQ"** |
| Phản hồi ngay sau khi bấm | Hộp thông báo xanh **"Đã lưu kết quả thẩm định"** |
| Kiểm tra phía Người hỗ trợ | Đăng nhập tài khoản NHT → màn **Thông báo** → chỉ có **1** mục "Kích hoạt tài khoản…" ngày 11/05/2026, **không có** thông báo từ chối |
| **Khoảng trống của bằng chứng** | Video **không** chứng minh tài khoản NHT đó là người đã gửi hồ sơ `cb345570-…`; cũng **không** kiểm hộp thư email. QA đã bịt cả hai khoảng trống này ở Cổng 2 |

## Cổng 2 — Hiểu đúng bug đối tác báo

Đối tác báo **một** ý: sau khi hồ sơ bị kết luận "Không đạt", **Người hỗ trợ pháp lý** không nhận được thông báo kèm lý do.

Cách hiểu này bám theo cột "Kết quả mong đợi" của chính phiếu kiểm thử, trong đó ghi *"gửi thông báo kèm lý do đến **Người hỗ trợ**"*.

## Cổng 3 — Đối chiếu đặc tả

| # | Điểm đối chiếu | Đặc tả (`Docs-PM-HTPLDN/…/srs-v3.5/srs-fr-04-chuyen-gia-tvv.md`) | Bản đang chạy | Đánh giá |
|---|---|---|---|---|
| 1 | **Ai** là người nhận thông báo khi kết luận KHÔNG ĐẠT | `:522` — FR-IV-06 §Processing bước 6: *"Nếu KHONG_DAT: chuyển trạng thái TU_CHOI, gửi thông báo **TVV/CG (chủ hồ sơ)**"*. `:548` §Postconditions: *"**TVV/CG (chủ hồ sơ)** nhận thông báo (nếu cần bổ sung hoặc từ chối)"*. `:2325` SM-TVV dòng DANG_THAM_DINH → TU_CHOI: *"Thông báo **TVV/CG (chủ hồ sơ)** + ghi lý do"* | Thông báo gửi **email tới địa chỉ khai trên hồ sơ ứng viên**, nội dung có kèm nguyên văn lý do | **Khớp đặc tả.** Đặc tả **không** nêu tên Người hỗ trợ ở bất kỳ dòng nào của luồng này |
| 2 | Thông báo đi bằng kênh nào | `:595` — FR-IV-07 §Processing bước 4: *"Gửi thông báo TVV/CG (chủ hồ sơ) **qua email đã khai**"* ⇒ đặc tả xác định kênh là email tới địa chỉ khai trên hồ sơ | Đúng kênh email tới địa chỉ khai trên hồ sơ | **Khớp** |
| 3 | Trạng thái sau khi gửi kết quả | `:522` + `:2325` — chuyển sang **TU_CHOI** | Hồ sơ chuyển **TU_CHOI** (phiên bản 2 → 3) | **Khớp** |
| 4 | Ghi lý do | `:2325` — *"… + **ghi lý do**"* | Dữ liệu hồ sơ lưu `lyDo` đúng nguyên văn + `ngayThamDinh` | **Khớp** |
| 5 | *(QA phát hiện thêm)* Tiêu đề email từ chối | Không có dòng đặc tả quy định nội dung tiêu đề; nguyên tắc chung của đặc tả (`:198-199`, `:422`) là thông báo phải nói đúng bản chất sự việc | Tiêu đề trong thân email là **"✅ Phê duyệt: Hồ sơ bị từ chối"** — chữ "Phê duyệt" + dấu tích xanh trên một email báo **từ chối** | **Sai** — nội dung email mâu thuẫn chính nó |

**Kết luận Cổng 3:** ý đối tác báo **không** vi phạm dòng đặc tả nào. Quan sát của họ đúng sự thật (Người hỗ trợ không nhận được gì), nhưng **kỳ vọng** "Người hỗ trợ phải nhận thông báo" là kỳ vọng **nằm ngoài đặc tả** ⇒ theo QA_VERIFY_PROTOCOL, thuộc nhóm **`BA confirm`**, không phải `Open` và cũng không phải `Reject`.

---

## Các phép đo

### Đo 1 — Dựng lại tình huống, bịt luôn khoảng trống của video

| Bước | Thao tác | Kết quả đo |
|---|---|---|
| 1 | Đăng nhập `nht_qa_tw` (NHT, Cục Bổ trợ tư pháp) | `vaiTro = ["NHT"]`, mã đơn vị `…8000-000000000001` |
| 2 | Đọc danh sách thông báo **trước** thao tác (mốc so sánh) | Tổng **1** mục — "Kích hoạt tài khoản hệ thống PM-HTPLDN" ngày 12/07/2026; số chưa đọc = 1 |
| 3 | Chính tài khoản NHT này tạo hồ sơ tư vấn viên mới | Tạo thành công `TVV-BTP-TW-0021`, trạng thái **MOI_DANG_KY**, `nguoiTaoId` = chính tài khoản NHT ⇒ quan hệ "Người hỗ trợ ↔ hồ sơ" là chắc chắn |
| 4 | Đăng nhập `cbnv_tw` (cùng đơn vị) → mở hồ sơ → bấm **"Bắt đầu thẩm định"** | Trạng thái **MOI_DANG_KY → DANG_THAM_DINH** (phiên bản 1 → 2); thẻ **"Thẩm định"** xuất hiện |
| 5 | Thẻ Thẩm định: điền nhận xét 4 nhóm, tích "Có tham gia mạng lưới", chọn **KHÔNG ĐẠT**, nhập **Lý do** | Nút **"Gửi KQ"** hiện lên sau khi chọn KHÔNG ĐẠT |
| 6 | Bấm **"Gửi KQ"** (bộ bắt thông báo tự kiểm: `soObserverDangSong = 1`, không lọc trùng) | Lời gọi gửi kết quả trả **200**; trạng thái hồ sơ **DANG_THAM_DINH → TU_CHOI** (phiên bản 2 → 3); hộp thông báo hiện **"Đã lưu kết quả thẩm định"**. Số hộp thông báo cùng tồn tại tối đa = **1** ⇒ không phải lỗi hiện thông báo trùng |
| 7 | Đọc lại dữ liệu hồ sơ | `thamDinhMoiNhat.ketLuan = "KHONG_DAT"`, `thamDinhMoiNhat.lyDo` = đúng nguyên văn lý do đã nhập, `ngayThamDinh` có giá trị |

### Đo 2 — Người hỗ trợ có nhận được gì không?

| Nơi kiểm | Kết quả |
|---|---|
| Màn **Thông báo** trong ứng dụng của `nht_qa_tw` (đăng nhập lại sau thao tác) | Vẫn đúng **1** mục — "Kích hoạt tài khoản hệ thống PM-HTPLDN" 12/07/2026; số chưa đọc = 1. **Không** có thông báo từ chối ⇒ **giống hệt màn hình đối tác quay được** |
| Hộp thư của hệ thống | **Có** một email mới đúng thời điểm bấm "Gửi KQ" — nhưng người nhận là **địa chỉ email khai trên hồ sơ ứng viên** (`qa.tvv.tdhstvv14.r2@htpldn.gov.vn`), **không phải** địa chỉ của Người hỗ trợ |

Nội dung email (đã giải mã):

```
Tiêu đề thư : Hồ sơ bị từ chối
Người nhận  : qa.tvv.tdhstvv14.r2@htpldn.gov.vn   (email khai trên hồ sơ ứng viên)
Tiêu đề trong thân thư :
   ✅ Phê duyệt: Hồ sơ bị từ chối          <-- chữ "Phê duyệt" + tích xanh trên thư TỪ CHỐI
Nội dung :
   Hồ sơ TVV của bạn đã bị từ chối: QA verify TDHSTVV_14 - ho so khong dat,
   thieu chung chi hanh nghe               <-- CÓ kèm nguyên văn lý do
```

⇒ **Thông báo kèm lý do có được gửi**, chỉ là gửi cho **chủ hồ sơ qua email**, không phải cho Người hỗ trợ trong ứng dụng.

### Đo 3 — Vì sao đây là câu hỏi đáng hỏi BA

Ở thời điểm bị từ chối, hồ sơ mới ở nhánh **Mới đăng ký → Đang thẩm định**. Theo `:2326` (SM-TVV), hệ thống **chỉ tự cấp tài khoản cho tư vấn viên khi Cán bộ Phê duyệt duyệt** (CHO_PHE_DUYET → CHO_KICH_HOAT). Nghĩa là **ứng viên bị từ chối ở bước thẩm định chưa hề có tài khoản** trong hệ thống.

Hệ quả thực tế: email báo từ chối đi tới hộp thư ứng viên, còn **trong ứng dụng thì không ai** — kể cả Người hỗ trợ đã nộp hồ sơ thay ứng viên — nhìn thấy kết quả này. Đây là điểm đặc tả chưa nói, cần BA chốt.

---

## Verdict

| # | Ý | Kết quả verify | Verdict ý |
|:-:|---|---|---|
| 1 | "Người hỗ trợ không nhận được thông báo kèm lý do" | **Quan sát ĐÚNG** (NHT không nhận được gì trong ứng dụng) nhưng **không sai đặc tả**: `:522`/`:548`/`:2325` chỉ định người nhận là **chủ hồ sơ**, `:595` chỉ định kênh là **email đã khai**, và email đó **đã được gửi kèm lý do** | **BA confirm** |
| 2 | *(QA phát hiện thêm)* Email báo từ chối mang tiêu đề "✅ Phê duyệt: Hồ sơ bị từ chối" | Đo trực tiếp trên nội dung thư | **Open** (Minor) |

**Verdict tổng ghi lên phiếu: `BA confirm, Open`** — ý chính chờ BA, kèm 1 lỗi phụ đã log cho dev.

**Vì sao KHÔNG `Reject`:** `Reject` chỉ dùng khi chứng minh được đối tác thao tác/hiểu sai hoặc báo cáo vô hiệu. Ở đây thao tác của họ đúng, quan sát của họ đúng sự thật, chỉ có **kỳ vọng** là nằm ngoài đặc tả ⇒ theo protocol thuộc nhóm `BA confirm`.

**Vì sao KHÔNG `Open` cho ý 1:** không dẫn được dòng đặc tả nào bị vi phạm; trái lại `:522`/`:548`/`:595`/`:2325` đều khớp với hành vi đang chạy.

## Câu hỏi gửi BA

1. Khi Cán bộ Nghiệp vụ kết luận **Không đạt** ở bước thẩm định, **Người hỗ trợ pháp lý đã nộp hồ sơ** có phải nhận thông báo kèm lý do không? Đặc tả (`:522`, `:548`, `:2325`) chỉ nêu **chủ hồ sơ**.
2. Nếu **có**, thông báo cho Người hỗ trợ đi kênh nào — thông báo trong ứng dụng, email, hay cả hai?
3. Ứng viên bị từ chối ở bước thẩm định **chưa có tài khoản** trong hệ thống (`:2326` — tài khoản chỉ được cấp sau khi Cán bộ Phê duyệt duyệt). Vậy kết quả từ chối có cần hiện ở **thông báo trong ứng dụng** cho một vai trò nào đó (Người hỗ trợ / Cán bộ Nghiệp vụ) để còn theo dõi được không?
4. Thông báo hiện ra sau khi bấm "Gửi KQ" với kết luận Không đạt đang là **"Đã lưu kết quả thẩm định"**, trong khi phiếu kiểm thử của đối tác mong đợi câu phản ánh đúng việc hồ sơ đã bị từ chối. Đặc tả không quy định câu chữ này — BA muốn chốt theo hướng nào?

## Dữ liệu để lại

`TVV-BTP-TW-0021 — QA TVV TDHSTVV14 R2` (Cục Bổ trợ tư pháp, trạng thái **Từ chối**, lý do đã ghi) do QA dựng để tái hiện. **Giữ lại** cho dev/BA đối chiếu.

## Ghi chú nội bộ (KHÔNG đưa vào note phiếu)

Trong lúc đo, nút **"Bắt đầu thẩm định"** hoạt động **đúng đặc tả** (`:1545`): Mới đăng ký → Đang thẩm định, thẻ "Thẩm định" chỉ xuất hiện sau đó. Điều này **khác** với kết quả đo sáng cùng ngày ở audit `TDHSTVV_08` (khi đó nút không xuất hiện và thẻ Thẩm định mở ngay ở trạng thái Mới đăng ký). Bản triển khai đã đổi trong ngày — cần đo lại `TDHSTVV_08` trước khi dev đóng bug đó.
