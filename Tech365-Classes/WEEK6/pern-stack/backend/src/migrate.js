import { readdir, readFile } from 'node:fs/promises';
import { pool } from './db.js';
const directory=new URL('../migrations/',import.meta.url);
let client;
try {
  client=await pool.connect();
  // Prevent two migration jobs from modifying the schema concurrently.
  await client.query('SELECT pg_advisory_lock(365001)');
  await client.query('CREATE TABLE IF NOT EXISTS schema_migrations (name TEXT PRIMARY KEY, applied_at TIMESTAMPTZ NOT NULL DEFAULT NOW())');
  for(const name of (await readdir(directory)).filter(n=>n.endsWith('.sql')).sort()){
    const exists=await client.query('SELECT name FROM schema_migrations WHERE name=$1',[name]);
    if(exists.rowCount)continue;
    await client.query('BEGIN');
    try{
      await client.query(await readFile(new URL(name,directory),'utf8'));
      await client.query('INSERT INTO schema_migrations (name) VALUES ($1)',[name]);
      await client.query('COMMIT');console.log(`Applied ${name}`);
    }catch(error){await client.query('ROLLBACK');throw error;}
  }
  console.log('Database schema is up to date.');
}catch(error){console.error('Migration failed:',error.message);process.exitCode=1;}
finally{
  if(client){try{await client.query('SELECT pg_advisory_unlock(365001)');}finally{client.release();}}
  await pool.end();
}
