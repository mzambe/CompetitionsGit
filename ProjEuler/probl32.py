#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import array
from itertools import *

def corrperm():
    lst = list(permutations(["1","2","3","4","5","6","7","8","9"]))

    return lst

def main():
    plst = corrperm()
    reslst = []
    for p in plst:
        for i in xrange(1, 5):
            a = list(p)
            a.insert(i, "*")
            a.insert(6, "==")
            if eval("".join(a)):
                print "".join(a)
                reslst.append(int("".join(a[-4:])))

    reslst = list(set(reslst))
    res = sum(reslst)
    print reslst, res

if __name__ == '__main__':
    main()
