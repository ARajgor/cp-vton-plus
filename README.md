# CP-VTON+ (new 2023)

## Original Author
credits to original author. A very exceptional work. here the details.<br><br>
visit orignial repo : https://github.com/minar09/cp-vton-plus <br><br> 
Official implementation for "CP-VTON+: Clothing Shape and Texture Preserving Image-Based Virtual Try-On" from CVPRW 2020.
<br/>Project page: https://minar09.github.io/cpvtonplus/. 
<br/>Saved/Pre-trained models: [Checkpoints](https://1drv.ms/u/s!Ai8t8GAHdzVUiQA-o3C7cnrfGN6O?e=EaRiFP)
<br/>Dataset: [VITON_PLUS](https://1drv.ms/u/s!Ai8t8GAHdzVUiQQYX0azYhqIDPP6?e=4cpFTI)

## what's new 
- I upgrade the project to new version of libraries.
- code is tested on the new version of torch=1.13.1, torchvision=0.14.1 using with python 3.9 pip installation.
- run only one file app.py that can automatically run both commands (GMM and TOM). It also take care of copy of files.
- fix all the deprecated warning of torch and resolve all isuses regarding dependency.
- have a dedicated branch for only-cpu version.

if you find any problem feel free to raise issue.

### Pre-trained Models and datasets

download pre-trained models and dataset. copy the pre-trained models to checkpoints/ folder. copy the datasets to data/ folder.

### Installation
run `pip install -r requirements.txt`

### How to run
Run `python app.py` it will take care of both the operation GMM and TOM. you can customize as per your requirements. it also has copy functionality of files. if you want to run actual commands refer below steps.
<br>
for tensorboard run `tensorboard --logdir tensorboard`

### Testing with custom images

you can refer my other repo for this, https://github.com/ARajgor/VTryon-flask-new <br>
it is based on Flask App for custom images. A big thanks to @vinodbukya6 (https://github.com/vinodbukya6/cp-VTryon-plus-Flask-App) to make flask based application. I  fixed the minor bugs and upgrade to new version.

