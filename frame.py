from moviepy.editor import VideoFileClip
import os

def extract_frames(movie,times,video):
     clip = VideoFileClip(movie)
     for t in times:
          imgpath = os.path.join(video, '{}.png'.format(int(t*clip.fps))) 
          clip.save_frame(imgpath,t)
          
movie='static/files/test/input.mp4' 
video='static/files/output/video' 
clip = VideoFileClip(movie)
times =[i/(10) for i in range(int(10*clip.duration))]
extract_frames(movie,times,video)
