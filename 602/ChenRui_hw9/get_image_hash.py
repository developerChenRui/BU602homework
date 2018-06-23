import cv2
#import cv2.cv as cv
import numpy as np
 
from compiler.ast import flatten
import sys
 
def pHash(imgfile):
	"""get image pHash value"""
	img=cv2.imread(imgfile, cv2.CV_LOAD_IMAGE_GRAYSCALE)
	img=cv2.resize(img,(32,32),interpolation=cv2.INTER_CUBIC)
 

	h, w = img.shape[:2]
	vis0 = np.zeros((h,w), np.float32)
	vis0[:h,:w] = img  
 

	vis1 = cv2.dct(cv2.dct(vis0))
	vis1.resize(8,8)
 
	img_list=flatten(vis1.tolist()) 
 
	avg = sum(img_list)*1./len(img_list)
	avg_list = ['0' if i<avg else '1' for i in img_list]
 
	return ''.join(['%x' % int(''.join(avg_list[x:x+4]),2) for x in range(0,64,4)])
 
if __name__ == '__main__':
    print pHash('/Users/chenrui/Desktop/602/ChenRui_hw9/duplicate_examples/one/rasber502.png')