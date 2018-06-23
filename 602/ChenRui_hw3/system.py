# Copyright 2017 ChenRui ruirui@bu.edu
import numpy as np
x = input()
h = input()
x = x.split()
h = h.split()
result=[0]*(len(x)+len(h)-1)
for i in range(len(x)):
	for j in range(len(h)):
		result[i+j] = round(float(x[i])*float(h[j]),1) + result[i+j]
while result[len(result)-1]==0 and len(result)>1:
	result = result[:-1]
for i in result:
	print(i)
