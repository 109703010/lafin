import cv2
import os

INPUT_PATH = './inputData/images/'
OUTPUT_PATH = INPUT_PATH

filenames = os.listdir(INPUT_PATH)

for file in filenames:
    img = cv2.imread(os.path.join(INPUT_PATH, file))
    img = cv2.resize(img, (256,256))
    cv2.imwrite(os.path.join(INPUT_PATH,file[:-4]+'.jpg'), img)