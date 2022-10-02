from pytube import YouTube
from sys import argv

link = argv[1]
yt = YouTube(link)

print("Title:", yt.title)
print("View:", yt.views)

ydown = yt.streams.get_highest_resolution()
ydown.download('./YouTubeDownloader/download')
