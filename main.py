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

newPath = imgFolderPath + creation_time + '\\'
images = [oldPath]

try:
    os.mkdir(creation_time)
    print(creation_time,  "created")
    for f in images:
        shutil.copy(f, creation_time)
    print(newPath, "copied")
except FileExistsError:
    print(creation_time, "already exists")

# a.jpg
# C:\\Users\\Théo Jeux\\Desktop\\
