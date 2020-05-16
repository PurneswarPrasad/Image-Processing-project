#Adaptive thresholding

import cv2
import matplotlib.pyplot as plt

def main():
    
    imgpath1 = "C:\\Users\\Purneswar Prasad\\Documents\\misc\\5.1.12.tiff"
    
    img1 = cv2.imread(imgpath1, 0)
    
    block_size = 73 #This can only contain odd values
    constant = 2
    th1 = cv2.adaptiveThreshold(img1, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, block_size, constant)
    th2 = cv2.adaptiveThreshold(img1, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, block_size, constant)
    
    output = [img1, th1, th2]
    
    titles = ["Original Image", "Mean Adaptive", "Gaussian Adaptive"]
    
    for i in range(3):
        plt.subplot(1, 3, i+1)
        plt.imshow(output[i], cmap = "gray")
        plt.title(titles[i])
    
    plt.show()
    
if __name__ == "__main__":
    main()