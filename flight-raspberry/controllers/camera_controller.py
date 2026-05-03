from fastapi import FastAPI
from services.image_processing import ImageProcessing
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Camera module"}

@app.get("/pictures/latest")
async def get_picture():
    return ImageProcessing().get_picture(ImageProcessing().get_last_picture_id())

@app.get("/pictures/{id}")
async def get_picture(id: int):
    picture = ImageProcessing().get_picture(id)
    return {"image": picture}

@app.post("/pictures")
async def take_picture():

    num_picture, file_name = ImageProcessing().take_picture()

    return {
        "id": num_picture,
        "file_name": file_name
    }
