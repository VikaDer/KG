import cv2
import glob;

path = glob.glob('assets/*.jpg')
cv_img = []
for img in path:
    n = cv2.imread(img)
    cv_img.append(n)
    cv2.imshow('Image', n)
    cv2.waitKey(0)
