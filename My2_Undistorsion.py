import cv2 
import numpy as np
from color_recognition import color_detect


img = cv2.VideoCapture(1)

dist = np.array([[-5.17994872e-02, 1.33860825e+00, -2.93913838e-03, -3.28111848e-03, -5.27297925e+00]])

cameraMatrix = np.array([[816.53414246, 0., 284.80505879],
                         [0., 809.129015, 246.80347752],
                         [0., 0., 1.]])

while True:
    check, frame = img.read()
    # แก้ Distorsion
    newCameraMatrix, roi = cv2.getOptimalNewCameraMatrix(cameraMatrix, dist, (640,480), 1, (640,480))
    dst_frame = cv2.undistort(frame, cameraMatrix, dist, None, newCameraMatrix) 
    cv2.imshow("Undistorsion VDO", dst_frame)
    if cv2.waitKey(1) &0xFF == ord("e"):
        break
img.release()
cv2.destroyAllWindows()

