from pathlib import Path
from collections import defaultdict
from openpyxl import Workbook, load_workbook
from openpyxl.styles import Font, PatternFill, Border, Side, Alignment
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.utils import get_column_letter

OUT = Path(__file__).resolve().parent
SRS = "Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5"
TODAY = "2026-08-12"
PRIMARY_MAILBOX = "diupt01@gmail.com"

def load_existing_execution_results():
    path = OUT / "UAT-Email-Reverify-Test-Suite.xlsx"
    if not path.exists():
        return {}
    wb = load_workbook(path, data_only=False, read_only=True)
    results = {}
    for sheet_name in ("02_Tai_khoan", "03_Doanh_nghiep", "04_Notification", "05_SMTP_Sec_NFR"):
        if sheet_name not in wb.sheetnames:
            continue
        ws = wb[sheet_name]
        rows = ws.iter_rows(values_only=True)
        headers = {name: idx for idx, name in enumerate(next(rows))}
        for row in rows:
            tcid = row[headers["Test Case ID"]]
            status = row[headers["Trạng thái"]]
            if tcid and status in {"Pass", "Fail"}:
                results[tcid] = {
                    key: row[headers[key]] or ""
                    for key in ("Kết quả thực tế", "Evidence", "Trạng thái", "Bug ID", "Tester / Ngày", "Ghi chú")
                }
    wb.close()
    return results

existing_execution_results = load_existing_execution_results()

def tc_alias(tcid, suffix=""):
    tag = tcid.lower()
    extra = f"-{suffix}" if suffix else ""
    return f"diupt01+uat-{tag}{extra}@gmail.com"

MAILBOX_ROWS = [
    ("MB_PRIMARY", PRIMARY_MAILBOX, "Oracle nhận OTP và email thông báo thật trên DEV", "Đăng nhập Gmail; tìm `to:<alias>` kèm mốc thời gian/subject", "Mọi diupt01+...@gmail.com sẽ về hộp thư này"),
    ("MB_ALIAS_CHECK", "diupt01+check@gmail.com", "Preflight kiểm tra Gmail plus alias", "to:diupt01+check@gmail.com", "Đã gửi/nhận và xác minh trường To lúc 14:07 ICT 2026-08-12"),
    ("MB_QTHT", "diupt01+qtht@gmail.com", "Quản trị hệ thống", "to:diupt01+qtht@gmail.com", "TAI_KHOAN.email của username admin trên DEV"),
    ("MB_TK_CURRENT", "diupt01+tk-current@gmail.com", "TAI_KHOAN.email hiện tại", "to:diupt01+tk-current@gmail.com", "Khác MB_TK_OLD/MB_TK_NEW/MB_DN_CONTACT"),
    ("MB_TK_OLD", "diupt01+tk-old@gmail.com", "Email tài khoản trước khi đổi", "to:diupt01+tk-old@gmail.com", "Mailbox âm sau khi đổi"),
    ("MB_TK_NEW", "diupt01+tk-new@gmail.com", "Email tài khoản sau khi đổi", "to:diupt01+tk-new@gmail.com", "Mailbox dương sau khi đổi"),
    ("MB_DN_CONTACT", "diupt01+dn-contact@gmail.com", "DOANH_NGHIEP.email liên hệ", "to:diupt01+dn-contact@gmail.com", "Khác email TK khi test routing"),
    ("MB_DN_LOGIN", "diupt01+dn-login@gmail.com", "TAI_KHOAN.email của DN đã có tài khoản", "to:diupt01+dn-login@gmail.com", "Khác MB_DN_CONTACT để kiểm đúng nguồn recipient"),
    ("MB_DN_AG_LOGIN", "diupt01+dn-ag-login@gmail.com", "TAI_KHOAN.email của DN An Giang", "to:diupt01+dn-ag-login@gmail.com", "TK 0209888006; khác email liên hệ DN"),
    ("MB_DN_AG_CONTACT", "diupt01+dn-ag-contact@gmail.com", "DOANH_NGHIEP.email liên hệ của DN An Giang", "to:diupt01+dn-ag-contact@gmail.com", "DN-AGG-0001; không dùng thay email TK trong workflow"),
    ("MB_DN_NO_ACCOUNT", "diupt01+dn-no-account@gmail.com", "DOANH_NGHIEP.email của DN không có tài khoản", "to:diupt01+dn-no-account@gmail.com", "MST 0108051801; email-only; không tạo TAI_KHOAN"),
    ("MB_DN_REGISTER", "diupt01+dn-register@gmail.com", "DN tự đăng ký: cùng giá trị ở TAI_KHOAN.email và DOANH_NGHIEP.email", "to:diupt01+dn-register@gmail.com", "Chỉ dùng case yêu cầu đồng bộ ban đầu"),
    ("MB_CB_NV_A", "diupt01+cb-nv-a@gmail.com", "CB nghiệp vụ đúng đơn vị A", "to:diupt01+cb-nv-a@gmail.com", "Khác CB PD và đơn vị B"),
    ("MB_CB_NV_A_2", "diupt01+cb-nv-a-2@gmail.com", "CB nghiệp vụ thứ hai cùng đơn vị A", "to:diupt01+cb-nv-a-2@gmail.com", "Tách người tạo và người được giao xử lý"),
    ("MB_CB_PD_A", "diupt01+cb-pd-a@gmail.com", "CB phê duyệt đúng đơn vị A", "to:diupt01+cb-pd-a@gmail.com", "Khác CB NV và đơn vị B"),
    ("MB_CB_PD_A_2", "diupt01+cb-pd-a-2@gmail.com", "CB phê duyệt thứ hai cùng đơn vị TW", "to:diupt01+cb-pd-a-2@gmail.com", "Chỉ dùng cho escalation sau khi dev xác nhận/config đúng quan hệ nhận"),
    ("MB_CB_NV_B", "diupt01+cb-nv-b@gmail.com", "CB nghiệp vụ mailbox âm đơn vị B", "to:diupt01+cb-nv-b@gmail.com", "Không được nhận sự kiện của A"),
    ("MB_CB_PD_B", "diupt01+cb-pd-b@gmail.com", "CB phê duyệt mailbox âm đơn vị B", "to:diupt01+cb-pd-b@gmail.com", "Không được nhận sự kiện của A"),
    ("MB_CB_NV_HN", "diupt01+cb-nv-dn@gmail.com", "CB nghiệp vụ Sở Tư pháp Hà Nội", "to:diupt01+cb-nv-dn@gmail.com", "Dùng sửa/kiểm DN Hà Nội và workflow địa phương"),
    ("MB_CB_PD_HN", "diupt01+cb-pd-dn@gmail.com", "CB phê duyệt Sở Tư pháp Hà Nội", "to:diupt01+cb-pd-dn@gmail.com", "Cùng đơn vị với DN 0109998887"),
    ("MB_CB_NV_AG", "diupt01+cb-nv-ag@gmail.com", "CB nghiệp vụ Sở Tư pháp An Giang", "to:diupt01+cb-nv-ag@gmail.com", "Dùng lane vụ việc/chi trả An Giang"),
    ("MB_CB_PD_AG", "diupt01+cb-pd-ag@gmail.com", "CB phê duyệt Sở Tư pháp An Giang", "to:diupt01+cb-pd-ag@gmail.com", "Cùng đơn vị với DN/TVV/NHT An Giang"),
    ("MB_TVV_TW", "diupt01+tvv-tw@gmail.com", "Tư vấn viên thuần cấp TW", "to:diupt01+tvv-tw@gmail.com", "qa_tvv_tw_r19 / TVV-BTP-TW-0016"),
    ("MB_TVV_AG", "diupt01+tvv-ag@gmail.com", "Tư vấn viên thuần An Giang", "to:diupt01+tvv-ag@gmail.com", "qa_tvv_dp_r18 / TVV-STP-AG-0001"),
    ("MB_CG", "diupt01+cg@gmail.com", "Chuyên gia/người được phân công đánh giá", "to:diupt01+cg@gmail.com", "Không dùng chung TVV/NHT"),
    ("MB_NHT_TW", "diupt01+nht-tw@gmail.com", "Người hỗ trợ đơn vị TW", "to:diupt01+nht-tw@gmail.com", "Không dùng chung TVV/CG"),
    ("MB_NHT_AG", "diupt01+nht-ag@gmail.com", "Người hỗ trợ Sở Tư pháp An Giang", "to:diupt01+nht-ag@gmail.com", "Dùng kiểm đúng phạm vi đơn vị/địa phương"),
    ("MB_HV_01", "diupt01+hv-01@gmail.com", "HOC_VIEN.email học viên 01", "to:diupt01+hv-01@gmail.com", "Dùng sự kiện hủy/bắt đầu khóa theo BR-NOTIF-01; đã set"),
    ("MB_HV_02", "diupt01+hv-02@gmail.com", "HOC_VIEN.email học viên 02", "to:diupt01+hv-02@gmail.com", "Dùng kiểm gửi đủ học viên; đã set"),
    ("MB_GV_01", "diupt01+gv-01@gmail.com", "GIANG_VIEN.email giảng viên của khóa", "to:diupt01+gv-01@gmail.com", "Dùng sự kiện khóa bắt đầu theo BR-NOTIF-01; đã set"),
    ("MB_ORG_A", "diupt01+org-a@gmail.com", "Email liên hệ tổ chức tư vấn A/CC dương", "to:diupt01+org-a@gmail.com", "Khác ORG_B"),
    ("MB_ORG_B", "diupt01+org-b@gmail.com", "Email liên hệ tổ chức tư vấn B/mailbox âm", "to:diupt01+org-b@gmail.com", "Không được nhận sự kiện của A"),
    ("MB_ATTACKER", "diupt01+attacker@gmail.com", "Mailbox âm cho header injection", "to:diupt01+attacker@gmail.com", "Tuyệt đối không được nhận"),
    ("PATTERN_TC", "diupt01+uat-{test-case-id}@gmail.com", "Email mới/unique theo từng TC tạo TK, đăng ký, token hoặc claim", "to:<email cụ thể đã sinh>", "Ví dụ EM-TK-ACT-01 → diupt01+uat-em-tk-act-01@gmail.com; không tái sử dụng"),
    ("PATTERN_TC_VARIANT", "diupt01+uat-{test-case-id}-{old|new|dn}@gmail.com", "Các biến thể cần phân biệt email cũ/mới/DN trong cùng TC", "to:<email biến thể>", "Mỗi biến thể là một recipient logic riêng"),
    ("MB_BOUNCE", "bounce@example.invalid", "SMTP failure/bounce", "Không có inbox", "Không thay bằng Gmail alias; cần SMTP stub/DSN harness"),
    ("MST_RANGE", "0100000001..0100009999", "Mỗi TC một MST", "—", "Không tái sử dụng"),
]

DEV_SETUP_COLS = [
    "Nhóm setup", "Username/Mã record", "ID trên DEV", "Vai trò/Loại",
    "Đơn vị đã xác minh", "Trạng thái", "Email trước setup", "Email hiện tại/đã set",
    "Trường đã cập nhật", "Liên kết/Điều kiện", "Mục đích test", "Kết quả xác minh"
]

DEV_SETUP_ROWS = [
    ("TAI_KHOAN", "admin", "00000000-0000-4000-8000-000000000099", "QTHT", "Không gắn đơn vị", "HOAT_DONG", "admin@htpldn.gov.vn", "diupt01+qtht@gmail.com", "TAI_KHOAN.email", "Tài khoản quản trị hiện hữu", "Quản trị/cấp tài khoản", "ĐÃ SET + đọc lại API"),
    ("TAI_KHOAN", "cbnv_tw_01", "6647b7bb-db9a-4a12-9535-766c77a4f04b", "CB_NV_TW", "Cục Bổ trợ tư pháp - Bộ Tư pháp", "HOAT_DONG", "cbnv_tw_01@htpldn.test", "diupt01+cb-nv-a@gmail.com", "TAI_KHOAN.email", "CB NV chính lane TW", "Hỏi đáp/đào tạo/TVV-CG/TVCS/đánh giá", "ĐÃ SET + OTP/login verified"),
    ("TAI_KHOAN", "cbnv_tw_02", "75ef9f6b-5f5b-474d-9861-dde1c1563f50", "CB_NV_TW", "Cục Bổ trợ tư pháp - Bộ Tư pháp", "HOAT_DONG", "cbnv_tw_02@htpldn.test", "diupt01+cb-nv-a-2@gmail.com", "TAI_KHOAN.email", "Assignee thứ hai cùng đơn vị", "Phân công/chuyển xử lý", "ĐÃ SET + đọc lại API"),
    ("TAI_KHOAN", "cbpd_tw_01", "2bd5fc7f-8b33-4427-954d-c011a7555f06", "CB_PD_TW", "Cục Bổ trợ tư pháp - Bộ Tư pháp", "HOAT_DONG", "cbpd_tw_01@htpldn.test", "diupt01+cb-pd-a@gmail.com", "TAI_KHOAN.email", "CB phê duyệt chính lane TW", "Duyệt/từ chối/đánh giá", "ĐÃ SET + OTP/login verified"),
    ("TAI_KHOAN", "cbpd_tw_02", "305a7f9c-cfcd-41ea-8354-108f42dfca7f", "CB_PD_TW", "Cục Bổ trợ tư pháp - Bộ Tư pháp", "HOAT_DONG", "cbpd_tw_02@htpldn.test", "diupt01+cb-pd-a-2@gmail.com", "TAI_KHOAN.email", "Một ứng viên nhận escalation tại đơn vị cha TW; không cố định cardinality khi SRS không nêu", "Escalation", "ĐÃ SET email; đối soát recipient theo role + don_vi_cha_id"),
    ("TAI_KHOAN", "cbnv_bn_01", "a2ad2192-ebaf-4971-9b36-2beca4d1c216", "CB_NV_BN", "Bộ Kế hoạch và Đầu tư", "HOAT_DONG", "cbnv_bn_01@htpldn.test", "diupt01+cb-nv-b@gmail.com", "TAI_KHOAN.email", "Đơn vị B", "Mailbox âm", "ĐÃ SET + đọc lại API"),
    ("TAI_KHOAN", "cbpd_bn_01", "e8a57e11-77a4-40f6-8907-30a95b1e229f", "CB_PD_BN", "Bộ Kế hoạch và Đầu tư", "HOAT_DONG", "cbpd_bn_01@htpldn.test", "diupt01+cb-pd-b@gmail.com", "TAI_KHOAN.email", "Đơn vị B", "Mailbox âm", "ĐÃ SET + đọc lại API"),
    ("TAI_KHOAN", "cbnv_hn", "87bb5785-2ab8-4fa1-847b-ce2ac61f1793", "CB_NV_DP", "Sở Tư pháp Hà Nội", "HOAT_DONG", "cbnv.hn@htpldn.test", "diupt01+cb-nv-dn@gmail.com", "TAI_KHOAN.email", "Lane Hà Nội", "DN 0109998887", "ĐÃ SET + OTP/login verified"),
    ("TAI_KHOAN", "cbpd_hn", "82ff67b4-7702-4a6a-b4bd-0d41ddc3311d", "CB_PD_DP", "Sở Tư pháp Hà Nội", "HOAT_DONG", "cbpd.hn@htpldn.test", "diupt01+cb-pd-dn@gmail.com", "TAI_KHOAN.email", "Lane Hà Nội", "Duyệt hồ sơ Hà Nội", "ĐÃ SET + đọc lại API"),
    ("TAI_KHOAN", "cbnv_dp_01", "e81aa51b-e132-49a4-8831-fd404512af40", "CB_NV_DP", "Sở Tư pháp An Giang", "HOAT_DONG", "cbnv_dp_01@htpldn.test", "diupt01+cb-nv-ag@gmail.com", "TAI_KHOAN.email", "Lane An Giang", "Vụ việc/chi trả", "ĐÃ SET + đọc lại API"),
    ("TAI_KHOAN", "cbpd_dp_01", "8ed9e497-387f-4d37-ac06-8c1545b593a5", "CB_PD_DP", "Sở Tư pháp An Giang", "HOAT_DONG", "cbpd_dp_01@htpldn.test", "diupt01+cb-pd-ag@gmail.com", "TAI_KHOAN.email", "Lane An Giang", "Duyệt vụ việc/chi trả", "ĐÃ SET + đọc lại API"),
    ("TAI_KHOAN", "nht_qa_tw", "a31689a8-019e-40ff-b084-58f55589b694", "NHT", "Cục Bổ trợ tư pháp - Bộ Tư pháp", "HOAT_DONG", "nht.qa.tw@htpldn.test", "diupt01+nht-tw@gmail.com", "TAI_KHOAN.email", "NHT TW", "Nộp hồ sơ/đăng ký học", "ĐÃ SET + đọc lại API"),
    ("TAI_KHOAN", "nht_qa_01", "9a1fbbcd-364a-4b41-9dac-15696847caba", "NHT", "Sở Tư pháp An Giang", "HOAT_DONG", "nht_qa_01@htpldn.test", "diupt01+nht-ag@gmail.com", "TAI_KHOAN.email", "NHT An Giang", "Nộp hồ sơ/đăng ký học", "ĐÃ SET + đọc lại API"),
    ("TAI_KHOAN + TU_VAN_VIEN", "qa_tvv_tw_r19 | TVV-BTP-TW-0016", "TK 3f9d5fc4-eac3-4229-8c2c-3f79a952ed83 | TVV aaaa1707-0000-4000-8000-000000000d01", "TVV thuần", "Cục Bổ trợ tư pháp - Bộ Tư pháp", "HOAT_DONG", "qa.tvv.tw.r19@htpldn.gov.vn", "diupt01+tvv-tw@gmail.com", "TAI_KHOAN.email + TU_VAN_VIEN.email", "Đã khôi phục TK; reset mật khẩu test", "TVV lane TW", "ĐÃ SET + reset/login verified"),
    ("TAI_KHOAN + TU_VAN_VIEN", "qa_tvv_dp_r18 | TVV-STP-AG-0001", "TK a0529ecc-e050-4723-8b6b-5c15045cadf4 | TVV 4c1d3aab-db59-40f8-9a58-b8637c42d8ab", "TVV thuần", "Sở Tư pháp An Giang", "HOAT_DONG", "qa.tvv.dp.r18@htpldn.gov.vn", "diupt01+tvv-ag@gmail.com", "TAI_KHOAN.email + TU_VAN_VIEN.email", "Liên kết TC-STP-AG-0001; reset mật khẩu test", "TVV lane An Giang", "ĐÃ SET + reset/login verified"),
    ("TAI_KHOAN + TU_VAN_VIEN", "qa_tvvseed28 | TVV-BTP-TW-0002", "TK 5432719c-c542-4a5d-8c3a-db1b8a918bbf | TVV 98cfd963-3cd3-4c8a-bfa9-625460824d6d", "TVV+CG; hồ sơ CG", "Cục Bổ trợ tư pháp - Bộ Tư pháp", "HOAT_DONG", "qa.tvvseed28@htpldn-uat.local", "diupt01+cg@gmail.com", "TAI_KHOAN.email + TU_VAN_VIEN.email", "Liên kết TCTV-SEED-0001", "CG fixture chính; người được phân công đánh giá", "ĐÃ SET + login endpoint verified"),
    ("TAI_KHOAN + DOANH_NGHIEP", "0109998887 | DN-HNI-0001", "TK 996cc5db-43c5-4903-b3d1-1c21adb2ece8 | DN 829abcac-b0af-4cde-9af9-ec51bc79014c", "DN", "Sở Tư pháp Hà Nội", "HOAT_DONG", "qa.uat.dn.verify@test.htpldn.vn", "TK: diupt01+dn-login@gmail.com | DN: diupt01+dn-contact@gmail.com", "TAI_KHOAN.email + DOANH_NGHIEP.email", "Hai email cố ý khác nhau", "Routing nguồn TK/DN", "ĐÃ SET + OTP/login verified"),
    ("TAI_KHOAN + DOANH_NGHIEP", "0209888006 | DN-AGG-0001", "TK b9c7f944-989f-48f4-8457-9d2e28875fc5 | DN c03a66bc-f584-437d-89c8-1371f6a69772", "DN", "Sở Tư pháp An Giang", "HOAT_DONG", "qa.uat.dn.angiang@test.htpldn.vn", "TK: diupt01+dn-ag-login@gmail.com | DN: diupt01+dn-ag-contact@gmail.com", "TAI_KHOAN.email + DOANH_NGHIEP.email", "Hai email cố ý khác nhau", "Vụ việc/chi trả An Giang", "ĐÃ SET + đọc lại API"),
    ("DOANH_NGHIEP", "DN-01-0002 | MST 0108051801", "6c75f283-d560-48ca-ba7c-524e6a690ff0", "DN không TK", "Cục Bổ trợ tư pháp - Bộ Tư pháp", "Đang hoạt động", "uat.v108.tvcs@example.test", "diupt01+dn-no-account@gmail.com", "DOANH_NGHIEP.email", "Không có TAI_KHOAN trùng MST", "TVCS email-only", "ĐÃ SET + xác minh không có account"),
    ("DOANH_NGHIEP", "DN-07-0001 | MST 0722072207", "92cdc9c1-41d1-4802-bc1f-bd7fb2e239de", "DN không TK", "Cục Bổ trợ tư pháp - Bộ Tư pháp", "Đang hoạt động", "NULL", "Giữ NULL", "Không cập nhật", "Không có TAI_KHOAN trùng MST", "Negative thiếu recipient", "ĐÃ xác minh giữ NULL"),
    ("TO_CHUC_TU_VAN", "TCTV-SEED-0001", "5eed0004-0000-4000-8000-000000000001", "Tổ chức A", "Cục Bổ trợ tư pháp - Bộ Tư pháp", "HOAT_DONG", "NULL", "diupt01+org-a@gmail.com", "TO_CHUC_TU_VAN.email", "Liên kết TVV-BTP-TW-0002", "CC tổ chức A", "ĐÃ SET + đọc lại API"),
    ("TO_CHUC_TU_VAN", "TC-STP-AG-0001", "d19eb64b-58ba-4993-b1d7-7762845459b6", "Tổ chức B", "Sở Tư pháp An Giang", "HOAT_DONG", "tctv.qa.dp@htpldn.test", "diupt01+org-b@gmail.com", "TO_CHUC_TU_VAN.email", "Liên kết TVV-STP-AG-0001", "CC/mailbox âm", "ĐÃ SET + đọc lại API"),
    ("HOC_VIEN", "Học viên TW 01", "aaaa1111-0000-4000-8001-000000000001", "HOC_VIEN", "Cục Bổ trợ tư pháp - Bộ Tư pháp", "taiKhoanId=NULL", "hv.aaaa1@htpldn.local", "diupt01+hv-01@gmail.com", "HOC_VIEN.email", "Dùng/gắn vào khóa fixture khi chạy TC", "Hủy/bắt đầu khóa gửi HV", "ĐÃ SET + đọc lại API"),
    ("HOC_VIEN", "Học viên TW 02", "aaaa1111-0000-4000-8001-000000000002", "HOC_VIEN", "Cục Bổ trợ tư pháp - Bộ Tư pháp", "taiKhoanId=NULL", "hv.aaaa2@htpldn.local", "diupt01+hv-02@gmail.com", "HOC_VIEN.email", "Dùng/gắn vào cùng khóa fixture khi chạy TC", "Kiểm gửi đủ HV", "ĐÃ SET + đọc lại API"),
    ("GIANG_VIEN", "GV-QA-001 | TS. Lê Hoàng Thái", "f0fafafa-0000-4000-8000-000000000001", "GIANG_VIEN", "Cục Bổ trợ tư pháp - Bộ Tư pháp", "DANG_HOAT_DONG; taiKhoanId=NULL", "qa-gv-thai@htpldn.test", "diupt01+gv-01@gmail.com", "GIANG_VIEN.email", "Có lịch sử giảng dạy; chọn làm GV cùng khóa fixture", "Khóa bắt đầu gửi GV", "ĐÃ SET + đọc lại API"),
    ("DYNAMIC", "DYNAMIC_NEW_ACCOUNT", "Không pre-seed", "Theo từng TC", "—", "Chưa tồn tại", "—", "diupt01+uat-{test-case-id}@gmail.com", "QA tạo qua UI/API", "Không seed trước; cleanup sau TC", "Activation/reset/unique/claim", "QA tạo khi chạy"),
    ("DYNAMIC", "DYNAMIC_DN_REGISTER", "Không pre-seed", "DN", "—", "Chưa tồn tại", "—", "Alias theo TC; TK.email = DN.email lúc đăng ký", "QA tạo qua tự đăng ký", "MST/username/email phải chưa tồn tại", "DN tự đăng ký", "QA tạo khi chạy"),
]

COLS = [
    "STT", "Test Case ID", "TraceID (Mã SRS)", "Nhóm/Feature", "Priority", "Type",
    "Tên Test Case / Mục tiêu", "Tác nhân", "Điểm bắt đầu luồng", "Pre-conditions (Tiền đề)",
    "Test Data (Dữ liệu)", "Các bước thực hiện", "Kết quả mong đợi theo bước",
    "Nguồn địa chỉ nhận", "Expected To / CC", "Mailbox KHÔNG được nhận",
    "UI / API / Queue / SMTP / Audit cần kiểm tra", "Post-condition / Cleanup",
    "Kết quả thực tế", "Evidence", "Trạng thái", "Bug ID", "Tester / Ngày", "Ghi chú"
]

groups = {"account": [], "enterprise": [], "notification": [], "infra": []}

def add(group, tcid, trace, feature, priority, typ, title, actor, start, pre, data, steps,
        expected, source="—", tocc="—", negative="—", oracle="—", cleanup="—",
        status="Not Run", note=""):
    groups[group].append({
        "Test Case ID": tcid, "TraceID (Mã SRS)": trace, "Nhóm/Feature": feature,
        "Priority": priority, "Type": typ, "Tên Test Case / Mục tiêu": title,
        "Tác nhân": actor, "Điểm bắt đầu luồng": start, "Pre-conditions (Tiền đề)": pre,
        "Test Data (Dữ liệu)": data, "Các bước thực hiện": steps,
        "Kết quả mong đợi theo bước": expected, "Nguồn địa chỉ nhận": source,
        "Expected To / CC": tocc, "Mailbox KHÔNG được nhận": negative,
        "UI / API / Queue / SMTP / Audit cần kiểm tra": oracle,
        "Post-condition / Cleanup": cleanup, "Kết quả thực tế": "", "Evidence": "",
        "Trạng thái": status, "Bug ID": "", "Tester / Ngày": "", "Ghi chú": note
    })

def ui_case(group, tcid, trace, title, actor, start, fields, absent=""):
    add(group, tcid, trace, "UI field verification", "P0", "UI", title, actor, start,
        "Có tài khoản đúng quyền; dữ liệu danh mục cần thiết đã seed.", "Không có.",
        "1. Đăng nhập bằng đúng vai trò.\n2. Mở màn hình theo điểm bắt đầu.\n3. Đối chiếu từng trường, kiểu input, required/readonly và nút với SRS.\n4. Kiểm tra điều kiện hiển thị/ẩn.\n5. Kiểm tra tab order, label và thông báo validation khi bỏ trống.",
        f"1. Đăng nhập và phân quyền đúng.\n2. Màn hình mở đúng.\n3. Có đủ: {fields}.\n4. Nút/field chỉ hiện đúng điều kiện.\n5. Required, readonly và validation đúng SRS." + (f"\nNEGATIVE: Không được có {absent}." if absent else ""),
        oracle="Kiểm tra màn hình không thay đổi dữ liệu và không phát sinh email; queue/audit chỉ khi có quyền.")

def validation_case(group, tcid, trace, title, start, data, expected, actor="QTHT/CB NV/DN"):
    rejected = expected.lstrip().startswith(("Không cho", "Từ chối"))
    post_submit = (
        "5. Reload: số bản ghi hiển thị không đổi, form không đóng/reset, không tạo token/job/email."
        if rejected else
        "5. Reload: email được lưu đúng; UI/API hiển thị đúng giá trị và chỉ phát sinh email nếu workflow của thao tác yêu cầu."
    )
    add(group, tcid, trace, "Email validation", "P0", "Negative/Edge", title, actor, start,
        "Đang ở form có trường email; ghi nhận số bản ghi hiển thị và inbox trước test.", data,
        "1. Mở form.\n2. Nhập đầy đủ các trường khác hợp lệ.\n3. Nhập email theo Test Data.\n4. Bấm Lưu/Đăng ký.\n5. Reload màn hình, kiểm tra UI/API response và inbox.",
        f"1-3. Form nhận đúng dữ liệu.\n4. {expected}\n{post_submit}",
        source="Field email đang kiểm tra", tocc="Không gửi mail nếu validation thất bại",
        negative="Tất cả mailbox test khi validation thất bại",
        oracle="Kiểm tra UI/API response, số bản ghi hiển thị và Gmail; queue/audit chỉ khi có quyền.")

FEATURE_FIXTURE = {
    "Hỏi đáp": "Lane TW: cbnv_tw_01=diupt01+cb-nv-a@gmail.com; cbnv_tw_02=diupt01+cb-nv-a-2@gmail.com; cbpd_tw_01=diupt01+cb-pd-a@gmail.com; mailbox âm khác đơn vị: cbnv_bn_01/cbpd_bn_01.",
    "Đào tạo": "Lane TW: cbnv_tw_01=diupt01+cb-nv-a@gmail.com; cbpd_tw_01=diupt01+cb-pd-a@gmail.com. Duyệt đăng ký/công bố KQ dùng TK 0109998887=diupt01+dn-login@gmail.com hoặc nht_qa_tw=diupt01+nht-tw@gmail.com. Hủy/bắt đầu khóa dùng HOC_VIEN aaaa...001=diupt01+hv-01@gmail.com, aaaa...002=diupt01+hv-02@gmail.com; GV-QA-001=diupt01+gv-01@gmail.com.",
    "TVV/CG": "Lane TW: nht_qa_tw=diupt01+nht-tw@gmail.com; cbnv_tw_01=diupt01+cb-nv-a@gmail.com; cbpd_tw_01=diupt01+cb-pd-a@gmail.com; TVV qa_tvv_tw_r19=diupt01+tvv-tw@gmail.com; CG qa_tvvseed28=diupt01+cg@gmail.com.",
    "Vụ việc": "Lane An Giang: DN 0209888006 TK=diupt01+dn-ag-login@gmail.com, DN liên hệ=diupt01+dn-ag-contact@gmail.com; cbnv_dp_01=diupt01+cb-nv-ag@gmail.com; cbpd_dp_01=diupt01+cb-pd-ag@gmail.com; nht_qa_01=diupt01+nht-ag@gmail.com; TVV qa_tvv_dp_r18=diupt01+tvv-ag@gmail.com; tổ chức TC-STP-AG-0001=diupt01+org-b@gmail.com.",
    "Chi trả": "Lane An Giang: DN 0209888006 TK=diupt01+dn-ag-login@gmail.com; cbnv_dp_01=diupt01+cb-nv-ag@gmail.com; cbpd_dp_01=diupt01+cb-pd-ag@gmail.com; TVV qa_tvv_dp_r18=diupt01+tvv-ag@gmail.com.",
    "Đánh giá": "Lane TW: cbnv_tw_01=diupt01+cb-nv-a@gmail.com; cbpd_tw_01=diupt01+cb-pd-a@gmail.com; người được phân công là CG qa_tvvseed28=diupt01+cg@gmail.com.",
    "Tư vấn chuyên sâu": "Lane TW: DN không TK MST 0108051801=diupt01+dn-no-account@gmail.com; CG qa_tvvseed28=diupt01+cg@gmail.com; cbnv_tw_01=diupt01+cb-nv-a@gmail.com; cbpd_tw_01=diupt01+cb-pd-a@gmail.com.",
}

def workflow_case(tcid, trace, feature, title, actor, start, pre, data, state_change,
                  source, tocc, negative, content, extra_oracle="", typ="Workflow", priority="P0",
                  email_expected=True, app_expected=True):
    fixture = FEATURE_FIXTURE.get(feature)
    if tcid in {"EM-NOT-HDD-04", "EM-NOT-HDD-07", "EM-NOT-VV-10"}:
        exact_data = data + "\nFixture escalation Bộ/ngành: tạo hồ sơ tại Bộ KH&ĐT; CB NV cùng cấp `cbnv_bn_01` = `diupt01+cb-nv-b@gmail.com`; CB PD cùng cấp `cbpd_bn_01` = `diupt01+cb-pd-b@gmail.com`. Trước trigger, đọc `DON_VI.don_vi_cha_id` của Bộ KH&ĐT và danh sách TAI_KHOAN `CB_PD_TW` hoạt động tại đúng đơn vị cha; mọi tài khoản có thể được resolver chọn phải được map sang alias `diupt01+...@gmail.com` để kiểm bằng Gmail thật."
        scope_oracle = "Escalation phải có ít nhất một recipient là TAI_KHOAN hoạt động, role CB_PD_TW, don_vi_id = don_vi_cha_id của Bộ KH&ĐT; không khẳng định gửi một hay tất cả khi SRS không quy định cardinality. Mọi recipient escalation thực tế phải thỏa role/phạm vi này."
        extra_oracle = (extra_oracle + " " + scope_oracle).strip()
    else:
        exact_data = data + (f"\nFixture DEV đã gắn email: {fixture}" if fixture else "")
    expected_email = (
        f"5. Chỉ đúng người nhận nhận email; {content}; đúng 1 email/người/sự kiện."
        if email_expected else
        "5. Không có email mới ở bất kỳ mailbox nào; Gmail count giữ nguyên."
    )
    if app_expected and email_expected:
        expected_app = "7. Với đối tượng được SRS chỉ định nhận in-app: đúng người nhận thấy đúng một thông báo mới trên chuông; số chưa đọc, nội dung, thời gian, link và trạng thái đã đọc đúng; tài khoản khác không thấy. Người chưa có tài khoản chỉ nhận email và không có thông báo trên ứng dụng."
    elif app_expected:
        expected_app = "7. Đúng người nhận thấy đúng một thông báo mới trên chuông; số chưa đọc, nội dung, thời gian, link và trạng thái đã đọc đúng; tài khoản khác không thấy; Gmail không có thư mới."
    else:
        expected_app = "7. Không có thông báo mới trên chuông; số chưa đọc giữ nguyên ở mọi tài khoản kiểm tra."
    add("notification", tcid, trace, feature, priority, typ, title, actor, start, pre, exact_data,
        "1. Xóa thư cũ; ghi nhận trạng thái hồ sơ và số chưa đọc trên chuông.\n2. Đăng nhập đúng tác nhân, mở đúng hồ sơ ở trạng thái nguồn.\n3. Thực hiện hành động trigger; không bấm lặp.\n4. Reload chi tiết/danh sách và chờ email tối đa 5 phút.\n5. Kiểm tra mailbox Expected To/CC và toàn bộ mailbox âm.\n6. Đối chiếu chuông với Gmail; kiểm queue/SMTP log và audit nếu có quyền.\n7. Nếu SRS quy định in-app: đăng nhập từng tài khoản nhận, mở chuông và trang Xem tất cả thông báo; kiểm số chưa đọc, nội dung, thời gian, link, trạng thái đã đọc; đăng nhập tài khoản âm để kiểm không nhìn thấy. Người nhận chưa có tài khoản không kiểm chuông.",
        f"1. Baseline sạch, không nhầm email cũ.\n2. Hồ sơ và quyền đúng tiền đề.\n3. {state_change}.\n4. UI phản ánh trạng thái mới.\n{expected_email}\n6. Gmail và chuông đúng với kênh được cấu hình; queue/audit khớp nếu có quyền.\n{expected_app}",
        source=source, tocc=tocc, negative=negative,
        oracle="Kiểm tra trạng thái trên UI/API, Gmail và chuông của đúng người nhận/tài khoản âm; queue/SMTP/audit chỉ khi có quyền." + (" " + extra_oracle if extra_oracle else ""),
        cleanup="Khôi phục fixture hoặc dùng hồ sơ mới cho case kế tiếp; lưu message-id và ảnh inbox/log.")

def no_mail_case(tcid, trace, title, start, actor, data):
    add("enterprise", tcid, trace, "Luồng chỉ tạo DOANH_NGHIEP", "P0", "Negative regression",
        title, actor, start,
        "MST chưa tồn tại; mailbox email DN đang trống; đã ghi số bản ghi hiển thị.", data,
        "1. Xóa thư cũ và ghi baseline UI.\n2. Thực hiện luồng tạo/tiếp nhận DN với dữ liệu hợp lệ.\n3. Chờ quá 5 phút.\n4. Reload hồ sơ DN.\n5. Kiểm tra hồ sơ trên UI/API, chuông và Gmail.",
        "1. Baseline xác định được.\n2. Tạo đúng một doanh nghiệp hiển thị trên hệ thống.\n3. Không có email kích hoạt.\n4. DN tồn tại với MST/tên/email liên hệ đúng.\n5. Không có tài khoản đăng nhập mới, email kích hoạt hoặc thông báo kích hoạt trên chuông.",
        source="Không áp dụng", tocc="Không có", negative="Mailbox DN và mọi mailbox test",
        oracle="Kiểm tra hồ sơ DN trên UI/API, không có tài khoản mới, Gmail và chuông không có kích hoạt.",
        cleanup="Xóa/đánh dấu fixture theo quy trình môi trường test; không dùng lại MST cho case khác.")

# ---------------------------------------------------------------------------
# 01. TÀI KHOẢN
# ---------------------------------------------------------------------------
ui_case("account", "EM-TK-UI-01", "FR-VIII-15 / SCR-VIII-03 / srs-fr-10:676-751,1707-1743",
        "Kiểm tra màn Quản lý tài khoản và form tạo/sửa", "QTHT", "Quản trị hệ thống > Tài khoản",
        "danh sách đối chiếu theo SCR-VIII-03; form UI có username*, email*, họ tên*, vai trò*, đơn vị*, loại TK*, CCCD; input nghiệp vụ FR-VIII-15 còn có điện thoại; tạo mới KHÔNG có mật khẩu",
        "nút admin đặt/đổi mật khẩu; mật khẩu trên form tạo")
ui_case("account", "EM-TK-UI-02", "FR-VIII-22 / SCR-VIII-08 / srs-fr-10:1024-1128,1900-1943",
        "Kiểm tra email trên form DN tự đăng ký", "DN chưa có TK", "Đăng nhập > Đăng ký dành cho doanh nghiệp",
        "một ô Email bắt buộc, tooltip nêu dùng cho login/kích hoạt/reset/notification và đồng thời là email liên hệ; username readonly tự lấy MST; mật khẩu + xác nhận + cam kết")
ui_case("account", "EM-TK-UI-03", "FR-VIII-26 / srs-fr-10:1278-1369",
        "Kiểm tra form Quên mật khẩu", "User bất kỳ", "Đăng nhập > Quên mật khẩu",
        "một ô Tên đăng nhập nhận email hoặc MST; nút gửi link; form qua link có mật khẩu mới + xác nhận",
        "hai ô riêng Email và MST; ô yêu cầu email khớp DOANH_NGHIEP.email")
ui_case("account", "EM-TK-UI-04", "FR-VIII-15 / SCR-VIII-03 / srs-fr-10:1726",
        "Kiểm tra điều kiện hiển thị Gửi lại email kích hoạt", "QTHT", "Quản trị hệ thống > Tài khoản",
        "hành động Gửi lại email kích hoạt chỉ ở trạng thái phù hợp; không có Đổi MK")

validation_case("account", "EM-TK-VAL-01", "FR-VIII-15 Inputs#2", "Bỏ trống email tài khoản", "Quản trị > Tài khoản > Thêm mới", "email = rỗng", "Không cho submit; field Email báo bắt buộc.")
validation_case("account", "EM-TK-VAL-02", "FR-VIII-15 Inputs#2; FR-VIII-22 Inputs#14", "Chấp nhận email hợp lệ cơ bản", "Form tạo tài khoản", tc_alias("EM-TK-VAL-02"), "Cho lưu nếu các field khác hợp lệ.")
validation_case("account", "EM-TK-VAL-03", "FR-VIII-15 Inputs#2; SCR-VIII-03 Email RFC 5322", "Chấp nhận Gmail plus alias", "Form tạo tài khoản", tc_alias("EM-TK-VAL-03"), "Cho lưu khi các field khác hợp lệ; nếu phát sinh thư thì Gmail thật phải nhận và trường To đúng alias.")
for i, (name, value) in enumerate([
    ("Thiếu ký tự @", "qa.example.test"), ("Thiếu local-part", "@example.test"),
    ("Thiếu domain", "qa@"), ("Có khoảng trắng giữa", "qa user@example.test"),
    ("Domain có hai dấu chấm liên tiếp", "qa@example..test")], start=4):
    validation_case("account", f"EM-TK-VAL-{i:02d}", "FR-VIII-15 E2/format; FR-VIII-22 Inputs#14", name,
                    "Form tạo tài khoản", f"email = {value}", "Từ chối, hiển thị lỗi định dạng email; không lưu.")
validation_case("account", "EM-TK-VAL-09", "TAI_KHOAN.email UNIQUE; FR-VIII-15 E2 ERR-TK-02 / srs-fr-10:737",
                "Email trùng tài khoản cùng vai trò", "Quản trị > Tài khoản > Thêm mới",
                "Email đã thuộc CB_A", "Từ chối với ERR-TK-02: \"Email '{email}' đã được sử dụng\".")
validation_case("account", "EM-TK-VAL-10", "TAI_KHOAN.email UNIQUE; FR-VIII-22 E3 ERR-REG-02",
                "Email trùng tài khoản khác vai trò", "Đăng ký DN",
                "Email đã thuộc TVV nhưng MST DN mới", "Từ chối với ERR-REG-02: \"Email đã được sử dụng\".")
validation_case("account", "EM-TK-VAL-13", "[NGOÀI SRS] §3.5 Security; email header injection",
                "Chống chèn header email", "Form tạo tài khoản",
                "diupt01+uat-em-tk-val-13@gmail.com\\r\\nBcc:diupt01+attacker@gmail.com", "Từ chối dữ liệu; tuyệt đối không sinh thư tới MB_ATTACKER.")

def account_flow(tcid, trace, title, actor, start, pre, data, steps, expected, source, tocc, negative="Mailbox khác vai trò; email cũ", oracle=""):
    add("account", tcid, trace, "Cấp/kích hoạt tài khoản", "P0", "Workflow", title, actor, start, pre, data, steps, expected,
        source, tocc, negative,
        oracle or "Kiểm tra TAI_KHOAN.trang_thai, role/link entity, token, email queue/SMTP message-id, AUDIT_LOG; chỉ một thư.",
        "Dùng fixture riêng; sau test khóa/vô hiệu hóa account nếu cần.")

account_flow("EM-TK-ACT-01", "FR-VIII-15 / SM-TAIKHOAN", "QTHT tạo tài khoản cán bộ và gửi mail kích hoạt", "QTHT", "Quản trị > Tài khoản > Thêm mới",
    "Username/email mới; đơn vị và vai trò tồn tại.", f"cb_email_01 / {tc_alias('EM-TK-ACT-01')}",
    "1. Dọn inbox; ghi count TAI_KHOAN/queue.\n2. Điền form, không có field mật khẩu.\n3. Bấm Lưu một lần.\n4. Mở inbox email mới.\n5. Kiểm tra UI/API/role/audit.",
    "1. Baseline sạch.\n2. Form hợp lệ, admin không biết/đặt mật khẩu.\n3. Tạo 1 TAI_KHOAN trạng thái CHO_KICH_HOAT và gán sẵn role/đơn vị.\n4. Nhận đúng 1 email có link đặt mật khẩu lần đầu.\n5. Có token/audit; chưa đăng nhập được trước kích hoạt.",
    "TAI_KHOAN.email", f"To: {tc_alias('EM-TK-ACT-01')}")
account_flow("EM-TK-ACT-02", "FR-IV-07 / FR-VIII-15 / srs-fr-04:598-636", "Duyệt TVV tự cấp TK và gửi mail kích hoạt", "CB Phê duyệt cùng đơn vị", "Hồ sơ TVV > Phê duyệt",
    "TVV ở CHO_PHE_DUYET, email mới, hồ sơ hợp lệ.", f"{tc_alias('EM-TK-ACT-02')}; số quyết định hợp lệ",
    "1. Dọn inbox/ghi baseline.\n2. Mở hồ sơ TVV chờ duyệt.\n3. Nhập số quyết định và phê duyệt.\n4. Kiểm tra inbox TVV.\n5. Kiểm tra TVV, TK, role, link và audit.",
    "1. Baseline sạch.\n2. Đúng hồ sơ/quyền.\n3. TVV và TK chuyển CHO_KICH_HOAT; tạo username từ local-part, role TVV/CG và đơn vị.\n4. Đúng 1 mail kích hoạt có mã số TVV/link.\n5. Liên kết 1:1 và audit đúng.",
    "TU_VAN_VIEN.email được copy sang TAI_KHOAN.email", f"To: {tc_alias('EM-TK-ACT-02')}")
account_flow("EM-TK-ACT-03", "FR-IV-NHT-01 / srs-fr-04:1214-1266", "Tạo NHT gửi mail kích hoạt", "QTHT/CB NV đúng đơn vị", "Quản lý Người hỗ trợ > Thêm mới",
    "Email/username mới; đơn vị và ≥1 lĩnh vực hợp lệ.", tc_alias("EM-TK-ACT-03"),
    "1. Dọn inbox/ghi baseline.\n2. Điền đủ form NHT.\n3. Lưu.\n4. Kiểm tra inbox.\n5. Kiểm tra NGUOI_HO_TRO, TAI_KHOAN, role và audit.",
    "1-2. Dữ liệu hợp lệ.\n3. Tạo đúng 1 NHT + 1 TK ở CHO_KICH_HOAT, gán role NHT.\n4. Nhận đúng 1 mail link đặt mật khẩu lần đầu.\n5. Entity liên kết, đơn vị/lĩnh vực đúng.",
    "NGUOI_HO_TRO/TAI_KHOAN.email", f"To: {tc_alias('EM-TK-ACT-03')}")
account_flow("EM-TK-ACT-04", "FR-VIII-22 Processing#10,#12", "DN tự đăng ký nhận link chỉ kích hoạt", "DN chưa có TK", "Đăng nhập > Đăng ký DN",
    "MST/email mới; toàn bộ field bắt buộc hợp lệ.", f"MST 0100000001; {tc_alias('EM-TK-ACT-04')}; mật khẩu Test@12345",
    "1. Dọn inbox/ghi baseline.\n2. Điền form và mật khẩu.\n3. Đăng ký.\n4. Mở email và bấm link.\n5. Quan sát trang sau link; đăng nhập bằng MST và mật khẩu đã đăng ký.",
    "1. Baseline sạch.\n2. Form hợp lệ.\n3. TK CHO_KICH_HOAT + DN được tạo, role DN gán sẵn.\n4. Link hợp lệ chuyển TK HOAT_DONG và bị hủy.\n5. Link KHÔNG hỏi đặt lại mật khẩu; đăng nhập bằng mật khẩu ban đầu thành công.",
    "TAI_KHOAN.email", f"To: {tc_alias('EM-TK-ACT-04')}")
account_flow("EM-TK-ACT-05", "FR-VIII-26 Processing#7-14", "TVV/NHT/CB kích hoạt lần đầu kèm đặt mật khẩu", "TVV/NHT/CB", "Link kích hoạt trong email",
    "TK CHO_KICH_HOAT chưa có mật khẩu; token hợp lệ chưa dùng.", "Mật khẩu mới Test@12345",
    "1. Bấm link trong mail.\n2. Kiểm tra form đặt mật khẩu.\n3. Nhập mật khẩu + xác nhận.\n4. Submit.\n5. Đăng nhập và kiểm tra entity liên quan.",
    "1. Link mở được.\n2. Có 2 field mật khẩu, không yêu cầu lại email.\n3-4. Mật khẩu đủ mạnh được hash; token bị hủy; TK HOAT_DONG.\n5. Đăng nhập được; TVV/NHT liên quan đồng thời HOAT_DONG.",
    "Link đã gửi tới TAI_KHOAN.email", "Không phát sinh email mới")
for tcid, trace, title, token, exp in [
    ("EM-TK-ACT-06", "FR-VIII-22 E8 ERR-REG-ACT-01", "Link kích hoạt DN sai/không tồn tại", "token sửa 1 ký tự", "Hiển thị nguyên văn: 'Liên kết kích hoạt không hợp lệ. Vui lòng kiểm tra lại thư điện tử hoặc liên hệ hỗ trợ.'; không đổi trạng thái."),
    ("EM-TK-ACT-07", "FR-VIII-22 E9 ERR-REG-ACT-02", "Dùng lại link kích hoạt DN", "token đã dùng", "Hiển thị nguyên văn: 'Liên kết kích hoạt đã được sử dụng. Tài khoản của bạn có thể đã kích hoạt — vui lòng đăng nhập.'; không thực hiện lần hai."),
    ("EM-TK-ACT-08", "FR-VIII-26 E4 ERR-PWD-04", "Dùng lại link đặt mật khẩu lần đầu", "reset token đã dùng", "Hiển thị 'Link đặt mật khẩu đã được sử dụng. Vui lòng yêu cầu link mới'; mật khẩu/trạng thái không đổi.")]:
    account_flow(tcid, trace, title, "User nhận mail", "URL token", "Có fixture đúng loại token.", token,
        "1. Ghi trạng thái/mật khẩu hash hiện tại.\n2. Mở URL chứa token theo Test Data.\n3. Thử submit nếu form xuất hiện.\n4. Kiểm tra UI và UI/API.",
        f"1. Có baseline.\n2-3. {exp}\n4. Không tạo session/token mới, không có audit kích hoạt thành công giả.",
        "Không áp dụng", "Không phát sinh mail")
account_flow("EM-TK-ACT-09", "SCR-VIII-03 srs-fr-10:1726 / FR-VIII-26 Processing#5 srs-fr-10:1322 / FR-VIII-22 token 1 lần srs-fr-10:1088 / TAI_KHOAN.token_reset_mk srs-v3.5:2121,2127 / BR-DATA-05", "Gửi lại email kích hoạt và kiểm link một lần dùng", "QTHT", "Quản trị > Tài khoản > CHO_KICH_HOAT",
    "TK CHO_KICH_HOAT đã có token/link cũ.", "Mailbox account; lưu URL cũ",
    "1. Lưu token/link cũ.\n2. Bấm Gửi lại email kích hoạt một lần.\n3. Nhận email mới và so sánh URL với link cũ.\n4. Mở link trong email mới để kích hoạt/đặt mật khẩu.\n5. Dùng lại chính link vừa dùng và kiểm tra UI/API.",
    "1. Có baseline.\n2-3. Nhận được thư kích hoạt. URL trong thư gửi lại trùng với link cũ là hành vi hợp lệ theo SRS hiện tại — ghi Actual link trùng hay khác, không Fail. [NGOÀI SRS] Số lượng thư, UI message, rate-limit và việc reuse hay thay token cũ chỉ ghi observation/BA clarification.\n4. Link trong thư thực hiện đúng luồng kích hoạt.\n5. Dùng lại cùng link bị từ chối vì token chỉ dùng một lần; hệ thống ghi nhật ký thao tác theo BR-DATA-05.",
    "TAI_KHOAN.email", "To: email TK", oracle="UI/API và Gmail; link trong thư hoạt động đúng luồng và bị từ chối khi dùng lại; audit thao tác nếu có quyền. Không bắt token mới khác token cũ, mã audit cụ thể hoặc số lượng thư vì SRS không đặc tả.")
account_flow("EM-TK-ACT-10", "BR-DATA/Concurrency; FR-VIII-15", "Double-click tạo tài khoản không tạo trùng/email trùng", "QTHT", "Form Thêm tài khoản",
    "Email/username mới; có thể gửi hai request gần đồng thời.", tc_alias("EM-TK-ACT-10"),
    "1. Dọn inbox/ghi baseline.\n2. Điền form hợp lệ.\n3. Double-click Lưu hoặc gửi 2 request đồng thời.\n4. Chờ queue.\n5. Kiểm tra UI/API/inbox/audit.",
    "1-2. Baseline/dữ liệu đúng.\n3. Hệ thống xử lý idempotent/unique.\n4-5. Chỉ 1 TK, 1 token hiệu lực, 1 email kích hoạt; request còn lại bị chặn, không 500/duplicate.",
    "TAI_KHOAN.email", f"To: {tc_alias('EM-TK-ACT-10')}")
account_flow("EM-TK-ACT-11", "FR-IV-07 W1 WRN-PD-01 / srs-fr-04:622-634", "SMTP lỗi khi duyệt TVV không rollback phê duyệt", "CB Phê duyệt", "Hồ sơ TVV > Phê duyệt",
    "SMTP giả lập lỗi; TVV CHO_PHE_DUYET hợp lệ.", "tvv.smtp.fail@example.invalid",
    "1. Cấu hình SMTP stub trả lỗi.\n2. Phê duyệt TVV.\n3. Quan sát UI.\n4. Kiểm tra TVV/TK.\n5. Kiểm tra queue/log/audit.",
    "1. Fault injection hoạt động.\n2. Quyết định duyệt vẫn commit.\n3. Hiển thị WRN-PD-01 nguyên văn theo SRS.\n4. TVV và TK vẫn CHO_KICH_HOAT.\n5. Mail ghi thất bại/retry; không tạo rollback hoặc TK thứ hai.",
    "TAI_KHOAN.email", "Không có SMTP accepted", negative="Mọi mailbox", oracle="TVV/TK CHO_KICH_HOAT; warning WRN-PD-01; failure log; retry; audit APPROVE vẫn tồn tại.")
account_flow("EM-TK-ACT-12", "SM-TVV CHO_KICH_HOAT→VO_HIEU_HOA / srs-fr-04:1597", "Vô hiệu hóa TVV làm link kích hoạt cũ vô tác dụng", "CB NV", "Chi tiết TVV CHO_KICH_HOAT > Cập nhật trạng thái",
    "TVV/TK CHO_KICH_HOAT; đã có link kích hoạt; lý do ≥10 ký tự.", "Lý do: Email nhập sai, không liên lạc được TVV",
    "1. Lưu link kích hoạt.\n2. Vô hiệu hóa khẩn cấp với lý do hợp lệ.\n3. Mở lại link cũ.\n4. Kiểm tra TVV/TK/audit.",
    "1. Có token cũ.\n2. TVV/TK bị vô hiệu hóa, token invalidated.\n3. Link cũ không thể kích hoạt/đặt mật khẩu.\n4. Audit đủ người, thời gian, lý do; thông báo CB PD theo SRS.",
    "Không áp dụng", "Thông báo CB PD nếu email channel áp dụng")

def pwd_case(tcid, trace, title, pre, data, expected, source="TAI_KHOAN.email", status="Not Run", note=""):
    add("account", tcid, trace, "Quên mật khẩu / Claim", "P0", "Workflow/Negative", title, "User bất kỳ", "Đăng nhập > Quên mật khẩu", pre, data,
        "1. Dọn inbox và ghi baseline TK/token/queue.\n2. Mở Quên mật khẩu.\n3. Nhập Tên đăng nhập theo Test Data, bấm gửi.\n4. Kiểm tra UI và inbox.\n5. Nếu có link: mở link, thao tác theo case.\n6. Kiểm tra UI/API/token/audit và thử đăng nhập khi cần.",
        expected, source, "To: email theo nguồn đã nêu nếu hợp lệ", "Email cũ/email DN khác/user khác",
        "Kiểm tra lookup đúng nhánh; token_reset_mk/token_het_han; queue/SMTP; password hash; trạng thái; AUDIT_LOG PASSWORD_RESET/ACCOUNT_ACTIVATE/DN_CLAIM.",
        "Thu hồi token còn sống; reset fixture về mật khẩu chuẩn.", status=status, note=note)

pwd_case("EM-TK-PWD-01", "FR-VIII-26 3b,4a,5-16", "Reset bằng email cho TK HOAT_DONG",
         "TK HOAT_DONG có email hợp lệ.", f"{tc_alias('EM-TK-PWD-01')}; mật khẩu mới New@Test123",
         "1-3. UI trả thông báo gửi link.\n4. Đúng 1 mail tới TAI_KHOAN.email.\n5. Link trong 30 phút mở form; mật khẩu mạnh submit thành công.\n6. Token bị hủy, TK vẫn HOAT_DONG, mật khẩu cũ thất bại và mật khẩu mới đăng nhập được.")
pwd_case("EM-TK-PWD-02", "FR-VIII-26 3a,4a; AC MST đã có TK", "Reset DN bằng MST đã có tài khoản",
         "DN có TK liên kết; TAI_KHOAN.email khác DOANH_NGHIEP.email.", f"MST 0100000010; TK={tc_alias('EM-TK-PWD-02', 'tk')}; DN={tc_alias('EM-TK-PWD-02', 'dn')}",
         f"1-3. Lookup theo username=MST.\n4. Mail chỉ tới {tc_alias('EM-TK-PWD-02', 'tk')}, không tới {tc_alias('EM-TK-PWD-02', 'dn')}.\n5-6. Token 30 phút; reset thành công, không tạo TK/DN mới.")
pwd_case("EM-TK-PWD-03", "FR-VIII-26 E1 ERR-PWD-01", "Email không tồn tại chống enumeration",
         "Email không có trong TAI_KHOAN.", "unknown.email@example.test",
         "1-3. Hiển thị đúng câu trung tính: 'Nếu tên đăng nhập đã đăng ký, link đặt mật khẩu sẽ được gửi đến hộp thư của bạn'.\n4. Không có email.\n5-6. Không tạo token/TK/queue/audit reset thành công.")
pwd_case("EM-TK-PWD-04", "FR-VIII-26 E1 ERR-PWD-01", "MST không tồn tại chống enumeration",
         "MST không có cả TAI_KHOAN và DOANH_NGHIEP.", "MST 0199999999",
         "Kết quả UI phải giống case email không tồn tại; không tạo TK/token/email; không tiết lộ MST tồn tại hay không.")
pwd_case("EM-TK-PWD-05", "FR-VIII-26 E1a ERR-PWD-FORMAT", "Tên đăng nhập sai định dạng",
         "Không có.", "abc-123",
         "UI hiển thị nguyên văn 'Tên đăng nhập phải là email hợp lệ hoặc Mã số thuế 10 chữ số'; không lookup/queue/email.")
pwd_case("EM-TK-PWD-06", "FR-VIII-26 E2 ERR-PWD-02", "Tài khoản TAM_KHOA không được reset",
         "TK TAM_KHOA.", "locked.user@example.test",
         "Hiển thị 'Tài khoản đã bị khóa hoặc vô hiệu hóa. Liên hệ quản trị viên để được hỗ trợ'; không sinh token/mail.")
pwd_case("EM-TK-PWD-07", "FR-VIII-26 E2 ERR-PWD-02", "Tài khoản VO_HIEU_HOA không được reset",
         "TK VO_HIEU_HOA.", "disabled.user@example.test",
         "Cùng ERR-PWD-02; không sinh token/mail và không đổi trạng thái.")
pwd_case("EM-TK-PWD-08", "FR-VIII-26 E3 ERR-PWD-03", "Token reset HOAT_DONG quá 30 phút",
         "Có token reset tạo >30 phút.", "URL token hết hạn; mật khẩu New@Test123",
         "Mở/submit link hiển thị 'Link đặt mật khẩu đã hết hạn. Vui lòng yêu cầu link mới'; hash và trạng thái không đổi; token không dùng được.")
pwd_case("EM-TK-PWD-09", "FR-VIII-26 E4 ERR-PWD-04", "Token reset đã sử dụng",
         "Token đã dùng thành công một lần.", "URL token đã dùng",
         "Hiển thị 'Link đặt mật khẩu đã được sử dụng. Vui lòng yêu cầu link mới'; không đổi lại mật khẩu.")
pwd_case("EM-TK-PWD-10", "FR-VIII-26 E5 ERR-PWD-05", "Mật khẩu mới yếu",
         "Token còn hiệu lực.", "password = 12345678",
         "Hiển thị 'Mật khẩu chưa đủ mạnh'; hash/trạng thái không đổi. Token không được tiêu thụ để user có thể sửa và submit lại.")
pwd_case("EM-TK-PWD-11", "FR-VIII-26 E6 ERR-PWD-06", "Xác nhận mật khẩu không khớp",
         "Token còn hiệu lực.", "New@Test123 / Different@Test123",
         "Hiển thị 'Mật khẩu xác nhận không khớp'; không đổi hash/trạng thái; token chưa dùng.")
for tcid, title, data, exp in [
    ("EM-TK-CHG-01", "Đổi email tài khoản độc lập email DN", "TK old=MB_TK_OLD; DN=MB_DN_CONTACT; new=MB_TK_NEW", "TAI_KHOAN.email=new; DOANH_NGHIEP.email giữ nguyên; không OTP/duyệt."),
    ("EM-TK-CHG-02", "Đổi sang email tài khoản đã tồn tại", "new=MB_TK_CURRENT đã thuộc TK khác", "Từ chối unique; cả hai email cũ giữ nguyên."),
    ("EM-TK-CHG-03", "Đổi sang email sai format", "new=invalid-email", "Từ chối format; UI/API không đổi."),
    ("EM-TK-CHG-04", "Notification sau đổi gửi email tài khoản mới", "old/new + trigger workflow", "Chỉ email mới nhận notification; email DN và email cũ không nhận."),
    ("EM-TK-CHG-05", "Reset sau đổi gửi email tài khoản mới", "old/new + Quên mật khẩu", "Chỉ email mới nhận link reset."),
    ("EM-TK-CHG-06", "Audit thay đổi email tài khoản", "old/new", "Nhật ký hiển thị đúng actor, thời gian, entity/mã bản ghi, loại Sửa và JSON diff email old→new; read-only.")]:
    trace_ref = "FR-VIII-15 / SCR-VIII-03 / BR-AUTH-EMAIL-01"
    if tcid == "EM-TK-CHG-05":
        trace_ref += " / FR-VIII-26 srs-fr-10:1313-1323,1339"
    elif tcid == "EM-TK-CHG-06":
        trace_ref += " / FR-VIII-28 / SCR-VIII-10 srs-fr-10:1370-1428,1969-1990"
    steps = (
        "1. QTHT mở form Sửa tài khoản; ghi email cũ và email DN.\n2. Đổi sang email mới và lưu; reload xác nhận.\n3. Mở Quên mật khẩu, nhập email mới và gửi yêu cầu; ghi mốc thời gian.\n4. Kiểm Gmail: email mới nhận đúng một link reset, email cũ không nhận.\n5. Gửi lại yêu cầu bằng email cũ; kiểm thông báo trung tính ERR-PWD-01 và không mailbox nào nhận thêm thư."
        if tcid == "EM-TK-CHG-05" else
        "1. QTHT mở form Sửa tài khoản.\n2. Ghi email TK và DN trước test.\n3. Sửa Email theo Test Data và lưu.\n4. Reload và phát sinh notification/reset nếu case yêu cầu.\n5. Kiểm tra UI/API/inbox; với CHG-06 mở Nhật ký hệ thống, lọc thao tác Sửa của đúng QTHT/entity rồi expand Chi tiết thay đổi."
    )
    add("account", tcid, trace_ref, "Đổi email tài khoản", "P1", "Workflow/Negative", title,
        "QTHT", "Quản trị hệ thống > Tài khoản > Sửa",
        "Có TK và dữ liệu theo Test Data.", data,
        steps,
        f"1. Form Sửa có trường Email theo SCR-VIII-03.\n2-5. {exp}",
        "TAI_KHOAN.email", "Email mới khi action thành công", "Email cũ và DOANH_NGHIEP.email trừ khi trùng giá trị",
        "UI/API; TAI_KHOAN.email; DOANH_NGHIEP.email; Gmail; CHG-06 kiểm trên màn Nhật ký hệ thống.",
        status="Not Run")

for num, title, data, expected, status in [
    (1, "Bắt buộc yếu tố thứ hai sau username/password đúng", "CB nội bộ HOAT_DONG", "Hệ thống PHẢI yêu cầu yếu tố thứ hai trước khi cấp session/JWT; đăng nhập thẳng sau bước mật khẩu là Fail. Ghi kênh nhận mã thực tế làm bằng chứng nhưng không chấm đúng/sai kênh — chờ BA tại GAP-EMAIL-01.", "Not Run"),
    (2, "Mã 2FA đúng", "Mã 6 số hợp lệ", "Chỉ tạo session khi mã đúng và còn hạn.", "Not Run"),
    (3, "Mã 2FA sai", "000000", "ERR-DN-08; không tạo session.", "Not Run"),
    (4, "Mã 2FA hết hạn", "mã cũ", "ERR-DN-08; không tạo session.", "Not Run"),
    (5, "Gửi lại/rate-limit mã email 2FA", "bấm gửi lại liên tục", "[NGOÀI SRS] SRS không đặc tả gửi lại, rate-limit hoặc TTL cụ thể của mã 2FA. Ghi observation và escalate chủ sở hữu bảo mật; không log bug sai spec, không tự chấm N/A.", "Not Run")]:
    trace_2fa = "BR-AUTH-01 canonical srs-v3.5:5582,5596 vs FR-VIII-20 srs-fr-10:901-974"
    if num == 5:
        trace_2fa = "[NGOÀI SRS] " + trace_2fa + "; resend/rate-limit/TTL chưa đặc tả"
    tail_2fa = ("Với case 02-04 chỉ chấm hành vi mã/session, không chấm kênh nhận mã; ghi bằng chứng kênh triển khai thực tế."
                if num in {2, 3, 4} else "Ghi Actual, kênh triển khai và bằng chứng session/mailbox theo phạm vi case.")
    add("account", f"EM-TK-2FA-{num:02d}", trace_2fa, "Đăng nhập 2FA", "P0", "Security", title,
        "Cán bộ nội bộ", "Màn đăng nhập Tier 1", "Tài khoản nội bộ HOAT_DONG; username/password đúng.", data,
        "1. Dọn mailbox/chuẩn bị authenticator.\n2. Nhập username/password đúng.\n3. Quan sát nguồn nhận mã.\n4. Nhập mã theo Test Data.\n5. Kiểm tra session, login audit và mailbox.",
        f"1-2. Qua bước mật khẩu.\n3. {expected}\n4-5. {tail_2fa}",
        "Kênh triển khai thực tế; chờ BA chốt email hay authenticator", "Ghi Actual", "User khác",
        "Session/JWT chỉ sinh sau 2FA; LOGIN audit; OTP/token không lộ log.", status=status,
        note="BR-AUTH-01 canonical yêu cầu email nhưng FR-VIII-20 vẫn ghi ứng dụng xác thực; build thiếu hoàn toàn yếu tố thứ hai là Fail nếu chưa có BA de-scope bằng văn bản.")

# ---------------------------------------------------------------------------
# 02. DOANH NGHIỆP
# ---------------------------------------------------------------------------
ui_case("enterprise", "EM-DN-UI-01", "FR-V.III-NEW-03 / SCR-V.III-03 / srs-fr-07:274-327,544-601",
        "Kiểm tra email trên form CB tạo DN", "CB NV", "Doanh nghiệp > Thêm mới",
        "Email doanh nghiệp là tùy chọn, input type email; chỉ MST + tên DN bắt buộc; không có password/username",
        "nút gửi mail kích hoạt; field trạng thái tài khoản")
ui_case("enterprise", "EM-DN-UI-02", "FR-V.III-02 / SCR-V.III-02 / srs-fr-07:344-404,529",
        "Kiểm tra email trên form DN cập nhật hồ sơ", "DN đăng nhập", "Hồ sơ doanh nghiệp > Cập nhật",
        "Email liên hệ là field tự cập nhật, tùy chọn, validate format; không OTP")
ui_case("enterprise", "EM-DN-UI-03", "FR-VIII-22 / SCR-VIII-08", "Phân biệt một ô email khi DN tự đăng ký", "DN chưa có TK",
        "Đăng nhập > Đăng ký DN", "một ô email bắt buộc; không có hai field 'Email tài khoản'/'Email liên hệ'; tooltip giải thích đồng bộ ban đầu")

validation_case("enterprise", "EM-DN-VAL-01", "FR-V.III-NEW-03; DOANH_NGHIEP.email N", "CB tạo DN để trống email", "Doanh nghiệp > Thêm mới", "MST/tên hợp lệ; email rỗng", "Cho tạo DOANH_NGHIEP; không tạo TK/mail.", actor="CB NV")
validation_case("enterprise", "EM-DN-VAL-02", "FR-V.III-NEW-03 Inputs email", "CB tạo DN với email hợp lệ", "Doanh nghiệp > Thêm mới", tc_alias("EM-DN-VAL-02"), "Lưu vào DOANH_NGHIEP.email; không gửi mail.", actor="CB NV")
validation_case("enterprise", "EM-DN-VAL-03", "FR-V.III-NEW-03 Inputs email", "CB tạo DN với email sai format", "Doanh nghiệp > Thêm mới", "dn-contact.example.test", "Từ chối format; không tạo DN/TK/mail.", actor="CB NV")
validation_case("enterprise", "EM-DN-VAL-04", "BR-AUTH-EMAIL-01", "Hai DN dùng chung email liên hệ", "Doanh nghiệp > Thêm mới", "Email đã ở DOANH_NGHIEP A, dùng cho DN B", "Cho phép; DOANH_NGHIEP.email không UNIQUE.", actor="CB NV")
validation_case("enterprise", "EM-DN-VAL-05", "BR-AUTH-EMAIL-01", "Email DN trùng email tài khoản người khác khi CB tạo", "Doanh nghiệp > Thêm mới", "Email đã ở TAI_KHOAN của TVV", "Cho phép vì đây là DOANH_NGHIEP.email và luồng không tạo TK.", actor="CB NV")

for tcid, title, data, exp in [
    ("EM-DN-UPD-01", "Đổi email liên hệ DN không đổi email tài khoản", "TK=MB_TK_CURRENT; DN old=MB_DN_CONTACT → new=diupt01+uat-em-dn-upd-01-new@gmail.com", "DOANH_NGHIEP.email=new; TAI_KHOAN.email vẫn là MB_TK_CURRENT; không OTP."),
    ("EM-DN-UPD-02", "Đổi email DN thành giá trị đang được DN khác dùng", "new=diupt01+uat-em-dn-upd-02-shared@gmail.com", "Cho phép; cả hai DN dùng chung email."),
    ("EM-DN-UPD-03", "Xóa email liên hệ tùy chọn", "new=rỗng", "Cho lưu nếu các field bắt buộc khác còn hợp lệ; TK email không đổi."),
    ("EM-DN-UPD-04", "Email DN sai format khi cập nhật", "new=bad-email", "Từ chối; old email giữ nguyên; không mail/OTP.")]:
    add("enterprise", tcid, "FR-V.III-02 / BR-AUTH-EMAIL-01", "Cập nhật email liên hệ DN", "P0", "Workflow/Negative", title,
        "DN hoặc CB NV đúng quyền", "Chi tiết DN > Chỉnh sửa", "Có DN/TK theo Test Data; ghi giá trị trước test.", data,
        "1. Ghi email TK/DN trước test.\n2. Mở form chỉnh sửa.\n3. Đổi email theo Test Data.\n4. Lưu và reload.\n5. Kiểm tra UI/API, inbox và audit.",
        f"1-4. {exp}\n5. Không sinh OTP/email kích hoạt; audit update nếu SRS/framework yêu cầu.",
        "DOANH_NGHIEP.email", "Không gửi mail do thao tác đổi", "Tất cả mailbox",
        "DOANH_NGHIEP.email; TAI_KHOAN.email không bị side-effect; queue +0; audit diff.")

no_mail_case("EM-DN-NOMAIL-01", "FR-V.III-NEW-03 / srs-fr-07:277-327", "CB NV chủ động tạo DN", "Doanh nghiệp > Thêm mới", "CB NV", f"MST 0100000101; tên DN; email {tc_alias('EM-DN-NOMAIL-01')}")
no_mail_case("EM-DN-NOMAIL-02", "FR-V.I-04 / srs-fr-05:317-329", "Tạo DN từ modal khi lập vụ việc", "Vụ việc > Tạo mới > MST chưa có > Tạo DN", "CB NV", f"MST 0100000102; tên DN; email {tc_alias('EM-DN-NOMAIL-02')}")
no_mail_case("EM-DN-NOMAIL-03", "FR-V.II-01 / srs-fr-06:115-116", "Tiếp nhận DN từ DVC/LGSP trong hồ sơ chi trả", "API LGSP nhận Mẫu 01", "Hệ thống TTHC BTP", f"Payload hợp lệ có MST/tên/email {tc_alias('EM-DN-NOMAIL-03')}")
no_mail_case("EM-DN-NOMAIL-04", "FR-X.1-03 / srs-fr-12:469-512", "Tiếp nhận DN từ Cổng PLQG cho TVCS", "API inbound TVCS", "Cổng PLQG", f"Payload hợp lệ có MST/tên/email {tc_alias('EM-DN-NOMAIL-04')}")
no_mail_case("EM-DN-NOMAIL-05", "FR-X.1-05 / srs-fr-12:748-782", "Tiếp nhận DN từ Cổng PLQG cho hồ sơ pháp lý", "API inbound hồ sơ pháp lý", "Cổng PLQG", f"Payload hợp lệ có MST/tên/email {tc_alias('EM-DN-NOMAIL-05')}")

def dn_reg_case(tcid, trace, title, pre, data, expected, source="TAI_KHOAN.email"):
    add("enterprise", tcid, trace, "DN tự đăng ký", "P0", "Workflow/Negative", title, "DN chưa có TK", "Đăng nhập > Đăng ký DN",
        pre, data,
        "1. Dọn inbox/ghi count UI/API, bridge, token, queue.\n2. Mở form đăng ký.\n3. Nhập dữ liệu theo Test Data và submit.\n4. Kiểm tra UI, UI/API và inbox.\n5. Nếu có link, mở và đăng nhập.\n6. Kiểm tra audit và mailbox âm.",
        expected, source, "To: email đăng ký nếu thành công", "Email của tài khoản khác; email DN fixture khác",
        "TAI_KHOAN/DOANH_NGHIEP liên kết qua MST; 2 email; role DN; token; queue; SMTP; AUDIT_LOG SELF_REGISTER_DN.",
        "Dùng MST/email riêng mỗi case; vô hiệu hóa fixture sau test.")

dn_reg_case("EM-DN-REG-01", "FR-VIII-22 Processing#7-12 / BR-AUTH-EMAIL-01", "Đăng ký thành công đồng bộ một email vào hai bảng",
            "MST/email chưa tồn tại; field bắt buộc hợp lệ.", f"MST 0100000201; {tc_alias('EM-DN-REG-01')} (gán cùng giá trị cho TK và DN)",
            "1-3. Submit thành công.\n4. Tạo 1 TK CHO_KICH_HOAT và 1 DN; TAI_KHOAN.email = DOANH_NGHIEP.email = input; một mail kích hoạt.\n5. Link kích hoạt một lần, không hỏi lại mật khẩu; đăng nhập bằng MST.\n6. Role/audit đúng.")
dn_reg_case("EM-DN-REG-02", "FR-VIII-22 E3 ERR-REG-02", "Đăng ký với email đã tồn tại trong TAI_KHOAN",
            "MST mới; email đã thuộc tài khoản khác.", "MST 0100000202; MB_TK_CURRENT đã thuộc tài khoản khác",
            "Submit bị từ chối với 'Email đã được sử dụng'; không tạo TK/DN/bridge/token/email.")
dn_reg_case("EM-DN-REG-03", "BR-AUTH-EMAIL-01", "Email đang dùng ở DOANH_NGHIEP nhưng chưa có trong TAI_KHOAN",
            "Email shared chỉ tồn tại ở DOANH_NGHIEP; MST mới.", f"MST 0100000203; {tc_alias('EM-DN-REG-03')} đã có ở DOANH_NGHIEP nhưng chưa có ở TAI_KHOAN",
            "Không được từ chối chỉ vì trùng DOANH_NGHIEP.email; đăng ký thành công nếu TAI_KHOAN.email chưa có; sau đó TAI_KHOAN.email unique được tạo.")
dn_reg_case("EM-DN-REG-04", "FR-VIII-22 E2 ERR-REG-MST-EXIST", "MST đã có hồ sơ doanh nghiệp",
            "DOANH_NGHIEP đã có MST, chưa có hoặc đã có TK.", "MST hiện hữu; email mới",
            "Hiển thị nguyên văn ERR-REG-MST-EXIST và nút Quên mật khẩu; không tạo DN/TK/mail mới; nút dẫn FR-VIII-26.")
dn_reg_case("EM-DN-REG-05", "FR-VIII-22 E8 ERR-REG-ACT-01", "Link kích hoạt DN bị sửa",
            "DN đăng ký thành công, TK CHO_KICH_HOAT.", "URL token sửa một ký tự",
            "Link báo không hợp lệ nguyên văn; TK vẫn CHO_KICH_HOAT; mật khẩu/token hợp lệ ban đầu không bị thay đổi.")
dn_reg_case("EM-DN-REG-06", "FR-VIII-22 E9 ERR-REG-ACT-02", "Link kích hoạt DN dùng lần hai",
            "Link đã kích hoạt thành công.", "Dùng lại cùng URL",
            "Báo link đã sử dụng nguyên văn; không tạo thêm audit/session/role; TK vẫn HOAT_DONG.")

def claim_case(tcid, trace, title, pre, data, expected, source="DOANH_NGHIEP.email"):
    add("enterprise", tcid, trace, "DN Claim Flow", "P0", "Workflow/Negative/Concurrency", title, "DN", "Đăng nhập > Quên mật khẩu",
        pre, data,
        "1. Dọn inbox; ghi count DN/TK/token/queue và liên kết hiện tại.\n2. Nhập MST vào một ô Tên đăng nhập.\n3. Bấm gửi link.\n4. Kiểm tra UI, UI/API và inbox.\n5. Mở link, đặt mật khẩu nếu nhận được.\n6. Đăng nhập và kiểm tra hồ sơ/quyền/audit.",
        expected, source, "To: DOANH_NGHIEP.email cho claim mới; TAI_KHOAN.email nếu TK đã có",
        "Email DN/TK khác; email cũ sau khi đã cập nhật", "TAI_KHOAN count/link DN/role DN; token vĩnh viễn một lần cho CHO_KICH_HOAT; queue/SMTP; AUDIT_LOG DN_CLAIM.",
        "Thu hồi token; vô hiệu hóa TK claim fixture nếu cần.")

claim_case("EM-DN-CLAIM-01", "FR-VIII-26 4b-16", "MST có DN chưa có TK và email hợp lệ",
           "DN tồn tại, chưa có TK, DOANH_NGHIEP.email hợp lệ.", f"MST 0100000301; {tc_alias('EM-DN-CLAIM-01')}",
           "1-3. Hệ thống tạo đúng 1 TK username=MST, email=DOANH_NGHIEP.email, CHO_KICH_HOAT, role DN và link DN cũ.\n4. Một mail tới email DN.\n5. Token vĩnh viễn một lần; đặt mật khẩu làm TK HOAT_DONG.\n6. Đăng nhập thấy đúng hồ sơ DN cũ, không tạo DN mới.")
claim_case("EM-DN-CLAIM-02", "FR-VIII-26 AC MST đã có TK", "MST có DN và đã có TK",
           "DN/TK đã liên kết; hai email khác nhau.", f"MST 0100000302; TK={tc_alias('EM-DN-CLAIM-02', 'tk')}; DN={tc_alias('EM-DN-CLAIM-02', 'dn')}",
           f"Không tạo TK/DN mới; xử lý reset thường; token hạn 30 phút; chỉ {tc_alias('EM-DN-CLAIM-02', 'tk')} nhận mail.", source="TAI_KHOAN.email")
claim_case("EM-DN-CLAIM-03", "FR-VIII-26 Processing#4b srs-fr-10:1320 / TAI_KHOAN.email bắt buộc+UNIQUE srs-v3.5:2110 / DOANH_NGHIEP.email tùy chọn srs-v3.5:1703 / ERR-PWD-01 srs-fr-10:1340", "DOANH_NGHIEP.email trống",
           "DN có MST, chưa TK, email NULL.", "MST 0100000303",
           "Không được tạo TAI_KHOAN với email trống, không cấp quyền truy cập và không gửi SMTP mail. Nếu có phản hồi UI thì không được làm lộ thông tin ngoài thông báo trung tính; câu chữ cụ thể chưa được SRS đặc tả nên ghi Actual/BA clarification, không tự log bug wording.")
claim_case("EM-DN-CLAIM-04", "FR-VIII-26 E7-NEW", "Email DN bounce/không khả dụng",
           "DN chưa TK; SMTP chấp nhận rồi bounce hoặc stub trả lỗi.", "MST 0100000304; bounce@example.invalid",
           "UI không hiển thị mã nội bộ ERR-PWD-DN-NO-MAIL; ghi mail failure/audit; DN không được active. Hỗ trợ phải cập nhật email rồi DN thực hiện lại.")
claim_case("EM-DN-CLAIM-05", "FR-VIII-26 fallback AC", "Cập nhật email DN rồi chạy lại Claim",
           "Claim trước thất bại; CB đã xác minh CNĐKKD và cập nhật email DN.", f"MST 0100000305; old=bad; new={tc_alias('EM-DN-CLAIM-05', 'new')}",
           "Lần mới gửi chỉ tới email mới; không tạo TK thứ hai; link mới đặt mật khẩu được; email cũ không nhận.")
claim_case("EM-DN-CLAIM-06", "FR-VIII-26 / Concurrency", "Hai yêu cầu Claim đồng thời",
           "DN tồn tại chưa có TK; hai request MST cùng lúc.", "MST 0100000306",
           "Chỉ một TAI_KHOAN liên kết DN và một role DN; không duplicate key/500. Chính sách số mail/token phải nhất quán; chỉ token được coi hiệu lực theo quy tắc hệ thống.")

# ---------------------------------------------------------------------------
# 03. NOTIFICATION WORKFLOW
# ---------------------------------------------------------------------------
workflow_case("EM-NOT-HDD-01", "FR-II-05 / srs-fr-02:510", "Hỏi đáp", "Phân công hỏi đáp", "CB NV có quyền", "Chi tiết hỏi đáp > Phân công",
              "Hỏi đáp TIEP_NHAN; người xử lý hợp lệ.", "Mã HĐ; người được phân công", "Hỏi đáp → DANG_XU_LY, người xử lý được set",
              "TAI_KHOAN.email người được phân công", "To: người được phân công", "CB khác/đơn vị khác/người gửi", "email chứa mã/nội dung phân công và link hồ sơ")
workflow_case("EM-NOT-HDD-02", "BR-NOTIF-01 trigger trình duyệt; srs-fr-02:1175", "Hỏi đáp", "Gửi phản hồi để trình phê duyệt", "CB NV xử lý", "Chi tiết hỏi đáp > Gửi phản hồi + Đã trả lời",
              "Hỏi đáp DANG_XU_LY; phản hồi hợp lệ.", "CB PD cùng đơn vị", "Hỏi đáp → CHO_PHE_DUYET",
              "TAI_KHOAN.email CB PD cùng đơn vị", "To: CB PD cùng đơn vị", "CB PD khác đơn vị/cấp không phù hợp", "email nêu hồ sơ chờ duyệt; ≤5 phút")
workflow_case("EM-NOT-HDD-03", "FR-II-08 / srs-fr-02:686,1118,1177", "Hỏi đáp", "CB PD từ chối phản hồi kèm lý do", "CB PD cùng đơn vị", "Chi tiết hỏi đáp CHO_PHE_DUYET > Từ chối",
              "Có lý do 10-1000 ký tự.", "Lý do: Nội dung cần bổ sung căn cứ pháp lý", "Hỏi đáp → DANG_XU_LY",
              "TAI_KHOAN.email CB NV soạn phản hồi", "To: CB NV soạn", "Người được phân công khác/CB PD khác", "email có nguyên văn lý do từ chối")
workflow_case("EM-NOT-HDD-04", "srs-fr-02:1181", "Hỏi đáp", "Auto-escalate hỏi đáp chờ duyệt quá 3 ngày làm việc", "Scheduled job", "Job auto-escalate",
              "Hỏi đáp CHO_PHE_DUYET >3 ngày LV; chưa escalate.", "Fixture clock/ngày lễ", "Giữ/đánh dấu escalation đúng SRS; tạo cảnh báo",
              "TAI_KHOAN.email CB PD Bộ/ngành hiện tại và CB_PD_TW thuộc DON_VI.don_vi_cha_id", "To: cbpd_bn_01 nhận nhắc nhở; escalation tới ít nhất 1 CB_PD_TW đúng đơn vị cha", "CB PD của Bộ/ngành/Địa phương khác; tài khoản TW không có role CB_PD_TW", "email thể hiện quá hạn phê duyệt")
for n, (level, recipient) in enumerate([("SAP_HET_HAN", "CB NV xử lý"), ("QUA_HAN", "CB NV + CB PD quản lý"), ("QUA_HAN_NGHIEM_TRONG", "CB NV + CB PD + cấp trên")], start=5):
    severe = level == "QUA_HAN_NGHIEM_TRONG"
    workflow_case(f"EM-NOT-HDD-{n:02d}", "FR-II-CROSS-01 / BR-SLA-03", "Hỏi đáp", f"Cảnh báo SLA hỏi đáp mức {level}", "Scheduled job", "Job SLA hỏi đáp",
                  f"Hỏi đáp chuyển mới sang {level}; cấu hình email bật.", "Clock tại đúng ngưỡng", f"Mức SLA → {level}",
                  "TAI_KHOAN.email cbnv_bn_01 + cbpd_bn_01 + CB_PD_TW đúng đơn vị cha" if severe else "TAI_KHOAN.email theo mức",
                  "To: cbnv_bn_01 + cbpd_bn_01 + ít nhất 1 CB_PD_TW đúng đơn vị cha" if severe else f"To: {recipient}",
                  "CB NV/CB PD thuộc đơn vị khác; tài khoản TW không có role CB_PD_TW" if severe else "Người ngoài ma trận nhận",
                  "email đúng mức, deadline và hồ sơ; không gửi lặp nếu không chuyển mức")

training_events = [
    ("EM-NOT-DT-01", "srs-fr-03:195", "Trình phê duyệt chương trình/kế hoạch", "CB NV", "Bản ghi hợp lệ chưa trình", "Bản ghi → CHO_DUYET", "CB PD cùng đơn vị", "email báo chờ duyệt", "TAI_KHOAN.email CB PD"),
    ("EM-NOT-DT-02", "srs-fr-03:205", "Phê duyệt chương trình/kế hoạch", "CB PD", "Bản ghi CHO_DUYET", "Bản ghi → DA_DUYET", "Người tạo", "email báo kết quả duyệt", "TAI_KHOAN.email người tạo"),
    ("EM-NOT-DT-03", "srs-fr-03:216", "Từ chối chương trình/kế hoạch", "CB PD", "Bản ghi CHO_DUYET; lý do hợp lệ", "Bản ghi → TU_CHOI", "Người tạo", "email có lý do từ chối", "TAI_KHOAN.email người tạo"),
    ("EM-NOT-DT-04", "srs-fr-03:227", "Gửi phê duyệt lại sau từ chối", "CB NV", "Bản ghi TU_CHOI đã sửa", "Bản ghi → CHO_DUYET", "CB PD cùng đơn vị", "email phân biệt resubmit", "TAI_KHOAN.email CB PD"),
    ("EM-NOT-DT-05", "srs-fr-03:237", "Trình duyệt khóa học", "CB NV", "Khóa hợp lệ", "Khóa → CHO_DUYET", "CB PD cùng đơn vị", "email báo khóa chờ duyệt", "TAI_KHOAN.email CB PD"),
    ("EM-NOT-DT-06", "srs-fr-03:248", "Từ chối khóa học về dự thảo", "CB PD", "Khóa CHO_DUYET; lý do hợp lệ", "Khóa → DU_THAO", "Người tạo", "email có lý do", "TAI_KHOAN.email người tạo"),
    ("EM-NOT-DT-07", "FR-III-04 EC-02 / srs-fr-03:513 vs BR-NOTIF-01(5)", "Hủy khóa có học viên đăng ký", "CB NV/CB PD", "Khóa có ít nhất 1 đăng ký DA_DUYET và 1 đăng ký CHO_DUYET/TU_CHOI để phân biệt recipient", "Khóa → DA_HUY; đăng ký liên quan → DA_HUY", "Tất cả học viên có đăng ký DA_DUYET", "email từng học viên đã duyệt có lý do hủy; đăng ký chưa duyệt không nhận trong khi chờ BA chốt mâu thuẫn", "HOC_VIEN.email; in-app theo HOC_VIEN.tai_khoan_id khi có"),
    ("EM-NOT-DT-08", "BR-NOTIF-01(6) / srs-v3.5:5721,5952", "Khóa bắt đầu diễn ra", "Scheduled/System hoặc CB NV", "Khóa DA_CONG_KHAI đến ngày bắt đầu; có lịch + GV + đăng ký", "Khóa → DANG_DIEN_RA", "HOC_VIEN + GIANG_VIEN của khóa", "email thông tin bắt đầu khóa", "HOC_VIEN.email + GIANG_VIEN.email"),
    ("EM-NOT-DT-09", "FR-III-03 / srs-fr-03:410-425", "Duyệt đăng ký học", "CB NV", "Đăng ký chờ duyệt", "Đăng ký → DA_DUYET", "TK DN/NHT đăng ký", "email kết quả duyệt", "DANG_KY_DAO_TAO.nguoi_dang_ky_id → TAI_KHOAN.email"),
    ("EM-NOT-DT-10", "FR-III-03 / srs-fr-03:410-425", "Từ chối đăng ký học", "CB NV", "Đăng ký chờ duyệt; có lý do", "Đăng ký → TU_CHOI", "TK DN/NHT đăng ký", "email có lý do từ chối", "DANG_KY_DAO_TAO.nguoi_dang_ky_id → TAI_KHOAN.email"),
    ("EM-NOT-DT-11", "FR-III-19 / srs-fr-03:1434", "Công bố kết quả đào tạo", "CB NV/System", "KQ đã duyệt", "Kết quả được công bố", "TK DN/NHT đã đăng ký học viên", "email 'KQ đào tạo đã có'", "DANG_KY_DAO_TAO.nguoi_dang_ky_id → TAI_KHOAN.email")]
for tcid, trace_ref, title, actor, pre, state, recipient, content, recipient_source in training_events:
    workflow_case(tcid, trace_ref, "Đào tạo", title, actor, "Module Đào tạo > hồ sơ tương ứng",
                  pre, "Dùng đăng ký do TK 0109998887 hoặc nht_qa_tw tạo; mailbox từng TK tách biệt", state, recipient_source, f"To: {recipient}",
                  "Đối tượng không thuộc khóa/đăng ký; email liên hệ DN nếu SRS yêu cầu TAI_KHOAN.email", content, priority="P1")

tvv_events = [
    ("EM-NOT-TVV-01", "Yêu cầu TVV/CG bổ sung hồ sơ", "CB NV", "Hồ sơ đang thẩm định", "→ YEU_CAU_BO_SUNG", "TVV/CG qua email khai; NHT nộp hồ sơ qua TK", "email cả hai, có lý do"),
    ("EM-NOT-TVV-02", "Kết luận hồ sơ TVV/CG không đạt", "CB NV", "Hồ sơ đang thẩm định", "→ TU_CHOI", "TVV/CG và NHT nộp hồ sơ", "email có lý do"),
    ("EM-NOT-TVV-03", "Phê duyệt TVV/CG và thông báo các bên", "CB PD", "Hồ sơ CHO_PHE_DUYET", "→ CHO_KICH_HOAT", "Chủ hồ sơ; CB NV thẩm định; NHT nộp", "kết quả duyệt; riêng chủ hồ sơ có link kích hoạt"),
    ("EM-NOT-TVV-04", "Từ chối TVV/CG ở bước phê duyệt", "CB PD", "Hồ sơ CHO_PHE_DUYET", "→ TU_CHOI", "Chủ hồ sơ; CB NV; NHT", "email cả ba có lý do")]
for tcid, title, actor, pre, state, recipient, content in tvv_events:
    workflow_case(tcid, "FR-IV-06/07 / BR-NOTIF-01 / srs-fr-04:525-635", "TVV/CG", title, actor, "Hồ sơ TVV/CG",
                  pre + "; có Người hỗ trợ nộp.", "Email TVV và TK NHT/CB khác nhau", state,
                  "Email khai TVV/CG; TAI_KHOAN.email NHT/CB", f"To riêng: {recipient}", "NHT khác/CB khác đơn vị/TVV khác", content)

vv_events = [
    ("EM-NOT-VV-01", "Tiếp nhận vụ việc inbound", "API/System", "Payload hợp lệ", "Tạo vụ việc", "CB NV phụ trách theo đơn vị", "email báo dữ liệu mới"),
    ("EM-NOT-VV-02", "Phân công vụ việc cho cá nhân", "CB NV", "Vụ việc đủ điều kiện phân công", "→ DA_PHAN_CONG", "TVV/CG/NHT được chọn", "email phân công"),
    ("EM-NOT-VV-03", "Phân công qua tổ chức tư vấn có CC", "CB NV", "Chọn tổ chức + TVV cụ thể", "→ DA_PHAN_CONG", "To TVV được cử; CC email liên hệ tổ chức", "đúng To/CC, không CC tổ chức khác"),
    ("EM-NOT-VV-04", "Hồ sơ kiểm tra không đạt tự động báo DN", "System", "DANG_KIEM_TRA; CB kết luận Không đạt", "→ TU_CHOI", "To: diupt01+dn-ag-login@gmail.com (TAI_KHOAN.email DN 0209888006)", "email có lý do; không có nút gửi thủ công"),
    ("EM-NOT-VV-05", "Hoàn thành vụ việc thông báo DN", "CB NV/System", "Vụ việc đủ điều kiện hoàn thành", "→ HOAN_THANH", "To: diupt01+dn-ag-login@gmail.com (TAI_KHOAN.email DN 0209888006)", "email kết quả đúng hồ sơ"),
    ("EM-NOT-VV-06", "Yêu cầu bổ sung hồ sơ", "CB NV", "Vụ việc cần bổ sung", "→ trạng thái bổ sung", "To: diupt01+dn-ag-login@gmail.com (TAI_KHOAN.email DN 0209888006)", "email nêu nội dung cần bổ sung"),
    ("EM-NOT-VV-07", "Phê duyệt vụ việc", "CB PD", "Vụ việc CHO_PHE_DUYET", "→ DA_DUYET", "To: CB NV phụ trách", "email kết quả phê duyệt đúng hồ sơ"),
    ("EM-NOT-VV-11", "Công khai vụ việc", "CB PD", "Vụ việc DA_DUYET/HOAN_THANH và cong_khai=0", "cong_khai=1", "To: diupt01+dn-ag-login@gmail.com (TAI_KHOAN.email DN 0209888006)", "email báo công khai; không chứa field nhạy cảm")]
for tcid, title, actor, pre, state, recipient, content in vv_events:
    source = "TO_CHUC_TU_VAN.email_lien_he cho CC; TAI_KHOAN.email người xử lý" if tcid == "EM-NOT-VV-03" else "TAI_KHOAN.email người nhận theo workflow"
    negative = "diupt01+dn-ag-contact@gmail.com (DOANH_NGHIEP.email) và người ngoài hồ sơ" if tcid in {"EM-NOT-VV-04", "EM-NOT-VV-05", "EM-NOT-VV-06", "EM-NOT-VV-11"} else "Người ngoài hồ sơ/khác đơn vị"
    workflow_case(tcid, "FR-V.I / BR-NOTIF-01 / srs-fr-05:419,750,908-956,2485", "Vụ việc", title, actor, "Module Vụ việc > hồ sơ tương ứng",
                  pre, "Fixture DN/người xử lý/đơn vị tách mailbox", state, source, f"{recipient}", negative, content)
for n, (level, recipient) in enumerate([("SAP_HET_HAN", "CB NV"), ("QUA_HAN", "CB NV + CB PD"), ("QUA_HAN_NGHIEM_TRONG", "CB NV + CB PD + cấp trên")], start=8):
    severe = level == "QUA_HAN_NGHIEM_TRONG"
    workflow_case(f"EM-NOT-VV-{n:02d}", "FR-V.I-CROSS SLA / BR-SLA-03 / srs-fr-05:2449", "Vụ việc", f"Cảnh báo SLA vụ việc {level}", "Scheduled job", "Job SLA vụ việc",
                  f"Vụ việc vừa chuyển {level}; email toggle bật.", "Clock đúng ngưỡng", f"Mức → {level}",
                  "TAI_KHOAN.email cbnv_bn_01 + cbpd_bn_01 + CB_PD_TW đúng đơn vị cha" if severe else "TAI_KHOAN.email theo ma trận",
                  "To: cbnv_bn_01 + cbpd_bn_01 + ít nhất 1 CB_PD_TW đúng đơn vị cha" if severe else f"To: {recipient}",
                  "CB NV/CB PD thuộc đơn vị khác; tài khoản TW không có role CB_PD_TW" if severe else "Người ngoài ma trận",
                  "email có mức/deadline/mã hồ sơ; không trùng")

workflow_case("EM-NOT-CT-01", "FR-V.II-08/10 / srs-fr-06:758-790", "Chi trả", "Gửi kết quả thẩm định cho TVV", "System sau UC76", "Hồ sơ chi trả > hoàn tất thẩm định",
              "Thẩm định hoàn tất; TVV có TK/email.", "Kết quả dạng chữ", "Kết quả thẩm định được ghi nhận",
              "TAI_KHOAN.email TVV", "To: TVV", "DN/TVV khác", "email kết quả dạng chữ, KHÔNG có file đính kèm",
              extra_oracle="SMTP attachment count = 0; in-app chỉ TVV thấy.")

for tcid, trace_ref, title, actor, pre, state, recipient, content, source in [
    ("EM-NOT-CT-02", "FR-V.II-07 / srs-fr-06:595-614", "DN gửi đề nghị thanh toán", "DVC/System", "Hồ sơ DA_DUYET; payload có ít nhất 1 file mới", "Giữ DA_DUYET và tiếp nhận chứng từ", "CB NV phụ trách", "email báo DN đã gửi đề nghị thanh toán", "TAI_KHOAN.email CB NV"),
    ("EM-NOT-CT-03", "FR-V.II-11 / srs-fr-06:795-840", "Trình phê duyệt hồ sơ thanh toán", "CB NV", "Hồ sơ DANG_THAM_DINH; kết quả Đạt", "→ CHO_PHE_DUYET", "CB PD cùng đơn vị", "email báo hồ sơ chờ duyệt", "TAI_KHOAN.email CB PD"),
    ("EM-NOT-CT-04", "FR-V.II-12 / srs-fr-06:845-911", "Phê duyệt hồ sơ thanh toán", "CB PD", "Hồ sơ CHO_PHE_DUYET; quyết định hợp lệ", "→ DA_DUYET", "CB NV + TVV + DN", "email kết quả duyệt đúng đối tượng", "TAI_KHOAN.email người nhận workflow"),
    ("EM-NOT-CT-05", "FR-V.II-13 / srs-fr-06:917-972", "Cập nhật đã thanh toán", "CB NV", "Hồ sơ DA_DUYET", "→ DA_THANH_TOAN", "TVV + DN", "email kết quả thanh toán", "TAI_KHOAN.email TVV/DN")]:
    workflow_case(tcid, trace_ref, "Chi trả", title, actor, "Module Chi trả > hồ sơ tương ứng", pre,
                  "Mailbox CB NV/CB PD/TVV/DN tách biệt", state, source, f"To: {recipient}",
                  "Người ngoài hồ sơ/khác đơn vị", content)

for tcid, trace_ref, title, actor, pre, state, recipient, content in [
    ("EM-NOT-DG-01", "FR-VI-03 / srs-fr-08:240-315", "Phân công người đánh giá", "CB NV", "Kế hoạch/tiêu chí đủ điều kiện phân công", "Lưu phân công", "Người được phân công", "email thông báo phân công"),
    ("EM-NOT-DG-02", "FR-VI-04 / srs-fr-08:322-396", "Phê duyệt phân công", "CB PD", "Phân công chờ phê duyệt", "→ THUC_HIEN", "CB NV trình", "email kết quả phê duyệt"),
    ("EM-NOT-DG-03", "FR-VI-08 / srs-fr-08:628-687", "Trình phê duyệt báo cáo đánh giá", "CB NV", "Báo cáo hoàn chỉnh", "→ CHO_PHE_DUYET", "CB PD", "email báo cáo chờ duyệt"),
    ("EM-NOT-DG-04", "FR-VI-09 / srs-fr-08:692-747", "Phê duyệt báo cáo đánh giá", "CB PD", "Báo cáo CHO_PHE_DUYET", "→ HOAN_THANH", "CB NV trình", "email kết quả phê duyệt")]:
    workflow_case(tcid, trace_ref, "Đánh giá", title, actor, "Module Đánh giá > hồ sơ tương ứng", pre,
                  "Mailbox người nhận tách biệt", state, "TAI_KHOAN.email người nhận", f"To: {recipient}",
                  "Người ngoài phân công/khác đơn vị", content)

tvcs_events = [
    ("EM-NOT-TVCS-01", "Phân công CG", "CB NV", "TIEP_NHAN; CG phù hợp", "TIEP_NHAN→PHAN_CONG", "CG", "in-app + email; SLA xác nhận 2 ngày LV"),
    ("EM-NOT-TVCS-02", "CG xác nhận", "CG", "PHAN_CONG", "PHAN_CONG→DANG_TU_VAN", "CB NV + DN", "CB NV in-app+email; DN email-only"),
    ("EM-NOT-TVCS-03", "CG từ chối", "CG", "PHAN_CONG; lý do hợp lệ", "PHAN_CONG→TIEP_NHAN", "CB NV", "email có lý do, cần phân công lại"),
    ("EM-NOT-TVCS-04", "Hoàn thành tư vấn tự trình duyệt", "System", "HOAN_THANH", "HOAN_THANH→CHO_PHE_DUYET", "CB PD cùng đơn vị", "in-app + email"),
    ("EM-NOT-TVCS-05", "Phê duyệt kết quả", "CB PD", "CHO_PHE_DUYET", "CHO_PHE_DUYET→DA_DUYET", "DN", "kết quả qua Cổng/email theo kênh; email-only mời đánh giá; không gửi trùng"),
    ("EM-NOT-TVCS-06", "Từ chối phê duyệt", "CB PD", "CHO_PHE_DUYET; lý do", "CHO_PHE_DUYET→DANG_TU_VAN", "CG", "in-app + email có lý do bổ sung"),
    ("EM-NOT-TVCS-07", "Hủy khi CG chưa xác nhận", "CB NV", "PHAN_CONG; có yêu cầu/lý do", "PHAN_CONG→HUY", "CG + DN", "CG in-app+email; DN email-only"),
    ("EM-NOT-TVCS-08", "Dữ liệu TVCS inbound", "Cổng PLQG/System", "Payload hợp lệ", "Tạo dữ liệu", "CB NV phụ trách theo đơn vị", "in-app + email")]
for tcid, title, actor, pre, state, recipient, content in tvcs_events:
    source = "DOANH_NGHIEP.email cho DN chưa TK; TAI_KHOAN.email cho CB/CG"
    extra = "Với DN: THONG_BAO.nguoi_nhan_id=NULL, email_nguoi_nhan=DOANH_NGHIEP.email, hien_trong_ung_dung=0. Email trống → warning, không rollback."
    workflow_case(tcid, "FR-X.1-01/03/05 / BR-NOTIF-01 / srs-fr-12:180-250,1549-1656", "Tư vấn chuyên sâu", title, actor, "Module TVCS/API inbound",
                  pre, "Mailbox CG/CB/DN tách biệt; DN nhóm này chưa TK", state, source, f"To: {recipient}", "DN/CG/CB không thuộc hồ sơ", content, extra_oracle=extra)

for n, (delta, label) in enumerate([(7, "trước hạn 7 ngày"), (3, "trước hạn 3 ngày"), (-1, "quá hạn")], start=1):
    workflow_case(f"EM-NOT-BC-{n:02d}", "FR-XI-NEW-01 / srs-fr-15:1047-1074", "Báo cáo HTPLDN", f"Nhắc đơn vị nộp báo cáo {label}", "Scheduled job", "Job nhắc báo cáo",
                  "Đợt đang mở; đơn vị CHUA_NOP/DANG_LAP; chưa gửi cùng loại trong 24h.", f"delta={delta}", "Không đổi trạng thái nộp; tạo notification đúng loại",
                  "TAI_KHOAN.email CB NV đơn vị nộp", "To: CB NV đúng đơn vị", "CB đơn vị khác/đơn vị đã nộp", f"email nhắc {label}")
workflow_case("EM-NOT-BC-04", "FR-XI-NEW-01 dedupe 24h / srs-fr-15:1072", "Báo cáo HTPLDN", "Không gửi lặp nhắc báo cáo trong 24 giờ", "Scheduled job", "Chạy lại job nhắc báo cáo",
              "Đã gửi cùng notification <24h; trạng thái vẫn CHUA_NOP/DANG_LAP.", "Chạy job lần 2", "Không tạo notification/email mới",
              "Không áp dụng", "Không có email mới", "Tất cả mailbox", "message-id/count giữ nguyên", typ="Negative regression",
              email_expected=False, app_expected=False)

workflow_case("EM-NOT-NO-01", "BR-SLA-03", "Cấu hình SLA", "Tắt gửi email nhưng giữ in-app", "QTHT + Scheduled job", "Cấu hình SLA > toggle Gửi email OFF",
              "Email OFF; in-app ON; hồ sơ chuyển mức cảnh báo.", "Trigger đúng ngưỡng", "Mức SLA đổi; in-app được tạo",
              "Không áp dụng", "Không email", "Tất cả mailbox", "không queue/SMTP; THONG_BAO in-app tồn tại", typ="Negative regression",
              email_expected=False, app_expected=True)
workflow_case("EM-NOT-NO-02", "BR-SLA-03 / BA 2026-08-09", "Cảnh báo SLA", "Không gửi khi xóa mức do hồ sơ kết thúc/không có hạn", "System", "Job SLA",
              "Hồ sơ vừa kết thúc hoặc deadline bị xóa; trước đó có mức cảnh báo.", "Remove warning level", "Mức được xóa nhưng không coi là chuyển mức gửi TB",
              "Không áp dụng", "Không email/in-app mới", "Tất cả mailbox", "count queue/THONG_BAO giữ nguyên", typ="Negative regression",
              email_expected=False, app_expected=False)

# Các field email ngoài TAI_KHOAN/DOANH_NGHIEP: UI, Excel và API.
field_cases = [
    ("EM-FLD-HDD-01", "FR-II-01 Inputs#5 / SCR-II-01 row 41 / srs-fr-02:104,1065", "Hỏi đáp", "Email người gửi là tùy chọn và hợp lệ",
     "CB NV", "Hỏi đáp > Tạo mới", "Form tạo hỏi đáp mở.", "email_nguoi_gui = qa.sender+uat@example.test",
     "1. Mở form.\n2. Để trống email và lưu hồ sơ A.\n3. Tạo hồ sơ B với email hợp lệ.\n4. Mở chi tiết/list.",
     "2. Hồ sơ A lưu được vì email không bắt buộc.\n3. Hồ sơ B lưu được.\n4. Email B hiển thị đúng, không bị cắt/sửa; hồ sơ A không phát sinh email giả.",
     "HOI_DAP.email_nguoi_gui; UI list/detail; không tự tạo TAI_KHOAN."),
    ("EM-FLD-HDD-02", "FR-II-01 Inputs#5 / SCR-II-01 row 41", "Hỏi đáp", "Email người gửi sai format",
     "CB NV", "Hỏi đáp > Tạo mới", "Form tạo hỏi đáp mở.", "email_nguoi_gui = invalid-email",
     "1. Nhập các field bắt buộc hợp lệ.\n2. Nhập email sai.\n3. Submit.\n4. Kiểm tra UI/API.",
     "3. Inline nguyên văn 'Email không đúng định dạng'; không submit.\n4. Không tạo/cập nhật HOI_DAP, queue hoặc email.",
     "HOI_DAP count trước/sau; validation UI/API."),
    ("EM-FLD-HDD-03", "FR-II-01 Inputs#5 max 100", "Hỏi đáp", "Biên độ dài email người gửi 100/101 ký tự",
     "CB NV", "Hỏi đáp > Tạo mới", "Có hai địa chỉ syntactically valid dài đúng 100 và 101 ký tự.", "email length = 100 rồi 101",
     "1. Submit địa chỉ dài 100.\n2. Ghi kết quả.\n3. Submit địa chỉ dài 101.\n4. Kiểm tra UI/API.",
     "1. Địa chỉ 100 ký tự được chấp nhận nếu hợp lệ.\n3. Địa chỉ 101 bị chặn; không truncate thầm lặng.\n4. UI/API lưu nguyên giá trị case 100, không có record case 101.",
     "Length client/server/UI/API; không truncate."),
    ("EM-FLD-HDD-04", "FR-II-01 Outputs Excel / srs-fr-02:155", "Hỏi đáp", "Xuất Excel hỏi đáp có cột Email đúng dữ liệu",
     "CB NV có quyền xuất", "Danh sách hỏi đáp > Xuất Excel", "Có 3 hồ sơ: email hợp lệ, email rỗng, ký tự tiếng Việt ở tên người gửi.", "Bộ lọc trả đúng 3 hồ sơ",
     "1. Áp bộ lọc.\n2. Xuất Excel.\n3. Mở file.\n4. Đối chiếu từng dòng với UI/API/detail.",
     "File mở được; có cột Email đúng thứ tự SRS; 3 dòng khớp hồ sơ/filter; email rỗng vẫn rỗng; không formula injection/truncate.",
     "File .xlsx; header/row count/cell value; so với HOI_DAP.email_nguoi_gui."),
    ("EM-FLD-DT-01", "srs-fr-03:1939-1953", "Đào tạo", "Email học viên hiển thị nhất quán trên các tab",
     "CB NV", "Chi tiết khóa học > Học viên/Điểm danh/Kết quả/Công bố", "Một học viên đã duyệt có email xác định.", "hoc_vien_id HV01; hv01@example.test",
     "1. Mở lần lượt Tab Học viên, Điểm danh, Kết quả, Công bố.\n2. Tìm HV01.\n3. Đối chiếu email từng tab với UI/API.",
     "HV01 hiển thị đúng cùng email ở tất cả tab có cột email; không lấy nhầm email DN/NHT đăng ký hoặc học viên khác.",
     "HOC_VIEN.email join theo hoc_vien_id; UI row mapping."),
    ("EM-FLD-DT-02", "FR-III-05 / srs-fr-03:580-615", "Đào tạo", "Mẫu Excel điểm danh/điểm kiểm tra điền đúng email học viên",
     "CB NV", "Chi tiết khóa học > Tải mẫu", "Khóa có ≥3 học viên, chọn buổi/đề hợp lệ.", "Ba hoc_vien_id/email khác nhau",
     "1. Chọn buổi và tải mẫu điểm danh.\n2. Chọn đề và tải mẫu điểm kiểm tra.\n3. Mở hai file, hiện cột/metadata ẩn nếu có.\n4. Đối chiếu từng hoc_vien_id-họ tên-email.",
     "Mỗi file có đúng danh sách học viên; email khớp hoc_vien_id; không dùng email làm khóa thay hoc_vien_id; metadata buổi/đề đúng.",
     "File protection/hidden id; mapping HOC_VIEN; checksum file."),
    ("EM-FLD-DT-03", "FR-III-05 KTDGKQHT_05", "Đào tạo", "Import không được nhận diện học viên bằng email",
     "CB NV", "Import điểm danh/điểm kiểm tra", "Tải mẫu hợp lệ; giữ hoc_vien_id HV01 nhưng sửa email hiển thị thành email HV02.", "hoc_vien_id HV01 + email hv02@example.test",
     "1. Sửa email trong bản sao mẫu, không đổi hoc_vien_id.\n2. Điền trạng thái/điểm hợp lệ.\n3. Import.\n4. Kiểm tra preview/kết quả và UI/API.",
     "Hệ thống nhận diện theo hoc_vien_id, không ghi kết quả sang HV02 vì email. Nếu cột email bị khóa và hệ thống từ chối file sửa, phải báo rõ; tuyệt đối không map theo email.",
     "Import parser key=hoc_vien_id; kết quả HV01/HV02 trước-sau."),
    ("EM-FLD-API-01", "FR-XII-19 Inputs email_nguoi_gui / srs-fr-16:1169", "API Hỏi đáp inbound", "Email người gửi API: absent/valid/invalid/max",
     "Cổng PLQG/API client", "API inbound hỏi đáp", "JWT/mTLS hợp lệ; payload base hợp lệ.", "4 payload: absent; valid; invalid; >100",
     "1. POST payload không email.\n2. POST email hợp lệ.\n3. POST email sai RFC.\n4. POST email >100.\n5. Kiểm tra response/UI/notification.",
     "1. Chấp nhận vì optional.\n2. Chấp nhận và lưu nguyên email.\n3-4. Từ chối validation, không partial save/notification.\n5. Chỉ 2 record hợp lệ và notification tương ứng được tạo.",
     "HTTP status/error detail; HOI_DAP; transaction/queue."),
    ("EM-FLD-API-02", "FR-V.I-05 EC-V.I-05-01 / srs-fr-05:393,478", "API Vụ việc inbound", "Validate email nested trong thong_tin_dn",
     "Hệ thống ngoài/API client", "API inbound vụ việc", "Auth hợp lệ; payload base hợp lệ.", "email valid rồi invalid",
     "1. POST payload email hợp lệ.\n2. POST payload email sai RFC.\n3. Kiểm tra response.\n4. Kiểm tra UI/API/notification.",
     "1. Payload hợp lệ được xử lý.\n2. Payload sai trả ERR-INTG-03 kèm field lỗi email.\n3-4. Không partial save/notification cho request sai.",
     "Response ERR-INTG-03; entity/transaction; queue."),
    ("EM-FLD-API-03", "FR-X.1-03 / srs-fr-12:469,483,499", "API TVCS inbound", "Email DN optional nhưng nếu có phải hợp lệ",
     "Cổng PLQG", "API inbound TVCS", "Auth/payload base hợp lệ; MST/tên DN hợp lệ.", "email absent; valid; invalid",
     "1. POST không email.\n2. POST email hợp lệ với MST khác.\n3. POST email invalid với MST khác.\n4. Kiểm tra UI/API và queue.",
     "1-2. Chấp nhận và tạo DN/TVCS theo spec; case absent lưu NULL.\n3. Từ chối format, không partial save.\n4. Không case nào tạo TAI_KHOAN/mail kích hoạt; chỉ notification CB cho request hợp lệ.",
     "DOANH_NGHIEP/TVCS transaction; TAI_KHOAN +0; activation queue +0."),
    ("EM-FLD-API-04", "FR-X.1-05 / srs-fr-12:748-782", "API Hồ sơ pháp lý inbound", "Email DN optional trong hồ sơ pháp lý inbound",
     "Cổng PLQG", "API inbound hồ sơ pháp lý", "Auth/payload base hợp lệ.", "email absent; valid; invalid",
     "1. Gửi lần lượt 3 payload.\n2. Đối chiếu response.\n3. Kiểm tra UI/API và queue.",
     "Absent/valid được xử lý; invalid bị từ chối không partial save; không tạo TK/mail kích hoạt; CB phụ trách chỉ nhận notification với request hợp lệ.",
     "Entity/transaction; TAI_KHOAN/token/queue activation +0."),
    ("EM-FLD-API-05", "BR-PUBLIC-04 / srs-fr-05:1369,2503", "API outbound/public", "Không xuất email/SĐT/địa chỉ DN trong vụ việc công khai",
     "Cổng PLQG/API client", "API outbound vụ việc công khai", "Vụ việc đã duyệt có đầy đủ PII DN.", "email_dn=secret@example.test",
     "1. Gọi API danh sách/chi tiết công khai.\n2. Tìm email và các PII trong JSON.\n3. Kiểm tra log sanitize.",
     "Response chỉ có 10 field whitelist; không có email/SĐT/địa chỉ DN trong key hoặc free-text; nếu phát hiện PII phải chặn publish và audit security.",
     "Raw JSON, whitelist keys, SEC_PII_LEAK audit."),
    ("EM-FLD-API-06", "FR-XII org mapping / srs-fr-16:536,1552", "API outbound tổ chức", "Email liên hệ công khai của tổ chức được map đúng",
     "Cổng PLQG/API client", "API outbound tổ chức tư vấn", "Tổ chức được phép công khai có email liên hệ.", "org.public@example.test",
     "1. Gọi API danh sách/chi tiết tổ chức.\n2. Đối chiếu email với TO_CHUC_TU_VAN.\n3. Kiểm tra tổ chức không được công khai.",
     "Tổ chức được phép có đúng email liên hệ theo mapping; không lẫn email cá nhân TVV/TK; tổ chức ngoài scope không xuất hiện.",
     "API JSON vs TO_CHUC_TU_VAN.email; scope/public flag."),
    ("EM-FLD-TVV-01", "FR-IV-02 Inputs email / srs-fr-04:302-364", "TVV/CG", "Đăng ký TVV với email hợp lệ duy nhất",
     "NHT", "Đăng ký hồ sơ TVV/CG", "Email chưa dùng trong hệ thống.", "new.tvv@example.test",
     "1. Mở form.\n2. Nhập email hợp lệ và dữ liệu bắt buộc.\n3. Submit.\n4. Kiểm tra hồ sơ/TK/queue.",
     "Tạo hồ sơ MOI_DANG_KY với email đúng; chưa tạo TK/mail kích hoạt trước khi CB PD duyệt.",
     "TU_VAN_VIEN.email; TAI_KHOAN/token/activation queue +0."),
    ("EM-FLD-TVV-02", "FR-IV-02 E7 ERR-DK-07", "TVV/CG", "Đăng ký TVV email sai format",
     "NHT", "Đăng ký hồ sơ TVV/CG", "Form hợp lệ trừ email.", "invalid-email",
     "1. Nhập dữ liệu.\n2. Submit.\n3. Kiểm tra UI/API.",
     "Hiển thị 'Email không đúng định dạng'; không tạo hồ sơ/TK/mail.",
     "TU_VAN_VIEN count; response/message; queue +0."),
    ("EM-FLD-TVV-03", "FR-IV-02 E9 ERR-DK-09", "TVV/CG", "Đăng ký TVV email đã tồn tại",
     "NHT", "Đăng ký hồ sơ TVV/CG", "Email đã thuộc TVV/tài khoản khác.", "existing.tvv@example.test",
     "1. Nhập dữ liệu.\n2. Submit.\n3. Kiểm tra UI/API.",
     "Hiển thị 'Email này đã được sử dụng bởi tư vấn viên khác'; không tạo hồ sơ/TK/mail.",
     "Unique lookup toàn hệ thống; entity count/queue."),
    ("EM-FLD-TVV-04", "FR-IV-10 / srs-fr-04:821-864", "TVV/CG", "Cập nhật email TVV validate format và unique",
     "NHT đúng đơn vị", "Chi tiết TVV > Cập nhật liên hệ", "TVV hiện hữu; chuẩn bị email valid mới, invalid, duplicate.", "3 lần cập nhật",
     "1. Đổi sang email valid mới, lưu/reload.\n2. Đổi sang invalid.\n3. Đổi sang duplicate.\n4. Kiểm tra UI/API/audit.",
     "1. Email mới lưu đúng.\n2. ERR-CN-01 'Định dạng email không hợp lệ'.\n3. ERR-CN-04 'Email này đã được sử dụng bởi tư vấn viên khác'.\n4. Hai case lỗi dữ liệu trên UI không đổi; audit case thành công.",
     "TU_VAN_VIEN.email old/new; uniqueness; audit."),
    ("EM-FLD-TVV-05", "FR-IV-11 srs-fr-04:815-849 / BR-AUTH-EMAIL-01 canonical srs-v3.5:5616 / FR-VIII-26 srs-fr-10:1319-1323", "TVV/CG", "TVV đã có TK đổi email liên hệ: kiểm routing và ghi nhận đồng bộ",
     "NHT đúng đơn vị", "Chi tiết TVV HOAT_DONG > Cập nhật liên hệ", "TU_VAN_VIEN.email = TAI_KHOAN.email trước test.", "new.tvv.contact@example.test",
     "1. Ghi hai email trước test.\n2. NHT đổi email TVV.\n3. Reload hai entity.\n4. Trigger reset/notification.\n5. Kiểm tra inbox.",
     "FR-IV-11 cập nhật TU_VAN_VIEN.email. Sau thay đổi, reset và mọi notification workflow vẫn phải gửi tới TAI_KHOAN.email; gửi sang email liên hệ TVV là Fail. Riêng việc TAI_KHOAN.email có tự đồng bộ hay không chưa được FR-IV-11 đặc tả: ghi Actual + BA clarification, không tự chấm.",
     "TU_VAN_VIEN.email, TAI_KHOAN.email, recipient routing, audit."),
]
for tcid, trace_id, feature, title, actor, start, pre, data, steps, expected, oracle in field_cases:
    add("notification", tcid, trace_id, feature + " — Field/API/Export", "P0", "UI/API/Data/Negative", title,
        actor, start, pre, data, steps, expected, "Field/entity nêu trong TraceID", "Theo case; không tự gửi nếu chỉ validate/display",
        "Mailbox/entity không thuộc record", oracle, "Dùng fixture riêng; rollback/delete fixture nếu quy trình cho phép.")

# ---------------------------------------------------------------------------
# 04. SMTP / SECURITY / NFR
# ---------------------------------------------------------------------------
def infra_case(tcid, trace, feature, title, priority, typ, pre, data, steps, expected, oracle, status="Not Run", note=""):
    add("infra", tcid, trace, feature, priority, typ, title, "QA kỹ thuật/QTHT", "SMTP test harness + ứng dụng",
        pre, data, steps, expected, "Theo testcase trigger", "Theo testcase trigger", "Mailbox không thuộc recipient matrix",
        oracle, "Khôi phục SMTP/config/clock; xóa fixture queue; lưu log và message-id.", status=status, note=note)

infra_specs = [
    ("EM-INF-01", "INT-06 / SEC-01 §3.5.1 srs-v3.5:4605 / Architecture srs-v3.5:394 / phụ: SEC-03 §4.2.18 srs-v3.5:5138", "SMTP", "Kết nối SMTP qua TLS", "P0", "Integration", "Có quyền xem handshake SMTP.", "SMTP TLS hợp lệ", "1. Bật capture handshake.\n2. Trigger một email.\n3. Kiểm tra protocol/cipher/certificate.\n4. Kiểm tra accepted.", "Ứng dụng kết nối SMTP/TLS 1.2+; cert hợp lệ; email accepted; không gửi credential plaintext.", "SMTP connection/handshake log; message-id."),
    ("EM-INF-02", "NFR-NOTIF-01", "Delivery SLA", "Email được SMTP accepted trong ≤5 phút", "P0", "Performance", "Đồng bộ clock ứng dụng/API/SMTP.", "Tối thiểu 20 trigger đại diện", "1. Ghi event timestamp.\n2. Trigger email.\n3. Ghi SMTP accepted timestamp.\n4. Tính delta từng mẫu.\n5. Kiểm tra alert nếu >5 phút.", "Mọi mẫu delta ≤5 phút. Mẫu >5 phút phải tạo alert QTHT và testcase delivery bị Fail.", "Event time, queue created/attempt time, SMTP accepted time, alert."),
    ("EM-INF-03", "[NGOÀI SRS] INT-06 Email HTML", "Rendering", "HTML và tiếng Việt hiển thị đúng", "P1", "Compatibility", "Gmail thật nhận được thư; có quyền mở Show original.", "Tên/mã/lý do có dấu tiếng Việt và ký tự &,<,>", "1. Trigger mail mẫu.\n2. Mở thư trong Gmail.\n3. Kiểm tra subject/body/link và Show original.\n4. Xem plain-text fallback nếu template có.", "Không lỗi font/encoding/layout; biến được escape; link đúng; nội dung không bị cắt sai.", "Gmail Show original: To/CC/Message-ID/Content-Type/charset + ảnh thư đã render."),
    ("EM-INF-04", "BR-EC-11", "Retry", "SMTP lỗi tạm thời được retry", "P0", "Resilience", "SMTP stub trả timeout/5xx 2 lần rồi success.", "Retry sequence fail,fail,success", "1. Cấu hình stub.\n2. Trigger một mail.\n3. Theo dõi attempts.\n4. Cho lần 3 success.\n5. Kiểm tra inbox/flags.", "Tối đa 3 lần gửi; lần 3 thành công; không gửi trùng; cuối cùng một mail accepted. Không assert khoảng cách retry, trừ case Hỏi đáp kiểm riêng 10 phút.", "Queue attempts/timestamps nếu có quyền; Gmail chỉ có một thư/message-id."),
    ("EM-INF-05", "BR-EC-11 / srs-fr-02 ERR-SLA-MAIL-01", "Retry", "Ba lần lỗi đánh dấu thất bại và cảnh báo QTHT", "P0", "Resilience", "SMTP fail liên tục.", "3 failures", "1. Trigger mail.\n2. Cho SMTP fail đủ 3 lần.\n3. Theo dõi queue.\n4. Kiểm tra dashboard/in-app QTHT.\n5. Kiểm tra recipient inbox.", "Sau 3 lần: trạng thái THAT_BAI/email_failed=true; tạo in-app + alert QTHT; recipient không có mail; nghiệp vụ không bị gửi/commit lặp.", "Attempts, final status, QTHT alert, audit. Lưu ý lịch retry 10 phút chỉ được nêu riêng Hỏi đáp."),
    ("EM-INF-06", "THONG_BAO entity srs-v3.5:2406-2407", "Delivery flags", "Chỉ set đã gửi và thời gian sau SMTP accepted", "P0", "Data integrity", "SMTP stub cho phép pause trước accepted.", "Kiểm tra trước/sau accepted", "1. Trigger email và pause SMTP.\n2. Đọc trạng thái gửi qua API/màn quản trị nếu có.\n3. Cho SMTP accepted.\n4. Đọc lại trạng thái và kiểm Gmail.", "Trước SMTP accepted chưa được báo gửi thành công. Sau accepted, trạng thái gửi và thời gian cập nhật đúng; Gmail nhận đúng một thư. Nếu môi trường không mở trạng thái này qua API/UI thì ghi Not Run, không yêu cầu DB.", "API/màn quản trị + Gmail + SMTP timestamp nếu có quyền."),
    ("EM-INF-07", "[NGOÀI SRS] BR-NOTIF-01", "Idempotency", "Double-click trigger không gửi trùng", "P1", "Concurrency", "Action workflow cho phép gửi notification.", "Hai request cùng idempotency context", "1. Ghi baseline.\n2. Double-click/gửi 2 request đồng thời.\n3. Chờ queue.\n4. Kiểm tra state/inbox/UI/API.", "Một transition, một THONG_BAO theo người/sự kiện, một email/message-id; request thứ hai không tạo side effect.", "Unique/idempotency key, state version, queue/message-id."),
    ("EM-INF-08", "[NGOÀI SRS] BR-NOTIF-01", "Recipient privacy", "Không lộ danh sách người nhận hàng loạt", "P1", "Security", "Sự kiện gửi nhiều học viên/CB.", "≥3 recipient khác domain", "1. Trigger bulk notification.\n2. Mở raw mail từng người.\n3. Kiểm tra To/CC/BCC.\n4. So recipient envelope.", "Mỗi người không thấy email người không cần biết; To/CC đúng nghiệp vụ; không dùng CC toàn bộ học viên.", "Raw MIME + SMTP envelope recipients."),
    ("EM-INF-09", "FR-V.I assignment", "CC routing", "CC đúng điểm liên hệ tổ chức tư vấn", "P0", "Integration", "Có 2 tổ chức, mỗi tổ chức email riêng.", "Chọn tổ chức A + TVV A", "1. Phân công qua tổ chức A.\n2. Kiểm tra raw mail.\n3. Kiểm tra inbox A/B.", "To TVV A; CC chính xác email liên hệ tổ chức A; tổ chức B và TVV B không nhận.", "SMTP To/CC; source TO_CHUC_TU_VAN.email_lien_he."),
    ("EM-INF-10", "§3.5 XSS policy srs-v3.5:4623-4639", "XSS", "Sanitize script trong nội dung email", "P0", "Security", "Có field rich-text đi vào email.", "<script>alert(1)</script><b>Hợp lệ</b>", "1. Nhập payload qua UI/API.\n2. Trigger email.\n3. Xem raw HTML và render.\n4. Kiểm tra security log.", "script bị loại/reject theo tầng; không thực thi; tag whitelist b được giữ đúng nếu request được chấp nhận.", "Raw HTML; UI/API response; security alert nếu bypass client."),
    ("EM-INF-11", "§3.5 XSS policy", "XSS", "Sanitize event handler và javascript URL", "P0", "Security", "Có field rich-text đi vào email.", "<img src=x onerror=alert(1)><a href=javascript:alert(1)>x</a>", "1. Gửi payload qua API bypass client.\n2. Trigger email.\n3. Xem raw/render.\n4. Kiểm tra log.", "Server/pre-email sanitize chặn tag/attribute/URL nguy hiểm; không thực thi và không gửi HTML độc hại.", "Raw MIME and security log."),
    ("EM-INF-12", "BR-SEC-01; srs-v3.5:5746", "PII", "Email/public content không rò dữ liệu nhạy cảm", "P0", "Security", "Fixture có CCCD, SĐT, email cá nhân, địa chỉ, tài khoản NH.", "Trigger công khai/email template", "1. Tạo fixture PII.\n2. Trigger publish/email liên quan.\n3. Tìm 6 nhóm PII trong raw body/attachment/link.\n4. Kiểm tra audit security.", "Chỉ field được phép xuất hiện; không có password/hash/token/CCCD/tài khoản NH; vi phạm bị chặn/log SEC_PII_LEAK.", "Raw body/attachment/API; security audit."),
    ("EM-INF-13", "[NGOÀI SRS] FR-VIII-22/26 token", "Token security", "Token không lộ trong log/analytics/Referer", "P0", "Security", "Có access log/APM/browser devtools.", "Activation/reset URL", "1. Yêu cầu link.\n2. Mở link.\n3. Kiểm tra app/proxy/APM/analytics logs.\n4. Điều hướng khỏi trang và xem Referer.", "Không log token đầy đủ; không gửi token tới analytics/third party/Referer; UI/API lưu an toàn theo thiết kế.", "Log search theo token; network capture."),
    ("EM-INF-15", "FR-V.II-08", "Attachment", "Mail thẩm định chi trả không có file", "P0", "Negative regression", "Có hồ sơ hoàn tất thẩm định.", "Kết quả chữ + hệ thống có file nghiệp vụ", "1. Trigger kết quả thẩm định.\n2. Mở raw MIME.\n3. Kiểm tra attachment count/link.", "Email/in-app chỉ có nội dung chữ; attachment count=0; không lộ file nghiệp vụ qua link.", "MIME parts; signed URLs; inbox."),
    ("EM-INF-18", "BR-NOTIF-01", "Data isolation", "Không gửi chéo đơn vị", "P0", "Security", "Có CB PD/CB NV cùng role ở hai đơn vị.", "Trigger trình duyệt tại đơn vị A", "1. Dọn mailbox A/B.\n2. Trigger ở A.\n3. Kiểm tra inbox và UI/API recipient.", "Chỉ CB đúng đơn vị/cấp theo BR-AUTH-05 nhận; đơn vị B không có THONG_BAO/email.", "Recipient query includes don_vi_id; inbox A/B."),
    ("EM-INF-19", "BR-AUTH-EMAIL-01", "Routing", "Workflow dùng TAI_KHOAN.email, không dùng email DN", "P0", "Integration", "TK email và DN email khác nhau.", "Trigger workflow người login", "1. Đặt hai email khác nhau.\n2. Trigger notification workflow.\n3. Kiểm tra inbox/log.", "Email gửi TAI_KHOAN.email; DOANH_NGHIEP.email không nhận trừ ngoại lệ DN chưa TK/TVCS.", "Resolved recipient source and message envelope."),
    ("EM-INF-20", "BR-NOTIF-01 TVCS", "Email-only", "Bản ghi thông báo email-only DN chưa tài khoản", "P0", "Data integrity", "TVCS có DN chưa TK và email hợp lệ.", "Trigger CG xác nhận/hủy", "1. Trigger sự kiện.\n2. Kiểm tra Gmail của DN.\n3. Đăng nhập các tài khoản liên quan và kiểm chuông/trang thông báo.\n4. Kiểm tra phản hồi API hoặc log nếu có quyền.", "DN chưa có tài khoản nhận đúng email; thông báo không xuất hiện trên chuông của bất kỳ người dùng nào; nghiệp vụ vẫn hoàn tất.", "UI/API + Gmail + chuông."),
    ("EM-INF-21", "THONG_BAO constraint srs-v3.5:2409", "Data integrity", "Không tạo THONG_BAO trống cả người nhận và email", "P0", "Negative", "DN chưa TK và email NULL.", "Trigger TVCS email-only", "1. Trigger sự kiện với DN chưa có tài khoản và email trống.\n2. Kiểm tra Gmail và chuông các tài khoản liên quan.\n3. Kiểm tra cảnh báo trên UI/log nếu có quyền.\n4. Kiểm tra trạng thái nghiệp vụ trên UI.", "Không gửi email và không hiện thông báo không có người nhận; có cảnh báo để CB liên hệ nếu UI/log hỗ trợ; luồng nghiệp vụ không bị chặn theo SRS.", "UI/API + Gmail + chuông + warning log nếu có quyền."),
]
for spec in infra_specs:
    infra_case(*spec)

# Chỉ đặt Blocked khi toàn bộ oracle bắt buộc chưa thể xác định hoặc thực thi.
blocked_by_gap = set()
for case in sum(groups.values(), []):
    if case["Test Case ID"] in blocked_by_gap:
        case["Trạng thái"] = "Blocked"

# Kết quả thực thi DEV ngày 2026-08-12. Giữ tại source generator để lần sinh lại
# không ghi đè các case đã chạy về Not Run.
execution_results = {
    "EM-TK-UI-01": ("Fail", "BUG-EM-TK-002: form sửa TK doanh nghiệp thiếu Vai trò. BA-CLAR-EM-TK-001 chờ BA chốt do FR Outputs và SCR mâu thuẫn. Evidence: bug-report/bug-report-em-tk.md", "BUG-EM-TK-002"),
    "EM-TK-UI-02": ("Fail", "BUG-EM-TK-003: tooltip Email doanh nghiệp thiếu mục đích login/reset mật khẩu/thông báo. Evidence: bug-report/bug-report-em-tk.md", "BUG-EM-TK-003"),
    "EM-TK-UI-03": ("Pass", "Form yêu cầu có đúng một ô “Email hoặc Mã số thuế”, required; Gmail thật nhận thư reset tới diupt01+cb-nv-a@gmail.com, link hiệu lực 30 phút mở form có đúng “Mật khẩu mới” và “Xác nhận mật khẩu mới”. Không submit đổi mật khẩu.", ""),
    "EM-TK-UI-04": ("Pass", "", ""),
    "EM-TK-VAL-01": ("Pass", "UI từ chối đúng, báo “Vui lòng nhập email”, giữ nguyên form và không phát sinh request submit.", ""),
    "EM-TK-VAL-02": ("Pass", "UI lưu thành công: POST 201, tổng tài khoản 83→84, email hiển thị đúng; Gmail thật nhận thư kích hoạt, To = diupt01+uat-em-tk-val-02@gmail.com.", ""),
    "EM-TK-VAL-03": ("Pass", "Dấu + được chấp nhận: POST 201, tổng tài khoản 84→85; Gmail thật nhận thư kích hoạt và chi tiết To = diupt01+uat-em-tk-val-03@gmail.com.", ""),
    "EM-TK-VAL-04": ("Pass", "UI từ chối đúng, báo “Email không hợp lệ”, giữ form và tổng tài khoản vẫn 85; không phát sinh request submit.", ""),
    "EM-TK-VAL-05": ("Pass", "UI từ chối đúng chuỗi @example.test, báo “Email không hợp lệ”, giữ nguyên form; tổng tài khoản không đổi ở 86 và không phát sinh request submit.", ""),
    "EM-TK-VAL-06": ("Pass", "UI từ chối đúng chuỗi qa@, báo “Email không hợp lệ”, giữ nguyên form; tổng tài khoản không đổi ở 86 và không phát sinh request submit.", ""),
    "EM-TK-VAL-07": ("Pass", "UI giữ nguyên đúng chuỗi có khoảng trắng, báo “Email không hợp lệ”, giữ form; tổng tài khoản không đổi ở 86 và không phát sinh request submit.", ""),
    "EM-TK-VAL-08": ("Pass", "UI giữ nguyên chuỗi qa@example..test, báo “Email không hợp lệ”, giữ form; tổng tài khoản không đổi ở 86 và không phát sinh request submit.", ""),
    "EM-TK-VAL-09": ("Fail", "BUG-EM-TK-004: POST 409 trả ERR-VAL-VIII-113-02/“Email đã tồn tại trong hệ thống” thay vì ERR-TK-02/“Email '{email}' đã được sử dụng”; UI không hiển thị lỗi. Evidence: bug-report/bug-report-em-tk.md", "BUG-EM-TK-004"),
    "EM-TK-VAL-10": ("Pass", "DN dùng MST mới 0312082697 và email của TVV: POST trả 409 ERR-REG-02, UI hiển thị đúng “Email đã được sử dụng”, form giữ nguyên; Gmail thật không có thư mới tới alias trong 1 giờ gần nhất.", ""),
    "EM-TK-VAL-13": ("Pass", "[Ngoài SRS] Chrome loại CR/LF khỏi input; chuỗi còn lại bị từ chối với “Email không hợp lệ”, form và tổng 86 giữ nguyên, không phát sinh request submit. Gmail thật không có thư mới tới diupt01+uat-em-tk-val-13@gmail.com hoặc diupt01+attacker@gmail.com trong 1 giờ gần nhất.", ""),
}
for case in sum(groups.values(), []):
    result = execution_results.get(case["Test Case ID"])
    if result:
        case["Trạng thái"], case["Ghi chú"], case["Bug ID"] = result
        case["Kết quả thực tế"] = result[1]
        case["Tester / Ngày"] = "QA Automation / 2026-08-12"
    previous = existing_execution_results.get(case["Test Case ID"])
    if previous:
        case.update(previous)

# ---------------------------------------------------------------------------
# OUTPUT MARKDOWN
# ---------------------------------------------------------------------------
def md_escape(v):
    return str(v).replace("|", "\\|").replace("\n", "<br>")

def write_md(filename, title, cases):
    lines = [f"# {title}", "", f"> Nguồn: LOCAL SRS v3.5 — `{SRS}`  ", f"> Ngày tạo: {TODAY}  ",
             "> Quy tắc chạy: chỉ Pass khi kiểm chứng đủ UI/state + API response + inbox dương/âm; kiểm queue/SMTP/audit khi có quyền. Không yêu cầu truy cập DB.",
             "> **Nhãn `[NGOÀI SRS]` ở cột TraceID:** case không có căn cứ trực tiếp trong SRS v3.5; kết quả xấu ghi observation/escalation, không log bug \"sai spec\".", ""]
    cols = ["Test Case ID", "TraceID (Mã SRS)", "Priority", "Type", "Tên Test Case / Mục tiêu", "Tác nhân",
            "Điểm bắt đầu luồng", "Pre-conditions (Tiền đề)", "Test Data (Dữ liệu)", "Các bước thực hiện",
            "Kết quả mong đợi theo bước", "Nguồn địa chỉ nhận", "Expected To / CC", "Mailbox KHÔNG được nhận",
            "UI / API / Queue / SMTP / Audit cần kiểm tra", "Post-condition / Cleanup", "Trạng thái", "Ghi chú"]
    lines += ["| " + " | ".join(cols) + " |", "|" + "|".join(["---"] * len(cols)) + "|"]
    for c in cases:
        lines.append("| " + " | ".join(md_escape(c[x]) for x in cols) + " |")
    (OUT / filename).write_text("\n".join(lines) + "\n", encoding="utf-8")

overview = f"""# Test Plan — Reverify luồng Email PM HTPLDN

> Nguồn: LOCAL SRS v3.5 — `{SRS}`  
> Ngày tạo: {TODAY}

## 1. Đánh giá template

Template `output/template/test-case-template.md` dùng được làm nền vì đã có TraceID, tiền đề, dữ liệu, bước và Expected theo STATE/UI/PERSIST. Bộ email bổ sung các cột: Priority, actor, điểm bắt đầu luồng, nguồn địa chỉ nhận, Expected To/CC, mailbox âm, oracle UI/API/queue/SMTP/audit, cleanup, evidence, trạng thái và Bug ID. Không yêu cầu quyền DB; không Pass chỉ vì nhìn thấy một email trong inbox.

## 2. Cấu trúc bộ test

- `01-TC-email-tai-khoan.md`: validation, cấp/kích hoạt TK, reset, đổi email, 2FA.
- `02-TC-email-doanh-nghiep.md`: email liên hệ, self-registration, các luồng không gửi mail, Claim Flow.
- `03-TC-email-notification-workflow.md`: trigger nghiệp vụ theo từng module/state transition.
- `04-TC-email-smtp-security-nfr.md`: SMTP/TLS, SLA, retry, dedupe, XSS, PII, bulk và isolation.
- `05-traceability-matrix.md`: ánh xạ requirement → testcase.
- `06-test-data-and-environment.md`: dữ liệu/mailbox/fault injection.
- `07-dev-email-account-setup.md`: mapping đã áp dụng trên DEV và đúng các mục còn cần dev xử lý.
- `08-prompt-run-email-test-new-session.md`: prompt master + cách chia batch để chạy ở session mới không vỡ context.
- `UAT-Email-Reverify-Test-Suite.xlsx`: workbook thực thi và ghi kết quả.

## 3. Entry criteria

1. UAT build/deployment version được ghi nhận.
2. Có quyền truy cập UI, API ứng dụng và Gmail thật. Email queue, SMTP log và audit chỉ là oracle bổ sung khi môi trường cho phép.
3. Clock ứng dụng/Gmail/SMTP đồng bộ; các testcase fault-injection chỉ chạy khi có khả năng giả lập thời gian/token và SMTP 4xx/5xx/timeout/bounce.
4. Mapping account/email trong file 07 đã được áp dụng và đọc lại trên DEV. Ba case escalation dùng hồ sơ Bộ/ngành và đối soát recipient theo role `CB_PD_TW` + `don_vi_cha_id`; trước khi chạy phải map mọi tài khoản có thể được resolver chọn sang alias Gmail thật.
5. Phải đăng nhập được hộp thư `diupt01@gmail.com`; mọi OTP và email thông báo DEV được kiểm trực tiếp trong Gmail bằng query `to:<alias>`. Mỗi TC tạo TK/đăng ký/token/claim dùng `PATTERN_TC`, MST riêng hoặc cleanup rõ ràng.

## 4. Quy tắc Pass/Fail/Blocked

- **Pass**: mọi Expected theo bước đều đạt qua UI/API/Gmail; đúng người nhận, đúng chuông nếu SRS yêu cầu in-app, mailbox/tài khoản âm không nhận hoặc không nhìn thấy; không có side effect ngoài dự kiến. Queue/SMTP/audit chỉ đối chiếu khi có quyền.
- **Fail**: ít nhất một expected có căn cứ SRS không đạt, kể cả email đã tới inbox nhưng state, nội dung, recipient, count, audit hoặc SLA sai.
- **Blocked**: SRS chưa chốt tiêu chí hoặc môi trường không cung cấp oracle bắt buộc; tuyệt đối không đổi thành Pass.
- **Not Run**: chưa thực hiện.

## 5. Exit criteria

1. 100% P0 đã Run và Pass; không còn P0 Fail/Blocked, trừ blocker BA được chấp nhận bằng văn bản.
2. 100% requirement trong ma trận có ít nhất một TC và đã Run.
3. Không còn lỗi gửi nhầm, gửi chéo đơn vị, gửi trùng, token dùng lại, PII/XSS hoặc sai nguồn email.
4. Email delivery ≤5 phút; failure/retry/alert đã kiểm chứng.

## 6. SRS blockers không được Pass oan

1. 2FA: BR-AUTH-01 canonical đã được CĐT xác nhận và ghi mã qua email, trong khi FR-VIII-20 vẫn ghi ứng dụng xác thực. Chờ BA sửa nguồn lệch. EM-TK-2FA-01 kiểm bắt buộc có yếu tố thứ hai nhưng không chấm kênh; EM-TK-2FA-02/03/04 chấm hành vi mã/session; build thiếu 2FA là Fail nếu chưa có quyết định BA bằng văn bản. EM-TK-2FA-05 là kiểm tra bảo mật `[NGOÀI SRS]`.
2. QTHT đổi email tài khoản qua FR-VIII-15/SCR-VIII-03 và xem JSON diff trên FR-VIII-28/SCR-VIII-10 đủ đường chạy cho CHG-01..06. Chỉ nhánh self-service của chủ tài khoản chưa có FR/SCR.
3. SCR có hành động gửi lại email kích hoạt và token một lần cho phép chạy lõi EM-TK-ACT-09; số lượng thư, rate-limit và UI message vẫn là observation ngoài SRS.
4. Lịch retry giữa các module chưa thống nhất.
5. Khi chỉ dùng Gmail thật, phải bảo đảm mọi `CB_PD_TW` có thể được resolver escalation chọn đều đã map sang alias nhận được tại `diupt01@gmail.com`.

## 7. Quy ước ID

Các ID `EM-TK-VAL-11`, `EM-TK-VAL-12`, `EM-INF-14`, `EM-INF-16`, `EM-INF-17` không được khai báo trong source generator và hiện không đại diện testcase nào; đây là khoảng ID chưa sử dụng, không phải lỗi sinh thiếu testcase.
"""
(OUT / "00-test-plan-overview.md").write_text(overview, encoding="utf-8")
write_md("01-TC-email-tai-khoan.md", "Test Cases — Email Tài khoản", groups["account"])
write_md("02-TC-email-doanh-nghiep.md", "Test Cases — Email Doanh nghiệp", groups["enterprise"])
write_md("03-TC-email-notification-workflow.md", "Test Cases — Email Notification Workflow", groups["notification"])
write_md("04-TC-email-smtp-security-nfr.md", "Test Cases — SMTP, Security và NFR", groups["infra"])

all_cases = sum(groups.values(), [])
trace = defaultdict(list)
for c in all_cases:
    for r in [x.strip() for x in c["TraceID (Mã SRS)"].split(" / ") if x.strip()]:
        trace[r].append(c["Test Case ID"])
trace_lines = ["# Traceability Matrix — Email", "", "| Requirement/Reference | Test Case IDs | Số TC |", "|---|---|---:|"]
for r, ids in sorted(trace.items()):
    trace_lines.append(f"| {md_escape(r)} | {', '.join(ids)} | {len(ids)} |")
(OUT / "05-traceability-matrix.md").write_text("\n".join(trace_lines) + "\n", encoding="utf-8")

mailbox_md_rows = ["| " + " | ".join(md_escape(v) for v in row) + " |" for row in MAILBOX_ROWS]
data_md = """# Test Data & Environment — Email

## 1. Mailbox thật và alias thực thi

Hộp thư thật duy nhất là `diupt01@gmail.com`. Các địa chỉ có dấu `+` không cần tạo tài khoản hay mật khẩu riêng; Gmail tự chuyển thư của mọi alias vào hộp thư này. Bộ test DEV dùng Gmail thật làm oracle nhận OTP và thông báo; không dùng dịch vụ bắt thư SMTP. Alias đã được preflight bằng thư thật tới `diupt01+check@gmail.com` ngày 2026-08-12.

| Alias/Fixture | Email hoặc pattern | Mục đích | Cách kiểm tra DEV/Gmail | Tách biệt/Ghi chú |
|---|---|---|---|---|
""" + "\n".join(mailbox_md_rows) + """

## 2. Cách chọn email khi chạy TC

1. Khi chạy DEV, chỉ đăng nhập Gmail bằng `MB_PRIMARY`; không đăng nhập từng alias. Tìm thư bằng query `to:<alias>` kết hợp `after:YYYY/MM/DD`, subject và mốc trigger.
2. TC workflow trên actor/record đã setup dùng alias cố định tương ứng: `MB_CB_*`, `MB_TVV_TW`, `MB_TVV_AG`, `MB_CG`, `MB_NHT_*`, `MB_HV_*`, `MB_GV_01`, `MB_ORG_*`.
3. TC tạo tài khoản, tự đăng ký DN, activation/reset token, claim hoặc kiểm unique phải sinh email từ `PATTERN_TC`, thay `{test-case-id}` bằng ID viết thường. Ví dụ `EM-TK-ACT-01` dùng `diupt01+uat-em-tk-act-01@gmail.com`.
4. TC cần phân biệt email TK cũ/mới/DN dùng `MB_TK_OLD`, `MB_TK_NEW`, `MB_DN_CONTACT` hoặc `PATTERN_TC_VARIANT`; tuyệt đối không cho các giá trị giống nhau.
5. Riêng DN tự đăng ký, gán cùng một alias của TC cho `TAI_KHOAN.email` và `DOANH_NGHIEP.email` để kiểm đồng bộ ban đầu.
6. Trước khi trigger, tìm Gmail theo `to:<alias>` và ghi baseline count/thời gian. Sau trigger, tìm lại đúng alias, mở **Show details/Show original** và lưu To/CC, subject, timestamp, message-id đã mask.
7. Mailbox âm cũng được kiểm bằng query `to:<alias>` trong cùng khoảng thời gian. Không kết luận chỉ vì thấy thư trong inbox chung.
8. Không tái sử dụng alias của case tạo TK/token nếu fixture cũ chưa cleanup; TAI_KHOAN.email vẫn phải unique.

## 3. Giới hạn khi dùng một inbox Gmail thật

- `EM-INF-08` cần nhiều recipient logic; với một Gmail phải đối chiếu chính xác trường `To` và SMTP envelope, không chỉ nhìn inbox chung.
- Bounce/4xx/5xx/timeout không dùng Gmail alias; bắt buộc SMTP stub/DSN harness và `MB_BOUNCE`.
- Email xuất hiện trong Gmail chứng minh thư đã được chuyển tới hộp thư thật; với case `in-app`, phải đối chiếu thêm chuông/trang thông báo của đúng tài khoản. Queue/audit chỉ kiểm khi môi trường cho phép; không yêu cầu DB.
- Các alias chung một inbox chỉ chứng minh routing theo địa chỉ To, không chứng minh cách ly vật lý giữa các mailbox.

## 4. Fixture trạng thái và routing đào tạo

- TAI_KHOAN: CHO_KICH_HOAT, HOAT_DONG, TAM_KHOA, VO_HIEU_HOA; email TK khác email DN ở case routing.
- DOANH_NGHIEP: có/không email; có/không TK liên kết; hai DN dùng chung email.
- TVV/NHT: CHO_PHE_DUYET, CHO_KICH_HOAT, HOAT_DONG.
- Hỏi đáp/Vụ việc/TVCS/Đào tạo/Báo cáo: đủ state nguồn của từng transition.
- Cấu hình: email ON/OFF; in-app ON/OFF; lịch/ngày lễ; SMTP success/4xx/5xx/timeout/bounce.
- FR-III-03/19: duyệt/từ chối đăng ký và công bố kết quả dùng `DANG_KY_DAO_TAO.nguoi_dang_ky_id → TAI_KHOAN.email` của DN/NHT. BR-NOTIF-01(5)(6): hủy/bắt đầu khóa gửi `HOC_VIEN.email`; bắt đầu khóa còn gửi `GIANG_VIEN.email`. Không tạo tài khoản riêng cho HV/GV.

## 5. Quy tắc dữ liệu và bằng chứng

1. Mỗi TC dùng MST/username riêng; không tái sử dụng nếu TC kiểm unique/token.
2. Lưu baseline count, event timestamp và message-id trước/sau trigger.
3. Dùng clock cố định cho test 30 phút, 5 phút, ngày làm việc và reminder 24h.
4. Không ghi mật khẩu thật/token đầy đủ vào evidence hoặc file testcase.
5. Nếu ứng dụng từ chối dấu `+`, dừng các case nhận mail và mở defect/blocker môi trường; không tự đổi sang email không tồn tại.
"""
(OUT / "06-test-data-and-environment.md").write_text(data_md, encoding="utf-8")

dev_setup_md_rows = ["| " + " | ".join(md_escape(v) for v in row) + " |" for row in DEV_SETUP_ROWS]
dev_setup_md = """# Dev Setup — Tài khoản, liên kết và email trên DEV

> Hộp thư thật duy nhất: `diupt01@gmail.com`. Tất cả địa chỉ `diupt01+...@gmail.com` tự đổ về hộp thư này, không cần tạo Gmail hay mật khẩu riêng. OTP và email thông báo DEV phải được kiểm trực tiếp trong Gmail thật bằng trường `To`.  
> Căn cứ SRS: `TAI_KHOAN.email` là email duy nhất của tài khoản để nhận kích hoạt/reset/workflow; `DOANH_NGHIEP.email` là email liên hệ và có thể trùng; DN không có tài khoản nhận email-only qua `DOANH_NGHIEP.email`.
> Nguồn kiểm tra: `https://18.143.165.120.nip.io` — đọc trực tiếp API DEV ngày 2026-08-12. Mọi username/ID trong bảng là record thực tế trên DEV.
> Trạng thái: mapping email trong bảng đã được áp dụng và đọc lại. OTP/login đã được kiểm chứng cho các fixture trọng yếu được ghi rõ ở cột cuối.

## Kết quả setup

1. Không cần seed thêm actor bắt buộc: các role/record cần cho luồng email đều đã tồn tại. Một tài khoản TVV thuần được khôi phục và hai tài khoản TVV thuần được reset để đăng nhập test; không tạo record rời không liên kết nghiệp vụ.
2. Mỗi `TAI_KHOAN.email` dùng một plus alias riêng để giữ unique và kiểm chính xác trường `To`; mọi alias cùng đổ về Gmail thật `diupt01@gmail.com`.
3. DN `0109998887` và `0209888006` cố ý tách email tài khoản với email liên hệ DN. DN `0108051801` chỉ có email nghiệp vụ và không có tài khoản. DN `0722072207` giữ email NULL cho negative case.
4. Duyệt/từ chối đăng ký và công bố kết quả đào tạo gửi tới `TAI_KHOAN.email` của DN/NHT đã tạo đăng ký. Riêng hủy/bắt đầu khóa gửi học viên qua `HOC_VIEN.email`; sự kiện bắt đầu còn gửi giảng viên qua `GIANG_VIEN.email`, đúng BR-NOTIF-01.
5. Các dòng `DYNAMIC` do QA tạo trong lúc chạy đúng testcase, không seed trước.

## Phương án setup escalation không cần dev gán recipient cố định

1. Dùng hồ sơ thuộc Bộ KH&ĐT cho `EM-NOT-HDD-04`, `EM-NOT-HDD-07`, `EM-NOT-VV-10`. Theo BR-AUTH-02, Bộ/ngành có `don_vi_cha_id` trỏ trực tiếp tới TW. Trước trigger, đọc lại quan hệ này và danh sách tài khoản hoạt động có role `CB_PD_TW` tại đơn vị cha.
2. Pass recipient khi có ít nhất một email escalation tới tài khoản thỏa đúng role + đơn vị cha, và mọi recipient escalation thực tế đều thỏa điều kiện đó. Không ép hệ thống gửi riêng `cbpd_tw_02`, cũng không ép gửi một hay tất cả vì SRS không quy định cardinality.
3. Do chỉ dùng Gmail thật, trước khi chạy ba case phải map toàn bộ tài khoản `CB_PD_TW` hoạt động mà resolver có thể chọn sang các alias Gmail riêng. Hiện `cbpd_tw_01` và `cbpd_tw_02` đã map; các tài khoản ứng viên còn lại phải được QA cập nhật nếu có quyền, nếu không thì liệt kê cho dev. Nếu không có quyền tạo fixture thời gian/chạy scheduled job thì Blocked riêng do clock/job.

## Danh sách setup

| """ + " | ".join(DEV_SETUP_COLS) + " |\n|" + "|".join(["---"] * len(DEV_SETUP_COLS)) + "|\n" + "\n".join(dev_setup_md_rows) + """

## Nguyên tắc không vượt SRS

Chỉ setup trường/quan hệ cần bởi testcase có trace SRS. Học viên/giảng viên không cần tài khoản đăng nhập riêng; BR-NOTIF-01 vẫn yêu cầu email ở sự kiện hủy/bắt đầu khóa nên dùng email trực tiếp trên entity. Các case kỹ thuật không có căn cứ SRS đã được loại khỏi suite.

## Lưu ý riêng cho alias và username TVV/CG

SRS cho biết username TVV/CG tự sinh từ phần trước `@`, trong khi regex username chỉ cho chữ thường, số và `_`. Plus alias như `diupt01+tvv@gmail.com` có dấu `+`, nên **không dùng plus alias cho testcase đang kiểm việc tự sinh username**. Các tài khoản có sẵn trong bảng giữ nguyên username hiện hữu; chỉ thay trường email. Riêng testcase auto-create cần một địa chỉ có local-part hợp regex và chưa tồn tại trong `TAI_KHOAN`, rồi cleanup sau test. Đây là giới hạn dữ liệu test cần dev biết, không phải yêu cầu tạo thêm Gmail.
"""
(OUT / "07-dev-email-account-setup.md").write_text(dev_setup_md, encoding="utf-8")

gaps = [
    ("GAP-EMAIL-01", "P0", "FR-VIII-20:923 ghi mã TOTP sinh bởi ứng dụng xác thực có phải nội dung chưa cập nhật theo BR-AUTH-01 canonical đã chốt TOTP qua email không", "CHANGELOG-v3-to-v3.5:2459-2464; BR-AUTH-01 srs-v3.5:5582,5596 vs FR-VIII-20 srs-fr-10:923,936", "EM-TK-2FA-01 không chấm kênh; EM-TK-2FA-05 là [NGOÀI SRS]; 02-04 chấm hành vi mã/session"),
    ("GAP-EMAIL-02", "P1", "Có yêu cầu self-service Đổi email cho chủ tài khoản không", "FR-VIII-15/SCR-VIII-03 chỉ đặc tả QTHT sửa", "Nhánh self-service chưa có TC; EM-TK-CHG-01..06 chạy bằng QTHT"),
    ("GAP-EMAIL-03", "P0", "Đổi TU_VAN_VIEN.email có tự đồng bộ sang TAI_KHOAN.email không", "FR-IV-11 chỉ cập nhật TU_VAN_VIEN; BR-AUTH-EMAIL-01 chốt routing qua TAI_KHOAN.email", "EM-FLD-TVV-05; routing vẫn chạy và chấm độc lập"),
    ("GAP-EMAIL-04", "P1", "Số lượng thư, UI message, rate-limit và resend reuse hay thay token cũ", "SCR-VIII-03 nêu hành động; SRS chỉ chốt link kích hoạt dùng một lần, không chốt token mới phải khác token cũ", "EM-TK-ACT-09 — phần này chỉ observation/BA clarification"),
    ("GAP-EMAIL-05", "P1", "Mã SEC-01..SEC-06 bị dùng cho hai bộ yêu cầu khác nhau", "srs-v3.5 §3.5.1 và §4.2.18; trace phải kèm section+dòng", "EM-INF-01 và các TC security dùng SEC code"),
    ("GAP-EMAIL-06", "P1", "Retry policy giữa các module chưa đồng nhất", "BR-EC-11 và ERR-SLA-MAIL-01", "EM-INF-04..05"),
    ("GAP-EMAIL-08", "P0", "TVV/CG auto-username lấy local-part email nhưng regex username không nhận dấu +/./- phổ biến", "TAI_KHOAN.username regex vs luồng auto-create TVV/CG", "EM-TK-ACT-02 và dữ liệu plus alias")
]

# ---------------------------------------------------------------------------
# OUTPUT XLSX
# ---------------------------------------------------------------------------
wb = Workbook()
wb.remove(wb.active)
navy = "17365D"; blue = "4472C4"; light = "D9EAF7"; white = "FFFFFF"
orange = "F4B183"; yellow = "FFF2CC"; green = "E2F0D9"; red = "F4CCCC"; gray = "E7E6E6"
thin = Side(style="thin", color="B7B7B7")

def style_header(ws, row=1):
    for cell in ws[row]:
        cell.fill = PatternFill("solid", fgColor=navy)
        cell.font = Font(name="Arial", bold=True, color=white, size=10)
        cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
        cell.border = Border(left=thin, right=thin, top=thin, bottom=thin)
    ws.row_dimensions[row].height = 48

def base_sheet(ws):
    ws.sheet_view.showGridLines = False
    ws.freeze_panes = "A2"
    ws.auto_filter.ref = ws.dimensions
    ws.sheet_properties.pageSetUpPr.fitToPage = True
    ws.page_setup.fitToWidth = 1
    ws.page_setup.fitToHeight = 0

guide = wb.create_sheet("00_Huong_dan")
guide.append(["UAT EMAIL REVERIFY — HƯỚNG DẪN CHẠY"])
guide.merge_cells("A1:H1")
guide["A1"].fill = PatternFill("solid", fgColor=navy); guide["A1"].font = Font(name="Arial", bold=True, color=white, size=16)
guide["A1"].alignment = Alignment(horizontal="center")
guide_rows = [
    ("Nguồn", f"LOCAL SRS v3.5: {SRS}"), ("Ngày tạo", TODAY),
    ("Nguyên tắc Pass", "Chỉ Pass khi mọi Expected theo bước đạt qua UI/API/Gmail + đúng To/CC + mailbox âm không nhận + chuông đúng nếu SRS yêu cầu in-app; queue/SMTP/audit chỉ kiểm khi có quyền."),
    ("Fail", "Một expected theo SRS không đạt, kể cả email tới inbox nhưng state/count/recipient/content/audit/SLA sai."),
    ("Blocked", "Thiếu BA decision hoặc oracle môi trường; tuyệt đối không đổi thành Pass."),
    ("Trình tự", "1) 00 Hướng dẫn → 2) Test Data → 3) Dev Setup → 4) Tài khoản → 5) Doanh nghiệp → 6) Notification → 7) SMTP/Security/NFR → 8) Traceability/Summary."),
    ("Mailbox DEV", "Dùng duy nhất Gmail thật diupt01@gmail.com để lấy OTP và kiểm thông báo. Tìm đúng alias bằng query to:<alias> + mốc thời gian/subject trong sheet 06_Test_Data."),
    ("Dev setup", "Sheet 07_Dev_Setup ghi mapping đã áp dụng/read-back và đúng mục còn cần dev xử lý. Không seed lại các record đã tồn tại."),
    ("Đăng nhập fixture", "Dev cung cấp mật khẩu/cách đăng nhập và trạng thái 2FA qua kênh bảo mật; không ghi mật khẩu thật vào workbook/evidence."),
    ("Kiểm tra alias", "Trong Gmail query to:<alias>, mở Show details/Show original và đối chiếu To/CC + timestamp/message-id. Không Pass chỉ vì thấy thư trong inbox chung."),
    ("Evidence tối thiểu", "Ảnh UI/chuông + raw email/MIME hoặc message-id + API response; timestamp event/SMTP khi test SLA nếu có quyền."),
    ("Bảo mật", "Không đưa mật khẩu thật hoặc token đầy đủ vào evidence/workbook.")]
for k, v in guide_rows: guide.append([k, v])
for row in guide.iter_rows(min_row=2, max_row=guide.max_row, max_col=2):
    row[0].font = Font(name="Arial", bold=True); row[0].fill = PatternFill("solid", fgColor=light)
    for c in row: c.font = Font(name="Arial", bold=c.column==1); c.alignment = Alignment(vertical="top", wrap_text=True); c.border=Border(left=thin,right=thin,top=thin,bottom=thin)
guide.column_dimensions["A"].width=24; guide.column_dimensions["B"].width=120

summary = wb.create_sheet("01_Tong_hop")
summary.append(["Nhóm", "Tổng TC", "P0", "P1", "Not Run", "Pass", "Fail", "Blocked", "Pass rate (đã run)"])
sheet_map = {"Tài khoản":"02_Tai_khoan", "Doanh nghiệp":"03_Doanh_nghiep", "Notification":"04_Notification", "SMTP/Security/NFR":"05_SMTP_Sec_NFR"}
row_ranges = {}

def add_case_sheet(name, cases):
    ws = wb.create_sheet(name)
    ws.append(COLS)
    for idx, c in enumerate(cases, 1):
        ws.append([idx] + [c.get(col, "") for col in COLS[1:]])
    style_header(ws); base_sheet(ws)
    widths = [6,18,34,20,9,17,38,22,30,38,34,60,65,28,30,34,48,32,36,25,13,16,20,30]
    for i,w in enumerate(widths,1): ws.column_dimensions[get_column_letter(i)].width=w
    for row in ws.iter_rows(min_row=2):
        for c in row:
            c.font=Font(name="Arial",size=9); c.alignment=Alignment(vertical="top",wrap_text=True); c.border=Border(left=thin,right=thin,top=thin,bottom=thin)
        row[4].fill=PatternFill("solid",fgColor=red if row[4].value=="P0" else yellow)
        row[20].fill=PatternFill("solid",fgColor=gray if row[20].value=="Not Run" else (yellow if row[20].value=="Blocked" else white))
    dv=DataValidation(type="list",formula1='"Not Run,Pass,Fail,Blocked"',allow_blank=False)
    ws.add_data_validation(dv); dv.add(f"U2:U{ws.max_row}")
    ws.auto_filter.ref=f"A1:X{ws.max_row}"
    row_ranges[name] = ws.max_row
    return ws

add_case_sheet("02_Tai_khoan", groups["account"])
add_case_sheet("03_Doanh_nghiep", groups["enterprise"])
add_case_sheet("04_Notification", groups["notification"])
add_case_sheet("05_SMTP_Sec_NFR", groups["infra"])

for label, sname in sheet_map.items():
    summary.append([label,
        f"=COUNTA('{sname}'!B2:B{row_ranges[sname]})",
        f'=COUNTIF(\'{sname}\'!E2:E{row_ranges[sname]},"P0")',
        f'=COUNTIF(\'{sname}\'!E2:E{row_ranges[sname]},"P1")',
        f'=COUNTIF(\'{sname}\'!U2:U{row_ranges[sname]},"Not Run")',
        f'=COUNTIF(\'{sname}\'!U2:U{row_ranges[sname]},"Pass")',
        f'=COUNTIF(\'{sname}\'!U2:U{row_ranges[sname]},"Fail")',
        f'=COUNTIF(\'{sname}\'!U2:U{row_ranges[sname]},"Blocked")',
        f'=IFERROR(F{summary.max_row+1}/(F{summary.max_row+1}+G{summary.max_row+1}),0)'])
total_row = summary.max_row + 1
summary.append(["TỔNG", f"=SUM(B2:B{total_row-1})", f"=SUM(C2:C{total_row-1})", f"=SUM(D2:D{total_row-1})",
                f"=SUM(E2:E{total_row-1})", f"=SUM(F2:F{total_row-1})", f"=SUM(G2:G{total_row-1})", f"=SUM(H2:H{total_row-1})",
                f"=IFERROR(F{total_row}/(F{total_row}+G{total_row}),0)"])
style_header(summary); base_sheet(summary)
for row in summary.iter_rows(min_row=2):
    for c in row: c.font=Font(name="Arial",bold=(c.row==total_row)); c.alignment=Alignment(horizontal="center"); c.border=Border(left=thin,right=thin,top=thin,bottom=thin)
for col,w in enumerate([26,12,10,10,12,10,10,12,20],1): summary.column_dimensions[get_column_letter(col)].width=w
for r in range(2,summary.max_row+1): summary.cell(r,9).number_format="0.0%"

td = wb.create_sheet("06_Test_Data")
td.append(["Alias/Fixture", "Email hoặc pattern", "Mục đích", "Cách kiểm tra DEV/Gmail", "Tách biệt/Ghi chú"])
for row in MAILBOX_ROWS:
    td.append(row)
style_header(td); base_sheet(td)
for col,w in enumerate([28,52,52,44,66],1): td.column_dimensions[get_column_letter(col)].width=w
for row in td.iter_rows(min_row=2):
    for c in row: c.font=Font(name="Arial",size=10); c.alignment=Alignment(vertical="top",wrap_text=True); c.border=Border(left=thin,right=thin,top=thin,bottom=thin)
    if row[0].value in {"MB_PRIMARY", "MB_ALIAS_CHECK"}:
        for c in row: c.fill=PatternFill("solid",fgColor=green)
    elif row[0].value == "MB_BOUNCE":
        for c in row: c.fill=PatternFill("solid",fgColor=yellow)

devws = wb.create_sheet("07_Dev_Setup")
devws.append(DEV_SETUP_COLS)
for row in DEV_SETUP_ROWS:
    devws.append(row)
style_header(devws); base_sheet(devws)
for col,w in enumerate([24,34,52,24,58,28,46,56,46,72,52,42],1): devws.column_dimensions[get_column_letter(col)].width=w
for row in devws.iter_rows(min_row=2):
    for c in row: c.font=Font(name="Arial",size=9); c.alignment=Alignment(vertical="top",wrap_text=True); c.border=Border(left=thin,right=thin,top=thin,bottom=thin)
    if row[0].value == "DYNAMIC":
        for c in row: c.fill=PatternFill("solid",fgColor=yellow)
    elif row[0].value == "DEV_ONLY" or "CẦN DEV" in str(row[11].value):
        for c in row: c.fill=PatternFill("solid",fgColor=orange)
    elif row[0].value in {"TAI_KHOAN + DOANH_NGHIEP", "DOANH_NGHIEP"}:
        for c in row: c.fill=PatternFill("solid",fgColor=light)

tr = wb.create_sheet("08_Traceability")
tr.append(["Requirement/Reference", "Test Case IDs", "Số TC"])
for r, ids in sorted(trace.items()): tr.append([r, ", ".join(ids), len(ids)])
style_header(tr); base_sheet(tr); tr.column_dimensions["A"].width=55; tr.column_dimensions["B"].width=110; tr.column_dimensions["C"].width=10
for row in tr.iter_rows(min_row=2):
    for c in row: c.font=Font(name="Arial",size=9); c.alignment=Alignment(vertical="top",wrap_text=True); c.border=Border(left=thin,right=thin,top=thin,bottom=thin)

gapws = wb.create_sheet("09_SRS_Gaps")
gapws.append(["Gap ID","Priority","Nội dung cần BA chốt","Nguồn mâu thuẫn/thiếu","TC bị ảnh hưởng","Quyết định BA","Ngày chốt"])
for row in gaps: gapws.append(list(row)+["",""])
style_header(gapws); base_sheet(gapws)
for col,w in enumerate([16,10,58,38,38,45,15],1): gapws.column_dimensions[get_column_letter(col)].width=w
for row in gapws.iter_rows(min_row=2):
    for c in row: c.font=Font(name="Arial",size=10); c.alignment=Alignment(vertical="top",wrap_text=True); c.border=Border(left=thin,right=thin,top=thin,bottom=thin)
    row[1].fill=PatternFill("solid",fgColor=red if row[1].value=="P0" else yellow)

path = OUT / "UAT-Email-Reverify-Test-Suite.xlsx"
wb.calculation.calcMode = "auto"
wb.calculation.fullCalcOnLoad = True
wb.calculation.forceFullCalc = True
wb.save(path)

# Basic workbook integrity check before external recalculation.
chk = load_workbook(path, data_only=False)
assert chk.sheetnames == ["00_Huong_dan","01_Tong_hop","02_Tai_khoan","03_Doanh_nghiep","04_Notification","05_SMTP_Sec_NFR","06_Test_Data","07_Dev_Setup","08_Traceability","09_SRS_Gaps"]
assert sum(len(v) for v in groups.values()) == sum(row_ranges[s]-1 for s in row_ranges)
print({"account":len(groups["account"]),"enterprise":len(groups["enterprise"]),"notification":len(groups["notification"]),"infra":len(groups["infra"]),"total":len(all_cases),"xlsx":str(path)})
