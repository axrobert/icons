import { buildStackIndex, assetPath } from './resolve.mjs';

const root = document.getElementById('grid');
const search = document.getElementById('search');
const category = document.getElementById('category');
const format = document.getElementById('format');
const count = document.getElementById('count');
const empty = document.getElementById('empty');
const list = document.getElementById('categories');
const status = document.getElementById('status');
let records = [];

function card(record) {
  const link = document.createElement('a');
  link.className = 'icon-card';
  const [kind, setting] = format.value.split(':');
  const path = assetPath(record, kind === 'png'
    ? { format: 'png', size: Number(setting) }
    : { format: 'svg', svgVariant: setting });
  link.href = path;
  link.download = path.split('/').at(-1);
  link.title = `Download ${record.name} (${kind === 'png' ? `${setting}px PNG` : setting + ' SVG'})`;
  const art = document.createElement('img');
  art.src = path;
  art.alt = '';
  art.loading = 'lazy';
  art.decoding = 'async';
  art.width = 82;
  art.height = 82;
  const label = document.createElement('span');
  label.textContent = record.name;
  label.className = 'name';
  const categoryName = document.createElement('small');
  categoryName.className = 'category-name';
  categoryName.textContent = document.querySelector(`#category option[value="${record.category}"]`)?.textContent ?? record.category;
  link.append(art, label, categoryName);
  return link;
}

function render() {
  const term = search.value.trim().toLowerCase();
  const visible = records.filter(item =>
    (category.value === 'all' || category.value === item.category) &&
    (!term || [item.slug, item.name, ...item.aliases].some(value => value.toLowerCase().includes(term)))
  );
  root.replaceChildren(...visible.map(card));
  count.textContent = `${visible.length} / ${records.length} icons`;
  empty.hidden = visible.length !== 0;
}

try {
  const response = await fetch('./registry.json');
  if (!response.ok) throw new Error('registry.json not found');
  records = await response.json();
  buildStackIndex(records);  // Refuse inconsistent names/aliases at load time.
  const names = new Map([
    ['languages', 'Languages'], ['frontend', 'Frontend'], ['backend', 'Backend'],
    ['databases', 'Databases'], ['cloud', 'Cloud'], ['devops', 'DevOps'],
    ['observability', 'Observability'], ['desktop', 'Desktop & mobile'],
    ['ai', 'AI & data'], ['tools', 'Tools'], ['os', 'Operating systems'],
    ['games', 'Games & 3D'], ['design', 'Design']
  ]);
  for (const [value, text] of names) {
    const option = document.createElement('option');
    option.value = value;
    option.textContent = text;
    category.append(option);
  }
  status.textContent = 'Library ready';
  list.textContent = `${records.length} original stack illustrations`;
  for (const control of [search, category, format]) control.addEventListener(control === search ? 'input' : 'change', render);
  render();
} catch (error) {
  status.textContent = 'Could not load catalog';
  root.textContent = 'The catalog could not be opened. Run a local HTTP server (python -m http.server 8000) and reload.';
  console.error(error);
}
