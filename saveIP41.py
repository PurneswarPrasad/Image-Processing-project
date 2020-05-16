#Image quantization with K Means

import cv2
import numpy as np
import matplotlib.pyplot as plt

def main():
    
    location = "C:\\Users\\Purneswar Prasad\\Documents\\misc\\"
    imgpath1 = location + "4.2.03.tiff"
    img1 = cv2.imread(imgpath1, 1)
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
    
    z = img1.reshape(-1, 3)
    z = np.float32(z)
    
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    
    k = 2
    ret, label1, center1 = cv2.kmeans(z, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
    
    center1 = np.uint8(center1)
    res1 = center1[label1.flatten()]
    output1 = res1.reshape((img1.shape))
    
    k = 4
    ret, label1, center1 = cv2.kmeans(z, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
    
    center1 = np.uint8(center1)
    res1 = center1[label1.flatten()]
    output2 = res1.reshape((img1.shape))
    
    
    k = 6
    ret, label1, center1 = cv2.kmeans(z, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
    
    center1 = np.uint8(center1)
    res1 = center1[label1.flatten()]
    output3 = res1.reshape((img1.shape))
    
    output = [img1, output1, output2, output3]
    titles = ["Original Image", "K=2","Trial 1", "Trial 2"]
    
    for i in range(4):
        plt.subplot(2, 2, i+1)
        plt.imshow(output[i])
        plt.title(titles[i])
        plt.xticks([])
        plt.yticks([])
        
    plt.show()
    
if __name__ == "__main__":
    main()