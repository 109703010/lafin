# python3 splitData.py

python3 ./scripts/preprocess_celeba.py --path celebA/img_align_celeba/ --output celebA/
python3 ./scripts/flist.py --path celebA/train/images/ --output celebA/datasets/trainImages.flist
python3 ./scripts/flist.py --path celebA/validation/images/ --output celebA/datasets/validImages.flist

python3 ./scripts/preprocess_landmark.py --path celebA/train/images/ --output celebA/train/landmarks
python3 ./scripts/flist.py --path celebA/train/landmarks --output celebA/datasets/trainLandmarks.flist
python3 ./scripts/preprocess_landmark.py --path celebA/validation/images --output celebA/validation/landmarks
python3 ./scripts/flist.py --path celebA/validation/landmarks --output celebA/datasets/validLandmarks.flist

python3 maskSet.py

python3 train.py --model 1 --checkpoints checkpoints/celebA
python3 train.py --model 2 --checkpoints checkpoints/celebA