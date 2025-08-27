import runpod  

def handler(event):
    
    data = event.get("input", {})
    return {"status": "ok", "echo": data}


runpod.serverless.start({"handler": handler})
