import pg from 'pg';
import { configFromEnv } from './config.js';
export const config = configFromEnv();
export const pool = new pg.Pool(config.database);
// An idle connection can fail when the database restarts. Keep the process alive.
pool.on('error', error => console.error(JSON.stringify({event:'database_pool_error', code:error.code || 'unknown'})));
