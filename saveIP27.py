#Affine Transformations

import cv2
#import matplotlib.pyplot as plt
import numpy as np

def main():
    
    windowName = "Live Video Feed"
    cv2.namedWindow(windowName)
    cap = cv2.VideoCapture(0)
    
    if cap.isOpened():
        ret, frame = cap.read()
    else:
        ret = False
        
#    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
#    imgpath1 = "C:\\Users\\Purneswar Prasad\\Documents\\misc\\4.2.01.tiff"
#    img1 = cv2.imread(imgpath1, 1)
#    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
    
    rows, columns, channels = frame.shape
    
    while True:
        
        ret, frame = cap.read()
        
        point1 = np.float32([[100, 100], [300, 100], [100, 300]])
        point2 = np.float32([[200, 150], [400, 150], [400, 300]])
    
        A = cv2.getAffineTransform(point1, point2)
    
        print(A)
    
        output = cv2.warpAffine(frame, A, (rows, columns))
        
        cv2.imshow(windowName, output)
        
        if cv2.waitKey(1) == 27:
            break
        
    cv2.destroyAllWindows()
    cap.release()
#        plt.imshow(output)
#        plt.title("Affine Transform")
#        plt.show()
if __name__ == "__main__":
    main()
        
    
