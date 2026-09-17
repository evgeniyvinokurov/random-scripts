import os
import hashlib
from textwrap import wrap
import shutil
import sys
import os
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

class RandomIO:	
    @staticmethod
    def getmd5(path) :
        try:
            with open(path, "rb") as f:
                bytes = f.read()
                return hashlib.md5(bytes).hexdigest()
        except: 
            pass

    @staticmethod
    def files(path, exts) :
        result = []
        for file in os.listdir(path):
            newpath = path + "/" + file
            try:
                if not os.path.isfile(newpath):	
                    result.extend(RandomIO.files(newpath, exts))
            except:
                pass
            for ext in exts:
                try:
                    if os.path.isfile(newpath) and newpath.endswith(ext):
                        result.append(newpath)
                except:
                    pass
        return result

    @staticmethod
    def dirs(path):
        result = []
        for file in os.listdir(path):
            newpath = path + "/" + file
            try:
                if not os.path.isfile(newpath):	
                    result.append(newpath)
                    result.extend(RandomIO.dirs(newpath))
            except:
                pass
        return result

    @staticmethod
    def getTextBytesFromTextDir(folder):
        string_from_files = ""	
        filestxt = RandomIO.files(folder, [".txt", ".TXT", '.html'])
        
        for file in filestxt:
            try:
                with open(file, 'r', encoding="utf-8") as f:
                    string_from_files += f.read()
            except:
                pass
        return string_from_files   

    @staticmethod	      
    def getBytesFromImage(pathToImage):	
        sums = RandomIO.getmd5(pathToImage)
        wrapped = wrap(sums, 4)	
        string_bytes = " ".join(wrapped)			
        return string_bytes
    
    @staticmethod
    def getBytesFromImages(folder):	
        images = RandomIO.files(folder, [".jpg"])
        string_bytes = ""
        
        for i in images:
            sums = RandomIO.getmd5(i)
            wrapped = wrap(sums, 5)	
            string_bytes += " "+(" ".join(wrapped))
        
        return string_bytes

    @staticmethod		
    def music(musicfolder):
        return RandomIO.files(musicfolder, [".mp3", ".MP3"])

    @staticmethod
    def pyllowDraw(text, dir):
        width, height = 400, 200
        image = Image.new("RGB", (width, height), color="white")

        # Создаем объект для рисования
        draw = ImageDraw.Draw(image)

        # 1. Получаем абсолютный путь к папке lib, где лежит этот файл utils.py
        LIB_DIR = Path(__file__).resolve().parent
        
        
        font_path = str(LIB_DIR / "PTSerif-Bold.ttf")
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

        image.save(dir + text + ".png")
        print("Картинка успешно создана!")
