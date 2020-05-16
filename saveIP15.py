#displaying multiple images with matplotlib
import cv2
import matplotlib.pyplot as plt

def main():
    
    path = "C:\\Users\\Purneswar Prasad\\Documents\\misc\\"
    
    imgpath1 = path + "4.1.05.tiff"
    imgpath2 = path + "4.1.06.tiff"
    
    img1 = cv2.imread(imgpath1, 1)
    img2 = cv2.imread(imgpath2, 1)
    
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
    img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
    
    titles = ["Home", "Bonsai"]
    images = [img1, img2]
    
    for i in range(2):  #this loop helps in doing the iteration for displaying side by side images
        
        plt.subplot(1, 2, i+1)
        plt.imshow(images[i])
        plt.title(titles[i])
        plt.xticks([])
        plt.yticks([])
    
if __name__ == "__main__":
    main()    