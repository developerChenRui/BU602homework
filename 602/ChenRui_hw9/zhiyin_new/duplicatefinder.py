# Copyright jbc@bu.edu

"""Assignment9"""

from re import search
from hashlib import sha256, sha1
from sys import argv
from os import listdir
from collections import defaultdict
from numpy import transpose, nonzero
from skimage.io import imread


def search_digits(name):
    "re_sort_names"
    return int(search(r'[0-9]{1,4}', name).group())


def search_digits_line(line):
    "re_sort_lines"
    return int(search(r'[0-9]{1,4}', line[0]).group())


def generate_pic_key(name):
    "generate_picture_key"
    img = imread(name, as_grey=True)
    col, row = nonzero(img < 1)
    img = img[min(col):max(col)+1, min(row):max(row)+1]
    imgls = []
    translist = [img, img[::1, ::-1],
                 transpose(img[::-1, ]), transpose(img),
                 img[::-1, ::-1], img[::-1],
                 transpose(img[::1, ::-1]), transpose(img[::-1, ::-1])]
    for i in range(8):
        imgls.append(sha1(bytes(translist[i])).hexdigest())
    return frozenset(imgls)


def main():
    "main"
    categ, result = defaultdict(list), []
    for name in listdir():  #
        if name.endswith('png'):
            categ[generate_pic_key(name)].append(name)

    for k in categ:
        result.append(sorted(categ[k], key=search_digits))
    result.sort(key=search_digits_line)

    length = len(result)
    for i in range(length):
        result[i] = ' '.join(nm for nm in result[i])
    outstr = '\n'.join(line for line in result) + '\n'

    with open(argv[1], 'w') as outf:
        outf.write(outstr)

    print(sha256(outstr.encode('utf-8')).hexdigest())

main()
