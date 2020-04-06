#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 14:11:49 2020

@author: nenad
"""


"""
Problem description:
You are given a list of numbers, and a target number k. Return whether or not there are two numbers in the list that add up to k.

Example:
Given [4, 7, 1 , -3, 2] and k = 5,
return true since 4 + 1 = 5.

def two_sum(list, k):
  # Fill this in.

print two_sum([4,7,1,-3,2], 5)
# True

Try to do it in a single pass of the list.

"""
# Time: O(n)
# Space: O(1)
def two_sum(nums, k):
    # nlogn
    nums.sort()
    i, j = 0, len(nums)-1
    # until the indices meet
    while i < j:
        sum = nums[i] + nums[j]
        # sum found - return True
        if sum == k:
            return True
        # increase sum -> i + 1 (use bigger element)
        if sum < k:
            i += 1
        # decrease sum -> j-1 (use smaller element)
        else:
            j -= 1
    # otherwise
    return False

# Time/space: O(n)
def two_sum(nums, k):
    els = set(nums)
    # for each element, check that its complement is in an array
    for val in nums:
        if k-val in nums:
            return True
    # there is no such pair that sum up to k
    return False


            
    

print (two_sum([4,7,1,-3,2], 5))
# True

print (two_sum([3,2,4], 6))
# True

print (two_sum([3,2,4], 1))
# True



