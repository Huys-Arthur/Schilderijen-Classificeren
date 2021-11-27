import os
import shutil
import random

def createDataset(folderName, pathSchilderijen="schilderijen", artists=["Picasso", "Rubens"], aantal = {"train": 400, "validation": 100, "test": 100}):
    os.mkdir(folderName)

    for key in aantal.keys():
        os.mkdir(folderName + '/' + key)
    
    os.chdir(pathSchilderijen)
    for artist in artists:
        os.chdir(artist)

        files = os.listdir()
        random.shuffle(files)

        length = len(files)
        
        i=0
        for file in files:
            dataset = ''
            if i < aantal.get("train"):
                dataset = "train"
            elif aantal.get("train") <= i < aantal.get("train") + aantal.get("validation"):
                dataset = "validation"
            elif aantal.get("train") + aantal.get("validation") <= i < aantal.get("train") + aantal.get("validation") + aantal.get("test"):
                dataset = "test"

            if dataset!='':
                dir = '../../' + folderName + '/' + dataset + '/' + artist
                if not os.path.isdir(dir):
                    os.mkdir(dir)

                shutil.copyfile(file, dir + '/' + str(i) + '.jpg')
            i+=1

        os.chdir("..")
    os.chdir("..")

createDataset("Picasso_Rubens_400_100_100")