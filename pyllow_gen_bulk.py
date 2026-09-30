import shutil
import sys
import os
from PIL import Image, ImageDraw, ImageFont
from lib.randomio import RandomIO


wordsdir="./bulkwords/"

try:
    os.makedirs(wordsdir)
except:
    pass


words = [
    "битрикс"
]

for word in words:
    RandomIO.pyllowDraw(word, wordsdir)