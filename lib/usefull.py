import os
import hashlib
from textwrap import wrap

import os
import hashlib
import sys
import shutil

from pathlib import Path
from lib.randomio import RandomIO

import ffmpeg
from moviepy import VideoFileClip

from html.parser import HTMLParser
from datetime import date
import time

class Usefull:	

    @staticmethod
    # cutting audio to the size of video and appending to video
    def appendAudio(videofile, audiofile, out):
        with VideoFileClip(videofile) as clip:
            audio_input = ffmpeg.input(audiofile)
            audio_cut = audio_input.audio.filter('atrim', duration=clip.duration)
            audio_output = ffmpeg.output(audio_cut, audiofile + "-test.mp3")
            ffmpeg.run(audio_output)

            video = ffmpeg.input(videofile)
            audio = ffmpeg.input(audiofile+"-test.mp3")
            ffmpeg.concat(video, audio, v=1, a=1).output(out).run()

    # seaarching for duplicates, using extensions param and flags array
    # printing duplicates and stores them in folder
    @staticmethod
    def duplicates(params, flags, dir, duplicatesdir):
        movefiles = False

        if len(params) > 0:
            exts = params
        else:
            exts = [".jpg"]

        if "move" in flags:
            movefiles = True

        md5hashes = []
        dublicates = []

        for file in RandomIO.files(dir, exts):
            md5 = RandomIO.getmd5(file)
            if md5 not in md5hashes:
                md5hashes.append(md5)
            else:
                dublicates.append(file)

        if movefiles: 
            try:
                os.makedirs(duplicatesdir)
            except:
                pass
            for file in dublicates:
                f = Path(file)		
                newdir = duplicatesdir + str(f.parent).replace(dir, "")		
                try:
                    os.makedirs(newdir)
                except:
                    pass
                print(file)
                print(newdir)
                shutil.move(file, newdir)
        else:
            print(dublicates)
    
    # makes sitemap.xml
    @staticmethod
    def links(html):      
        class MyHTMLParser(HTMLParser):
            allhtml = ""
            baseurl = "http://site.ru"
            todate = date.fromtimestamp(time.time())

            def handle_starttag(self, tag, attrs):
                for attr in attrs:
                    if (tag == "a" and attr[0] == "href"):
                        self.allhtml +="<url><loc>" + self.baseurl + attr[1] + "</loc><lastmod>" + self.todate.isoformat() + "</lastmod></url>\r\n"

        parser = MyHTMLParser()
        parser.feed(html)
        print(parser.allhtml)

    @staticmethod
    def remove_spaces(str):
        result = str.replace(")","")
        result = result.replace("(","")
        result = result.replace("'","")
        return result.replace(" ", "")	