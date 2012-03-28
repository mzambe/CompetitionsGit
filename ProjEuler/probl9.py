#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import array

def primes(n):
    natnum = array.array('h')
    for i in range(0, n + 1):
        natnum.append(1)
    primes = [2]
    i = 2
    while ((i <= n) and (i != -1)):
        j = i
        while (j <= n):
            natnum[j] = 0
            j += i
        u = i + 1
        while ((u <= n) and (natnum[u] == 0)):
            u += 1
        if (u <= n):
            i = u
            primes.append(i)
        else:
            i = -1

    return primes

def main():
    for a in range(1, 1000):
        u = 1000000 - 2000*a
        v = 2000 - 2*a
        if (u % v) == 0:
            b = u / v
            c = 1000 -b -a
            print a, b, c
            print a*b*c

if __name__ == '__main__':
    main()
