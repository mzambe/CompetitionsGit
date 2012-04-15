#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import array
from itertools import *

def primes(n):
    natnum = array.array('h')
    for i in range(0, n + 1):
        natnum.append(1)
    primes = [2]
    i = 2
    while ((i <= n) and (i != -1)):
        j = 2*i
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

    return (primes, natnum)

def polcheck(a, b, prms):
    cnt = 2
    poly = lambda x: (x*x + a*x + b)
    for i in xrange(2, 80):
        if poly(i) > 0:
            if (prms[poly(i)] == 1):
                cnt += 1
            else:
                break
        else:
            break

    return cnt

def main():
    bs = (primes(1000))[0]
    prms = (primes(100000))[1]
    res = 0
    resa = 0
    resb = 0
    for b in bs:
        ass = list(imap(lambda x: x - b - 1, list(bs)))
        for a in ass:
            tpl = polcheck(a, b, prms)
            if res < tpl:
                res = tpl
                resa = a
                resb = b

    print resa, resb, res, resa*resb

    #print polcheck(1, 41, prms), prms[2]

if __name__ == '__main__':
    main()
