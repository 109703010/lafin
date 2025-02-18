import numpy as np
import cv2
import os

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")

INPUT_PATH = './inputData/images/'
OUTPUT_PATH = './inputData/masks/'

select = input('file name:')
if select == '0':
  filenames = os.listdir(INPUT_PATH)
else:
  filenames = [select + '.jpg']
for file in filenames:
    img = cv2.imread(os.path.join(INPUT_PATH, file))
    # img = cv2.resize(img, (256,256))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray)
    for (x, y, w, h) in faces:
        # cv2.rectangle(img, (x,y), (x+w, y+h), (0, 255, 0), 2)
        x1 = x - 80
        x2 = x + w + 65
        y1 = y - 65
        y2 = y + h + 30
        new_img = img[y1:y2, x1:x2]
        new_img = cv2.resize(new_img, (256,256))
        cv2.rectangle(img, (x,y), (x+w, y+h), (0, 255, 0), 2)
    gray = cv2.cvtColor(new_img, cv2.COLOR_BGR2GRAY)
    eyes = eye_cascade.detectMultiScale(gray)
    y_mask = 0
    for (x, y, w, h) in eyes:
        # cv2.rectangle(img, (x,y), (x+w, y+h), (0, 255, 255), 2)
        y1_mask = max(y_mask, y+h)
    faces = face_cascade.detectMultiScale(gray)
    for (x, y, w, h) in faces:
        # cv2.rectangle(img, (x,y), (x+w, y+h), (0, 255, 0), 2)
        x1_mask = x
        x2_mask = x + w
        y2_mask = y + h
    mask = np.zeros((256,256,4), np.uint8)
    mask[y1_mask-8:y2_mask+20,x1_mask:x2_mask,:] = 255
    # img[y_mask-10:,:,:] = 255
    cv2.imwrite(os.path.join(INPUT_PATH,file[:-4]+'.jpg'), new_img)
    cv2.imwrite(os.path.join(OUTPUT_PATH,file[:-4]+'.png'), mask)
    # cv2.imshow('img', img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()