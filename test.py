import cv2 
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('images/jazzfront.jpeg')
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) 
ret,thresh = cv2.threshold(img_gray, 127 , 255 , cv2.THRESH_BINARY);
plt.imshow(thresh , 'gray')
plt.show()

