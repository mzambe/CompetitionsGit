#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import array

def fact(x):
    if x <= 1:
        return 1
    else:
        return x*fact(x - 1)

def main():
    print fact(100)
    print sum(map(int, str(fact(100))))

if __name__ == '__main__':
    main()
