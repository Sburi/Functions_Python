# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 10:51:00 2018

@author: steve
"""

#Prompt: Build a Tower that given n floors returns that many floors in a list with floors incrememnting by +1
#MyCode
def tower_builder(n_floors, i_madeof):
    n = 1
    a = 1
    lst_Pyramid = list()
    chk_TotalSpaceNeeded = n_floors + (n_floors-1)
    while n <= n_floors:
        chk_SpacesNeeded = "_" * int((chk_TotalSpaceNeeded - a)/2)
        chk_AsterisksNeeded = i_madeof * (a)
        cnct_StringtoInput = chk_SpacesNeeded + chk_AsterisksNeeded + chk_SpacesNeeded
        lst_Pyramid.append(cnct_StringtoInput)
        a = a + 2
        n = n + 1
    
    lst_Pyramid2 = list()
    lst_Pyramid2 = [w.replace ("_", " ") for w in lst_Pyramid]
    return(lst_Pyramid2)
        
#BestCode
#def tower_builder(n):
#    return [("*" * (i*2-1)).center(n*2-1) for i in range(1, n+1)]
#        
#tower_builder(5)
        
def PrintList(usrList):
    for items in list(usrList):
        print(items)

def PrintListSlow(usrList):
    import time
    for items in list(usrList):
        print(items)
        time.sleep(.1)
        
        
#UserInteraction
TowerCount = input("How many levels would you like your christmas tree to have?")
i_madeof = input("What character would you like the tower to be made of?")
PrintListSlow(tower_builder(int(TowerCount), str(i_madeof)))
k = input("Press close to exit.")
