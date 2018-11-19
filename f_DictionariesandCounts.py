# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 02:36:30 2018

@author: steve
"""

#Prompt: Make a way to determine, given an input string and suggested values, which values have the highest sum

##MyCode
#def alphabet_war(fight):
#    #code dictionary
#    dct_right = {'m':4, 'q':3, 'd':2, 'z':1}
#    dct_left = {'w':4, 'p':3, 'b':2, 's':1}
#    #calc right side
#    lst_right = map(dct_right.get, fight)
#    lst_right = [x for x in lst_right if x is not None]
#    clc_right = sum(lst_right)
#    print('[%s]' % ', '.join(map(str, lst_right)))
#    print(clc_right)
#    #calc left side
#    lst_left = map(dct_left.get, fight)
#    lst_left = [x for x in lst_left if x is not None]
#    print('[%s]' % ', '.join(map(str, lst_left)))
#    clc_left = sum(lst_left)
#    print(clc_left)
#    #Determine winner
#    if clc_right > clc_left:
#       return "Right side wins!"
#    elif clc_right < clc_left:
#       return "Left side wins!"
#    else:
#        return "Let's fight again!"
    
#BestCode
def alphabet_war(fight):
    d = {'w':4,'p':3,'b':2,'s':1,
         'm':-4,'q':-3,'d':-2,'z':-1}
    r = sum(d[c] for c in fight if c in d)
    
    return {r==0:"Let's fight again!",
            r>0:"Left side wins!",
            r<0:"Right side wins!"
            }[True]
