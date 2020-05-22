#!/bin/python

import math
import os
import random
import re
import sys


def mergeSort(alist):
    inversion_count = 0

    n = len(alist)
    if n == 1:
        return 0

    mid = len(alist) // 2
    lefthalf = alist[:mid]
    righthalf = alist[mid:]

    inversion_count += mergeSort(lefthalf)
    inversion_count += mergeSort(righthalf)

    i = 0
    j = 0
    k = 0
    while i < len(lefthalf) and j < len(righthalf):
        if lefthalf[i] <= righthalf[j]:
            alist[k] = lefthalf[i]
            i = i + 1
        else:
            alist[k] = righthalf[j]
            j = j + 1
            inversion_count += len(lefthalf) - i
        k = k + 1

    while i < len(lefthalf):
        alist[k] = lefthalf[i]
        i = i + 1
        k = k + 1

    while j < len(righthalf):
        alist[k] = righthalf[j]
        j = j + 1
        k = k + 1

    return inversion_count


if __name__ == '__main__':

    t = int(raw_input())

    for t_itr in xrange(t):
        n = int(raw_input())

        arr = map(int, raw_input().rstrip().split())

        result = mergeSort(arr)

        print result
