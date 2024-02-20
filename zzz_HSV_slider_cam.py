### version ###
# 20240220.1028 : add print string

import cv2
import numpy as np
import math

### Cam Window ####################################################################################
cap = cv2.VideoCapture(1)

vid_w = int(cap.get(3))
vid_h = int(cap.get(4))
vid_fps = int(cap.get(cv2.CAP_PROP_FPS))
vid_scale = 0.4
print(f'video size = {vid_w} x {vid_h}\nframerate = {vid_fps}')

mask_rgb1 = np.zeros((int(vid_h*vid_scale), int(vid_w*vid_scale), 3), np.uint8)
mask_rgb2 = np.zeros((int(vid_h*vid_scale), int(vid_w*vid_scale), 3), np.uint8)

### Slider Window #################################################################################
# Screen Setup
width = 400
heigth = 300
LRsplit = 20 # Left-Right screen split

w_split = math.floor(width*(LRsplit/100))

h_split = heigth/6
h_splita1 = 0
h_splita2 = math.floor(h_split)
h_splita3 = math.floor(h_split*2)
h_splita4 = math.floor(heigth/2) # half
h_splitb1 = math.floor(heigth/2) # half
h_splitb2 = math.floor(h_split*4)
h_splitb3 = math.floor(h_split*5)
h_splitb4 = math.floor(heigth)

# Window and Value Slider setup
img = np.zeros((heigth, width, 3), np.uint8) # create blank image (300*250 3channel)
cv2.namedWindow('HSV Color Slider')

def consol_debug(_h, _s, _v):
    print(f'HSV = {_h}, {_s}, {_v}')

H1,S1,V1 = 0,0,0
H2,S2,V2 = 0,0,0

def on_trackbar_H1(value):
    global H1
    global S1
    global V1
    H1 = value
    consol_debug(H1, S1, V1)
def on_trackbar_S1(value):
    global H1
    global S1
    global V1
    S1 = value
    consol_debug(H1, S1, V1)
def on_trackbar_V1(value):
    global H1
    global S1
    global V1
    V1 = value
    consol_debug(H1, S1, V1)

def on_trackbar_H2(value):
    global H2
    global S2
    global V2
    H2 = value
    consol_debug(H2, S2, V2)
def on_trackbar_S2(value):
    global H2
    global S2
    global V2
    S2 = value
    consol_debug(H2, S2, V2)
def on_trackbar_V2(value):
    global H2
    global S2
    global V2
    V2 = value
    consol_debug(H2, S2, V2)

cv2.createTrackbar('H1', 'HSV Color Slider', 0, 180, on_trackbar_H1)
cv2.createTrackbar('S1', 'HSV Color Slider', 0, 255, on_trackbar_S1)
cv2.createTrackbar('V1', 'HSV Color Slider', 0, 255, on_trackbar_V1)
cv2.createTrackbar('H2', 'HSV Color Slider', 0, 180, on_trackbar_H2)
cv2.createTrackbar('S2', 'HSV Color Slider', 0, 255, on_trackbar_S2)
cv2.createTrackbar('V2', 'HSV Color Slider', 0, 255, on_trackbar_V2)


### Main ##########################################################################################
while cap.isOpened():
    check, frame = cap.read()
    if check != True:
        print('>> video ended or not available')
        break

    frame = cv2.resize(frame, (int(vid_w*vid_scale),int(vid_h*vid_scale)))
    frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_hsv = np.array([H1, S1, V1]) # hsv mask lower bound color
    upper_hsv = np.array([H2, S2, V2]) # hsv mask upper bound color
  
    mask_hsv = cv2.inRange(frame_hsv, lower_hsv, upper_hsv) # create simple mask

    mask_hsv_org = cv2.bitwise_and(frame, frame, mask = mask_hsv) # create mask with original image

    
    # show window
    cv2.imshow('Raw Webcam', frame)
    cv2.imshow('HSV', frame_hsv)
    cv2.imshow('Masked', mask_hsv_org)

    cv2.imshow('HSV Color Slider', img)

    if cv2.waitKey(1) & 0xFF == ord('e'):
        break
    
    hue1 = cv2.getTrackbarPos('H1', 'HSV Color Slider')
    saturation1 = cv2.getTrackbarPos('S1', 'HSV Color Slider')
    value1 = cv2.getTrackbarPos('V1', 'HSV Color Slider')

    hue2 = cv2.getTrackbarPos('H2', 'HSV Color Slider')
    saturation2 = cv2.getTrackbarPos('S2', 'HSV Color Slider')
    value2 = cv2.getTrackbarPos('V2', 'HSV Color Slider')

    img[        0:h_splita4, w_split:width] = [hue1, saturation1, value1] # pixel value [heigth range:width range]
    img[h_splitb1:heigth   , w_split:width] = [hue2, saturation2, value2]

    img[h_splita1:h_splita2, 0:w_split] = [hue1, 255, 255]
    img[h_splita2:h_splita3, 0:w_split] = [hue1, saturation1, 255]
    img[h_splita3:h_splita4, 0:w_split] = [0, 0, value1]
    img[h_splitb1:h_splitb2, 0:w_split] = [hue2, 255, 255]
    img[h_splitb2:h_splitb3, 0:w_split] = [hue2, saturation2, 255]
    img[h_splitb3:h_splitb4, 0:w_split] = [0, 0, value2]

    img = cv2.cvtColor(img, cv2.COLOR_HSV2BGR) # convert HSV value to BGR

cap.release()
cv2.destroyAllWindows()

print(f'[np.array([ {hue1}, {saturation1}, {value1}]), np.array([ {hue2}, {saturation2}, {value2}])]')