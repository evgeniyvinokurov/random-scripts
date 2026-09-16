from lib.randomio import RandomIO
from lib.eightball import EightBall
from lib.musicle import Musicle

from predefined_vars import music_folders
from predefined_vars import text_folders

# image1 = "./samples_img/10.jpg"
# image2 = "/home/evgenii/Desktop/music folder/"

# folder = "./samples/"
files = []

for folderm in music_folders: 
    mfiles = Musicle.music_files(folderm)
    files.extend(mfiles)


#salt_bytes = getTextBytesFromTextDir(folder)

salt_bytes1 = ""

for txtdir in text_folders:
    salt_bytes1 += RandomIO.getTextBytesFromTextDir(txtdir)

# salt_bytes1 = RandomIO.getBytesFromImage(image1)
e81 = EightBall(salt_bytes1)
# one = e81.getOneBySalts(files)
one = e81.getOneByEightBall(files)

print(one)
print("------------------------------------------------")


#salt_bytes2 = getBytesFromImage(image2)
#e82 = EightBall(salt_bytes2)
#two = e82.getOneByEightBall(musics)
#print(two)

#print("------------------------------------------------")

