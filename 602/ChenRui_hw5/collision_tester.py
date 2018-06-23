"""this is the main part of the assignment"""

# AUTHOR ? ?@bu.edu
# AUTHOR ? ??@bu.edu
# AUTHOR ??? ???@bu.edu
import unittest
import subprocess

#please change this to valid author emails
AUTHORS = ['?@bu.edu', '??@bu.edu', '???@bu.edu']

PROGRAM_TO_TEST = "collision"

def runprogram(program, args, inputstr):
    coll_run = subprocess.run(
        [program, *args],
        input=inputstr.encode(),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE)

    ret_code = coll_run.returncode
    program_output = coll_run.stdout.decode()
    program_errors = coll_run.stderr.decode()
    return (ret_code, program_output, program_errors)


class CollisionTestCase(unittest.TestCase):
    "empty class - write this"
    def test_one(self):
        strin = "one 20 10 -2 1"
        correct_out = "3\none 14 13 -2 1\n"
        (rc,out,errs) = runprogram(PROGRAM_TO_TEST,["3"],strin)
        self.assertEqual(rc,0)
        self.assertEqual(out,correct_out)
        self.assertEqual(errs,"")
        
#    def test_multiargs_collision(self):
#        strin = "one 0 0 2 0\ntwo 40 0 0 0"
#        correct_out = "2\none 4 0 2 0\ntwo 40 0 0 0\n4\none 8 0 2 0\ntwo 40 0 0 0\n20\none 30 0 0 0\ntwo 50 0 2 0\n"
#        (rc,out,errs) = runprogram(PROGRAM_TO_TEST,["2 4 20"],strin)
#        self.assertEqual(rc,0)
#        self.assertEqual(out,correct_out)
#        self.assertEqual(errs,"")
#    def 
        
    def test_programname(self):
        self.assertTrue(PROGRAM_TO_TEST.endswith('.py'),"wrong program name")

def main():
    "show how to use runprogram"

    print(runprogram('./test_program.py', ["4", "56", "test"], "my input"))
    unittest.main()

if __name__ == '__main__':
    main()

