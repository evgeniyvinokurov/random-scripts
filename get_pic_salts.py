from lib.randomio import RandomIO
from lib.eightball import EightBall
from lib.pic_service import PicsService

from predefined_vars import music_folders
from predefined_vars import text_folders

image1 = "/home/evgenii/Desktop/с мамой в городе/elka26"
# image2 = "/home/evgenii/Desktop/music folder/"

# folder = "./samples/"

files = []


#salt_bytes = getTextBytesFromTextDir(folder)

salt_bytes1 = ""

# for txtdir in text_folders:
#     salt_bytes1 += RandomIO.getTextBytesFromTextDir(txtdir)

salt_bytes1 = RandomIO.getBytesFromImages(image1)

print(salt_bytes1)
e81 = EightBall(salt_bytes1)
# one = e81.getOneBySalts(files)
ps = PicsService(e81)
ps.do_stuff()

# print(one)
print("------------------------------------------------")


#salt_bytes2 = getBytesFromImage(image2)
#e82 = EightBall(salt_bytes2)
#two = e82.getOneByEightBall(musics)
#print(two)

#print("------------------------------------------------")

