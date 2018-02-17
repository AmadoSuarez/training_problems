#!/bin/python3
#https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem
import sys
from collections import Counter

def isValid(s):
    # Complete this function
    unique_chars = set(s)
    char_freq = Counter(s)
        
    freq = list(char_freq.values())
    freq_set = set(freq)
    freq_min = min(freq)
    freq_max = max(freq)
  

    #print(unique_chars)
    #print(char_freq)
    #print(freq)
   
    
    if freq_min == freq_max :
        return "YES"
    elif (freq_max - 1) == (freq_min) and freq.count(freq_max) == 1 and len(freq_set) <= 2:
        return "YES"
    
    elif len(freq_set) == 2 and min(freq_set) == 1:
        freq.remove(1)
        if len(set(freq)) == 1:
            return "YES"
        else:
            return "NO"
    else:
         return "NO"
        
        
s = input().strip()
result = isValid(s)
print(result)
