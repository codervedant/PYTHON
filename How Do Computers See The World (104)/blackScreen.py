import cv2
import numpy as np

#CREATE A BLACK IMAGE
black = np.zeros([600,600])

f_col = black[1:2,:]
print(f_col)

black[200:400,200:400] = 255
print(black)
cv2.imshow("black",black)
cv2.waitKey(0)
