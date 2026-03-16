# This activity will guide students through accessing their computer’s camera and performing real-time face detection using OpenCV’s pre-trained Haar Cascade classifier.
import cv2

# Loading Haarcascade
faceCascade=  cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml') # haarcascade is a pre-trained model used for face detection.  

# Initialize video capture
cap= cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error! Could not open webcam")
    exit()

while True:
    ret, frame= cap.read()

    if not ret:
        print("Error! Failed to capture image")
        break
    gray= cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
# Detect faces in gray scale image
    faces= faceCascade.detectMultiScale(gray, scaleFactor= 1.1, minNeighbors= 5, minSize= (30,30)) # minneighbors will control how many detections are required to confirm a face.

# drawing rectangle around face
    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0), 2) # x and y are the top left corner of rectangle, x+w and y+h both are the bottom-right corners.
    
    # Display no. of faces
    font= cv2.FONT_HERSHEY_COMPLEX
    cv2.putText(frame, f"People count: {len(faces)} ", (10,30), font, 1, (255,0,0), 2, cv2.LINE_AA)
    
    cv2.imshow("Face Tracking and Counting", frame)

    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()
    


    
    

