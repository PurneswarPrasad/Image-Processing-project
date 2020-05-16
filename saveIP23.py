#Scaling operation on image

import cv2

def main():
     imgpath1 = "C:\\Users\\Purneswar Prasad\\Documents\\misc\\4.2.01.tiff"
     
     img1 = cv2.imread(imgpath1, 1)
     
     output = cv2.resize(img1, None, fx=0.5, fy=0.5, interpolation = cv2.INTER_AREA)
     
     cv2.imshow("Output", output)
     cv2.waitKey(0)
     cv2.destroyAllWindows()
     
if __name__ == "__main__":
     main()
     