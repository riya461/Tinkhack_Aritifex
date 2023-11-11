from moviepy.editor import VideoFileClip
import os


def extract_frames(movie,times,video):
    clip = VideoFileClip(movie)
    i=0
    print(clip.duration)
    d=clip.duration
    for t in times:
        i=i+1
        imgpath = os.path.join(video, '{}.png'.format(i)) 
        clip.save_frame(imgpath,t)

        

    

def frame():
    
    movie='static/files/input/input_video.mp4' 
    video='static/files/output/video' 
    clip = VideoFileClip(movie)
    
    print(clip.duration)
    
    times =[i/(15) for i in range(int(15*clip.duration))]

    extract_frames(movie,times,video)


