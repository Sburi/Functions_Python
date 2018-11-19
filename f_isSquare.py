# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 15:24:15 2018

@author: steve
"""

#My solution below, works in 651ms
#def isSquare(number):    
#    import math
#    if number < 0:
#        print(str(number) + " is not an integer.")
#        return False
#    elif float(math.sqrt(number)).is_integer():
#        print (str(number) + " is an integer.")
#        return True
#    else:
#        print(str(number) + " is not an integer.")
#        return False
#
#isSquare(-1)
        
#Best solution below
import math
def is_square(n):    
    if n < 0:
        return False
    sqrt = math.sqrt(n)
    return sqrt.is_integer()
print(is_square(4))

    