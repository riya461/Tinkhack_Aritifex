import os 
from flask import Flask, render_template, request


from main import main, load_img

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():


    if request.method == 'POST':
        file = request.files['file']
        try:
            file.save('./static/files/input/input.jpeg')
            content_image = load_img('static/files/input/input.jpeg')

            main(content_image=content_image)

        except:
            return render_template('index.html', error='Please upload a file')
        
        
    return render_template('index.html')


# @app.route('/video', methods=['GET', 'POST'])
# def video():


#     if request.method == 'POST':
#         file = request.files['file']
#         try:
#             file.save('./static/files/input/input_video.mp4')
#             frame()

#         except:
#             return render_template('video.html', error='Please upload the video')
        
        
#     return render_template('video.html')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')