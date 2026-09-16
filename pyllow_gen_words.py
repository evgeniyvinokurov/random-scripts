import shutil
import sys
import os
from PIL import Image, ImageDraw, ImageFont
from lib.randomio import RandomIO

# Создаем картинку 400x200 с белым фоном

words = [
    "любовь",
    "мечта",
    "пчела",
    "цветок",
    "трава",
    "краска",
    "гром",
    "подарок",
    "мотоцикл"
]

wordsdir="./wordsdir/"

try:
    shutil.rmtree(wordsdir)
except:
    pass

try:
    os.makedirs(wordsdir)
except:
    pass


font_path = './PTSerif-Bold.ttf'  
font_size = 40
font = ImageFont.truetype(font_path, font_size)
        
for texti in words:
    RandomIO.pyllowDraw(texti, font, wordsdir)