# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 23:17:50 2018

@author: steve
"""

#def to_weird_case(s):
#    arr_Words = s.split(" ")
#    ret = ""
#    arr_Proper = ""
#    for word in arr_Words:
#        arr_Proper += word.title() + " "
#    cnct_String = " ".join(arr_Words)
#    print(arr_Proper)
#    return s

#My Code
#def to_weird_case(s):
#    arr_Words = s.split(" ")
#    ret = ""
#    arr_Proper = ""
#    list_alteredLetters = ""
#    for word in arr_Words:
#        list_Letters = list(word)
#        i = True
#        for letter in list_Letters:
#            if i:
#                list_alteredLetters += letter.upper()
#            else:
#                list_alteredLetters += letter.lower()
#            i = not i 
#        list_alteredLetters = list_alteredLetters + " "
#    list_alteredLetters = list_alteredLetters.strip()
#    return list_alteredLetters


#Best Code
def to_weird_case_word(string):
    return "".join(c.upper() if i%2 == 0 else c for i, c in enumerate(string.lower()))
    
def to_weird_case(string):
    return " ".join(to_weird_case_word(str) for str in string.split())
to_weird_case("This is a test")