# flask-whisper-speech-to-text
Flask based web application that records audio and transribes it using OpenAI's Whisper API. 

This demo at the moment transcribes audio files in Turkish. You can change this settings in the app.py file to your preffered language.

Don't forget to supply your own OpenAI API key when running the code. You can do it by adding .env file to the root directory of the project and putting your key as follows:
```
# inside .env file 
api_key = "YOUR_OPENAI_API_KEY"
```
