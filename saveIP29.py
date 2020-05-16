#Thresholding and basic segmentation

import cv2
import matplotlib.pyplot as plt

def main():
    
    imgpath1 = "C:\\Users\\Purneswar Prasad\\Documents\\misc\\4.1.04.tiff"
    img1 = cv2.imread(imgpath1, 0)
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
    
    th = 127
    max_val = 255
    
    ret, o1 = cv2.threshold(img1, th, max_val, cv2.THRESH_BINARY)   #If the value of pixel is greater than threshold, then it's assigned the max value, else the min value
    ret, o2 = cv2.threshold(img1, th, max_val, cv2.THRESH_BINARY_INV)  #Opposit of previous
    ret, o3 = cv2.threshold(img1, th, max_val, cv2.THRESH_TOZERO)   #If the value of the pixel is less than threshold, it is set to zero and above threshold remains the same
    ret, o4 = cv2.threshold(img1, th, max_val, cv2.THRESH_TOZERO_INV)  #Opposite to previous
    ret, o5 = cv2.threshold(img1, th, max_val, cv2.THRESH_TRUNC)    #If the value of the pixel is greater than threshold, then it remains the same
    
    output = [img1, o1, o2, o3, o4, o5]
    
    titles = ["Orig Image", "Binary", "Binary Inv", "Zero", "Zero Inv", "Trunc"]
    
    for i in range(6):
        plt.subplot(2, 3, i+1)
        plt.imshow(output[i])
        plt.title(titles[i])
        
    plt.show()
    
if __name__ == "__main__":
    main()