import os
import random

file_source = 'celebA/train/images/img_align_celeba/'
file_destination = 'celebA/validation/images/'

get_files = os.listdir(file_source)

for g in get_files:
   if random.uniform(1, 10) > 8:
      os.replace(file_source + g, file_destination + g)