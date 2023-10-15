import cv2
import glob
from moviepy import *
from moviepy.editor import *
import os
import analyze

path1 = glob.glob('assets/*.jpg')
path2 = glob.glob('assets/*.mp4')
path_all = path1 + path2
path_all.sort()


width = 1280
height = 720
points = (width, height)
Fps1 = 30
volume = 0.5

out = cv2.VideoWriter('tem_output.mp4', cv2.VideoWriter_fourcc(*'mp4v'), Fps1, points)


for img in path_all:
    if(img in path1):
        n = analyze.crop_image(img)
        for i in range(Fps1*2):
            out.write(n)
    else:
        cap = cv2.VideoCapture(img)
        ret = True
        num_of_img = 0
        while(ret == True and num_of_img<Fps1*6):
            num_of_img+=1
            ret, frame = cap.read()
            frame = cv2.resize(frame, points, interpolation= cv2.INTER_LINEAR)
            out.write(frame)
        print('Video')

cap.release()
out.release()


result = VideoFileClip("tem_output.mp4")
duration = result.duration
audio = AudioFileClip('assets/music.mp3')
audio = audio.subclip(0, duration)
audio = audio.volumex(0.5)

result.audio = CompositeAudioClip([audio])
result.write_videofile('result.mp4')
os.remove('tem_output.mp4')
