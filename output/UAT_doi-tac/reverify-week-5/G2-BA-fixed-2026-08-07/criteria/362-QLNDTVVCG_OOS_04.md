# Tiêu chí chấm — dòng 362 · `QLNDTVVCG_OOS_04` (nhật ký thao tác CG từ chối)

> **Nguồn đặc tả duy nhất:** `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-12-tv-chuyen-sau.md`
> (mtime 06/08/2026 22:52) + `srs-v3.5.md` §3.4.2. **Mọi số dòng dưới đây do chính lượt này mở file đọc lại
> ngày 2026-08-07.** **File này KHÔNG chứa verdict.** Chỉ là chuẩn để agent đo đối chiếu.

---

## 🔴 CẢNH BÁO — số dòng trong phiếu BA và ô sheet ĐÃ SAI

`srs-fr-12-tv-chuyen-sau.md` được sửa ngày 06/08/2026 theo chính các quyết định BA chốt hôm đó (chèn ghi
chú tác nhân CG, mã lỗi `ERR-TVCS-08/09`, các dòng `[BA chốt 2026-08-06]`) → nội dung trôi xuống. **Phiếu BA
`phan-hoi-ba-7-diem-can-chot-2026-08-06.md` §6 và ô `Kết quả mong đợi` cột K của dòng 362 đều quote số dòng
CŨ** (chúng được soạn trước lượt sửa file).

| Nội dung | Số dòng phiếu BA §6 / ô sheet ghi | **Số dòng THẬT (07/08/2026)** | Lệch |
|---|---|---|---|
| Bước "Ghi nhật ký thao tác (kèm lý do từ chối)" — luồng **CG từ chối** | `:198` | **`:204`** | +6 |
| Bước gửi thông báo CB NV — luồng CG từ chối | `:197` | **`:203`** | +6 |
| Khuôn khối Nhật ký thao tác (SCR-X1-02 thành phần 8) | `:1160` | **`:1173`** | +13 |
| CB PD từ chối phê duyệt — ghi nhật ký kèm lý do | `:232` | **`:238`** | +6 |
| Hủy yêu cầu — *"KHÔNG lưu thành cột riêng trên entity"* | `:244` | **`:250`** | +6 |
| BR-FLOW-04 (định nghĩa) | `:1614` | **`:1641`** | +27 |
| Tác nhân chính nhóm X.1 | `:37` | **`:34`** | −3 |

🔴 **Quan trọng hơn số dòng: NỘI DUNG đã đổi.** Phiếu BA §6 trích `:1160` là *"dd/mm/yyyy HH:mm -- {User} --
{Hành động}"* rồi kết luận *"**không có chỗ cho lý do**"*. Câu đó **đúng với bản SRS TRƯỚC lượt sửa 06/08**.
Bản hiện hành ở `:1173` **đã được sửa** và **đã đòi dòng phụ "Lý do: {nội dung}"**. Ai đọc phiếu BA §6 rồi
suy ra "đặc tả không đòi hiện lý do" là **đọc bản đã lỗi thời**.

---

## 1. Bug gốc — nguyên văn ô `Kết quả thực tế` (cột L), dòng 362

```
Nhật ký có ghi thao tác nhưng mất lý do, đo bằng 2 đường:
- Bảng "Nhật ký thao tác" trên màn chi tiết hiển thị "06/08/2026 09:31 · Cập nhật · QA TVV Seed28 Active
  (qa_tvvseed28) · Chuyên gia tư vấn, Tư vấn viên" — hành động ghi chung chung là "Cập nhật", không có cột
  hay dòng nào chứa lý do; bảng cũng không phân biệt được thao tác từ chối với thao tác chấp nhận.
- Bản ghi nhật ký đọc trực tiếp từ hệ thống có 18 trường (…) — không có trường nào mang lý do hay nội dung
  thay đổi. Giá trị hành động là UPDATE.
Đối chứng cho thấy lý do CÓ được hệ thống lưu ở nơi khác: nội dung thông báo gửi Cán bộ Nghiệp vụ có đoạn
"Lý do: QA FLOW04 QLNDTVVCG_26 - ly do tu choi ban ghi B luc 20260806". Nghĩa là dữ liệu không mất ngay,
nhưng nhật ký — nơi đặc tả chỉ định để tra cứu về sau — thì không giữ, còn thông báo và trường ghi chú của
bản ghi đều có thể bị ghi đè bởi lượt phân công / từ chối kế tiếp.
Đo trên bản dựng nhãn HTPLDN · V1.0.8, ngày 06/08/2026.
```

**Bóc ra 2 triệu chứng quan sát được:**
- **(a)** dòng nhật ký của thao tác từ chối **không mang lý do**;
- **(b)** nhãn hành động là **"Cập nhật"** chung, **không phân biệt được** thao tác từ chối.

⚠️ Đây là phiếu **QA phát hiện ngoài phạm vi đối tác** (ô `Mô tả` ghi rõ: *"QA phát hiện ngoài phạm vi (không
thuộc case nào của đối tác), phát sinh khi verify QLNDTVVCG_26"*), `Dopai = BA`, `Trạng thái dev fix = Fixed`.

---

## 2. Đặc tả nói gì

### 2.1 Luồng "CG từ chối" — các bước, và bước ghi nhật ký nằm ở dòng nào

`srs-v3.5/srs-fr-12-tv-chuyen-sau.md:195` — `**Processing — CG từ chối** (PHAN_CONG → TIEP_NHAN) [GAP-X.1-01]`

| Dòng | Bước | Nguyên văn đọc được | BR |
|---|---|---|---|
| `:199` | 1 | `Kiểm tra user là CG được phân công cho bản ghi này` | BR-AUTH-01 |
| `:200` | 2 | `Kiểm tra trạng thái hiện tại = PHAN_CONG` | SM-TVCS |
| `:201` | 3 | `Yêu cầu lý do từ chối (bắt buộc)` | — |
| `:202` | 4 | `Xóa liên kết chuyen_gia_id, trạng thái → TIEP_NHAN` | — |
| `:203` | 5 | `Gửi thông báo CB NV (in-app + email): CG từ chối, cần phân công lại — **nội dung thông báo phải đính kèm lý do từ chối** [BA chốt 2026-08-06]` | BR-NOTIF-01 |
| 🔴 `:204` | 6 | `Ghi nhật ký thao tác (kèm lý do từ chối) — **lý do hiển thị trên khối Nhật ký thao tác của hồ sơ** (SCR-X1-02 thành phần 8), nhãn hành động là "Từ chối" (không gộp vào "Cập nhật") [BA chốt 2026-08-06]` | **BR-DATA-05** |

⇒ Bước ghi nhật ký = **bước 6**, ở **`srs-fr-12-tv-chuyen-sau.md:204`** (KHÔNG phải `:198`), gắn **BR-DATA-05**.

### 2.2 BR-DATA-05 — định nghĩa ở đâu, đòi gì

| Vị trí | Nguyên văn đọc được |
|---|---|
| `srs-v3.5/srs-fr-12-tv-chuyen-sau.md:1619` | `### BR-DATA-05: Audit trail` (bảng ở `:1621`–`:1623`) |
| `srs-v3.5/srs-fr-12-tv-chuyen-sau.md:1623` | `\| BR-DATA-05 \| Mọi thao tác CUD + phê duyệt + đăng nhập/xuất đều ghi vào AUDIT_LOG. Log là immutable, không sửa/xóa. **[STT63 UAT 2026-06-02] Bổ sung: ghi AUDIT_LOG cả hành vi ĐỌC/TẢI tư liệu pháp lý của Chuyên gia (CG)** — hành vi đọc nhạy cảm của mạng lưới ngoài, phục vụ truy vết \| NFR-06 \| FR-X.1-01 đến FR-X.1-07 \| — \| Verify INSERT-only trên AUDIT_LOG + log read của CG \|` |
| `srs-v3.5/srs-v3.5.md:5569` | (bản master, cùng nội dung) `\| BR-DATA-05 \| **Audit trail:** Mọi thao tác CUD + phê duyệt + đăng nhập/xuất đều ghi vào AUDIT_LOG. Log là immutable, không sửa/xóa…` |
| `srs-v3.5/srs-fr-12-tv-chuyen-sau.md:289` | `- **BR-DATA-05**: Ghi nhật ký thao tác -> Xem Phụ lục B (file chính)` |

🔴 **BR-DATA-05 KHÔNG liệt kê trường nào phải lưu.** Nó chỉ chốt 3 điều: (1) mọi thao tác CUD/phê duyệt/đăng
nhập-xuất **phải** vào AUDIT_LOG; (2) log **immutable**; (3) mở rộng ghi cả hành vi đọc/tải tư liệu của CG.
**Yêu cầu "kèm lý do từ chối" KHÔNG đến từ BR-DATA-05** — nó đến từ **chính câu chữ của bước 6 tại `:204`**.

Đối chứng cấu trúc bản ghi nhật ký: `srs-v3.5/srs-v3.5.md:2236` —
`| hanh_dong | text | Y | CHECK IN ('CREATE','UPDATE','DELETE','APPROVE','REJECT','CANCEL','ASSIGN','LOGIN','LOGOUT','PUBLISH','UNPUBLISH') [bổ sung 'CANCEL','ASSIGN' 2026-08-06 — hủy và phân công vốn không có giá trị riêng, bị gộp vào 'UPDATE'] | | Loại hành động |`
⇒ Giá trị `REJECT` **đã có sẵn** trong danh mục hành động; giá trị `UPDATE` mà QA quan sát được ở lượt 06/08
đúng là biểu hiện của việc gộp thao tác.

### 2.3 Nhãn hành động có phải phân biệt "Từ chối" với "Cập nhật" không — **CÓ, đặc tả đòi rõ**

Đây là điểm **đã đổi** so với hiểu biết cũ. Bản hiện hành đòi ở **4 chỗ độc lập**:

| Dòng | Nguyên văn đọc được |
|---|---|
| 🔴 `srs-v3.5/srs-fr-12-tv-chuyen-sau.md:204` | `… nhãn hành động là "Từ chối" (không gộp vào "Cập nhật") [BA chốt 2026-08-06]` |
| 🔴 `srs-v3.5/srs-fr-12-tv-chuyen-sau.md:1173` | `\| 8 \| content \| Accordion: Nhật ký thao tác \| timeline \| Lịch sử chuyển trạng thái + CUD. Khuôn dòng: "dd/mm/yyyy HH:mm -- {User} -- {Hành động}". **Riêng hành động Từ chối (CG từ chối nhận việc · CB PD từ chối phê duyệt) và Hủy yêu cầu: thêm dòng phụ "Lý do: {nội dung}"** — chỉ hiện phần lý do, KHÔNG mở các trường khác của bản chụp hồ sơ [BA chốt 2026-08-06]. **Dòng phụ Lý do chỉ hiện với vai trò nội bộ** (CB NV, CB PD, NHT theo phạm vi đơn vị); **KHÔNG** hiện với người trong mạng lưới tư vấn — họ vẫn xem được phần còn lại của khối nhật ký như trước. Nhãn hành động lấy từ bảng action-level `TU_VAN_CHUYEN_SAU` (`srs-v3.5.md` §3.4.2) — thao tác Từ chối phải có nhãn riêng, không gộp vào "Cập nhật" \| — \| mode chi tiết \|` |
| 🔴 `srs-v3.5/srs-v3.5.md:1442` | `\| TVCS_REJECT \| **Từ chối nhận việc** (nhãn hiển thị trên Nhật ký thao tác: "Từ chối", KHÔNG gộp vào "Cập nhật") \| CG \| record.chuyen_gia_id = current_user AND record.trang_thai = PHAN_CONG AND có lý do từ chối \| FR-X.1-01 \|` (bảng *TU_VAN_CHUYEN_SAU — Action-level permissions*, tiêu đề `srs-v3.5.md:1428`, `[BA chốt 2026-08-06 — UAT tuần 5]`) |
| 🔴 `srs-v3.5/srs-fr-12-tv-chuyen-sau.md:347` | `- **Given** CB NV mở hồ sơ đã có lượt từ chối **When** xem khối Nhật ký thao tác **Then** thấy dòng hành động "Từ chối" kèm dòng phụ "Lý do: …" [BA chốt 2026-08-06]` |

Và một tiêu chí chấp nhận **giới hạn phạm vi xem**:

`srs-v3.5/srs-fr-12-tv-chuyen-sau.md:348` — `- **Given** CG mở chính hồ sơ đó **When** xem khối Nhật ký thao tác **Then** thấy đủ các dòng nhật ký nhưng **không** thấy dòng phụ "Lý do" [BA chốt 2026-08-06]`

⇒ **Đặc tả KHÔNG im lặng về nhãn hành động.** Nó đòi cả hai: **nhãn riêng "Từ chối"** *và* **dòng phụ
"Lý do: …"** — nhưng dòng phụ **chỉ** hiện với vai trò nội bộ.

### 2.4 Đặc tả IM LẶNG về những gì

| # | Điểm im lặng | Hệ quả khi chấm |
|---|---|---|
| S-1 | **Chữ chính xác** của nhãn (vd "Từ chối" hay "Từ chối nhiệm vụ") | `:1173` + `:1442` chỉ đòi nhãn **riêng, không gộp vào "Cập nhật"**. Cấm chấm Fail vì sai một chữ |
| S-2 | **Vị trí/hình thức** của phần lý do (dòng phụ, tooltip, cột, khối bung ra) | `:1173` nêu khuôn *"Lý do: {nội dung}"* nhưng ràng buộc thật là **chỉ hiện phần lý do, không mở các trường khác** |
| S-3 | Lý do có phải lưu thành **cột riêng trên entity** không | Đặc tả **cố ý không** — tiền lệ `:250` cho thao tác hủy: *"KHÔNG lưu thành cột riêng trên entity"*. Lý do sống ở nhật ký |
| S-4 | BR-DATA-05 **không** liệt kê trường bắt buộc của bản ghi nhật ký | Cấm suy ra "bản ghi nhật ký phải có trường `ly_do`" từ BR-DATA-05 (xem §2.2) |

⚠️ **BR-FLOW-04 KHÔNG phủ ca này.** `srs-v3.5/srs-fr-12-tv-chuyen-sau.md:1641` — `| BR-FLOW-04 | Mọi hành động
từ chối phê duyệt PHẢI có lý do (text, min 10 ký tự)… | CĐT xác nhận | FR-X.1-01 (CB PD từ chối TVCS) | … |`
⇒ áp cho **CB Phê duyệt từ chối phê duyệt**, không phải **CG từ chối nhận việc**. Đừng quote nhầm.

---

## 3. Tiêu chí chấm

> **Bug gốc = "dòng nhật ký của thao tác từ chối không lưu / không mang được lý do"** (`00-BRIEF.md` §Bảng bug
> gốc: *"đạt khi dòng nhật ký của thao tác từ chối mang được lý do"*). Mô tả yêu cầu nghiệp vụ, không kê đơn
> implementation.

**Phép đo bắt buộc chạy trên DỮ LIỆU MỚI:** tạo/lấy một hồ sơ TVCS ở trạng thái *Phân công* → đăng nhập bằng
chính chuyên gia được phân công → bấm [Từ chối], nhập **chuỗi lý do có dấu nhận dạng riêng** → đăng nhập lại
bằng **CB Nghiệp vụ cùng đơn vị** → mở màn chi tiết hồ sơ đó → mở khối **"Nhật ký thao tác"**.

### ✅ `Test done` khi

Trên khối "Nhật ký thao tác" của **chính hồ sơ vừa bị từ chối**, xem bằng **vai trò nội bộ** (CB Nghiệp vụ /
CB Phê duyệt cùng đơn vị):

1. **Có một dòng ứng với thao tác từ chối** (đúng thời điểm + đúng người là chuyên gia đã bấm Từ chối), **và**
2. **Dòng đó mang được lý do** — đọc lại được đúng chuỗi lý do đã nhập ở bước từ chối, **và**
3. **Nhãn hành động của dòng đó phân biệt được thao tác từ chối** — không còn là nhãn "Cập nhật" chung dùng
   lẫn với thao tác khác (`:204`, `:1173`, `:1442`, AC `:347`), **và**
4. **Lý do không bị mất/ghi đè** sau khi hồ sơ được phân công lại cho chuyên gia khác — mở lại khối nhật ký
   vẫn đọc được lý do của lượt từ chối cũ (đây chính là điều cột L nêu: *"thông báo và trường ghi chú… đều có
   thể bị ghi đè bởi lượt phân công / từ chối kế tiếp"*).

⇒ Verdict `Test done`, ô `Kết quả verify` mở đầu `✅ ĐÃ HẾT LỖI`.

### ❌ `Reopen` khi

Trên hồ sơ **vừa bị từ chối sau khi có bản sửa**, xem bằng **vai trò nội bộ**:

- Khối nhật ký **không có dòng nào mang lý do** cho thao tác từ chối — cán bộ phải phân công lại không có
  đường chính thức nào trên hồ sơ để tra lại vì sao bị từ chối; **hoặc**
- Dòng từ chối vẫn mang **nhãn "Cập nhật"** chung, **không phân biệt** được với thao tác cập nhật/chấp nhận
  (vi phạm `:204` + `:1173` + `:1442` + AC `:347` — cả 4 đều là câu chữ đang có hiệu lực); **hoặc**
- Lý do đọc được ngay sau khi từ chối nhưng **biến mất / bị ghi đè** sau lượt phân công hoặc từ chối kế tiếp.

⇒ Ô `Kết quả verify` mở đầu `🔁 CÒN LỖI — chuyển lại dev`, **BẮT BUỘC** kèm mục `CÁCH KIỂM LẠI SAU KHI SỬA`
(điều kiện trước · các bước · ✅ đạt khi · ❌ chưa đạt khi · ⚠️ bẫy), ghi **giống hệt từng chữ** với file report.

### ⚠️ `BA confirm` khi — **về nguyên tắc KHÔNG dùng cho case này**

BA **đã chốt** case này ngày 06/08 (xem §4). Chỉ mở lại nhánh BA khi gặp **mâu thuẫn spec mới**, cụ thể:
quan sát được cả hai vế đều đạt nhưng **hành vi thực tế ngược một câu chữ khác của chính đặc tả** đến mức
không thể vừa Pass vừa đúng SRS. Khi đó ghi rõ 2 câu chữ mâu thuẫn + số dòng, không tự chọn bên.

> **Không** dùng `BA confirm` chỉ vì hình thức hiển thị lý do khác khuôn *"Lý do: {nội dung}"* — xem §2.4 S-2.

### 🚫 KHÔNG được dùng làm lý do Reopen (ngoài bug gốc — `00-BRIEF.md` §PHẠM VI)

- Thông báo gửi CB Nghiệp vụ có/không đính lý do (`:203`) — khác vế với nhật ký.
- Dòng phụ "Lý do" **có hiện** với vai trò mạng lưới tư vấn (ngược AC `:348`) → ghi **1 dòng** vào
  `99-quan-sat-ngoai-pham-vi.md`, KHÔNG chặn Pass, KHÔNG điều tra thêm.
- Nhãn hành động của các thao tác **khác** (Hủy, Phân công, Chấp nhận) còn gộp vào "Cập nhật".
- Luồng **CB PD từ chối phê duyệt** (`:238`) hoặc **Hủy yêu cầu** (`:250`) chưa hiện lý do — hai ca đó BA ghi
  *"Đề nghị áp cùng cách"*, là việc dev khác, không phải bug gốc của dòng 362.
- Bất kỳ 4xx/5xx nào gặp khi chuyển màn / đổi vai trò ngoài các bước bắt buộc của phép đo trên.

---

## 4. Trạng thái BA — **ĐÃ CHỐT 06/08/2026**

**Phiếu:** `../ba-confirm/phan-hoi-ba-7-diem-can-chot-2026-08-06.md` §6 (heading ở dòng `:443` —
*"# 6. Cán bộ phải phân công lại nhưng không tra lại được lý do chuyên gia từ chối"*).

**Trích nguyên văn câu chốt** (`:477`):

> **→ Kết luận: yêu cầu "ghi nhật ký kèm lý do từ chối" là ĐẠT — không phải lỗi. Nhưng chốt cải tiến: HIỆN LÝ
> DO CÓ KIỂM SOÁT trên khối nhật ký của hồ sơ. Dev action: Có · Sửa đặc tả: Có · Sheet: giữ xử lý.** ✅ **BA
> duyệt 06/08/2026.**

**Câu ghi rõ để Dev và QA không hiểu nhầm** (`:479`):

> ⚠️ **Ghi rõ để Dev và QA không hiểu nhầm:** đây **không phải bug** — dữ liệu đã ghi đúng đặc tả. Đây là
> **cải tiến đã được duyệt**, làm vì cán bộ phải phân công lại cần tra lại lý do. Phiếu `QLNDTVVCG_OOS_04` để
> **giữ xử lý**, không Reject.

**Bảng "Việc phải thi hành sau khi chốt"** (`:654`): `| QLNDTVVCG_OOS_04 | giữ xử lý | Dev làm cải tiến đã duyệt |`

**Cái gì ĐẠT / cái gì là cải tiến — tách bạch:**

| | Nội dung | BA chốt |
|---|---|---|
| **ĐẠT (không phải lỗi)** | Yêu cầu **"ghi nhật ký kèm lý do từ chối"** — lý do **có** được lưu, không bị lượt sau ghi đè (dev đo lại) | ✅ ĐẠT |
| **Cải tiến đã duyệt** (Dev action: Có · Sửa đặc tả: Có) | ① **Tách nhãn riêng cho thao tác Từ chối** — đang gộp vào "Cập nhật" · ② **Hiển thị duy nhất phần lý do** trên khối nhật ký, KHÔNG mở các trường khác của bản chụp hồ sơ · ③ **Phạm vi xem:** chỉ vai trò nội bộ (CB NV, CB PD, NHT theo đơn vị), KHÔNG mở cho người trong mạng lưới tư vấn · ④ nhãn lấy từ bảng quyền mức thao tác `TU_VAN_CHUYEN_SAU` | ✅ duyệt |

🔴 **Cả 4 hạng mục cải tiến ĐÃ ĐƯỢC ĐƯA VÀO SRS** (`:204`, `:1173`, `:347`, `:348`, `srs-v3.5.md:1442`) — nên
tại thời điểm đo 07/08, chúng **không còn là "mong muốn ngoài đặc tả"** mà đã là **câu chữ đặc tả có hiệu
lực**. Đây là lý do §3 đặt nhãn hành động vào nhánh `Reopen` chứ không phải "bỏ qua".

**Ô `DEV phản hồi lần 1` của dòng 362** (chỉ là manh mối, không phải căn cứ verdict):

> *"Dev đã tách nhãn thao tác "Từ chối" khỏi thao tác cập nhật chung và hiển thị lý do có kiểm soát trên nhật ký."*

---

## 5. Bẫy khi đo

### 5.1 Bẫy làm **Reopen oan**

1. 🔴 **Đo lại trên bản ghi CŨ đã bị từ chối TRƯỚC bản sửa** (vd `TVCS-20260803-0003` của lượt 06/08). Đây là
   bug về **dữ liệu đã lưu** — bản ghi nhật ký cũ đóng băng ở trạng thái trước fix, mở lại vẫn thiếu lý do dù
   dev đã sửa đúng. **Phép thử quyết định BẮT BUỘC là một lượt từ chối MỚI**, tạo sau bản dựng đang đo.
2. 🔴 **Đọc khối nhật ký bằng chính tài khoản chuyên gia.** AC `:348` chốt: CG **KHÔNG** được thấy dòng phụ
   "Lý do". Đo bằng CG rồi kết luận "không có lý do" = **chấm Reopen oan trên hành vi đúng đặc tả**. Phải đăng
   nhập **CB Nghiệp vụ cùng đơn vị**.
3. **Đo bằng vai trò ngoài đơn vị của hồ sơ.** Phạm vi xem gắn đơn vị — sai đơn vị thì không thấy hồ sơ.
4. **Không mở accordion.** "Nhật ký thao tác" là **accordion** (`:1173`, thành phần 8) và chỉ có ở **mode chi
   tiết** — mặc định thu gọn, dễ tưởng là trống.
5. **Đòi đúng chữ "Lý do:" hoặc đúng nhãn "Từ chối" từng ký tự.** Xem §2.4 S-1, S-2 — đặc tả đòi **phân biệt
   được** và **đọc được lý do**, không đòi khớp từng chữ.
6. **Đòi bản ghi nhật ký phải có trường `ly_do` riêng.** Đặc tả **cố ý không** tạo cột riêng trên entity
   (`:250`). Chấm theo **thứ đọc được trên khối nhật ký của hồ sơ**, không theo tên trường kỹ thuật.
7. **Quote `:198` / `:1160` / `:1614` từ phiếu BA §6 hoặc ô cột K.** Cả 3 đều đã lệch, và `:1160` còn lệch cả
   **nội dung** — xem §Cảnh báo đầu file. Quote sai bản = bug invalid.
8. **Tab mở lâu chạy bó mã cũ** → tải lại trang, ghi vân tay bản dựng trước khi đo.

### 5.2 Bẫy làm **Pass oan**

1. 🔴 **Thấy lý do trong THÔNG BÁO gửi CB Nghiệp vụ rồi kết luận đạt.** Lượt 06/08 đã chứng minh thông báo
   **có** lý do trong khi nhật ký **không** có. Bug gốc nói về **khối nhật ký của hồ sơ** (`:204` + `:1173`),
   không phải thông báo (`:203`). Hai vế khác nhau.
2. 🔴 **Thấy có dòng nhật ký mới sinh ra là đạt.** Cột L đã ghi rõ: *"Nhật ký **có ghi thao tác** nhưng mất lý
   do"*. Sinh dòng ≠ mang lý do.
3. 🔴 **Dừng lại ngay sau khi từ chối.** Phải **phân công lại cho chuyên gia khác** rồi mở lại khối nhật ký —
   cột L cảnh báo lý do *"có thể bị ghi đè bởi lượt phân công / từ chối kế tiếp"*. Đây là điều kiện ✅ số 4.
4. **Dùng lý do trùng chữ với lần trước / chuỗi chung chung.** Phải nhập **chuỗi có dấu nhận dạng riêng** (mã
   phiếu + thời điểm) để phân biệt lý do của lượt này với lượt cũ, tránh đọc nhầm dòng.
5. **Chỉ có 1 dòng nhật ký trong khối.** Nếu hồ sơ mới tinh chỉ có đúng 1 dòng thì **không phân biệt được**
   "nhãn riêng cho Từ chối" với "nhãn chung". Cần hồ sơ có **≥2 loại thao tác** (vd Phân công → Từ chối) để
   thấy nhãn có tách hay không.
6. **Đọc nhầm dòng theo thời gian.** Đối chiếu **cả 3**: thời điểm · người thực hiện (phải là chuyên gia đã
   bấm Từ chối) · nội dung lý do.
