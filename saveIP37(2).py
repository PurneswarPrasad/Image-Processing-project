#High pass filter
#Laplacian, Sobel and Scharr operators

import cv2
import matplotlib.pyplot as plt

def main():
    
    imgpath1 = "C:\\Users\\Purneswar Prasad\\Documents\\misc\\5.1.11.tiff"
    img1 = cv2.imread(imgpath1, 1)
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
    
    #Sobel Operator
    edgesx = cv2.Sobel(img1, -1, dx = 1, dy = 0, ksize = 7, scale = 1, delta = 0, borderType = cv2.BORDER_DEFAULT)
    #giving dy = 0 helps to find vertical edges
    edgesy = cv2.Sobel(img1, -1, dx = 0, dy = 1, ksize = 7, scale = 1, delta = 0, borderType = cv2.BORDER_DEFAULT)
    #giving dx = 0 helps to find horizontal edges
    
    edges = edgesx + edgesy
    
    output = [img1, edgesx, edgesy, edges]
    titles = ["Original Image", "Edges Vertical", "Edges Horizontal", "All Edges"]
    
    for i in range(4):
        plt.subplot(2, 2, i+1)
        plt.imshow(output[i])
        plt.title(titles[i])
        plt.xticks([])
        plt.yticks([])
        
    plt.show()
    
if __name__ == "__main__":
    main()