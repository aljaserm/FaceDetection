import cv2 as cv
cap=cv.VideoCapture(0)
path = 'C:\\Users\\aljas\\OneDrive\\Documents\\Development\\Python\\OpenCV\\FaceDetection\\haarcascade_frontalface_default.xml'
faceCase=cv.CascadeClassifier(path)

while True:
    ret,Frame=cap.read()
    if ret==True:
        faces=faceCase.detectMultiScale(Frame,scaleFactor=1.10,minNeighbors=5,minSize=(40,40))
        if len(faces)!=0:
            for (x, y, w, h) in faces:
                cv.rectangle(Frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
                cv.imshow("Frame",Frame)
        else:
            cv.imshow("Frame", Frame)
    if cv.waitKey(33)==ord('q'):
        break

cap.release()
cv.destroyAllWindows()
