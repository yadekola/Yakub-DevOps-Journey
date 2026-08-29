// The API base is empty because Nginx reverse-proxies /api to the API container.
// The browser therefore never needs to know the API's address, which is what makes this
// work identically on localhost, in Docker Compose and behind a Kubernetes Ingress.
const API = "";

const $ = (id) => document.getElementById(id);

async function req(path, options = {}) {
  const res = await fetch(API + path, {
    headers: { "Content-Type": "application/json" },
    ...options,
  });
  if (!res.ok) {
    const body = await res.json().catch(() => ({ detail: res.statusText }));
    throw new Error(body.detail || `HTTP ${res.status}`);
  }
  return res.status === 204 ? null : res.json();
}

function flash(text, ok = false) {
  const el = $("msg");
  el.textContent = text;
  el.className = "msg " + (ok ? "ok" : "err");
  setTimeout(() => { el.textContent = ""; }, 4000);
}

async function loadSummary() {
  try {
    const s = await req("/api/summary");
    $("m-items").textContent = s.total_items;
    $("m-units").textContent = s.total_units;
    $("m-low").textContent = s.low_stock_count;
    const b = $("cache-badge");
    b.textContent = s.cached ? "cache hit" : "cache miss";
    b.className = "badge " + (s.cached ? "hit" : "");
  } catch (e) {
    $("cache-badge").textContent = "api down";
  }
}

async function loadItems() {
  const term = $("search").value.trim();
  const tbody = $("rows");
  try {
    const items = await req("/api/items" + (term ? `?search=${encodeURIComponent(term)}` : ""));
    if (!items.length) {
      tbody.innerHTML = '<tr><td colspan="6" class="muted">No items.</td></tr>';
      return;
    }
    tbody.innerHTML = "";
    for (const it of items) {
      const tr = document.createElement("tr");
      if (it.is_low_stock) tr.className = "low";
      tr.innerHTML = `<td>${it.sku}</td><td>${it.name}</td><td class="muted">${it.category}</td>
        <td>${it.quantity} <span class="muted">${it.unit}</span></td>
        <td class="muted">${it.reorder_level}</td><td></td>`;
      const cell = tr.lastElementChild;
      for (const [label, kind] of [["+1", "in"], ["−1", "out"]]) {
        const b = document.createElement("button");
        b.className = "ghost";
        b.textContent = label;
        b.style.marginRight = "6px";
        b.onclick = () => move(it.sku, kind);
        cell.appendChild(b);
      }
      tbody.appendChild(tr);
    }
  } catch (e) {
    tbody.innerHTML = `<tr><td colspan="6" class="muted">Could not load items: ${e.message}</td></tr>`;
  }
}

async function move(sku, kind) {
  try {
    await req("/api/movements", {
      method: "POST",
      body: JSON.stringify({ sku, kind, quantity: 1, note: "dashboard" }),
    });
    await refresh();
  } catch (e) {
    // This is where the "stock cannot go negative" rule becomes visible to the user.
    flash(e.message);
  }
}

async function addItem() {
  try {
    await req("/api/items", {
      method: "POST",
      body: JSON.stringify({
        sku: $("f-sku").value.trim(),
        name: $("f-name").value.trim(),
        category: $("f-category").value.trim() || "general",
        quantity: Number($("f-qty").value || 0),
        reorder_level: Number($("f-reorder").value || 5),
      }),
    });
    $("f-sku").value = ""; $("f-name").value = "";
    flash("Item added.", true);
    await refresh();
  } catch (e) {
    flash(e.message);
  }
}

async function refresh() { await Promise.all([loadSummary(), loadItems()]); }

$("f-add").onclick = addItem;
let t;
$("search").oninput = () => { clearTimeout(t); t = setTimeout(loadItems, 250); };
refresh();
setInterval(loadSummary, 5000);   // watch the cache badge flip between hit and miss
