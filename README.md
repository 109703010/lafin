To test the model, first download the pretrain model(trained with celebA)
from https://drive.google.com/file/d/1iCkh0k0I364u54nqGziPo6kxmcqLdEr_/view?usp=sharing,
and put it into checkpoints/model//

Then put your photos into the inputData/images/,
and put the corresponding masks into inputData/masks/. 

Use 
```./oneLineTest.sh```
to start training.

The results are under the directory checkpoints/model/results/landmark_inpaint/joint/