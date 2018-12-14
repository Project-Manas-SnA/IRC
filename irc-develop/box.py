import cv2
import numpy as np


def detectColour(image):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    blue = cv2.inRange(hsv,(90,180,160),(200,255,255))

    red_l = cv2.inRange(hsv,(0,100,120),(10,255,255))
    red_u = cv2.inRange(hsv,(160,100,100),(179,255,255))
    red = red_l + red_u

    green = cv2.inRange(hsv,(45,40,30),(80,255,255))

    cv2.imshow("blue",blue)
    cv2.imshow("green",green)
    cv2.imshow("red",red)

    blue_px = cv2.countNonZero(blue)
    red_px = cv2.countNonZero(red)
    green_px = cv2.countNonZero(green)

    height, width, _ = image.shape
    pixels = height * width

    if (pixels / 100.0) * 30 <= blue_px:
        return "blue"
    elif (pixels / 100.0) * 30 <= red_px:
        return "red"
    elif (pixels / 100.0) + 30 <= green_px:
        return "green"

    return None


