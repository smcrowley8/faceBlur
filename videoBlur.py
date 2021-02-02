import cv2
import numpy as np 

class FaceBlur:
    def __init__(self):
        self.face_cascade = cv2.CascadeClassifier('haarcascade_frontalface.xml')

    def blur_img(self, img):
        gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces=self.face_cascade.detectMultiScale(gray,1.3,5)
        #blur boxes
        for (x,y,w,h) in faces:
            sub_face=img[y:y+h, x:x+w]
            sub_face=cv2.GaussianBlur(sub_face, (23,23),70)
            img[y:y+sub_face.shape[0], x:x+sub_face.shape[1]] = sub_face

        #newImg=cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
        return img

    def process_img(self, imgPath='', outputPath=''):
        if outputPath=='':
            outputPath='output.png'
        if not imgPath=='':
            inImg=cv2.imread(imgPath)
            outImg=self.blur_img(inImg)
            cv2.imwrite(outputPath, outImg)
            

    def process_video(self, vidPath='', outputPath=''):
        if outputPath=='':
            outputPath='output.avi'
        if not vidPath=='': 

            inVid=cv2.VideoCapture(vidPath)
            outVid=[]
            width,height,layers=0,0,0
            while(inVid.isOpened()):
                ret,frame=inVid.read()
                height,width,layers=frame[1].shape #save for video saving

                outputImg=self.blur_img(frame)
                
                outVid.append(outputImg)
            #save new vid
            video=cv2.VideoWriter(outputPath, -1,1,(width,height))
            for i in range(len(outVid)):
                video.write(outVid)
        