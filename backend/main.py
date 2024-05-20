from flask import Flask, jsonify
from flask_cors import CORS  # import the flask_cors module
import json
from openai import OpenAI

app = Flask(__name__)
CORS(app)  # enable CORS for all routes

@app.route('/')
def home():
    client = OpenAI(api_key="sk-proj-xyp7YNkatNWb5XqMQm3lT3BlbkFJrXRw0kB4gyDcoBNhifhG")

    # Open the audio file, place here address of your audio file
    audio_file = open("C:\\aaa_programovai_kodovani\\python_projekty\\trenovani\\hacktion-speech-to-text\\samples\\zaznam-test.m4a", "rb")
    transcription = client.audio.transcriptions.create(
      model="whisper-1", 
      file=audio_file
    )

    # Convert the transcription object to a dictionary, then to a JSON string
    json_output = json.dumps(transcription.to_dict(), ensure_ascii=False)

    # Return the JSON output as a Flask response
    return jsonify(json_output)

if __name__ == '__main__':
    app.run(port=5000)