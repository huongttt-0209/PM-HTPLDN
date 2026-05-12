# TODO — fr-11-bao-cao — Báo cáo 23 loại

> **Module:** FR-11 Báo cáo Thống kê (SCR-IX-01, UC124-146 v3.5)
> **Nhóm:** D SKIP (smoke 5 phút mỗi loại BC + sample 8/23)
> **Tier:** 5 (downstream của FR-02/03/04/05/06/07/08/12/13/14/15)
> **Test plan:** [test-plan.md](test-plan.md) v1.1 revised 2026-05-12
> **BA-Q treo (xem test-plan §2.7):** BA-Q-FR11-001 (DOCX vs PDF), BA-Q-FR11-002 (FR-IX-08 dia_ban), BA-Q-FR11-003 (50K vs 10K)

---

## Icon meaning
- ✅ Đạt (PASS) · ⚠️ Sai spec · ❌ Lỗi · 🚫 Không test được · ⏭ Hoãn · 🤷 Không xác định
- 🟢 Ready (dep thoả) · ⏳ Pending dep · 🔄 In-progress

---

## Task list

- 🟢 **T-FR11-001** Smoke login + open SCR-IX-01 (qtht_01, cb_nv_tw_01)
  - **Kết quả:** TBD — chưa chạy round
  - **Cần có sẵn:** [need: ≥1 account QTHT + CB_NV cấp TW login OK (✓ users.csv); URL `/bao-cao`]
  - **Output:** docs/todo-test/fr-11-bao-cao/results/<round>/

- ⏳ **T-FR11-002** Smoke 15 loại BC không sample — render + filter + chart × 5 phút/loại
  - **Kết quả:** TBD — chưa chạy round
  - **Cần có sẵn:** [need: ≥1 record state cuối mỗi entity upstream 8 entity (✗ chờ T-FR02/03/04/05/06/07/08/15-seed); T-FR11-001 ✅]
  - **Output:** docs/todo-test/fr-11-bao-cao/results/<round>/

- ⏳ **T-FR11-003** Permission test 11 role × {Xem dropdown, Chạy query, Tạo NHAP, Trình duyệt, Duyệt, Xuất XLSX, Xuất PDF}
  - **Kết quả:** TBD — chưa chạy round
  - **Cần có sẵn:** [need: 11 account role (QTHT/3CB_NV/3CB_PD/DN/NHT/TVV/CG) login OK (✓ users.csv); T-FR11-001 ✅]
  - **Output:** docs/todo-test/fr-11-bao-cao/results/<round>/

- ⏳ **T-FR11-004** Functional UC124 BC Hỏi đáp pháp luật + verify wording v3.5 (KHÔNG còn "pháp lý")
  - **Kết quả:** TBD — chưa chạy round
  - **Cần có sẵn:** [need: ≥1 HOI_DAP state DA_TRA_LOI mỗi đơn vị TW/BN/ĐP × ≥3 lĩnh vực × ≥3 kỳ từ FR-02 (✗ chờ FR-02 seed)]
  - **Output:** docs/todo-test/fr-11-bao-cao/results/<round>/

- ⏳ **T-FR11-005** Functional UC126 BC VV đang hỗ trợ + verify BR-SLA-02 4 mức
  - **Kết quả:** TBD — chưa chạy round
  - **Cần có sẵn:** [need: ≥1 VU_VIEC mỗi state {DA_TIEP_NHAN, DANG_XU_LY} × 4 mức SLA từ FR-05 (✗ chờ FR-05 seed)]
  - **Output:** docs/todo-test/fr-11-bao-cao/results/<round>/

- ⏳ **T-FR11-006** Functional UC129 BC Lớp ĐT đang diễn ra
  - **Kết quả:** TBD — chưa chạy round
  - **Cần có sẵn:** [need: ≥1 KHOA_HOC state DANG_DIEN_RA × 2 hình thức {OFFLINE, ONLINE} × 3 lĩnh vực từ FR-03 (✗ chờ FR-03 seed)]
  - **Output:** docs/todo-test/fr-11-bao-cao/results/<round>/

- 🚫 **T-FR11-007** Functional UC131 BC số lượng CG/TVV — BLOCK BA-Q-FR11-002 (dia_ban contradiction)
  - **Kết quả:** 🚫 BLOCK BA-Q-FR11-002 — chờ BA confirm FR-IX-08 spec cuối
  - **Cần có sẵn:** [need: BA confirm FR-IX-08 dia_ban_id bỏ hay giữ (✗ chờ BA reply); ≥1 TU_VAN_VIEN loại {CG, TVV} từ FR-04]
  - **Output:** docs/todo-test/fr-11-bao-cao/results/<round>/

- ⏳ **T-FR11-008** Functional UC132 BC ĐG hiệu quả + verify rename "Kế hoạch đánh giá" v3.5
  - **Kết quả:** TBD — chưa chạy round
  - **Cần có sẵn:** [need: ≥1 BAO_CAO_DANH_GIA state DA_DUYET × 3 lĩnh vực × 3 kỳ từ FR-08 (✗ chờ FR-08 seed)]
  - **Output:** docs/todo-test/fr-11-bao-cao/results/<round>/

- ⏳ **T-FR11-009** Functional UC138 BC Chi phí chi trả
  - **Kết quả:** TBD — chưa chạy round
  - **Cần có sẵn:** [need: ≥3 HO_SO_CHI_TRA state DA_THANH_TOAN/đơn vị × 3 lĩnh vực × 3 kỳ từ FR-06 (✗ chờ FR-06 seed)]
  - **Output:** docs/todo-test/fr-11-bao-cao/results/<round>/

- ⏳ **T-FR11-010** Functional UC134 BC VV phân tích theo đơn vị (Stacked bar cover nhóm VV phân tích)
  - **Kết quả:** TBD — chưa chạy round
  - **Cần có sẵn:** [need: ≥1 VU_VIEC HOAN_THANH mỗi đơn vị TW/BN/ĐP × 3 lĩnh vực từ FR-05 (✗ chờ FR-05 seed)]
  - **Output:** docs/todo-test/fr-11-bao-cao/results/<round>/

- ⏳ **T-FR11-011** Functional UC143 + UC146 BC CT HTPLDN + CT theo thời gian (chart perf)
  - **Kết quả:** TBD — chưa chạy round
  - **Cần có sẵn:** [need: ≥1 CT_HTPLDN state DA_CONG_BO × ≥12 tháng để verify trend line từ FR-15 (✗ chờ FR-15 seed)]
  - **Output:** docs/todo-test/fr-11-bao-cao/results/<round>/

- 🚫 **T-FR11-012** Export XLSX + PDF + 50K boundary — BLOCK BA-Q-FR11-001/003
  - **Kết quả:** 🚫 BLOCK BA-Q-001/003 — chờ BA confirm DOCX vs PDF + 50K vs 10K limit
  - **Cần có sẵn:** [need: BA confirm format cuối + export limit (✗ chờ BA reply); ≥1 BC DA_DUYET từ T-FR11-014]
  - **Output:** docs/todo-test/fr-11-bao-cao/results/<round>/

- ⏳ **T-FR11-013** Workflow đợt BC v3.5: NHAP → CHO_DUYET → DA_DUYET → DA_XUAT + BR-AUTH-05 cùng cấp
  - **Kết quả:** TBD — chưa chạy round
  - **Cần có sẵn:** [need: ≥1 account CB_NV cấp X + CB_PD cùng cấp X login OK (✓ users.csv); ≥1 entity upstream seed xong (✗ chờ T-FR11-004..011)]
  - **Output:** docs/todo-test/fr-11-bao-cao/results/<round>/

- ⏳ **T-FR11-014** Edge: date validation + timeout + empty data + URL deep-link + lý do từ chối boundary
  - **Kết quả:** TBD — chưa chạy round
  - **Cần có sẵn:** [need: T-FR11-001 ✅ login OK; tối thiểu 1 dataset seed để trigger query]
  - **Output:** docs/todo-test/fr-11-bao-cao/results/<round>/

- ⏳ **T-FR11-015** Audit log split: 8 sample loại × 2 action (Xem + Xuất) = 16 verify point qua curl API
  - **Kết quả:** TBD — chưa chạy round
  - **Cần có sẵn:** [need: T-FR11-002..011 đã chạy để có audit row (✗ chờ functional run); endpoint `/api/v1/audit-logs` reachable]
  - **Output:** docs/todo-test/fr-11-bao-cao/results/<round>/

---

## Tiến độ

| Status | Count |
|--------|------:|
| ✅ Đạt | 0 |
| ⚠️ Sai spec | 0 |
| ❌ Lỗi | 0 |
| 🚫 Không test được | 2 (BA-Q gate) |
| 🟢 Ready | 1 |
| ⏳ Pending dep | 12 |
| **Tổng** | **15** |

> **Cross-module dep count:** 13/15 task có dep cross-module (chờ FR-02/03/04/05/06/07/08/15 seed) + 2 task BLOCK BA-Q.
