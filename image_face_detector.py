import cv2
from detector import dt
#intialize my package
dt = dt.dt()

img = dt.capture('one.jpg')


#convert to gray
grayscale_img = dt.toGrayScale(img)
#detect face
face_coordinates = dt.getCoordinates(grayscale_img)
dt.drawRectangle(img,face_coordinates)
dt.end()
print("Completed")
