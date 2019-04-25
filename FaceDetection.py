import cv2 as cv

img = cv.imread("hilal.jpg")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
path = 'C:\\Users\\aljas\\OneDrive\\Documents\\Development\\Python\\OpenCV\\FaceDetection\\haarcascade_frontalface_default.xml'
face = cv.CascadeClassifier(path)
faces = face.detectMultiScale(gray, scaleFactor=1.10, minNeighbors=5, minSize=(40, 40))
print(len(faces))
for (x, y, w, h) in faces:
    cv.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

cv.imshow('Faces', img)
cv.waitKey(0)
