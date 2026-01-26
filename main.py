import os
from fastapi import FastAPI, HTTPException

app = FastAPI()


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/ready")
def ready():
    if not os.getenv("DATABASE_URL"):
        raise HTTPException(status_code=503, detail="DATABASE_URL is not set")
    return {"status": "ready"}
