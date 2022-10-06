import cv2
from cv2 import imshow
from numpy import where
from ExtractFrames import ExtractFrames

def main():
    
    #Camera Resolution Setup
    CAMERA_WIDTH = 1920
    CAMERA_HEIGHT = 1080
    
    #Transparent Video Setup
    VIDEO_WIDTH = 1920
    VIDEO_HEIGHT = 1080
    
    video_frames,num_of_frames=ExtractFrames(<!!!!!!!!!!!ENTER PATH TO FOLDER CONTAINING TRANSPARENT PNG HERE!!!!!!!!!!!>,(VIDEO_WIDTH,VIDEO_HEIGHT))
    
    
    #Webcam Setup
    vs = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    vs.set(cv2.CAP_PROP_FRAME_WIDTH, CAMERA_WIDTH)
    vs.set(cv2.CAP_PROP_FRAME_HEIGHT, CAMERA_HEIGHT)
    vs.set(cv2.CAP_PROP_FPS, 60)
    vs.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))
    
    
    #Window Setup
    cv2.namedWindow("window", cv2.WINDOW_NORMAL)
    cv2.setWindowProperty("window", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    
    
    #Variables Setup
    #Change x1 and y1 to modify starting position of transparent video overlay. 
    #!!!!DONT FORGET TO MAKE SURE WIDTH AND HEIGHT OF VIDEO FRAMES FIT IN WEBCAM FRAME IF YOU CHANGE x1 AND x2!!!!!! 
    #EXAMPLE: If x1 = 10 --> x2 = 10 + 1920 = 1930 >1920 --> ERROR
    
    x1 = 0
    y1 = 0
    
    
    x2 = x1 + VIDEO_WIDTH
    y2 = y1 + VIDEO_HEIGHT
    
    if(x2>CAMERA_HEIGHT or y1>CAMERA_WIDTH):
        print("Video Frame out of bound.")
    
    framecounter = 0
    
    while (1):
    
        ret, cameraframe = vs.read()
        
        if(not ret):
            print("Frame not found! Check Camera.")
    
    
    
        roi = cameraframe[y1:y2 , x1:x2]
        videoframe = video_frames[framecounter]
        finalroi = where((videoframe[..., 3] < 100)
                         [..., None] , roi, videoframe[..., 0:3])
        cameraframe[y1:y2 , x1:x2] = finalroi
        
    
    
        imshow("window", cameraframe)
        
        framecounter += 1
        
        if cv2.waitKey(20) & 0xFF == ord('q'):
            break
    
        if framecounter == num_of_frames:
            framecounter = 0
    
    
    cv2.destroyAllWindows()



if __name__=='__main__':
    main()