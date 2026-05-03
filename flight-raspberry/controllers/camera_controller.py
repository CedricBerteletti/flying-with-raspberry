from fastapi import FastAPI
from fastapi.responses import FileResponse
from services.image_processing import ImageProcessing

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Camera module"}

@app.get("/pictures/latest")
async def get_picture():
    file_name = ImageProcessing().get_picture(ImageProcessing().get_last_picture_id())
    return FileResponse(file_name, media_type="image/jpeg")

@app.get("/pictures/{id}")
async def get_picture(id: int):
    file_name = ImageProcessing().get_picture(id)
    return FileResponse(file_name, media_type="image/jpeg")

@app.post("/pictures")
async def take_picture():

    num_picture, file_name = ImageProcessing().take_picture()

    return {
        "id": num_picture,
        "file_name": file_name
    }
