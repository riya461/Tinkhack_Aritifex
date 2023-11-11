import os 
from flask import Flask, render_template, request
import random
from frame import frame
from main import main, load_img, video_main

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    li = ['starry',  'wave', 'picasso', 'sunflower']

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
        
        
    return render_template('index.html')


@app.route('/video', methods=['GET', 'POST'])
def video():


    if request.method == 'POST':
        file = request.files['file']
        try:
            file.save('./static/files/input/input_video.mp4')
            frame()
            directory = 'static/files/output/video'
            i=0
            for filename in os.listdir(directory):
                f = os.path.join(directory, filename)
                # checking if it is a file
                print(f)
                if os.path.isfile(f):
                    print(f)
                    content_image = load_img(f)
                    i=i+1
                    video_main(i=i,content_image=content_image)

            

        except:
            return render_template('video.html', error='Please upload the video')
        
        
    return render_template('video.html')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')