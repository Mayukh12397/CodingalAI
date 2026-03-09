# py -m pip install opencv-python (for installation of open cv library. It contains functions for image processing and computer vision task.)
import cv2

image= cv2.imread('dogimage.jpg') # its used to load the image
cv2.namedWindow('loaded image', cv2.WINDOW_NORMAL) # it creates a window where you can display the image.
cv2.resizeWindow('loaded image', 800,500) # sets the size to 800*500 pixels and its also resizable.(width- 800, height - 500)
cv2.imshow('loaded image', image ) # it displays the image in the created window with the set credentials of the size of the image. Arguements are the data you are passing in the function. e.g- in imshow function, image variable, created window(loaded image).
cv2.waitKey(0) # 0 represents indefinity and it will wait indefinetely until a key is pressed.
cv2.destroyAllWindows() #close the windows. If there is any open window, it should be closed properly.
print("imagedimension: ", image.shape) # it will just print the dimensions of the image in the terminal.