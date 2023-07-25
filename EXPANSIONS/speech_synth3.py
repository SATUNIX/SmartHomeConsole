from gtts import gTTS
import os
import re

# open the file and read lines
with open("input.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    # remove trailing spaces and newline character
    line = line.strip()

    # skip blank lines
    if line == '':
        continue

    # the text you want to convert to speech
    text = line

    # language you want to use (this is English)
    language = 'en'

    # call the gTTS API
    speech = gTTS(text=text, lang=language, slow=False)

    # make a valid filename: replace spaces with underscores and remove special characters
    filename = re.sub('[^A-Za-z0-9 _-]+', '', line.replace(' ', '_')) + ".mp3"

    # save the speech audio into a file
    speech.save(filename)

    print(f"Saved speech audio to '{filename}'")

print("Done!")

