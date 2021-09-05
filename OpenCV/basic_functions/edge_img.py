import cv2
import numpy as np

read_img = cv2.imread("files/fmh2.jpg")

# define a kernel #np.ones- all value is 1, size of matrix = 5x5
kernel = np.ones((5,5), np.uint8) # unsigned int of 8 bits(0-255)

# # convert img in greyscale
# # cvtColor() converts img into different color spaces
# imgGray = cv2.cvtColor(read_img, cv2.COLOR_BGR2GRAY)  # cv2.COLOR - color space you want to convert into

# imgBlur = cv2.GaussianBlur(imgGray, (7,7), 0) #ksize - kernal size - has to be odd no, sigmax =0

# finding edges in our image - we will use Canny func
imgCanny = cv2.Canny(read_img, 100, 100)  # threshold values 100,100 - can be any no.
# to increase thickness of edge, iteration= how much thickness we need 
imgDialation = cv2.dilate(imgCanny,kernel, iterations = 1 ) # add a kernel - size of and value of(use matrix)

# erosion - to make img edge thiner
imgEroded = cv2.erode(imgDialation, kernel, iterations=1)

# cv2.imshow("Gray Image", imgGray)
# cv2.imshow("Blur Image", imgBlur)
cv2.imshow("Blur Image", imgCanny)
cv2.imshow("Dialation Image", imgDialation)
cv2.imshow("Eroded Image", imgEroded)
cv2.waitKey(0)