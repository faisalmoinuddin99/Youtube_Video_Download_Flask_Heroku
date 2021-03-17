from flask import Flask
from pytube import YouTube

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, faisal!'

@app.route('/download')
def download():
    link = 'https://youtu.be/cl0a3i2wFcc'
    yt = YouTube( link )
    video_title = yt.title
    print(video_title)
    SAVE_PATH = "Faisal_PyTube_Downloader"
    data = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(SAVE_PATH)

    return data

if __name__ == "__main__":
    app.run(debug = True, port = 8000)