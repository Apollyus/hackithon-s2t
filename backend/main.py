from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from openai import OpenAI

app = FastAPI()

origins = ["*"]

app.add_middleware(CORSMiddleware, allow_origins=origins)

class Transcription(BaseModel):
    model: str
    file: str

@app.get('/')
async def home():
    client = OpenAI(api_key="")

    # Open the audio file, place here address of your audio file
    audio_file = open("C:\\aaa_programovai_kodovani\\python_projekty\\trenovani\\hacktion-speech-to-text\\samples\\test.m4a", "rb")
    transcription = client.audio.transcriptions.create(
      model="whisper-1", 
      file=audio_file
    )

    # Convert the transcription object to a dictionary
    dict_output = transcription.to_dict()

    # Return the dictionary as a FastAPI response
    return dict_output