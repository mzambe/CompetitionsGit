#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import array

def main():
    lst = []
    for a in xrange(2, 101):
        for b in xrange(2, 101):
            lst.append(a**b)
    lst = list(set(lst))

    print len(lst)

if __name__ == '__main__':
    main()
