import os
from fastapi import FastAPI
from routers import inserate, inserat, health
import uvicorn

app = FastAPI(
    version="1.0.0"
)

@app.get("/")
async def root():
    return {
        "message": "Welcome to the Kleinanzeigen API",
        "endpoints": [
            "/inserate",
            "/inserat/{id}",
            "/health"
        ]
    }

app.include_router(inserate.router)
app.include_router(inserat.router)
app.include_router(health.router)

if __name__ == "__main__":
    port_str = os.environ.get("PORT")
    if port_str is None:
        raise RuntimeError("Environment variable PORT must be set.")
    
    uvicorn.run("main:app", host="0.0.0.0", port=int(port_str), reload=False)
