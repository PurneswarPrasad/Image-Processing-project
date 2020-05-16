#High pass filter
#Laplacian, Sobel and Scharr operators

import cv2
import matplotlib.pyplot as plt

def main():
    
    imgpath1 = "C:\\Users\\Purneswar Prasad\\Documents\\misc\\testcow.jpg"
    img1 = cv2.imread(imgpath1, 1)
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
    
    #Laplacian Method
    edges = cv2.Laplacian(img1, -1, ksize = 9, scale = 1, delta = 0, borderType = cv2.BORDER_DEFAULT)
    #ksize is the kernel size
    
    output = [img1, edges]
    titles = ["Original Image", "Edges"]
    
    for i in range(2):
        plt.subplot(1, 2, i+1)
        plt.imshow(output[i])
        plt.title(titles[i])
        plt.xticks([])
        plt.yticks([])
        
    plt.show()
    
if __name__ == "__main__":
    main()