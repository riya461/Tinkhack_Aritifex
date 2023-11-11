import os
import moviepy.video.io.ImageSequenceClip
def reframe():
    image_folder='static/files/output/format_video'
    fps=10

    image_files = [os.path.join(image_folder,img)
                for img in os.listdir(image_folder)
                if img.endswith(".jpeg")]
    clip = moviepy.video.io.ImageSequenceClip.ImageSequenceClip(image_files, fps=fps)
    clip.write_videofile('static/files/output/my_video.mp4')