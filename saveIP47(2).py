#Morphological Operations in colored images

import cv2
import matplotlib.pyplot as plt
import numpy as np

def main():
    
    location = "C:\\Users\\Purneswar Prasad\\Documents\\standard_test_images\\"
    imgpath = location + "lena_color_512.tif"
    img = cv2.imread(imgpath, 1)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        
    k = np.ones((5, 5), np.uint8)
#    k = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))
#    k = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5))
#    k = cv2.getStructuringElement(cv2.MORPH_CROSS, (5,5))
    
    print(k)
    
    erosion = cv2.erode(img, k, iterations = 3) #Erosion means the white surfaces are slowly covered by black grounds
    dilation = cv2.dilate(img, k, iterations = 3) #Dilation means the black surfaces are slowly covered by white grounds
    gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, k) #Difference between the eroded and dilated images 
    
    output = [img, erosion, dilation, gradient]
    titles = ["Original Image", "Eroded Image", "Dilated Image", "Gradient"]
    
    for i in range(4):
        plt.subplot(2, 2, i+1)
        plt.imshow(output[i])
        plt.title(titles[i])
        plt.xticks([])
        plt.yticks([])
        
    plt.show()
    
if __name__ == "__main__":
    main()
        