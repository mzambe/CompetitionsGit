#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import array

def main():
    strnames = input()
    listnames = list(strnames)
    listnames.sort()
    teststr = "COLIN"
    print map(lambda x : ord(x) - ord('A') + 1, teststr)
    res = 0
    for i in xrange(len(listnames)):
        res += (sum(map(lambda x: ord(x) - ord('A') + 1, listnames[i])))*(i+1)
    print res

if __name__ == '__main__':
    main()
