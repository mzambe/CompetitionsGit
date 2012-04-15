#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import array

def main():
    upl = 1
    upr = 1
    dwnr = 1
    dwnl = 1
    res = 1
    step = 1
    for i in xrange(500):
        step, upl, dwnr, upr, dwnl = step + 2, upl + 4*step + 2, dwnr + 4*step - 2, upr + 4*step + 4, dwnl +4*step
        res += upl + upr + dwnl + dwnr
        #print step, upl, upr, dwnl, dwnr
    print res

if __name__ == '__main__':
    main()
