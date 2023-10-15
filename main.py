import cv2
import glob
from moviepy import *
import moviepy
from moviepy.editor import *

path1 = glob.glob('assets/*.jpg')
path2 = glob.glob('assets/*.mp4')
path3 = glob.glob('assets/*.mp3')
path_all = path1 + path2

cv_img = []
width = 1600
height = 900
points = (width, height)
Fps1 = 30
volume = 0.5

"""for player in path3:
    audio_path = player
audio = cv2.VideoCapture(audio_path)
ret, audio_frames = audio.read()
"""

out = cv2.VideoWriter('output.mp4', cv2.VideoWriter_fourcc(*'mp4v'), Fps1, points)


for img in path_all:
    n = cv2.imread(img)
    cv_img.append(n)
    if(img in path1):
        n = cv2.resize(n, points, interpolation= cv2.INTER_LINEAR)
        for i in range(Fps1*2):
            out.write(n)
        #cv2.imshow('Image', n)
        #cv2.waitKey(0)
    else:
        cap = cv2.VideoCapture(img)
        #if (cap.isOpened()== False): 
        #    print("Error opening video stream or file")
        #while(cap.isOpened()):
        ret = True
        num_of_img = 0
        while(ret == True and num_of_img<Fps1*6):
            num_of_img+=1
            ret, frame = cap.read()
            frame = cv2.resize(frame, points, interpolation= cv2.INTER_LINEAR)
            out.write(frame)
            #cv2.imshow('Frame',frame)
            #if cv2.waitKey(25) & 0xFF == ord('q'):
               #break
        print('Video')

#for player in path3:
#    audio_path = player
cap.release()
out.release()

audio_path = 'assets/music.mp3'
result = VideoFileClip("output.mp4")
duration = result.duration
audio = AudioFileClip('music.mp3')
audio = audio.subclip(0, duration)
audio = audio.volumex(0.5)

result.audio = CompositeAudioClip([audio])
result.write_videofile('output1.mp4')