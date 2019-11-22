import cv2.cv as cv
import cv2
import threading

cv.NamedWindow("camera", 1)

capture = cv2.VideoCapture(0)

count = 0
faces = []

class DetectThread(threading.Thread):
    def __init__(self, img, faces):
        super(DetectThread, self).__init__()
        self.img = img
        self.faces = faces
    def run(self):
        gray = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
        detectedFaces = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml').detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=3,
            minSize=(30, 30),
            flags=cv.CV_HAAR_SCALE_IMAGE
        )
        self.faces[:] = detectedFaces

while True:
    _, img = capture.read()
    img = cv2.resize(img, (320, 240))
    if count == 30:
        thread = DetectThread(img, faces)
        thread.start()
        count = 0
    else:
        count += 1
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
    cv2.imshow("camera", img)
    if cv.WaitKey(10) > 0:
      break
cv.DestroyAllWindows()