import cv2
cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")

name = input("file name:")
OUTPUT_PATH = './inputData/images/'

if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    ret, frame = cap.read()
    if not ret:
        print("Cannot receive frame")
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray)
    eyes = eye_cascade.detectMultiScale(gray)
    if len(faces) != 0 and len(eyes) != 0:
        cv2.imwrite(OUTPUT_PATH+name+'.jpg', frame)
    for (x, y, w, h) in eyes:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 255), 2)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 0), 2)
    cv2.imshow('oxxostudio', frame)
    if cv2.waitKey(1000) == ord('q'):
        break     # 按下 q 鍵停止
cap.release()
cv2.destroyAllWindows()