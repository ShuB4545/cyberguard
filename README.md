# CyberGuard (Frontend + FastAPI Backend)

This package includes your full 956-line **CyberGuard** frontend plus a working **FastAPI** backend API.

## Project Structure
```
cyberguard/
├── backend/
│   ├── main.py
│   └── requirements.txt
└── frontend/
    ├── index.html              # your original 956-line UI (client-side computation)
    ├── index_backend.html      # same UI + adds an "Analyze (API)" button
    └── enable_backend.js       # wires the API button to FastAPI
```

## How to Run (Backend)
1) Open a terminal in `cyberguard/backend`
2) Create venv (optional) and install deps:
```
pip install -r requirements.txt
```
3) Start the API:
```
uvicorn main:app --reload
```
The API will be on `http://127.0.0.1:8000`

## How to Open the Frontend
- **Local only (no API needed):**
  - Double click `frontend/index.html` to open in your browser. It performs all analysis in the browser.

- **With API (to show client-server integration):**
  - After starting the backend, open `frontend/index_backend.html` in your browser.
  - It shows the same UI but adds an extra button: **"Analyze (API)"** which sends the request to `http://127.0.0.1:8000/api/analyze` and displays the backend result.

> Tip: If your browser blocks local scripts, you can serve the frontend with a simple local server:
```
cd frontend
python -m http.server 8001
```
Then open `http://127.0.0.1:8001/index_backend.html`.

## Notes
- The simulator tab is a **safe, offline simulation** — it does not touch real systems.
- All calculations are strictly educational and designed to demonstrate security concepts.
