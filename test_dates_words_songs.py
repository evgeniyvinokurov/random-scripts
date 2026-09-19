from lib.randomio import RandomIO
from lib.eightball import EightBall
from lib.musicle import Musicle

from predefined_vars import music_folders

wordsFolder="./wordsdir"
datesFolder="./datesdir"

imagesDates = RandomIO.files(datesFolder, [".png"])
imagesWords = RandomIO.files(wordsFolder, [".png"])


array = []
for music_folder in music_folders: 
    array.extend(Musicle.music_files(music_folder))

for word in imagesWords:
    salt_bytes1 = RandomIO.getBytesFromImage(word)
    e81 = EightBall(salt_bytes1)
    song = e81.getOneBySalts(array)
   
    print(song)
    print(word)
    print("------------------------------------------------")

for date in imagesDates:
    salt_bytes1 = RandomIO.getBytesFromImage(date)
    e81 = EightBall(salt_bytes1)
    song = e81.getOneBySalts(array)
   
    print(song)
    print(date)
    print("------------------------------------------------")


#salt_bytes2 = getBytesFromImage(image2)
#e82 = EightBall(salt_bytes2)
#two = e82.getOneByEightBall(musics)
#print(two)

#print("------------------------------------------------")

