# Rotate an image by 45 degrees and adjust its brightness to see the effects of basic arithmetic operations on images.
import cv2
import matplotlib.pyplot as plt
import numpy as np

image= cv2.imread('example.jpg')
# Convert BGR to RGB
imageRGB= cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Rotate image by 45 degree.
(h,w)=image.shape[:2] # :2 is just used to take height and width as there are 3 values by which image is represented(height,width and color channel), so it ignores the channel.
center= (w//2,h//2) # finding centre of image.
M= cv2.getRotationMatrix2D(center,45,1.0)
rotated= cv2.warpAffine(image, M, (w,h))

rotatedRGB= cv2.cvtColor(rotated, cv2.COLOR_BGR2RGB)
plt.imshow(rotatedRGB)
plt.title("Rotated Image")
plt.show()

# Changine the brightness
brightnessMatrics= np.ones(image.shape, dtype="uint8")*75 # np is a library for numerical operations in python.
brighter= cv2.add(image,brightnessMatrics) # add function is used to combine the two images for a more brighter image.

brighterRGB= cv2.cvtColor(brighter, cv2.COLOR_BGR2RGB)
plt.imshow(brighterRGB)
plt.title("BRIGHTER IMAGE")
plt.show()
