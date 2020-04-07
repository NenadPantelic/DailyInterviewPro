#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 11:03:11 2020

@author: nenad
"""


"""
Problem description:
Given a list of numbers, where every number shows up twice except for one number, find that one number.

Example:
Input: [4, 3, 2, 4, 1, 3, 2]
Output: 1
Here's the function signature:

def singleNumber(nums):
  # Fill this in.

print singleNumber([4, 3, 2, 4, 1, 3, 2])
# 1

Challenge: Find a way to do this using O(1) memory.    

"""
# Time: O(n)
# Space: O(1)
def singleNumber(nums):
    res = 0
    for val in nums:
        res = res ^ val
    return res

print(singleNumber([4, 3, 2, 4, 1, 3, 2]))