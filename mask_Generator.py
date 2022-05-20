import cv2
import numpy as np

mask = np.zeros((256,256,4), np.uint8)
mask[150:210, 80:185,:] = 255
mask[150:210, 80:185,:] = 255
cv2.imwrite('Fixed_mask.png', mask)
