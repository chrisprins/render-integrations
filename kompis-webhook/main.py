from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

@app.post("/submit-kompis")
async def submit_kompis(request: Request):
    data = await request.json()
    print("Received Kompis data:", data)

    # TODO: Save to file, database, or forward as needed
    return JSONResponse(content={"status": "ok", "message": "Data received"})
