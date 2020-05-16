#Create a Max RGB filter

import cv2
import numpy as np

def main():
    
    w = 640
    h = 480
    
    cap = cv2.VideoCapture(0)
    
    cap.set(3, w)
    cap.set(4, h)
    
    print(cap.get(3))
    print(cap.get(4))
    
    if cap.isOpened():
        ret, frame = cap.read()
    else:
        ret = False
        
    while ret:
        
        ret, frame = cap.read()
        
        R, G, B = cv2.split(frame)
        
        M = np.maximum(np.maximum(R, G), B)
        
        R[M > R] = 0
        G[M > G] = 0
        B[M > B] = 0
        
        frame1 = cv2.merge((R, G, B), None)
        
        cv2.imshow("Original Image", frame)
        cv2.imshow("Final Image", frame1)
        
        if cv2.waitKey(1)==27:
            break
        
    cv2.destroyAllWindows()
    cap.release()
    
if __name__ == "__main__":
    main()