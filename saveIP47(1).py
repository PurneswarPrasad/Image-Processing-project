#Morphological Operations oin gray scale images

import cv2
import matplotlib.pyplot as plt
import numpy as np

def main():
    
    location = "C:\\Users\\Purneswar Prasad\\Documents\\standard_test_images\\"
    imgpath = location + "cameraman.tif"
    img = cv2.imread(imgpath, 0)
    
    th = 0
    max_val = 255
    
    ret, binary_inv = cv2.threshold(img, th, max_val, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    
    k = np.ones((5, 5), np.uint8)
#    k = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))
#    k = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5))
#    k = cv2.getStructuringElement(cv2.MORPH_CROSS, (5,5))
    
    print(k)
    
    erosion = cv2.erode(binary_inv, k, iterations = 3) #Erosion means the white surfaces are slowly covered by black grounds
    dilation = cv2.dilate(binary_inv, k, iterations = 3) #Dilation means the black surfaces are slowly covered by white grounds
    gradient = cv2.morphologyEx(binary_inv, cv2.MORPH_GRADIENT, k) #Difference between the eroded and dilated images 
    
    output = [img, binary_inv, erosion, dilation, gradient]
    titles = ["Original Image", "Binary Inverted Image", "Eroded Image", "Dilated Image", "Gradient"]
    
    for i in range(5):
        plt.subplot(3, 2, i+1)
        plt.imshow(output[i], cmap = "gray")
        plt.title(titles[i])
        plt.xticks([])
        plt.yticks([])
        
    plt.show()
    
if __name__ == "__main__":
    main()
        