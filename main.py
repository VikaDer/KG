import cv2
import glob

path1 = glob.glob('assets/*.jpg')
path2 = glob.glob('assets/*.mp4')
path_all = path1 + path2

cv_img = []
width = 1600
height = 900
points = (width, height)
for img in path_all:
    n = cv2.imread(img)
    cv_img.append(n)
    if(img in path1):
        n = cv2.resize(n, points, interpolation= cv2.INTER_LINEAR)
        cv2.imshow('Image', n)
        cv2.waitKey(0)
    else:
        cap = cv2.VideoCapture(img)
        if (cap.isOpened()== False): 
            print("Error opening video stream or file")
        while(cap.isOpened()):
            ret, frame = cap.read()
            if ret == True:
                cv2.imshow('Frame',frame)
                if cv2.waitKey(25) & 0xFF == ord('q'):
                    break
            else: 
                break
        print('Video')