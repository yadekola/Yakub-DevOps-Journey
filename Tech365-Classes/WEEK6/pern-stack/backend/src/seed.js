import { pool } from './db.js';
const samples=[
  ['KB-001','Wireless keyboard','Accessories',1850000,24],
  ['MS-001','Wireless mouse','Accessories',850000,36],
  ['MN-001','24-inch monitor','Displays',14500000,8],
  ['HB-001','USB-C hub','Accessories',2250000,15],
  ['HD-001','External SSD 1 TB','Storage',9800000,6],
];
try{
  for(const item of samples)await pool.query('INSERT INTO products (sku,name,category,price_minor,quantity) VALUES ($1,$2,$3,$4,$5) ON CONFLICT (sku) DO NOTHING',item);
  console.log('Sample products ready. Existing SKUs were left unchanged.');
}catch(error){console.error('Seed failed:',error.message);process.exitCode=1;}
finally{await pool.end();}
