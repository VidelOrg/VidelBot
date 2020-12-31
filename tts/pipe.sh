cd video-maker
node index.js > pipe_example.txt
cd ..
python3 tts.py -t pipe_example.txt -a teste-pipe.wav
