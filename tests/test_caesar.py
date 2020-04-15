import os
import random
import string
import sys
import unittest
from random import seed

from experder import *

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
seed(1000)

CHARS = string.ascii_letters + string.punctuation + ' ' + string.digits


# function to generate a random string of length k
def gen_rands(k):
    return ''.join(random.choice(CHARS))


class test_caesar(unittest.TestCase):

    def test_basics(self):
        self.assertEqual(caesar_rshift('abc'), 'nop')
        self.assertEqual(caesar_lshift('nop'), 'abc')
        caesar_bruteforce('nom')
        tenkey_rshift('aaaaa', 16543)
        tenkey_lshift('aaaaa', 16543)

    def test_rshift(self):
        teststring = 'aaa'
        self.assertEqual(caesar_rshift(teststring, 1), 'bbb')
        self.assertEqual(caesar_rshift(teststring, 9), 'jjj')
        self.assertEqual(caesar_rshift(teststring, 26), 'aaa')
        self.assertEqual(caesar_rshift(teststring, 0), 'aaa')
        teststring = 'AAA'
        self.assertEqual(caesar_rshift(teststring, 9), 'JJJ')

    def test_lshift(self):
        teststring = 'zzz'
        self.assertEqual(caesar_lshift(teststring, 1), 'yyy')
        self.assertEqual(caesar_lshift(teststring, 10), 'ppp')
        self.assertEqual(caesar_lshift(teststring, 0), 'zzz')
        self.assertEqual(caesar_lshift(teststring, 26), 'zzz')
        teststring = 'ZZZ'
        self.assertEqual(caesar_lshift(teststring, 2), 'XXX')

    def test_bruteforce(self):
        teststring = gen_rands(10)
        caesar_bruteforce(teststring)

    def test_tenkey_rshift(self):
        teststring = gen_rands(40)
        key = random.randint(1000000000, 9999999999)
        self.assertEqual(tenkey_lshift(tenkey_rshift(teststring, key), key),
                         teststring)
        self.assertEqual(
            tenkey_lshift(tenkey_rshift(teststring, key, False), key, False),
            teststring)


if __name__ == '__main__':
    unittest.main()
