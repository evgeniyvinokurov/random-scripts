from lib.remixer import ReMixer

settings = {	
	"folders": ["/home/evgenii/2023","/home/evgenii/2024","/home/evgenii/2025", "/media/evgenii/TOSHIBA EXT/zhenya/zhszh", "/media/evgenii/85799339-6cf7-41b9-902d-ac6601c1dc21/2026"],	
	"mfolders": ["/home/evgenii/Desktop/all/music folder"],
	"seconds": [1, 1.5, 1.7, 2,3, 4.2, 4.6, 5, 2.5, 3.4],
	"flags": ["horizontal", "song", "8ball"]
}

print(settings)

count = 10
i = 0

while i	< count:
	rem = ReMixer(settings)
	x = rem.run()
	i = i + 1
	

#rem.run("i")
