import cv2

read_img = cv2.imread("feles/fmh2.jpg")

cv2.imshow("output", read_img)

cv2.waitKey(0)   # 0 means infinite delay
