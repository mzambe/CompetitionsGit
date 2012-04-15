#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import array

def div4(x):
    if (x % 4) == 0:
        if (x % 100) == 0:
            if (x % 400) == 0:
                return 1
            else:
                return 0
        else:
            return 1
    else:
        return 0

def yeardays(months, mondays, x):
    count = 0
    for i in months:
        count += mondays[i](x)

    return count

def main():
    months = ("January", "Febuary", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
    mondays = {"January" : (lambda x: 31), "Febuary" : (lambda x: (28 + div4(x))), "March" : (lambda x: 31), "April" : (lambda x: 30), "May" : (lambda x: 31), "June" : (lambda x: 30), "July" : (lambda x: 31), "August" : (lambda x: 31), "September" : (lambda x: 30), "October" : (lambda x: 31), "November" : (lambda x: 30), "December" : (lambda x: 31)}
    count = 0
    day = 1
    day = (day + (yeardays(months, mondays, 1900))) % 7
    for i in xrange(1901, 2001):
        for j in months:
            print day
            if ((day % 7) == 0):
                count += 1
            day = (day + mondays[j](i)) % 7

    print count, day

if __name__ == '__main__':
    main()
