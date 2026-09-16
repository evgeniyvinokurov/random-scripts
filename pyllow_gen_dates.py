import shutil
import sys
import os
from PIL import Image, ImageDraw, ImageFont

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
    width, height = 400, 200
    image = Image.new("RGB", (width, height), color="white")

    # Создаем объект для рисования
    draw = ImageDraw.Draw(image)

    # Текст для надписи
    text = texti

    # Пробуем загрузить стандартный шрифт, если нет — используем базовый
    font = ImageFont.load_default(size=60)
    
    # Вычисляем координаты для центрирования текста (современный метод getbbox)
    bbox = font.getbbox(text)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    x = (width - text_width) / 2
    y = (height - text_height) / 2

    # Рисуем текст черным цветом
    draw.text((x, y), text, fill="black", font=font)

    # Сохраняем результат в файл

    image.save(datesdir + texti + ".dates.png")
    print("Картинка успешно создана!")
