# Condition table — BUG-EM-TVCS-001 (R3)

| Điều kiện | Thao tác | Kỳ vọng | Thực tế | Kết quả |
|---|---|---|---|---|
| Chuyên gia `qa_tvvseed28`; `TVCS-20260823-0002` ở `DANG_TU_VAN`; đơn vị TW có 6 CB Phê duyệt và 9 CB Nghiệp vụ | Nhập kết quả và bấm Hoàn thành lúc `2026-08-25T04:27:03Z` | Hồ sơ sang `CHO_PHE_DUYET`; chỉ CB Phê duyệt cùng đơn vị nhận email + in-app | Hồ sơ sang Chờ phê duyệt; MailHog sinh đúng 6 thư cho 6 địa chỉ CB_PD_TW | PASS |
| Cửa sổ thư của đúng sự kiện | Quét toàn bộ thư chứa `TVCS-20260823-0002` tại mốc trigger | Không có người nhận CB_NV_TW | 6 người nhận: `diupt01+cb-pd-a@gmail.com`, `diupt01+cb-pd-a-2@gmail.com`, `cbpd_tw@htpldn.test`, `cbpd_tw_03@htpldn.test`, `cbpd_tw_04@htpldn.test`, `cbpd_tw_05@htpldn.test`; không có địa chỉ CB_NV | PASS |
| Kênh in-app | Tra thông báo theo entity `12f89ff2-...` trên `cbpd_tw_01` và `cbnv_tw_01` | CB PD có thông báo phê duyệt; CB NV không có thông báo mới | CB PD có đúng một `PHE_DUYET` lúc `04:27:03.607Z`; CB NV có 0 thông báo mới sau trigger | PASS |
| Kết thúc kiểm tra | CB PD từ chối với lý do hoàn nguyên QA | Trả fixture về trạng thái nguồn | Hồ sơ đã về `DANG_TU_VAN` | PASS |

**Kết luận:** PASS — hoàn thành TVCS chỉ gửi email/in-app cho nhóm Cán bộ Phê duyệt cùng đơn vị, không còn gửi thừa Cán bộ Nghiệp vụ.

**Evidence:** [MailHog — đúng 6 người nhận CB PD](../bug-report/image/bug-em-tvcs-001-r3-only-six-cbpd-recipients-2026-08-25.png) — SHA-256 `2121dfb4f231a223ad4752b12d1dbd650c8257b80f8cadf0aa548cbb79f266ca`.
