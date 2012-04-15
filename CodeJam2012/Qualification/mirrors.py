#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from math import *

def reflpoint(mir, point, origin):
    ret = False
    newpoint = []
    if mir[0] == 'lv':
        if (point[0] > mir[1]):
            newpoint = [(2*mir[1] - point[0]), point[1]]
    elif mir[0] == 'rv':
        if (point[0] < mir[1]):
            newpoint = [(2*mir[1] - point[0]), point[1]]
    elif mir[0] == 'dh':
        if (point[1] > mir[1]):
            newpoint = [point[0], (2*mir[1] - point[1])]
    elif mir[0] == 'uh':
        if (point[1] < mir[1]):
            newpoint = [point[0], (2*mir[1] - point[1])]

    if newpoint != []:
        newmirlst = []
        mirlst = point[2]
        for i in mirlst:
            a = reflmirror(mir, i)
            if a != ():
                newmirlst.append(a)
        newpoint.append(newmirlst)

        if isCurrRefl(origin, mir, newpoint):
            newpoint[2] = []
            ret = True
        else:
            newpoint[2].append(mir)

    return (newpoint, ret)

def checkmirtouch(mir, point, origin):
    if mir[0][1] == 'v':
        if mir[0][0] == 'l':
            if origin[0] < mir[1]:
                return False
        elif mir[0][0] == 'r':
            if origin[0] > mir[1]:
                return False

        if point[0] != origin[0]:
            a = (point[1] - origin[1])/(point[0] - origin[0])
            b = a*mir[1] + origin[1]
            if (mir[2][0] <= b) and (b <= mir[2][1]):
                return True
            else:
                return False
        else:
            return False
    elif mir[0][1] == 'h':
        if mir[0][0] == 'u':
            if origin[1] > mir[1]:
                return False
        elif mir[0][0] == 'd':
            if origin[1] < mir[1]:
                return False

        if point[1] != origin[1]:
            a = (point[0] - origin[0])/(point[1] - origin[1])
            b = a*mir[1] + origin[0]
            if (mir[2][0] <= b) and (b <= mir[2][1]):
                return True
            else:
                return False
        else:
            return False

def isCurrRefl(origin, mir, point):
    checkmir = point[2]
    if checkmirtouch(mir, point, origin):
        for i in checkmir:
            if not checkmirtouch(i, point, origin):
                return False

        return True

    return False

def reflmirror(mir, mirto):
    newmir = ()
    if mir[0] == 'lv':
        if mirto[0][1] == 'h':
            if mirto[2][0] > mir[1]:
                newmir = (mirto[0], mirto[1], (2*mir[1] - mirto[2][0], 2*mir[1] - mirto[2][1]))
        elif mirto[0] == 'lv':
            if mirto[1] > mir[1]:
                newmir = ('rv', 2*mir[1] - mirto[1], (mirto[2][0], mirto[2][1]))
        elif mirto[0] == 'rv':
            if mirto[1] > mir[1]:
                newmir = ('lv', 2*mir[1] - mirto[1], (mirto[2][0], mirto[2][1]))
    elif mir[0] == 'rv':
        if mirto[0][1] == 'h':
            if mirto[2][1] < mir[1]:
                newmir = (mirto[0], mirto[1], (2*mir[1] - mirto[2][0], 2*mir[1] - mirto[2][1]))
        elif mirto[0] == 'lv':
            if mirto[1] < mir[1]:
                newmir = ('rv', 2*mir[1] - mirto[1], (mirto[2][0], mirto[2][1]))
        elif mirto[0] == 'rv':
            if mirto[1] < mir[1]:
                newmir = ('lv', 2*mir[1] - mirto[1], (mirto[2][0], mirto[2][1]))
    elif mir[0] == 'uh':
        if mirto[0][1] == 'v':
            if mirto[2][1] < mir[1]:
                newmir = (mirto[0], mirto[1], (2*mir[1] - mirto[2][0], 2*mir[1] - mirto[2][1]))
        elif mirto[0] == 'uh':
            if mirto[1] < mir[1]:
                newmir = ('dh', 2*mir[1] - mirto[1], (mirto[2][0], mirto[2][1]))
        elif mirto[0] == 'dh':
            if mirto[1] < mir[1]:
                newmir = ('up', 2*mir[1] - mirto[1], (mirto[2][0], mirto[2][1]))
    elif mir[0] == 'dh':
        if mirto[0][1] == 'v':
            if mirto[2][0] > mir[1]:
                newmir = (mirto[0], mirto[1], (2*mir[1] - mirto[2][0], 2*mir[1] - mirto[2][1]))
        elif mirto[0] == 'uh':
            if mirto[1] > mir[1]:
                newmir = ('dh', 2*mir[1] - mirto[1], (mirto[2][0], mirto[2][1]))
        elif mirto[0] == 'dh':
            if mirto[1] > mir[1]:
                newmir = ('uh', 2*mir[1] - mirto[1], (mirto[2][0], mirto[2][1]))

    return newmir

def distance(p1, p2):
    return sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def signi(p):
    if p >= 0:
        return 1
    return -1

def isvalid(point, points):
    if point[0] != 0:
        a = point[1]/point[0]
        #print a
        for i in xrange(1, int(abs(point[0]))):
            i = signi(point[0])*float(i)
            #print i
            pdot = (i, a*i)
            if pdot in points:
                return False
        return True
    else:
        for i in xrange(1, int(abs(point[1]))):
            pdot = (0, signi(point[1])*float(i))
            if pdot in points:
                return False
        return True

def main():
    origin = (0.5, 1.5)
    D = 8
    mirrors = [('lv', 0, (0, 2)), ('rv', 1, (0, 2)), ('dh', 0, (0, 1)), ('uh', 2, (0, 1))]
    points = [origin]
    allpoints = []
    finpoints = []
    respoints = []
    while len(points) > 0:
        newpoints = []
        for point in points:
            for mir in mirrors:
                if mir[0] == 'lv':
                    if (point[0] > mir[1]):
                        newpoint = ((2*mir[1] - point[0]), point[1])
                        if (distance(origin, newpoint)) < D and (not (newpoint in allpoints)):
                            newpoints.append(newpoint)
                            allpoints.append(newpoint)
                elif mir[0] == 'rv':
                    if (point[0] < mir[1]):
                        newpoint = ((2*mir[1] - point[0]), point[1])
                        if (distance(origin, newpoint) < D) and (not (newpoint in allpoints)):
                            newpoints.append(newpoint)
                            allpoints.append(newpoint)
                elif mir[0] == 'dh':
                    if (point[1] > mir[1]):
                        newpoint = (point[0], (2*mir[1] - point[1]))
                        if (distance(origin, newpoint) < D) and (not (newpoint in allpoints)):
                            newpoints.append(newpoint)
                            allpoints.append(newpoint)
                elif mir[0] == 'uh':
                    if (point[1] < mir[1]):
                        newpoint = (point[0], (2*mir[1] - point[1]))
                        if (distance(origin, newpoint) < D) and (not (newpoint in allpoints)):
                            newpoints.append(newpoint)
                            allpoints.append(newpoint)
        points = newpoints

    for i in allpoints:
        i = (i[0] - origin[0], i[1] - origin[1])
        finpoints.append(i)

    for i in finpoints:
        if isvalid(i, finpoints):
            respoints.append(i)

    respoints = list(set(respoints))
    print respoints, len(respoints)

    origin = [2.5, 2.5, []]
    D = 10
    mirrors = [('lv', 0, (0, 3)), ('rv', 4, (0, 3)), ('up', 3, (0, 4)), ('lv', 2, (1, 2)), ('rv', 1, (1, 2)), ('rv', 3, (0, 1)), ('dh', 2, (1, 2)), ('dh', 1, (3, 4)), ('dh', 0, (0, 3)), ('uh', 1, (1, 2))]
    points = [origin]
    allpoints = []
    finpoints = []
    respoints = []
    it = 0
    old = 0
    while len(points) > 0:
        newpoints = []
        for point in points:
            for mir in mirrors:
                tupl = reflpoint(mir, point, origin)
                newpoint = tupl[0]
                #print tupl, point, mir
                if (newpoint != []) and (distance(origin, newpoint) < D) and (not ((newpoint[0], newpoint[1]) in allpoints)) :
                    newpoints.append(newpoint)
                    if tupl[1]:
                        allpoints.append((newpoint[0], newpoint[1]))
        points = newpoints
        if (old == len(allpoints)):
            it += 1
        if (it == 2):
            break
        old = len(allpoints)
        print len(points), len(allpoints), it

    print "Here"
    for i in allpoints:
        i = (i[0] - origin[0], i[1] - origin[1])
        finpoints.append(i)

    for i in finpoints:
        if isvalid(i, finpoints):
            respoints.append(i)

    respoints = list(set(respoints))
    print respoints, len(respoints)


if __name__ == '__main__':
    main()
