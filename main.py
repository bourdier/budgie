import os
import shutil
import glob
import exifread
from PIL import Image

imgPath = input("Path > ")
imgFormat = input("Format > ")
imgList = []

os.chdir(imgPath)
for imgName in glob.glob("*." + imgFormat):
    imgList.append(imgName)

print(imgList)

for img in imgList:
    def process_img(path):
        f = open(path, 'rb')
        tags = exifread.process_file(f)
        info = tags["Image DateTime"]
        return str(info)
    
    exif = process_img(img)
     
    remove_characters = [":"]
    for character in remove_characters:
        exif = exif.replace(character, "-")
    splitString = exif.split(" ", 1) 
    substring = splitString[0]

    print(substring)

    try:
        os.mkdir(substring)
    except:
        pass
    
    # copy
    try:
        if os.path.isfile(substring + "\\" + img):
            yn = input(img + " already exist, replace ? Y/N")
            if not yn == "Y":
                continue     
              
        try: 
            shutil.copy(img, substring)
            print(img, "copied")
        except:
            pass
        
    except:
        pass