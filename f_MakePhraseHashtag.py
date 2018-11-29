# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 22:56:26 2018

@author: steve
"""

#Prompt: Given string, title case words, remove spaces, prepend #. If >140 or "", return False
#MyCode
#def generate_hashtag(s):
#    if s == "" or len(s)>140: return False
#    s = s.title()
#    return "#" + ''.join([x for x in s if x!=" "])

#BestCode
def generate_hashtag(s): return '#' +s.strip().title().replace(' ','') if 0<len(s)<=140 else False