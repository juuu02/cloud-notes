# cloud_notes

Minimal FastAPI service with Docker.

## Run (local)
```bash
python -m venv .venv
# PowerShell
.\.venv\Scripts\Activate.ps1

python -m pip install -r requirements.txt
python -m uvicorn main:app --host 127.0.0.1 --port 8000

/health (liveness): always 200 if server is running
/ready (readiness): returns 503 if DATABASE_URL is missing
CI runs Docker smoke test + healthy/ready checks