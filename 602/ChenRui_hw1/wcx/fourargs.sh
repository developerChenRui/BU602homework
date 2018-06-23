# copyright ChunxiWang tracycxw@bu.edu
#!/bin/bash

g++ fourargs.cpp -o fourargs
python fourargs.py one two 3 four five six
python fourargs.py one two 3
./fourargs one two 3 four five six
./fourargs one two 3