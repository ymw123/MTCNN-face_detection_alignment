# MTCNN for face detection and alignment

![Python 3.6](https://img.shields.io/badge/python-3.6-green.svg?style=plastic)
![Pytorch 0.4.0](https://img.shields.io/badge/pytorch-0.4.0-green.svg?style=plastic)
![cuDNN 7.3.1](https://img.shields.io/badge/cudnn-7.3.1-green.svg?style=plastic)
![License CC BY-NC](https://img.shields.io/badge/license-CC_BY--NC-green.svg?style=plastic)

## Description
Recently, companies need to use face detection and face alignment. When I accept this job. Almost all the repos on the github which related face detection were downloaded into my disk. Through my learning about this, finally I decided use mtcnn since it can get best result for me. And it is widely accepted in industriy.
But, all of the high star repos on github have some common diseases:
1. No one-click script.
2. The loss function is wrong. The pnet and rnet also need landmark loss. Not just onet.
3. Since I'm familiar with pytorch and it considered to be suitable for image process, I decieded use pytorch. And most repos which written by pytorch were not updated for a long time. You run by them will appear lots of bugs.  

So, I write it myself. With lots of work I accept a nice result in online environment.

## Requirment
pytorch 0.4.0  

## Usage
### Predict
```bash
python predict.py --input-data-dir ./test
```
### Train
#### one-click script  
```bash
sh run.sh
```
  
  
#### step-by-step
```bash
python train.py
```

## Training data source
If you just make a toy, you can use this:
1. [WIDER FACE](http://shuoyang1213.me/WIDERFACE/) for face classification and face bounding box regression.
2. [CNN FACE](http://mmlab.ie.cuhk.edu.hk/archive/CNN_FacePoint.htm) for landmark regression.

Else if you have industrial needs you can connect [me](yangbisheng2009@gmail.com). The industrial version has much higher accuracy and recall rate.  

STATEMENT:  
The code between toy-version and industrial-version are same. The only difference is the data.
## Current status

## Detail
## Thanks
## TODO
The code will be upload before 2019-06-30.