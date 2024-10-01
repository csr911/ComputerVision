from fastapi import FastAPI, File, UploadFile
import shutil

app = FastAPI()

@app.post("/predict/")
async def predict(file: UploadFile = File(...)):
    # Save uploaded file, predict using the best model, return result
    return {"filename": file.filename}
