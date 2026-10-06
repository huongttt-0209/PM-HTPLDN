# Evidence-quality audit — lô cũ (rows 2–34) · 2026-07-12

Kiểm: mỗi verdict cũ có artifact web THẬT chứng minh không (bắt lỗi kiểu _18/_24/_28: ảnh không khớp claim / chỉ frame đối tác / absence chưa quan sát trigger).

## VALID (13) — evidence khớp verdict, giữ nguyên
| Case | Verdict | Ghi chú |
|---|---|---|
| KTDGKQHT_01 | Open | VALID (nửa "Điểm danh" chỉ có frame đối tác → bổ ảnh web; spec-map BA risk) |
| TTKTDGKQHT_01 | Open | VALID (SRS FR-III-06 dòng 620 đúng tab) |
| KTDGKQHT_03 | Reject | VALID |
| QLGVTG_02 | Open | VALID (report ghi 6 cột nhưng ảnh 4 cột — sửa text) |
| QLGVTG_03 | Open | VALID |
| QLGVTG_09 | Open | VALID (mạnh nhất — bắt đúng lỗi 2 lần) |
| TKGVTG_02 | Open | VALID |
| QLNHCH_08 | Open | VALID |
| TKNHCH_05 | Open | VALID (yếu — chỉ 1 record; API-backed) |
| QLNHCH_15 | Reject | VALID |
| QLLKHDTBD_02 | Reject | VALID |
| QLKTLBG_02 | Reject | VALID (note ghi thừa cột — cosmetic) |
| QLKTLBG_08 | Reject | VALID |

## CẦN RE-VERIFY LIVE (8)
| Case | Verdict | Loại lỗi evidence | Rủi ro flip verdict | Trạng thái |
|---|---|---|---|---|
| PDKQDTTH_05 | Open | INVALID — 0 ảnh web, chỉ frame đối tác, dialog từ chối chưa confirm, audit tự nhận nhánh reject CHƯA reproduce | **CAO** (giống _28) | ⏳ chưa chạy |
| DKTGKH_07 | Reject | AMBIGUOUS — QA test khác course/data đối tác, chưa mở đúng course cột trống | **CAO** (false negative) | ✅ RE-VERIFY: học viên NHAP_TAY của AAA-KH-TW render **Họ tên + Email ĐÚNG** (data thật), SĐT/Đơn vị "-" vì BE `donVi=null`. FE render đúng field có dữ liệu, "-" chỉ khi null → **bác claim "mọi cột kể cả Họ tên = -"**. **Reject GIỮ**. Ảnh `DKTGKH_07-web-hocvien-nhaptay-hoten-email-render-donvi-null.png`. Residual: chưa add được record đủ 4 field (không có khóa DA_DUYET) — nhưng core claim đã bác. |
| TTKTLBG_01 | Reject | AMBIGUOUS — search "QA"→1 nhưng có 3 record "QA UAT" cùng session → nghi under-match | **CAO** (false negative) | ✅ RE-VERIFY: search discriminate ĐÚNG (baseline 3 · "QA"→3 · "Video"→1 · nomatch→0). **Reject GIỮ**. Ảnh mới `TTKTLBG_01-search-discriminates-video-1of3.png` |
| PDKQDTTH_01 | Open | AMBIGUOUS — ảnh notif list nhưng chưa gắn trigger duyệt trên env này | Trung bình | 🚫 RE-SEED BLOCKED (xem dưới). Verdict Open GIỮ NGUYÊN (triage: methodology có API 200 trigger trong audit.md, chỉ ảnh yếu). Chưa tự re-verify được. |
| QLDXDTTH_09 | Open/BA | AMBIGUOUS — bắt sai recipient (CB_NV_TW toàn quốc thay vì CB_NV_DP đơn vị) | Trung bình | 🚫 RE-SEED BLOCKED. Verdict GIỮ NGUYÊN. Cần chụp lại notif của recipient đúng (CB_NV_DP) + đề xuất mới. |

### 🚫 3 case notif — RE-SEED BLOCKED (2026-07-12, đã cố gắng thật)
**Đã user duyệt "seed cả 3 tới cùng". Tôi đã thử thật và gặp tường nested-dependency + session bất ổn:**
- Verify approve/reject-result-notif cần 1 khóa học TW ở trạng thái CHO_DUYET_KQ. Khóa TW duy nhất (AAA-KH-TW) đã HOAN_THANH + kết quả khóa. Khóa ĐP (AAA-KH-DP) submit-result trả **403 "Đơn vị người phê duyệt khác đơn vị khóa học"** (CB_NV_TW ≠ ĐP).
- Build khóa TW mới: `POST /khoa-hocs` cần `giangVienIds` → **DB có 0 giảng viên** → phải seed giảng viên trước → giảng viên cần `linhVucIds` → endpoint lĩnh vực không nằm ở path chuẩn (cần UI-capture). Đây mới là layer 1/~12 (khóa→duyệt khóa→khai giảng→buổi học→điểm danh→học viên→nhập KQ→gửi duyệt→switch CB_PD duyệt/từ chối→switch CB_NV check notif).
- Env **logout mỗi ~3-5 phút** → seed multi-role dài liên tục bị ngắt, phải re-login+OTP nhiều lần giữa chừng.
- **KHÔNG assert verdict** cho 3 case này (tránh lặp lỗi _28 = kết luận không data). Verdict cũ GIỮ NGUYÊN, đánh dấu "evidence yếu, cần re-seed ở session env ổn định / có sẵn khóa TW CHO_DUYET_KQ".
- **Việc cần để re-verify sau:** (a) seed sẵn 1 khóa TW + 1 khóa để reject ở trạng thái CHO_DUYET_KQ (hoặc DBA seed), (b) env session dài hơn, (c) tài khoản CB_PD_TW cùng đơn vị. Recipe chi tiết đã có trong report của triage agent.
| QLLKHDTBD_06 | Open | INVALID — 2 ảnh web trùng byte, ảnh "toast" là form tĩnh, chưa bắt 500 | Thấp (API+partner corroborate) | ⚠️ RE-VERIFY: create Kế hoạch **201 THÀNH CÔNG** cả khi KHÔNG file lẫn CÓ file .xlsx (upload 201 + create 201, toast "Tạo kế hoạch thành công"). **500 KHÔNG còn tái hiện** → nhiều khả năng dev đã fix. **Cần user quyết verdict** (bug thật lúc log, giờ hết). |
| QLKTLBG_03 | Reject | INVALID — ảnh cắt cụt, không thấy field "Ảnh đại diện" đang bảo vệ | Thấp | ✅ RE-VERIFY: modal Thêm bài giảng CÓ field "Ảnh đại diện" (.jpg/.jpeg/.png/.gif ≤5MB). **Reject GIỮ**. Ảnh mới `QLKTLBG_03-form-co-truong-anh-dai-dien.png` (đã scroll đủ) |
| KTDGKQHT_08 | Reject | INVALID sub-claim — ảnh "0-10-enforced" chỉ có điểm in-range, không chứng minh clamp | Thấp (core reject VALID) | ✅ RE-VERIFY: nhập 15 vào ô Điểm → blur **clamp về 10.0** (AAA-KH-DP, ô editable). Core reject + sub-claim "0-10 enforced" đều xác nhận data thật. Không lưu (restore 7.5). |

### Seed artifacts tạo trong lúc re-verify (cần dọn hoặc note)
- Kế hoạch đào tạo: `2b4285ce` (no-file), `0495854e` (+file) — QA reverify QLLKHDTBD_06.
