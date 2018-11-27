# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 17:23:28 2018

@author: 431165
"""
#Prompt: Given a number, write that number in expanded form. For Ex: 4032 = '4000 + 30 + 2'
#MyCode:
def expanded_form(num):
    #Setup
    lst_numbers = list(str(num))
    
    #Loop and alter
    lst_numbers2 = list()
    numlen = len(lst_numbers) - 1
    for num in lst_numbers:
        if num != "0":
            num = num + "0"*numlen
            lst_numbers2.append(num)
            numlen = numlen - 1
        else:
            numlen = numlen - 1
            
    #Format
    str_ExpandedForm = " + ".join(lst_numbers2)
    print(str_ExpandedForm)
    
    return str_ExpandedForm
