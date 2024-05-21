from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from typing import List
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from openai import OpenAI


app = FastAPI()

origins = ["*"]

app.add_middleware(CORSMiddleware, allow_origins=origins)

client = OpenAI(api_key="")

class Transcription(BaseModel):
    model: str
    file: str

@app.get('/')
async def home():
    

    # Open the audio file, place here address of your audio file
    audio_file = open("C:\\aaa_programovai_kodovani\\python_projekty\\trenovani\\hacktion-speech-to-text\\samples\\test.m4a", "rb")
    transcription = client.audio.transcriptions.create(
      model="whisper-1", 
      file=audio_file
    )

    # Convert the transcription object to a dictionary
    dict_output = transcription.to_dict()

    # Post-process the text output
    system_prompt = "You are bot that repairs transcripted voice to text. The provided text may have some misspellings which you have to repair, but do not force it to change. If you do not know what's that, just leave it alone. Most of provided text is in czech. Do not forget interpunction and special characters"
    dict_output['text'] = generate_corrected_transcript(0, system_prompt, dict_output['text'])

    # Return the dictionary as a FastAPI response
    return dict_output

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

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        # Now you can use the contents of the file
        # For example, you can save it to a file
        with open(file.filename, "wb") as f:
            f.write(contents)
        return {"filename": file.filename}
    except Exception as e:
        return JSONResponse(status_code=400, detail=str(e))