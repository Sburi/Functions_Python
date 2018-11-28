# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 10:38:49 2018

@author: 431165
"""
#Prompt: Given a number (e.g. 61534), find out if the number is "colorful" in that the products of all numbers (if more than 2) and
#the product of each number with the next number do not produce any matching results.
#For ex: Given 132, 1*3 = 3, 3*2 = 6. 1,3,2,3,6 contains 2 threes so it's not colorful == false

#MyCode
#def colorful(number):
#    
#    #Convert to list of numbers
#    lst_n = list(map(int, list(str(number))))
#    
#    #If there is only 1 number, it's colorful, return true
#    if len(lst_n)<2:
#        return True
#    
#    #Multiply each number by the next number
#    x = 0
#    lst_products = list()
#    for n in range(len(lst_n)-1):
#        lst_products.append(lst_n[x]*lst_n[x+1])
#        x = x + 1
#    
#    #If more than 2 numbers, multiply all numbers together
#    if len(lst_n) > 2:
#        product = 1
#        for n in lst_n:
#            product *= n
#        lst_products.append(product)
#    
#    #Add the original numbers to the product list and return result
#    lst_products = lst_products + lst_n
#    result = True if len(lst_products) == len(set(lst_products)) else False
#    return result

#BestCode
def colorful(number):
    base_result = []
    for x in str(number):
        base_result.append(int(x))
    for y in range(len(base_result) - 1):
        temp = base_result[y] * base_result[y + 1]
        base_result.append(temp)
    # Should you really eval the last value ? :shrug: If so, would use eval
    return len(set(base_result)) == len(base_result)