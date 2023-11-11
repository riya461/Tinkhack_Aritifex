import os 
from flask import Flask, render_template, request, redirect
from werkzeug.utils import secure_filename
from main import main

UPLOAD_FOLDER = './files/input/'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'POST':
        file = request.files['file']
        filename = file.filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(filename)))
        main()
        
    return render_template('index.html')



if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')