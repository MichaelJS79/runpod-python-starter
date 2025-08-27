import runpod  

def process_data(input_data):
    
    return {"status": "ok", "echo": input_data}

def handler(event):
   
    input_data = event.get("input", {})
    result = process_data(input_data)
    return result


runpod.serverless.start({"handler": handler})
