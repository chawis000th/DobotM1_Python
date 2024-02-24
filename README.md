#### Changelog
>- 20240218-1424: <br>
>   - merged to main, split calculate function x,y <br>
>- 20240220-1029: <br>
>   - fix '_hsv' in 'def Mask_n_Draw' <br>
>   - add 'contourArea' variable 'def Mask_n_Draw' <br>
>- 20240220-1500: <br>
>   - loop dobot <br>
>- 20240221-1954: <br>
>   - remove cv2 normal box function (unused) <br>
>   - rearrange function order <br>
>   - trim unuse variable <br>
>   - rearrange object merge list <br>
>- 20240222-0234: <br>
>   - rearrange text <br>
>- 20240224-1458: <br>
>   - trim unuse library
>- 20240224-1543: <br>
>   - fix last_clean (really duplicate from frame)
>   - fix double contour
>   - move convert frame_hsv to inside mask_n_draw function

>TO DO : <br>
>   - add webcam manual focus
***

# DobotSDK_Python
越疆机械臂的Python版本SDK，比官方API更强大，修复若干bug，支持多机协作