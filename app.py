from flask import Flask, redirect, request, url_for
from flask import render_template
import openai
from dotenv import load_dotenv
import os

# get the current absolute path
current_path = os.path.dirname(__name__)
abs_path = os.path.abspath(current_path) 

# load environment files for the project
load_dotenv(os.path.join(abs_path, '.env'))

# add your own OpenAI api key to .env file
openai.api_key = os.environ.get("api_key") 

app = Flask(__name__)

# Whisper API audio transcription - you can set the language according to your preference
def transcribe_audio(audio_file_path):
    with open(audio_file_path, 'rb') as audio_file:
        transcription = openai.Audio.transcribe(model="whisper-1", file=audio_file, language="tr")
    return transcription['text']

@app.route("/")
def index():
    return render_template("index.html")

# this route is called by the frontend app.js file
@app.route("/upload_audio", methods=['POST', 'GET'])
def upload():
    if request.method == "POST":
        # request.files['audio_data'] is return from the front-end
        f = request.files['audio_data']
        with open('audio.wav', 'wb') as audio:
            f.save(audio)
        print('Backend message: file uploaded successfully') 

        # generate text from audio file using OpenAI whisper
        transcribed_text = transcribe_audio("./audio.wav")

        # this is returned to the front-end
        return transcribed_text
    
    return redirect(url_for('index'))

# run the flask app
if __name__ == "__main__":
    app.run()