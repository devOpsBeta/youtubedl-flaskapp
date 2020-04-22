# This is the folder in the container.
#Do not change without updating docker-compose.yml.
dlDir = "/data/scratch/"
# This is the audio file name schema
fileFormat = "%(title)s.%(ext)s"
# Flags for youtube-dl - modify to suite your need.
# This will give you already meta and thumbnail picture in m4a format
ytdl_flags = "-f bestaudio[ext=m4a] -i --embed-thumbnail --add-metadata"
