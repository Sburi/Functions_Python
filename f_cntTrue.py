# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 20:28:44 2018

@author: 431165
"""
lst = list[True, True, True, False]
def cnt_True(lst):
    from collections import Counter
    print(lst)
    cnt = Counter(lst)
    print(cnt)
    cntTrue == cnt.get(True)
    print(cntTrue)
    return cntTrue