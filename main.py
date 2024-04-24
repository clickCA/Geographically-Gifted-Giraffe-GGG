from typing import Union

import os
from cloud_vision import detect_landmarks
from fastapi import FastAPI, File, UploadFile,HTTPException
from fastapi.responses import FileResponse
from gemini import generate_gemini_content
from text_to_speech import text_to_speech
app = FastAPI()

@app.get("/")
async def get_api_sample():
    return {"message": "Welcome to the Geographically-Gifted-Giraffe-GGG API!"}
@app.post("/find_place")
async def find_place(file_path):
    result = detect_landmarks(file_path)
    if result is None:
        return {
  "landmark": "This is a magical place!",
  "latitude": 48.8588443,
  "longtitude": 2.2943506
}
        # raise HTTPException(status_code=404, detail="Cannot detect location")
    return result

@app.get("/gemini/{place}")
async def get_gemini_content(place: str):
    result = generate_gemini_content(place)
    return {"gemini_content": result}



@app.post("/text_to_speech")
async def get_text_to_speech(text: str):
    try:
        file_path = text_to_speech(text)
        return FileResponse(file_path, media_type="audio/wav")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))