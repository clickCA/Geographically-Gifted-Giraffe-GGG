from typing import Union
from google.cloud import texttospeech
import os
from cloud_vision import detect_landmarks
from fastapi import FastAPI, File, UploadFile,HTTPException
from fastapi.responses import FileResponse
from gemini import generate_gemini_content, convert_md_to_text
from text_to_speech import text_to_speech
import random
app = FastAPI()

@app.get("/")
async def get_api_sample():
    return {"message": "Welcome to the Geographically-Gifted-Giraffe-GGG API!"}

@app.post("/find_place")
async def find_place(file_path: str):
    result = detect_landmarks(file_path)
    latitude = random.uniform(-90, 90)
    longitude = random.uniform(-180, 180)
    if result is None:
        return {
            "landmark": "This is a magical place!",
            "latitude": latitude ,
            "longitude": longitude
        }
    return result

@app.get("/gemini/{place}")
async def get_gemini_content(place: str):
    result = generate_gemini_content(place)
    text = convert_md_to_text(result)
    return {"gemini_content": text}



# @app.post("/text_to_speech")
# async def get_text_to_speech(text: str):
#     output_file = "speech_" + str(hash(text[:5])) + ".mp3"
#     try:
#         # file_path = text_to_speech(text)
#         client = texttospeech.TextToSpeechClient()
#         synthesis_input = texttospeech.SynthesisInput(text=text)
#         voice = texttospeech.VoiceSelectionParams(
#             language_code="en-US", ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
#         )
#         audio_config = texttospeech.AudioConfig(
#             audio_encoding=texttospeech.AudioEncoding.MP3
#         )
#         response = client.synthesize_speech(
#             input=synthesis_input, voice=voice, audio_config=audio_config
#         )
#         with open(output_file, "wb") as out:
#             # Write the response to the output file.
#             out.write(response.audio_content)
#             print("Audio content written to file", output_file)
#         return FileResponse(output_file, media_type="audio/wav")
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))