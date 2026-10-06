# QLHDTVVCG_03 (sheet `bug` dòng 309) — Tìm kiếm hợp đồng bằng tiếng Việt CÓ DẤU

- Môi trường: https://18.143.165.120.nip.io — bản dựng **HTPLDN · V1.0.11**
- Tài khoản: `cbnv_tw_03` (CB Nghiệp vụ Trung ương, Cục Bổ trợ tư pháp - Bộ Tư pháp)
- Thời điểm: 2026-08-10 ~21:45
- Đường vào (đúng lối còn hiệu lực, KHÔNG log lại chuyện bỏ menu riêng): Vụ việc HTPL → chi tiết `VV-BTP-TW-20260804-002` → mục **HĐ tư vấn liên kết** → ô tìm kiếm gợi ý **"Tìm theo tên HĐ, mã HĐ, bên B"**
- Bảng đang có **4 hợp đồng** (lần verify trước có 2): `HDTV-20260808-0001` · `HDTV-20260807-0008` · `HDTV-20260807-0007` · `HDTV-20260807-0006`

## Tiêu chí đang verify (nguyên văn mục "DEV SỬA" trong ô Kết quả verify)

> Gõ một từ/cụm tiếng Việt có dấu đang có trong tên HĐ hoặc bên B của hợp đồng xem được → phải trả hợp đồng đó về bảng. Áp thống nhất cho cả 3 trường.

## Đo lại đúng các phép đo của lần reopen

| Từ khóa gõ | Trường chứa từ đó | Lần reopen | Lần này (2026-08-10) | Kết |
|---|---|---|---|---|
| `sở hữu trí tuệ` | tên HĐ (nguyên văn) | 0 — "Không tìm thấy hợp đồng phù hợp" | **1** → HDTV-20260807-0006 | ✅ |
| `nghiệp` (có dấu) | tên HĐ | 0 | **3** → 0001 · 0007 · 0006 | ✅ |
| `doanh` (đối chứng không dấu) | tên HĐ | 2 | **3** (bảng nay có 4 HĐ) | ✅ |
| `Chuyên` (có dấu) | bên B "Chuyên gia UAT QLNDTVVCG 38" | 0 | **1** → HDTV-20260807-0006 | ✅ |
| `chuyên gia` | bên B | — | **1** | ✅ |
| `UAT` / `QLNDTVVCG` | bên B | 1 / 1 | **1** / **1** | ✅ |
| `HDTV-20260807-0006` | mã HĐ | 1 | **1** | ✅ |
| `nghiep` (bản không dấu) | tên HĐ | 0 | **3** | ✅ |
| `so huu tri tue` (bản không dấu) | tên HĐ | 0 | **1** | ✅ |

Đo thêm để chắc quy luật cũ đã hết (mọi cụm đều có dấu, lấy nguyên văn từ dữ liệu đang hiện):
`trí tuệ` → 1 · `xác lập quyền` → 1 · `tuệ` → 1 · `bảo hiểm xã hội` → 1 (HDTV-20260807-0007) · `siêu nhỏ` → 1 (0007) · `hợp đồng` → 4 · `Hợp` → 4 · `đồng tư vấn` → 2.

⇒ **Quy luật "từ có dấu thì không tìm được" đã hết.** Cả hai chiều đều khớp: gõ có dấu ra đúng bản ghi, gõ bản không dấu của cùng từ cũng ra đúng bản ghi. Áp cho cả 3 trường: tên HĐ (`sở hữu trí tuệ`), bên B (`Chuyên`), mã HĐ (`HDTV-20260807-0006`).

## Ghi nhận thêm — KHÔNG thuộc tiêu chí lần verify này, không đổi verdict

Khớp **mã HĐ theo đầu chuỗi**, không khớp mảnh giữa: `HDTV` → 4 · `HDTV-20260807` → 3 · nhưng `0006` → 0. (`20260807` → 1 và bản ghi đó khớp vì chuỗi này nằm trong TÊN hợp đồng, không phải nhờ mã.) srs-fr-14-hop-dong-tv.md:224 ghi "Tìm kiếm toàn văn trên tên HĐ, mã HĐ, bên B" — người dùng dán trọn mã hoặc gõ đoạn đầu thì ra, gõ 4 số cuối thì rỗng. Chi tiết này KHÔNG phải nội dung lỗi đang treo (lỗi đang treo là dấu tiếng Việt) nên không mở rộng case; ghi lại để đơn vị chủ quản quyết có tách phiếu riêng hay không.

## Bằng chứng

- [image/QLHDTVVCG_03-r309-tim-so-huu-tri-tue-ra-ket-qua.png](image/QLHDTVVCG_03-r309-tim-so-huu-tri-tue-ra-ket-qua.png) — gõ `sở hữu trí tuệ` → 1-1 / 1 mục, đúng HDTV-20260807-0006, bản dựng V1.0.11 hiện ở thanh bên
