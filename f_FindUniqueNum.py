# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 20:50:45 2018

@author: steve
"""
#Prompt:
#You are given an odd-length array of integers, in which all of them are the same, except for one single number.
#Complete the method which accepts such an array, and returns that single different number.
#The input array will always be valid! (odd-length >= 3)

#My Solution
#def stray(arr):
#    from collections import Counter
#    cnt_Array = Counter(arr)
#    for num, count in cnt_Array.items():
#        if count == 1:
#            unq_Value = num
#    return unq_Value

#Best Solution
def stray(arr):
    for x in arr:
        if arr.count(x) == 1:
            return x