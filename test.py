import cv2
import numpy as np

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
    # turns into grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # gaussianblur
    gray = cv2.GaussianBlur(gray, (15, 15), 0)

    canny = cv2.Canny(gray, 100, 150)
    cannycopy = canny.copy()
    circles = cv2.HoughCircles(canny, cv2.HOUGH_GRADIENT, 1.5, 999, param1=120, param2=70, minRadius=0, maxRadius=0)
    # loops through the circles
    if circles is not None:
        circlelist = np.uint16(np.around(circles))
        # generates a circle and center dot for each circle
        for circle in circlelist[0, :]:
            x = circle[0]
            y = circle[1]
            radius = circle[2]
            # draws the circle
            cv2.ellipse(frame, (x, y), (radius, radius), 0,0, -90,(0,255,0),15)

            # draw a dot at the center
            cv2.circle(frame, (x, y), 1, (50, 255, 20), 10)

        height, width = canny.shape
        # this makes a rectangle
        mask = np.zeros_like(gray)
        # points of the rectangle
        point1 = (0, height)
        point2 = (0, y-radius+20)
        point3 = (x+radius-20, y-radius+20)
        point4 = (x+radius-20, height)
        cv2.line(frame, point1, point2, (0, 255, 0), 3)
        cv2.line(frame, point2, point3, (0, 255, 0), 3)
        cv2.line(frame, point3, point4, (0, 255, 255), 3)
        cv2.line(frame, point4, point1, (255, 255, 255), 3)
        # array showing the coordinates of the trapezoid
        rectangle = np.array([[point1, point2, point3, point4]])

        # creates plolygon
        mask = cv2.fillPoly(mask, rectangle, 255)
        # adds the mask
        mask = cv2.bitwise_and(canny, mask)
        circlespart2 = cv2.HoughCircles(mask, cv2.HOUGH_GRADIENT, 1.5, 999, param1=120, param2=70, minRadius=0, maxRadius=0)
        # loops through the circles
        if circlespart2 is not None:
            circlelist = np.uint16(np.around(circlespart2))
            # generates a circle and center dot for each circle
            for circle in circlelist[0, :]:
                x2 = circle[0]
                y2 = circle[1]
                radius2 = circle[2]
                # draws the arc
                cv2.ellipse(frame, (x2, y2), (radius2, radius2), 0,0, -90,(0,255,0),15)

            cv2.ellipse(frame, (x, y), ((radius2+radius)//2, (radius2+radius)//2), 0, 0, -90, (255, 0, 255), 15)



    # shows the untouched video
    cv2.imshow("Camera", canny)
    # video with lines
    cv2.imshow("Lines", frame)

    # breaks the video if chracter i is pressed
    if cv2.waitKey(15) & 0xFF == ord('i'):
        break
video.release()
cv2.destroyAllWindows()