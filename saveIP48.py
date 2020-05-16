#Finding an drawing contours

import cv2
import matplotlib.pyplot as plt

def main():
    
    location = "C:\\Users\\Purneswar Prasad\\Documents\\misc\\"
    imgpath = location + "4.2.07.tiff"
    img = cv2.imread(imgpath, 1)
    
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    grayscale_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    ret, thresh = cv2.threshold(grayscale_img, 127, 255, 0) #Change thresh value for different outputs
     
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    #In the video, it uses a img2 variable which is not required in higher versions of OpenCV
    
    cv2.drawContours(img, contours, -1, (0, 0, 255), 2)
    
    original = cv2.imread(imgpath, 1)
    
    original = cv2.cvtColor(original, cv2.COLOR_BGR2RGB)
    
    output = [original, img]
    titles = ["Original Image", "Contours"]
    
    for i in range(2):
        plt.subplot(1, 2, i+1)
        plt.imshow(output[i])
        plt.title(titles[i])
        plt.xticks([])
        plt.yticks([])
        
    plt.show()
    
if __name__ == "__main__":
    main()
    
    