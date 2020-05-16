#playback of a video file
import cv2

def main():
    windowname = "OpenCV Video Player"
    cv2.namedWindow(windowname)
    
    filename = "C:\\Users\\Purneswar Prasad\\Documents\\OPpath\\video1.avi"
    cap = cv2.VideoCapture(filename)
    
    while (cap.isOpened()):
        
        ret, frame = cap.read()
        
        print(ret)
        
        if ret:
            cv2.imshow(windowname, frame)
            if cv2.waitKey(1)==27:  #here the argument of waitKey can be changed to change the speed of video playback. Here it's 1000/30
                break
        else:
            break
        
    cv2.destroyAllWindows()
    cap.release()
    
if __name__ == "__main__":
    main()
        
        