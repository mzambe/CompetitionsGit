#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import array
from itertools import *

def fib(n):
    a, b = 1, 1
    for i in xrange(3, n + 1):
        a ,b = b, (a + b)

    return b

def main():
    a, b = 1, 1
    for i in xrange(3, 5000):
        a ,b = b, (a + b)
        if (len(str(b))) == 1000:
            print i
            break

if __name__ == '__main__':
    main()
