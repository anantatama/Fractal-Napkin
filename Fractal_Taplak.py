import numpy as np
import cv2
import math

#Declare the size of canvas
image = np.zeros((500,500,3), np.uint8)

x = 250 	#Titik pusat awal
y = 250		#Titik pusat awal
rad = 50	#Radius dari lingkaran

def draw(x,y,rad):
	#Create the circle
	cv2.circle(image, (x, y), rad, (255,255,255), 1)
	#Attractor, to stop the generation of fractal
	if rad > 0 :

		#Transformation
		x2 = x + int(math.cos(math.radians(90)))
		y2 = y + int(math.sin(math.radians(90)))
		
		#Recursive step
		draw(int(x2+rad*2), y2, int(rad/2))
		draw(x2, int(y2+rad*2), int(rad/2))
		draw(int(x2-rad*2), y2, int(rad/2))
		draw(x2, int(y2-rad*2), int(rad/2))
#Calling the draw function
draw(x, y, 50)
cv2.imwrite("circle.png", image)

#This is optional
#Preview
cv2.imshow("image", image)
cv2.waitKey(0)
