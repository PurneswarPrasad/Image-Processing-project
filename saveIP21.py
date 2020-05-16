#Creating the negative of an image

import cv2
import matplotlib.pyplot as plt

def main():
    imgpath1 = "C:\\Users\\Purneswar Prasad\\Documents\\misc\\4.2.06.tiff"
    
    img = cv2.imread(imgpath1, 1)
    
    img1 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img2 = cv2.cv2.imread(imgpath1, 0)
    
    img3 = abs(255 - img1)
    img4 = abs(1 - img2)
    
    titles = ["Color Image", "Gray scale image", "Color-negative", "Gray scale-negative"]
    images = [img1, img2, img3, img4]
        
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