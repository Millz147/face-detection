import cv2

class dt:

    def __init__(self) -> None:
        self.trained_data_file = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


    def toGrayScale(self,img):
        return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    def getCoordinates(self,img):
       
        return self.trained_data_file.detectMultiScale(img)
    
    def drawRectangle(self,img,coordinates):
        for x,y,w,h in coordinates:
            cv2.rectangle(img,(x,y),(x+w, y+h),(0,255,0),2)
            cv2.imshow('Face Detector',img)
    def capture(self, src):
        if src == "webcam":
            return cv2.VideoCapture(0)
        elif src.endswith(('.mp4', '.3gp')):
            return cv2.VideoCapture(src)
        elif src.endswith(('.jpg', '.png', '.gif', '.jpeg')):
            return cv2.imread(src)
        else:
            raise ValueError("Unsupported source format: {}".format(src))

    def end(self,ms=0):
        quit =False
        keyPressed = cv2.waitKey(ms)
        # print(keyPressed)
        if keyPressed in (81, 113):
           quit=True
        return quit