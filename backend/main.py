from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os

app = FastAPI()

# Allow frontend to talk to backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 📂 Mount the frontend folder
frontend_path = os.path.join(os.path.dirname(__file__), "..", "frontend")
app.mount("/static", StaticFiles(directory=frontend_path), name="static")

# 🏠 Serve index.html at "/"
@app.get("/")
def read_index():
    return FileResponse(os.path.join(frontend_path, "index.html"))

# =========================================
# Your API endpoints (keep them here)
# =========================================
@app.post("/analyze-password")
def analyze_password(password: str):
    # example response
    return {"password": password, "strength": "Strong"}

@app.post("/bruteforce-estimate")
def bruteforce_estimate(password: str):
    # example response
    return {"password": password, "time_to_crack": "2 days"}
