import cv2 
import numpy as np
from color_recognition import color_detect

#####################################################################
img = cv2.VideoCapture(1)

dist = np.array([[-5.17994872e-02, 1.33860825e+00, -2.93913838e-03, -3.28111848e-03, -5.27297925e+00]])

cameraMatrix = np.array([[816.53414246, 0., 284.80505879],
                         [0., 809.129015, 246.80347752],
                         [0., 0., 1.]])

######################################################################

while True:
    check, frame = img.read()
    # แก้ Distorsion
    newCameraMatrix, roi = cv2.getOptimalNewCameraMatrix(cameraMatrix, dist, (640,480), 1, (640,480))
    dst_frame = cv2.undistort(frame, cameraMatrix, dist, None, newCameraMatrix) 

    hsv = cv2.cvtColor(dst_frame, cv2.COLOR_BGR2HSV)
    lower_green = np.array([40, 120, 80])       # HSV color - circle : ใน OpenCV ต้องหาร 2 ก่อนนำค่ามาใส่
    upper_green = np.array([85, 255, 255])
    mask_green = cv2.inRange(hsv, lower_green, upper_green)

    # ปรับภาพโดยใช้การ Dilation
    kernel = np.ones((5, 5), np.uint8) 
    #cv2.imshow("MG", mask_green)
    dilated = cv2.dilate(mask_green, kernel, iterations=3)      # ขยายโซนสีขาวปรับ iteration ได้
    #cv2.imshow("dilated", dilated) 
    contours_green, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    cx = 0
    cy  = 0
    for cnt in contours_green:
        contour_area = cv2.contourArea(cnt)
        if contour_area > 50:
            x, y, w, h = cv2.boundingRect(cnt)
            # Centroid
            cx = x+w*0.5
            cy = y+h*0.5
            cv2.rectangle(dst_frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
               
    mm_per_px = 0.6363      # เทียบระยะจริงกับระยะกล้อง mm/px

    mm_cx_offset = cx * mm_per_px   #mm
    mm_cy_offset = cy * mm_per_px   #mm

    x_robot2cam = 335
    x_real = mm_cy_offset + x_robot2cam

    # find y robot to cam
    y_robot2cam = 219.45
    y_2 = (640-cx)*mm_per_px
    y_real = y_robot2cam - y_2

    coordinate_word = "(" + str(round(x_real,2)) + "," + str(round(y_real,2)) + ")" 
    cv2.putText(dst_frame,coordinate_word, (int(cx), int(cy)-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
    
    # print("CY is: ", cx)
    cv2.imshow("Undistorsion VDO", dst_frame)

    
    if cv2.waitKey(1) &0xFF == ord("e"):
        break
img.release()
cv2.destroyAllWindows()