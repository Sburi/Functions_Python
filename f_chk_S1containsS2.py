# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 23:31:04 2018

@author: steve
"""

#Purpose: 
#MyCode
def chk_s1containsS2(s1, s2):
    from collections import Counter
    return not Counter(s2)-Counter(s1)