# Bảng đối chiếu điều kiện — CNKQHT_03

Loại bug: **phụ thuộc role + state** (bộ trường của modal "Cập nhật kết quả hỗ trợ" khác nhau theo vai trò người thao tác và trạng thái vụ việc — theo SRS, người được phân công và CB NV có bộ trường khác nhau) → BẮT BUỘC điền bảng, chỉ kết luận khi 0 GAP.

| Điều kiện có thể đổi kết quả | Đối tác (từ evidence, full-res) | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò người thao tác | `huongcg` — vai trò **TVV · CG**, đơn vị **BTP · TW**, là người được phân công (header frame: "huongcg · TVV · CG · BTP · TW") | `qa_tvvseed28` ("QA TVV Seed28 Active") — vai trò **TVV · CG**, đơn vị Cục Bổ trợ tư pháp - Bộ Tư pháp = **BTP · TW**, `auth/me` trả `["TVV","CG"]`, là người được phân công của vụ việc | Không |
| Entity + trạng thái trước thao tác | Vụ việc `9ed9d021...` (**VV-BTP-TW-20260709-001**, lĩnh vực Thuế, ưu tiên Trung bình) ở trạng thái **Đang xử lý** (stepper "Đang xử lý" active, có nút [Cập nhật kết quả] [Trình phê duyệt]) | Vụ việc VV-BTP-TW cấp TW ở trạng thái **Đang xử lý** (DANG_XU_LY), stepper bước "Đang xử lý", có nút [Cập nhật kết quả] [Trình phê duyệt], nhóm "Kết quả hỗ trợ" hiện "Tư vấn viên chưa cập nhật kết quả" | Không |
| Thao tác mở màn đối chiếu | Bấm [Cập nhật kết quả] → mở modal "Cập nhật kết quả hỗ trợ" (chức năng Cập nhật kết quả của người được phân công — FR-V.I-15) | Bấm [Cập nhật kết quả] → mở đúng modal "Cập nhật kết quả hỗ trợ", cùng chức năng FR-V.I-15 | Không |
| Bộ trường hiển thị để đối chiếu thiết kế | Modal có 3 trường: Nội dung kết quả (bắt buộc, đếm 0/5000), Kết luận (tùy chọn), Ghi chú (tùy chọn); **không có** ô đính kèm tệp | Đo trực tiếp: Nội dung kết quả TEXTAREA `maxLength=5000` bắt buộc · Kết luận INPUT `maxLength=500` tùy chọn · Ghi chú TEXTAREA `maxLength=1000` tùy chọn · **0 input file, 0 vùng upload, không chữ nào nhắc tệp** | Không |

**Kết luận: 0 GAP.** Mọi điều kiện của đối tác đều được tái lập bằng test thật trên đúng vai trò (TVV·CG người được phân công) và đúng trạng thái (vụ việc Đang xử lý) — không đóng bằng lập luận. Bộ trường modal là form tĩnh, không phụ thuộc từng vụ việc cụ thể; vụ việc đối tác và vụ việc mình test tuy khác mã nhưng cùng chức năng/vai trò/trạng thái nên bộ trường trùng khớp.

**Đo lường bộ trường modal (env test):**
`{ "Nội dung kết quả": TEXTAREA maxLength 5000 bắt buộc, "Kết luận": INPUT maxLength 500 tùy chọn, "Ghi chú": TEXTAREA maxLength 1000 tùy chọn, coInputFile: 0, coAntUpload: 0, chuChuaTuTep: false }` — trùng đúng frame đối tác.

Chi tiết đối chiếu SRS v3.5 từng ý con + phần cần BA chốt phiên bản: xem [`../reverify-audit/CNKQHT_03/audit.md`](../reverify-audit/CNKQHT_03/audit.md).
