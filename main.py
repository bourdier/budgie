import sys
import os
from PIL import Image

path = input("Path:")

im = Image.open(path)
exif = im.getexif()
creation_time = exif.get(36868)

remove_characters = [":"]
for character in remove_characters:
    creation_time = creation_time.replace(character, "-")

try:
    os.mkdir(creation_time)
    print(creation_time ,  "created ")
except FileExistsError:
    print(creation_time , "already exists")
