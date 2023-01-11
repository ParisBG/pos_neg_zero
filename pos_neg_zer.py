#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 16:02:30 2022
@author: parisbg

Given an array of integers, calculate the ratios of its elements that are positive,
negative, and zero. Print the decimal value of each fraction on a new line with 
places after the decimal.
"""

 #How many elements are in array for ratio
#Traverse array
#Check each element for pos, neg, or zero
#tally up each
#take final tallys and divide each by length of array, respectively

#how to do 6 decimanl precision?
arr = [1,2,3,-2,0]
pos, neg, zer = 0,0,0

for i in arr:
    if i < 0:
        neg += 1
    if i == 0:
        zer += 1
    if i > 0:
        pos += 1
        
print("{:.6f}".format(pos/len(arr)))
print("{:.6f}".format(neg/len(arr)))
print("{:.6f}".format(zer/len(arr)))