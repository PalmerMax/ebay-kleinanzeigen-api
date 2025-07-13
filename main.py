from fastapi import FastAPI
from routers import inserate, inserat, health

app = FastAPI(
    version="1.0.0"
)

@app.get("/")
async def root():
    return {
        "message": "Welcome to the Kleinanzeigen API",
        "endpoints": [
            "/inserate",
            "/inserat/{id}"
            "/health"
        ]
    }

app.include_router(inserate.router)
app.include_router(inserat.router) 
app.include_router(health.router)