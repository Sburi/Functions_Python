# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 22:12:34 2018

@author: steve
"""
#Prompt: Can you clean the crap from your garden? Not if the dog's around, program accordingly.
#MyCode
#def crap(garden, bags, cap):
#    from collections import Counter
#    clc_TotalCap = bags * cap
#    flt_Garden = [item for sublist in garden for item in sublist]
#    cnt_Garden = Counter(flt_Garden)
#    chk_DogPresent = cnt_Garden.get("D", 0) > 0
#    clc_Crap = cnt_Garden.get("@", 0)
#    
#    if chk_DogPresent == True:
#        return "Dog!!"
#    elif clc_TotalCap >= clc_Crap:
#        return "Clean"
#    else:
#        return "Cr@p"
    
#BetterCode
def crap(garden, bags, cap):
    # Flatten list including only cr@p and dogs
    flat = [e for line in garden for e in line if e in 'D@']
    return 'Dog!!' if 'D' in flat else 'Clean' if len(flat) <= bags * cap else 'Cr@p'