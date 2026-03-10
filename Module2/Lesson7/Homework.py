import cv2

# load the image
image = cv2.imread("dogimage.jpg")

# predefined sizes
size1 = (800, 500)
size2 = (400, 300)
size3 = (224, 224)

# resizing the image into three sizes
resizedImage1 = cv2.resize(image, size1)
resizedImage2 = cv2.resize(image, size2)
resizedImage3 = cv2.resize(image, size3)

# display the resized images
cv2.imshow("Resized Image 1 (800x500)", resizedImage1)
cv2.imshow("Resized Image 2 (400x300)", resizedImage2)
cv2.imshow("Resized Image 3 (224x224)", resizedImage3)

# wait indefinitely until a key is pressed
cv2.waitKey(0)

# save the resized images
cv2.imwrite("resizedImage_800x500.jpg", resizedImage1)
cv2.imwrite("resizedImage_400x300.jpg", resizedImage2)
cv2.imwrite("resizedImage_224x224.jpg", resizedImage3)

print("All resized images are saved.")

# print dimensions of each image
print("Image 1 dimension:", resizedImage1.shape)
print("Image 2 dimension:", resizedImage2.shape)
print("Image 3 dimension:", resizedImage3.shape)

# close all windows
cv2.destroyAllWindows()