from lib.remixer import ReMixer

from predefined_vars import video_folders_zhszh
from predefined_vars import video_folders_films
from predefined_vars import music_folders
from predefined_vars import seconds

video_folders = []
video_folders.extend(video_folders_zhszh)
# video_folders.extend(video_folders_films)

settings = {	
	"folders": video_folders,
	"mfolders": music_folders,
	"seconds": seconds,
	"flags": ["vertical", "song", "8ball", "que"]
}


print(settings)
rem = ReMixer(settings)
x = rem.run()	

#rem.run("i")
