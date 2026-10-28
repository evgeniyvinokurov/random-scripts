from pathlib import Path
import math
import random
import os
from lib.VideoCutsAndJoin import VideoCutsAndJoin

from lib.eightball import EightBall

from lib.randomio import RandomIO

from predefined_vars import video_folders_zhszh
from predefined_vars import music_folders
from predefined_vars import seconds

# if __name__ == "__main__":

# get video files 
# get music files 
# get randomizer 
# get time or song by randomizer
# cicle 
# ? get random video by randomizer  
# ? cut one piece by random time
# ? make ts file
# ? cicle while time or song
# join files
# add audio 

folderOutput="./splits/videcutsandjoin/"
dir_path = Path(folderOutput)
dir_path.mkdir(parents=True, exist_ok=True)

filesofvideos = []

for folder in video_folders_zhszh:
    filesofvideos.extend(RandomIO.files(folder, [".mp4", ".avi"]))


filesofmusic = []

for folder in music_folders:
    filesofmusic.extend(RandomIO.files(folder, [".mp3", ".m4a"]))


e81 = EightBall()


def makeTsFilesOneClip(fileOut):
    filesoftsvideos = RandomIO.files(folderOutput, [".ts"])
    VideoCutsAndJoin.concatenate_video_files(filesoftsvideos, fileOut)

           
song = e81.random(filesofmusic)
time = 30
duration = 0
count = 0

while duration < time:
    video = e81.random(filesofvideos)
    duration_file = VideoCutsAndJoin.get_video_duration(video)
    if isinstance(duration_file,(int, float)):
        start = e81.randomFromRange(0, duration_file)
        duration_segment = 999999
        end = 0

        while start + duration_segment > end:
            duration_segment = e81.random(seconds)
            end = start + duration_segment

        fileOutSegment = folderOutput + "tempfile" + str(count) + ".mp4"
        fileOutSegmentTs = folderOutput + "tempfile" + str(count) + ".ts"

        VideoCutsAndJoin.cut_video_segment(video, start, end, fileOut=fileOutSegment)
        VideoCutsAndJoin.make_ts_file(fileOutSegment, fileOutSegmentTs)

        duration = duration + duration_segment
    count = count + 1


name = e81.randomFromRange(0, 100000)
fileOut = folderOutput + str(name) + "_final.mp4"
fileOutWidthAudio = folderOutput + str(name) + "_a_final.mp4"

makeTsFilesOneClip(fileOut)

fileIn = fileOut
VideoCutsAndJoin.append_audio_to_video(fileIn, song, fileOutWidthAudio)

print("ok")