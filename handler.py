import runpod  

def handler(event):
    
    input_data = event.get("input", {})
    
    return {"status": "ok", "echo": input_data}


runpod.serverless.start({"handler": handler})
