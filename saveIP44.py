#Numpy Histograms

import cv2
import numpy as np
import matplotlib.pyplot as plt

def main():
    
    location = "C:\\Users\\Purneswar Prasad\\Documents\\misc\\"
    imgpath = location + "4.1.08.tiff"
    img = cv2.imread(imgpath, 1)
    
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    R, G, B = cv2.split(img)
    
    plt.subplot(2, 2, 1)
    plt.imshow(img)
    plt.title("Beads")
    plt.xticks([])
    plt.yticks([])
    
    plt.subplot(2, 2, 2)
    hist, bins = np.histogram(R.ravel(), 256, [0, 255])
    plt.xlim([0, 255])
    plt.ylim([0, 3000])
    plt.plot(hist, color = "r")
    plt.title("Histogram")
    
    
    plt.subplot(2, 2, 3)
    hist, bins = np.histogram(G.ravel(), 256, [0, 255])
    plt.xlim([0, 255])
    plt.ylim([0, 3000])
    plt.plot(hist, color = "g")
    plt.title("Histogram")
    
    plt.subplot(2, 2, 4)
    hist, bins = np.histogram(B.ravel(), 256, [0, 255])
    plt.xlim([0, 255])
    plt.ylim([0, 3000])
    plt.plot(hist, color = "b")
    plt.title("Histogram")
    
    plt.show()
    
if __name__ == "__main__":
    main()
    