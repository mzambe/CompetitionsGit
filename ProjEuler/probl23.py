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

def divis(x):
    divisors = []
    for i in xrange(1, x):
        if (x % i) == 0:
            divisors.append(i)

    return divisors

def abundant():
    abu = []
    for i in xrange(1, 30000):
        if (sum(divis(i)) > i):
            abu.append(i)

    return abu

def main():
    abu = abundant()
    divarr = array.array('h')
    for i in xrange(0, 30001):
        divarr.append(0)
    res = 0

    for i in abu:
        for j in abu:
            if (i+j) <= 30000:
                divarr[i+j] = 1

    for i in xrange(1, 30001):
        if (divarr[i] == 0):
            res += i

    print res

if __name__ == '__main__':
    main()
