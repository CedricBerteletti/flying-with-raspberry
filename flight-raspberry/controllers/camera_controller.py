import os
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Camera module"}

@app.post("/pictures")
async def take_picture():
    command = "rpicam-still -0 test.jpg -t 1ms"
    os.system(command)

    return {"file_name": "test.jpg"}
