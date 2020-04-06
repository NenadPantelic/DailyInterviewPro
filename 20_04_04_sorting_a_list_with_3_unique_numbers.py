#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 13:40:40 2020

@author: nenad
"""


"""
Problem description: 
    Given a list of numbers with only 3 unique numbers (1, 2, 3), sort the list in O(n) time.

Example 1:
Input: [3, 3, 2, 1, 3, 2, 1]
Output: [1, 1, 2, 2, 3, 3, 3]
Challenge: Try sorting the list using constant space.


"""
# Universal solution for any three numbers
from collections import Counter
def sortNums(nums):
    counter = Counter()
    # count occurences of elements - O(n)
    for val in nums:
        counter[val] += 1
    # sort values present in array
    values = sorted(counter.keys())
    offset = 0
    # O(n) - based on freqs update value of every element
    for val in values:
        i = 0
        # set counter[val] values of elements with value val
        while i < counter[val]:
            # new positions
            nums[i+offset] = val
            i += 1
        offset += counter[val]
    return nums
    

print (sortNums([3, 3, 2, 1, 3, 2, 1]))
# [1, 1, 2, 2, 3, 3, 3]