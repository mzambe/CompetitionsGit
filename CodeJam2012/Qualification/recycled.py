#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from string import *

def main():
    T = input()
    for i in xrange(T):
        res = 0
        inp = raw_input()
        inp = map(int, inp.split())
        A = inp[0]
        af = str(A)[0]
        B = inp[1]
        bf = str(B)[0]
        for j in xrange(A, B + 1):
            jstr = str(j)
            strlen = len(jstr)
            lstprev = []
            for k in xrange(1, strlen):
                if ((jstr[k] >= af) and (jstr[k] <= bf) and (jstr[k] >= jstr[0])):
                    #print "Here", j
                    jdotf, jdotl = jstr[0:k], jstr[k:strlen]
                    jdot = int(jdotl + jdotf)
                    if (j < jdot) and (not jdot in lstprev):
                        if (jdot <= B) and (A <= jdot):
                            lstprev.append(jdot)
                            #print j, jdot, jdotf, jdotl
                            res += 1
        print ("Case #"+str(i+1)+":"), res

if __name__ == '__main__':
    main()
