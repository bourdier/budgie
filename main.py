import os
import shutil
import glob
from PIL import Image

folderPath = input("Image folder path:")
imglist = []

# check all files in directory
os.chdir(folderPath)
for imagesname in glob.glob("*.jpg"):
    imglist.append(imagesname)

print(imglist)

for image in imglist:

    # create file from date and time (36868) exif
    img = Image.open(image)
    exif = img.getexif()
    creation_time = exif.get(36868)

    # replace : characters to -
    remove_characters = [":"]
    for character in remove_characters:
        creation_time = creation_time.replace(character, "-")
    split_string = creation_time.split(" ", 1)  # delete characters after space
    substring = split_string[0]

    # create new directory
    try:
        os.mkdir(substring)
        print(substring,  "created")
    except FileExistsError:
        print(image, "already exists")

    
    # copy
    try:
        if os.path.isfile(substring + "\\" + image):
            yn = input("Replace ? Y/N")
            if not yn == "Y":
                continue     
              
        try: 
            shutil.copy(image, substring)
            print(image, "copied")
        except:
            pass
        
    except:
        pass