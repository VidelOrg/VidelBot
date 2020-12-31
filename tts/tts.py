import os
import sys

params = sys.argv[1:]
for flag in params:
    if flag == "--audio-name" or flag == "-a":
        audio_name = params[1]
        params = params[2:]
    if flag == "--text-file" or flag == "-t":
        text_file = params[1]
        params = params[2:]

fo = open(text_file, "r")
text = fo.read().replace(" ", "%20").replace("?", "\?")
print(text)


print(f"Calling: curl http://localhost:5002/api/tts\?text\={text} --output {audio_name}")
os.system(f"curl --output {audio_name} http://localhost:5002/api/tts\?text\={text}")
