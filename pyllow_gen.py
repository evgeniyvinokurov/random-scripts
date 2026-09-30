import shutil
import sys
import os
from PIL import Image, ImageDraw, ImageFont
from lib.randomio import RandomIO


wordsdir="./test/"
word = "test"

try:
    os.makedirs(wordsdir)
except:
    pass

try:
    word = sys.argv[1]
except:    
    pass

RandomIO.pyllowDraw(word, wordsdir)