import cv2
from detector import dt

#intialize my package
dt = dt.dt()

webcam = dt.capture("xxxxxx.mp4")
webcamIsOpened = webcam.isOpened()

while webcamIsOpened:
    #read the webcam video, and get us a frame
    success,img = webcam.read()
    if success:
        #convert to gray
        grayscale_img = dt.toGrayScale(img)
        #detect face and give us coordinates
        face_coordinates = dt.getCoordinates(grayscale_img)
        #draw rectangle
        dt.drawRectangle(img,face_coordinates)
        
        if dt.end(1):
            break
            
webcam.release()
cv2.destroyAllWindows()
print("Completed")
