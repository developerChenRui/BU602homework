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
    transform_list = ()
    transform_list += (hashlib.sha1(bytes(img)).hexdigest(),)
    turn_mirror = img[::1, ::-1]
    transform_list += (hashlib.sha1(bytes(turn_mirror)).hexdigest(),)
    turn_90 = np.transpose(img[::-1, ])
    transform_list += (hashlib.sha1(bytes(turn_90)).hexdigest(),)
    turn_90_mirror = np.transpose(img)
    transform_list += (hashlib.sha1(bytes(turn_90_mirror)).hexdigest(),)
    turn_180 = img[::-1, ::-1]
    transform_list += (hashlib.sha1(bytes(turn_180)).hexdigest(),)
    turn_180_mirror = img[::-1]
    transform_list += (hashlib.sha1(bytes(turn_180_mirror)).hexdigest(),)
    turn_270 = np.transpose(img[::1, ::-1])
    transform_list += (hashlib.sha1(bytes(turn_270)).hexdigest(),)
    turn_270_mirror = np.transpose(img[::-1, ::-1])
    transform_list += (hashlib.sha1(bytes(turn_270_mirror)).hexdigest(),)
    return frozenset(transform_list)


def main():
    "main"
    # get image file names
    answer = {}
    regex = re.compile(r'\d+')
    for png in listdir('.'):
        if png.endswith(".png"):
            num = regex.findall(png)
            num = int(num[0])
            img = 1-imread(png, as_grey=True)
            cut = np.nonzero(img)
            img = img[min(cut[0]):max(cut[0])+1, min(cut[1]):max(cut[1])+1]
            shape = make_transforms(img)
            if shape in answer:
                answer[shape].append((num, png))
            else:
                answer[shape] = [(num, png)]
    # Order the matches appropriately
    order_img = list(answer.values())
    for index, item in enumerate(order_img):
        order_img[index] = sorted(item)

    write_to_file = sorted(order_img)
    # write to file
    result = ''
    for item in write_to_file:
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
