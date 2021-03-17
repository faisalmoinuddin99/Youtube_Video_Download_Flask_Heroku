from pytube import YouTube



link = 'https://youtu.be/YKLX3QbKBg0'
yt = YouTube( link )

video_title = yt.title
print(video_title)
SAVE_PATH = "Faisal_PyTube_Downloader"
yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(SAVE_PATH)