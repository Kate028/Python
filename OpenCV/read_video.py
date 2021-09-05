import cv2

# create videocapture object
capture = cv2.VideoCapture("files/video.mp4")

# video is sequence of images 
# we need while loop to go through each frame one by one

while True:
    # save our img in capture_img and will let us know if it was successful or not(boolean).
    success, capture_img = capture.read()  
    
    # showing the result
    cv2.imshow("video", capture_img)

    # add a delay 
    # press 'q' to break the loop(close the video)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
