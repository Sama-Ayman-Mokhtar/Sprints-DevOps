#!/usr/bin/env python

def MyFunc(nums):
    foundFloat = False
    foundInt = False
    sumEvenInts = 0
    countEventInts = 0
    maxFloat = "invalid"
    for i in nums:
        if(isinstance(i,int)):
            foundInt = True
            if(i%2==0):
                sumEvenInts += i
                countEventInts += 1
        if(isinstance(i,float)):
            if(not foundFloat):
                foundFloat = True
                maxFloat = i
            else:
               if( i > maxFloat):
                   maxFloat = i
    if(foundInt or foundFloat):
        return sumEvenInts/countEventInts, maxFloat
    return 0,0


