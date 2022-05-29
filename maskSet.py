import glob

names = glob.glob("celebA/train/images/*")

f = open('celebA/datasets/trainMasks.flist', 'w')
for i in range(len(names)):
    f.write("celebA/train/masks/Fixed_mask.png\n")
f.close()

names = glob.glob("celebA/validation/images/*")

f = open('celebA/datasets/validMasks.flist', 'w')
for i in range(len(names)):
    f.write("celebA/validation/masks/Fixed_mask.png\n")
f.close()