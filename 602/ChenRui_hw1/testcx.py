import sys
for i in sys.argv[1:5]:
	print(i)
for i in sys.argv[5:]:
	print(i,file = sys.stderr)