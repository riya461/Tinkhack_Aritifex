import os 
from flask import Flask, render_template, request
import random
from frame import frame
from reframe import reframe
from main import main, load_img, video_main
from dele_f import delete_files,file_del
file_del()

app = Flask(__name__)
li = ['starry',  'wave', 'picasso', 'sunflower']


@app.route('/', methods=['GET', 'POST'])
def index():
    
    if os.path.isfile('static/files/input/input.jpeg'):
        os.remove(os.path.join('static/files/input/input.jpeg'))

    if request.method == 'POST':
        file = request.files['file']
        option = request.form['dropdown']
        print(option)
        try:
            file.save('./static/files/input/input.jpeg')
            content_image = load_img('static/files/input/input.jpeg')
            if(option=='random'):
                option = random.choice(li)
                
            main(content_image=content_image,option=option)

        except:
            return render_template('index.html', error='Please upload a file')
    else:
        delete_files('static/files/output')
        
        
    return render_template('index.html')


@app.route('/video', methods=['GET', 'POST'])
def video():

    if os.path.isfile('static/files/input/input_video.mp4'):
                os.remove(os.path.join('static/files/input/input_video.mp4'))

    if request.method == 'POST':
        delete_files('static/files/output/video')
        delete_files('static/files/output/format_video')

        file = request.files['file']
        option = request.form['dropdown']
        print(option)
        try:
            file.save('./static/files/input/input_video.mp4')
            frame()
            directory = 'static/files/output/video'
            i=0
            if(option=='random'):
                option = random.choice(li)
            for filename in os.listdir(directory):
                f = os.path.join(directory, filename)
                # checking if it is a file
                print(f)
                if os.path.isfile(f):
                    print(f)
                    content_image = load_img(f)
                    i=i+1
                    video_main(i=i,content_image=content_image,option=option)
            reframe()

            

        except:
            return render_template('video.html', error='Please upload the video')
    else:
        delete_files('static/files/output/video')
        delete_files('static/files/output/format_video')
        delete_files('static/files/output')
        
    return render_template('video.html')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')