from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/")
async def root(payload: dict):
    
    input_data = payload.get("input", {})
    return {"status": "ok", "echo": input_data}
