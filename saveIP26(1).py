#Rotating and scaling images dynamically

import cv2
import time

def main():
    
    imgpath = "C:\\Users\\Purneswar Prasad\\Documents\\misc\\4.2.01.tiff"
    img1 = cv2.imread(imgpath, 1)
        
    rows, columns, channels = img1.shape
    
    angle = 0
    
    scale = 0.01
    
    while(True):
        
        if angle == 360:
            angle = 0
            
        R = cv2.getRotationMatrix2D((rows/2, columns/2), angle, scale)
        
        print(R)
        
        output = cv2.warpAffine(img1, R, (rows, columns))
        
        if (scale <= 1):
            scale = scale + 0.1
        else:
            scale = 0.01
        
        cv2.imshow("Rotated image", output)
        angle = angle + 1
        time.sleep(0.1)
        
        if cv2.waitKey(1) == 27:
            break
        
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()