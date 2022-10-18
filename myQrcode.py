import cv2
import numpy as np
from pyzbar.pyzbar import decode

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
received_data = None

with open('zzzz\myData_File_final.txt') as f:
    myDataList = f.read()

while True:

    ret, frame = cap.read()
    for barcode in decode(frame):
        myData = barcode.data.decode('utf-8')

        if myData != received_data:
            print(myData)
            if myData in myDataList:
                print('Unlock. Please enjoy the movie')
                myOutput = 'Unlock'
                myColor = (0,255,0)
            else:
                print('Lock. Sorry, the QR Code does not match.')
                myOutput = 'Lock'
                myColor = (0,0,255)
            received_data = myData
        else:
            pass

        pts = np.array([barcode.polygon],np.int32)
        pts = pts.reshape((-1,1,2))
        cv2.polylines(frame,[pts],True,myColor,5)
        pts2 = barcode.rect
        cv2.putText(frame,myOutput,(pts2[0],pts2[1]),cv2.FONT_HERSHEY_SIMPLEX,
        0.9,myColor,2)

    cv2.imshow('Result',frame)
    
    if cv2.waitKey(1) & 0xFF == ord('e'):
      break
cap.release()
cv2.destroyAllWindows()