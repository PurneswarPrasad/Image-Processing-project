#Rotation of an image

import cv2
import matplotlib.pyplot as plt

def main():
    
    imgpath = "C:\\Users\\Purneswar Prasad\\Documents\\misc\\4.2.01.tiff"
    img1 = cv2.imread(imgpath, 1)
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
    
    rows, columns, channels = img1.shape
    
    R = cv2.getRotationMatrix2D((rows/2, columns/2), 0, 0.5)
    
    print(R)
    
    output = cv2.warpAffine(img1, R, (rows, columns))
    
    plt.imshow(output)
    plt.title("Rotated Image")
    plt.show()
    
if __name__ == "__main__":
    main()