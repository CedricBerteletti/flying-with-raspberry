from fastapi import FastAPI
from services.image_processing import ImageProcessing
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Camera module"}

@app.post("/pictures")
async def take_picture():

    num_picture, file_name = ImageProcessing().take_picture()
    
    return {
        "id": num_picture,
        "file_name": file_name
    }
