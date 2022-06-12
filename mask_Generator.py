import cv2
import numpy as np

mask = np.zeros((256,256,4), np.uint8)
mask[150:210, 80:185,:] = 255
# mask[150:, 60:200,:] = 255
# cv2.imshow('1', mask)
# cv2.waitKey(0)
cv2.imwrite('Fixed_mask.png', mask)
