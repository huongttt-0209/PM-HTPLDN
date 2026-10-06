# 00 — Test Plan Overview: FR-04 CG/TVV (Mạng lưới Tư vấn viên) v3.1

> **SRS Ref**: FR-04 — `srs-fr-04-chuyen-gia-tvv-v3.1.md` (2547 dòng)
> **Source**: NotebookLM (notebook id `4dd0675e-a4fa-4ea6-80ae-48e76b3fa264`) + LOCAL `input/srs-v3/srs-fr-04-chuyen-gia-tvv- v3.1.md`
> **Ngày tạo**: 2026-05-09
> **CHANGELOG ref**: `input/srs-v3/CHANGELOG-v3-to-v3.1.md` §srs-fr-04 (18 thay đổi cherry-pick + 1 OUT D.2.1)
> **Sibling check**: W2.1 DN (rolled back), W1.4 TKPQ (200 TC v3.1), W3.2 VV (294 TC FK trỏ TVV)

---

## A. Phạm vi

**19 FR · 9 SCR · 3 SM · 7 Entity owned · 13 BR · 14 UC files · ~218 TC dự kiến**

### A.1 FR list (19 FRs)

| FR | UC | Mô tả |
|----|----|----|
| FR-IV-01 | UC39 | Quản lý TVV (CRUD) — SCR-IV-01 + SCR-IV-02 |
| FR-IV-02 | UC40 | Tìm kiếm TVV + Xuất Phụ lục 1 BTP (10 cột — QĐ 1322/QĐ-BTP) |
| FR-IV-03 | UC41 | NHT đăng ký TVV vào mạng lưới (đại diện) |
| FR-IV-04 | UC42 | NHT cập nhật năng lực TVV (TVV/CG readonly) |
| FR-IV-05 | UC43 | Xem chi tiết TVV (4 tab: Hồ sơ / Năng lực / Lịch sử / Đánh giá) |
| FR-IV-06 | UC44 | Thẩm định 4 nhóm tiêu chí — DAT/KHONG_DAT/YEU_CAU_BO_SUNG |
| FR-IV-07 | UC45 | Phê duyệt TVV — auto cấp TK (CHO_KICH_HOAT) + mail kích hoạt |
| FR-IV-08 | UC46 | Công khai TVV + TC TV lên Cổng PLQG (cá nhân + tổ chức) |
| FR-IV-09 | UC47 | Đánh giá TVV (3 điểm 1-5: Chuyên môn / Thái độ / Đúng hạn) |
| FR-IV-10 | UC48 | Xem lịch sử hỗ trợ (VV + TVCS + Đào tạo) |
| FR-IV-11 | UC49 | NHT cập nhật thông tin TVV (Address/Phone/Email/LV) |
| FR-IV-12 | UC50 | Cập nhật trạng thái TVV — guard cả VV + Hỏi đáp |
| FR-IV-13 | — | Tiếp nhận + chuyển trạng thái tiền thẩm định (3 transitions) |
| FR-IV-NEW-01 | — | CRUD Tổ chức TV + Xuất Phụ lục 2 BTP (12 cột) |
| FR-IV-NEW-02 | — | Cập nhật trạng thái TC TV (SM-TCTV) |
| FR-IV-NEW-04 | — | Phê duyệt TC TV (NĐ 55/2019 Đ.9) |
| FR-IV-NHT-01 | — | Quản lý NHT — auto cấp TK + gán vai trò |
| FR-IV-NHT-02 | — | Tìm kiếm NHT (phục vụ UC59 phân công VV) |
| FR-IV-NHT-03 | — | Xem hồ sơ NHT (3 tab: Thông tin / Bồi dưỡng / VV đã hỗ trợ) |
| FR-IV-CROSS-01 | — | Tổng hợp điểm đánh giá AVG round-half-up |

### A.2 SCR list (9 màn hình)

| SCR | Mô tả | Đường dẫn |
|----|----|----|
| SCR-IV-01 | DS Tư vấn viên — 7 tab + 6 filter + batch action | `/chuyen-gia-tvv/danh-sach` |
| SCR-IV-02 | Form Thêm/Sửa TVV — 5 accordion | `/chuyen-gia-tvv/form` |
| SCR-IV-03 | Chi tiết TVV — 5 tab (Hồ sơ / Năng lực / Thẩm định / Lịch sử / Đánh giá) | `/chuyen-gia-tvv/chi-tiet/{id}` |
| SCR-IV-NEW-01 | DS Tổ chức TV — 4 tab + 4 filter | `/to-chuc-tv/danh-sach` |
| SCR-IV-NEW-02 | Form Thêm/Sửa TC TV | `/to-chuc-tv/form` |
| SCR-IV-NEW-03 | Chi tiết TC TV + 3 nút action | `/to-chuc-tv/chi-tiet/{id}` |
| SCR-IV-NHT-01 | DS Người hỗ trợ — filter | `/nguoi-ho-tro/danh-sach` |
| SCR-IV-NHT-02 | Form Thêm/Sửa NHT | `/nguoi-ho-tro/form` |
| SCR-IV-NHT-03 | Chi tiết NHT — 3 tab | `/nguoi-ho-tro/chi-tiet/{id}` |

### A.3 State Machines (3 SMs)

**SM-TVV (10 trạng thái — 16 transitions):**
```
[*] → MOI_DANG_KY → CHO_THAM_DINH → DANG_THAM_DINH → CHO_PHE_DUYET → CHO_KICH_HOAT → HOAT_DONG
                                  ↓ YEU_CAU_BO_SUNG ↑
                                  ↓ TU_CHOI ↑ (NĐ 55/2019: KHÔNG có cooldown)
HOAT_DONG ↔ TAM_DUNG ↔ VO_HIEU_HOA → HOAT_DONG (khôi phục)
```
- **MỚI v3.1**: CHO_KICH_HOAT (sau Phê duyệt → tự cấp TK + chờ TVV bấm link kích hoạt)
- **OUT v3.1**: D.2.1 wrapper "Tiếp nhận hồ sơ" — bỏ FR-IV-13 nút riêng, gộp 1 thao tác

**SM-TCTV (6 trạng thái — 9 transitions, MỚI):**
```
[*] → MOI_DANG_KY → CHO_PHE_DUYET → HOAT_DONG ↔ TAM_DUNG ↔ VO_HIEU_HOA
                                  ↓ TU_CHOI → CHO_PHE_DUYET (sửa lại)
```

**SM-NHT (4 trạng thái, MỚI):**
```
CHO_KICH_HOAT (mới tạo) → HOAT_DONG (TVV bấm kích hoạt) → TAM_DUNG → VO_HIEU_HOA
```

### A.4 Entity owned (7)

| Entity | Mô tả | Volume |
|--------|------|---|
| TU_VAN_VIEN | TVV/CG cá nhân (NĐ 77/2008) — KHÔNG cover NHT | ~2K records/năm |
| NGUOI_HO_TRO + NGUOI_HO_TRO_LINH_VUC (junction) | Cán bộ HTPL nội bộ (NĐ 55/2019 Đ.7) — 1:1 TAI_KHOAN | ~500 records |
| HO_SO_TU_VAN_VIEN | Hồ sơ năng lực 1:1 với TVV | ~2K |
| TVV_TO_CHUC | Junction N:N TVV ↔ Tổ chức | ~3K/năm |
| DANH_GIA_TU_VAN_VIEN | Thẩm định nội bộ 4 nhóm tiêu chí (CB NV) — KHÔNG dùng tính TB | ~5K/năm |
| DANH_GIA_SAU_VU_VIEC | Đánh giá sau VV (3 điểm 1-5 từ DN) — DÙNG tính BR-CALC-06 | ~3K/năm |
| LICH_SU_HO_TRO_TVV | Lịch sử VV/TVCS/Đào tạo | ~10K/năm |
| TO_CHUC_TU_VAN | TC TV (mới — entity riêng, có Phụ lục 2 BTP) | ~500 |

### A.5 Business Rules (13)

| BR ID | Tóm tắt | FR áp dụng |
|----|----|----|
| BR-AUTH-01 | Xác thực bắt buộc + TOTP 2FA | Toàn bộ FR-IV |
| BR-AUTH-05 | Phê duyệt cùng cấp (BR-FLOW-03) | FR-IV-07, FR-IV-NEW-04 |
| BR-AUTH-08 | Phân quyền dữ liệu theo đơn vị (cây 2 tầng TW/BN/ĐP) | Toàn bộ CRUD FR-IV |
| BR-DATA-01 | Soft delete (set is_deleted=1) | FR-IV-01, NEW-01 |
| BR-DATA-03 | Common fields (created_by, updated_by, ...) | FR-IV-01, NEW-01 |
| BR-DATA-05 | Audit trail INSERT-only AUDIT_LOG | Toàn bộ CUD |
| BR-DATA-07 | Pagination 20/trang | FR-IV-02, FR-IV-10 |
| BR-FLOW-02 | Phê duyệt hàng loạt + Từ chối từng bản ghi | FR-IV-07, SCR-IV-01 |
| BR-FLOW-03 | Không sửa/xóa sau phê duyệt | FR-IV-06 |
| BR-FLOW-04 | Từ chối yêu cầu lý do ≥10 ký tự | FR-IV-07, FR-IV-12, FR-IV-NEW-02/04 |
| BR-LEGAL-04 | NĐ77/2008 Tư vấn pháp luật | FR-IV-01..13 |
| BR-LEGAL-09 | NĐ55/2019 Đ.9 — TVV công khai toàn quốc | FR-IV-08, FR-IV-02 |
| BR-CALC-06 | `diem_danh_gia_tb` = AVG(DANH_GIA_SAU_VU_VIEC.diem_trung_binh), thang 1-5, round-half-up | FR-IV-09, FR-IV-CROSS-01 |
| BR-PUBLIC-01 | Chỉ HOAT_DONG mới công khai (TVV cho cả CHO_KICH_HOAT) | FR-IV-08, FR-IV-NEW-01 |
| BR-PUBLIC-02 | Hủy/vô hiệu hóa → tự gỡ Cổng | FR-IV-08, FR-IV-12, FR-IV-NEW-02 |
| BR-PUBLIC-03 | API outbound retry 3 lần (backoff 1/2/4s, timeout 30s) + queue retry 5 phút | FR-IV-08 |

---

## B. Permission Matrix

| Vai trò | Tạo TVV | Sửa TVV | Xóa TVV | Thẩm định | Phê duyệt | Công khai | Đăng ký NHT | Quản lý TC TV | Phê duyệt TC TV | Quản lý NHT |
|---------|---|---|---|---|---|---|---|---|---|---|
| QTHT (qtht_01) | ✅ TW/BN/ĐP | ✅ TW/BN/ĐP | ✅ TW/BN/ĐP | — | — | — | ✅ | ✅ | — | ✅ TW/BN/ĐP |
| CB NV TW (cb_nv_tw_01) | ✅ TW only | ✅ TW only | ✅ TW only | ✅ TW | — | ✅ TW | — | ✅ TW | — | ✅ TW |
| CB NV BN (cb_nv_bn_01) | ✅ BN only | ✅ BN only | ✅ BN only | ✅ BN | — | ✅ BN | — | ✅ BN | — | ✅ BN |
| CB NV ĐP (cb_nv_dp_01) | ✅ ĐP only | ✅ ĐP only | ✅ ĐP only | ✅ ĐP | — | ✅ ĐP | — | ✅ ĐP | — | ✅ ĐP |
| CB PD TW (cb_pd_tw_01) | — | — | — | — | ✅ TW (cùng cấp) | — | — | — | ✅ TW | — |
| CB PD BN (cb_pd_bn_01) | — | — | — | — | ✅ BN (cùng cấp) | — | — | — | ✅ BN | — |
| CB PD ĐP (cb_pd_dp_01) | — | — | — | — | ✅ ĐP (cùng cấp) | — | — | — | ✅ ĐP | — |
| NHT (nht_01) | — | — | — | — | — | — | ✅ ĐP own unit | — | — | — |
| TVV/CG (tvv_01, cg_01) | — | — | — | — | — | — | — | — | — | — |

**Quy tắc cốt lõi:**
- BR-AUTH-08: CB NV/PD chỉ CRUD bản ghi cùng `don_vi_id`. TW xem được toàn bộ.
- BR-AUTH-05: CB PD chỉ duyệt bản ghi do CB NV cùng cấp thẩm định.
- TVV/CG: chỉ xem hồ sơ của mình qua chuyên trang công khai (read-only).
- NHT: có quyền theo VAI_TRO + đơn vị, KHÔNG sở hữu hồ sơ TVV (tách riêng entity).

---

## C. Mapping UC files → FR/SCR/SM/BR

| # | UC File | FR cover | SCR cover | SM cover | BR chính | TC dự kiến |
|---|---------|---|---|---|---|---:|
| 01 | `01-TC-FR-IV-01-quan-ly-tvv-CRUD.md` | FR-IV-01 | SCR-IV-01, SCR-IV-02 | SM-TVV (MOI_DANG_KY) | AUTH-08, DATA-01/03/05, FLOW-03 | 25 |
| 02 | `02-TC-FR-IV-02-tim-kiem-tvv.md` | FR-IV-02 | SCR-IV-01 | — | DATA-07, AUTH-08, LEGAL-09 | 12 |
| 03 | `03-TC-FR-IV-03-13-dang-ky-tiep-nhan.md` | FR-IV-03, FR-IV-13 | SCR-IV-02 | SM-TVV (MOI_DANG_KY → CHO_THAM_DINH; YEU_CAU_BO_SUNG → DANG_THAM_DINH; TU_CHOI → CHO_THAM_DINH) | AUTH-08, DATA-05 | 20 |
| 04 | `04-TC-FR-IV-04-cap-nhat-nang-luc.md` | FR-IV-04 | SCR-IV-03 (Tab Năng lực) | SM-TVV (auto trigger YEU_CAU_BO_SUNG → DANG_THAM_DINH) | AUTH-08, DATA-05 | 12 |
| 05 | `05-TC-FR-IV-05-10-xem-chi-tiet-lich-su.md` | FR-IV-05, FR-IV-10 | SCR-IV-03 (4 tab) | — | AUTH-01, DATA-07 | 10 |
| 06 | `06-TC-FR-IV-06-tham-dinh.md` | FR-IV-06 | SCR-IV-03 (Tab Thẩm định) | SM-TVV (DANG_THAM_DINH → CHO_PHE_DUYET / YEU_CAU_BO_SUNG / TU_CHOI) | LEGAL-04, FLOW-03/04, DATA-05 | 16 |
| 07 | `07-TC-FR-IV-07-phe-duyet.md` | FR-IV-07 | SCR-IV-03 (header + modal MD-PHE-DUYET) + SCR-IV-01 (batch tab Chờ phê duyệt) | SM-TVV (CHO_PHE_DUYET → CHO_KICH_HOAT / TU_CHOI) | AUTH-05, FLOW-02/04 | 18 |
| 08 | `08-TC-FR-IV-08-cong-khai.md` | FR-IV-08 | SCR-IV-01 (batch) + SCR-IV-03 (modal MD-CONG-KHAI) + SCR-IV-NEW-01/03 | — | PUBLIC-01/02/03, LEGAL-09 | 14 |
| 09 | `09-TC-FR-IV-09-CROSS-01-danh-gia.md` | FR-IV-09, FR-IV-CROSS-01 | SCR-IV-03 (Tab Đánh giá) | — | CALC-06, AUTH-08 | 10 |
| 10 | `10-TC-FR-IV-11-12-cap-nhat-trang-thai.md` | FR-IV-11, FR-IV-12 | SCR-IV-03 (Tab Hồ sơ + nút header) | SM-TVV (HOAT_DONG ↔ TAM_DUNG ↔ VO_HIEU_HOA) | AUTH-08, FLOW-04, DATA-05 | 16 |
| 11 | `11-TC-FR-IV-NEW-01-quan-ly-TC-TV.md` | FR-IV-NEW-01 | SCR-IV-NEW-01, SCR-IV-NEW-02, SCR-IV-NEW-03 | SM-TCTV (MOI_DANG_KY → CHO_PHE_DUYET) | AUTH-08, DATA-01/03/05 | 18 |
| 12 | `12-TC-FR-IV-NEW-02-04-trang-thai-phe-duyet-TC-TV.md` | FR-IV-NEW-02, FR-IV-NEW-04 | SCR-IV-NEW-01/03 | SM-TCTV (toàn bộ transitions) | AUTH-05, FLOW-04 | 12 |
| 13 | `13-TC-FR-IV-NHT-01-02-03-quan-ly-NHT.md` | FR-IV-NHT-01/02/03 | SCR-IV-NHT-01/02/03 | SM-NHT (CHO_KICH_HOAT → HOAT_DONG) | AUTH-08, DATA-05 | 20 |
| 14 | `14-TC-permission-matrix.md` | Cross-FR | Cross-SCR | Cross-SM | AUTH-01/05/08, IDOR | 15 |

**Tổng:** 218 TC dự kiến (estimate trong plan ~80 → revised ~218 do v3.1 mở rộng scope FR từ 13 → 19 + thêm 3 SM mới + 3 SCR mới TC TV + 3 SCR mới NHT)

---

## D. Test Data dự kiến

| Loại | Mô tả | Source |
|----|----|----|
| TK login | qtht_01, cb_nv_tw_01/bn_01/dp_01, cb_pd_tw_01/bn_01/dp_01, nht_01, tvv_01, cg_01 | `users.csv` (Secret@123) |
| TVV/CG seed | ≥3 record per state SM-TVV (10 state × 3 ≥ 30 record) | Phase B B-Seed via MCP |
| TC TV seed | ≥3 record per state SM-TCTV (6 state × 3 = 18) | Phase B B-Seed via MCP |
| NHT seed | ≥3 record per state SM-NHT (4 state × 3 = 12) | Phase B B-Seed via MCP |
| Lĩnh vực PL | DM dùng chung — đã có data cho W1.3 (FR-VIII-01) | DM dùng chung |
| Đơn vị | DON_VI cây 2 tầng TW/BN/ĐP — đã có data | FR-VIII-06 CR-02 |
| Doanh nghiệp | DN ≥3 record để DN đánh giá TVV (FR-IV-09) | W2.1 DN — depend |
| Vụ việc | VV HOAN_THANH ≥1 để DN đánh giá TVV | W3.2 VV — depend |

---

## E. SPEC-CLARIFY pending BA (sẽ phát hiện qua A3-A6)

| Mã | Mô tả | Dự kiến phát hiện ở |
|----|---|---|
| TBD | Sẽ list chi tiết sau A3-A6 | — |

---

## F. Iron rules áp dụng

1. **A4/A6/A7 inline merge** — Mọi TC mới hoặc TC bị xóa/sửa PHẢI Edit trực tiếp vào file UC `NN-TC-*.md`. File 08/10/11 chỉ là audit log.
2. **A7 filter** — 0 TC chỉ-DB/API thuần. TC verify-DB → verify-network qua MCP `list_network_requests`.
3. **Section A. UI FIELD VERIFICATION đầu tiên** — mỗi file UC bắt đầu bằng TC verify SCR (LAYOUT + FIELDS + TABLE + NEGATIVE).
4. **BR quote SRS line** — mỗi BR tham chiếu SRS line cụ thể (vd `srs-fr-04-chuyen-gia-tvv- v3.1.md:2487`).
5. **Error message NGUYÊN VĂN SRS** — KHÔNG paraphrase. Nếu SRS không ghi → "SRS Gap: chưa định nghĩa message".
6. **Permission TC tách file 14** — pattern theo W1.4 TKPQ + W2.3 BM.
7. **Sibling CHANGELOG references**:
   - SM-TVV mới CHO_KICH_HOAT (FR-IV-07 auto-cấp TK qua FR-VIII-15)
   - Bỏ địa bàn → filter theo `don_vi_id` (NĐ 77/2008 Đ.19)
   - Bỏ cooldown 6 tháng (NĐ 77/2008/NĐ-CP + NĐ 55/2019 không quy định)
   - TVV/CG readonly hồ sơ — chỉ NHT cùng đơn vị sửa được
   - TC TV phải qua phê duyệt (NĐ 55/2019 Đ.9)
   - NHT entity riêng (NĐ 55/2019 Đ.7) — KHÔNG nằm trong TU_VAN_VIEN.loai_tvv
   - Guard vô hiệu hóa cả VV + Hỏi đáp (FR-IV-12)
   - Optimistic lock `version` cho FR-IV-07 + FR-IV-NEW-04
   - 4 nhóm tiêu chí: 2 boolean + 2 thang 1-5 (DECIMAL(3,1))
   - 3 điểm 1-5 sau VV (DN đánh giá) → AVG round-half-up
   - Phụ lục 1 (TVV) + Phụ lục 2 (TC TV) BTP — Excel xuất theo mẫu

---

## G. Acceptance criteria Phase A

- ✅ A1-A7 done
- ✅ Traceability ≥95% BR + 100% AC
- ✅ 0 TC chỉ-DB/API thuần (A7 verified)
- ✅ 0 TC sống ở file phụ (08/10/11) — mọi TC nằm trong file UC
- ✅ SPEC-CLARIFY listed (gửi BA Phase B)
