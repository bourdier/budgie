import sys
import os
from PIL import Image

path = input("Path:")

im = Image.open(path)
exif = im.getexif()
creation_time = exif.get(36868)

def changeWord(creation_time):
    for letter in creation_time:
        if letter != ":":
            word = word.replace(letter,"-")
        return word

try:
    os.mkdir(creation_time)
    print(creation_time ,  " created ")
except FileExistsError:
    print(creation_time , " already exists")
