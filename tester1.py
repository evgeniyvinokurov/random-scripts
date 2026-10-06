from pathlib import Path 

from lib.randomio import RandomIO
from lib.eightball import EightBall

class Tester:
    @staticmethod
    def to_check(word, cat, db):
        wordsFolder = db
        testFolder = "./test/"
        
        imagesWords = RandomIO.files(wordsFolder, [".png"]) 
        res = RandomIO.search_by_name(testFolder, word)

        if len(res) > 0:            
            salt_bytes1 = RandomIO.getBytesFromImage(res[0])
            e81 = EightBall(salt_bytes1)
            choosen = e81.getOneBySalts(imagesWords)
        else:
            RandomIO.pyllowDraw(word, testFolder)
            choosen = testFolder + word + ".png"
        
        if cat in choosen:
            return True

        return False
    
    @staticmethod
    def test_current_base(): 
        dbs = [
            "./db/db1",
            "./db/db2",
            "./db/db3",
            "./db/db4",
            "./db/db5",
        ]

        for db in dbs:
            tests = ""

            tests += "+" if Tester.to_check("ворон", "птицы", db)  else "-"
            tests += "+" if Tester.to_check("кот", "животные", db)  else "-"
            tests += "+" if Tester.to_check("лось", "животные", db)  else "-"
            tests += "+" if Tester.to_check("21мая", "области", db)  else "-"
            tests += "+" if Tester.to_check("22мая", "гордость", db)  else "-"
            tests += "+" if Tester.to_check("оса", "животные", db)  else "-"
            tests += "+" if Tester.to_check("шакал", "животные", db)  else "-"
            tests += "+" if Tester.to_check("обезьяна", "животные", db)  else "-"

            print(tests)

        
Tester.test_current_base()