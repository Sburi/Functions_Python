# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 19:53:15 2018

@author: 431165
"""
###Prompt: Create a function that will take a text string and multiply each letter by its position in the string.
###My Solution
##def accum(string):
##    splt_string = list(string)
##    i = 0
##    maxnumber = len(splt_string)
##    newstring = ""
##    for char in splt_string:
##        newstring = newstring + char.upper() + char.lower() * i
##        if i < maxnumber - 1:
##            newstring = newstring + "-"
##        i = i + 1
##    print(newstring)
##
##accum("test")

#BetterSolution
def accum(s):
    return '-'.join(c.upper() + c.lower() * i for i, c in enumerate(s))

print(accum("check"))
