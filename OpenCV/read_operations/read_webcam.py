import cv2

# create webcam object  # id of webcam # if having one webcam enter 0 else id of webcam
capture = cv2.VideoCapture(0)


capture.set(3,640)   # define width (id= 3)
capture.set(4,480)   # define height (id = 4)

# increasing brightness id is 10 for brightness
capture.set(10, 100)

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