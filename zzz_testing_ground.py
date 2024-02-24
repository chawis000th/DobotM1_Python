import cv2
import numpy as np
import matplotlib.pyplot as plt
import time

cap = cv2.VideoCapture(0)

# .get image properties https://docs.opencv.org/3.4/d4/d15/group__videoio__flags__base.html#gaeb8dd9c89c10a5c63c139bf7c4f5704d
vid_w = int(cap.get(3)) 
vid_h = int(cap.get(4))
vid_fps = int(cap.get(cv2.CAP_PROP_FPS)) # or use int(cap.get(5))
vid_scale = 1 # image scale; 1=100% 0.5=50%
print(f'video size = {vid_w} x {vid_h}\nframerate = {vid_fps}')

cap.set(cv2.CAP_PROP_AUTO_EXPOSURE,0)
cap.set(cv2.CAP_PROP_AUTOFOCUS,0)
cap.set(cv2.CAP_PROP_AUTO_WB,0)




while (cap.isOpened()):
    # read and check for image availability before continue
    check, frame = cap.read()
    if check != True:
        print('>> video ended or not available')
        break
    
    cap.set(cv2.CAP_PROP_EXPOSURE,-100.0)
    cap.set(cv2.CAP_PROP_FOCUS,5)
    cap.set(cv2.CAP_PROP_BRIGHTNESS,255)
    cap.set(cv2.CAP_PROP_CONTRAST,255)
    cap.set(cv2.CAP_PROP_SATURATION,255)


    # show window
    cv2.imshow('RGB', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('e'):
        print('>> Keyboard Exit')
        break
cap.release()
cv2.destroyAllWindows()

print('>> Exit Phase 1')