import cv2
import numpy as np


def detectColour(image):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    blue = cv2.inRange(hsv, (80, 80, 160), (200, 255, 255))
    pink = cv2.inRange(hsv, (156, 74, 76), (166, 255, 255))

    blue_px = cv2.countNonZero(blue)
    pink_px = cv2.countNonZero(pink)

    height, width, _ = image.shape
    pixels = height * width

    if (pixels / 100.0) * 30 <= blue_px:
        return "blue"
    elif (pixels / 100.0) * 30 <= pink_px:
        return "pink"

    return None

