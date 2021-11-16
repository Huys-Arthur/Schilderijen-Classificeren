import os
import shutil

newFolderName = 'schilderijen-new'
procentTrain = 60
procentValidation = 20
procentTest = 20

os.chdir('schilderijen')
artists = os.listdir()
os.mkdir('../' + newFolderName)

split = ['train', 'validation', 'test']
for s in split:
    os.mkdir('../' + newFolderName + '/' + s)

for artist in artists:
    os.chdir(artist)
    files = os.listdir()

    length = len(files)
    
    i=0
    for file in files:
        dataset = ''
        if i < (length/100)*procentTrain:
            dataset = 'train'
        elif i < (length/100)*procentTrain + (length/100)*procentValidation:
            dataset = 'validation'
        else:
            dataset = 'test'

        dir = '../../' + newFolderName + '/' + dataset + '/' + artist
        if not os.path.isdir(dir):
            os.mkdir(dir)

        shutil.copyfile(file, dir + '/' + str(i) + '.jpg')
        i+=1

    os.chdir('..')