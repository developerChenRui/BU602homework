"""this is the main part of the assignment"""

# Copyright 2017 ChenRui ruirui@bu.edu
# Copyright 2017 Peixin Li pxli@bu.edu
# Copyright 2017 Yimeng Wang wym613@bu.edu

import unittest
import subprocess
import math
import sys
#import timeout_decorator
#please change this to valid author emails
AUTHORS = ['ruirui@bu.edu','pxli@bu.edu','wym613@bu.edu']

PROGRAM_TO_TEST = "collisionc_0"
#@timeout_decorator.timeout(0.1)
def runprogram(program, args, inputstr):
    coll_run = subprocess.run(
        [program, *args],
        input=inputstr.encode(),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,timeout=0.1)

    ret_code = coll_run.returncode
    program_output = coll_run.stdout.decode()
    program_errors = coll_run.stderr.decode()
    return (ret_code, program_output, program_errors)

def float_check(out,arg_num,ball_num):
    out_corrected=""
    temp = out.split('\n')
    for target in range(0,(1+ball_num)*arg_num,ball_num+1):
        if float(temp[target])-math.floor(float(temp[target]))==0:
            temp[target] = str(math.floor(float(temp[target])))

    for i in range(len(temp)):
        out_corrected = out_corrected + temp[i]
        if i < len(temp)-1:
            out_corrected = out_corrected+"\n"

    return out_corrected
    
#def float_check(out,arg_num,ball_num):
#    return out.replace('.0000','')
    






class CollisionTestCase(unittest.TestCase):
#    def setUp(self):
 #    suffix="_hard"
  #   self.assertFalse(PROGRAM_TO_TEST.endswith(suffix),"wrong program name")
#    def tearDown(self):
#     pass
    "empty class - write this"
#    def trick(out):
#        out_corrected=""
#        temp = out.split('\n')
#        if float(temp[0])-math.floor(float(temp[0]))==0:
#            temp[0] = str(math.floor(float(temp[0])))
#        for i in range(len(temp)):
#            out_corrected = out_corrected + temp[i]
#            if i < len(temp)-1:
#                out_corrected = out_corrected+"\n"
#


    def test_large_number(self):
    	strin = "one 9999999.9999 9999999.9999 -0.9999 -0.9999"
    	correct_out = "1\none 9999999 9999999 -0.9999 -0.9999\n"
    	(rc,out,errs) = runprogram(PROGRAM_TO_TEST,["1"],strin)
    	out = float_check(out,1,1)
    	self.assertEqual(rc,0)
    	self.assertEqual(out,correct_out)
    	self.assertEqual(errs,"")

    def test_large_time(self):
        strin = "one 20 10 -2 1"
        correct_out = "3000000\none -5999980 3000010 -2 1\n"
        (rc,out,errs) = runprogram(PROGRAM_TO_TEST,["3000000"],strin)

        out = float_check(out,1,1)
        self.assertEqual(rc,0)
        self.assertEqual(out,correct_out)
        self.assertEqual(errs,"")

    def test_input_twelve_input(self):
        strin = "one 10 10 1 1"
        correct_out = "1\none 11 11 1 1\n2\none 12 12 1 1\n3\none 13 13 1 1\n4\none 14 14 1 1\n5\none 15 15 1 1\n6\none 16 16 1 1\n7\none 17 17 1 1\n8\none 18 18 1 1\n9\none 19 19 1 1\n10\none 20 20 1 1\n11\none 21 21 1 1\n12\none 22 22 1 1\n13\none 23 23 1 1\n14\none 24 24 1 1\n15\none 25 25 1 1\n16\none 26 26 1 1\n17\none 27 27 1 1\n18\none 28 28 1 1\n19\none 29 29 1 1\n20\none 30 30 1 1\n21\none 31 31 1 1\n"
        (rc,out,errs) = runprogram(PROGRAM_TO_TEST,["1","2","3","4","5","6","7",
        	"8","9",'10',"11","12","13","14","15",'16',"17","18","19","20","21"],strin)

        out = float_check(out,21,1)
        self.assertEqual(rc,0)
        self.assertEqual(out,correct_out)
        self.assertEqual(errs,"")
    def test_12_ball(self):
        strin = "i 0 0 0 0\ni 0 0 0 0\ni 0 0 0 0\ni 0 0 0 0\ni 0 0 0 0\ni 0 0 0 0\ni 0 0 0 0\ni 0 0 0 0\ni 0 0 0 0\ni 0 0 0 0\ni 0 0 0 0\ni 0 0 0 0"
        correct_out = "1\ni 0 0 0 0\ni 0 0 0 0\ni 0 0 0 0\ni 0 0 0 0\ni 0 0 0 0\ni 0 0 0 0\ni 0 0 0 0\ni 0 0 0 0\ni 0 0 0 0\ni 0 0 0 0\ni 0 0 0 0\ni 0 0 0 0\n"
        (rc,out,errs) = runprogram(PROGRAM_TO_TEST,["1"],strin)
        out = float_check(out,1,12)
        self.assertEqual(rc,0)
        self.assertEqual(out,correct_out)
        self.assertEqual(errs,"")

    def test_ball_name(self):
        strin = "o_n1e?^_ 20 10 -2 1"
        correct_out = "3\no_n1e?^_ 14 13 -2 1\n"
        (rc,out,errs) = runprogram(PROGRAM_TO_TEST,["3"],strin)

        out = float_check(out,1,1)
        self.assertEqual(rc,0)
        self.assertEqual(out,correct_out)
        self.assertEqual(errs,"")
        
    def test_reverse_time(self):
        strin = "one 20 10 0 0"
        correct_out = '1\none 20 10 0 0\n3\none 20 10 0 0\n'
        (rc,out,errs) = runprogram(PROGRAM_TO_TEST,['3','1'],strin)
        out = float_check(out,2,1)
        self.assertEqual(rc,0)
        self.assertEqual(out,correct_out)
        self.assertEqual(errs,"")

        
    def test_one(self):
        strin = "one 20 10 -2 1"
        correct_out = "3\none 14 13 -2 1\n"
        (rc,out,errs) = runprogram(PROGRAM_TO_TEST,["3"],strin)

        out = float_check(out,1,1)
        self.assertEqual(rc,0)
        self.assertEqual(out,correct_out)
        self.assertEqual(errs,"")
        
    def test_onearg_collision(self):
        strin = "one 0 0 2 0\ntwo 40 0 0 0"
        correct_out = "20\none 30 0 0 0\ntwo 50 0 2 0\n"
        (rc,out,errs) = runprogram(PROGRAM_TO_TEST,["20"],strin)
        out = float_check(out,1,2)
        self.assertEqual(rc,0)
        self.assertEqual(out,correct_out)
        self.assertEqual(errs,"")
        
    def test_multiargs_collision(self):
        strin = "one 0 0 2 0\ntwo 40 0 0 0"
        correct_out = "2\none 4 0 2 0\ntwo 40 0 0 0\n4\none 8 0 2 0\ntwo 40 0 0 0\n20\none 30 0 0 0\ntwo 50 0 2 0\n"
        (rc,out,errs) = runprogram(PROGRAM_TO_TEST,['2','4','20'],strin)
        out = float_check(out,3,2)
        self.assertEqual(rc,0)
        self.assertEqual(out,correct_out)
        self.assertEqual(errs,"")

    def input_format(self):
        strin = "one"
        correct_out = ""
        (rc,out,errs) = runprogram(PROGRAM_TO_TEST,["2"],strin)

        self.assertEqual(rc,1)
        self.assertEqual(out,correct_out)
        self.assertEqual(errs,"")

    def bad_input(self):
        strin = "one i 10 10 10"
        correct_out = ""
        (rc,out,errs) = runprogram(PROGRAM_TO_TEST,["2"],strin)

        self.assertEqual(rc,1)
        self.assertEqual(out,correct_out)
        self.assertEqual(errs,"")

    def invalid_command_line(self):
        strin = "one 1 10 10 10"
        correct_out = ""
        (rc,out,errs) = runprogram(PROGRAM_TO_TEST,["i"],strin)

        self.assertEqual(rc,2)
        self.assertEqual(out,correct_out)
        self.assertEqual(errs,"")
    def invalid_command_input(self):
        strin = "one 1 10 10 10"
        correct_out = ""
        (rc,out,errs) = runprogram(PROGRAM_TO_TEST,["1 2 3"],strin)

        self.assertEqual(rc,2)
        self.assertEqual(out,correct_out)
        self.assertEqual(errs,"")
    def test_three(self):
        strin = "one 0 0 3 4\ntwo 40 0 -3 4\nthree 80 0 -3 4"       
        correct_out = "6\none 12 24 -3 4\ntwo 28 24 3 4\nthree 62 24 -3 4\n11\none -3 44 -3 4\ntwo 37 44 -3 4\nthree 53 44 3 4\n"
        (rc,out,errs) = runprogram(PROGRAM_TO_TEST,['6','11'],strin)
        out = float_check(out,2,3)
        self.assertEqual(rc,0)
        self.assertEqual(out,correct_out)
        self.assertEqual(errs,"")
    def test_four(self):
        strin = "one -20 0 3 4\ntwo 0 0 3 4\nthree 40 0 -3 4\nfour 80 0 -3 4"       
        correct_out = "11\none -13 44 -3 4\ntwo 23 44 3 4\nthree 37 44 -3 4\nfour 53 44 3 4\n"
        (rc,out,errs) = runprogram(PROGRAM_TO_TEST,["11"],strin)
        out = float_check(out,1,4)
        self.assertEqual(rc,0)
        self.assertEqual(out,correct_out)
        self.assertEqual(errs,"")
    def none_command_line(self):
        strin = "one 1 10 10 10"
        correct_out = ''
        (rc,out,errs) = runprogram(PROGRAM_TO_TEST,[''],strin)

        self.assertEqual(rc,2)
        self.assertEqual(out,correct_out)
        self.assertEqual(errs,"")
    def test_digit(self):
        strin = "one 1.1111 2.4111 2.5 3.6"
        correct_out = "2\none 6.1111 9.6111 2.5 3.6\n"
        (rc,out,errs) = runprogram(PROGRAM_TO_TEST,['2'],strin)
        out = float_check(out,1,1)
        self.assertEqual(rc,0)
        self.assertEqual(out,correct_out)
        self.assertEqual(errs,"")
    def test_no_return(self):
        strin = "one -20 0 3 4 two 0 0 3 4 three 40 0 -3 4"
        correct_out = ''
        (rc,out,errs) = runprogram(PROGRAM_TO_TEST,['2'],strin)

        self.assertEqual(rc,1)
        self.assertEqual(out,correct_out)
        self.assertEqual(errs,"")


    def test_programname(self):
        self.assertTrue(PROGRAM_TO_TEST.startswith('col'),"wrong program name")

def main():
    "show how to use runprogram"

    print(runprogram('./test_program.py', ["4", "56", "test"], "my input"))
    unittest.main()

if __name__ == '__main__':
    main()

