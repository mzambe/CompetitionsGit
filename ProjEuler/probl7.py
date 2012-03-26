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
    u = 1
    m = int(sys.argv[1])
    n = int(sys.argv[2])
    a = primes(m)

    if len(a) >= n:
        print a[n-1]
    else:
        print "NO!"

if __name__ == '__main__':
    main()
