#Kernel and Convolution
#Differnt matrices can be found on wikipedia.
#Use different values in the matrices to get more effects 

import cv2
import matplotlib.pyplot as plt
import numpy as np

def main():
    
    imgpath1 = "C:\\Users\\Purneswar Prasad\\Documents\\misc\\4.1.08.tiff"
    img1 = cv2.imread(imgpath1, 1)
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
    
    k = np.array(np.ones((3,3), np.float32))/9
    
    print(k)
    
    output = cv2.filter2D(img1, -1, k)  #This is used for convloution. -1 gives output the same depth as the input image.
    
    plt.imshow(output)
    plt.title("Identity operation")
    plt.show()
    
if __name__ == "__main__":
    main()