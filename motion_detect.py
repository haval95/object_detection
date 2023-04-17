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
    
    #chaning the color of the moving parts that are bigger than 30 to white
    #this returns two values, first one is needed when we use other thresh methods but not in binary.
    thresh_frame = cv2.threshold(comparing_frames, 30, 255, cv2.THRESH_BINARY)[1]
    #clearing the black holes in the img
    thresh_frame = cv2.dilate(thresh_frame, None, iterations=3)
    
    #FINDING THE MOVING AREAS WHEN ARE TWO DIFFERENT OBJECTS
    (cnts,_) = cv2.findContours(thresh_frame.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)  
    
    #checking the moving parts if they are big enough to draw a rect around it 
    for countour in cnts:
        if cv2.contourArea(countour) < 1000:
            continue
        (x,y,w,h) = cv2.boundingRect(countour)
        cv2.rectangle(frame, (x,y), (x+w, y+h),(0,255,0),3)
        
        
        
 
    cv2.imshow("Live", frame)
    cv2.imshow("Mixed Frames", comparing_frames)
    cv2.imshow("Thresh", thresh_frame)
    key = cv2.waitKey(1)
    
    
    if key == ord("q"):
        break


video.release()
cv2.destroyAllWindows()
