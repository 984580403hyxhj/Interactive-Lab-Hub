echo "What is your phone number?" | festival --tts
arecord -D hw:1,0 -f cd -c1 -r 16000 -d 5 -t wav recorded_mono.wav
python3 test_words.py recorded_mono.wav
