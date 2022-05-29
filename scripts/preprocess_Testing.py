import os
import argparse
from skimage import io
from scipy.misc import imresize

output_path = "./inputData/images/"
dataset_path = "./inputData/images/"

filenames = os.listdir(dataset_path)

for filename in filenames:
    save_path = output_path
    img = io.imread(os.path.join(dataset_path,filename))
    h,w,c = img.shape
    border = (h-w)//2
    img = img[border:-border,...]
    img = imresize(img,(256,256))
    io.imsave(os.path.join(save_path,filename[:-4]+'.png'),img)





