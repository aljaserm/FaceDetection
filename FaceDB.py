import cv2 as cv
import os
facepath='haarcascade_frontalface_default.xml'
faceCase=cv.CascadeClassifier(facepath)

def getImages():
    if not  os.path.exists('database'):
        os.makedirs('database')

    picId=len(os.listdir('database/'))
    for files in ['source','source2']:
        for image in os.listdir(files):
            try:
                imgPath=str(files)+'/'+str(image)
                image=cv.imread(imgPath)
                gray=cv.cvtColor(image,cv.COLOR_BGR2GRAY)
                faces=faceCase.detectMultiScale(gray,scaleFactor=1.10,minNeighbors=8,minSize=(40,40))

                for (x,y,w,h) in faces:
                    resizeImg=image[y:y+h,x:x+w]
                    cv.imwrite('database/' + str(picId) + '.jpg', resizeImg)

                picId+=1
                print('Successful')
            except Exception as e:
                print(str(e))


getImages()

