// Runs against a started stack. Creates and deletes only its own product.
import assert from 'node:assert/strict';
const base=(process.argv[2] || 'http://localhost:3000').replace(/\/$/,'');
async function request(path,method='GET',body){
  const response=await fetch(base+path,{method,headers:{'Content-Type':'application/json'},body:body===undefined?undefined:JSON.stringify(body),signal:AbortSignal.timeout(10000)});
  const text=await response.text();return {status:response.status,body:text?JSON.parse(text):null};
}
assert.equal((await request('/api/health/ready')).status,200);
const sku='SMOKE-'+Date.now();
const created=await request('/api/products','POST',{sku,name:'Smoke product',category:'Verification',price_minor:150000,quantity:5});
assert.equal(created.status,201,JSON.stringify(created.body));
const path='/api/products/'+created.body.data.id;
try{
  assert.equal((await request(path)).body.data.sku,sku);
  assert.equal((await request(path,'PATCH',{quantity:7})).body.data.quantity,7);
  assert.equal((await request('/api/products?search='+sku)).body.pagination.total,1);
  assert.equal((await request(path,'PATCH',{quantity:-1})).status,400);
}finally{assert.equal((await request(path,'DELETE')).status,204);}
assert.equal((await request(path)).status,404);
console.log('PASS: readiness, create, retrieve, update, search, validation and delete.');
