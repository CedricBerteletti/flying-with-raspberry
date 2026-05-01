import os
from fastapi import FastAPI
import datetime

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Camera module"}

@app.post("/pictures")
async def take_picture():
    time_format = "%Y-%m-%dT%H-%M-%S%z"
    time_str = datetime.date.today().strftime(time_format)
    num_picture = 0
    folder = "/home/rasp/flight-pictures/"
    file_name = folder + time_str + "test" + str(num_picture) + ".jpg"
    if not os.path.exists(folder):
        os.makedirs(folder)
    os.system("rpicam-still" + " -o " + file_name + " -t 1ms")

    return {
        "id": num_picture,
        "file_name": file_name
    }
