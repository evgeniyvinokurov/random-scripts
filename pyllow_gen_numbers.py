import shutil
import sys
import os
import random
from PIL import Image, ImageDraw, ImageFont

from lib.randomio import RandomIO

numbersDir ="./numbersdir/"

try:
    shutil.rmtree(numbersDir)
except:
    pass

try:
    os.makedirs(numbersDir)
except:
    pass

numbers = []

for i in range(1,10):
    number1 = random.randint(0,1000)
    number2 = random.randint(0,1000)
    numbers.append(str(number1) + "+" + str(i*number2))
       
for texti in numbers:
    RandomIO.pyllowDraw(texti, numbersDir)