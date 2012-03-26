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

def getdigits(m):
    mym = m
    dig = []
    while (mym != 0):
        dig.append(mym % 10)
        mym = mym / 10

    return dig

def numlistostr(dig):
    digstr = ""
    for i in dig:
        digstr += str(i)
    return digstr

def palidrcheck(pstr):
    n = len(pstr)
    for i in range(0, n/2):
        if (pstr[i] != pstr[n - 1 - i]):
            return False
    return True

def main():
    u = 0
    i1 = 0
    j1 = 0
    for i in range(900, 1000):
        for j in range(i, 1000):
            m = i*j
            if (palidrcheck(numlistostr(getdigits(m)))):
                if(u < m):
                    i1 = i
                    j1 = j
                    u = m

    print u, i1, j1

if __name__ == '__main__':
    main()
