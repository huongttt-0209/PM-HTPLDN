# Thông tin môi trường và tài khoản kiểm thử

> ⚠️ Chọn đúng môi trường và đúng kênh nhận OTP/email. Riêng **DEV nội bộ có hai phần tách biệt: dùng Gmail thật hoặc dùng MailHog**.

| Phần | Môi trường | Kênh nhận OTP/email |
|---|---|---|
| **Phần 1A** | DEV nội bộ `18.143.165.120.nip.io` | **Gmail thật** `diupt01@gmail.com` và các alias `diupt01+...@gmail.com` |
| **Phần 1B** | DEV nội bộ `18.143.165.120.nip.io` | **MailHog DEV** `http://18.143.165.120:8025/#` |
| **Phần 2** | Nghiệm thu đối tác `htpldn-uat.ospgroup.vn` | **MailHog nghiệm thu** `https://htpldn-uat.ospgroup.vn/mailhog/` |

---

## PHẦN 1 — DEV nội bộ

### Thông tin truy cập chung

- Web: https://18.143.165.120.nip.io/login

> ⚠️ Truy cập web bằng hostname `18.143.165.120.nip.io`, không dùng IP trực tiếp.

### Tài khoản DEV dùng chung cho cả hai phần
  

:key: ADMIN (Quản trị hệ thống)
  Username: admin
  Họ tên: Quản trị hệ thống
  Email: admin@htpldn.gov.vn
  Vai trò: QTHT (Quản trị hệ thống)
  Mật khẩu: Secret@123

  :bust_in_silhouette: TÀI KHOẢN NGHIỆP VỤ (mật khẩu Test@1234 — đã test login OK)
  cbnv_tw  | CB Nghiệp vụ - Trung ương | CB_NV_TW | Test@1234
  cbnv_bn  | CB Nghiệp vụ - Bộ ngành   | CB_NV_BN | Test@1234
  cbnv_dp  | CB Nghiệp vụ - Địa phương | CB_NV_DP | Test@1234
  cbpd_tw  | CB Phê duyệt - Trung ương | CB_PD_TW | Test@1234
             ↳ ⚠️ 11/08/2026 (env nội bộ 18.143.165.120): báo "Tên đăng nhập hoặc mật khẩu không đúng"
               → đã fallback `cbpd_tw_01` / Test@1234 (đăng nhập OK).
  cbpd_bn  | CB Phê duyệt - Bộ ngành   | CB_PD_BN | Test@1234
  cbpd_dp  | CB Phê duyệt - Địa phương | CB_PD_DP | Test@1234 

  Bộ tài khoản nghiệp vụ _01:
  cbnv_tw_01 | CB Nghiệp vụ - Trung ương | CB_NV_TW | Test@1234
  cbnv_bn_01 | CB Nghiệp vụ - Bộ ngành   | CB_NV_BN | Test@1234
  cbnv_dp_01 | CB Nghiệp vụ - Địa phương | CB_NV_DP | Test@1234
  cbpd_tw_01 | CB Phê duyệt - Trung ương | CB_PD_TW | Test@1234
  cbpd_bn_01 | CB Phê duyệt - Bộ ngành   | CB_PD_BN | Test@1234
  cbpd_dp_01 | CB Phê duyệt - Địa phương | CB_PD_DP | Test@1234

  Bộ tài khoản nghiệp vụ _02:
  cbnv_tw_02 | CB Nghiệp vụ - Trung ương | CB_NV_TW | Test@1234
  cbnv_bn_02 | CB Nghiệp vụ - Bộ ngành   | CB_NV_BN | Test@1234
  cbnv_dp_02 | CB Nghiệp vụ - Địa phương | CB_NV_DP | Test@1234
  cbpd_tw_02 | CB Phê duyệt - Trung ương | CB_PD_TW | Test@1234
  cbpd_bn_02 | CB Phê duyệt - Bộ ngành   | CB_PD_BN | Test@1234
  cbpd_dp_02 | CB Phê duyệt - Địa phương | CB_PD_DP | Test@1234

  Bộ tài khoản nghiệp vụ _03:
  cbnv_tw_03 | CB Nghiệp vụ - Trung ương | CB_NV_TW | Test@1234
  cbnv_bn_03 | CB Nghiệp vụ - Bộ ngành   | CB_NV_BN | Test@1234
  cbnv_dp_03 | CB Nghiệp vụ - Địa phương | CB_NV_DP | Test@1234
  cbpd_tw_03 | CB Phê duyệt - Trung ương | CB_PD_TW | Test@1234
  cbpd_bn_03 | CB Phê duyệt - Bộ ngành   | CB_PD_BN | Test@1234
  cbpd_dp_03 | CB Phê duyệt - Địa phương | CB_PD_DP | Test@1234

  Bộ tài khoản nghiệp vụ _04:
  cbnv_tw_04 | CB Nghiệp vụ - Trung ương | CB_NV_TW | Test@1234
  cbnv_bn_04 | CB Nghiệp vụ - Bộ ngành   | CB_NV_BN | Test@1234
  cbnv_dp_04 | CB Nghiệp vụ - Địa phương | CB_NV_DP | Test@1234
  cbpd_tw_04 | CB Phê duyệt - Trung ương | CB_PD_TW | Test@1234
  cbpd_bn_04 | CB Phê duyệt - Bộ ngành   | CB_PD_BN | Test@1234
  cbpd_dp_04 | CB Phê duyệt - Địa phương | CB_PD_DP | Test@1234

  Bộ tài khoản nghiệp vụ _05:
  cbnv_tw_05 | CB Nghiệp vụ - Trung ương | CB_NV_TW | Test@1234
  cbnv_bn_05 | CB Nghiệp vụ - Bộ ngành   | CB_NV_BN | Test@1234
  cbnv_dp_05 | CB Nghiệp vụ - Địa phương | CB_NV_DP | Test@1234
  cbpd_tw_05 | CB Phê duyệt - Trung ương | CB_PD_TW | Test@1234
  cbpd_bn_05 | CB Phê duyệt - Bộ ngành   | CB_PD_BN | Test@1234
  cbpd_dp_05 | CB Phê duyệt - Địa phương | CB_PD_DP | Test@1234

  nht_qa_01 | Người hỗ trợ pháp lý       | NHT      | Test@1234   (Sở Tư pháp An Giang)
  nht_qa_tw | Người hỗ trợ pháp lý       | NHT      | Test@1234   (Cục Bổ trợ tư pháp - Bộ Tư pháp, cấp TW)
             ↳ Dùng khi cần vai trò NHT thao tác trên tư vấn viên cùng đơn vị cấp TW.

  nht_ag_uat2 | Người hỗ trợ pháp lý      | NHT      | Test@1234   (Sở Tư pháp An Giang — NHT-STP-AG-0001, Đang hoạt động)
             ↳ Dùng khi cần người nhận phân công ở cấp Địa phương (An Giang). Lĩnh vực: Thương mại.

  0109998887 | QA UAT Kiểm Thử DN        | DN       | Test@1234   (DN-HNI-0001, Hà Nội)
  0209888006 | (Doanh nghiệp)            | DN       | Test@1234
  2323232323 | (Doanh nghiệp)            | DN       | Test@1234
             ↳ Tên đăng nhập của doanh nghiệp là mã số thuế. Dùng `0109998887` khi cần DN thuộc Hà Nội.

  cbnv_hn | CB Nghiệp vụ - Địa phương | CB_NV_DP | Test@1234   (Sở Tư pháp Hà Nội)
  cbpd_hn | CB Phê duyệt - Địa phương | CB_PD_DP | Test@1234   (Sở Tư pháp Hà Nội)
             ↳ Dùng khi cần thao tác trên dữ liệu thuộc Sở Tư pháp Hà Nội.

  qa_tvvseed28 | Tư vấn viên + Chuyên gia tư vấn | TVV + CG | Test@1234   (Cục Bổ trợ tư pháp - Bộ Tư pháp, cấp TW)
             ↳ Hiện có vai trò TVV + CG và loại tư vấn viên là CG. Dùng khi cần nhận hoặc từ chối phân công
               ở cấp TW. Nếu cần loại TVV thuần trong cùng đơn vị thì dùng tài khoản khác hoặc đổi lại loại.

### PHẦN 1A — DEV dùng Gmail thật nhận OTP/email

- Hộp thư thật nhận OTP/email: **`diupt01@gmail.com`**.
- Các tài khoản được gắn alias theo dạng `diupt01+...@gmail.com`; tất cả mail vẫn về hộp thư `diupt01@gmail.com`.
- Lấy OTP và kiểm thông báo trực tiếp trong Gmail thật theo đúng alias ở mapping bên dưới.
- **Không dùng MailHog khi chạy phần 1A.**

#### Mapping Gmail thật chạy bộ reverify — đã áp dụng 12/08/2026

  | Username/MST | Vai trò / đơn vị | TAI_KHOAN.email đã set |
  |---|---|---|
  | `admin` | QTHT | `diupt01+qtht@gmail.com` |
  | `cbnv_tw_01` / `cbnv_tw_02` | CB NV TW | `diupt01+cb-nv-a@gmail.com` / `diupt01+cb-nv-a-2@gmail.com` |
  | `cbpd_tw_01` / `cbpd_tw_02` | CB PD TW | `diupt01+cb-pd-a@gmail.com` / `diupt01+cb-pd-a-2@gmail.com` |
  | `cbnv_bn_01` / `cbpd_bn_01` | CB NV / CB PD Bộ KH&ĐT (lane escalation) | `diupt01+cb-nv-b@gmail.com` / `diupt01+cb-pd-b@gmail.com` |
  | `cbnv_hn` / `cbpd_hn` | CB NV / CB PD Sở TP Hà Nội | `diupt01+cb-nv-dn@gmail.com` / `diupt01+cb-pd-dn@gmail.com` |
  | `cbnv_dp_01` / `cbpd_dp_01` | CB NV / CB PD Sở TP An Giang | `diupt01+cb-nv-ag@gmail.com` / `diupt01+cb-pd-ag@gmail.com` |
  | `nht_qa_tw` / `nht_qa_01` | NHT TW / An Giang | `diupt01+nht-tw@gmail.com` / `diupt01+nht-ag@gmail.com` |
  | `qa_tvv_tw_r19` | TVV thuần TW | `diupt01+tvv-tw@gmail.com` |
  | `qa_tvv_dp_r18` | TVV thuần An Giang | `diupt01+tvv-ag@gmail.com` |
  | `qa_tvvseed28` | hồ sơ loại CG đang hoạt động | `diupt01+cg@gmail.com` |
  | `0109998887` | DN Hà Nội | `diupt01+dn-login@gmail.com` |
  | `0209888006` | DN An Giang | `diupt01+dn-ag-login@gmail.com` |

  - `qa_tvv_tw_r19` và `qa_tvv_dp_r18` đã được đặt lại mật khẩu thành `Test@1234` qua đúng luồng Quên mật khẩu và kiểm tra login thành công.
  - Email nghiệp vụ tách riêng: DN Hà Nội `diupt01+dn-contact@gmail.com`; DN An Giang `diupt01+dn-ag-contact@gmail.com`; DN không TK MST `0108051801` = `diupt01+dn-no-account@gmail.com`; tổ chức TW/An Giang = `diupt01+org-a@gmail.com` / `diupt01+org-b@gmail.com`.
  - Duyệt/từ chối đăng ký và công bố kết quả đào tạo dùng email TK DN/NHT đã tạo lượt đăng ký. Hủy/bắt đầu khóa dùng `HOC_VIEN.email`; bắt đầu khóa còn dùng `GIANG_VIEN.email` theo BR-NOTIF-01.
  - `GV-QA-001` đã set `diupt01+gv-01@gmail.com`. Hai HOC_VIEN `aaaa1111-0000-4000-8001-000000000001/2` đã set `diupt01+hv-01/02@gmail.com` bằng quyền QTHT và đọc lại thành công.
  - Ba case escalation dùng hồ sơ Bộ KH&ĐT. Theo BR-AUTH-02, đơn vị cha của Bộ/ngành là TW. Khi chạy phải đọc lại `donViChaId` và tập tài khoản hoạt động role `CB_PD_TW` tại đơn vị cha; không cố định `cbpd_tw_02` và không áp đặt gửi một hay tất cả khi SRS không nêu cardinality. Do kiểm bằng Gmail thật, mọi tài khoản có thể được resolver chọn phải được map sang alias `diupt01+...@gmail.com` trước khi chạy.

### PHẦN 1B — DEV dùng MailHog nhận OTP/email

- MailHog DEV: **http://18.143.165.120:8025/#**
- Khi chạy phần này, lấy OTP và kiểm email trực tiếp trong MailHog DEV.
- Lọc theo đúng địa chỉ người nhận gắn với tài khoản đang kiểm thử, sau đó chọn email mới nhất.
- **Không cần truy cập hộp thư Gmail thật khi chạy phần 1B.**
- Dùng bộ tài khoản DEV chung ở trên; không dùng bộ tài khoản của môi trường nghiệm thu.

---

## PHẦN 2 — Nghiệm thu của đối tác: dùng MailHog nhận OTP/email

### Truy cập và nguyên tắc nhận mail

- Web: https://htpldn-uat.ospgroup.vn/login
- Hộp thư nhận OTP/email: **MailHog** `https://htpldn-uat.ospgroup.vn/mailhog/`.
- Lọc thư theo đúng địa chỉ email gắn với tài khoản.
- **Không cần và không dùng quyền truy cập Gmail thật ở phần này.**

  > ⚠️ Môi trường này **có** bước nhập mã xác thực khi đăng nhập; lấy OTP trong **MailHog của env nghiệm thu**
  >    tại `https://htpldn-uat.ospgroup.vn/mailhog/`. Lọc theo đúng địa chỉ người nhận gắn với tài khoản;
  >    không cần quyền truy cập hộp thư email thật.
  >    Bộ tài khoản KHÁC env nội bộ — `nht_qa_tw`, `nht_01..04`, `cbpd_tw_01`… **không tồn tại hoặc
  >    không dùng `Test@1234`**. Đã kiểm chứng dùng được:

### Tài khoản kiểm thử trên môi trường nghiệm thu

  admin      | Quản trị hệ thống          | QTHT     | Secret@123
  cbnv_tw    | CB Nghiệp vụ - Trung ương  | CB_NV_TW | Test@1234   (donViId `...8000-000000000001`, cấp TW)
  nht_04_ui  | Người hỗ trợ pháp lý       | NHT      | Test@1234   (Cục Bổ trợ tư pháp - Bộ Tư pháp, cấp TW)
             ↳ Tài khoản kiểm thử NHT cấp TW. Giới hạn đăng nhập: 5 lượt / 60 giây.

  0151554887 | TKM Company (Tester TKM)   | DN       | Test@1234   (mã DN của Sở Tư pháp Hà Nội, tên đăng nhập = mã số thuế)
             ↳ Email nhận mã xác thực: `tkm@gmail.com`; lấy OTP trong MailHog bằng cách lọc theo địa chỉ này.

  cbnv_dp    | CB Nghiệp vụ - Địa phương  | CB_NV_DP | Test@1234   (Sở Tư pháp Hà Nội, donViId `...8002-000000000001`)
             ↳ Kiểm chứng 10/08/2026. Là người TẠO bản ghi `TVCS-20260803-0002` (TKM Company).
               ⚠️ Không phân công chuyên gia được: pool CG của đơn vị này RỖNG (cả 4 CG dùng được đều ở BTP·TW).

  truong_16    | Trương Văn Mười Sáu (CG)  | CG       | Test@1234   (BTP·TW, lĩnh vực **Thuế**, TVV-BTP-TW-0004)
  cb_nv_tw_03  | CB Nghiệp vụ - Trung ương | CB_NV_TW | Test@1234   (BTP·TW, `cb_nv_tw_03@htpldn.test`)
             ↳ Hai tài khoản seed QA, mật khẩu do QA **đặt lại ngày 10/08/2026** qua luồng Quên mật khẩu
               (mật khẩu cũ không phải `Test@1234`). Ghi lại để lượt sau khỏi dò.

  nht_01     | Người hỗ trợ pháp lý       | NHT      | Test@1234   (**Sở Tư pháp An Giang** — NHT-STP-AG-0001
             |                            |          |              "Phùng Thị NHT An Giang", email `nht_01@htpldn.test`)
             ↳ **Đây là tài khoản NHT cấp ĐỊA PHƯƠNG duy nhất đã dùng được trên env nghiệm thu.**
               Tiêu chí trong sheet ghi `nht_ag_uat2` — tên đó KHÔNG đăng nhập được ở env này, nhưng cùng
               trỏ về bản ghi NHT-STP-AG-0001. Mật khẩu do QA **đặt lại 11/08/2026** qua luồng Quên mật khẩu
               (chỉ nhận EMAIL, lấy link đặt lại mật khẩu trong MailHog theo địa chỉ đã gắn).
               ⚠️ Lần đăng nhập đầu phần mềm bắt bổ sung **CCCD của tài khoản** mới cho dùng tiếp — QA đã nhập
               `089185000835`, các lượt sau không hỏi lại nữa.
               Pool Tổ chức tư vấn của Sở Tư pháp An Giang **rỗng** (ô "Tổ chức hành nghề chính" không chọn được).

  ### Tài khoản cấp Bộ / Sở — QA đặt lại mật khẩu ngày 11/08/2026 (đều `Test@1234`)

  | Tên đăng nhập | Vai trò | Đơn vị |
  |---|---|---|
  | `cb_nv_bn_09` / `cb_pd_bn_09` | CB_NV_BN / CB_PD_BN | **Bộ Công Thương** (`00000000-0000-4000-8001-000000000003`) |
  | `cb_nv_dp_09` / `cb_pd_dp_09` | CB_NV_DP / CB_PD_DP | **Sở Tư pháp Bắc Ninh** (`00000000-0000-4000-8002-000000000011`) |
  | `cb_nv_dp_10` / `cb_pd_dp_10` | CB_NV_DP / CB_PD_DP | **Sở Tư pháp An Giang** (`00000000-0000-4000-8002-000000000006`) |
  | `tvv_dp_ag_01` | TVV | Sở Tư pháp An Giang — dùng để kiểm quyền "tư vấn viên KHÔNG xem được hồ sơ chi trả" |

  > ⚠️ **Tên đăng nhập ≠ phần trước `@` của email** với nhóm này: email là `tvv.dp.ag.01@htpldn.test`
  >    nhưng tên đăng nhập là `tvv_dp_ag_01` (dấu chấm → gạch dưới). Tra bằng `GET /api/v1/tai-khoan?search=<email>`
  >    trước khi đăng nhập, đừng đoán.
  >
  > ⚠️ **Luồng Quên mật khẩu:** `POST /api/v1/auth/forgot-password` chỉ nhận `{"tenDangNhap":"<EMAIL>"}`
  >    (phải là email hoặc MST 10 số, KHÔNG nhận tên đăng nhập). Đặt lại:
  >    `POST /api/v1/auth/reset-password` với `{"token","newPassword","newPasswordConfirm"}`.
  >
  > ⚠️ **Đăng nhập lần đầu bị chặn bởi hộp thoại bắt nhập số CCCD.** QA đã điền giá trị kiểm thử:
  >    `cb_nv_tw_03` 000000000003 · `cbnv_bn` 000000000011 · `cb_nv_bn_09` 000000000009 ·
  >    `cb_pd_bn_09` 000000000019 · `cb_nv_dp_09` 000000000029 · `cb_pd_dp_09` 000000000039 ·
  >    `cb_nv_dp_10` 000000000049.
  >
  > 🔴 **Một tài khoản chỉ giữ ĐƯỢC MỘT phiên.** Đăng nhập lại ở nơi khác (kể cả bằng `curl`) sẽ **đá**
  >    phiên đang mở trên trình duyệt. Nhiều vai trò song song thì mỗi vai trò một `isolatedContext`
  >    riêng và **một** lần đăng nhập duy nhất cho mỗi tài khoản.
  >
  > 🔴 **Kênh Cổng Dịch vụ công (LGSP) CHƯA mở trên env này** — `/ho-so-chi-tras/tiep-nhan-dvc`,
  >    `/bo-sung-dvc`, `/de-nghi-thanh-toan-dvc`, `/{id}/bo-sung-chung-tu` đều trả `401 ERR-CT-AUTH-01`;
  >    sổ `nhat-ky-tich-hops` và `ho-so-lgsp` đều 0 bản ghi. Hệ quả: **không** đưa được hồ sơ từ
  >    *Yêu cầu bổ sung* trở lại *Đang kiểm tra*, và **không** kiểm chứng được việc gửi ra Cổng.

  > ⚠️ **Tài khoản CG trên env này:** chỉ 4 CG có gắn tài khoản và đang hoạt động — `huongcg` (CG+TVV,
  >    lĩnh vực Đất đai/Hình sự/Lao động/Thuế), `truong_16` (Thuế), `ho_18` (Đất đai), `dinh_14` (chưa gán
  >    lĩnh vực). `huongcg` là tài khoản ĐỐI TÁC dùng trong video bug — **không** đặt lại mật khẩu của nó;
  >    `Test@1234` và các mật khẩu chung đều sai. `ho_18` cũng không dùng `Test@1234`.
  >
  > ⚠️ **Tài khoản chỉ có vai trò CG không thấy menu "Tư vấn chuyên sâu"** — phải vào bản ghi bằng URL
  >    trực tiếp `/tv-chuyen-sau/{id}`. Trên env này `navigate_page` (tải lại cả trang) KHÔNG làm mất phiên.

  ---
