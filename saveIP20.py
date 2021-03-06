#Splitting and merging color channels

import cv2
import matplotlib.pyplot as plt

def main():
    
    imgpath1 = "C:\\Users\\Purneswar Prasad\\Documents\\misc\\4.2.01.tiff"
    
    img1 = cv2.imread(imgpath1, 1)
    
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
    
    r, g, b = cv2.split(img1)
    
    titles = ["Original Image", "R", "G", "B"]
    images = [cv2.merge((r,g,b)), r, g, b]
        
       
    plt.subplot(2, 2, 1)
    plt.imshow(images[0])
    plt.title(titles[0])
    plt.xticks([])
    plt.yticks([])
    
    plt.subplot(2, 2, 2)
    plt.imshow(images[1])
    plt.title(titles[1])
    plt.xticks([])
    plt.yticks([])
    
    plt.subplot(2, 2, 3)
    plt.imshow(images[2])
    plt.title(titles[2])
    plt.xticks([])
    plt.yticks([])
    
    plt.subplot(2, 2, 4)
    plt.imshow(images[3])
    plt.title(titles[3])
    plt.xticks([])
    plt.yticks([])
    
    plt.show()
    
if __name__ == "__main__":
    main()