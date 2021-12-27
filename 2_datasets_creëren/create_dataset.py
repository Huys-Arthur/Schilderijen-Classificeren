import os
import shutil
import random

def createDataset(folderName, pathSchilderijen="schilderijen", artists=["Picasso", "Rubens"], aantal = {"train": 400, "validation": 100, "test": 100}):
    os.mkdir(folderName)

    for key in aantal.keys():
        os.mkdir(folderName + '/' + key)
    
    print(os.getcwd())
    os.chdir(pathSchilderijen)
    for artist in artists:
        os.chdir(artist)

        files = os.listdir()
        random.shuffle(files)

        length = len(files)

        for i in range(aantal.get("train") + aantal.get("validation") + aantal.get("test")):
            dataset = ''
            if i < aantal.get("test"):
                dataset = "test"
            elif aantal.get("test") <= i < aantal.get("test") + aantal.get("validation"):
                dataset = "validation"
            elif aantal.get("test") + aantal.get("validation") <= i < aantal.get("test") + aantal.get("validation") + aantal.get("train"):
                dataset = "train"

            if dataset!='':
                dir = '../../' + folderName + '/' + dataset + '/' + artist
                if not os.path.isdir(dir):
                    os.mkdir(dir)
                if dataset=="train":
                    shutil.copyfile(files[(aantal.get("validation") + aantal.get("test") - 1) + i%(length - aantal.get("validation") - aantal.get("test"))], dir + '/' + str(i) + '.jpg')
                else:
                    shutil.copyfile(files[i%length], dir + '/' + str(i) + '.jpg')

        os.chdir("..")
    os.chdir("..")

#createDataset("datasets/Picasso_Rubens_400_100_100")
#createDataset("datasets/Picasso_Rubens_VanGogh_400_100_100", pathSchilderijen="schilderijen", artists=["Picasso", "Rubens", "VanGogh"])
#createDataset("datasets/Picasso_Rubens_VanGogh_Mondriaan_220_55_55", pathSchilderijen="schilderijen", artists=["Picasso", "Rubens", "VanGogh", "Mondriaan"], aantal = {"train": 220, "validation": 55, "test": 55})

#oversampling
#createDataset("datasets/Picasso_Rubens_VanGogh_1000_100_100_oversampling", pathSchilderijen="schilderijen", artists=["Picasso", "Rubens", "VanGogh"], aantal = {"train": 1000, "validation": 100, "test": 100})
#createDataset("datasets/Picasso_Rubens_VanGogh_Mondriaan_1000_50_50", pathSchilderijen="schilderijen", artists=["Picasso", "Rubens", "VanGogh", "Mondriaan"], aantal = {"train": 1000, "validation": 50, "test": 50})
createDataset("datasets/Picasso_Rubens_VanGogh_Mondriaan_rembrandt_AI_1000_20_20", pathSchilderijen="schilderijen", artists=["Picasso", "Rubens", "VanGogh", "Mondriaan", "Rembrandt", "AI"], aantal = {"train": 1000, "validation": 20, "test": 20})

#weighted sampling
#createDataset("datasets/Picasso_weightedsampling", pathSchilderijen="schilderijen", artists=["Picasso"], aantal = {"train": 1400, "validation": 20, "test": 20})
#createDataset("datasets/Rubens_weightedsampling", pathSchilderijen="schilderijen", artists=["Rubens"], aantal = {"train": 350, "validation": 20, "test": 20})
#createDataset("datasets/VanGogh_weightedsampling", pathSchilderijen="schilderijen", artists=["VanGogh"], aantal = {"train": 700, "validation": 20, "test": 20})
#createDataset("datasets/Mondriaan_weightedsampling", pathSchilderijen="schilderijen", artists=["Mondriaan"], aantal = {"train": 280, "validation": 20, "test": 20})
#createDataset("datasets/Rembrandt_weightedsampling", pathSchilderijen="schilderijen", artists=["Rembrandt"], aantal = {"train": 175, "validation": 20, "test": 20})
#createDataset("datasets/AI_weightedsampling", pathSchilderijen="schilderijen", artists=["AI"], aantal = {"train": 70, "validation": 20, "test": 20})