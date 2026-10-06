# BA confirm (theo xlsx) + Commit fix sau mốc — 2026-07-29

- **Mốc UAT** = commit `e1b53b6be` (dev @ ~09:43, v1.0.2). Commit ≤ mốc = đã lên UAT; > mốc = chưa lên.
- Nguồn: cột "Trạng thái dev fix" trong `UAT-PM HTPLDN .xlsx` + đối soát `git log origin/dev`.

---

## PHẦN 1 — Toàn bộ 22 bug BA confirm (theo xlsx) + commit fix

> BA chưa confirm ⇒ **coi là CHƯA LÊN hết** (kể cả phần code đã có commit).

| Tuần | Mã bug | Commit fix | Ngày |
|---|---|---|---|
| Tuần 1 | TKDGHQHTPL_02 | `671ba8309` | 27/07 |
| Tuần 2 | QLKTLBG_02 | `ae6cc4540` | 27/07 |
| Tuần 2 | DKTGMLTVV_03 | `baaa8bb2b` | 28/07 |
| Tuần 2 | QLHSTVV_03 | `c960e6190` | 27/07 |
| Tuần 2 | TDHSTVV_14 | `baaa8bb2b` | 28/07 |
| Tuần 4 | QLKCHTV_10 | — | — |
| Tuần 4 | QLKCHTV_12 | — | — |
| Tuần 4 | QLKCHTV_13 | — | — |
| Tuần 4 | QLKCHTV_14 | `e539cc64d` | 28/07 |
| Tuần 4 | QLKCHTV_18 | — | — |
| Tuần 4 | QLKCHTV_22 | `98d2a7ef0` | 28/07 |
| Tuần 4 | QLKCHTV_26 | `a9f300557` | 28/07 |
| Tuần 4 | QLKCHTV_31 | — | — |
| Tuần 4 | QLKCHTV_32 | — | — |
| Tuần 4 | QLKCHTV_36 | — | — |
| Tuần 4 | TKCHTV_02 | — | — |
| Tuần 4 | TKCHTV_03 | — | — |
| Tuần 4 | KHTHCTHTPLDN_03 | — | — |
| Tuần 4 | KHTHCTHTPLDN_07 | `2cd34b85b` | 28/07 |
| Tuần 4 | KHTHCTHTPLDN_08 | — | — |
| Tuần 4 | KHTHCTHTPLDN_12 | — | — |
| Tuần 4 | TKKHCTHTPL_01 | — | — |

**Tổng 22 BA confirm — coi là chưa lên hết** (9 đã có commit, 13 chưa code) vì đều chờ BA confirm. Phân bố tuần: Tuần 1 (1) · Tuần 2 (4) · Tuần 4 (17).

---

## PHẦN 2 — Commit fix các bug SAU MỐC (chưa lên UAT)

9 commit (`--no-merges` trong `e1b53b6be..origin/dev`), đều 29/07 → **8 bug Tuần 4**:

| Mã bug | Commit fix | Giờ (29/07) |
|---|---|---|
| QLKCHTV_OOS_01 | `7a61a5865` | 10:41 |
| QLCKCHTV_02 | `9acbc7f04` | 10:41 |
| XUATTEP_OOS_08 | `be17c64b0` | 11:54 |
| XUATTEP_OOS_09 | `7fe8ba9e6` + `f64e0a6ff` | 11:54 + 17:12 |
| HIENTHI_OOS_10 | `be17c64b0` + `8fb426065` | 11:54 + 17:45 |
| DAOTAO_OOS_11 | `69fc67f15` | 11:54 |
| BCTK_OOS_14 | `790ba9443` | 12:11 |
| HIENTHI_OOS_15 | `6b0068e31` | 12:11 |

**→ Chỉ 8 bug này là "chưa lên do deploy". OSP kéo `dev` build lại là có.**

*Các merge-commit PR #52/#53/#54 (28/07) chỉ là merge-object; nội dung fix của chúng đã là ancestor của mốc (đã ở UAT). 2026-07-29.*
