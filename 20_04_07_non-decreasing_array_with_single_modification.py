#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 11:37:50 2020

@author: nenad
"""


"""
Problem description: 
    
You are given an array of integers in an arbitrary order. Return whether or not it is possible to make the array non-decreasing by modifying at most 1 element to any value.

We define an array is non-decreasing if array[i] <= array[i + 1] holds for every i (1 <= i < n).


Example:

[13, 4, 7] should return true, since we can modify 13 to any value 4 or less, to make it non-decreasing.

[13, 4, 1] however, should return false, since there is no way to modify just one element to make the array non-decreasing.

Here is the function signature:

def check(lst):
  # Fill this in.

print check([13, 4, 7])
# True
print check([5,1,3,2,5])
# False

Can you find a solution in O(n) time?
Asked at Microsoft.
"""
# Time: O(n), space:O(1)
def check(lst) -> bool:
     # flag that tells if at most one element is modified
    modified = False
    prev = None
    for i in range(len(lst)-1):
        if lst[i] > lst[i+1]:
            # one element is already modified
            if modified:
                return False
            # otherwise - set flag as True - element is modified
            modified = True
            # check what to do - to set lst[i+1] = lst or lst[i] = lst[i+1]
            # based on lst[i-1]
            if prev and prev > lst[i+1]:
                lst[i+1] = lst[i]
            else:
                lst[i] = lst[i+1]
        prev = lst[i]
            
    return True

# Test 1
print(check([13,4,7]))

# Test 1
print(check([5,1,3,2,5]))

# Additional check
[4,2,3]
[4,2,1]
[3,4,2,3]