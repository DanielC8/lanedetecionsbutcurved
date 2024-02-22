import cv2
import numpy as np

# researched from https://medium.com/analytics-vidhya/building-a-lane-detection-system-f7a727c6694
# get video from camera
video = cv2.VideoCapture(0)

while True:
    # get every frame of video
    ret, image = video.read()
    # breaks if the video has ended
    if image is None:
        break
    image = cv2.imread('ee.png')

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Find Canny edges
    edged = cv2.Canny(gray, 30, 200)

    # Finding Contours
    # Use a copy of the image e.g. edged.copy()
    # since findContours alters the image
    contours, hierarchy = cv2.findContours(edged,
                                           cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    cv2.imshow('Canny Edges After Contouring', edged)

    print("Number of Contours found = " + str(len(contours)))

    # Draw all contours
    # -1 signifies drawing all contours
    cv2.drawContours(image, contours, -1, (0, 255, 0), thickness=-1)

    # video with lines
    cv2.imshow("Lines", image)

    # breaks the video if chracter i is pressed
    if cv2.waitKey(15) & 0xFF == ord('i'):
        break
video.release()
cv2.destroyAllWindows()