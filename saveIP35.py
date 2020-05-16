#Low pass filters
#Using built-in kernels to do convolution

import cv2
import matplotlib.pyplot as plt

def main():
    
    imgpath1 = "C:\\Users\\Purneswar Prasad\\Documents\\misc\\4.2.07.tiff"
    img1 = cv2.imread(imgpath1, 1)
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
    
    box = cv2.boxFilter(img1, -1, (53, 53))
    
    blurimg = cv2.blur(img1, (13, 13))
    
    gaussian = cv2.GaussianBlur(img1, (17, 17), 0)   #Gaussian Blur is used to remove any Gaussian Noise present iin the image
    
    output = [img1, box, blurimg, gaussian]
    titles = ["Original", "Box blur", "Blur", "Gaussian blur"]
    
    for i in range(4):
        plt.subplot(2, 2, i+1)
        plt.imshow(output[i])
        plt.title(titles[i])
        
    plt.show()
    
if __name__ == "__main__":
    main()