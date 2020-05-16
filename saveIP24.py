#Translation and shifting in images

import cv2
import matplotlib.pyplot as plt
import numpy as np

def main():
    
    imgpath = "C:\\Users\\Purneswar Prasad\\Documents\\misc\\4.2.01.tiff"
    img1 = cv2.imread(imgpath, 1)
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
    
    rows, columns, channels = img1.shape
    
    T = np.float32([[1, 0, 50], [0, 1, 50]])
    
    print(T)
    
    output = cv2.warpAffine(img1, T, (columns, rows))
    #output = img1
    
    plt.imshow(output)
    plt.title("Shifted Image")
    plt.show()
    
if __name__ == "__main__":
    main()