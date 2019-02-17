#!/bin/python3
import sys


def subSum(arr):
    meh = 0
    msf = 0
    ePoz = False

    for i in range(len(arr)):
        if (arr[i] >= 0):
            ePoz = True
        meh += arr[i]
        if (meh < 0):
            meh = 0
        msf = max(msf, meh)
    if (not ePoz):
        msf = max(arr)
    return msf


def subSumNonCont(arr):
    macs = 0
    ePoz = False
    for i in arr:
        if (i >= 0):
            macs += i
            ePoz = True
    if (not ePoz):
        macs = max(arr)
    return macs


def subsumcont(st, fn, arr):
    if (st > fn):
        return max(arr)
    else:
        cMax = max(sum(arr[st:fn + 1]), sum(arr[st + 1:fn + 1]), sum(arr[st:fn]))

        rmL = sum(arr[st:fn])
        rmF = sum(arr[st + 1:fn + 1])
        noM = sum(arr[st:fn + 1])
        # print(str(noM)+ "-"+ str(rmL) + "-" + str(rmF))
        if (cMax != noM or noM == rmL or noM == rmF):
            if (rmL > rmF):
                return subsumcont(st, fn - 1, arr)
            else:
                return subsumcont(st + 1, fn, arr)
        else:
            return cMax


t = int(input().strip())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    # print(arr)
    # arrSum = subsum(arr,False) if (subsum(arr,False) != None) else max(arr)
    arrSumCont = subSum(arr)  # subsumCont(0,len(arr)-1,arr)
    arrSumNonCont = subSumNonCont(arr)

    print(str(arrSumCont) + " " + str(arrSumNonCont))
