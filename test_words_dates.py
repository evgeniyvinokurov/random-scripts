from lib.randomio import RandomIO
from lib.eightball import EightBall

import random

wordsFolder="./wordsdir"
datesFolder="./datesdir"

imagesDates = RandomIO.files(datesFolder, [".png"])
imagesWords = RandomIO.files(wordsFolder, [".png"])

for date in imagesDates:
    salt_bytes1 = RandomIO.getBytesFromImage(date)
    e81 = EightBall(salt_bytes1)
    word = e81.getOneBySalts(imagesWords)
   
    print(date)
    print(word)
    print("------------------------------------------------")


#salt_bytes2 = getBytesFromImage(image2)
#e82 = EightBall(salt_bytes2)
#two = e82.getOneByEightBall(musics)
#print(two)

#print("------------------------------------------------")

