# Báo cáo cuối lô — B6 Vụ việc HTPL (verify bug dev đã fix)

| | |
|---|---|
| **Lô** | B6 — Vụ việc HTPL · 5 case / 1 menu |
| **Nguồn** | Bảng theo dõi, tab `bug` — dòng 45 · 50 · 51 · 62 · 64 |
| **Đặc tả đối chiếu** | `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/` |
| **Môi trường đo** | `https://18.143.165.120.nip.io` (nội bộ) |
| **Ngày** | 2026-08-06 |
| **Trạng thái** | ✅ **ĐÃ XONG 5/5 case** — cập nhật lần cuối 2026-08-06 17:20 |

## Kết quả từng case

| Dòng | Mã TC | Verdict | Đã ghi vào ô `Trạng thái dev fix` |
|---:|---|---|---|
| 45 | KTHSYCHTPL_11 | ✅ Pass | `Test done` |
| 50 | TKHSYCHTPL_03 | ✅ Pass | `Test done` |
| 51 | XNTGHTVV_03 | 🔁 Reopen | `Reopen` |
| 62 | CNKQHT_07 | ✅ Pass | `Test done` |
| 64 | DGKQHTVV_01 | 🔁 Reopen | `Reopen` |

---

## 1. Lỗi phát hiện ngoài phạm vi 5 case

| Mã | Nội dung | Đã xử lý thế nào |
|---|---|---|
| `KTHSYCHTPL_QA01` (dòng 364) | Dòng thời gian vụ việc chỉ hiện sự kiện do **chính người đang đăng nhập** thực hiện. Cán bộ khác — kể cả cùng vai trò, cùng đơn vị — mở đúng vụ việc đó thấy "Chưa có lịch sử hoạt động". Hệ quả: không truy được lịch sử xử lý khi bàn giao giữa hai cán bộ. | Đã mở **dòng mới** trên bảng (`Trạng thái`=Fail, `Dopai`=bug) kèm liên kết ảnh xem được. Phiếu nội bộ: `BUG-VV-LICHSU-THEO-NGUOI`. Gặp lại khi verify CNKQHT_07 → **không log trùng**. |

Case **DGKQHTVV_01** (dòng 64) **không mở thêm dòng bug mới**: việc doanh nghiệp không mở được chi tiết vụ
việc của chính mình có **cùng gốc** với vế "không có điểm vào đánh giá" mà đối tác đã phản ánh (cùng một
rào quyền theo vai trò), nên đã ghi trong chính phiếu `BUG-VV-DGKQHTVV-01` thay vì tách phiếu riêng —
tránh hai dòng cùng một nguyên nhân. Rào quyền này còn chặn cả các chức năng khác của doanh nghiệp trên
màn chi tiết; nếu người phụ trách bảng muốn theo dõi riêng thì mở 1 dòng mới, lô này **không tự mở**.

**8 điểm cần BA chốt** (`cau-hoi-BA.md`) — chưa chốt thì không kết luận đúng/sai được:

| # | Case | Câu hỏi |
|---:|---|---|
| 1 | KTHSYCHTPL_11 | Nhãn lựa chọn kết luận "Đạt — chuyển sang phân công" hứa một việc mà hệ thống cố ý không làm |
| 2 | TKHSYCHTPL_03 | Mã của mức "Sắp hết hạn" là `SAP_HET` hay `SAP_HET_HAN` — **đặc tả tự mâu thuẫn** giữa các tài liệu |
| 3 | TKHSYCHTPL_03 | Bộ lọc chỉ chạy khi bấm [Tìm kiếm], trong khi đặc tả ghi "change → filter" |
| 4 | TKHSYCHTPL_03 | Hồ sơ chưa có thời hạn xử lý vẫn lọt bộ lọc "Bình thường" và hiện dấu "—" |
| 5 | CNKQHT_07 | Chữ trên thông báo: "Đã cập nhật kết quả" hay "Đã cập nhật kết quả hỗ trợ" |
| 6 | CNKQHT_07 | Cập nhật kết quả lần sau không đính tệp thì tệp của lần trước còn hay mất |
| 7 | DGKQHTVV_01 | Vụ việc đã ở "Đã đánh giá" thì bên còn lại có được vào đánh giá không — **đặc tả tự mâu thuẫn** giữa bảng nút theo trạng thái và 3 chỗ khác |
| 8 | DGKQHTVV_01 | Đánh giá xong một vụ việc thì điểm trung bình của tư vấn viên có phải cập nhật không — **đặc tả tự mâu thuẫn** giữa Postconditions và bảng Processing |

---

## 2. Dữ liệu đã dựng / đã thay đổi

Toàn bộ trên env nội bộ `18.143.165.120.nip.io`. **Không đụng dữ liệu của đối tác**, không đụng env nghiệm thu.

| Case | Bản ghi | Để lại ở trạng thái |
|---|---|---|
| KTHSYCHTPL_11 | `VV-STP-AG-20260806-001` · `-002` · `-003` | -001 Đã phân công · -002 Yêu cầu bổ sung · -003 đã kiểm tra lại (ghi đè bởi cán bộ #02) |
| TKHSYCHTPL_03 | **không dựng gì** — 4 mức cảnh báo thời hạn đều đã có sẵn bản ghi thật | — |
| XNTGHTVV_03 | `VV-BTP-TW-20260806-001` · `-002` · `VV-STP-AG-20260806-004` | cả 3 ở "Đã tiếp nhận" sau khi bị từ chối phân công — **phải phân công lại nếu muốn dùng tiếp** |
| CNKQHT_07 | `VV-BTP-TW-20260806-003` · `-004` · `VV-STP-AG-20260806-005` | cả 3 ở "Đang xử lý", đã có kết quả hỗ trợ |
| CNKQHT_07 | `VV-STP-HN-20260806-002` | bỏ dở ở "Đang kiểm tra" — Hà Nội không có người để phân công |
| DGKQHTVV_01 | `VV-BTP-TW-20260806-003` · `-004` | cả 2 ở **"Đã đánh giá"**, mỗi vụ việc có 1 đánh giá của cán bộ nghiệp vụ (9 · 8 · 10) |
| DGKQHTVV_01 | `VV-STP-AG-20260806-005` | **"Hoàn thành"**, chưa có đánh giá nào — dùng lại được ngay cho vòng verify sau |

**Can thiệp ngoài dữ liệu nghiệp vụ (khai bắt buộc):**

- Tài khoản doanh nghiệp `0209888006` đăng nhập không được → **đặt lại mật khẩu về `Test@1234` bằng chính luồng quên mật khẩu của ứng dụng**. Không sửa dữ liệu nghiệp vụ nào của tài khoản này.
- Tệp `qa-cnkqht07-ket-qua.pdf` (641 byte) tự tạo để thử đính kèm; thư mục tạm đã xoá.

**Nới phạm vi có chủ đích** (đã khai trong bảng điều kiện của từng file tiêu chí, không phải thiếu sót):

- CNKQHT_07 dạng ③ dùng cán bộ **cấp Sở** thay vì cấp Trung ương, vì vụ việc do doanh nghiệp gửi sẽ về đơn vị theo tỉnh/thành.
- CNKQHT_07 đổi địa bàn **Hà Nội → An Giang** giữa chừng: ở Hà Nội không có người nào nhận được phân công (bản ghi tư vấn viên duy nhất không gắn tài khoản đăng nhập nên không thực hiện được bước "Chấp nhận"), không tới được "Đang xử lý" thì không đo được.

---

## 3. Case chưa khép — vì sao · ai phải làm gì

| Việc | Vì sao chưa khép | Ai làm |
|---|---|---|
| **XNTGHTVV_03** (dòng 51) — Reopen | Nhật ký vụ việc **không lưu lý do từ chối** khi người được phân công từ chối tham gia. Bốn vế còn lại của case đã đạt (thông báo về đúng người tiếp nhận, trên cả hai kênh). | **Dev BE** |
| **`KTHSYCHTPL_QA01`** (dòng 364) — Open | Dòng thời gian lọc theo người thực hiện thay vì theo vụ việc. Mới mở, chưa qua vòng sửa nào. | **Dev BE** |
| **8 điểm hỏi BA** | Đặc tả im lặng hoặc tự mâu thuẫn — chưa chốt thì không kết luận đúng/sai được. Riêng điểm #2 là **mâu thuẫn giữa hai chỗ trong chính bộ đặc tả**, không phải chuyện phần mềm. | **BA** |
| **DGKQHTVV_01** (dòng 64) — Reopen | Doanh nghiệp **không tiếp cận được chức năng đánh giá**: mở chi tiết vụ việc của chính mình cũng bị đẩy sang trang báo không có quyền, và máy chủ cũng từ chối chính thao tác đánh giá của doanh nghiệp. Vế "gửi xong đọc lại được ở Nhóm 8" **đã hết lỗi** ở nhánh cán bộ nghiệp vụ (đo trên 2 vụ việc riêng, hai đường đo trùng khít). Phiếu nội bộ: `BUG-VV-DGKQHTVV-01`. | **Dev BE** + **Dev FE** |

### Hai việc đã quyết (2026-08-06, người phụ trách lô)

**a) Bản dựng đổi giữa lô — hai kết quả Pass đầu ứng với bản dựng cũ.**

| Case | Bó mã đo được | Vân tay trang gốc | Ngày dựng |
|---|---|---|---|
| KTHSYCHTPL_11 (45) · TKHSYCHTPL_03 (50) | `assets/index-CNwX9JjX.js` | `etag "6a73f6a4-428"` | 06/08/2026 09:51 giờ VN |
| XNTGHTVV_03 (51) · CNKQHT_07 (62) · DGKQHTVV_01 (64) | `assets/index-DIABnbIr.js` — nhãn `HTPLDN · V1.0.8` | `etag "6a74340b-428"` | 06/08/2026 14:13 giờ VN |

> Vân tay `…-428` là của **trang gốc** (`index.html`, 428 byte), không phải của bó mã. Vân tay riêng của bó mã hiện hành là `etag "6a74340b-1124ed"`.

Một bản dựng mới lên giữa lô. Kiểm lại lúc 16:47 cùng ngày: env **vẫn đang chạy `index-DIABnbIr.js`**, không có bản dựng thứ ba — nên ba case 51 · 62 · 64 cùng nằm trên bản dựng hiện hành.

Verdict chỉ có hiệu lực cho bản dựng đã ghi, nên **hai case 45 và 50 chưa được kiểm trên bản dựng hiện hành**.

> **🔵 Đã quyết: giữ nguyên kết quả cũ, không đo lại.** Hai dòng 45 và 50 giữ `Test done`, và **giới hạn hiệu lực của chúng là bản dựng 06/08/2026 09:51**, không phải bản dựng hiện hành. Nếu bản dựng 14:13 có làm hỏng lại hai chức năng này thì bảng đang ghi thiếu — đây là rủi ro đã biết và đã chấp nhận, không phải sơ suất.

**Mức rủi ro của hai case không bằng nhau:**

- **Case 45** có kiểm chứng gián tiếp trên bản dựng mới: khi dựng dữ liệu cho case 62 và 64 trên bản 14:13, thao tác *kiểm tra hồ sơ → kết luận Đạt → phân công* đã chạy nhiều lần và **đều chạy được** — đúng chức năng mà case 45 verify. Rủi ro thấp.
- **Case 50** (bộ lọc "Mức SLA") **không được chạy lại lần nào** trên bản dựng mới. Không có kiểm chứng gián tiếp nào. Đây là dòng nên đo lại trước tiên nếu về sau muốn siết.

**b) Dòng 145 tab tuần-2 — `TKHSYCHTPL_OOS_01`.**

Nằm **ngoài giới hạn 5 case** nên lô này không đụng tới. Nhưng khi đo case 50 trên bản dựng hiện hành, hai bản ghi liên quan **nay đã hiện đúng "Sắp hết hạn"**, nên trạng thái đang ghi ở dòng 145 có thể đã cũ.

> **🔵 Đã quyết: để nguyên, không đụng.** Lô này chỉ nêu quan sát để người phụ trách tab tuần-2 tự quyết. Không đo lại, không ghi vào dòng đó.
