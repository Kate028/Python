import cv2

# load face detector
face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# capture video from webcam
cap = cv2.VideoCapture(0)

while True:
    # read frame
    ret, img = cap.read()
    if not ret:
        continue
    # convert to grayscle
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # detect
    faces = face_detector.detectMultiScale(
        gray_img,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )
    cv2.imshow('img', img)
    # draw rectangle on each face
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

    cv2.imshow('img', img)
    if cv2.waitKey(1) == ord('q'): # press 'q' to quit
        break

cap.release()