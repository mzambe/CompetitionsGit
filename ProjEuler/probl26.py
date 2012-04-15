#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import array
from itertools import *

def divpros(n, m):
    modulst = []
    cnt = 0
    divis = n
    while ((not (divis in modulst)) and (divis != 0)):
        modulst.append(divis)
        while (divis < m):
            divis = divis*10
        #print m, divis
        divis = divis % m
        cnt += 1

    #print cnt, modulst, m
    if (divis in modulst):
        return (len(modulst) - modulst.index(divis))
    else:
        return 0

def main():
    res = 0
    resi = 0
    for i in xrange(1, 1000):
        a = divpros(1, i)
        if res < a:
            res = a
            resi = i
        print i, a
    #divpros(1, 884)

    print res, resi

if __name__ == '__main__':
    main()
