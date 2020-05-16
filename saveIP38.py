#Canny Edge Detection algorithm using Trackbar

import cv2
#import matplotlib.pyplot as plt

def emptyFunc():
    pass

def main():
    
    windowName = "Canny Edge"
    cv2.namedWindow(windowName)
    
    imgpath1 = "C:\\Users\\Purneswar Prasad\\Documents\\misc\\5.1.11.tiff"
    img1 = cv2.imread(imgpath1, 1)
#    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
    
    cv2.createTrackbar("L1adj", windowName, 0, 150, emptyFunc)
    cv2.createTrackbar("L2adj", windowName, 151, 500, emptyFunc)
    cv2.createTrackbar("BoolAdj", windowName, 0, 1, emptyFunc)
    
    while(True):
        
        l1 = cv2.getTrackbarPos("L1adj", windowName)
        l2 = cv2.getTrackbarPos("L2adj", windowName)
        l3 = cv2.getTrackbarPos("BoolAdj", windowName)
        
        if l3 == 0:
            L1 = cv2.Canny(img1, l1, l2, L2gradient = False)
            L2 = cv2.Canny(img1, l1, l2, L2gradient = True)
        else:
            L2 = cv2.Canny(img1, l1, l2, L2gradient = True)
            L1 = cv2.Canny(img1, l1, l2, L2gradient = False)
        
        
        cv2.imshow("L1", L1)
        cv2.imshow("L2", L2)
        
        if cv2.waitKey(1)==27:
            break
    
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
    