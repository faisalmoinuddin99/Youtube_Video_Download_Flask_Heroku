from flask import Flask, render_template, request
from pytube import YouTube
from pytube.cli import on_progress

app = Flask(__name__)



@app.route('/', methods= ["GET","POST"])
def home():

    if request.method == "POST":
        # print(request.form) ImmutableMultiDict([('youtube_link', 'https://youtu.be/jWtztbHctl4')])
        myDict = request.form
        print(myDict)
        yt_link = myDict['youtube_link'] # url
        disk_link = myDict['disk_link']
    
        try:
            yt = YouTube(yt_link, on_progress_callback=on_progress)
            video_title = yt.title
            print("Title " + video_title)
            
           
            SAVE_PATH = disk_link
            # data = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(SAVE_PATH)
            # .download(SAVE_PATH)
            stream = yt.streams.first()
            stream.download(SAVE_PATH)

        except Exception  as error:
            error_string = repr(error)          
            return render_template('show.html', error_string = error_string)     
              
        return render_template('show.html', video_title = video_title)

    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/test')
def test():
    return render_template('test.html')




if __name__ == "__main__":
    app.run(debug = True, port = 8000)