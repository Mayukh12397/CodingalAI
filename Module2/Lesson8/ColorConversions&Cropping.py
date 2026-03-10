#py -m pip install matplotlib 9installation of matplot library).
import cv2
import matplotlib.pyplot as plt # pyplot module is for displaying the image. Its a module in matplot library.

image= cv2.imread('example.jpg')
# Convert BGR to RGB
imageRGB= cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
plt.imshow(imageRGB) # displaying the image in the window.
plt.title("RGB IMAGE")
plt.show() # to display the window

# Convert to grayscale
grayimage= cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
plt.imshow(grayimage, cmap='gray')
plt.title("GRAY IMAGE")
plt.show()

# crop the image
croppedImage= image[100:300,200:400] # 100:300 is for height and 200:400 is for width. Cropped image will include pixels from 100 to 299 and 200 to 399.
croppedImageRGB= cv2.cvtColor(croppedImage, cv2.COLOR_BGR2RGB)
plt.imshow(croppedImageRGB)
plt.title("CROPPED IMAGE(RGB)")
plt.show()

