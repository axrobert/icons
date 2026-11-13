/** Normalize source technology names to stable lookup keys. */
export function normalizeStack(value) {
  return String(value ?? '')
    .trim()
    .normalize('NFKD')
    .replace(/[\u0300-\u036f]/g, '')
    .toLowerCase()
    .replace(/c\+\+/g, 'cpp')
    .replace(/c#/g, 'csharp')
    .replace(/\.net/g, 'dotnet')
    .replace(/[^a-z0-9]+/g, '-')
    .replace(/^-+|-+$/g, '');
}

/** Build once and reuse for repeated stack resolutions. */
export function buildStackIndex(records) {
  if (!Array.isArray(records)) throw new TypeError('Expected an array of records');
  const index = new Map();
  for (const record of records) {
    for (const candidate of [record.slug, record.name, ...(record.aliases ?? [])]) {
      const key = normalizeStack(candidate);
      if (!key) throw new Error(`Empty stack alias for ${record.slug}`);
      if (index.has(key) && index.get(key).slug !== record.slug) {
        throw new Error(`Alias collision: ${candidate} -> ${record.slug} / ${index.get(key).slug}`);
      }
      index.set(key, record);
    }
  }
  return index;
}

export function resolveStack(index, name) {
  if (!(index instanceof Map)) throw new TypeError('Call buildStackIndex(registry) first');
  return index.get(normalizeStack(name)) ?? null;
}

/** Paths are repository-relative, safe to resolve against a chosen asset base URL. */
export function assetPath(record, { format = 'png', size = 64, svgVariant = 'vector' } = {}) {
  if (!record) return null;
  if (format === 'png') {
    if (![16, 32, 64, 256].includes(Number(size))) throw new RangeError('Unsupported PNG size');
    return record.assets.png[String(size)];
  }
  if (format === 'svg') {
    if (!['vector', 'fidelity'].includes(svgVariant)) throw new RangeError('Unknown SVG variant');
    return record.assets.svg[svgVariant];
  }
  throw new RangeError('Unknown format');
}

/** Example: resolveIcon(buildStackIndex(registry), 'Next.js', { size: 32 }). */
export function resolveIcon(index, name, options = {}) {
  return assetPath(resolveStack(index, name), options);
}
