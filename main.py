#Real time face detection using OpenCV
import cv2

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

#Start video capture from webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

while True:
    #Capture frame-by-frame
    ret, frame = cap.read()

    #Check if frame is read correctly
    if not ret:
        print("Error: Could not read frame.")
        break

    #Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #Detect the faces in gray scale image
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    #Draw rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    #Display the resulting frame
    cv2.imshow('Face Detection', frame)

    #Break the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#Release the capture and destroy all windows
cap.release()
cv2.destroyAllWindows()