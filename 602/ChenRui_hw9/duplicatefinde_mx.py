from os import listdir
import re
from skimage.io import imread
import numpy as np
import hashlib

#img=imread('orange817.png')
#m=hashlib.sha256(img).hexdigest()
#img2=imread('kiwi9117.png')
#n=hashlib.sha256(img2).hexdigest()
#print(m)
#print(n)

def make_transforms(img):

    #change hash libs to just standard hash
    transform_list = []
    
    transform_list.append(hashlib.sha256(bytes(img)).hexdigest())
    
    turn_mirror = img[::1,::-1]
    turn_mirror_hash = hashlib.sha256(bytes(turn_mirror)).hexdigest()
    transform_list.append(turn_mirror_hash)

    turn_90 = np.transpose(img[::-1,])
    turn_90_hash = hashlib.sha256(bytes(turn_90)).hexdigest()
    transform_list.append(turn_90_hash)
                
    turn_90_mirror = np.transpose(img)
    turn_90_mirror_hash = hashlib.sha256(bytes(turn_90_mirror)).hexdigest()
    transform_list.append(turn_90_mirror_hash)

    turn_180 = img[::-1,::-1]
    turn_180_hash = hashlib.sha256(bytes(turn_180)).hexdigest()
    transform_list.append(turn_180_hash)
                
                
    turn_180_mirror = img[::-1]
    turn_180_mirror_hash = hashlib.sha256(bytes(turn_180_mirror)).hexdigest()
    transform_list.append(turn_180_mirror_hash)

    turn_270 = np.transpose(img[::1,::-1])
    turn_270_hash = hashlib.sha256(bytes(turn_270)).hexdigest()
    transform_list.append(turn_270_hash)
                
                
    turn_270_mirror = np.transpose(img[::-1,::-1])
    turn_270_mirror_hash = hashlib.sha256(bytes(turn_270_mirror)).hexdigest()
    transform_list.append(turn_270_mirror_hash)

    
    return frozenset(transform_list)

def main():
    files = []
    for file in listdir('/Users/wangmengxi/Documents/mercy/wmx_ec602/hw9/duplicate_examples/one'):
        if file.endswith(".png"):
            files.append(file)
    
    # read in images and compare
    
    ans = {}
    
    for png in files:
        img = 1-imread(png,as_grey=True) # read gray scale image
        x = np.nonzero(img) # identify colored sqaures
        img = img[min(x[0]):max(x[0])+1,min(x[1]):max(x[1])+1] # object area
        shape = make_transforms(img)
        if shape in ans.keys():
            ans[shape].append(png)
        else:
            ans[shape] = [png]

    order = []
    reg = re.compile(r'\d+')

    for i in ans.keys():
        order.append(ans[i])
        
  
    for j in range(len(order)):
        for k in range(len(order[j])):
            num = reg.findall(order[j][k])
            num = int(num[0])
            order[j][k] = (num,order[j][k])
            

    order.sort()

    for t in range(len(order)):
        order[t] = sorted(order[t])

    To_write = sorted(order)
    # write to file 
    with open("answers_one.txt", "w") as text_file:
        for l in range(len(To_write)):
            for m in range(len(To_write[l])):
                if m == len(To_write[l])-1:
                    text_file.write(To_write[l][m][1])
                else:
                    text_file.write(To_write[l][m][1]+ " ")
            text_file.write("\n")
#
#    has = open('answers_one.txt','r')
#    h = has.read()
#    done = hashlib.sha256(bytes(h)).hexdigest()
#    has.close()
#
#    print(done)
#    return done
    
    
if __name__ == '__main__':
    main()