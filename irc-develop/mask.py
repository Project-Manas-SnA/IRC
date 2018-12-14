from box import detectColour
from qr import decode
import cv2

cap = cv2.VideoCapture(0)

if __name__ == "__main__":
    while True:
        ret,frame = cap.read()
        detectColour(frame)
        data = decode(frame)
        if data!=None:
                print(data)
        cv2.waitKey(1)
