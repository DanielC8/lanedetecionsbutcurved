import cv2
import numpy as np
from Paralleldetection import *

# researched from https://medium.com/analytics-vidhya/building-a-lane-detection-system-f7a727c6694
# get video from camera
video = cv2.VideoCapture(0)

while True:
    # get every frame of video
    ret, frame = video.read()
    # breaks if the video has ended
    if frame is None:
        break
    # duplicate the frame
    dup = frame.copy()

    frame = linedetect(frame)
    # shows the untouched video
    cv2.imshow("Camera", dup)
    # video with lines
    cv2.imshow("Lines", frame)

    # breaks the video if chracter i is pressed
    if cv2.waitKey(15) & 0xFF == ord('i'):
        break
video.release()
cv2.destroyAllWindows()