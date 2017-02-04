import cv2 
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('images/jazzfront.jpeg')
img = cv2.medianBlur(img,5)
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) 
ret,thresh = cv2.threshold(img_gray, 127 , 255 , cv2.THRESH_BINARY);
th2 = cv2.adaptiveThreshold(img_gray ,255 , cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY , 11 , 2 )
plt.imshow(thresh , 'gray')
plt.show()

