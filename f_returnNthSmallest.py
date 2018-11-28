# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 19:56:24 2018

@author: 431165
"""
#Prompt: Given an array, return the nth smallest position. For Ex (1,3,6), 2, return 2)
##MyCode
#def nth_smallest(arr, pos):
#    arr.sort()
#    nthSmallest = arr[pos-1]
#    return nthSmallest

#BestCode
def nth_smallest(arr, pos):
    return sorted(arr)[pos-1] # Gotta love Python