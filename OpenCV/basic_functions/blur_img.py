import cv2

read_img = cv2.imread("files/fmh2.jpg")

# convert img in greyscale
# cvtColor() converts img into different color spaces
imgGray = cv2.cvtColor(read_img, cv2.COLOR_BGR2GRAY)  # cv2.COLOR - color space you want to convert into

imgBlur = cv2.GaussianBlur(imgGray, (7,7), 0) #ksize - kernal size - has to be odd no, sigmax =0

cv2.imshow("Gray Image", imgGray)
cv2.imshow("Blur Image", imgBlur)
cv2.waitKey(0)
