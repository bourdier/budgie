import sys
import os
from PIL import Image

path = input("Path:")

im = Image.open(path)
exif = im.getexif()
creation_time = exif.get(36867)

print(creation_time)
