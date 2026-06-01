from fastapi import FastAPI, UploadFile, File
import os

app = FastAPI()

UPLOAD_FOLDER = "uploads"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.get("/")
def home():
    return {"status": "running"}

@app.post("/upload")
async def upload_image(file: UploadFile = File(...)):

    filepath = os.path.join(
        UPLOAD_FOLDER,
        file.filename
    )

    with open(filepath, "wb") as buffer:
        buffer.write(await file.read())

    return {
        "message": "uploaded",
        "filename": file.filename
    }
