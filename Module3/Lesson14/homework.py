import cv2
import numpy as np


def apply_filter(image, filterType): 
    """Apply a filter to the image based on the filter type.""" # Its a docstring, just contains the details about what the function does. 
    img = image.copy()
    if filterType == "red_tint":
        img[:, :, 1] = img[:, :, 0] = 0
    elif filterType == "green_tint":
        img[:, :, 0] = img[:, :, 2] = 0
    elif filterType == "blue_tint":
        img[:, :, 1] = img[:, :, 2] = 0
    elif filterType == "sobel":
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        sx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=5)
        sy = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=5)
        sob = cv2.bitwise_or(sx.astype('uint8'), sy.astype('uint8'))
        img = cv2.cvtColor(sob, cv2.COLOR_GRAY2BGR)
    elif filterType == "canny":
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        can = cv2.Canny(gray, 150, 300)
        img = cv2.cvtColor(can, cv2.COLOR_GRAY2BGR)
    elif filterType == "cartoon":
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        gray = cv2.medianBlur(gray, 5)
        edges = cv2.adaptiveThreshold(
            gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9
        )
        color = cv2.bilateralFilter(image, 9, 300, 300)
        img = cv2.bitwise_and(color, color, mask=edges)
    return img


def main():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Could not initialize camera")
        return
    filterType = "original"
    print("Keys: r=Red, g=Green, b=Blue, s=Sobel, c=Canny, t=Cartoon, q=Quit")
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Can't receive frame")
            break
        out = apply_filter(frame, filterType)
        cv2.imshow("Filter", out)
        key = cv2.waitKey(1) & 0xFF
        if key == ord('r'):
            filterType = "red_tint"
        elif key == ord('g'):
            filterType = "green_tint"
        elif key == ord('b'):
            filterType = "blue_tint"
        elif key == ord('s'):
            filterType = "sobel"
        elif key == ord('c'):
            filterType = "canny"
        elif key == ord('t'):
            filterType = "cartoon"
        elif key == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()





