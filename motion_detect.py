import cv2, time


video = cv2.VideoCapture(0)
first_frame = None

while True:
    check, frame = video.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    #blurring so we remove noises 
    gray = cv2.GaussianBlur(gray, (21,21),0)
    # we get the first frame
    if first_frame is None:
        first_frame = gray
        continue
    
    #creating a new img based on the first frame and the new frames
    comparing_frames = cv2.absdiff(first_frame,gray)
        
    cv2.imshow("Live", gray)
    cv2.imshow("Mixed Frames", comparing_frames)
    key = cv2.waitKey(1)
    
    
    if key == ord("q"):
        break


video.release()
cv2.destroyAllWindows()
