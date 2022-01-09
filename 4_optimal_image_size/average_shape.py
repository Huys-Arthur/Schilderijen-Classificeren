import os
import shutil
from PIL import Image
import math

os.chdir("schilderijen")

artists = ["Picasso", "Rubens"]

imagesWidth = []
imagesHeight = []
for artist in artists:
    os.chdir(artist)

    files = os.listdir()

    for file in files:
        im = Image.open(file)
        width, height = im.size
        imagesWidth.append(width)
        imagesHeight.append(height)
    
    os.chdir("..")

print("MAX:", (max(imagesWidth), max(imagesHeight)))
print("MIN:", (min(imagesWidth), min(imagesHeight)))
print("AVG:", (sum(imagesWidth)/len(imagesWidth), sum(imagesHeight)/len(imagesHeight)))
print("MED:", (sorted(imagesWidth)[round(len(imagesWidth)/2)], sorted(imagesHeight)[round(len(imagesHeight)/2)]))

print("AVG factor:", (sum(imagesHeight)/len(imagesHeight))/(sum(imagesWidth)/len(imagesWidth)))