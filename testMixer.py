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


from lib.videomix import VideoMix



class TestVideoMix:
    def test_ProbeFile(self):
        vm = VideoMix()        
        res = vm.probeFile(fileIn = "./testFiles/probeTest.mp4" )
        assert True == res

    def test_Make_ts_file(self):
        vm = VideoMix()
        fileOut = "./testFiles/probeTestOut.ts"
        
        vm.make_ts_file(fileIn="./testFiles/probeTest.mp4", fileOut=fileOut)
        res = vm.probeFile(fileIn=fileOut)
        
        assert res != False

    def test_Concatenate_video_files(self):
        vm = VideoMix()

        folder = "./testFiles/testConcatenate/"        
        alltemp_vids = glob.glob(folder + "*.ts")

        vm.concatenate_video_files(filesIn = alltemp_vids, fileOut = "./testFiles/concatenateTestOut.mp4")                        
        res = vm.probeFile(fileIn="./testFiles/concatenateTestOut.mp4")  
        
        assert res != False

    def test_Cut_segements_from_video(self):
        vm = VideoMix()

        fileOut = "./testFiles/cuttedFragment.mp4"
        vm.cut_video_segment(file="./testFiles/probeTest.mp4", start=60, end=120, fileOut=fileOut)

        duration = vm.get_video_duration(fileOut)
        assert duration == 60
