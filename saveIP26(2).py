#Roatating and scaling live video feed

import cv2
import time

def main():
    
    windowName = "Live Video Feed"
    cv2.namedWindow(windowName)
    cap = cv2.VideoCapture(0)
    
    if cap.isOpened():
        ret, frame = cap.read()
    else:
        ret = False
        
    angle = 0
    scale = 0.01
    
    rows, columns, channels = frame.shape
    
    while (True):
        
        ret, frame = cap.read()
        
        R = cv2.getRotationMatrix2D((rows/1.5, columns/1.5), angle, scale)
        
        if (angle == 360):
            angle = 0
            
        output = cv2.warpAffine(frame, R, (rows, columns))
        
        angle = angle + 10
         
        if (scale <= 1):
             scale = scale + 0.1
        else:
             scale = 0.01
        
        cv2.imshow(windowName, output)
        time.sleep(0.01)
        
        if (cv2.waitKey(1) == 27):
            break
        
    cv2.destroyAllWindows()
    cap.release()
        
if __name__ == "__main__":
    main()