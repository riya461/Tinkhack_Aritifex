import os 
from flask import Flask, render_template, request, redirect
from werkzeug.utils import secure_filename
from main import main


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'POST':
        file = request.files['file']
        filename = file.filename
        file.save('./static/files/input/input.jpeg')
        if filename.endswith('.jpeg') :
            main()
        
        
    return render_template('index.html')



if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')