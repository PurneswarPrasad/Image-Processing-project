#Blending and transitioning images(2)

import cv2
import numpy as np
import time

def main():
    
    location = "C:\\Users\\Purneswar Prasad\\Documents\\misc\\"
    
    imgpath1 = location + "4.1.03.tiff"
    imgpath2 = location + "4.1.04.tiff"
    
    img1 = cv2.imread(imgpath1, 1)
    img2 = cv2.imread(imgpath2, 1)
    
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
    img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
    
    for  i  in np.linspace(0, 1 ,10):
        alpha = i
        beta = 1 - alpha
        gamma = 0
        output = cv2.addWeighted(img1, alpha, img2, beta, gamma)
        cv2.imshow("Transition", output)
        time.sleep(0.25)
        if cv2.waitKey(1)==27:
            break
    
    cv2.destroyAllWindows()
    
if __name__ == "__main__":
    main()