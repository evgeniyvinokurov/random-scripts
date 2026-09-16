import shutil
import sys
import os
from PIL import Image, ImageDraw, ImageFont

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


for texti in words:
    width, height = 400, 200
    image = Image.new("RGB", (width, height), color="white")

    # Создаем объект для рисования
    draw = ImageDraw.Draw(image)

    # Текст для надписи
    text = texti

    # Пробуем загрузить стандартный шрифт, если нет — используем базовый
    font_path = './PTSerif-Bold.ttf'  
    font_size = 40
    font = ImageFont.truetype(font_path, font_size)

    
    # Вычисляем координаты для центрирования текста (современный метод getbbox)
    bbox = font.getbbox(text)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    x = (width - text_width) / 2
    y = (height - text_height) / 2

    # Рисуем текст черным цветом
    draw.text((x, y), text, fill="black", font=font)

    # Сохраняем результат в файл

    image.save(wordsdir + texti + ".words.png")
    print("Картинка успешно создана!")
