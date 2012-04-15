#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import array
from itertools import *

def main():
    perm = list(permutations(['0','1','2','3','4','5','6','7','8','9']))
    perm.sort()
    print perm[999999]

if __name__ == '__main__':
    main()
