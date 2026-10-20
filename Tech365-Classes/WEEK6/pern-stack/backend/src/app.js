import express from 'express';
import helmet from 'helmet';
import { randomUUID } from 'node:crypto';
import { readFileSync } from 'node:fs';
import { ApiError, validateProduct, productId, listOptions } from './validation.js';
const spec = JSON.parse(readFileSync(new URL('../openapi.json', import.meta.url), 'utf8'));
export function createApp(repository, {log = true} = {}) {
  const app = express();
  app.disable('x-powered-by');
  app.use(helmet());
  app.use((req,res,next) => {
    req.requestId = randomUUID(); res.setHeader('X-Request-ID',req.requestId);
    const start = Date.now();
    res.on('finish',()=>{if(log) console.log(JSON.stringify({request_id:req.requestId,method:req.method,path:req.path,status:res.statusCode,duration_ms:Date.now()-start}));});
    next();
  });
  app.use(express.json({limit:'32kb', strict:true}));
  app.get('/api', (req,res)=>res.json({name:'Tech365 Inventory API',version:'1.0.0',documentation:'/api/openapi.json',currency:'NGN'}));
  app.get('/api/openapi.json', (req,res)=>res.json(spec));
  app.get('/api/health/live', (req,res)=>res.json({status:'ok'}));
  app.get('/api/health/ready', async (req,res) => {
    try { await repository.ready(); res.json({status:'ok',database:'ready'}); }
    catch { res.status(503).json({error:{code:'NOT_READY',message:'Database or schema unavailable.',request_id:req.requestId}}); }
  });
  app.get('/api/products', async (req,res)=>res.json(await repository.list(listOptions(req.query))));
  app.get('/api/products/:id', async (req,res)=>{
    const product = await repository.get(productId(req.params.id));
    if(!product) throw new ApiError(404,'NOT_FOUND','Product not found.');
    res.json({data:product});
  });
  app.post('/api/products', async (req,res)=>{
    if(!req.is('application/json')) throw new ApiError(415,'UNSUPPORTED_MEDIA_TYPE','Send Content-Type: application/json.');
    const product=await repository.create(validateProduct(req.body));
    res.location(`/api/products/${product.id}`).status(201).json({data:product});
  });
  const update = partial => async (req,res)=>{
    if(!req.is('application/json')) throw new ApiError(415,'UNSUPPORTED_MEDIA_TYPE','Send Content-Type: application/json.');
    const id=productId(req.params.id);
    const product=await repository.update(id,validateProduct(req.body,partial));
    if(!product) throw new ApiError(404,'NOT_FOUND','Product not found.');
    res.json({data:product});
  };
  app.put('/api/products/:id',update(false));
  app.patch('/api/products/:id',update(true));
  app.delete('/api/products/:id',async (req,res)=>{
    if(!await repository.remove(productId(req.params.id))) throw new ApiError(404,'NOT_FOUND','Product not found.');
    res.status(204).end();
  });
  app.use((req,res,next)=>next(new ApiError(404,'NOT_FOUND','Endpoint not found.')));
  app.use((error,req,res,next)=>{
    if(res.headersSent) return next(error);
    let failure = error;
    if(error.type==='entity.parse.failed') failure=new ApiError(400,'INVALID_JSON','Request body is not valid JSON.');
    else if(error.type==='entity.too.large') failure=new ApiError(413,'BODY_TOO_LARGE','JSON body must be 32 KB or smaller.');
    else if(error.code==='23505') failure=new ApiError(409,'SKU_EXISTS','A product with that SKU already exists.');
    else if(!(error instanceof ApiError)) {
      if(log) console.error(JSON.stringify({request_id:req.requestId,event:'request_error',code:error.code||'unknown'}));
      failure=new ApiError(500,'INTERNAL_ERROR','Unable to complete the request.');
    }
    res.status(failure.status).json({error:{code:failure.code,message:failure.message,...(failure.details?{details:failure.details}:{}),request_id:req.requestId}});
  });
  return app;
}
