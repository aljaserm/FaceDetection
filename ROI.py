import cv2 as cv
import  numpy as np

img=cv.imread('hilal.jpg')

r=cv.selectROI(img)
cropped=img[int(r[1]):int(r[1]+r[3]),int(r[0]):int(r[0]+r[2])]

cv.imshow('Cropped',cropped)

cv.imwrite('cropped.jpg',cropped)

q=cv.waitKey(0)

if q==ord('q'):
    cv.destroyAllWindows()