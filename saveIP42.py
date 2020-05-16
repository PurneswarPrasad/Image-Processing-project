#Quantization of Live Video Feed

import cv2
import numpy as np

def main():
    
    w = 160
    h = 120
    
    cap = cv2.VideoCapture(0)
    
    cap.set(3, w)
    cap.set(4, h)
    
    print(cap.get(3), cap.get(4))
    
    if cap.isOpened():
        ret, frame = cap.read()
    else:
        ret = False
        
    while ret:
        
        ret, frame = cap.read()
        
        z = frame.reshape(-1, 3)
        z = np.float32(z)
        
        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
        
        k = 2
        ret, label1, center1 = cv2.kmeans(z, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
        
        center1 = np.uint8(center1)
        res1 = center1[label1.flatten()]
        output = res1.reshape((frame.shape))
        
        cv2.imshow("Original Image", frame)
        cv2.imshow("Quantized Image", output)
        
        if cv2.waitKey(1) == 27:
            break
        
    cv2.destroyAllWindows()
    cap.release()
    
if __name__ == "__main__":
    main()
        
        