# CP-VTON+ (new 2023)

## Original Author
```
@InProceedings{Minar_CPP_2020_CVPR_Workshops,
	title={CP-VTON+: Clothing Shape and Texture Preserving Image-Based Virtual Try-On},
	author={Minar, Matiur Rahman and Thai Thanh Tuan and Ahn, Heejune and Rosin, Paul and Lai, Yu-Kun},
	booktitle = {The IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) Workshops},
	month = {June},
	year = {2020}
}
```

credits to original author. A very exceptional work. here the details.<br>
visit original repo : https://github.com/minar09/cp-vton-plus <br><br> 
Official implementation for "CP-VTON+: Clothing Shape and Texture Preserving Image-Based Virtual Try-On" from CVPRW 2020.
<br/>Project page: https://minar09.github.io/cpvtonplus/. 
<br/>Saved/Pre-trained models: [Checkpoints](https://1drv.ms/u/s!Ai8t8GAHdzVUiQA-o3C7cnrfGN6O?e=EaRiFP)
<br/>Dataset: [VITON_PLUS](https://1drv.ms/u/s!Ai8t8GAHdzVUiQQYX0azYhqIDPP6?e=4cpFTI)

## what's new 
- I upgrade the project to new version of libraries.
- code is tested on the new version of torch=1.13.1, torchvision=0.14.1 using with python 3.9 pip installation. [March2023 update: code is compatible with torch 2.0.0+cu117 on python 3.9.13]
- run only one file app.py for testing/training. it can automatically run both commands (GMM and TOM) and take care of copying files. 
if you want to train first then `Line 8 : subprocess.call(gmm_train, shell=True)`<br>`Line 17 :subprocess.call(gmm_train, shell=True)`
- fix all the deprecated warning of torch and resolve all isuses regarding dependency.
- have a dedicated branch for only-cpu version.

if you find any problem feel free to raise issue.


## Installation and Run

run `pip install -r requirements.txt`

### AutoRun
Run `python app.py` it will take care of both the operation GMM and TOM. you can customize as per your requirements. it also has copy functionality of files. if you want to run actual commands refer below steps.
<br>
for tensorboard run `tensorboard --logdir tensorboard`

### Training
Run `python train.py` with your specific usage options for GMM and TOM stage. \
example GMM: `python train.py --name GMM --stage GMM --workers 4 --save_count 5000 --shuffle`

Then run `test.py` for GMM network with the training dataset, which will generate the warped clothes and masks in "warp-cloth" and "warp-mask" folders inside the "result/GMM/train/" directory. Copy the "warp-cloth" and "warp-mask" folders into your data directory, for example inside "data/train" folder.\
example TOM: `python train.py --name TOM --stage TOM --workers 4 --save_count 5000 --shuffle`

### Testing
Run `python test.py` with your specific usage options.\
example, GMM: `python test.py --name GMM --stage GMM --workers 4 --datamode test --data_list test_pairs.txt --checkpoint checkpoints/GMM/gmm_final.pth`

Then run `test.py` for GMM network with the testing dataset, which will generate the warped clothes and masks in "warp-cloth" and "warp-mask" folders inside the "result/GMM/test/" directory. Copy the "warp-cloth" and "warp-mask" folders into your data directory, for example inside "data/test" folder.\
example TOM: `python test.py --name TOM --stage TOM --workers 4 --datamode test --data_list test_pairs.txt --checkpoint checkpoints/TOM/tom_final.pth`


## Pre-trained Models and datasets

download pre-trained models and dataset. \
Create checkpoints folder and copy the pre-trained models to checkpoints/ . [Checkpoints](https://1drv.ms/u/s!Ai8t8GAHdzVUiQA-o3C7cnrfGN6O?e=EaRiFP)\
Create data folder copy the datasets to data/ folder. [VITON_PLUS](https://1drv.ms/u/s!Ai8t8GAHdzVUiQQYX0azYhqIDPP6?e=4cpFTI)


## Testing with custom images

you can refer my other repo for this, https://github.com/ARajgor/VTryon-flask-new <br>
it is based on Flask App for custom images. A big thanks to @vinodbukya6 (https://github.com/vinodbukya6/cp-VTryon-plus-Flask-App) to make flask based application. I  fixed the minor bugs and upgrade to new version.

