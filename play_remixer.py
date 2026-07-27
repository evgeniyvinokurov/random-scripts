from lib.remixer import ReMixer

from predefined_vars import video_folders_zhszh
from predefined_vars import video_folders_films
from predefined_vars import music_folders

videos = []
# videos.extend(video_folders_zhszh)
videos.extend(video_folders_films)

settings = {	
	"folders": videos,
	"mfolders": music_folders,
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
