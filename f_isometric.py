# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#My Code
#def is_isometric(string):
#    from collections import Counter
#    if string == "":
#        return True
#    else:
#        dct_String = Counter(list(string.lower())).values()
#        print(dct_String)
##        print(Counter(list(string.lower())).items())
#        print(all(value < 2 for value in dct_String))
#        return all(value < 2 for value in dct_String)
#    
#is_isometric("yzikvwn")

#Best Code
def is_isogram(string):
    print(set(string))
    return len(string) == len(set(string.lower()))
#This works because set returns a list of unique elements. When compared to the original string length, the set's length will be shorter if it contains duplications

print(is_isogram("Test"))