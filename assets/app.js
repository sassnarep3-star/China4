const escapeHtml = (value = "") => String(value).replace(/[&<>"']/g, c => ({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c]));
const linkList = sources => (sources || []).map(source => `<a href="${escapeHtml(source.url)}" target="_blank" rel="noopener noreferrer">${escapeHtml(source.label)} ↗</a>`).join("");
const readData = async file => {
  const base = document.body.dataset.base || ".";
  const response = await fetch(`${base}/data/${file}.json`);
  if (!response.ok) throw new Error(`Unable to load ${file}.json (${response.status})`);
  return response.json();
};
const showError = target => { if (target) target.innerHTML = '<tr><td colspan="8" class="empty-state">Could not load this research table. Please reload the page.</td></tr>'; };

async function renderRoutes() {
  const body = document.getElementById("routes-table");
  try {
    const rows = await readData("routes");
    const search = document.getElementById("route-search");
    const category = document.getElementById("route-category");
    const count = document.getElementById("route-count");
    const paint = () => {
      const query = search.value.trim().toLowerCase();
      const selected = category.value;
      const visible = rows.filter(row => (!selected || row.category === selected) && (!query || [row.route,row.category,row.what,row.pros,row.cons,row.limit].join(" ").toLowerCase().includes(query)));
      count.textContent = `${visible.length} of ${rows.length} routes`;
      body.innerHTML = visible.length ? visible.map((row, index) => `<tr>
        <td><div class="route-title"><span class="route-index">${String(rows.indexOf(row)+1).padStart(2,"0")}</span><div><strong>${escapeHtml(row.route)}</strong><div class="source-note">${escapeHtml(row.category)}</div></div></div></td>
        <td>${escapeHtml(row.what)}</td><td>${escapeHtml(row.pros)}</td><td>${escapeHtml(row.cons)}</td>
        <td><span class="tag tag-${escapeHtml(row.status)}">${escapeHtml(row.status.replaceAll("-"," "))}</span><div class="source-note">${escapeHtml(row.limit)}</div>${row.fees ? `<div class="source-note">Fee: ${escapeHtml(row.fees)}</div>` : ""}</td>
        <td><div class="source-links">${linkList(row.sources)}</div></td></tr>`).join("") : '<tr><td colspan="6" class="empty-state">No routes match your search.</td></tr>';
    };
    search.addEventListener("input", paint); category.addEventListener("change", paint); paint();
  } catch (error) { console.error(error); showError(body); }
}

async function renderTax() {
  const body = document.getElementById("tax-table");
  const costsBody = document.getElementById("costs-table");
  try {
    const rows = await readData("tax");
    body.innerHTML = rows.map(row => `<tr><td><span class="tag tag-narrow-use">${escapeHtml(row.area)}</span></td><td><strong>${escapeHtml(row.item)}</strong></td><td>${escapeHtml(row.rule)}<div class="source-note"><strong>Published value:</strong> ${escapeHtml(row.amount)}</div></td><td>${escapeHtml(row.application)}</td><td>${escapeHtml(row.status)}</td><td><div class="source-links">${linkList(row.sources)}</div></td></tr>`).join("");
    const costs = await readData("costs");
    costsBody.innerHTML = costs.map(row => `<tr><td><strong>${escapeHtml(row.item)}</strong></td><td>${row.amount ? escapeHtml(row.amount) : '<span class="unverified">—</span>'}</td><td>${escapeHtml(row.impact)}</td><td>${escapeHtml(row.status)}</td><td><div class="source-links">${linkList(row.sources)}</div></td></tr>`).join("");
  } catch (error) { console.error(error); showError(body); showError(costsBody); }
}

async function renderRequirements() {
  const body = document.getElementById("requirements-table");
  try {
    const rows = await readData("requirements");
    body.innerHTML = rows.map(row => `<tr><td><strong>${escapeHtml(row.step)}</strong></td><td>${escapeHtml(row.required)}</td><td>${escapeHtml(row.why)}</td><td><div class="source-links">${linkList(row.sources)}</div></td></tr>`).join("");
  } catch (error) { console.error(error); showError(body); }
}

async function renderSources() {
  const list = document.getElementById("sources-list");
  try {
    const sources = await readData("sources");
    const search = document.getElementById("source-search");
    const count = document.getElementById("source-count");
    const paint = () => {
      const q = search.value.trim().toLowerCase();
      const selected = sources.filter(item => !q || [item.id,item.authority,item.title,item.note].join(" ").toLowerCase().includes(q));
      count.textContent = `${selected.length} of ${sources.length} sources`;
      list.innerHTML = selected.map(item => `<article class="source-card"><span class="source-id">${escapeHtml(item.id)}</span><div><strong>${escapeHtml(item.title)}</strong><small>${escapeHtml(item.authority)} · checked ${escapeHtml(item.checked)}</small><a href="${escapeHtml(item.url)}" target="_blank" rel="noopener noreferrer">Open official source ↗</a><p>${escapeHtml(item.note)}</p></div></article>`).join("") || '<div class="empty-state">No sources match your search.</div>';
    };
    search.addEventListener("input", paint); paint();
  } catch (error) { console.error(error); list.innerHTML = '<div class="empty-state">Could not load the official source register.</div>'; }
}

async function renderFlags() {
  const list = document.getElementById("flags-list");
  try {
    const rows = await readData("flags");
    list.innerHTML = rows.map((row,index) => `<article class="flag-card"><span class="flag-index">${String(index+1).padStart(2,"0")}</span><div><h3>${escapeHtml(row.flag)}</h3><p>${escapeHtml(row.detail)}</p><div class="flag-meta"><span class="severity">${escapeHtml(row.severity)}</span><div class="source-links">${linkList(row.sources)}</div></div></div></article>`).join("");
  } catch (error) { console.error(error); list.innerHTML = '<div class="empty-state">Could not load the review items.</div>'; }
}

const page = document.body.dataset.page;
if (page === "routes") renderRoutes();
if (page === "tax") renderTax();
if (page === "requirements") renderRequirements();
if (page === "sources") renderSources();
if (page === "review") renderFlags();
