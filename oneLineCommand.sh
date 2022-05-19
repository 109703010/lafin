python3 ./scripts/flist.py --path inputData/images --output ./datasets/images.flist
python3 ./scripts/flist.py --path inputData/masks --output ./datasets/masks.flist
python3 test.py --model 3 --checkpoints ./checkpoints/model