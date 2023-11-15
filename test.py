"""A tiny example binary for the native Python rules of Bazel."""

import unittest
from lib import GetNumber
from fib import Fib


class TestGetNumber(unittest.TestCase):

  def test_ok(self):
    if GetNumber() == 42:
    	print("Number == ", GetNumber())
    else:
    	print("Number != ", GetNumber())
    	
  def test_fib(self):
    if Fib(5) == 8:
    	print("Fib(5) == ", Fib(5))
    else:
    	print("Fib(5) != ", Fib(5))

if __name__ == '__main__':
  unittest.main()
