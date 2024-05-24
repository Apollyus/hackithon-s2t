from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from fastapi.responses import RedirectResponse
from typing import List
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from openai import OpenAI
from fastapi.templating import Jinja2Templates
from starlette.requests import Request
from starlette.responses import RedirectResponse
from starlette.middleware.sessions import SessionMiddleware
from authlib.integrations.starlette_client import OAuth, OAuthError
from fastapi.staticfiles import StaticFiles
from dotenv import load_dotenv
import os
import requests

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI()

# Add the session middleware to the FastAPI app - netusim co to dela xd
app.add_middleware(SessionMiddleware, secret_key="add any string...")

origins = ["*"]

app.add_middleware(CORSMiddleware, allow_origins=origins,
                   allow_credentials=True, allow_methods=["*"], allow_headers=["*"])


# Initialize the OpenAI client by putting secret API key
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class Transcription(BaseModel):
    model: str
    file: str

    




@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        # Save the uploaded file
        with open(file.filename, "wb") as f:
            f.write(contents)
        return {"filename": file.filename}
    except Exception as e:
        return JSONResponse(status_code=400, content=str(e))

@app.get("/transcribe/{filename}")
async def transcribe_file(filename: str):
    try:
        # Open the saved file
        with open(filename, "rb") as audio_file:
            # Call the transcription endpoint
            transcription = client.audio.transcriptions.create(
              model="whisper-1", 
              file=audio_file
            )

        # Convert the transcription object to a dictionary
        dict_output = transcription.to_dict()

        # Return the transcription as a JSON response
        return JSONResponse(content=dict_output)
    except Exception as e:
        return JSONResponse(status_code=400, content={"error": str(e)})
    
@app.post("/upload-react-app/")
async def upload_file_from_react_app(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        # Check if the file format is supported
        if file.filename.split('.')[-1] not in ['flac', 'm4a', 'mp3', 'mp4', 'mpeg', 'mpga', 'oga', 'ogg', 'wav', 'webm']:
            return JSONResponse(status_code=400, content={"error": "Unsupported file format. Please upload a file in one of the following formats: 'flac', 'm4a', 'mp3', 'mp4', 'mpeg', 'mpga', 'oga', 'ogg', 'wav', 'webm'"})
        # Save the uploaded file
        with open(file.filename, "wb") as f:
            f.write(contents)
        return {"filename": file.filename}
    except Exception as e:
        return JSONResponse(status_code=400, content={"error": str(e)})
    
@app.get("/api/tile/{tile_number}")
async def get_tile(tile_number: int):
    if 1 <= tile_number <= 32:
        print(f"Accessed tile: {tile_number}")
        # Replace this with the actual logic for each tile
        return {"tile": tile_number}
    else:
        raise HTTPException(status_code=404, detail="Tile not found")


response = requests.get(f'http://localhost:8000/transcribe/recording.webm')

# The .json() method converts the JSON response to a Python dictionary
data = response.json()

# Endpoint for processing the key phrase
@app.get("/proccess_teeth")
async def get_tile():
    if "citron" in data:
        print("The phrase 'citron' is in the data.")
    else:
        print("The phrase 'citron' is not in the data.")




# Function that repairs the text of output before sending to frontend. It's using GPT-4o model.
def generate_corrected_transcript(temperature, system_prompt, transcribed_text):
    response = client.chat.completions.create(
        model="gpt-4o",
        temperature=temperature,
        messages=[
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": transcribed_text
            }
        ]
    )
    return response.choices[0].message.content