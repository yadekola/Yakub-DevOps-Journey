export class ApiError extends Error {
  constructor(status, code, message, details) {
    super(message); this.status = status; this.code = code; this.details = details;
  }
}
const allowed = ['sku', 'name', 'category', 'price_minor', 'quantity'];
export function validateProduct(body, partial = false) {
  const errors = {};
  if (!body || typeof body !== 'object' || Array.isArray(body)) {
    throw new ApiError(400, 'VALIDATION_ERROR', 'A JSON object is required.');
  }
  for (const key of Object.keys(body)) if (!allowed.includes(key)) errors[key] = 'Unknown or read-only field.';
  if (partial && Object.keys(body).length === 0) errors.body = 'At least one editable field is required.';
  const value = {};
  for (const key of allowed) {
    if (!(key in body)) { if (!partial) errors[key] = 'This field is required.'; continue; }
    if (['sku', 'name', 'category'].includes(key)) {
      const max = {sku:40, name:160, category:80}[key];
      if (typeof body[key] !== 'string' || !body[key].trim() || body[key].trim().length > max) {
        errors[key] = `Use nonblank text up to ${max} characters.`;
      } else value[key] = body[key].trim();
    } else {
      if (!Number.isSafeInteger(body[key]) || body[key] < 0 || body[key] > 1000000000) errors[key] = 'Use an integer from 0 to 1000000000.';
      else value[key] = body[key];
    }
  }
  if (value.sku) {
    value.sku = value.sku.toUpperCase();
    if (!/^[A-Z0-9][A-Z0-9_-]*$/.test(value.sku)) errors.sku = 'Use letters, numbers, underscores or hyphens; start with a letter or number.';
  }
  if (Object.keys(errors).length) throw new ApiError(400, 'VALIDATION_ERROR', 'Check the submitted fields.', errors);
  return value;
}
export function productId(value) {
  if (!/^[1-9][0-9]*$/.test(value) || !Number.isSafeInteger(Number(value))) throw new ApiError(400,'INVALID_ID','ID must be a positive integer.');
  return Number(value);
}
export function listOptions(query) {
  const result = {};
  for (const [key, fallback, max] of [['page', 1, 1000000], ['limit', 10, 100]]) {
    const raw = query[key];
    if (raw === undefined) { result[key] = fallback; continue; }
    if (typeof raw !== 'string' || !/^[1-9][0-9]*$/.test(raw) || Number(raw) > max) throw new ApiError(400,'INVALID_QUERY',`${key} must be an integer from 1 to ${max}.`);
    result[key] = Number(raw);
  }
  for (const key of ['search','category']) {
    if (query[key] !== undefined && (typeof query[key] !== 'string' || query[key].length > 160)) throw new ApiError(400,'INVALID_QUERY',`${key} must be a string up to 160 characters.`);
    result[key] = (query[key] || '').trim();
  }
  return result;
}
