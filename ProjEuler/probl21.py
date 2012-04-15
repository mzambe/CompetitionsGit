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

def main():
    divarr = array.array('h')
    for i in xrange(0, 10001):
        divarr.append(0)
    res = 0
    for i in xrange(1, 10001):
        if (divarr[i] == 0):
            j = divarr[i] = sum(divis(i))
        else:
            j = divarr[i]
        if (j <= 10000):
            if (divarr[j] == 0):
                divarr[j] = sum(divis(j))
            if ((divarr[j] == i) and (i != j)):
                print i, j
                res += i

    print res

if __name__ == '__main__':
    main()
