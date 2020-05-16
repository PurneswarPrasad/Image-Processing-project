#webcam video recording to a file
import cv2

def main():
    
    windowname = "Live Webcm Video Record"
    cv2.namedWindow(windowname)
    
    cap = cv2.VideoCapture(0)
    
    filename = "C:\\Users\\Purneswar Prasad\\Documents\\OPpath\\video1.avi"
    codec = cv2.VideoWriter_fourcc('M', 'J', 'P', 'G')
    framerate = 30
    resolution = (640,480)
    
    VideoFileOutput = cv2.VideoWriter(filename, codec, framerate, resolution)
    
    if cap.isOpened():
        ret, frame = cap.read()
    else:
        ret = False
        
    while ret:
        
        ret,frame = cap.read()
        
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) #to change into BGR format
        
        VideoFileOutput.write(frame)
        
        cv2.imshow(windowname, frame)
        if cv2.waitKey(1) == 27:
            break
        
    cv2.destroyAllWindows()
    cap.release()
    VideoFileOutput.release()
        
if __name__ == "__main__":
    main()