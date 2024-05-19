import json
from openai import OpenAI

client = OpenAI(api_key="sk-proj-dz3nLvTaPgYDBngaMe0qT3BlbkFJEdS7Ltcn9wGgUsFRdsBt")

audio_file = open("C:\\aaa_programovai_kodovani\\python_projekty\\trenovani\\hacktion-speech-to-text\\samples\\zaznam-test.m4a", "rb")
transcription = client.audio.transcriptions.create(
  model="whisper-1", 
  file=audio_file
)

# Convert the transcription object to a dictionary, then to a JSON string
json_output = json.dumps(transcription.to_dict(), ensure_ascii=False)

print(json_output)

# Write the JSON output to a file
with open('output.json', 'w', encoding='utf-8') as f:
    f.write(json_output)