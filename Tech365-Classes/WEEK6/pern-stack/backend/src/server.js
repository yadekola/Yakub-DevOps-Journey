import { createApp } from './app.js';
import { createRepository } from './repository.js';
import { pool, config } from './db.js';
const server=createApp(createRepository(pool)).listen(config.port,'0.0.0.0',()=>console.log(`Inventory API listening on ${config.port}`));
server.on('error',async error=>{console.error(error.message);await pool.end();process.exitCode=1;});
let stopping=false;
function shutdown(signal){
  if(stopping)return;stopping=true;
  console.log(`Received ${signal}; closing HTTP server.`);
  const timer=setTimeout(()=>process.exit(1),10000);timer.unref();
  server.close(async()=>{await pool.end();clearTimeout(timer);process.exitCode=0;});
}
process.on('SIGTERM',()=>shutdown('SIGTERM'));
process.on('SIGINT',()=>shutdown('SIGINT'));
