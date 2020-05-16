import cv2
import matplotlib.pyplot as plt

def main():
    
    imgpath = "C:\\Users\\Purneswar Prasad\\Documents\\misc\\4.2.03.tiff"
    img = cv2.imread(imgpath,1)
    
    img1 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    plt.imshow(img)
    plt.title('monkey BGR')
    plt.xticks([])
    plt.yticks([])
    plt.show()
    
    plt.imshow(img1)
    plt.title('monkey RGB')
    plt.xticks([])
    plt.yticks([])
    plt.show()
    
#    cv2.imshow("Monkey", img)
#    cv2.waitKey(0)
#    cv2.destroyAllWindows()
    
if __name__ == "__main__":
    main()