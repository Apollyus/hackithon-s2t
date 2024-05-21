from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from fastapi.responses import RedirectResponse
from typing import List
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from openai import OpenAI


app = FastAPI()

origins = ["*"]

app.add_middleware(CORSMiddleware, allow_origins=origins,
                   allow_credentials=True, allow_methods=["*"], allow_headers=["*"])


# Initialize the OpenAI client by putting secret API key
client = OpenAI(api_key="")

class Transcription(BaseModel):
    model: str
    file: str

@app.get("/")
def redirect_to_existing_endpoint():
    return RedirectResponse(url='/transcribe')

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        # Save the uploaded file
        with open(file.filename, "wb") as f:
            f.write(contents)
        return {"filename": file.filename}
    except Exception as e:
        return JSONResponse(status_code=400, detail=str(e))

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
        return JSONResponse(status_code=400, detail=str(e))




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