import shutil
import sys
import os
from PIL import Image, ImageDraw, ImageFont
from lib.randomio import RandomIO

# Создаем картинку 400x200 с белым фоном

# words = [
#     "любовь",
#     "мечта",
#     "пчела",
#     "цветок",
#     "трава",
#     "краска",
#     "гром",
#     "подарок",
#     "мотоцикл"
# ]


words = [
    "Озеро",
    "Фонарь",
    "Скорость",
    "Блокнот",
    "Прохлада",
    "Музыка",
    "Дорога",
    "Камень",
    "Ветер",
    "Звезда"
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


for texti in words:
    RandomIO.pyllowDraw(texti, wordsdir)