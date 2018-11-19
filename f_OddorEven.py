# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 03:02:11 2018

@author: steve
"""
#Prompt: Check if number is odd or even
##MyCode
#def even_or_odd(number):
#    number = (number/2)
#    if number == int(number) : #if number = rounded number it must be Even, else odd.
#        return "Even"
#    else:
#        return "Odd"
    
##MyCode Optimized
#def even_or_odd(number):
#    return "Even" if number/2 == int(number/2) else "Odd"

#BestCode
def even_or_odd(number):
  return 'Odd' if number % 2 else 'Even'