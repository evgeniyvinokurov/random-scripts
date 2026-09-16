from lib.musicle import Musicle


# where to search for a music
dir = "/media/evgenii/TOSHIBA EXT/zhenya"

# where to store it
dirfound = "/home/evgenii/Desktop/music"


musicfiles = Musicle.library(dir, dirfound)

