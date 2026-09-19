from lib.randomio import RandomIO
from lib.eightball import EightBall
from lib.musicle import Musicle

from predefined_vars import music_folders

wordsFolder="./wordsdir"
datesFolder="./datesdir"
numbersFolder="./numbersdir"

imagesDates = RandomIO.files(datesFolder, [".png"])
imagesWords = RandomIO.files(wordsFolder, [".png"])
imagesNumbers = RandomIO.files(numbersFolder, [".png"])

tests = [
    imagesDates,
    imagesWords,
    imagesNumbers
]

for test in tests:
    for num in imagesNumbers:
        salt_bytes1 = RandomIO.getBytesFromImage(num)
        e81 = EightBall(salt_bytes1)
        song = e81.getOneBySalts(test)
    
        print(song)
        print(num)
        print("------------------------------------------------")

    for word in imagesWords:
        salt_bytes1 = RandomIO.getBytesFromImage(word)
        e81 = EightBall(salt_bytes1)
        song = e81.getOneBySalts(test)
    
        print(song)
        print(word)
        print("------------------------------------------------")

    for date in imagesDates:
        salt_bytes1 = RandomIO.getBytesFromImage(date)
        e81 = EightBall(salt_bytes1)
        song = e81.getOneBySalts(test)
    
        print(song)
        print(date)
        print("------------------------------------------------")


#salt_bytes2 = getBytesFromImage(image2)
#e82 = EightBall(salt_bytes2)
#two = e82.getOneByEightBall(musics)
#print(two)

#print("------------------------------------------------")

