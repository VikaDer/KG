import cv2
import glob
import os

#fname = r"C:\...\Library\etc\haarcascades\haarcascade_frontalface_default.xml"

#print(os.path.isfile(fname))

path = glob.glob('faces/*.jpg')
def_height: int = 720
def_width: int = 1280
points = (def_width, def_height)

def define_face(img: str):
    picture = cv2.imread(img)
    gray = cv2.cvtColor(picture, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    print(faces)
    if (len(faces) == 0):
        print('end')
        a = [-1, -1, -1, -1]
        return a
    #if(faces == []):
    #   faces = [-1, -1, -1, -1]
    else: return faces[0]



def crop_image(img: str):
    n = cv2.imread(img)
    print(define_face(img))
    (x, y, w, h) = define_face(img)
    if(x==-1):
        n = cv2.resize(n, points, interpolation= cv2.INTER_LINEAR)
        return n
    else:
        centx = x+w//2 
        centy = y+h//2
        print(centx, centy)
        height, width, channels = n.shape
        if(height>def_height and width>def_width):

            left_horizont = centx - def_width//2
            right_horizont = (width - centx) - def_width//2
            up_vertical = centy - def_height//2
            down_vertical = (height - centy) - def_height//2
            col_1 = centx - def_width//2
            col_2 = centx + def_width//2
            row_1 = centy - def_height//2
            row_2 = centy + def_height//2
            if(left_horizont<=0):
                col_1 = 0
                col_2 = centx + (def_width//2) - left_horizont
            if(right_horizont<=0):
                col_1 = centx - def_width//2 + right_horizont
                col_2 = width
            if(up_vertical<=0):
                row_1 = 0
                row_2 = centy + (def_height//2) - up_vertical
            if(down_vertical<=0):
                row_1 = centy - def_height//2 + down_vertical
                row_2 = height
            print(row_1, row_2, col_1, col_2)
            #horizontal: int = def_width//2
            #vertical: int = def_height//2
            cropped = n[ row_1:row_2, col_1:col_2]
            #cv2.imshow("cropped", cropped)
            #cv2.waitKey(0)
        return cropped

#for img in path:
#    result = crop_image(img)
#    cv2.imshow('img', result)
#    cv2.waitKey(0)
