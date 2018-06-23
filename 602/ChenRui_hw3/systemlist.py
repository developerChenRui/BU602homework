# Copyright 2017 ChenRui ruirui@bu.edu
import numpy as np

x = input()
h = input()
x = x.split()
h = h.split()

result=[0]*(len(x)+len(h)-1)
ans = ""
for i in range(len(x)):
	for j in range(len(h)):
		result[i+j] = int(x[i])*int(h[j]) + result[i+j]
for i in range(len(result)):
	ans = ans + str(int(result[i]))+" "
print(result)

# Copyright 2017 ChenRui ruirui@bu.edu
import numpy as np

x = input()
h = input()
x = x.split()
h = h.split()

result=np.zeros((1,len(x)+len(h)-1))
ans = ""
for i in range(len(x)):
	for j in range(len(h)):
		result[0][i+j] = int(x[i])*int(h[j]) + result[0][i+j]
for i in range(len(result[0])):
	ans = ans + str(int(result[0][i]))+" "
print(ans)




# Copyright 2017 ChenRui ruirui@bu.edu
import numpy as np

x = input()
h = input()
x = x.split()
h = h.split()

def transformTonum(inputStr):  # float() also ok

	X="";
	flag=0
	num = 0
	for i in range(len(inputStr)):
		if inputStr[i]!='.':
			X = X+inputStr[i]
		else: flag=len(inputStr)-1-i
	num = int(X)/(10**flag)
	return num


result=[0]*(len(x)+len(h)-1)
#ans = ""
for i in range(len(x)):
	for j in range(len(h)):
		result[i+j] = round(transformTonum(x[i])*transformTonum(h[j]),1) + result[i+j]
#ans = "("+ans+str(result[len(result)-1])+")"
while result[len(result)-1]==0 and len(result)>1:
	result = result[:-1]
for i in result:
	print(i)





