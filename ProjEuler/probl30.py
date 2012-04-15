#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import array

def main():
    powlist = {}
    lastnum = 0
    res = 0
    for i in xrange(10):
        powlist[i] = i**5

    for i in xrange(2, 1000000):
        diglist = map(int, str(i))
        sumdig = sum(map(lambda x: powlist[x], diglist))
        if i == sumdig:
            lastnum = i
            res += i

    print res, lastnum

if __name__ == '__main__':
    main()
