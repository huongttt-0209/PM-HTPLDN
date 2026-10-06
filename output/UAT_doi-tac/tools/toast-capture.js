// Bộ bắt thông báo (toast/notification) dùng cho QA trên Chrome DevTools MCP.
// Dán nguyên khối này vào evaluate_script TRƯỚC khi bấm nút cần đo.
//
// VÌ SAO CÓ FILE NÀY — bài học 2026-07-16:
// Bản cũ tôi tự viết có 2 lỗi khiến QA báo sai:
//   1) `if (t && !window.__t.includes(t))` -> TỰ LỌC TRÙNG.
//      Hai toast giống hệt nhau bị gộp thành một => lỗi "double toast" bị che
//      suốt cả đợt verify. Đây là lý do đã đánh Pass mà không thấy lỗi.
//   2) Dùng `textContent` để đọc chữ -> nối cả node ẩn dành cho trình đọc màn hình.
//      Ant Design dựng tiêu đề hộp thoại ở 2 node: `.ant-modal-title` (ẨN) và
//      `.ant-modal-confirm-title` (hiện). `textContent` gom cả hai => chữ nhìn như
//      bị lặp, suýt log thành bug ma. Người dùng KHÔNG hề thấy lặp.
//
// BÀI HỌC 2026-07-17 — LỖI NẶNG NHẤT, chính file này gây ra:
//   Bản trước KHÔNG ngắt observer cũ khi cài lại, mà callback lại tra `window.__qa`
//   TẠI THỜI ĐIỂM CHẠY. Nên mọi observer cũ còn sống đều đẩy vào mảng __qa MỚI.
//   => Cài N lần trong cùng phiên trang thì 1 toast THẬT bị đếm N LẦN.
//   Hậu quả thật: đã Reopen oan BUG-FE-TOAST-LAP (QLKH_02) mà dev đã fix xong,
//   dựng ra cả "quy luật" giả ("từ lần tạo thứ 2 trở đi thì lặp; tải lại trang thì
//   hết") — thực chất đó chỉ là biểu đồ SỐ LẦN TÔI CÀI BỘ ĐO.
//   Dấu hiệu nhận biết đã bỏ lỡ:
//     - `khoangCachMs` cỡ **micro-giây/dưới 1ms** = 2 observer chạy trong CÙNG một lô
//       mutation. React render lặp thật thì cách nhau nhiều mili-giây.
//     - Ảnh chụp KHÔNG BAO GIỜ bắt được toast thứ 2 -> vì màn hình không hề có nó.
//   => Nay bắt buộc: ngắt observer cũ + KHÔNG bọc lại fetch/XHR + TỰ KIỂM số observer.
//
// NGUYÊN TẮC:
//   - KHÔNG lọc trùng. Trùng chính là dữ liệu cần đo.
//   - Đọc bằng `innerText` (chỉ chữ NHÌN THẤY), không dùng `textContent`.
//   - Đếm luôn số request để phân biệt "gửi 2 lần" với "gửi 1 lần hiện 2 thông báo".
//   - Cài lại phải IDEMPOTENT: ngắt cái cũ, không chồng thêm.
//   - Trước khi tin số liệu: `soObserverDangSong` PHẢI = 1. Khác 1 => số liệu VÔ HIỆU.

(() => {
  // 0) IDEMPOTENT — gỡ sạch lần cài trước (nếu có) rồi mới cài lại.
  //    Thiếu bước này = đếm bội số lần cài (xem "BÀI HỌC 2026-07-17" ở trên).
  if (window.__qaObserver) { window.__qaObserver.disconnect(); window.__qaObserver = null; }
  if (window.__qaFetchGoc) { window.fetch = window.__qaFetchGoc; window.__qaFetchGoc = null; }
  if (window.__qaXhrOpenGoc) { XMLHttpRequest.prototype.open = window.__qaXhrOpenGoc; window.__qaXhrOpenGoc = null; }

  window.__qa = { toast: [], net: [] };

  // 1) Bắt MỌI khung thông báo được thêm vào — không lọc trùng
  window.__qaObserver = new MutationObserver((muts) => {
    for (const m of muts) for (const n of m.addedNodes) {
      if (n.nodeType !== 1) continue;
      const cls = n.className?.toString() || '';
      if (/ant-message-notice-wrapper|ant-notification-notice-wrapper/.test(cls)) {
        window.__qa.toast.push({
          thoiDiem: +performance.now().toFixed(1),
          chu: (n.innerText || '').trim(),   // innerText: chỉ chữ người dùng thấy
          loai: /notification/.test(cls) ? 'notification (không tự tắt)' : 'toast (tự tắt ~3s)',
        });
      }
    }
  });
  window.__qaObserver.observe(document.body, { childList: true, subtree: true });

  // 2) Đếm request ghi dữ liệu (bỏ qua GET) — để biết máy chủ được gọi mấy lần
  const ghi = (method, url) => {
    if (!/^GET$/i.test(method)) window.__qa.net.push({ thoiDiem: +performance.now().toFixed(1), method, url });
  };
  window.__qaFetchGoc = window.fetch;
  window.fetch = function (...a) {
    ghi(a[1]?.method || a[0]?.method || 'GET', typeof a[0] === 'string' ? a[0] : a[0]?.url);
    return window.__qaFetchGoc.apply(this, a);
  };
  window.__qaXhrOpenGoc = XMLHttpRequest.prototype.open;
  XMLHttpRequest.prototype.open = function (m, u) { ghi(m, u); return window.__qaXhrOpenGoc.apply(this, arguments); };

  return { daCaiDat: true };
})();

// ---- BẮT BUỘC chạy trước khi tin bất kỳ số liệu nào: TỰ KIỂM số observer ----
// Chèn 1 node giả rồi đếm xem nó bị ghi nhận mấy lần. Phải = 1.
//
// (async () => {
//   window.__qa.toast = [];
//   const gia = document.createElement('div');
//   gia.className = 'ant-message-notice-wrapper';
//   gia.innerText = 'NODE_TU_KIEM';
//   document.body.appendChild(gia);
//   await new Promise(r => setTimeout(r, 400));
//   gia.remove();
//   const soObserverDangSong = window.__qa.toast.filter(x => /NODE_TU_KIEM/.test(x.chu)).length;
//   window.__qa.toast = [];
//   return {
//     soObserverDangSong,
//     hopLe: soObserverDangSong === 1,
//     canhBao: soObserverDangSong === 1 ? null
//       : `CO ${soObserverDangSong} observer -> MOI TOAST BI DEM ${soObserverDangSong} LAN. SO LIEU VO HIEU.`,
//   };
// })();

// ---- Sau khi bấm nút, đợi ~3s rồi chạy đoạn này để đọc kết quả ----
//
// (async () => {
//   await new Promise(r => setTimeout(r, 3000));
//   const t = window.__qa.toast, n = window.__qa.net;
//   return {
//     SO_REQUEST: n.length, request: n.map(x => x.method + ' ' + x.url),
//     SO_KHUNG_THONG_BAO: t.length, chu: t.map(x => x.chu),
//     BI_LAP: t.length > 1 && new Set(t.map(x => x.chu)).size < t.length,
//     khoangCachMs: t.length > 1 ? +(t[1].thoiDiem - t[0].thoiDiem).toFixed(2) : null,
//   };
// })();
//
// ĐỌC KẾT QUẢ (chỉ đọc khi TỰ KIỂM cho soObserverDangSong = 1):
//   SO_REQUEST = 1, SO_KHUNG = 2, chữ giống nhau  -> lỗi HIỂN THỊ phía giao diện,
//                                                    dữ liệu KHÔNG bị tạo trùng.
//   SO_REQUEST = 2, SO_KHUNG = 2                  -> NẶNG: gửi máy chủ 2 lần,
//                                                    phải kiểm ngay có tạo trùng bản ghi không.
//
// CỜ ĐỎ "lỗi là do bộ đo, không phải do app" — gặp thì DỪNG, chạy lại TỰ KIỂM:
//   - SO_KHUNG > 1 nhưng `khoangCachMs` < 1ms          -> observer bị nhân bản.
//   - SO_KHUNG > 1 nhưng chụp ảnh không thấy toast thứ 2 -> màn hình không hề có nó.
//   - Số lần lặp TĂNG DẦN theo thời gian phiên trang / reset khi tải lại trang
//     -> đó là số lần CÀI BỘ ĐO, không phải hành vi của app.
//
// ---- Muốn chụp ảnh toast (toast tự tắt ~3s) ----
// Đừng chèn evaluate_script ở giữa. Bấm nút xong gọi take_screenshot NGAY.
// Không cố chặn AntD gỡ toast bằng cách vá removeChild/remove — đã thử 16/07, KHÔNG ăn
// (AntD gỡ node qua React portal, không đi qua 2 hàm đó).
