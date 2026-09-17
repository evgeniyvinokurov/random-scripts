import shutil
import sys
import os
from PIL import Image, ImageDraw, ImageFont

from lib.randomio import RandomIO

# Создаем картинку 400x200 с белым фоном

dates = [
   "01.01.2027",
   "25.02.2027",
   "23.02.2027",
   "08.03.2027",
   "12.04.2027",
   "01.05.2027",
   "09.05.2027",
   "01.06.2027",
   "12.06.2027",
   "07.07.2027",
   "21.07.2027",
   "02.08.2027",
   "01.09.2027",
   "01.10.2027",
   "11.11.2027",
   "01.12.2027",
   "31.12.2027"
]

datesdir ="./datesdir/"

try:
    shutil.rmtree(datesdir)
except:
    pass

try:
    os.makedirs(datesdir)
except:
    pass

       
for texti in dates:
    RandomIO.pyllowDraw(texti, datesdir)