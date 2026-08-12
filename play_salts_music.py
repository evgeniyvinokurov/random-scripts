from lib.randomio import RandomIO
from lib.eightball import EightBall

image1 = "/home/evgenii/Desktop/imagesforscan/Screenshot at 2026-07-24 13-34-52.png"
image2 = "/home/evgenii/Desktop/music folder/"

musicfolder = "/home/evgenii/Desktop/all/music folder"


musics = RandomIO.music(musicfolder)

#salt_bytes = getTextBytesFromTextDir(folder)


salt_bytes1 = RandomIO.getBytesFromImage(image1)
e81 = EightBall(salt_bytes1)
one = e81.getOneBySalts(musics)
# one = e81.getOneByEightBall(files)

print(one)
print("------------------------------------------------")


#salt_bytes2 = getBytesFromImage(image2)
#e82 = EightBall(salt_bytes2)
#two = e82.getOneByEightBall(musics)
#print(two)

#print("------------------------------------------------")

