import pyzbar.pyzbar as pyzbar
import cv2
def decode(image):
  decodedObjects = pyzbar.decode(image)

  for obj in decodedObjects:
    if obj.type == "QRCODE":
        print(obj.type)
        return obj.data
