# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 10:16:31 2018

@author: 431165
"""
#Prompt: Given a list of positive and negative numbers, return back even numbers ascending + odd numbers sorted descending. Remove dupes
MyCode:
def men_from_boys(arr):
    lst_Even = list()
    lst_Odd = list()
    for n in set(arr):
        lst_Even.append(n) if n % 2 == 0 else lst_Odd.append(n)
            
    lst_Even.sort()
    lst_Odd.sort(reverse=True)
    lst_All = lst_Even + lst_Odd
    return lst_All
