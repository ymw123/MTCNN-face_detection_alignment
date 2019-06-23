#!/usr/bin/env python
#-*- coding: utf-8 -*-

'''

@author: yangfengguang

@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.

@contact: yangbisheng2009@gmail.com

@file: preprocess_pnet.py

@time: 2019/6/23 15:43

@desc:

'''

import sys
import os
import argparse
import numpy as np
import cv2
import numpy.random as npr

import config

def gen_pnet_data(args):


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='preprocess pnet data')
    parser.add_argument('--cls-bbox-train-dir', default=config.CLS_BBOX_TRAIN_DIR, help='face train data temporary folder')
    parser.add_argument('--annotation', default=os.path.join(config.ANNOTATION_FILE, "wider_origin_anno.txt"),
                        help='wider face original annotation file')
    args = parser.parse_args()

    print(args)
