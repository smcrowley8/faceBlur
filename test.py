from videoBlur import FaceBlur 
import cv2 
import numpy as np 

blurrer=FaceBlur()

blurrer.process_img('me.jpg')