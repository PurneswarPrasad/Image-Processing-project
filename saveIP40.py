#Image restoration by Inpainting
#Doubt :- How to create a mask

import cv2
import matplotlib.pyplot as plt

def main():
    
    imgpath1 = "C:\\Users\\Purneswar Prasad\\Documents\\misc\\OpenCV_Logo_B.png"
    img1 = cv2.imread(imgpath1, 1)
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)

    maskpath = "C:\\Users\\Purneswar Prasad\\Documents\\misc\\OpenCV_Logo_C.png"
    mask = cv2.imread(maskpath, 0)
#    img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
    
    output1 = cv2.inpaint(img1, mask, 5, cv2.INPAINT_TELEA)
    output2 = cv2.inpaint(img1, mask, 5, cv2.INPAINT_NS)
    
    output = [img1, mask, output1, output2]
    titles = ["Damaged Image", "Mask", "TELEA", "NS"]
    
    for i in range(4):
        plt.subplot(2, 2, i+1)
        if i==1:
            plt.imshow(output[i], cmap = "gray")
        else:
            plt.imshow(output[i])
        plt.title(titles[i])
        plt.xticks([])
        plt.yticks([])
        
    plt.show()
    
if __name__ == "__main__":
    main()