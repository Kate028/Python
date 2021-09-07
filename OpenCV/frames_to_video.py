import cv2
import time

vidcap = cv2.VideoCapture('big_buck_bunny_720p_5mb.mp4')
success,frame = vidcap.read()
count = 0
while success:
  cv2.imwrite("frame%d.jpg" % count, frame)     # save frame as JPEG file      
  success,frame = vidcap.read()
  print('Read a new frame: ', success)
  count += 1

starttime = time.time()

# get frame
timestamp = time.time() - starttime
cv2.putText(frame,timestamp,(10,500), 4,(255,255,255),2,cv2.CV_AA)

0   