import numpy as np
import cv2 as cv
# Load an color image in grayscale
img = cv.imread('fire2.jpg',-1)#1为彩色，忽略透明度，0为灰色，-1不更改
cv.imshow('image',img)
cv.waitKey(0)
cv.destroyAllWindows()
#cv.imwrite('messigray.png',img)

""" from matplotlib import pyplot as plt
img = cv.imread('fire2.jpg',0)
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()
 """

