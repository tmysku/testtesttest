#!/usr/bin/env python
#coding:utf-8
#---------------------------------------------------------------------
import unittest
from plus import plus
#---------------------------------------------------------------------
class TestPlus(unittest.TestCase):
    def test_int(self):
        self.assertEqual(plus(1, 2), 3, "Error on int")
    def test_float(self):
        self.assertTrue(3.299999 < plus(1.1, 2.2) < 3.300001, "error on float")
    def test_str(self):
        self.assertEqual(plus("ab", "cd"), "abcd", "error on str")
#---------------------------------------------------------------------
if __name__ == '__main__':
    unittest.main()
#---------------------------------------------------------------------
