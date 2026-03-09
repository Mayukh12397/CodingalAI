#load an image, convert it to grayscale, resize it to a standard size (224x224), display the processed image, and optionally save it based on key press.
import cv2

image= cv2.imread("dogimage.jpg")
grayImage= cv2.cvtColor(image,cv2.COLOR_BGR2GRAY) # this line of code will convert image to grayscale. first arguement is the image variable and the second arguement is BGR2GRAY. This is taken from cv2. This will specify to convert image to grayscale.
resizedImage= cv2.resize(grayImage, (224,224) )
cv2.imshow('processed image', resizedImage)
key=cv2.waitKey(0)

if key== ord('s'):
    cv2.imwrite('grayscaleResizedImage.jpg', resizedImage)
    print("image saved")
else:
    print("Image not saved")
cv2.destroyAllWindows()
print("imagedimension: ", resizedImage.shape) 

