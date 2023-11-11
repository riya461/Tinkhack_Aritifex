import os 
from flask import Flask, render_template, request, redirect
from werkzeug.utils import secure_filename
import tensorflow as tf
import tensorflow_hub as hub
import numpy as np
import PIL.Image

UPLOAD_FOLDER = './files/input/'

def tensor_to_image(tensor):
  tensor = tensor*255
  tensor = np.array(tensor, dtype=np.uint8)
  if np.ndim(tensor)>3:
    assert tensor.shape[0] == 1
    tensor = tensor[0]
  return PIL.Image.fromarray(tensor)

def load_img(path_to_img):
  max_dim = 512
  img = tf.io.read_file(path_to_img)
  img = tf.image.decode_image(img, channels=3)
  img = tf.image.convert_image_dtype(img, tf.float32)

  shape = tf.cast(tf.shape(img)[:-1], tf.float32)
  long_dim = max(shape)
  scale = max_dim / long_dim

  new_shape = tf.cast(shape * scale, tf.int32)

  img = tf.image.resize(img, new_shape)
  img = img[tf.newaxis, :]
  return img
hub_model = hub.load('https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/2')
content_image = load_img('files\input\input.jpeg')
style_image = load_img('files\input\starrynight.jpg')
stylized_image = hub_model(tf.constant(content_image), tf.constant(style_image))[0]
tensor_to_image(stylized_image)
# app = Flask(__name__)
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


# @app.route('/')
# def index():

#     if request.method == 'POST':
#         file = request.files['file']
#         filename = file.filename
#         file.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(filename)))



        