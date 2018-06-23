# Copyright 2017 ChenRui ruirui@bu.edu
# Copyright 2017 mengxi wang wmx@bu.edu
# Copyright 2017 lyz lyz95222@bu.edu
"""Assignment9"""
from os import listdir
import re
from sys import argv
import hashlib
from skimage.io import imread
import numpy as np


def make_transforms(img):
    "transformatioin"
    transform_list = []
    transform_list.append(hashlib.sha1(bytes(img)).hexdigest())
    turn_mirror = img[::1, ::-1]
    turn_mirror_hash = hashlib.sha1(bytes(turn_mirror)).hexdigest()
    transform_list.append(turn_mirror_hash)
    turn_90 = np.transpose(img[::-1, ])
    turn_90_hash = hashlib.sha1(bytes(turn_90)).hexdigest()
    transform_list.append(turn_90_hash)
    turn_90_mirror = np.transpose(img)
    turn_90_mirror_hash = hashlib.sha1(bytes(turn_90_mirror)).hexdigest()
    transform_list.append(turn_90_mirror_hash)
    turn_180 = img[::-1, ::-1]
    turn_180_hash = hashlib.sha1(bytes(turn_180)).hexdigest()
    transform_list.append(turn_180_hash)
    turn_180_mirror = img[::-1]
    turn_180_mirror_hash = hashlib.sha1(bytes(turn_180_mirror)).hexdigest()
    transform_list.append(turn_180_mirror_hash)
    turn_270 = np.transpose(img[::1, ::-1])
    turn_270_hash = hashlib.sha1(bytes(turn_270)).hexdigest()
    transform_list.append(turn_270_hash)
    turn_270_mirror = np.transpose(img[::-1, ::-1])
    turn_270_mirror_hash = hashlib.sha1(bytes(turn_270_mirror)).hexdigest()
    transform_list.append(turn_270_mirror_hash)
    return frozenset(transform_list)


def main():
    "main"
    # get image file names
    files = []
    for file in listdir('.'):
        if file.endswith(".png"):
            files.append(file)
    # read in images and compare to existing
    Answer_List = {}
    for png in files:
        img = 1-imread(png, as_grey=True)  # read an inverse gray scale image
        x = np.nonzero(img)  # identify colored sqaures
        img = img[min(x[0]):max(x[0])+1, min(x[1]):max(x[1])+1]
        shape = make_transforms(img)
        if shape in Answer_List:
            Answer_List[shape].append(png)
        else:
            Answer_List[shape] = [png]
    # Order the matches appropriately
    ORDER = []
    regex = re.compile(r'\d+')
    for kind in Answer_List.values():
        for index, item in enumerate(kind):
            num = regex.findall(item)
            num = int(num[0])
            kind[index] = (num, item)
        ORDER.append(kind)
    for index, item in enumerate(ORDER):
        ORDER[index] = sorted(item)

    To_write = sorted(ORDER)
    # write to file
    result = ''
    for item in To_write:
        line = ''
        for index, img in enumerate(item):
            if index == len(item)-1:
                line = line + ''.join(img[1])
            else:
                line = line + ''.join(img[1]) + ' '
        result = result + line + '\n'

    with open(argv[1], 'w') as outf:
        outf.write(result)

    print(hashlib.sha256(result.encode('utf-8')).hexdigest())

main()