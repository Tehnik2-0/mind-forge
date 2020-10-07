from fastapi import FastAPI, File, UploadFile
from typing import List
from PIL import Image

app = FastAPI()



@app.post("/files/")
async def create_files(files: List[bytes] = File(...)):
    return {"file_sizes": [len(file) for file in files]}


@app.post("/uploadfiles/")
async def create_upload_files(files: List[UploadFile] = File(...)):

    image1 = files[0]
    im1 = Image.open(image1.file)
    (width1, height1) = im1.size
    image2 = files[1]
    im2 = Image.open(image2.file)
    (width2, height2) = im2.size
    return (width1 * height1 + width2 * height2)

