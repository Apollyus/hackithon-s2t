from fastapi import FastAPI, UploadFile, File
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


CLIENT_ID = "685328022387-3ird41n6oqrmg0csksu7ta58sevktttb.apps.googleusercontent.com"
CLIENT_SECRET = "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"


app = FastAPI()

# Add the session middleware to the FastAPI app - netusim co to dela xd
app.add_middleware(SessionMiddleware, secret_key="add any string...")

origins = ["*"]

app.add_middleware(CORSMiddleware, allow_origins=origins,
                   allow_credentials=True, allow_methods=["*"], allow_headers=["*"])


# Initialize the OpenAI client by putting secret API key
client = OpenAI(api_key="")

class Transcription(BaseModel):
    model: str
    file: str


oauth = OAuth()
oauth.register(
    name='google',
    server_metadata_url='https://accounts.google.com/.well-known/openid-configuration',
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    client_kwargs={
        'scope': 'email openid profile',
        'redirect_url': 'http://localhost:8000/auth'
    }
)

#Endpointy z tutorialu
@app.get("/")
def index(request: Request):
    user = request.session.get('user')
    if user:
        return RedirectResponse(url="http://localhost:5173/")

    return templates.TemplateResponse(
        name="home.html",
        context={"request": request}
    )


@app.get('/welcome')
def welcome(request: Request):
    user = request.session.get('user')
    if not user:
        return RedirectResponse('/')
    return templates.TemplateResponse(
        name='welcome.html',
        context={'request': request, 'user': user}
    )


@app.get("/login")
async def login(request: Request):
    url = request.url_for('auth')
    return await oauth.google.authorize_redirect(request, url)


@app.get('/auth')
async def auth(request: Request):
    try:
        token = await oauth.google.authorize_access_token(request)
    except OAuthError as e:
        return templates.TemplateResponse(
            name='error.html',
            context={'request': request, 'error': e.error}
        )
    user = token.get('userinfo')
    if user:
        request.session['user'] = dict(user)
    return RedirectResponse('welcome')


@app.get('/logout')
def logout(request: Request):
    request.session.pop('user')
    request.session.clear()
    return RedirectResponse('/')
# Konec endpoinjtu z tutorialu




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