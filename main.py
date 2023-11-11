import tensorflow as tf
import tensorflow_hub as hub
import numpy as np
import PIL.Image

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


def main(content_image):
    hub_model = hub.load('https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/2')
    style_image = load_img('static/files/input/styleimg/starrynight.jpg')
    stylized_image = hub_model(tf.constant(content_image), tf.constant(style_image))[0]
    img = tensor_to_image(stylized_image)
    img.save('static/files/output/output.jpeg')

def video_main(content_image,i):
    print("Entered video main")
    hub_model = hub.load('https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/2')
    style_image = load_img('static/files/input/styleimg/starrynight.jpg')
    stylized_image = hub_model(tf.constant(content_image), tf.constant(style_image))[0]
    img = tensor_to_image(stylized_image)
    print("val")
    img.save('static/files/output/format_video/{}.jpeg'.format(i))
