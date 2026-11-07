/* China4 dashboard — shared shell + table/card renderers. No external dependencies. */
(function () {
  "use strict";

  var isSubpage = /\/site\//.test(location.pathname);
  var base = isSubpage ? "../" : "";

  var NAV = [
    { href: base + "index.html", label: "Executive Summary", key: "index" },
    { href: base + "site/methods.html", label: "Conversion Methods", key: "methods" },
    { href: base + "site/costs.html", label: "Costs & Penalties", key: "costs" },
    { href: base + "site/us-reporting.html", label: "US Tax & Reporting", key: "us" },
    { href: base + "site/rules-china.html", label: "China FX Rules", key: "rules" },
    { href: base + "site/flagged.html", label: "Flagged for Review", key: "flagged" }
  ];

  function escapeHtml(s) {
    return String(s)
      .replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;").replace(/'/g, "&#39;");
  }

  function buildShell() {
    var mount = document.getElementById("topbar");
    if (!mount) return;
    var page = document.body.getAttribute("data-page") || "";
    var html = '<a class="brand" href="' + base + 'index.html">China4 — CNY → USD' +
      '<small>Verified sources · Updated 2026-11-07 · For a US citizen</small></a><nav>';
    NAV.forEach(function (item) {
      html += '<a href="' + item.href + '"' + (item.key === page ? ' class="current"' : "") +
        ">" + escapeHtml(item.label) + "</a>";
    });
    html += "</nav>";
    mount.className = "topbar";
    mount.innerHTML = html;

    var fm = document.getElementById("footer");
    if (fm) {
      fm.className = "footer";
      fm.innerHTML =
        "<p><strong>Verification policy:</strong> every row marked <span class='badge verified'>verified</span> " +
        "links to an official source that was retrieved and read line-by-line on 2026-11-07 " +
        "(see <a href='https://github.com/sassnarep3-star/China4/blob/main/VERIFICATION.md'>VERIFICATION.md</a>). " +
        "Rows marked <span class='badge unverified'>unverified</span> could not be confirmed on an official page " +
        "and appear on the Flagged for Review page. This dashboard is informational research, " +
        "not tax, legal or financial advice.</p>";
    }
  }

  function srcLink(src) {
    if (!src || !src.url) return '<span class="sub">—</span>';
    var t = src.title || "source";
    return '<span class="srclink"><a href="' + escapeHtml(src.url) + '" target="_blank" rel="noopener">' +
      escapeHtml(t) + " ↗</a></span>";
  }

  function badge(status, label) {
    var map = { verified: "verified", conditional: "conditional", prohibited: "prohibited", unverified: "unverified", analysis: "analysis", historical: "historical" };
    var cls = map[status] || "unverified";
    return '<span class="badge ' + cls + '">' + escapeHtml(label || status) + "</span>";
  }

  /* Generic table renderer.
     cols: [{key, title, render(row) (optional)}]  rows: array of objects */
  function renderTable(mountId, cols, rows, opts) {
    var mount = document.getElementById(mountId);
    if (!mount) return;
    opts = opts || {};

    var toolbarHtml = "";
    if (opts.filter !== false) {
      toolbarHtml = '<div class="toolbar"><input type="search" id="' + mountId + '-q" placeholder="Filter rows…" aria-label="Filter rows"><span class="count" id="' + mountId + '-count"></span></div>';
    }

    var head = "<thead><tr>" + cols.map(function (c) { return "<th>" + escapeHtml(c.title) + "</th>"; }).join("") + "</tr></thead>";
    var bodyRows = rows.map(function (r) {
      var tds = cols.map(function (c) {
        var v = c.render ? c.render(r) : escapeHtml(r[c.key] == null || r[c.key] === "" ? "" : r[c.key]);
        if (c.key === "source" && !c.render) v = srcLink(r.source);
        if (c.key === "status" && !c.render) v = badge(r.status, r.statusLabel);
        return "<td>" + (v === "" ? '<span class="sub">—</span>' : v) + "</td>";
      });
      return { html: "<tr>" + tds.join("") + "</tr>", hay: JSON.stringify(Object.keys(r).map(function (k) { var x = r[k]; if (x && typeof x === "object") { return (x.title || "") + " " + (x.url || ""); } return x; }).join(" ")).toLowerCase() };
    });

    mount.innerHTML = toolbarHtml + '<div class="tablewrap"><table class="data">' + head + "<tbody>" +
      bodyRows.map(function (b) { return b.html; }).join("") + "</tbody></table></div>";

    function updateCount(shown) {
      var c = document.getElementById(mountId + "-count");
      if (c) c.textContent = shown + " of " + rows.length + " rows";
    }
    updateCount(rows.length);

    if (opts.filter !== false) {
      var input = document.getElementById(mountId + "-q");
      var trs = mount.querySelectorAll("tbody tr");
      input.addEventListener("input", function () {
        var q = input.value.trim().toLowerCase();
        var shown = 0;
        trs.forEach(function (tr, i) {
          var ok = !q || bodyRows[i].hay.indexOf(q) !== -1;
          tr.style.display = ok ? "" : "none";
          if (ok) shown++;
        });
        updateCount(shown);
      });
    }
  }

  /* Method card renderer for the Conversion Methods page */
  function renderMethods(mountId, groups) {
    var mount = document.getElementById(mountId);
    if (!mount) return;
    var html = "";
    groups.forEach(function (g) {
      html += '<h2 id="' + g.id + '">' + escapeHtml(g.title) + "</h2>";
      html += '<p class="note" style="color:var(--muted);margin:-.4rem 0 1rem">' + escapeHtml(g.intro || "") + "</p>";
      g.methods.forEach(function (m) {
        html += '<article class="method">';
        html += "<header><h3>" + escapeHtml(m.name) + "</h3>" +
          '<span class="tag">' + escapeHtml(m.category || "") + "</span>" +
          badge(m.status, m.statusLabel || m.status) + "</header>";
        html += '<div class="body">';
        html += '<div class="col"><h4>How it works</h4><p style="margin:0">' + m.how + "</p>" +
          (m.limit ? '<p style="margin:.5rem 0 0"><span class="chip"><strong>Limit:</strong> ' + escapeHtml(m.limit) + "</span></p>" : "") + "</div>";
        html += '<div class="col"><h4>Pros</h4><ul>' + m.pros.map(function (p) { return "<li>" + p + "</li>"; }).join("") + "</ul></div>";
        html += '<div class="col"><h4>Cons / risks</h4><ul>' + m.cons.map(function (c) { return "<li>" + c + "</li>"; }).join("") + "</ul></div>";
        html += "</div>";
        html += "<footer>" +
          '<span class="meta"><strong>Cost &amp; tax:</strong> ' + m.cost + "</span>" +
          '<span class="meta"><strong>Sources:</strong> ' +
          m.sources.map(function (s) { return srcLink(s); }).join(" ") + "</span>" +
          "</footer>";
        html += "</article>";
      });
    });
    mount.innerHTML = html;
  }

  function renderStats(mountId, stats) {
    var mount = document.getElementById(mountId);
    if (!mount) return;
    mount.className = "cards";
    mount.innerHTML = stats.map(function (s) {
      return '<div class="card ' + s.kind + '"><h3>' + escapeHtml(s.label) + "</h3>" +
        '<div class="big">' + escapeHtml(s.value) + "</div><p>" + s.note + "</p></div>";
    }).join("");
  }

  window.DASH = {
    buildShell: buildShell,
    renderTable: renderTable,
    renderMethods: renderMethods,
    renderStats: renderStats,
    srcLink: srcLink,
    badge: badge
  };

  document.addEventListener("DOMContentLoaded", buildShell);
})();
