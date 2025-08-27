from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/")
def root(payload: dict):
   
    return {"status": "ok", "echo": payload.get("input", {})}
