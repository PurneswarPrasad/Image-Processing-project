# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 03:31:21 2020

@author: Purneswar Prasad
"""

import cv2

def main():
    imgpath = "C:\\Users\\Purneswar Prasad\\Documents\\misc\\4.2.07.tiff"
    img = cv2.imread(imgpath,0)
    
    outpath = "C:\\Users\\Purneswar Prasad\\Documents\\OPpath\\4.2.07.jpg"
    cv2.imshow("Veggies", img)
    cv2.imwrite(outpath,img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
if __name__ == "__main__":
    main()