# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 03:58:23 2020

@author: Purneswar Prasad
"""


import cv2

def main():
    imgpath = "C:\\Users\\Purneswar Prasad\\Documents\\misc\\4.2.06.tiff"
    img1 = cv2.imread(imgpath,0) # 0 for gray and 1 for colored
    
    print(img1) #object of type numpy.ndarray _ ndaray stands for n dimensional array 
    print(type(img1))
    print(img1.dtype)  # uint8
    print(img1.shape)  # (512, 512)
    print(img1.ndim)   # 2
    print(img1.size)   # 262144 = 512*512
    
#    print(img1.dtype) # uint8
#    print(img1.shape) # (512, 512, 3)
#    print(img1.ndim)  # 3
#    print(img1.size)  # 786432 = 512*512*3
    
    cv2.imshow(('River'), img1)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
if __name__ == "__main__":
    main()