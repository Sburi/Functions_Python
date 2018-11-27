# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#Prompt: Find outlier parity, for ex given 1,3,5,2 find 2. Given 2,4,6,3 find 3.
#MyCode
#def find_outlier(integers):
#    #Setup
#    from collections import Counter
#    
#    #chkLoop, Build Even/Ddd lists
#    EvenNums = list()
#    OddNums = list()
#    for item in integers:
#        if item % 2 == 0:
#            EvenNums.append(item)
#        else:
#            OddNums.append(item)
#           
#    #FindParity
#    parityOutlier = OddNums if len(EvenNums)>1 else EvenNums
#    print(parityOutlier)
#    return parityOutlier[0]

#BetterCode
def find_outlier(int):
    odds= [x for x in int if x%2!=0]
    evens= [x for x in int if x%2==0]
    return odds[0] if len(odds)<len(evens) else evens[0]
    