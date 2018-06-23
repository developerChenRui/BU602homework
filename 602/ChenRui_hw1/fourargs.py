# Copyright 2017 ChenRui ruirui@bu.edu
import sys
#fout = open('stdout_python_'+str(len(sys.argv))+'.txt','w')
#sys.stdout = fout

#ferr = open('stderr_python_'+str(len(sys.argv))+'.txt','w')
#sys.stderr = ferr

for i in range(1,5):
	if i<len(sys.argv):
	   print(sys.argv[i])
for i in range(5,len(sys.argv)):
	if i<len(sys.argv):
	   sys.stderr.write(sys.argv[i]+"\n")