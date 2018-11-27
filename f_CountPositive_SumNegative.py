# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 15:56:56 2018

@author: 431165
"""
#Prompt: Given integers, count positives, sum negatives
#MyCode
#def count_positives_sum_negatives(arr):
#    #Setup
#    print(arr)
#    
#    #Handle []
#    if arr == []:
#        return []
#    
#    #chk_Pos_Neg
#    PosNums = list()
#    NegNums = list()
#    for item in arr:
#        PosNums.append(item) if item > 0 else NegNums.append(item)
#        
#    #Wrap Up
#    FinArr = [len(PosNums), sum(NegNums)]
#    print(FinArr)
#    return FinArr

#BestCode
def count_positives_sum_negatives(arr):
    if not arr: return []
    pos = 0
    neg = 0
    for x in arr:
      if x > 0:
          pos += 1
      if x < 0:
          neg += x
    return [pos, neg]