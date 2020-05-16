#Blending and transitioning images(1)

import cv2
import matplotlib.pyplot as plt

def main():
    
    location = "C:\\Users\\Purneswar Prasad\\Documents\\misc\\"
    
    imgpath1 = location + "4.1.03.tiff"
    imgpath2 = location + "4.1.04.tiff"
    
    img1 = cv2.imread(imgpath1, 1)
    img2 = cv2.imread(imgpath2, 1)
    
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
    img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
    
    alpha = 0.5
    beta = 0.5
    gamma = 0
    
    output = cv2.addWeighted(img1, alpha, img2, beta, gamma)
    
    titles = ["Green Girl", "Pink Girl", "Blended Image"]
    images = [img1, img2, output]
    
    for i in range(3):
        
        plt.subplot(1, 3, i+1)
        plt.imshow(images[i])
        plt.title(titles[i])
        plt.xticks([])
        plt.yticks([])
        
    plt.show()
    
if __name__ == "__main__":
    main()