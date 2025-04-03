from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import uvicorn
import datetime
import json

app = FastAPI()

@app.post("/submit")
async def receive_entry(request: Request):
    data = await request.json()
    data["timestamp"] = datetime.datetime.now().isoformat()

    with open("memory.json", "a") as f:
        f.write(json.dumps(data) + "\n")

    return JSONResponse(content={"status": "success", "received": data})
