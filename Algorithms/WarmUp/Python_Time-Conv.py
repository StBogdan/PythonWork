#!/bin/python3

import sys


time = input().strip()
dayPart = time[len(time)-2:]
timeArr = time[:len(time)-2].split(":")


if(dayPart == "PM"):
    if(timeArr[0] != "12"):
        timeArr[0]=str(int(timeArr[0])+12)
elif(timeArr[0] == "12"):
    timeArr[0] = "00"
print(":".join(timeArr))

