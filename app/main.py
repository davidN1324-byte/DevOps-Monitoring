from fastapi import FastAPI, Request, Response as FastAPIResponse
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST
from fastapi.responses import Response
import time

app = FastAPI()

REQUEST_COUNTER = Counter(
    "http_requests_total",
    "Total number of HTTP requests",
    ["method", "path", "status_code"]
)

@app.middleware("http")
async def metrics_middleware(request: Request, call_next):
    start_time = time.time()
    response: FastAPIResponse = await call_next(request)

    REQUEST_COUNTER.labels(
        method=request.method,
        path=request.url.path,
        status_code=str(response.status_code)
    ).inc()
    
    return response

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI!"}

@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)

@app.get("/error")
def trigger_error():
    raise HTTPException(status_code=400, detail="Bad Request")

@app.get("/server_error")
def trigger_server_error():
    raise HTTPException(status_code=500, detail="Server Error")

@app.get("/not_found")
def trigger_not_found():
    raise HTTPException(status_code=404, detail="Page not found")