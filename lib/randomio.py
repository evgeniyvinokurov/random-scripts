import os
import hashlib
from textwrap import wrap

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
