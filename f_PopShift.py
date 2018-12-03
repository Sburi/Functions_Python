# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 22:08:10 2018

@author: 431165
"""

#Prompt: Given a str, remove the last letter, add to str2. Remove the first letter, add to str1. Repeat until str ==1. Return str2, str1, str.
#MyCode
def pop_shift(str):
    ostr = list(str)
    str1 = ""
    str2 = ""
    while len(ostr)>1:
        max = len(ostr)-1
        str1 = str1 + ostr[max]
        ostr.pop(max)
        if max > 2:
            str2 = str2 + ostr[0]
            ostr.pop(0)
    return [str1, str2, ostr[0]]
        