#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from string import *

def main():
    n = input()
    googlerese = {'a': 'y', 'b': 'h', 'c': 'e', 'd': 's', 'e': 'o', 'f': 'c', 'g': 'v', 'h': 'x', 'i': 'd', 'j': 'u', 'k': 'i', 'l': 'g', 'm': 'l', 'n': 'b', 'o': 'k', 'p': 'r', 'q': 'z', 'r': 't', 's': 'n', 't': 'w', 'u': 'j', 'v': 'p', 'w': 'f', 'x': 'm', 'y': 'a', 'z': 'q'}
    for i in xrange(n):
        stringin = raw_input()
        for j in stringin:
            if ('a' <= j) and (j <= 'z'):
                stringin = replace(stringin, j, upper(googlerese[j]))
        stringin = lower(stringin)
        print ("Case #" + str(i + 1) + ":"), stringin

if __name__ == '__main__':
    main()
