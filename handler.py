def handler(event):
    # "event" is the JSON payload you POST
    return {"status": "ok", "echo": event}
