from fastapi import FastAPI, File, UploadFile
from typing import List
from PIL import Image
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)


@app.get("/")
async def home():
    return {"message": "Hello world"}


@app.post("/uploadfiles/")
async def create_upload_files(files: List[UploadFile] = File(...)):
    image1 = files[0]
    im1 = Image.open(image1.file)
    (width1, height1) = im1.size
    image2 = files[1]
    im2 = Image.open(image2.file)
    (width2, height2) = im2.size
    message = width1 * height1 + width2 * height2
    return {"message": message}


