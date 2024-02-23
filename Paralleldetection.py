import cv2
import numpy as np

def linedetect(frame):
    # turns into grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # gaussianblur
    gray = cv2.GaussianBlur(gray, (15, 15), 0)
    # finds the black areas

    # gets all the edges
    canny = cv2.Canny(gray, 140, 150)

    # gets the  height and width of the frame
    height, width = canny.shape
    # this makes a rectangle
    #mask = np.zeros_like(gray)
    # points of the rectangle
    #point1 = (100, height - 150)
    #point2 = (100, 100)
    #point3 = (height - 150, 100)
    #point4 = (height - 150, height - 150)
    # array showing the coordinates of the trapezoid
    #trapezoid = np.array([[point1, point2, point3, point4]])
    # outlines the rectangle for user use
    #cv2.line(frame, point1, point2, (255, 255, 255), 3)
    #cv2.line(frame, point2, point3, (255, 255, 255), 3)
    #cv2.line(frame, point3, point4, (255, 255, 255), 3)
    #cv2.line(frame, point4, point1, (255, 255, 255), 3)
    # creates plolygon
    #mask = cv2.fillPoly(mask, trapezoid, 255)
    # adds the mask
    #mask = cv2.bitwise_and(canny, mask)

    # houghlines (gets a set of lines that are outlined in the masked image)
    lines = cv2.HoughLinesP(canny, 1, np.pi / 180, 50, maxLineGap=100, minLineLength=80)
    # lists for slopes
    slopes = {}
    # keeps track of the number of kinda unique slopes
    slopecount = {}
    # makes sure there are lines
    if lines is not None:
        for line in lines:
            # gets endpoints for line
            x1, y1, x2, y2 = line[0]
            cv2.line(frame, (x1, y1), (x2, y2), (255, 0, 255), 3)

            # if the slope is infinite then set it to a huge number
            try:
                slope = (y1 - y2) / (x1 - x2)
            except:
                slope = 99999999999999999999999
            # adds the slope to the slopes dictionary with the endpoints of the line
            slopes[(x1, y1), (x2, y2)] = slope
            # keeps track of the unique slope count
            test = 0
            for a in slopecount:
                # looks to see if the slope is similar to the slopes in slopecount
                if a - 0.2 < slope < 0.2 + a:
                    slopecount[a] += 1
                    test = 1
                    break
            if test == 0:
                slopecount[slope] = 1
    slopeintercept = {}
    for a in slopecount:
        if a - 0.2 < slope < 0.2 + a:


    return(frame)


def maskout(frame,point1,point2,point3,point4):
    # gets the  height and width of the frame
    height, width = frame.shape
    # this makes a rectangle
    mask = np.zeros_like(gray)

    # array showing the coordinates of the trapezoid
    trapezoid = np.array([[point1, point2, point3, point4]])
    # outlines the rectangle for user use
    cv2.line(frame, point1, point2, (255, 255, 255), 3)
    cv2.line(frame, point2, point3, (255, 255, 255), 3)
    cv2.line(frame, point3, point4, (255, 255, 255), 3)
    cv2.line(frame, point4, point1, (255, 255, 255), 3)
    # creates plolygon
    mask = cv2.fillPoly(mask, trapezoid, 255)
    # adds the mask
    mask = cv2.bitwise_and(canny, mask)
    return(mask)