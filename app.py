import os 
from flask import Flask, render_template, request, redirect

UPLOAD_FOLDER = './files/input/'


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():