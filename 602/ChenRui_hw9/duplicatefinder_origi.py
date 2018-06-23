#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 14:59:19 2017

@author: chenrui
"""

from os import listdir
import re
from skimage.io import imread
import numpy as np
import hashlib

dir0 = "/Users/chenrui/Desktop/602/ChenRui_hw9/duplicate_examples"
dir1 = listdir(r"/Users/chenrui/Desktop/602/ChenRui_hw9/duplicate_examples")
dir1 = dir1[1:]

for item in dir1:
    dir2 = listdir(dir0+'/'+item)
    for image in dir2:
        if image[-3:] == 'png':
            image_path = dir2 + image
        
        
        