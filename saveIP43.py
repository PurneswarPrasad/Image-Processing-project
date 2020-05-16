#Matlpotlib histograms

import cv2
import matplotlib.pyplot as plt

def main():
    
    path = "C:\\Users\\Purneswar Prasad\\Documents\\misc\\"
    imgpath = path + "4.2.07.tiff"
    img = cv2.imread(imgpath, 1) #0 reads in grayscale mode and 1 in color mode
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    R, G, B = cv2.split(img)
    
    plt.subplot(2, 2, 1)
    plt.imshow(img)
    plt.title("Beads")
    plt.xticks([])
    plt.yticks([])
    
    plt.subplot(2, 2, 2)
    plt.hist(R.ravel(), 256, [0, 255]) #ravel() flattens the image, 256 is the no. of bins
    plt.title("Red Channel Histogram")
    plt.xlim(xmin = 0, xmax = 256)
    
    plt.subplot(2, 2, 3)
    plt.hist(G.ravel(), 256, [0, 255]) #ravel() flattens the image, 256 is the no. of bins
    plt.title("Green Channel Histogram")
    plt.xlim(xmin = 0, xmax = 256)
    
    plt.subplot(2, 2, 4)
    plt.hist(B.ravel(), 256, [0, 255]) #ravel() flattens the image, 256 is the no. of bins
    plt.title("Blue Channel Histogram")
    plt.xlim(xmin = 0, xmax = 256)
    
    plt.show()
    
if __name__ == "__main__":
    main()