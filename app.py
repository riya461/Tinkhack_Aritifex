import os 
from flask import Flask, render_template, request, redirect

UPLOAD_FOLDER = './files/input'