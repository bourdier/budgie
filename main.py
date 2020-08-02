import sys, os, shutil
from PIL import Image

imgPath = input("Image name:")
imgFolderPath = input("Image folder path:")
oldPath = imgFolderPath + '\\' + imgPath

img = Image.open(oldPath)
exif = img.getexif()
creation_time = exif.get(36868)

remove_characters = [":"]
for character in remove_characters:
    creation_time = creation_time.replace(character, "-")

split_string = creation_time.split(" ", 1)
substring = split_string[0]

newPath = imgFolderPath + substring + '\\'
images = [oldPath]

try:
    os.mkdir(substring)
    print(substring,  "created")
    for f in images:
        shutil.copy(f, substring)
    print(imgPath, "copied")
except FileExistsError:
    print(substring, "already exists")
