import openai

API_KEY = "YOUR_API_KEY"
openai.api_key = API_KEY
audio_file = open("audio1.m4a", "rb") # replace with your own audio file
transcript = openai.Audio.translate("whisper-1", audio_file)

print(transcript)