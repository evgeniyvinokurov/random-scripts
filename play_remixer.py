from lib.remixer import ReMixer

from predefined_vars import video_folders_zhszh
from predefined_vars import video_folders_films
from predefined_vars import music_folders
from predefined_vars import seconds

videos = []
videos.extend(video_folders_zhszh)
# videos.extend(video_folders_films)

settings = {	
	"folders": videos,
	"mfolders": music_folders,
	"seconds": seconds,
	"flags": ["vertical", "song", "8ball"]
}

print(settings)

count = 10
i = 0

while i	< count:
	rem = ReMixer(settings)
	x = rem.run()
	i = i + 1
	

#rem.run("i")
