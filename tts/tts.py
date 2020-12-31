import os

def generate_audio(audio_name, text_file):
    fo = open(text_file, "r")
    text = fo.read().replace(" ", "%20").replace("?", "\?")

    print(f"Calling: curl http://localhost:5002/api/tts\?text\={text} --output {audio_name}")
    os.system(f"curl --output audios/{audio_name} http://localhost:5002/api/tts\?text\={text}")
