# cloud_notes

Minimal FastAPI service with Docker.

## Run (local)
```bash
python -m venv .venv
# PowerShell
.\.venv\Scripts\Activate.ps1

python -m pip install -r requirements.txt
python -m uvicorn main:app --host 127.0.0.1 --port 8000
