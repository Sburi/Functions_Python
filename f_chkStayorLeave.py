# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 12:20:54 2018

@author: 431165
"""

#Prompt: Given dict of happiness ratings of a room, determine if you should leave or not. You will also be given your
#bosses happiness rating which counts twice. Sum all then divide by two. If <5, return "Get Out Now!", else return "Nice Work Champ!"

#MyCode
#def outed(meet, boss):
#    return  "Get Out Now!" if (sum(meet.values()) + meet.get(boss))/len(meet.values())<=5 else "Nice Work Champ!"

#BestCode
def outed(meet, boss):
    return 'Get Out Now!' if (sum(meet.values()) + meet[boss] ) / len(meet) <= 5 else 'Nice Work Champ!'