# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 20:10:38 2018

@author: steve
"""

#v1
#def is_Unique(string):
#    from collections import Counter
#    arr = list(string)
#    Count = Counter(arr)
#    #print(Count.values())
#    #print(all(value < 2 for value in Count.values()))
#    return all(value < 2 for value in Count.values())
#    
#is_Unique("tes")

#v2
def chk_Unique(inp):
    from collections import Counter
    inp = str(inp)
    arr = list(inp)
    Count = Counter(arr)
    print(Count.values())
    print(all(value < 2 for value in Count.values()))
    return all(value < 2 for value in Count.values())
    
is_Unique(123)