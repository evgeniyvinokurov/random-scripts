from lib.randomio import RandomIO
from lib.eightball import EightBall
from lib.musicle import Musicle

from predefined_vars import music_folders

wordsFolder = "./world_things"
imagesWords = RandomIO.files(wordsFolder, [".png"])

files = []
files = RandomIO.files("./test", [".png"])
print(files)

for word in files:
    salt_bytes1 = RandomIO.getBytesFromImage(word)
    e81 = EightBall(salt_bytes1)
    song = e81.getOneBySalts(imagesWords)

    print(song)
    print(word)
    print("------------------------------------------------")
    