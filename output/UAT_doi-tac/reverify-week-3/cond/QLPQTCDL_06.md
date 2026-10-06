# Bảng đối chiếu điều kiện — QLPQTCDL_06

Loại bug: **thao tác/state** (tick checkbox nút cha trên cây đơn vị → kỳ vọng cascade tự tick nút con). Cây đơn vị dùng chung cho mọi vai trò, hành vi cascade là thuộc tính của component cây, không phụ thuộc vai trò cụ thể. BẮT BUỘC điền bảng, chỉ kết luận khi 0 GAP.

| Điều kiện có thể đổi kết quả | Đối tác (từ evidence, full-res) | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò được cấu hình phân quyền | Vai trò "Chuyên viên kiểm thử tkm" (env đối tác `ospgroup.vn`, roleId `ff22d33f...`), màn "Cấu hình phân quyền dữ liệu" | Vai trò "Cán bộ Nghiệp vụ Địa phương" (CB_NV_DP, roleId `aaaaaaaa-...-010`), cùng màn "Cấu hình phân quyền dữ liệu". Cây đơn vị render y hệt (root + 84 con) độc lập với vai trò được chọn → GAP vai trò không đổi kết quả cascade | Không |
| Cây đơn vị có quan hệ cha-con | Root "Cục Bổ trợ tư pháp - Bộ Tư pháp" (có caret, expand) + các Bộ/Sở là nút con indent 1 | Đúng cây đó: root "Cục Bổ trợ tư pháp - Bộ Tư pháp" (`indent 0`, có `ant-tree-switcher_open` = cha) + 84 con `indent 1` (18 Bộ + 63 Sở + Thanh tra CP + Ủy ban Dân tộc) | Không |
| State trước thao tác | 0 nút được tick (trước khi đối tác tick nút cha) | Baseline đo trực tiếp: `checked=0, indeterminate=0` trên 84 checkbox | Không |
| Thao tác + kết quả | Tick checkbox nút cha "Cục Bổ trợ tư pháp" → con KHÔNG tự tick (kỳ vọng con theo) | Tick checkbox nút cha (uid) → đo lại: `rootChecked=true, checked=1 (chỉ nút cha), indeterminate=0`, mọi con sample (Bộ Công an, Bộ Y tế, Sở Tư pháp An Giang/Hà Nội) = `unchecked`, "Đã chọn (1 đơn vị)". Cascade KHÔNG chạy | Không |

**Kết luận: 0 GAP.** Tái lập đúng thao tác của đối tác (tick nút cha trên cùng cây đơn vị cha-con) bằng test thật, đo trạng thái checkbox trước/sau + chụp ảnh full-res. GAP env (đối tác `ospgroup.vn` vs mình `nip.io`) và GAP vai trò đã đóng bằng test thật — cascade thất bại giống hệt evidence đối tác. Cây đơn vị là dữ liệu hệ thống chung, không phụ thuộc vai trò đang cấu hình.

**Đo lường trạng thái checkbox (env test):**
- Trước tick nút cha: `{ total: 84, checked: 0, indeterminate: 0 }`
- Sau tick nút cha "Cục Bổ trợ tư pháp - Bộ Tư pháp": `{ rootChecked: true, checked: 1, indeterminate: 0, "Đã chọn": "1 đơn vị", childSample: [Bộ Công an, Bộ Y tế, Sở Tư pháp An Giang, Sở Tư pháp Hà Nội] đều unchecked }`

SRS SCR-VIII-05 §Thành phần màn hình dòng 1715: "Cây đơn vị ... check cha (TW) → auto check con (BN và ĐP)". App không cascade → vi phạm.

Evidence: `../bug-reports/image/BUG-QLPQTCDL_06-before.png` (baseline 0 tick), `../bug-reports/image/BUG-QLPQTCDL_06-after.png` (nút cha tick, con vẫn trống).
