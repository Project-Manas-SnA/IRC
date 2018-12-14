from box import detectColour
import cv2

cap = cv2.VideoCapture(0)

if __name__ == "__main__":
    while True:
        ret,frame = cap.read()
        detectColour(frame)
        cv2.waitKey(1)
