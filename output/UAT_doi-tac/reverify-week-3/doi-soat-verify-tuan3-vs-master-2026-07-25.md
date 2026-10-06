# Đối soát cột `Verify` (Sheet nội bộ tuần-3) ↔ master đối tác — 2026-07-25

**Nguồn:** `1OKBN...` tab `UAT_TGPL Doanh Nghiệp-tuần 3` (gid 387857822), cột `Verify`.  
**Đích:** `1dJat...` tab `UAT_TGPL Doanh Nghiệp` (gid 799081340), lọc cột `Tuần` = `Tuần 3`, đọc cột P `Trạng thái dev fix`.  
**Khoá map:** cột D `Mã TC` (cả 2 sheet). Không map theo số dòng.

## 1. Tổng quan map

| | Số dòng |
|---|---|
| Sheet 1 tuần-3 (mã TC khác rỗng) | 307 |
| Sheet 2 dòng `Tuần 3` | 897 |
| **Map khớp Mã TC** | **300** |
| Chỉ có ở Sheet 1 | 7 |
| Chỉ có ở Sheet 2 Tuần 3 (đều chưa có trạng thái) | 597 |

Không có mã trùng lặp trong Sheet 1 tuần-3, cũng không có mã trùng trong tập `Tuần 3` của Sheet 2.
Đã so cả bản chuẩn hoá (bỏ khoảng trắng/gạch, không phân biệt hoa thường): **0 mã lệch chính tả** —
các mã không map được là thiếu thật, không phải sai định dạng.

## 2. Bảng chéo `Verify` × `Trạng thái dev fix` (300 mã đã khớp)

| Verify (Sheet 1) | Trạng thái dev fix (Sheet 2) | Số | Đánh giá |
|---|---|---|---|
| Pass | dev done | 180 | ✅ Khớp quy ước |
| Reject | Reject | 51 | ✅ Khớp quy ước |
| Resolved | Resoved | 45 | ✅ Khớp quy ước |
| Reopen | InProcess | 22 | Chưa chốt / đang xử lý — `InProcess` hợp lý |
| Pass | Reject | 2 | ⚠️ Lệch — quy ước là `dev done` |

Quy ước map đang áp dụng: `Pass`→`dev done` · `Resolved`→`Resoved` · `Reject`→`Reject` ·
`Reopen`/`Open`/trống → giữ `InProcess` (còn việc cho dev).

## 3. Các dòng LỆCH quy ước

Tổng: **2** dòng.

| Mã TC | Sheet 1 row | Sheet 2 row | Verify | Sheet 2 P hiện tại | Cần |
|---|---|---|---|---|---|
| `QLDMTCDGHTCP_06` | 160 | 1118 | Pass | Reject | `dev done` |
| `QLDMTCDGHTCP_12` | 161 | 1124 | Pass | Reject | `dev done` |

## 4. Chưa map được

### 4.1 Chỉ có ở Sheet 1 tuần-3 — 7 mã

Đều là case OOS/tự thêm của QA, **không tồn tại ở master đối tác (mọi tuần)**.

| Mã TC | Sheet 1 row | Verify | Trạng thái dev fix 1 |
|---|---|---|---|
| `QLTMBMHD_OOS_01` | 302 | Pass | dev done |
| `XNTGHTVV_OOS_01` | 303 | Pass | dev done |
| `XNTGHTVV_OOS_02` | 304 | Pass | dev done |
| `CGTVPL_LINHVUC` | 305 | Pass | dev done |
| `QLNDTVVCG_CONGKHAI` | 306 | Pass | dev done |
| `QLDNDHTPL_OOS_01` | 307 | (trống) | BA confirm |
| `QLTLPLCVV_OOS_01` | 308 | (trống) | BA confirm |

### 4.2 Chỉ có ở Sheet 2 `Tuần 3` — 597 mã

**Toàn bộ đều có cột `Trạng thái dev fix` TRỐNG** → là test case tuần 3 chưa phát sinh bug,
không có gì để map. Nói cách khác: mọi dòng `Tuần 3` ở master đối tác **có mang trạng thái**
đều đã map được sang Sheet 1 tuần-3 — **0 dòng bị bỏ sót**.

<details><summary>Danh sách đầy đủ 597 mã (P trống)</summary>

```
XNTGHTVV_02               XNTGHTVV_05               TPDHSVV_01                TPDHSVV_03              
TBKQTNHS_02               TBKQTNHS_03               TBKQTNHS_04               PDHSVV_01               
PDHSVV_06                 CNKQHT_01                 CNKQHT_02                 CNKQHT_04               
CNKQHT_05                 CNKQHT_07                 CNKQVV_01                 CNKQVV_03               
CNKQVV_04                 CNKQVV_06                 DGKQHTVV_02               DGKQHTVV_03             
DGKQHTVV_04               DGKQHTVV_05               DGKQHTVV_06               DGKQHTVV_07             
DGKQHTVV_08               DGKQHTVV_09               TNHSDNHTCP_01             QLHSDNHTCP_01           
QLHSDNHTCP_02             QLHSDNHTCP_05             QLHSDNHTCP_06             QLHSDNHTCP_07           
QLHSDNHTCP_08             QLHSDNHTCP_14             QLHSDNHTCP_15             QLHSDNHTCP_16           
QLHSDNHTCP_17             QLHSDNHTCP_18             QLHSDNHTCP_20             QLHSDNTT_01             
QLHSDNTT_02               QLHSDNTT_03               QLDNDHTPL_01              QLDNDHTPL_03            
QLDNDHTPL_08              QLDNDHTPL_09              QLDNDHTPL_11              QLDNDHTPL_12            
QLDNDHTPL_15              QLDNDHTPL_16              QLDNDHTPL_18              QLDNDHTPL_19            
QLDNDHTPL_20              QLDNDHTPL_22              QLDNDHTPL_29              QLDNDHTPL_30            
TKDNHTPL_01               TKDNHTPL_04               LKHDG_01                  LKHDG_05                
LKHDG_06                  LKHDG_09                  LKHDG_11                  LKHDG_13                
LKHDG_14                  LKHDG_15                  LKHDG_17                  LKHDG_18                
TLCTCDG_01                TLCTCDG_02                TLCTCDG_03                TLCTCDG_04              
TLCTCDG_05                TLCTCDG_06                TLCTCDG_10                TLCTCDG_13              
PCNTHDG_01                PCNTHDG_02                PCNTHDG_03                PCNTHDG_04              
PCNTHDG_05                PCNTHDG_07                PCNTHDG_08                PCNTHDG_09              
PDPCDG_02                 PDPCDG_03                 PDPCDG_04                 THDG_01                 
THDG_06                   THDG_07                   THDG_08                   LBCDG_01                
LBCDG_03                  TPDBC_01                  PDBCDG_02                 PDBCDG_03               
QLTMBMHD_01               QLTMBMHD_02               QLTMBMHD_03               QLTMBMHD_04             
QLTMBMHD_05               QLTMBMHD_06               QLTMBMHD_09               QLTMBMHD_11             
QLTMBMHD_12               QLTMBMHD_14               QLTMBMHD_15               QLTMBMHD_16             
QLTMBMHD_18               QLTMBMHD_21               QLTMBMHD_22               TKTMBMHD_01             
TKTMBMHD_03               TKTMBMHD_05               CKTMBMHDLCTT_01           CKTMBMHDLCTT_03         
CKTMBMHDLCTT_04           CKTMBMHDLCTT_05           CKTMBMHDLCTT_06           CKTMBMHDLCTT_09         
QLBMHD_01                 QLBMHD_04                 QLBMHD_05                 QLBMHD_20               
QLBMHD_21                 TKBMHD_01                 TKBMHD_02                 TKBMHD_05               
IBMHD_01                  IBMHD_05                  IBMHD_06                  IBMHD_08                
IBMHD_09                  QLDMLVPL_01               QLDMLVPL_03               QLDMLVPL_04             
QLDMLVPL_05               QLDMLVPL_06               QLDMLVPL_07               QLDMLVPL_08             
QLDMLVPL_10               QLDMLVPL_11               QLDMLVPL_12               QLDMLVPL_13             
QLDMLVPL_15               QLDMLVPL_17               QLDMLVPL_18               QLDMLVPL_20             
QLDMLVPL_22               QLDMLHHT_01               QLDMLHHT_02               QLDMLHHT_03             
QLDMLHHT_04               QLDMLHHT_05               QLDMLHHT_07               QLDMLHHT_08             
QLDMLHHT_09               QLDMLHHT_10               QLDMLHHT_12               QLDMLHHT_14             
QLDMLHHT_15               QLDMLHHT_17               QLDMCTHT_01               QLDMCTHT_02             
QLDMCTHT_03               QLDMCTHT_04               QLDMCTHT_05               QLDMCTHT_07             
QLDMCTHT_08               QLDMCTHT_09               QLDMCTHT_10               QLDMCTHT_12             
QLDMCTHT_14               QLDMCTHT_15               QLDMCTHT_16               QLDMCTHT_17             
QLDMTTVV_01               QLDMTTVV_02               QLDMTTVV_03               QLDMTTVV_04             
QLDMTTVV_05               QLDMTTVV_07               QLDMTTVV_08               QLDMTTVV_09             
QLDMTTVV_10               QLDMTTVV_12               QLDMTTVV_14               QLDMTTVV_15             
QLDMTTVV_16               QLDMTTVV_17               QLDMTTVV_18               QLDMCQDVQL_01           
QLDMCQDVQL_02             QLDMCQDVQL_03             QLDMCQDVQL_04             QLDMCQDVQL_06           
QLDMCQDVQL_07             QLDMCQDVQL_08             QLDMCQDVQL_09             QLDMCQDVQL_10           
QLDMCQDVQL_11             QLDMCQDVQL_13             QLDMCQDVQL_14             QLDMCQDVQL_15           
QLDMCQDVQL_16             QLDMCQDVQL_17             QLDMCQDVQL_18             QLDMTCTV_02             
QLDMTCTV_03               QLDMTCTV_04               QLDMTCTV_05               QLDMTCTV_06             
QLDMTCTV_07               QLDMTCTV_08               QLDMTCTV_09               QLDMTCTV_10             
QLDMTCTV_11               QLDMTCTV_12               QLDMTCTV_13               QLDMTCTV_14             
QLDMTCTV_15               QLDMTCTV_16               QLDMTCTV_17               QLDMTCTV_18             
QLDMTCTV_19               QLDMLDN_01                QLDMLDN_02                QLDMLDN_03              
QLDMLDN_04                QLDMLDN_05                QLDMLDN_07                QLDMLDN_08              
QLDMLDN_09                QLDMLDN_10                QLDMLDN_12                QLDMLDN_14              
QLDMLDN_15                QLDMLDN_17                QLDMLDN_18                QLDMHSDNHT_01           
QLDMHSDNHT_02             QLDMHSDNHT_03             QLDMHSDNHT_04             QLDMHSDNHT_05           
QLDMHSDNHT_07             QLDMHSDNHT_08             QLDMHSDNHT_09             QLDMHSDNHT_10           
QLDMHSDNHT_12             QLDMHSDNHT_14             QLDMHSDNHT_15             QLDMHSDNHT_16           
QLDMHSDNHT_17             QLDMHSDNTT_01             QLDMHSDNTT_02             QLDMHSDNTT_03           
QLDMHSDNTT_04             QLDMHSDNTT_05             QLDMHSDNTT_07             QLDMHSDNTT_08           
QLDMHSDNTT_09             QLDMHSDNTT_10             QLDMHSDNTT_12             QLDMHSDNTT_14           
QLDMHSDNTT_15             QLDMHSDNTT_16             QLDMHSDNTT_17             QLCHTHXLHS_01           
QLCHTHXLHS_04             QLCHTHXLHS_08             QLCHTHXLHS_09             QLDMTCDGHQ_01           
QLDMTCDGHQ_02             QLDMTCDGHQ_03             QLDMTCDGHQ_04             QLDMTCDGHQ_05           
QLDMTCDGHQ_07             QLDMTCDGHQ_08             QLDMTCDGHQ_09             QLDMTCDGHQ_10           
QLDMTCDGHQ_11             QLDMTCDGHQ_13             QLDMTCDGHQ_14             QLDMTCDGHQ_15           
QLDMTCDGHQ_16             QLDMTCDGHTCP_01           QLDMTCDGHTCP_02           QLDMTCDGHTCP_03         
QLDMTCDGHTCP_04           QLDMTCDGHTCP_05           QLDMTCDGHTCP_07           QLDMTCDGHTCP_08         
QLDMTCDGHTCP_09           QLDMTCDGHTCP_10           QLDMTCDGHTCP_11           QLDMTCDGHTCP_13         
QLDMTCDGHTCP_14           QLDMTCDGHTCP_15           QLDMTCDGHTCP_16           QLDMLTK_01              
QLDMLTK_02                QLDMLTK_03                QLDMLTK_04                QLDMLTK_05              
QLDMLTK_07                QLDMLTK_08                QLDMLTK_09                QLDMLTK_10              
QLDMLTK_11                QLDMLTK_13                QLDMLTK_14                QLDMLTK_15              
QLDMLTK_16                QLDMLTK_17                QLVT_01                   QLVT_02                 
QLVT_03                   QLVT_04                   QLVT_05                   QLVT_06                 
QLVT_07                   QLVT_08                   QLVT_09                   QLVT_10                 
QLVT_11                   QLVT_12                   QLVT_13                   QLVT_15                 
QLVT_16                   QLVT_17                   QLTKND_01                 QLTKND_04               
QLTKND_05                 QLTKND_07                 QLTKND_08                 QLTKND_09               
QLTKND_10                 QLTKND_11                 QLTKND_12                 QLTKND_13               
QLTKND_14                 QLTKND_16                 QLTKND_18                 QLTKND_19               
QLTKND_20                 QLTKND_21                 QLTKND_22                 QLTKND_23               
QLTKND_24                 QLTKND_26                 QLTKND_28                 QLPQTCDL_01             
QLPQTCDL_02               QLPQTCDL_03               QLPQTCDL_04               QLPQTCDL_05             
QLPQTCDL_07               QLPQTCDL_08               QLPQCN_01                 QLPQCN_04               
QLPQCN_05                 QLPQCN_06                 QLPQCN_07                 QLPQCN_08               
QLPQCN_09                 QLPQCN_10                 QLPQCN_11                 QLLHTNHS_01             
QLLHTNHS_02               QLLHTNHS_03               QLLHTNHS_04               QLLHTNHS_05             
QLLHTNHS_07               QLLHTNHS_08               QLLHTNHS_09               QLLHTNHS_10             
QLLHTNHS_11               QLLHTNHS_13               QLLHTNHS_14               QLLHTNHS_15             
QLLHTNHS_16               QLDMKTNHS_01              QLDMKTNHS_02              QLDMKTNHS_03            
QLDMKTNHS_04              QLDMKTNHS_05              QLDMKTNHS_07              QLDMKTNHS_08            
QLDMKTNHS_09              QLDMKTNHS_10              QLDMKTNHS_11              QLDMKTNHS_13            
QLDMKTNHS_14              QLDMKTNHS_15              QLDMKTNHS_16              QLDN_01                 
QLDN_02                   QLDN_03                   QLDN_04                   QLDN_05                 
QLDN_06                   QLDN_08                   QLDN_09                   QLDN_11                 
QLDN_13                   QLDN_14                   QLDX_04                   QLDX_05                 
QLDX_06                   QLDKTK_01                 QLDKTK_05                 QLDKTK_06               
QLDKTK_07                 QLDKTK_10                 QLDKTK_11                 QLDKTK_12               
QLDNV_01                  QLDNV_02                  QLDNV_03                  QLDNBV_01               
QLDBTK_01                 SLHDVM_01                 SLHDVM_02                 SLHDVM_04               
SLHDVM_05                 VVDTN_01                  VVDTN_02                  VVDTN_03                
VVDTN_05                  VVDHT_02                  VVDHT_05                  VVDHTHT_01              
VVDHTHT_02                VVDHTHT_05                VVTTG_04                  CLDTBDDDR_01            
CLDTBDDDR_02              CLDTBDDDR_05              LDTBDDDR_01               LDTBDDDR_02             
LDTBDDDR_03               LDTBDDDR_05               LDTBDDDR_08               LDTBDDDR_09             
CGTVPL_01                 CGTVPL_02                 CGTVPL_03                 CGTVPL_05               
CGTVPL_08                 CGTVPL_09                 DGHQHTPL_01               DGHQHTPL_02             
DGHQHTPL_04               DGHQHTPL_05               DGHQHTPL_08               DGHQHTPL_09             
CLDTBDPL_01               CLDTBDPL_02               CLDTBDPL_05               CLDTBDPL_08             
CLDTBDPL_09               VVTDVQL_01                VVTDVQL_02                VVTDVQL_03              
VVTDVQL_04                VVTDVQL_05                VVTDVQL_08                VVTDVQL_09              
VVTLV_02                  VVTLV_04                  VVTLV_07                  VVTLV_08                
VVTLHDN_01                VVTLHDN_02                VVTLHDN_04                VVTLHDN_07              
VVTLHDN_08                VVTTGCT_01                VVTTGCT_02                VVTTGCT_03              
VVTTGCT_04                VVTTGCT_07                VVTTGCT_08                CPHTCT_01               
CPHTCT_02                 CPHTCT_03                 CPHTCT_04                 CPHTCT_05               
CPHTCT_08                 CPHTCT_09                 CPCTHTTDVQL_01            CPCTHTTDVQL_02          
CPCTHTTDVQL_04            CPCTHTTDVQL_05            CPCTHTTDVQL_08            CPCTHTTDVQL_09          
CPCTHTTLV_01              CPCTHTTLV_02              CPCTHTTLV_03              CPCTHTTLV_04            
CPCTHTTLV_05              CPCTHTTLV_06              CPCTHTTLV_07              CPCTHTTLV_08            
CPCTHTTLV_09              CPCTHTTLHDN_01            CPCTHTTLHDN_02            CPCTHTTLHDN_05          
CPCTHTTLHDN_08            CPCTHTTLHDN_09            CPCTHTTTG_01              CPCTHTTTG_02            
CPCTHTTTG_04              CPCTHTTTG_07              CPCTHTTTG_08              SLCTHT_01               
SLCTHT_02                 SLCTHT_05                 SLCTHT_08                 SLCTHT_09               
CTTDVQL_01                CTTDVQL_06                CTTDVQL_07                CTTLV_02                
CTTLV_07                  CTTLV_08                  CTTTG_01                  CTTTG_02                
CTTTG_03                  CTTTG_06                  CTTTG_07                  QLNDTVVCG_01            
QLNDTVVCG_02              QLNDTVVCG_05              QLNDTVVCG_09              QLNDTVVCG_10            
QLNDTVVCG_12              QLNDTVVCG_13              QLNDTVVCG_14              QLNDTVVCG_16            
QLNDTVVCG_18              QLNDTVVCG_19              QLNDTVVCG_21              QLNDTVVCG_24            
QLNDTVVCG_25              QLNDTVVCG_26              QLNDTVVCG_28              QLNDTVVCG_29            
QLNDTVVCG_30              QLNDTVVCG_31              QLNDTVVCG_32              QLNDTVVCG_33            
QLNDTVVCG_34              QLNDTVVCG_35              QLNDTVVCG_37              QLNDTVVCG_38            
QLNDTVVCG_39              QLNDTVVCG_41              TKNDTVVCG_01              TKNDTVVCG_02            
TKNDTVVCG_04              TKNDTVVCG_05              TKNDTVVCG_06              TKNDTVVCG_07            
TKNDTVVCG_08              TKNDTVVCG_09              TNNDTVVCG_01              QLHSPLDN_01             
QLHSPLDN_04               QLHSPLDN_05               QLHSPLDN_06               QLHSPLDN_07             
QLHSPLDN_08               QLHSPLDN_09               QLHSPLDN_10               QLHSPLDN_11             
QLHSPLDN_12               QLHSPLDN_13               QLHSPLDN_14               QLHSPLDN_15             
QLHSPLDN_16               QLTLPLCVV_01              QLTLPLCVV_04              QLTLPLCVV_05            
QLTLPLCVV_06              QLTLPLCVV_10              QLTLPLCVV_12              QLTLPLCVV_13            
QLTLPLCVV_14              QLTLPLCVV_17              QLTLPLCVV_18              QLTLPLCVV_19            
QLTLPLCVV_20              QLTLPLCVV_21              QLTLPLCVV_22              QLTLPLCVV_23            
QLTLPLCVV_24            
```

</details>

## 5. Chi tiết 300 mã đã khớp

### Verify = `Pass` — 182 mã

| Mã TC | Sheet 1 row | Sheet 2 row | Sheet 1 `Trạng thái dev fix 1` | Sheet 2 `Trạng thái dev fix` | |
|---|---|---|---|---|---|
| `CGTVPL_07` | 231 | 1349 | dev done | dev done | ✅ |
| `CKTMBMHDLCTT_02` | 92 | 873 | dev done | dev done | ✅ |
| `CKTMBMHDLCTT_07` | 93 | 878 | dev done | dev done | ✅ |
| `CKTMBMHDLCTT_08` | 94 | 879 | dev done | dev done | ✅ |
| `CKTMBMHDLCTT_10` | 95 | 881 | dev done | dev done | ✅ |
| `CKTMBMHDLCTT_11` | 96 | 882 | dev done | dev done | ✅ |
| `CLDTBDDDR_03` | 220 | 1327 | dev done | dev done | ✅ |
| `CLDTBDDDR_07` | 223 | 1331 | dev done | dev done | ✅ |
| `CLDTBDPL_03` | 235 | 1363 | dev done | dev done | ✅ |
| `CLDTBDPL_04` | 236 | 1364 | dev done | dev done | ✅ |
| `CLDTBDPL_07` | 238 | 1367 | dev done | dev done | ✅ |
| `CNKQHT_06` | 12 | 638 | dev done | dev done | ✅ |
| `CNKQVV_02` | 13 | 641 | dev done | dev done | ✅ |
| `CNKQVV_05` | 14 | 644 | dev done | dev done | ✅ |
| `CPCTHTTDVQL_07` | 254 | 1418 | dev done | dev done | ✅ |
| `CPCTHTTLHDN_07` | 258 | 1436 | dev done | dev done | ✅ |
| `CPCTHTTTG_06` | 261 | 1444 | dev done | dev done | ✅ |
| `CPHTCT_07` | 251 | 1409 | dev done | dev done | ✅ |
| `CTTDVQL_03` | 267 | 1458 | dev done | dev done | ✅ |
| `CTTDVQL_05` | 269 | 1460 | dev done | dev done | ✅ |
| `CTTLV_01` | 270 | 1463 | dev done | dev done | ✅ |
| `CTTLV_04` | 272 | 1466 | dev done | dev done | ✅ |
| `CTTLV_06` | 274 | 1468 | dev done | dev done | ✅ |
| `CTTTG_05` | 276 | 1475 | dev done | dev done | ✅ |
| `CVVDG_03` | 67 | 818 | dev done | dev done | ✅ |
| `CVVDG_04` | 68 | 819 | dev done | dev done | ✅ |
| `DGHQHTPL_03` | 232 | 1354 | dev done | dev done | ✅ |
| `DGHQHTPL_07` | 234 | 1358 | dev done | dev done | ✅ |
| `DGKQHTVV_01` | 15 | 646 | dev done | dev done | ✅ |
| `IBMHD_04` | 118 | 914 | dev done | dev done | ✅ |
| `IBMHD_11` | 121 | 921 | dev done | dev done | ✅ |
| `LBCDG_02` | 73 | 829 | dev done | dev done | ✅ |
| `LBCDG_04` | 74 | 831 | dev done | dev done | ✅ |
| `LBCDG_05` | 75 | 832 | dev done | dev done | ✅ |
| `LDTBDDDR_07` | 228 | 1340 | dev done | dev done | ✅ |
| `LKHDG_02` | 43 | 766 | dev done | dev done | ✅ |
| `LKHDG_03` | 44 | 767 | dev done | dev done | ✅ |
| `LKHDG_04` | 45 | 768 | dev done | dev done | ✅ |
| `LKHDG_07` | 46 | 771 | dev done | dev done | ✅ |
| `LKHDG_08` | 47 | 772 | dev done | dev done | ✅ |
| `LKHDG_12` | 49 | 776 | dev done | dev done | ✅ |
| `LKHDG_16` | 50 | 780 | dev done | dev done | ✅ |
| `LKHDG_19` | 51 | 783 | dev done | dev done | ✅ |
| `LKHDG_20` | 52 | 784 | dev done | dev done | ✅ |
| `LKHDG_21` | 53 | 785 | dev done | dev done | ✅ |
| `LKHDG_22` | 54 | 786 | dev done | dev done | ✅ |
| `PCNTHDG_06` | 60 | 805 | dev done | dev done | ✅ |
| `PCNTHDG_11` | 62 | 810 | dev done | dev done | ✅ |
| `PDBCDG_01` | 78 | 836 | dev done | dev done | ✅ |
| `PDBCDG_04` | 79 | 839 | dev done | dev done | ✅ |
| `PDHSVV_02` | 7 | 618 | dev done | dev done | ✅ |
| `PDHSVV_03` | 8 | 619 | dev done | dev done | ✅ |
| `PDHSVV_04` | 9 | 620 | dev done | dev done | ✅ |
| `PDHSVV_05` | 10 | 621 | dev done | dev done | ✅ |
| `PDPCDG_01` | 63 | 811 | dev done | dev done | ✅ |
| `PDPCDG_05` | 64 | 815 | dev done | dev done | ✅ |
| `QLBMHD_02` | 97 | 885 | dev done | dev done | ✅ |
| `QLBMHD_03` | 98 | 886 | dev done | dev done | ✅ |
| `QLBMHD_06` | 99 | 889 | dev done | dev done | ✅ |
| `QLBMHD_07` | 100 | 890 | dev done | dev done | ✅ |
| `QLBMHD_09` | 102 | 892 | dev done | dev done | ✅ |
| `QLBMHD_16` | 109 | 899 | dev done | dev done | ✅ |
| `QLBMHD_17` | 110 | 900 | dev done | dev done | ✅ |
| `QLBMHD_18` | 111 | 901 | dev done | dev done | ✅ |
| `QLBMHD_19` | 112 | 902 | dev done | dev done | ✅ |
| `QLCHTHXLHS_02` | 152 | 1088 | dev done | dev done | ✅ |
| `QLCHTHXLHS_05` | 154 | 1091 | dev done | dev done | ✅ |
| `QLCHTHXLHS_06` | 155 | 1092 | dev done | dev done | ✅ |
| `QLCHTHXLHS_07` | 156 | 1093 | dev done | dev done | ✅ |
| `QLDKTK_02` | 185 | 1263 | dev done | dev done | ✅ |
| `QLDKTK_04` | 187 | 1265 | dev done | dev done | ✅ |
| `QLDKTK_08` | 188 | 1269 | dev done | dev done | ✅ |
| `QLDMCTHT_06` | 133 | 968 | dev done | dev done | ✅ |
| `QLDMCTHT_11` | 134 | 973 | dev done | dev done | ✅ |
| `QLDMHSDNHT_06` | 146 | 1058 | dev done | dev done | ✅ |
| `QLDMHSDNHT_11` | 147 | 1063 | dev done | dev done | ✅ |
| `QLDMHSDNTT_06` | 149 | 1075 | dev done | dev done | ✅ |
| `QLDMHSDNTT_11` | 150 | 1080 | dev done | dev done | ✅ |
| `QLDMHSDNTT_13` | 151 | 1082 | dev done | dev done | ✅ |
| `QLDMKTNHS_06` | 177 | 1231 | dev done | dev done | ✅ |
| `QLDMKTNHS_12` | 178 | 1237 | dev done | dev done | ✅ |
| `QLDMLDN_06` | 142 | 1040 | dev done | dev done | ✅ |
| `QLDMLDN_11` | 143 | 1045 | dev done | dev done | ✅ |
| `QLDMLDN_13` | 144 | 1047 | dev done | dev done | ✅ |
| `QLDMLHHT_06` | 128 | 950 | dev done | dev done | ✅ |
| `QLDMLHHT_11` | 129 | 955 | dev done | dev done | ✅ |
| `QLDMLHHT_13` | 130 | 957 | dev done | dev done | ✅ |
| `QLDMLTK_06` | 162 | 1134 | dev done | dev done | ✅ |
| `QLDMLTK_12` | 163 | 1140 | dev done | dev done | ✅ |
| `QLDMLVPL_02` | 122 | 924 | dev done | dev done | ✅ |
| `QLDMLVPL_09` | 123 | 931 | dev done | dev done | ✅ |
| `QLDMLVPL_14` | 124 | 936 | dev done | dev done | ✅ |
| `QLDMLVPL_16` | 125 | 938 | dev done | dev done | ✅ |
| `QLDMTCDGHQ_06` | 157 | 1101 | dev done | dev done | ✅ |
| `QLDMTCDGHQ_12` | 158 | 1107 | dev done | dev done | ✅ |
| `QLDMTCDGHTCP_06` | 160 | 1118 | dev done | Reject | ⚠️ |
| `QLDMTCDGHTCP_12` | 161 | 1124 | dev done | Reject | ⚠️ |
| `QLDMTTVV_06` | 136 | 985 | dev done | dev done | ✅ |
| `QLDMTTVV_11` | 137 | 990 | dev done | dev done | ✅ |
| `QLDMTTVV_13` | 138 | 992 | dev done | dev done | ✅ |
| `QLDNDHTPL_02` | 24 | 730 | dev done | dev done | ✅ |
| `QLDNDHTPL_04` | 25 | 732 | dev done | dev done | ✅ |
| `QLDNDHTPL_05` | 26 | 733 | dev done | dev done | ✅ |
| `QLDNDHTPL_06` | 27 | 734 | dev done | dev done | ✅ |
| `QLDNDHTPL_07` | 28 | 735 | dev done | dev done | ✅ |
| `QLDNDHTPL_10` | 29 | 738 | dev done | dev done | ✅ |
| `QLDNDHTPL_13` | 30 | 741 | dev done | dev done | ✅ |
| `QLDNDHTPL_14` | 31 | 742 | dev done | dev done | ✅ |
| `QLDNDHTPL_21` | 33 | 749 | dev done | dev done | ✅ |
| `QLDNDHTPL_26` | 37 | 754 | dev done | dev done | ✅ |
| `QLDNDHTPL_31` | 40 | 759 | dev done | dev done | ✅ |
| `QLDN_07` | 179 | 1248 | dev done | dev done | ✅ |
| `QLDN_10` | 180 | 1251 | dev done | dev done | ✅ |
| `QLDN_12` | 181 | 1253 | dev done | dev done | ✅ |
| `QLDX_01` | 182 | 1256 | dev done | dev done | ✅ |
| `QLDX_02` | 183 | 1257 | dev done | dev done | ✅ |
| `QLHSDNHTCP_09` | 18 | 666 | dev done | dev done | ✅ |
| `QLHSDNHTCP_11` | 20 | 668 | dev done | dev done | ✅ |
| `QLHSDNHTCP_12` | 21 | 669 | dev done | dev done | ✅ |
| `QLHSDNHTCP_13` | 22 | 670 | dev done | dev done | ✅ |
| `QLHSPLDN_02` | 292 | 1533 | dev done | dev done | ✅ |
| `QLLHTNHS_06` | 175 | 1215 | dev done | dev done | ✅ |
| `QLLHTNHS_12` | 176 | 1221 | dev done | dev done | ✅ |
| `QLNDTVVCG_04` | 278 | 1483 | dev done | dev done | ✅ |
| `QLNDTVVCG_07` | 280 | 1486 | dev done | dev done | ✅ |
| `QLNDTVVCG_08` | 281 | 1487 | dev done | dev done | ✅ |
| `QLNDTVVCG_15` | 283 | 1494 | dev done | dev done | ✅ |
| `QLNDTVVCG_17` | 284 | 1496 | dev done | dev done | ✅ |
| `QLNDTVVCG_27` | 288 | 1506 | dev done | dev done | ✅ |
| `QLPQTCDL_06` | 172 | 1196 | dev done | dev done | ✅ |
| `QLTKND_02` | 165 | 1164 | dev done | dev done | ✅ |
| `QLTKND_03` | 166 | 1165 | dev done | dev done | ✅ |
| `QLTKND_15` | 168 | 1177 | dev done | dev done | ✅ |
| `QLTLPLCVV_02` | 294 | 1551 | dev done | dev done | ✅ |
| `QLTLPLCVV_08` | 297 | 1557 | dev done | dev done | ✅ |
| `QLTLPLCVV_09` | 298 | 1558 | dev done | dev done | ✅ |
| `QLTLPLCVV_11` | 299 | 1560 | dev done | dev done | ✅ |
| `QLTLPLCVV_15` | 300 | 1564 | dev done | dev done | ✅ |
| `QLTMBMHD_08` | 81 | 849 | dev done | dev done | ✅ |
| `QLTMBMHD_13` | 83 | 854 | dev done | dev done | ✅ |
| `QLTMBMHD_19` | 85 | 860 | dev done | dev done | ✅ |
| `QLTMBMHD_23` | 87 | 864 | dev done | dev done | ✅ |
| `SLCTHT_03` | 262 | 1449 | dev done | dev done | ✅ |
| `SLCTHT_04` | 263 | 1450 | dev done | dev done | ✅ |
| `SLCTHT_07` | 265 | 1453 | dev done | dev done | ✅ |
| `SLHDVM_07` | 192 | 1287 | dev done | dev done | ✅ |
| `THDG_02` | 69 | 821 | dev done | dev done | ✅ |
| `THDG_04` | 71 | 823 | dev done | dev done | ✅ |
| `THDG_05` | 72 | 824 | dev done | dev done | ✅ |
| `TKBMHD_04` | 114 | 908 | dev done | dev done | ✅ |
| `TKDNHTPL_02` | 41 | 761 | dev done | dev done | ✅ |
| `TKDNHTPL_03` | 42 | 762 | dev done | dev done | ✅ |
| `TKNDTVVCG_03` | 291 | 1523 | dev done | dev done | ✅ |
| `TKTMBMHD_02` | 88 | 866 | dev done | dev done | ✅ |
| `TKTMBMHD_06` | 90 | 870 | dev done | dev done | ✅ |
| `TKTMBMHD_07` | 91 | 871 | dev done | dev done | ✅ |
| `TLCTCDG_07` | 55 | 793 | dev done | dev done | ✅ |
| `TLCTCDG_08` | 56 | 794 | dev done | dev done | ✅ |
| `TLCTCDG_12` | 59 | 798 | dev done | dev done | ✅ |
| `TPDBC_03` | 77 | 835 | dev done | dev done | ✅ |
| `TPDHSVV_02` | 4 | 610 | dev done | dev done | ✅ |
| `TPDHSVV_04` | 5 | 612 | dev done | dev done | ✅ |
| `VVDHTHT_03` | 207 | 1310 | dev done | dev done | ✅ |
| `VVDHTHT_04` | 208 | 1311 | dev done | dev done | ✅ |
| `VVDHTHT_07` | 210 | 1314 | dev done | dev done | ✅ |
| `VVDHT_01` | 200 | 1299 | dev done | dev done | ✅ |
| `VVDHT_04` | 202 | 1302 | dev done | dev done | ✅ |
| `VVDHT_07` | 204 | 1305 | dev done | dev done | ✅ |
| `VVDTN_04` | 195 | 1293 | dev done | dev done | ✅ |
| `VVDTN_07` | 197 | 1296 | dev done | dev done | ✅ |
| `VVTDVQL_07` | 240 | 1376 | dev done | dev done | ✅ |
| `VVTLHDN_03` | 245 | 1389 | dev done | dev done | ✅ |
| `VVTLHDN_06` | 247 | 1392 | dev done | dev done | ✅ |
| `VVTLV_01` | 241 | 1379 | dev done | dev done | ✅ |
| `VVTLV_03` | 242 | 1381 | dev done | dev done | ✅ |
| `VVTLV_06` | 244 | 1384 | dev done | dev done | ✅ |
| `VVTTGCT_06` | 249 | 1400 | dev done | dev done | ✅ |
| `VVTTG_01` | 213 | 1317 | dev done | dev done | ✅ |
| `VVTTG_03` | 215 | 1319 | dev done | dev done | ✅ |
| `VVTTG_06` | 217 | 1322 | dev done | dev done | ✅ |
| `XNTGHTVV_03` | 2 | 606 | dev done | dev done | ✅ |
| `XNTGHTVV_04` | 3 | 607 | dev done | dev done | ✅ |

### Verify = `Reject` — 51 mã

| Mã TC | Sheet 1 row | Sheet 2 row | Sheet 1 `Trạng thái dev fix 1` | Sheet 2 `Trạng thái dev fix` | |
|---|---|---|---|---|---|
| `CGTVPL_04` | 229 | 1346 | Reject | Reject | ✅ |
| `CLDTBDDDR_04` | 221 | 1328 | Reject | Reject | ✅ |
| `CLDTBDDDR_08` | 224 | 1332 | Reject | Reject | ✅ |
| `CLDTBDDDR_09` | 225 | 1333 | Reject | Reject | ✅ |
| `CPCTHTTDVQL_03` | 252 | 1414 | Reject | Reject | ✅ |
| `CPCTHTTLHDN_03` | 255 | 1432 | Reject | Reject | ✅ |
| `CPCTHTTLHDN_04` | 256 | 1433 | Reject | Reject | ✅ |
| `CPCTHTTTG_03` | 259 | 1441 | Reject | Reject | ✅ |
| `CTTDVQL_02` | 266 | 1457 | Reject | Reject | ✅ |
| `CTTLV_03` | 271 | 1465 | Reject | Reject | ✅ |
| `CVVDG_01` | 65 | 816 | Reject | Reject | ✅ |
| `CVVDG_02` | 66 | 817 | Reject | Reject | ✅ |
| `IBMHD_02` | 116 | 912 | Reject | Reject | ✅ |
| `IBMHD_03` | 117 | 913 | Reject | Reject | ✅ |
| `LDTBDDDR_04` | 226 | 1337 | Reject | Reject | ✅ |
| `LKHDG_10` | 48 | 774 | Reject | Reject | ✅ |
| `QLBMHD_12` | 105 | 895 | Reject | Reject | ✅ |
| `QLDMCQDVQL_05` | 139 | 1002 | Reject | Reject | ✅ |
| `QLDMTCTV_01` | 141 | 1016 | Reject | Reject | ✅ |
| `QLDNDHTPL_17` | 32 | 745 | Reject | Reject | ✅ |
| `QLDNDHTPL_23` | 34 | 751 | Reject | Reject | ✅ |
| `QLDNDHTPL_24` | 35 | 752 | Reject | Reject | ✅ |
| `QLDNDHTPL_25` | 36 | 753 | Reject | Reject | ✅ |
| `QLDNDHTPL_27` | 38 | 755 | Reject | Reject | ✅ |
| `QLDNDHTPL_28` | 39 | 756 | Reject | Reject | ✅ |
| `QLHSDNHTCP_19` | 23 | 676 | Reject | Reject | ✅ |
| `QLNDTVVCG_06` | 279 | 1485 | Reject | Reject | ✅ |
| `QLNDTVVCG_20` | 285 | 1499 | Reject | Reject | ✅ |
| `QLTKND_06` | 167 | 1168 | Reject | Reject | ✅ |
| `QLTKND_25` | 170 | 1187 | Reject | Reject | ✅ |
| `QLTKND_27` | 171 | 1189 | Reject | Reject | ✅ |
| `QLTLPLCVV_03` | 295 | 1552 | Reject | Reject | ✅ |
| `QLTLPLCVV_16` | 301 | 1565 | Reject | Reject | ✅ |
| `QLTMBMHD_10` | 82 | 851 | Reject | Reject | ✅ |
| `QLTMBMHD_17` | 84 | 858 | Reject | Reject | ✅ |
| `QLVT_14` | 164 | 1159 | Reject | Reject | ✅ |
| `SLHDVM_03` | 190 | 1283 | Reject | Reject | ✅ |
| `SLHDVM_08` | 193 | 1288 | Reject | Reject | ✅ |
| `SLHDVM_09` | 194 | 1289 | Reject | Reject | ✅ |
| `TBKQTNHS_01` | 6 | 613 | Reject | Reject | ✅ |
| `TLCTCDG_11` | 58 | 797 | Reject | Reject | ✅ |
| `VVDHTHT_08` | 211 | 1315 | Reject | Reject | ✅ |
| `VVDHTHT_09` | 212 | 1316 | Reject | Reject | ✅ |
| `VVDHT_03` | 201 | 1301 | Reject | Reject | ✅ |
| `VVDHT_08` | 205 | 1306 | Reject | Reject | ✅ |
| `VVDHT_09` | 206 | 1307 | Reject | Reject | ✅ |
| `VVDTN_08` | 198 | 1297 | Reject | Reject | ✅ |
| `VVDTN_09` | 199 | 1298 | Reject | Reject | ✅ |
| `VVTTG_02` | 214 | 1318 | Reject | Reject | ✅ |
| `VVTTG_07` | 218 | 1323 | Reject | Reject | ✅ |
| `VVTTG_08` | 219 | 1324 | Reject | Reject | ✅ |

### Verify = `Resolved` — 45 mã

| Mã TC | Sheet 1 row | Sheet 2 row | Sheet 1 `Trạng thái dev fix 1` | Sheet 2 `Trạng thái dev fix` | |
|---|---|---|---|---|---|
| `CGTVPL_06` | 230 | 1348 | Reject | Resoved | ✅ |
| `CKBMHDLCTT_01` | 115 | 910 | Reject | Resoved | ✅ |
| `CLDTBDDDR_06` | 222 | 1330 | Reject | Resoved | ✅ |
| `CLDTBDPL_06` | 237 | 1366 | Reject | Resoved | ✅ |
| `CPCTHTTDVQL_06` | 253 | 1417 | Reject | Resoved | ✅ |
| `CPCTHTTLHDN_06` | 257 | 1435 | Reject | Resoved | ✅ |
| `CPCTHTTTG_05` | 260 | 1443 | Reject | Resoved | ✅ |
| `CPHTCT_06` | 250 | 1408 | Reject | Resoved | ✅ |
| `CTTDVQL_04` | 268 | 1459 | Reject | Resoved | ✅ |
| `CTTLV_05` | 273 | 1467 | Reject | Resoved | ✅ |
| `CTTTG_04` | 275 | 1474 | Reject | Resoved | ✅ |
| `DGHQHTPL_06` | 233 | 1357 | Reject | Resoved | ✅ |
| `IBMHD_10` | 120 | 920 | Reject | Resoved | ✅ |
| `LDTBDDDR_06` | 227 | 1339 | Reject | Resoved | ✅ |
| `PCNTHDG_10` | 61 | 809 | Reject | Resoved | ✅ |
| `QLBMHD_10` | 103 | 893 | Reject | Resoved | ✅ |
| `QLBMHD_11` | 104 | 894 | Reject | Resoved | ✅ |
| `QLBMHD_14` | 107 | 897 | Reject | Resoved | ✅ |
| `QLBMHD_15` | 108 | 898 | Reject | Resoved | ✅ |
| `QLDKTK_09` | 189 | 1270 | Reject | Resoved | ✅ |
| `QLDMLDN_16` | 145 | 1050 | Reject | Resoved | ✅ |
| `QLDMLHHT_16` | 131 | 960 | Reject | Resoved | ✅ |
| `QLDMLHHT_18` | 132 | 962 | Reject | Resoved | ✅ |
| `QLDMLVPL_19` | 126 | 941 | Reject | Resoved | ✅ |
| `QLDMLVPL_21` | 127 | 943 | Reject | Resoved | ✅ |
| `QLDMTCDGHQ_17` | 159 | 1112 | Reject | Resoved | ✅ |
| `QLDX_03` | 184 | 1258 | Reject | Resoved | ✅ |
| `QLHSDNHTCP_04` | 17 | 661 | Reject | Resoved | ✅ |
| `QLNDTVVCG_03` | 277 | 1482 | Reject | Resoved | ✅ |
| `QLNDTVVCG_11` | 282 | 1490 | Reject | Resoved | ✅ |
| `QLNDTVVCG_23` | 287 | 1502 | Reject | Resoved | ✅ |
| `QLTKND_17` | 169 | 1179 | Reject | Resoved | ✅ |
| `QLTMBMHD_07` | 80 | 848 | Reject | Resoved | ✅ |
| `SLCTHT_06` | 264 | 1452 | Reject | Resoved | ✅ |
| `SLHDVM_06` | 191 | 1286 | Reject | Resoved | ✅ |
| `TLCTCDG_09` | 57 | 795 | Reject | Resoved | ✅ |
| `TPDBC_02` | 76 | 834 | Reject | Resoved | ✅ |
| `VVDHTHT_06` | 209 | 1313 | Reject | Resoved | ✅ |
| `VVDHT_06` | 203 | 1304 | Reject | Resoved | ✅ |
| `VVDTN_06` | 196 | 1295 | Reject | Resoved | ✅ |
| `VVTDVQL_06` | 239 | 1375 | Reject | Resoved | ✅ |
| `VVTLHDN_05` | 246 | 1391 | Reject | Resoved | ✅ |
| `VVTLV_05` | 243 | 1383 | Reject | Resoved | ✅ |
| `VVTTGCT_05` | 248 | 1399 | Reject | Resoved | ✅ |
| `VVTTG_05` | 216 | 1321 | Reject | Resoved | ✅ |

### Verify = `Reopen` — 22 mã

| Mã TC | Sheet 1 row | Sheet 2 row | Sheet 1 `Trạng thái dev fix 1` | Sheet 2 `Trạng thái dev fix` | |
|---|---|---|---|---|---|
| `CNKQHT_03` | 11 | 635 | dev done | InProcess | — |
| `IBMHD_07` | 119 | 917 | dev done | InProcess | — |
| `QLBMHD_08` | 101 | 891 | dev done | InProcess | — |
| `QLBMHD_13` | 106 | 896 | dev done | InProcess | — |
| `QLCHTHXLHS_03` | 153 | 1089 | dev done | InProcess | — |
| `QLDKTK_03` | 186 | 1264 | dev done | InProcess | — |
| `QLDMCQDVQL_12` | 140 | 1009 | dev done | InProcess | — |
| `QLDMCTHT_13` | 135 | 975 | dev done | InProcess | — |
| `QLDMHSDNHT_13` | 148 | 1065 | Reopen | InProcess | — |
| `QLHSDNHTCP_03` | 16 | 660 | dev done | InProcess | — |
| `QLHSDNHTCP_10` | 19 | 667 | dev done | InProcess | — |
| `QLHSPLDN_03` | 293 | 1534 | dev done | InProcess | — |
| `QLNDTVVCG_22` | 286 | 1501 | dev done | InProcess | — |
| `QLNDTVVCG_36` | 289 | 1515 | Reopen | InProcess | — |
| `QLNDTVVCG_40` | 290 | 1519 | dev done | InProcess | — |
| `QLPQCN_02` | 173 | 1200 | dev done | InProcess | — |
| `QLPQCN_03` | 174 | 1201 | dev done | InProcess | — |
| `QLTLPLCVV_07` | 296 | 1556 | dev done | InProcess | — |
| `QLTMBMHD_20` | 86 | 861 | dev done | InProcess | — |
| `THDG_03` | 70 | 822 | dev done | InProcess | — |
| `TKBMHD_03` | 113 | 907 | dev done | InProcess | — |
| `TKTMBMHD_04` | 89 | 868 | dev done | InProcess | — |

