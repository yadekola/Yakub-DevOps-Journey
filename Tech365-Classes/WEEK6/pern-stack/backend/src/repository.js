// SQL values use parameters; column names only come from a fixed allowlist.
export function createRepository(pool) {
  return {
    async ready() { await pool.query('SELECT id FROM products LIMIT 1'); },
    async list({page, limit, search, category}) {
      const values = [];
      const clauses = [];
      if (search) {
        values.push(`%${search}%`);
        clauses.push(`(name ILIKE $${values.length} OR sku ILIKE $${values.length})`);
      }
      if (category) { values.push(category); clauses.push(`category = $${values.length}`); }
      const where = clauses.length ? ' WHERE ' + clauses.join(' AND ') : '';
      const count = await pool.query('SELECT COUNT(*) AS total FROM products' + where, values);
      const rows = await pool.query(`SELECT * FROM products${where} ORDER BY id DESC LIMIT $${values.length+1} OFFSET $${values.length+2}`, [...values, limit, (page-1)*limit]);
      return {data:rows.rows, pagination:{page, limit, total:Number(count.rows[0].total), total_pages:Math.ceil(Number(count.rows[0].total)/limit)}};
    },
    async get(id) { return (await pool.query('SELECT * FROM products WHERE id=$1',[id])).rows[0]; },
    async create(v) {
      return (await pool.query('INSERT INTO products (sku,name,category,price_minor,quantity) VALUES ($1,$2,$3,$4,$5) RETURNING *', [v.sku,v.name,v.category,v.price_minor,v.quantity])).rows[0];
    },
    async update(id, v) {
      const keys = ['sku','name','category','price_minor','quantity'].filter(k => Object.hasOwn(v,k));
      const sets = keys.map((key,i) => `${key}=$${i+1}`).join(',');
      return (await pool.query(`UPDATE products SET ${sets}, updated_at=NOW() WHERE id=$${keys.length+1} RETURNING *`, [...keys.map(k=>v[k]),id])).rows[0];
    },
    async remove(id) { return (await pool.query('DELETE FROM products WHERE id=$1 RETURNING id',[id])).rowCount > 0; },
  };
}
