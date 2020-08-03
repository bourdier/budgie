import os
import shutil
import glob
from PIL import Image

folderPath = input("Image folder path:")

# check all files in directory
os.chdir(folderPath)
for images in glob.glob("*.jpg"):
    print(images)

# create file from date and time (36868) exif
img = Image.open(images)
exif = img.getexif()
creation_time = exif.get(36868)

# replace : characters to -
remove_characters = [":"]
for character in remove_characters:
    creation_time = creation_time.replace(character, "-")

# delete characters after space
split_string = creation_time.split(" ", 1)
substring = split_string[0]

# create new directory
try:
    os.mkdir(substring)
    print(substring,  "created")
    for f in images:
        shutil.copy(f, substring)
    print(images, "copied")
except FileExistsError:
    print(substring, "already exists")
