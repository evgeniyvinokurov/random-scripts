import sys
import os
import glob
import random
import json

# getting the name of the directory
# where the this file is present.
current = os.path.dirname(os.path.realpath(__file__))
 
# Getting the parent directory name
# where the current directory is present.
parent = os.path.dirname(current)
parentmore = os.path.dirname(parent)
 
# adding the parent directory to 
# the sys.path.
sys.path.append(parentmore)


from lib.VideoCutsAndJoin import VideoCutsAndJoin


class TestVideoMix:
    def test_Probe_file(self):
        res = VideoCutsAndJoin.probe_file(fileIn = "./testFiles/probeTest.mp4" )
        assert True == res

    def test_Make_ts_file(self):
        fileOut = "./testFiles/probeTestOut.ts"
        
        VideoCutsAndJoin.make_ts_file(fileIn="./testFiles/probeTest.mp4", fileOut=fileOut)
        res = VideoCutsAndJoin.probe_file(fileIn=fileOut)
        
        assert res != False

    def test_Concatenate_video_files(self):
        folder = "./testFiles/testConcatenate/"        
        alltemp_vids = glob.glob(folder + "*.ts")

        VideoCutsAndJoin.concatenate_video_files(filesIn = alltemp_vids, fileOut = "./testFiles/concatenateTestOut.mp4")                        
        res = VideoCutsAndJoin.probe_file(fileIn="./testFiles/concatenateTestOut.mp4")  
        
        assert res != False

    def test_Cut_segements_from_video(self):
        fileOut = "./testFiles/cuttedFragment.mp4"
        VideoCutsAndJoin.cut_video_segment(file="./testFiles/probeTest.mp4", start=60, end=120, fileOut=fileOut)

        duration = VideoCutsAndJoin.get_video_duration(fileOut)
        assert duration == 60

    def test_Add_audio(self):
        audio = "./testFiles/Nirvana_-_Do_You_Love_Me.mp3"
        fileOut = "./testFiles/addedMusicClip.mp4"

        VideoCutsAndJoin.append_audio_to_video(fileIn="./testFiles/probeTest.mp4", audio=audio, fileOut=fileOut)
        res = VideoCutsAndJoin.probe_file(fileIn=fileOut)  
                
        assert res != False