from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from openai import OpenAI
import json

origins = ["*"]

app = FastAPI()

app.add_middleware(CORSMiddleware, allow_origins=origins)

class Transcription(BaseModel):
    model: str
    file: str

@app.get('/')
async def home():
    client = OpenAI(api_key="sk-proj-8ihZYyihRtEkUUzYfm09T3BlbkFJzb7MVi8JzZEkwjbRP4pe")

    # Open the audio file, place here address of your audio file
    audio_file = open("C:\\aaa_programovai_kodovani\\python_projekty\\trenovani\\hacktion-speech-to-text\\samples\\zaznam-test.m4a", "rb")
    transcription = client.audio.transcriptions.create(
      model="whisper-1", 
      file=audio_file
    )

    # Convert the transcription object to a dictionary, then to a JSON string
    json_output = json.dumps(transcription.to_dict(), ensure_ascii=False)

    # Return the JSON output as a FastAPI response
    return json_output