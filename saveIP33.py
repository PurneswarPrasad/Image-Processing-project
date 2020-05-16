#Introducing salt and pepper noise in he image

import cv2
import matplotlib.pyplot as plt
import numpy as np
import random

def main():
    
    imgpath1 = "C:\\Users\\Purneswar Prasad\\Documents\\misc\\4.1.04.tiff"
    img1 = cv2.imread(imgpath1, 1)
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
    
    rows, columns, channels = img1.shape
    
    output = np.zeros(img1.shape, np.uint8) #Creates a placeholder for output image
    p = 0.5
    
#    while(True):
    for i in range(rows):
            for j in range(columns):
                r = random.random()
                if r <= p/2:
                    #Pepper sprinkled
                    output[i][j] = [0, 0, 0]
                elif r > p/2 and r <= p:
                    #Salt sprinkled
                    output[i][j] = [255, 255, 255]
                else:
                    output[i][j] = img1[i][j]
                
    plt.imshow(output)
    plt.title("Salt and Pepper Image")
    plt.show()
        
#        if cv2.waitKey(1)==27:
#            break
    
if __name__ == "__main__":
    main()

    