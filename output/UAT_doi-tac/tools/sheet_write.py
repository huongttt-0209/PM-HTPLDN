#!/usr/bin/env python3
"""
sheet_write.py — Ghi verdict verify vào Google Sheet UAT (CÓ GUARD).

BA CHẾ ĐỘ (--mode), tương ứng các vòng trong QA_VERIFY_PROTOCOL:

  --mode verify1   (MẶC ĐỊNH — vòng đầu, verify bug đối tác gửi, TRƯỚC khi dev fix)
      Ghi ĐÚNG 2 ô: "Trạng thái dev fix 1" (P) + "DEV phản hồi lần 1" (R).
      Verdict: Open / Reject / BA confirm / "" (ô TRỐNG).
      NGOẠI LỆ --status Resolved (thêm 2026-08-03): bug KHÔNG tái hiện nhưng đối tác CÓ bằng
      chứng lỗi thật → ghi 3 ô P="Reject" + Q="Resolved" + R=note, đúng cặp mã hoá ở
      QA_VERIFY_PROTOCOL §Verdict. BẮT BUỘC --evidence là artifact re-verify LIVE (cấm
      Resolved tĩnh dựa trên đọc SRS / xem lại video đối tác).

  --mode qaverdict (thêm 2026-08-03 — verdict QA vòng 1 khi cột P ĐÃ có trạng thái của DEV)
      Ghi ĐÚNG 2 ô: "Verify" (Q) + "DEV phản hồi lần 1" (R). TUYỆT ĐỐI KHÔNG đụng P.
      Verdict: Open / Reject / BA confirm / Resolved / Pass / Reopen / "" (blocked -> chỉ ghi R).

      VÌ SAO CẦN MODE NÀY (đo trên sheet 2026-08-03):
        (a) P là cột trạng thái xử lý của DEV. Trên các dòng dev vừa đụng, dropdown của P là bộ
            từ vựng DEV ['New','Reopent','InProcess','Resoved','Reject','dev done'] — KHÔNG có
            'Open'/'BA confirm'. Ghi verdict QA vào P sẽ (1) bị guard dropdown chặn, hoặc
            (2) XOÁ trạng thái xử lý của dev.
        (b) Chính QA_VERIFY_PROTOCOL §Verdict đã quy ước cặp "P='Reject' (GIỮ NGUYÊN) +
            Verify='Resolved'" — tức khi P đã có giá trị của dev thì QA chỉ set Q. Mode này
            tổng quát hoá đúng quy ước đó cho MỌI verdict, không riêng Resolved.
        Đọc sheet ra: P = dev nói gì · Q = QA soát lại kết luận gì. Hai cột không mâu thuẫn nhau,
        vd P='Reject' (dev bảo không phải bug) + Q='Open' (QA soát lại: đúng là bug) là hợp lệ.

      Guard riêng: Q đang CÓ verdict cũ -> DỪNG (không âm thầm đè kết luận QA lần trước).

  --mode baapply   (thêm 2026-08-04 — BƯỚC 2: áp QUYẾT ĐỊNH CỦA BA lên dòng đang chờ BA)
      Ghi ĐÚNG 3 ô: "Trạng thái dev fix 1" (P) + "Verify" (Q) + "DEV phản hồi lần 1" (R).
      Verdict: Open / Reject. KHÔNG nhận 'BA confirm' (bước này là để GỠ 'BA confirm', không phải đặt lại).

      VÌ SAO CẦN MODE NÀY (QA_BA_APPLY_PROTOCOL §Ghi sheet):
        Bước 2 không phải verify web — nó dịch quyết định BA thành verdict. Dòng đích đang mang
        'BA confirm' ở CẢ P lẫn Q (quy ước tuần 2/3: dropdown sheet không có giá trị "chờ BA" nên
        QA đặt 'BA confirm' vào cả hai). Không mode nào cũ ghi đúng bộ 3 ô đó:
          - verify1  ghi P+R, để Q kẹt ở 'BA confirm' → verdict STALE cạnh P đã đổi.
          - qaverdict ghi Q+R nhưng die() vì Q đang có giá trị.
        Mode này ghi trọn bộ 3 ô trong MỘT batch, kèm 4 guard riêng dưới đây.

      Guard riêng (ngoài 6 guard chung):
        B1. Ô Q phải đang là 'BA confirm' — đó là dấu hiệu dòng thật sự đang chờ BA.
            Khác → DỪNG (dòng không thuộc phạm vi bước 2, ghi vào là đè nhầm kết luận khác).
        B2. Ô P: CHỈ ghi khi giá trị hiện tại == 'BA confirm'. P đang là 'dev done' hay bất kỳ
            giá trị nào khác → GIỮ NGUYÊN, in cảnh báo, chỉ ghi Q+R. P là cột trạng thái xử lý
            của DEV, không phải ô của QA.
        B3. KHÔNG đè dòng đã là BUG: P hoặc Q đang mang 'Open'/'Reopen' → DỪNG. Bước 2 chỉ gỡ
            'BA confirm', tuyệt đối không xoá/ghi đè verdict bug đã chốt.
        B4. Layout note phải khớp verdict:
            --status Open   → note BẮT BUỘC có khối '── CÁCH VERIFY sau Dev fix ──' + đủ 3 dòng
                              'Precondition:' · '✅ PASS khi:' · '❌ FAIL nếu:'. Thiếu → DỪNG.
                              (Không có CÁCH VERIFY thì bước 3 re-verify sẽ tự chế lại tiêu chí → sai.)
            --status Reject → note KHÔNG được có khối CÁCH VERIFY (người đọc là ĐỐI TÁC, và
                              Reject thì không có gì để re-verify). Có → DỪNG.

  --mode verify2   (thêm 2026-07-27 — verify PHẢN ÁNH VÒNG 2 của đối tác)
      Dùng khi đối tác đã test lại và ghi "Trạng thái 2" = Fail (cột U) kèm "Kết quả thực tế
      lần 2" (S) + "Ảnh/video 2" (T). QA xác minh phản ánh vòng 2 đó có đúng không.
      Ghi ĐÚNG 2 ô: "Trạng thái dev fix 2" (W) + "DEV phản hồi lần 2" (Y).
      KHÔNG đụng P/Q/R — đó là lịch sử verdict + phản hồi dev của vòng 1, phải giữ.
      Verdict: Open / Reject / BA confirm / "" (ô TRỐNG) — GIỐNG verify1, vì phản ánh vòng 2
      thường là claim MỚI (lỗi khác vòng 1) nên phải verify lần đầu, không phải re-verify.

  --mode reverify2 (thêm 2026-07-27 — re-verify SAU khi dev claim fix bug của VÒNG 2)
      Đối xứng hoàn toàn với --mode reverify, chỉ khác bộ cột đích: vòng 1 dùng P/Q/R thì
      vòng 2 dùng W/X/Y. Cột "Verify 2" (X) được thêm vào sheet ngày 27/07/2026 đúng để
      chứa kết quả này — trước đó vòng 2 không có ô nào ghi kết quả QA re-verify.
      Verdict: Pass / Reopen / "" (blocked).
        Pass    -> ghi 1 ô:  "Verify 2" (X) = "Pass".  KHÔNG đụng W, KHÔNG đụng Y (giữ note dev).
                   NGOẠI LỆ --pass-ghi-de-note / --pass-khoi-phuc-dev-done: giống mode reverify.
        Reopen  -> ghi 3 ô:  W = "Reopen" (ĐÈ 'dev done') · X = "Reopen" · Y = ĐÈ note mới.
        ""      -> ghi 1 ô:  Y = note lý do blocked. KHÔNG đụng W/X. Bắt buộc --blocker-category.
      Giữ nguyên guard của verify2: dòng phải có "Trạng thái 2" + "Kết quả thực tế lần 2".

  --mode reverify  (re-verify SAU khi dev claim fix; xem §Vòng 2)
      Verdict: Pass / Reopen / "" (blocked).
        Pass    -> ghi 1 ô:  "Verify" (Q) = "Pass".  KHÔNG đụng P, KHÔNG đụng R (giữ note dev).
                   NGOẠI LỆ --pass-ghi-de-note: ghi thêm R. Dùng khi vòng trước QA ra Reopen (nên chính
                   QA đã đè R), giờ Pass mà để nguyên thì R còn note Reopen LỖI THỜI, mâu thuẫn Q=Pass.
        Reopen  -> ghi 3 ô:  P = "Reopen" (ĐÈ 'dev done') · Q = "Reopen" · R = ĐÈ note mới ngắn gọn.
        ""      -> ghi 1 ô:  R = note lý do blocked. KHÔNG đụng P/Q. Bắt buộc --blocker-category.

Guard (mọi lệch → DỪNG, không ghi):
  1. Spreadsheet ID + tên tab phải khớp hằng số hardcode.
  2. Dò cột theo TÊN header ("Trạng thái dev fix 1" / "Verify" / "DEV phản hồi lần 1" / "Mã TC"),
     KHÔNG tin cứng chữ cái — sheet đổi layout vẫn ghi đúng cột.
  3. Ô D{row} (Mã TC) phải == --ma-tc truyền vào.
  4. Giá trị ghi phải NẰM TRONG dropdown (data-validation) của cột đó, nếu cột có dropdown.
     Đọc được validation mà giá trị không thuộc list -> DỪNG (không tự bịa option).
  5. Chỉ set đúng các ô của mode. In old->new cho MỌI ô sắp ghi (kể cả ô sắp bị ĐÈ).
  6. Đọc lại sau ghi để xác nhận == giá trị vừa ghi.

Credential (thử theo thứ tự):
  --sa <service_account.json>  hoặc  env SHEET_SA  -> service account (không cần login lại)
  --token <token.json>         hoặc  env SHEET_TOKEN (default: tools/token.json) -> OAuth authorized_user

Cổng bằng chứng (enforced 2026-07-12 — chống verify hời hợt, xem QA_VERIFY_PROTOCOL §GATE):
  - status là verdict (Open/Reject/BA confirm/Pass/Reopen) -> BẮT BUỘC --evidence <path>: file phải
    tồn tại, KHÔNG rỗng, tên KHÔNG chứa 'partner' (chặn dán frame đối tác làm bằng chứng).
    Ở mode reverify: Pass -> evidence phải bắt thao tác THÀNH CÔNG; Reopen -> bắt thao tác LỖI.
  - status="" (ô TRỐNG / blocked) -> BẮT BUỘC --blocker-category A-F. Nhóm A ("thiếu seed") -> DỪNG
    (thiếu seed không phải blocker nếu flow tạo data tồn tại — phải seed hoặc đổi blocker khách quan).
    Nhóm F ("lý do khác") -> BẮT BUỘC kèm --user-approved (F là hộp mở, dễ bị lạm dụng để né test).

Cổng ĐIỀU KIỆN (enforced 2026-07-12 — chống đóng GAP bằng lập luận, xem §Quy tắc VÀNG + §Nguyên tắc 4):
  - status là verdict -> BẮT BUỘC --condition-table <file.md> chứa Bảng đối chiếu điều kiện đã điền.
    Script parse bảng: còn ô placeholder ('...') hoặc cột GAP không khẳng định "Không" -> DỪNG.
    Lý do: bảng này là thứ chặn lỗi "test bằng vai trò/state KHÁC đối tác rồi kết luận".
    Ở mode reverify, cột giữa là điều kiện của BUG GỐC (bug-report) thay vì của đối tác —
    guard giống hệt: re-test phải đúng vai trò/state/data mà bug gốc mô tả.
  - Bug TĨNH (typo/label/icon/màu — không phụ thuộc role/state/data) -> miễn bảng, nhưng phải khai
    rõ bằng --static-bug "<lý do>". Miễn trừ phải CỐ Ý và có dấu vết, không được im lặng bỏ qua.

Mọi lần ghi thật đều append 1 dòng JSON vào tools/sheet_write.log (dấu vết audit) — GỒM CẢ giá trị CŨ
của mọi ô bị đè, để khôi phục được nếu ghi nhầm.

Usage:
  # vòng 1 (mặc định)
  python3 sheet_write.py --row 2 --ma-tc DKTGKH_07 --status "Reject" --note-file n.txt \
      --evidence img/DKTGKH_07-web.png --condition-table cond/DKTGKH_07.md --dry-run

  # verify phản ánh vòng 2 của đối tác (ghi W + X, không đụng P/Q/R)
  UAT_TAB="UAT_TGPL Doanh Nghiệp-tuần 2" python3 sheet_write.py --mode verify2 --row 3 \
      --ma-tc DKTGKH_12 --status "Open" --note-file n.txt \
      --evidence img/DKTGKH_12-r2-web.png --condition-table cond/DKTGKH_12-r2.md --dry-run

  # re-verify sau dev fix
  python3 sheet_write.py --mode reverify --row 5 --ma-tc TKTVV_08 --status "Pass" \
      --evidence img/TKTVV_08-retest-ok.png --condition-table cond/TKTVV_08.md --dry-run
  python3 sheet_write.py --mode reverify --row 9 --ma-tc QLTVV_21 --status "Reopen" --note-file n.txt \
      --evidence img/QLTVV_21-retest-still-fail.png --condition-table cond/QLTVV_21.md
"""
import argparse, datetime, json, os, re, sys, warnings
warnings.filterwarnings("ignore")

SPREADSHEET_ID = "1OKBN2otlmdZ44THkmhtsn-_63M2Boh7zQwearwjYR3s"
TAB_NAME = "UAT_TGPL Doanh Nghiệp-tuần 3"
# --- Tab override (thêm 2026-07-27 cho đợt tuần 4) ---------------------------
# Guard gốc: TAB_NAME hardcode để không ghi nhầm tab. Đợt tuần 4 cần tab khác ->
# cho override QUA ENV `UAT_TAB` nhưng chỉ chấp nhận tên nằm trong ALLOWED_TABS
# (vẫn là hằng số hardcode). Không set env -> giữ nguyên default.
_ALLOWED_TABS = {
    "UAT_TGPL Doanh Nghiệp-tuần 1",
    "UAT_TGPL Doanh Nghiệp-tuần 2",
    "UAT_TGPL Doanh Nghiệp-tuần 3",
    "UAT_TGPL Doanh Nghiệp-tuần 4",
}
_env_tab = os.environ.get("UAT_TAB", "").strip()
if _env_tab:
    if _env_tab not in _ALLOWED_TABS:
        raise SystemExit(f"\u274c DUNG (guard): UAT_TAB={_env_tab!r} khong nam trong ALLOWED_TABS {_ALLOWED_TABS}")
    TAB_NAME = _env_tab
# -----------------------------------------------------------------------------
COL_STATUS_HEADER = "Trạng thái dev fix 1"   # cột dev-fix status (P)
COL_VERIFY_HEADER = "Verify"                  # cột QA re-verify   (Q)
COL_NOTE_HEADER = "DEV phản hồi lần 1"       # cột note           (R)
COL_STATUS2_HEADER = "Trạng thái dev fix 2"  # cột verdict vòng 2 (W)
COL_VERIFY2_HEADER = "Verify 2"               # cột QA re-verify vòng 2 (X, thêm 2026-07-27)
COL_NOTE2_HEADER = "DEV phản hồi lần 2"      # cột note vòng 2    (Y)
COL_MATC_HEADER = "Mã TC"                     # cột D
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

VERIFY1_STATUSES = {"Open", "Reject", "BA confirm"}
REVERIFY_STATUSES = {"Pass", "Reopen"}
# reverify2 nhận thêm 'BA confirm': re-verify vòng 2 có tình huống mà claim gốc của đối tác ĐÃ hết,
# nhưng "Kết quả mong đợi" của họ đòi thứ KHÔNG có trong SRS (vd bản PDF Báo cáo thống kê: đối tác
# đòi quốc hiệu + khối ký + tên tệp + ký số, trong khi FR-IX chỉ đặc tả A4/Times 13 và header =
# tiêu đề BC + kỳ + đơn vị + ngày tạo). Chấm Pass = lờ đi chỗ lệch; chấm Reopen = đẩy sang dev một
# yêu cầu không có trong đặc tả. Cả hai đều sai → để BA chốt kỳ vọng trước.
REVERIFY2_STATUSES = {"Pass", "Reopen", "BA confirm"}
# Ca đặc biệt CHỈ của mode verify1 (thêm 2026-08-03): bug KHÔNG tái hiện nhưng đối tác CÓ bằng
# chứng (video/ảnh lỗi thật) → QA_VERIFY_PROTOCOL §Verdict quy ước cặp mã hoá P="Reject" +
# Verify="Resolved". Trước đây sheet_write.py không ghi được cặp này nên các đợt cũ phải viết
# script rời (sheet_resoved_write.py...) = mất toàn bộ guard. Nay gộp vào đây để giữ guard.
# KHÔNG mở cho verify2/reverify: verify2 ghi W/Y (chưa có tiền lệ Resolved), reverify đã có Pass.
VERIFY1_RESOLVED = "Resolved"
# mode qaverdict (2026-08-03): QA kết luận gì cũng ghi vào cột Verify (Q), P giữ nguyên của dev.
QAVERDICT_STATUSES = {"Open", "Reject", "BA confirm", "Resolved", "Pass", "Reopen"}
# mode baapply (2026-08-04): áp quyết định BA. CHỈ Open/Reject — mục đích là GỠ 'BA confirm',
# nên nhận lại chính 'BA confirm' là vô nghĩa; 'Pass'/'Reopen' thuộc vòng re-verify sau dev fix.
BAAPPLY_STATUSES = {"Open", "Reject"}
BAAPPLY_MARKER = "BA confirm"            # giá trị đánh dấu dòng đang chờ BA
BAAPPLY_BUG_VERDICTS = {"open", "reopen"}  # dòng đã là BUG → cấm đè (B3)
# Khối bắt buộc trong note khi verdict = Open (B4). Bước 3 re-verify đọc đúng 3 dòng này.
CACH_VERIFY_HEADING = "── CÁCH VERIFY sau Dev fix ──"
CACH_VERIFY_REQUIRED = ("Precondition:", "✅ PASS khi:", "❌ FAIL nếu:")

HERE = os.path.dirname(os.path.abspath(__file__))
AUDIT_LOG = os.path.join(HERE, "sheet_write.log")

# Ô chưa điền — template QA_VERIFY_PROTOCOL để '...' ở cột Đối tác / Mình test.
PLACEHOLDER = {"", "...", "…", ".", "-", "–", "?", "??", "n/a", "na", "tbd", "x"}
# Chỉ chấp nhận khẳng định DƯƠNG là "không còn GAP". Ô trống KHÔNG được coi là 0 GAP —
# phải ghi rõ, để việc "0 GAP" là một khẳng định CÓ Ý THỨC chứ không phải quên điền.
NO_GAP = {"không", "khong", "ko", "no", "none", "0", "✓", "✅", "không có", "khong co"}


def die(msg):
    print(f"❌ DỪNG (guard): {msg}", file=sys.stderr)
    sys.exit(2)


def _norm(s):
    return (s or "").strip().strip("*").strip().lower()


def check_condition_table(path):
    """Parse Bảng đối chiếu điều kiện (§Quy tắc VÀNG). DỪNG nếu chưa điền / còn GAP.

    Đây là guard chống lỗi đắt nhất của quy trình: test bằng vai trò/state KHÁC đối tác
    (vòng 1) hoặc KHÁC bug gốc (vòng 2 re-verify) rồi kết luận.
    Bảng phải chứng minh 0 GAP TRƯỚC khi được ghi verdict.
    """
    if not os.path.exists(path):
        die(f"--condition-table '{path}' không tồn tại.")
    with open(path, encoding="utf-8") as f:
        lines = f.read().splitlines()

    rows = []
    for ln in lines:
        ln = ln.strip()
        if not ln.startswith("|"):
            continue
        cells = [c.strip() for c in ln.strip("|").split("|")]
        if all(set(c) <= set("-: ") for c in cells):      # dòng phân cách ---|---
            continue
        if _norm(cells[0]).startswith("điều kiện"):        # dòng header
            continue
        rows.append(cells)

    if not rows:
        die(f"--condition-table '{path}' không có dòng dữ liệu nào. "
            "Bảng phải có ≥1 dòng điều kiện có khả năng đổi kết quả (vai trò / state / data / input).")

    for cells in rows:
        if len(cells) < 4:
            die(f"Bảng điều kiện sai format ở dòng: {' | '.join(cells)}\n"
                "   Cần đủ 4 cột: Điều kiện | Đối tác (vòng 1) hoặc Bug gốc (vòng 2) | Mình test | GAP?")
        cond, ref, mine, gap = cells[0], cells[1], cells[2], cells[3]
        if _norm(ref) in PLACEHOLDER:
            die(f"Dòng '{cond}': cột tham chiếu CHƯA điền ({ref!r}). "
                "Vòng 1 → trích từ evidence full-res của đối tác. "
                "Vòng 2 → trích từ 'Bước tái hiện' của bug gốc trong bug-report.")
        if _norm(mine) in PLACEHOLDER:
            die(f"Dòng '{cond}': cột 'Mình test' CHƯA điền ({mine!r}). "
                "Phải ghi điều kiện THỰC TẾ bạn đã test.")
        if _norm(gap) not in NO_GAP:
            die(f"Dòng '{cond}': cột GAP = {gap!r} → CHƯA khẳng định 0 GAP.\n"
                "   Còn 1 ô GAP = CHƯA verify xong → CẤM mọi verdict (kể cả ô TRỐNG).\n"
                "   → Đóng GAP: tạo tài khoản / seed / chuyển đúng state rồi TEST LẠI (§Nguyên tắc 4).\n"
                "   → CẤM đóng GAP bằng lập luận kiểu 'màn dùng chung nên vai trò không đổi kết quả'.\n"
                "   Đóng xong ghi 'Không' vào cột GAP rồi chạy lại.")
    print(f"✅ Bảng điều kiện: {len(rows)} dòng, tất cả đã điền + 0 GAP  ({path})")


def check_baapply_note(status, note):
    """Guard B4 — layout note phải khớp verdict của bước 2 (QA_BA_APPLY_PROTOCOL §Layout note).

    Open   : người đọc là DEV → note phải kèm khối CÁCH VERIFY đủ 3 dòng đo được, nếu không
             bước 3 re-verify sẽ tự chế lại tiêu chí PASS/FAIL và chấm sai.
    Reject : người đọc là ĐỐI TÁC → không có gì để re-verify, kèm khối CÁCH VERIFY là sai layout
             (và lộ jargon nội bộ ra phía đối tác).
    """
    note = note or ""
    has_heading = CACH_VERIFY_HEADING in note
    if status == "Open":
        if not has_heading:
            die("--status Open nhưng note THIẾU khối "
                f"'{CACH_VERIFY_HEADING}'.\n"
                "   Bước 3 re-verify đọc khối này để biết chấm PASS/FAIL theo tiêu chí nào.\n"
                "   Thiếu → người re-verify tự chế tiêu chí → chấm sai. Bổ sung rồi chạy lại.")
        missing = [k for k in CACH_VERIFY_REQUIRED if k not in note]
        if missing:
            die(f"--status Open: khối CÁCH VERIFY thiếu dòng bắt buộc {missing}.\n"
                f"   Phải có đủ: {list(CACH_VERIFY_REQUIRED)}.\n"
                "   'PASS khi' phải ĐO ĐƯỢC (cấm 'kiểm tra kết quả đúng' / 'hiển thị hợp lý').")
    elif status == "Reject":
        if has_heading:
            die(f"--status Reject nhưng note CÓ khối '{CACH_VERIFY_HEADING}' → sai layout.\n"
                "   Reject = không phải bug, dev không sửa gì, nên không có gì để re-verify.\n"
                "   Note Reject viết cho ĐỐI TÁC: chỉ UC + mô tả bằng lời, bỏ khối CÁCH VERIFY.")


def check_gates(args):
    """Cổng bằng chứng + cổng điều kiện — chạy TRƯỚC khi mở sheet (fail-fast, không tốn network)."""
    status = (args.status or "").strip()

    # Từ vựng verdict phải khớp mode. Chặn cả typo ('open', 'BA Confirm') lẫn nhầm vòng —
    # KHÔNG dựa vào guard dropdown để bắt hộ, vì dropdown có thể không tồn tại trên cột.
    # verify2 dùng CHUNG từ vựng với verify1 (Open/Reject/BA confirm): phản ánh vòng 2 của đối tác
    # phần lớn là claim MỚI → verify lần đầu, không phải Pass/Reopen của re-verify sau dev fix.
    if args.mode == "qaverdict":
        allowed = set(QAVERDICT_STATUSES)
    elif args.mode == "baapply":
        allowed = set(BAAPPLY_STATUSES)
        if status == "":
            die("--mode baapply KHÔNG nhận status='' (ô TRỐNG). Bước 2 áp QUYẾT ĐỊNH của BA nên "
                "luôn có kết luận.\n"
                "   BA chưa đủ rõ để viết được CÁCH VERIFY → DỪNG, hỏi user (protocol §2), "
                "đừng ghi ô trống đè lên 'BA confirm'.")
    elif args.mode == "reverify2":
        allowed = set(REVERIFY2_STATUSES)
    elif args.mode == "reverify":
        allowed = set(REVERIFY_STATUSES)
    else:
        allowed = set(VERIFY1_STATUSES)
        if args.mode == "verify1":
            allowed = allowed | {VERIFY1_RESOLVED}
    # Hỗ trợ ĐA-TRẠNG THÁI (dropdown multi-select), vd "Open, BA confirm" — tách theo dấu phẩy,
    # MỖI phần phải là một verdict hợp lệ của mode. Không verdict nào chứa dấu phẩy → tách an toàn.
    status_parts = [p.strip() for p in status.split(",") if p.strip()]
    if status != "":
        bad = [p for p in status_parts if p not in allowed]
        if bad:
            other = VERIFY1_STATUSES if args.mode in ("reverify", "reverify2") else REVERIFY_STATUSES
            wrong_mode = [p for p in bad if p in other]
            extra = (f"\n   {wrong_mode} là verdict của mode kia → đổi --mode."
                     if wrong_mode else
                     "\n   Phân biệt HOA/thường + dấu cách: phải khớp CHÍNH XÁC.")
            die(f"--mode {args.mode} chỉ nhận --status là (tổ hợp) {sorted(allowed)} "
                f"hoặc '' (blocked). Phần không hợp lệ: {bad}.{extra}")
        # 'Resolved' KHÔNG ghép được với verdict khác: nó đã hàm ý P='Reject' rồi, ghép
        # 'Open, Resolved' là tự mâu thuẫn (vừa là bug vừa không tái hiện).
        if VERIFY1_RESOLVED in status_parts and len(status_parts) > 1:
            die(f"--status '{status}': '{VERIFY1_RESOLVED}' phải đứng MỘT MÌNH.\n"
                "   Nó đã hàm ý P='Reject' + Verify='Resolved'; ghép verdict khác là tự mâu thuẫn.")

    if status == "":
        cat = (args.blocker_category or "").strip().upper()
        if not cat:
            die("status='' (ô TRỐNG / blocked) → BẮT BUỘC --blocker-category A-F "
                "(A=thiếu seed · B=chờ dev fix · C=chờ BA · D=env/infra · E=dep upstream · F=lý do khác).")
        if cat not in ("A", "B", "C", "D", "E", "F"):
            die(f"--blocker-category='{cat}' không hợp lệ. Chỉ nhận A-F.")
        if cat == "A":
            die("Blocker nhóm A = 'thiếu seed data' KHÔNG hợp lệ nếu flow tạo data tồn tại. "
                "→ SEED tới đúng state rồi verify (QA_VERIFY_PROTOCOL §GATE), "
                "hoặc đổi sang blocker khách quan (B/C/D/E) nếu thật sự bị chặn.")
        if cat == "F" and not args.user_approved:
            die("Blocker nhóm F ('lý do khác') là HỘP MỞ — dễ bị lạm dụng để né bước test đắt.\n"
                "   → Phải HỎI USER và được đồng ý trước, rồi chạy lại kèm --user-approved.\n"
                "   Nếu thực chất là thiếu tài khoản/data/state → KHÔNG phải F, phải TỰ TẠO (§Nguyên tắc 4).")
        return

    # --- mode baapply: cổng riêng, KHÔNG dùng cổng bằng chứng/điều kiện của các mode verify ---
    # Bước 2 KHÔNG test lại web (QA_BA_APPLY_PROTOCOL, đầu đề): đầu vào là QUYẾT ĐỊNH CỦA BA,
    # không phải quan sát UI. Bắt --evidence ở đây sẽ ép người chạy đi chụp một ảnh không liên
    # quan chỉ để qua guard — guard mất tác dụng mà còn tạo bằng chứng giả. Thứ phải truy vết
    # được là "quyết định này lấy từ đâu" → --ba-source.
    if args.mode == "baapply":
        src = args.ba_source
        if not src:
            die("--mode baapply → BẮT BUỘC --ba-source <file BA phản hồi>.\n"
                "   Phải là file BA TRẢ LỜI (phan-hoi-ba-*.md / ba-response-*.md / phiếu phản hồi),\n"
                "   KHÔNG phải file QA đi hỏi (ba-confirmation-needed-*.md) — nhầm 2 loại file này "
                "là cập nhật sai toàn bộ (protocol §Phân biệt 2 loại file).")
        if not os.path.exists(src):
            die(f"--ba-source '{src}' không tồn tại.")
        if os.path.getsize(src) == 0:
            die(f"--ba-source '{src}' RỖNG (0 byte).")
        base = os.path.basename(src).lower()
        if "confirmation-needed" in base or "ba-confirm-needed" in base:
            die(f"--ba-source '{os.path.basename(src)}' là file QA ĐI HỎI BA, không phải BA TRẢ LỜI.\n"
                "   File đó chỉ chứa câu hỏi → không có quyết định nào để áp.\n"
                "   → Trỏ vào phiếu phản hồi của BA (vd phan-hoi-cac-diem-cho-BA-chot-<ngày>.md).")
        print(f"✅ Nguồn quyết định BA: {src}")
        if args.condition_table:
            print("ℹ️  --condition-table bị bỏ qua ở mode baapply (bước 2 không đo lại web).")
        return

    # --- status là verdict (Open / Reject / BA confirm / Pass / Reopen) ---
    ev = args.evidence
    if not ev:
        hint = ("Pass → ảnh/log thao tác THÀNH CÔNG. Reopen → ảnh/log thao tác LỖI (toast/4xx/5xx)."
                if args.mode in ("reverify", "reverify2") else
                "ảnh/log của CHÍNH thao tác/hiển thị đã tự verify trên data thật, không phải frame đối tác.")
        die(f"status='{status}' (verdict) → BẮT BUỘC --evidence <path> ({hint})")
    if not os.path.exists(ev):
        die(f"--evidence '{ev}' không tồn tại. Phải là file artifact THẬT đã chụp/log.")
    if os.path.getsize(ev) == 0:
        die(f"--evidence '{ev}' RỖNG (0 byte). Screenshot/log hỏng → chụp lại rồi chạy lại.")
    if "partner" in os.path.basename(ev).lower():
        die(f"--evidence '{os.path.basename(ev)}' trông như frame ĐỐI TÁC (tên chứa 'partner'). "
            "Evidence phải là quan sát WEB của CHÍNH BẠN trên data đã seed. "
            "Nếu đây thật sự là ảnh web bạn tự chụp, đổi tên bỏ chữ 'partner'.")

    if args.condition_table:
        check_condition_table(args.condition_table)
    elif args.static_bug:
        if len(args.static_bug.strip()) < 10:
            die("--static-bug cần LÝ DO cụ thể (≥10 ký tự), vd: "
                '--static-bug "thiếu icon sắp xếp — không phụ thuộc role/state/data".')
        print(f"⚠️  Miễn bảng điều kiện — khai bug TĨNH: {args.static_bug.strip()}")
        print("   (Nếu bug thực ra phụ thuộc vai trò/state/data → khai sai, verdict sẽ không đáng tin.)")
    else:
        die(f"status='{status}' (verdict) → BẮT BUỘC --condition-table <file.md> "
            "(Bảng đối chiếu điều kiện đã điền, 0 GAP — §Quy tắc VÀNG).\n"
            "   Bảng chặn lỗi: test bằng vai trò/state KHÁC đối tác (vòng 1) / KHÁC bug gốc (vòng 2).\n"
            "   Bug TĨNH (typo/label/icon/màu — không phụ thuộc role/state/data) → dùng "
            '--static-bug "<lý do>" để miễn bảng.')


def audit(args, writes, ok):
    """Append-only trail — mỗi lần ghi thật để lại dấu vết, đối soát được về sau.

    `writes` = list dict {cell, header, old, new} — GIỮ CẢ giá trị CŨ để khôi phục nếu ghi nhầm.
    """
    try:
        with open(AUDIT_LOG, "a", encoding="utf-8") as f:
            f.write(json.dumps({
                "ts": datetime.datetime.now().isoformat(timespec="seconds"),
                "tab": TAB_NAME,
                "mode": args.mode,
                "row": args.row, "ma_tc": args.ma_tc, "status": args.status,
                "evidence": args.evidence, "condition_table": args.condition_table,
                "static_bug": args.static_bug, "blocker_category": args.blocker_category,
                "user_approved": bool(args.user_approved),
                "writes": writes, "ok": ok,
            }, ensure_ascii=False) + "\n")
    except Exception as e:
        print(f"⚠️  Không ghi được audit log: {e}", file=sys.stderr)


def get_client(args):
    import gspread
    sa = args.sa or os.environ.get("SHEET_SA")
    if sa and os.path.exists(sa):
        print(f"🔑 Dùng service account: {sa}")
        return gspread.service_account(filename=sa, scopes=SCOPES)
    token = args.token or os.environ.get("SHEET_TOKEN") or os.path.join(HERE, "token.json")
    if os.path.exists(token):
        from google.oauth2.credentials import Credentials
        from google.auth.transport.requests import Request
        print(f"🔑 Dùng OAuth token: {token}")
        creds = Credentials.from_authorized_user_file(token, SCOPES)
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
            with open(token, "w") as f:
                f.write(creds.to_json())
        return gspread.authorize(creds)
    die(f"Không có credential. Cần service account (--sa) hoặc OAuth token ({token}). "
        f"Chạy tools/sheet_auth.py để tạo token.json.")


def col_index(header_row, name):
    for i, v in enumerate(header_row):
        if (v or "").strip() == name:
            return i  # 0-based
    return -1


def a1(col0, row):
    # col0 0-based -> letters
    n = col0 + 1
    s = ""
    while n:
        n, r = divmod(n - 1, 26)
        s = chr(65 + r) + s
    return f"{s}{row}"


def dropdown_options(sh, cell_a1, header):
    """Đọc data-validation của 1 ô.

    Trả `None` CHỈ khi xác nhận được là ô KHÔNG có dropdown ONE_OF_LIST (hợp lệ → bỏ qua guard).
    Gọi API lỗi / metadata đổi shape → DỪNG. Không được nuốt exception rồi bỏ qua guard:
    "không đọc được" != "không có dropdown", gộp 2 cái là cách guard bị vô hiệu hoá âm thầm.
    """
    try:
        meta = sh.fetch_sheet_metadata({
            "ranges": [f"'{TAB_NAME}'!{cell_a1}"],
            "includeGridData": True,
            "fields": "sheets(data(rowData(values(dataValidation))))",
        })
    except Exception as e:
        die(f"[{cell_a1}] '{header}': gọi API đọc data-validation LỖI ({type(e).__name__}: {str(e)[:120]}).\n"
            "   Guard dropdown KHÔNG được bỏ qua vì lỗi API → chạy lại, hoặc kiểm tra quyền/scope của token.")

    try:
        data = (meta.get("sheets") or [{}])[0].get("data") or [{}]
        rows = data[0].get("rowData") or []
        if not rows:                                   # ô ngoài vùng có format → coi như không có validation
            return None
        cells = rows[0].get("values") or []
        if not cells:
            return None
        dv = cells[0].get("dataValidation")
        if not dv:                                     # ô không đặt validation → hợp lệ
            return None
        cond = dv.get("condition") or {}
        if cond.get("type") != "ONE_OF_LIST":          # validation kiểu khác (số, ngày...) → không phải dropdown
            return None
        return [v.get("userEnteredValue", "") for v in cond.get("values", [])]
    except Exception as e:
        die(f"[{cell_a1}] '{header}': parse data-validation LỖI ({type(e).__name__}: {e}).\n"
            "   Shape metadata đã đổi → sửa dropdown_options(), KHÔNG bỏ qua guard.")


def check_dropdown(sh, cell_a1, header, value):
    """Guard 4 — giá trị ghi phải thuộc dropdown của cột (nếu cột có dropdown)."""
    if value == "":
        return
    opts = dropdown_options(sh, cell_a1, header)
    if opts is None:
        print(f"ℹ️  [{cell_a1}] '{header}': cột không có dropdown → guard 4 không áp dụng "
              "(từ vựng verdict đã được chặn ở check_gates).")
        return
    # ĐA-TRẠNG THÁI: cell multi-select lưu dạng "A, B" — MỖI phần phải thuộc dropdown của cột.
    value_parts = [p.strip() for p in value.split(",") if p.strip()]
    bad = [p for p in value_parts if p not in opts]
    if bad:
        die(f"[{cell_a1}] '{header}': giá trị {bad} KHÔNG nằm trong dropdown của cột.\n"
            f"   Option hợp lệ: {opts}\n"
            "   → CẤM tự bịa giá trị ngoài dropdown. Hỏi user chọn option đúng, hoặc nhờ owner sheet thêm option.")
    print(f"✅ [{cell_a1}] '{header}': '{value}' — mọi phần thuộc dropdown {opts}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--mode", choices=["verify1", "qaverdict", "baapply", "verify2", "reverify", "reverify2"], default="verify1",
                    help="baapply = BƯỚC 2 áp quyết định BA lên dòng 'BA confirm', ghi P+Q+R (Open/Reject) · "
                         "qaverdict = verdict QA vòng 1 khi P đã có trạng thái dev, ghi Q+R, KHÔNG đụng P · "
                         "verify1 = vòng đầu, ghi P+R (Open/Reject/BA confirm) · "
                         "verify2 = verify phản ánh vòng 2 của đối tác, ghi W+Y (Open/Reject/BA confirm) · "
                         "reverify = sau dev fix vòng 1, ghi Q(+P,R) (Pass/Reopen) · "
                         "reverify2 = sau dev fix vòng 2, ghi X(+W,Y) (Pass/Reopen)")
    ap.add_argument("--row", type=int, required=True, help="Số dòng trên sheet (1-based, gồm header)")
    ap.add_argument("--ma-tc", required=True, help="Mã TC kỳ vọng ở cột D{row}")
    ap.add_argument("--status", required=True,
                    help='verify1: Open / Reject / BA confirm / Resolved / ""  ·  reverify: Pass / Reopen / ""')
    ap.add_argument("--ba-source", help="Path file BA PHẢN HỒI (không phải file QA đi hỏi) — BẮT BUỘC khi --mode baapply")
    ap.add_argument("--evidence", help="Path artifact quan sát (ảnh/log) — BẮT BUỘC khi status là verdict")
    ap.add_argument("--condition-table", help="Path file .md chứa Bảng đối chiếu điều kiện đã điền, 0 GAP — BẮT BUỘC khi status là verdict")
    ap.add_argument("--static-bug", help='Miễn --condition-table cho bug TĨNH. Phải nêu lý do, vd: "thiếu icon sắp xếp — không phụ thuộc role/state"')
    ap.add_argument("--blocker-category", help="A-F — BẮT BUỘC khi status='' (ô TRỐNG). A=thiếu seed (invalid nếu seed được)")
    ap.add_argument("--user-approved", action="store_true", help="Xác nhận đã hỏi user — BẮT BUỘC khi --blocker-category F")
    ap.add_argument("--note", help="Note cột DEV phản hồi lần 1 (có \\n)")
    ap.add_argument("--note-file", help="Đường dẫn file chứa note (ưu tiên hơn --note; giữ nguyên xuống dòng)")
    ap.add_argument("--pass-ghi-de-note", action="store_true",
                    help="CHỈ dùng với reverify+Pass: cho phép ĐÈ cột note. Mặc định Pass không đụng note vì "
                         "cột đó thường giữ phản hồi của DEV. Nhưng nếu vòng trước QA ra Reopen thì chính QA đã "
                         "đè note đó rồi → Pass mà không sửa sẽ để lại note Reopen LỖI THỜI mâu thuẫn với "
                         "Verify=Pass. Cờ này bắt khai báo CÓ Ý THỨC + vẫn phải kèm --note/--note-file.")
    ap.add_argument("--pass-khoi-phuc-dev-done", action="store_true",
                    help="CHỈ dùng với reverify+Pass: ghi lại cột 'Trạng thái dev fix 1' (P) = 'dev done'. "
                         "Dùng khi vòng trước QA đã ghi P='Reopen' NHƯNG nay xác định kết luận Reopen đó SAI "
                         "(vd lỗi phép đo của QA). Không có cờ này, P sẽ kẹt ở 'Reopen' cạnh Verify='Pass' → "
                         "sheet tự mâu thuẫn. Bắt khai báo CÓ Ý THỨC + buộc kèm --pass-ghi-de-note để note "
                         "cũng phải nói rõ vì sao thu hồi.")
    ap.add_argument("--vong2-do-dev-build", metavar="LYDO",
                    help="CHỈ dùng với verify2/reverify2: nới guard 'đối tác phải phản ánh vòng 2 trước'. "
                         "Dùng khi vòng 2 do DEV khởi xướng (dev build lên môi trường mới rồi nhờ QA verify "
                         "lại), nên cột 'Trạng thái 2' / 'Kết quả thực tế lần 2' của đối tác trống là ĐÚNG "
                         "bản chất chứ không phải thiếu dữ liệu. PHẢI ghi lý do bằng chữ; lý do được in ra "
                         "màn hình để người duyệt dry-run nhìn thấy guard đã được nới và vì sao.")
    ap.add_argument("--sa", help="service_account.json")
    ap.add_argument("--token", help="OAuth token.json")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    status = (args.status or "").strip()
    # reverify/reverify2 + Pass: KHÔNG đụng cột note (giữ nguyên phản hồi dev) → note không cần thiết.
    # Ngoại lệ: --pass-ghi-de-note (khai báo có ý thức) → vẫn bắt buộc có note.
    is_reverify_pass = args.mode in ("reverify", "reverify2") and status == "Pass"
    pass_ghi_note = is_reverify_pass and args.pass_ghi_de_note
    note_needed = not is_reverify_pass or pass_ghi_note

    if args.pass_ghi_de_note and not is_reverify_pass:
        die("--pass-ghi-de-note chỉ dùng được với --mode reverify/reverify2 + --status Pass.")

    pass_khoi_phuc_p = is_reverify_pass and args.pass_khoi_phuc_dev_done
    if args.pass_khoi_phuc_dev_done:
        if not is_reverify_pass:
            die("--pass-khoi-phuc-dev-done chỉ dùng được với --mode reverify/reverify2 + --status Pass.")
        if not args.pass_ghi_de_note:
            die("--pass-khoi-phuc-dev-done phải đi kèm --pass-ghi-de-note: đã thu hồi Reopen thì note "
                "BẮT BUỘC phải nói rõ vì sao, không được để note Reopen cũ.")

    note = None
    if args.note_file:
        with open(args.note_file, encoding="utf-8") as f:
            note = f.read().rstrip("\n")
    elif args.note is not None:
        note = args.note.replace("\\n", "\n")
    elif note_needed:
        die("Thiếu --note hoặc --note-file")

    if not note_needed and note is not None:
        print(f"ℹ️  mode={args.mode} + status=Pass → KHÔNG ghi cột note (giữ nguyên phản hồi dev). --note bị bỏ qua.")
        note = None
    if pass_ghi_note:
        print("⚠️  --pass-ghi-de-note: Pass NHƯNG VẪN ĐÈ cột note (khai báo có ý thức).")
    if pass_khoi_phuc_p:
        _col = "W" if args.mode == "reverify2" else "P"
        print(f"⚠️  --pass-khoi-phuc-dev-done: THU HỒI Reopen — ghi lại cột {_col} = 'dev done'.")

    # Cổng bằng chứng + cổng điều kiện (áp mọi case) — chặn trước khi mở sheet
    check_gates(args)
    if args.mode == "baapply":
        check_baapply_note(status, note)          # B4 — layout note phải khớp verdict

    gc = get_client(args)
    try:
        sh = gc.open_by_key(SPREADSHEET_ID)
    except Exception as e:
        die(f"Mở spreadsheet lỗi: {type(e).__name__}: {str(e)[:200]}")

    # Guard 1: tab
    titles = [w.title for w in sh.worksheets()]
    if TAB_NAME not in titles:
        die(f"Không thấy tab '{TAB_NAME}'. Có: {titles}")
    ws = sh.worksheet(TAB_NAME)

    header = ws.row_values(1)
    ci_status = col_index(header, COL_STATUS_HEADER)
    ci_verify = col_index(header, COL_VERIFY_HEADER)
    ci_note = col_index(header, COL_NOTE_HEADER)
    ci_status2 = col_index(header, COL_STATUS2_HEADER)
    ci_verify2 = col_index(header, COL_VERIFY2_HEADER)
    ci_note2 = col_index(header, COL_NOTE2_HEADER)
    ci_matc = col_index(header, COL_MATC_HEADER)
    # Guard 2: header names
    if ci_status < 0:
        die(f"Không tìm thấy cột header '{COL_STATUS_HEADER}'. Header: {header}")
    if ci_note < 0:
        die(f"Không tìm thấy cột header '{COL_NOTE_HEADER}'. Header: {header}")
    if ci_matc < 0:
        die(f"Không tìm thấy cột header '{COL_MATC_HEADER}'. Header: {header}")
    if args.mode in ("reverify", "baapply") and ci_verify < 0:
        die(f"mode={args.mode} cần cột header '{COL_VERIFY_HEADER}' nhưng không thấy. Header: {header}")
    if args.mode in ("verify2", "reverify2"):
        if ci_status2 < 0:
            die(f"mode={args.mode} cần cột header '{COL_STATUS2_HEADER}' nhưng không thấy. Header: {header}")
        if ci_note2 < 0:
            die(f"mode={args.mode} cần cột header '{COL_NOTE2_HEADER}' nhưng không thấy. Header: {header}")
    if args.mode == "reverify2" and ci_verify2 < 0:
        die(f"mode=reverify2 cần cột header '{COL_VERIFY2_HEADER}' nhưng không thấy. Header: {header}\n"
            "   Cột này chứa kết quả QA re-verify của VÒNG 2 (đối xứng với cột 'Verify' của vòng 1).\n"
            "   Sheet chưa có cột → thêm cột rồi chạy lại, KHÔNG ghi đè cột khác.")

    # Guard 3: D{row} == ma_tc
    cell_matc = ws.cell(args.row, ci_matc + 1).value or ""
    if cell_matc.strip() != args.ma_tc.strip():
        die(f"Mã TC dòng {args.row} = '{cell_matc}' != kỳ vọng '{args.ma_tc}'. Sai dòng → không ghi.")

    def read(ci):
        return ws.cell(args.row, ci + 1).value or ""

    def guard_co_claim_vong2():
        """Chỉ ghi được lên dòng mà ĐỐI TÁC thật sự đã phản ánh vòng 2.
        Không có claim vòng 2 mà vẫn ghi verdict vòng 2 = bịa kết luận cho một ô đối tác bỏ trống.

        Claim vòng 2 được chấp nhận ở MỘT trong hai chỗ:
          (a) Bộ cột vòng 2 chuẩn của đối tác: 'Trạng thái 2' (U) + 'Kết quả thực tế lần 2' (S).
          (b) Marker reopen được sync THẲNG vào 'DEV phản hồi lần 1' (R) — dạng
              "[Lý do reopen] TKM retest <ngày>: ...". Đợt reopen 31/07/2026 (53 dòng tuần 2+3)
              đi theo đường này: người sync từ sheet đối tác ghi nối vào R, để trống S/U/V.
              Bắt buộc U/S thì guard sẽ chặn đúng 100% dòng có claim thật → sai bản chất.
        Không có (a) lẫn (b) mới thật sự là "đối tác chưa phản ánh vòng 2" → DỪNG.
        """
        # NGOẠI LỆ (2026-08-04): vòng 2 do DEV khởi xướng — dev build lên môi trường UAT mới rồi
        # nhờ QA verify lại, đối tác CHƯA phản ánh gì. Khi đó S/U trống là đúng bản chất, không
        # phải "thiếu claim". Vẫn bắt khai báo lý do bằng chữ + in ra để người duyệt dry-run thấy.
        if getattr(args, "vong2_do_dev_build", None):
            print("ℹ️  Nới guard claim-vòng-2 theo --vong2-do-dev-build: "
                  f"{args.vong2_do_dev_build!r}")
            return
        ci_tt2 = col_index(header, "Trạng thái 2")
        ci_kq2 = col_index(header, "Kết quả thực tế lần 2")
        if ci_tt2 < 0 or ci_kq2 < 0:
            die(f"mode={args.mode} cần cột 'Trạng thái 2' + 'Kết quả thực tế lần 2' của đối tác "
                f"nhưng không thấy. Header: {header}")
        if read(ci_tt2).strip() and read(ci_kq2).strip():
            return                                            # (a) đường chuẩn
        note_r = read(ci_note) if ci_note >= 0 else ""
        if re.search(r"\[Lý do reopen\]|TKM\s+retest", note_r, re.IGNORECASE):
            marker = re.search(r"\[Lý do reopen\][^\n]{0,120}|TKM\s+retest[^\n]{0,110}", note_r, re.IGNORECASE)
            print(f"ℹ️  Claim vòng 2 lấy từ 'DEV phản hồi lần 1' (S/U trống): "
                  f"{marker.group(0).strip()[:130]!r}")
            return                                            # (b) đường sync-vào-R
        if not read(ci_tt2).strip():
            die(f"Dòng {args.row}: cột 'Trạng thái 2' TRỐNG và 'DEV phản hồi lần 1' cũng không có "
                "marker reopen ('[Lý do reopen]' / 'TKM retest') → đối tác chưa test lại vòng 2. "
                "Không có claim vòng 2 thì không được ghi verdict vòng 2.")
        die(f"Dòng {args.row}: cột 'Kết quả thực tế lần 2' TRỐNG → không có nội dung phản ánh "
            "để verify. Đối tác phải mô tả lỗi vòng 2 trước.")

    # --- Xác định CHÍNH XÁC những ô sẽ ghi, theo mode + status ---
    plan = []  # [(col_index, header, new_value)]
    if args.mode == "baapply":
        old_p, old_q = read(ci_status), read(ci_verify)

        # B3 — dòng đã là BUG thì tuyệt đối không đè. Đặt TRƯỚC B1 để thông báo đúng bản chất
        # (dòng 'Open' cũng trượt B1, nhưng lý do thật là "đã là bug", không phải "không chờ BA").
        bug_hits = [f"{h}='{v}'" for h, v in ((COL_STATUS_HEADER, old_p), (COL_VERIFY_HEADER, old_q))
                    if v.strip().lower() in BAAPPLY_BUG_VERDICTS]
        if bug_hits:
            die(f"Dòng {args.row} ĐÃ là BUG ({' · '.join(bug_hits)}) → mode baapply KHÔNG đè.\n"
                "   Bước 2 chỉ gỡ nhãn 'BA confirm'. Verdict bug đã chốt là kết luận có hiệu lực.\n"
                "   → Muốn đổi verdict bug: dùng --mode reverify (Pass/Reopen) sau khi dev fix.")

        # B1 — Q phải đang là 'BA confirm': đó là dấu hiệu dòng thật sự đang chờ BA.
        if old_q.strip() != BAAPPLY_MARKER:
            die(f"[Q{args.row}] '{COL_VERIFY_HEADER}' đang là '{old_q}', không phải "
                f"'{BAAPPLY_MARKER}' → dòng này KHÔNG thuộc phạm vi bước 2.\n"
                "   Ghi vào là đè nhầm một kết luận khác. Rà lại danh sách dòng chờ BA rồi chạy lại.")

        # B2 — P chỉ ghi khi đang là 'BA confirm'. Khác → giữ nguyên (cột trạng thái xử lý của DEV).
        plan = [(ci_verify, COL_VERIFY_HEADER, status), (ci_note, COL_NOTE_HEADER, note)]
        if old_p.strip() == BAAPPLY_MARKER:
            plan.insert(0, (ci_status, COL_STATUS_HEADER, status))
        else:
            print(f"⚠️  [P{args.row}] '{COL_STATUS_HEADER}' đang là '{old_p}' (≠ '{BAAPPLY_MARKER}') "
                  "→ GIỮ NGUYÊN, không ghi.")
            print("   Đó là trạng thái xử lý của DEV, không phải ô của QA (protocol §1). "
                  f"Chỉ ghi {COL_VERIFY_HEADER} + {COL_NOTE_HEADER}.")
    elif args.mode == "qaverdict":
        old_q = read(ci_verify)
        if old_q.strip():
            die(f"[Q{args.row}] '{COL_VERIFY_HEADER}' đang có '{old_q}' — mode qaverdict CHỈ dùng cho "
                "dòng QA chưa kết luận.\n"
                "   Đè kết luận QA cũ mà không có dấu vết = mất lịch sử verdict.\n"
                "   → Nếu đây là RE-VERIFY sau khi dev fix, dùng --mode reverify (Pass/Reopen).\n"
                "   → Nếu thật sự cần sửa verdict sai, HỎI USER rồi ghi tay có kiểm soát.")
        # P giữ nguyên tuyệt đối: đó là trạng thái xử lý của DEV, không phải kết luận của QA.
        if status == "":                                  # ô TRỐNG (blocked) → chỉ ghi lý do vào R
            plan = [(ci_note, COL_NOTE_HEADER, note)]
        else:
            plan = [(ci_verify, COL_VERIFY_HEADER, status), (ci_note, COL_NOTE_HEADER, note)]
    elif args.mode == "verify1":
        if status == VERIFY1_RESOLVED:
            # Cặp mã hoá chuẩn của protocol: P giữ 'Reject', kết quả QA nằm ở cột Verify.
            plan = [(ci_status, COL_STATUS_HEADER, "Reject"),
                    (ci_verify, COL_VERIFY_HEADER, VERIFY1_RESOLVED),
                    (ci_note, COL_NOTE_HEADER, note)]
        elif status == "Reject":
            # Reject = QA ĐÓNG case ở vòng 1 (không chờ dev fix, không chờ BA) → 'Verify' phải
            # mang kết quả cuối, nếu không cột Q kẹt rỗng vĩnh viễn và người đọc sheet không biết
            # QA đã soát hay chưa. Khớp tiền lệ đang có trên sheet: P='Reject' đi kèm Q='Reject'
            # ở 56/57 dòng (6 dòng tuần 2 + 50 dòng tuần 3).
            # KHÔNG mirror cho 'Open' / 'BA confirm': hai verdict đó case còn MỞ (chờ dev fix /
            # chờ BA chốt) → Q phải để trống cho vòng re-verify sau.
            plan = [(ci_status, COL_STATUS_HEADER, "Reject"),
                    (ci_verify, COL_VERIFY_HEADER, "Reject"),
                    (ci_note, COL_NOTE_HEADER, note)]
        else:
            plan = [(ci_status, COL_STATUS_HEADER, status), (ci_note, COL_NOTE_HEADER, note)]
    elif args.mode == "verify2":
        guard_co_claim_vong2()
        plan = [(ci_status2, COL_STATUS2_HEADER, status), (ci_note2, COL_NOTE2_HEADER, note)]
    elif args.mode == "reverify2":
        # Đối xứng mode reverify, đổi bộ cột P/Q/R -> W/X/Y.
        guard_co_claim_vong2()
        if status == "Pass":
            plan = [(ci_verify2, COL_VERIFY2_HEADER, "Pass")]     # W, Y giữ nguyên
            if pass_khoi_phuc_p:                                  # THU HỒI Reopen sai → W về 'dev done'
                plan.append((ci_status2, COL_STATUS2_HEADER, "dev done"))
            if pass_ghi_note:
                plan.append((ci_note2, COL_NOTE2_HEADER, note))   # ĐÈ note (chỉ khi khai báo cờ)
        elif status == "Reopen":
            plan = [(ci_status2, COL_STATUS2_HEADER, "Reopen"),   # ĐÈ 'dev done'
                    (ci_verify2, COL_VERIFY2_HEADER, "Reopen"),
                    (ci_note2, COL_NOTE2_HEADER, note)]           # ĐÈ note dev
        elif status == "BA confirm":
            # KHÔNG đụng W: cột đó là của dev, và phần dev nhận trách nhiệm (lỗi gốc) đã xong thật —
            # ghi 'Reopen' lên đó là đổ oan. Chỗ vướng nằm ở kỳ vọng chưa khớp đặc tả, không ở code.
            plan = [(ci_verify2, COL_VERIFY2_HEADER, "BA confirm"),
                    (ci_note2, COL_NOTE2_HEADER, note)]           # Y = câu hỏi gửi BA
        else:                                                     # reverify2 + blocked
            old_verify2 = read(ci_verify2)
            if old_verify2.strip():
                die(f"status='' (blocked) nhưng cột '{COL_VERIFY2_HEADER}' đang có '{old_verify2}' "
                    "từ lần verify trước.\n"
                    "   Để nguyên = verdict STALE trên sheet đối tác. Xoá = mất lịch sử.\n"
                    "   → HỎI USER: giữ verdict cũ hay xoá về trống, rồi chạy lại.")
            plan = [(ci_note2, COL_NOTE2_HEADER, note)]           # W, X giữ nguyên
    elif status == "Pass":
        plan = [(ci_verify, COL_VERIFY_HEADER, "Pass")]          # P, R giữ nguyên
        if pass_khoi_phuc_p:                                     # THU HỒI Reopen sai → P về 'dev done'
            plan.append((ci_status, COL_STATUS_HEADER, "dev done"))
        if pass_ghi_note:
            plan.append((ci_note, COL_NOTE_HEADER, note))        # ĐÈ note (chỉ khi khai báo cờ)
    elif status == "Reopen":
        plan = [(ci_status, COL_STATUS_HEADER, "Reopen"),        # ĐÈ 'dev done'
                (ci_verify, COL_VERIFY_HEADER, "Reopen"),
                (ci_note, COL_NOTE_HEADER, note)]                # ĐÈ note dev
    else:  # reverify + blocked
        # Q còn verdict cũ (vd 'Reopen' từ vòng trước) mà lần này blocked → giá trị đó STALE:
        # người đọc sheet tưởng verdict vẫn còn hiệu lực. Không tự đoán, dừng hỏi user.
        old_verify = read(ci_verify)
        if old_verify.strip():
            die(f"status='' (blocked) nhưng cột '{COL_VERIFY_HEADER}' đang có '{old_verify}' từ lần verify trước.\n"
                "   Để nguyên = verdict STALE trên sheet đối tác. Xoá = mất lịch sử.\n"
                "   → HỎI USER: giữ verdict cũ hay xoá về trống, rồi chạy lại.")
        plan = [(ci_note, COL_NOTE_HEADER, note)]                # P, Q giữ nguyên

    writes = [{"cell": a1(ci, args.row), "header": h, "old": read(ci), "new": v}
              for ci, h, v in plan]

    # Guard 4: giá trị phải thuộc dropdown của cột (nếu có dropdown)
    for w, (ci, h, v) in zip(writes, plan):
        if h in (COL_STATUS_HEADER, COL_VERIFY_HEADER, COL_STATUS2_HEADER, COL_VERIFY2_HEADER):
            check_dropdown(sh, w["cell"], h, v)

    print("─" * 60)
    print(f"Sheet : {sh.title}  |  Tab: {TAB_NAME}  |  Mode: {args.mode}")
    print(f"Dòng  : {args.row}  |  Mã TC (D) khớp: '{cell_matc}' ✅")
    for w in writes:
        overwrite = "  ⚠️  ĐÈ giá trị cũ" if w["old"].strip() else ""
        print(f"[{w['cell']}] '{w['header']}':{overwrite}")
        print(f"    old: {w['old']!r}")
        print(f"    new: {w['new']!r}")
    untouched = [h for ci, h in ((ci_status, COL_STATUS_HEADER), (ci_verify, COL_VERIFY_HEADER),
                                 (ci_note, COL_NOTE_HEADER), (ci_status2, COL_STATUS2_HEADER),
                                 (ci_verify2, COL_VERIFY2_HEADER), (ci_note2, COL_NOTE2_HEADER))
                 if ci >= 0 and h not in [w["header"] for w in writes]]
    if untouched:
        print(f"(giữ nguyên, KHÔNG đụng: {', '.join(untouched)})")
    print("─" * 60)

    if args.dry_run:
        print("🟡 DRY-RUN — không ghi.")
        return

    # Guard 5: ghi 1 REQUEST DUY NHẤT cho mọi ô trong plan.
    # Ghi từng ô rời sẽ để lại partial write (vd Reopen: P đã đổi nhưng R còn note cũ của dev
    # → sheet ở trạng thái tự mâu thuẫn). raw=True giữ nguyên semantics của update_acell cũ.
    #
    # audit() nằm trong finally: lần ghi cần dấu vết NHẤT chính là lần ghi hỏng giữa chừng.
    ok = False
    try:
        ws.batch_update([{"range": w["cell"], "values": [[w["new"]]]} for w in writes], raw=True)

        # Guard 6: đọc lại xác nhận
        ok = True
        for w, (ci, h, v) in zip(writes, plan):
            w["back"] = read(ci)
            if w["back"].strip() != (v or "").strip():
                ok = False
    finally:
        audit(args, writes, ok)

    if not ok:
        die("Đọc lại KHÔNG khớp (hoặc ghi lỗi giữa chừng) — xem sheet_write.log để lấy giá trị CŨ khôi phục:\n"
            + "\n".join(f"  [{w['cell']}] {w['header']}: old={w['old']!r} · new={w['new']!r} · "
                        f"back={w.get('back', '<chưa đọc lại>')!r}" for w in writes))
    print("✅ GHI THÀNH CÔNG + đọc lại khớp: " + " · ".join(
        f"[{w['cell']}]='{(w['new'] or '')[:20]}'" if len(w["new"] or "") <= 20
        else f"[{w['cell']}]=<{len(w['new'])} ký tự>" for w in writes))


if __name__ == "__main__":
    main()
