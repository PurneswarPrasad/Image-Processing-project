#create geometrical shapes and eneter text

import cv2
import numpy as np

def main():
    
    img1 = np.zeros((512,512,3), np.uint8)
    
    #cv2.line(img1, (0,99), (99,0), (255,0,0), 3)
    #cv2.rectangle(img1, (40,60), (100,150), (0,255,0), 3)
    #cv2.circle(img1, (60,60),15, (0,0,255), 3)
    #cv2.ellipse(img1, (200,200),(50,20),0,0,360, (127,127,127), -1)
 
    #points = np.array([[80,2],[125,5],[179,9],[230,5],[30,50]], np.int32)
    #points = points.reshape((-1,1,2))
    #cv2.polylines(img1, [points], True, (0,255,255))
    
    text1= "Test text"
    cv2.putText(img1, text1, (100,100), cv2.FONT_HERSHEY_SIMPLEX, 9, (127,0,127))

    cv2.imshow('River',img1)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()