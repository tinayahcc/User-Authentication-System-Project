import cv2
import numpy as np
from pyzbar.pyzbar import decode

class Video(object):
    def __init__(self):
        self.video=cv2.VideoCapture(0)
    def __del__(self):
        self.video.release()
    def get_frame(self):

        received_data = None
        with open('zzzz\myData_File_final.txt') as f:
            myDataList = f.read()

        ret,frame=self.video.read()

        for barcode in decode(frame):
            myData = barcode.data.decode('utf-8')
            if myData != received_data:
                #print(myData)
                if myData in myDataList:
                    #print('Unlock')
                    myOutput = 'Unlock'
                    myColor = (0,255,0)
                else:
                    #print('Lock')
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

        ret,jpg=cv2.imencode('.jpg',frame)
        return jpg.tobytes()
    