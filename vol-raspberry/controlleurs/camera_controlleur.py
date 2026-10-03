from fastapi import FastAPI
from fastapi.responses import FileResponse
from services.traitement_image import TraitementImage

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Module caméra"}

@app.get("/images/derniere")
async def get_picture():
    file_name = TraitementImage().get_image(TraitementImage().get_id_derniere_image())
    return FileResponse(file_name, media_type="image/jpeg")

@app.get("/images/{id}")
async def get_picture(id: int):
    file_name = TraitementImage().get_image(id)
    return FileResponse(file_name, media_type="image/jpeg")

@app.post("/images")
async def take_picture():

    num_picture, file_name = TraitementImage().prend_photo()

    return {
        "id": num_picture,
        "file_name": file_name
    }
