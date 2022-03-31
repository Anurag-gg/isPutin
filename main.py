from fastapi import FastAPI, UploadFile
from faceRecognition import compare

app = FastAPI()


@app.post("/")
async def create_upload_file(file: UploadFile):
    isPutin = compare(file.file)
    return {'isPutin' : isPutin}
