#Perspective Transformation

import cv2
import matplotlib.pyplot as plt
import numpy as np

def main():
    
    imgpath1 = "C:\\Users\\Purneswar Prasad\\Documents\\misc\\4.2.01.tiff"
    img1 = cv2.imread(imgpath1, 1)
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
    
    rows, columns, channels = img1.shape
    
    
    point1 = np.float32([[0, 0], [0, 400], [400, 0], [400, 400]])
    point2 = np.float32([[0, 0], [0, 300], [300, 0], [300, 300]])
    
    A = cv2.getPerspectiveTransform(point1, point2)
    
    print(A)
    
    output = cv2.warpPerspective(img1, A, (500, 500)) #Here the last set of point can be changed to zoomm in and out 

    plt.imshow(output)
    plt.title("Affine Transform")
    plt.show()
if __name__ == "__main__":
    main()
                
    