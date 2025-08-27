import runpod

def handler(job):
    """
    job is a dict like:
      {
        "id": "...",
        "input": { ... your JSON payload ... }
      }
    """
    data = job.get("input", {})
    return {"status": "ok", "echo": data}


runpod.serverless.start({"handler": handler})
