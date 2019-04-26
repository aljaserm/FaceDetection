from PIL import Image
import pytesseract as pct
import argparse as ag
import cv2 as cv
import os

ap = ag.ArgumentParser()
ap.add_argument('-i', '--image', required=True)
ap.add_argument('-p', '--preprocess', default='thresh', type=str)

args = vars(ap.parse_args())
img = cv.imread(args['image'])
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# gray = cv.cvtColor(cv.UMat(img), cv.COLOR_RGB2GRAY)

if args['preprocess'] == 'thresh':
    gray = cv.threshold(gray, 0, 255, cv.THRESH_BINARY)
elif args['preprocess'] == 'blur':
    gray = cv.medianBlur(gray, 3)

filename = '{}.png'.format(os.getpid())
cv.imwrite(filename, gray,None)

text = pct.image_to_string(Image.open(filename))
os.remove(filename)
print(text)
cv.imshow('Img', img)
cv.imshow('gray', gray)

cv.waitKey(0)
