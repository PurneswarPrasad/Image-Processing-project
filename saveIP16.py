#Arithmetic operations on images
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
    
    #We can also add constants and other matrices to the image 
    #add = img1 + img2  #it is commutative 
    #sub = img1 - img2  #it is not commutative
    
    #We can also multiply
    mul = img1 * img2  #it is commutative
    div = img1 / img2  #it is not commutative
    
    titles = ["Green Girl", "Pink Girl", "Combination", "Degradation"]
    images = [img1, img2, mul, div]
    
    for i in range(4):
        
        plt.subplot(1, 4, i+1)
        plt.imshow(images[i])
        plt.title(titles[i])
        plt.xticks([])
        plt.yticks([])
        
    plt.show()
    
if __name__ == "__main__":
    main()
    