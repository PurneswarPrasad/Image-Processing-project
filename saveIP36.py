#Applying median blur filter
#This filter is used to remove salt and pepper noise

import cv2
import matplotlib.pyplot as plt
import random
import numpy as np

def main():
    
    imgpath1 = "C:\\Users\\Purneswar Prasad\\Documents\\misc\\4.2.07.tiff"
    img1 = cv2.imread(imgpath1, 1)
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
    
    rows, columns, channels = img1.shape
    
    output = np.zeros(img1.shape, np.uint8)
    p = 0.95
    
    for i in range(rows):
        for j in range(columns):
            r = random.random()
            if r < p/2:
                #Pepper sprinkled
                output[i][j] = [0, 0, 0]
            elif r > p/2 and r <= p:
                #Salt sprinkled
                output[i][j] = [255, 255, 255]
            else:
                output[i][j] = img1[i][j]
                
    denoised = cv2.medianBlur(output, 95)
    
    images = [img1, output, denoised]
    titles = ["Original Image", "Salt and Pepper Image", "Denoised Image"]
    
    for i in range(3):
        plt.subplot(1, 3, i+1)
        plt.imshow(images[i])
        plt.title(titles[i])
        plt.xticks([])
        plt.yticks([])
        
    plt.show()
    
if __name__ == "__main__":
    main()