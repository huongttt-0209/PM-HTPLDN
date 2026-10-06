# Bảng đối chiếu điều kiện — QLDMTCTV_OOS_02 (dòng 328) — Cột "Công khai" là nhãn tĩnh, bấm không mở hộp thoại

**Kết luận:** Pass — cột "Công khai" nay là công tắc bấm được, mở đúng hộp thoại công khai / hủy công khai, và nhãn chữ đã đổi thành "Đã công khai" / "Chưa công khai".

| Điều kiện có thể đổi kết quả | Bug gốc (vòng 1) | Mình đo lại (cbnv_tw, 04/08/2026) | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | Cán bộ Nghiệp vụ cấp Trung ương (`cbnv_tw_04`), đơn vị Cục Bổ trợ tư pháp – Bộ Tư pháp | `cbnv_tw` — `CB_NV_TW`, đơn vị "Bộ Tư Pháp · Cục Bổ trợ tư pháp" (cùng vai trò + cùng cấp + cùng đơn vị) | Không |
| Màn hình / entity + trạng thái | Thẻ "Đang hoạt động", cột "Công khai" trên từng dòng | Đúng thẻ "Đang hoạt động" (8 dòng), cuộn ngang tới cột "Công khai" | Không |
| Dữ liệu tiền đề | 3 tổ chức Đang hoạt động, có cả đã công khai và chưa công khai | Đầu phiên **cả 8 dòng đều "Chưa công khai"** ⇒ để đo được cả hai nhãn, đã **tự công khai** TC-BTP-TW-0001 qua chính hộp thoại rồi **hủy công khai** trả lại nguyên trạng | Không |
| Thao tác / input | Bấm vào nhãn ở cột "Công khai" | **Bấm thật** vào công tắc (không kết luận bằng nhìn): lần 1 → mở hộp thoại công khai; nhập mô tả → bấm Công khai → đổi nhãn; lần 2 → mở hộp thoại hủy công khai; xác nhận → trả về "Chưa công khai" | Không |
| Con trỏ chuột / khả năng bấm | "con trỏ chuột không đổi thành hình bàn tay", bấm không có phản hồi | Phần tử là `<button role="switch" class="ant-switch">`, `cursor: pointer`, `disabled = false` | Không |
| Nhãn chữ so với đặc tả | Web ghi "Công khai" / "Riêng tư" (đặc tả yêu cầu "Đã công khai" / "Chưa công khai") | Chưa bật: chữ **"Chưa công khai"**, công tắc nền `rgb(191,191,191)` (xám). Đã bật: chữ **"Đã công khai"**, công tắc nền `rgb(9,88,217)` (xanh) | Không |

**Đo được khi bấm (bộ bắt thông báo dùng chung, `soObserverDangSong = 1`):**
- Bấm công tắc lần 1 → **0 request**, **0 thông báo nổi**, mở hộp thoại **"Công khai lên Cổng pháp luật quốc gia"** (ô "Mô tả công khai … — bắt buộc", bộ đếm 0/5000, nút Hủy / Công khai; nút Công khai bị vô hiệu khi chưa nhập mô tả).
- Nhập mô tả rồi bấm Công khai → **1 request** `POST /api/v1/to-chuc-tu-vans/beb25e6f-…/cong-khai`, **1 thông báo** "Đã công khai tổ chức tư vấn", `aria-checked` chuyển `true`.
- Bấm công tắc lần 2 → mở hộp thoại **"Hủy công khai tổ chức tư vấn"** ("Tổ chức "Công ty Luật TNHH Alpha Hà Nội" sẽ được gỡ khỏi Cổng pháp luật quốc gia ở lần đồng bộ kế tiếp", nút Đóng / Hủy công khai).
- Xác nhận → **1 request** `POST …/cong-khai`, **1 thông báo** "Đã hủy công khai", nhãn về "Chưa công khai" ⇒ **dữ liệu đã trả về nguyên trạng**.

**Bằng chứng:**
- `image/QLDMTCTV_OOS_02-v2-01-bam-cong-tac-cong-khai-mo-hop-thoai.png` — hộp thoại "Công khai lên Cổng pháp luật quốc gia" mở giữa màn, có ô nhập mô tả + bộ đếm 0/5000 + nút Hủy / Công khai (nút Công khai đang mờ).
- `image/QLDMTCTV_OOS_02-v2-02-sau-cong-khai-nhan-da-cong-khai-cong-tac-bat.png` — dòng Nguyễn Văn A / TC-BTP-TW-0001 có công tắc XANH bật kèm chữ "Đã công khai", 7 dòng còn lại công tắc xám + "Chưa công khai".
- `image/QLDMTCTV_OOS_02-v2-03-bam-lai-cong-tac-mo-hop-thoai-huy-cong-khai.png` — hộp thoại "Hủy công khai tổ chức tư vấn" với nút đỏ "Hủy công khai".
- Đặc tả: `srs-v3.5/srs-fr-04-chuyen-gia-tvv.md` dòng 1645 (Công khai — toggle, "Đã công khai" (xanh) / "Chưa công khai" (xám), Click → mở MD-CONG-KHAI hoặc MD-HUY-CONG-KHAI).
