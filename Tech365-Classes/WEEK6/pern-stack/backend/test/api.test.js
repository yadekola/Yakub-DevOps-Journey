import {test} from 'node:test';
import assert from 'node:assert/strict';
import {readFile} from 'node:fs/promises';
import {newDb} from 'pg-mem';
import {createApp} from '../src/app.js';
import {createRepository} from '../src/repository.js';
const sample={sku:'KB-TEST',name:'Wireless keyboard',category:'Accessories',price_minor:1850000,quantity:24};
async function fixture(t){
  // pg-mem checks query/API behavior without requiring a PostgreSQL daemon.
  const memory=newDb();
  memory.public.none(await readFile(new URL('../migrations/001_products.sql',import.meta.url),'utf8'));
  const {Pool}=memory.adapters.createPg();const pool=new Pool();
  const server=createApp(createRepository(pool),{log:false}).listen(0,'127.0.0.1');
  await new Promise(resolve=>server.once('listening',resolve));
  t.after(async()=>{await new Promise(resolve=>server.close(resolve));await pool.end();});
  return async (path,method='GET',body,headers={})=>{
    const result=await fetch(`http://127.0.0.1:${server.address().port}`+path,{method,headers:{'Content-Type':'application/json',...headers},body:body===undefined?undefined:typeof body==='string'?body:JSON.stringify(body)});
    const text=await result.text();return {status:result.status,body:text?JSON.parse(text):null,headers:result.headers};
  };
}
test('create, retrieve, replace, patch and delete a product',async t=>{
  const req=await fixture(t);
  const created=await req('/api/products','POST',sample);assert.equal(created.status,201);
  const path='/api/products/'+created.body.data.id;
  assert.equal(created.headers.get('location'),path);
  assert.equal((await req(path)).body.data.name,sample.name);
  assert.equal((await req(path,'PUT',{...sample,quantity:10})).body.data.quantity,10);
  assert.equal((await req(path,'PATCH',{price_minor:999})).body.data.price_minor,999);
  assert.equal((await req(path,'DELETE')).status,204);
  assert.equal((await req(path)).status,404);
});
test('duplicate SKU gives 409 and lowercase SKU is normalized',async t=>{
  const req=await fixture(t);
  assert.equal((await req('/api/products','POST',{...sample,sku:'kb-test'})).body.data.sku,'KB-TEST');
  assert.equal((await req('/api/products','POST',sample)).status,409);
});
test('bad product fields, malformed JSON and wrong content type are rejected',async t=>{
  const req=await fixture(t);
  for(const body of [{...sample,quantity:-1},{...sample,price_minor:0.5},{...sample,name:' '},{...sample,id:1},{...sample,sku:'bad sku'},{}])assert.equal((await req('/api/products','POST',body)).status,400);
  assert.equal((await req('/api/products','POST','{"bad":')).status,400);
  assert.equal((await req('/api/products','POST','hello',{'Content-Type':'text/plain'})).status,415);
});
test('search, category filter and pagination work together',async t=>{
  const req=await fixture(t);
  for(let i=0;i<12;i++)assert.equal((await req('/api/products','POST',{...sample,sku:'KB-'+i})).status,201);
  const result=await req('/api/products?search=wireless&category=Accessories&page=2&limit=10');
  assert.equal(result.body.pagination.total,12);assert.equal(result.body.data.length,2);
  assert.equal((await req('/api/products?category=Other')).body.data.length,0);
  assert.equal((await req('/api/products?page=0')).status,400);
  assert.equal((await req('/api/products?limit=101')).status,400);
  assert.equal((await req('/api/products?search=x&search=y')).status,400);
});
test('invalid IDs, missing products and empty patches give consistent errors',async t=>{
  const req=await fixture(t);
  assert.equal((await req('/api/products/abc')).status,400);
  assert.equal((await req('/api/products/999','PATCH',{quantity:1})).status,404);
  assert.equal((await req('/api/products/999','DELETE')).status,404);
  assert.equal((await req('/api/products/1','PATCH',{})).status,400);
  const missing=await req('/api/unknown');assert.equal(missing.status,404);assert.ok(missing.body.error.request_id);
});
test('health endpoints and API specification respond',async t=>{
  const req=await fixture(t);
  assert.equal((await req('/api/health/live')).status,200);
  assert.equal((await req('/api/health/ready')).status,200);
  assert.equal((await req('/api/openapi.json')).body.openapi,'3.0.3');
});
test('readiness returns 503 when the database fails',async t=>{
  const server=createApp({ready:async()=>{throw new Error('offline');}},{log:false}).listen(0,'127.0.0.1');
  await new Promise(resolve=>server.once('listening',resolve));
  t.after(()=>new Promise(resolve=>server.close(resolve)));
  const response=await fetch(`http://127.0.0.1:${server.address().port}/api/health/ready`);
  assert.equal(response.status,503);
});
