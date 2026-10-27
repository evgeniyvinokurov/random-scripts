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
        vm = VideoMix({})
        options = {
            "fileIn": "./testFiles/probeTest.mp4"
        }
        
        res = vm.probeFile(options)
        assert True == res

    def test_make_ts_file(self):
        vm = VideoMix({})
        
        options = {
            "fileIn": "./testFiles/probeTest.mp4",
            "fileOut": "./testFiles/probeTestOut.ts"
        }        
        
        vm.make_ts_file(options)

        options = {
            "fileIn": "./testFiles/probeTestOut.ts"
        }
        res = vm.probeFile(options)                
        
        
        assert res != False


    def test_concatenate_video_files(self):        
        vm = VideoMix({})

        folder = "./testFiles/testConcatenate/"
        
        alltemp_vids = glob.glob(folder + "*.ts")
           
        options = {
            "filesIn": alltemp_vids,
            "fileOut": "./testFiles/concatenateTestOut.mp4"
        }      
        vm.concatenate_video_files(options)        
        
        options = {
            "fileIn": "./testFiles/concatenateTestOut.mp4"
        }
        res = vm.probeFile(options)  
        
        assert res != False
