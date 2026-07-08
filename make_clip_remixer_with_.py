from lib.remixer import ReMixer
from lib.randomio import RandomIO

settings = {	
	"folders": ["/home/evgenii/2023","/home/evgenii/2024","/home/evgenii/2025", "/media/evgenii/TOSHIBA EXT/zhenya/zhszh", "/media/evgenii/85799339-6cf7-41b9-902d-ac6601c1dc21/2026"],	
	"mfolders": ["/home/evgenii/Desktop/all/music folder"],
	"seconds": [1, 1.5, 1.1, 0.8, 0.6, 0.67, 0.4, 2.1, 2.4],	
	"flags": ["horizontal", "song", "8ball"]
}

txts = "./textsdir/"
salt_bytes1 = RandomIO.getTextBytesFromTextDir(txts)

settings["salts"] = salt_bytes1

rem = ReMixer(settings)

count = 10
i = 0

while i	< count:
	x = rem.run()
	i = i + 1
	

#rem.run("i")
