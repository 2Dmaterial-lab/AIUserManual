/* Material's document$ also fires after navigation.instant swaps a page. */
(function () {
  "use strict";
  function updatePopularity() {
    var el = document.getElementById("site-ga-popularity");
    if (!el) return;
    el.hidden = true;
    var path = el.getAttribute("data-stats");
    if (!path) return;
    var url = new URL(path, document.baseURI);
    if (url.origin !== window.location.origin) return;
    fetch(url.href, { credentials: "same-origin", cache: "no-cache" })
      .then(function (response) {
        if (!response.ok) throw new Error("Statistics unavailable");
        return response.json();
      })
      .then(function (data) {
        if (!data || !Number.isSafeInteger(data.totalPageViews) || data.totalPageViews < 0) return;
        if (!el.isConnected) return;
        var when = "";
        if (typeof data.updatedAt === "string" && !isNaN(Date.parse(data.updatedAt))) {
          when = " · 数据更新 " + new Date(data.updatedAt).toISOString().slice(0, 10);
        }
        el.textContent = "全站累计约 " + data.totalPageViews.toLocaleString("zh-CN") + " 次页面浏览" + when;
        el.hidden = false;
      })
      .catch(function () {
        // Optional statistics must not interrupt reading or expose setup details.
        el.hidden = true;
      });
  }
  if (typeof document$ !== "undefined") {
    document$.subscribe(updatePopularity);
  } else if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", updatePopularity);
  } else {
    updatePopularity();
  }
})();
