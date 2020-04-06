#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 21:37:10 2020

@author: nenad
"""
"""

Given a sorted array, A, with possibly duplicated elements, find the indices of the first and last occurrences of a target element, x. Return -1 if the target is not found.

Example:
Input: A = [1,3,3,5,7,8,9,9,9,15], target = 9
Output: [6,8]

Input: A = [100, 150, 150, 153], target = 150
Output: [1,2]

Input: A = [1,2,3,4,5,6,10], target = 9
Output: [-1, -1]
Here is a function signature example:

class Solution: 
  def searchRange(self, arr, target):
    # Fill this in.
  
# Test program 
arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8] 
x = 2
print(Solution().searchRange(arr, x))
# [1, 4]
"""

class Solution: 
  
  def binarySearch(self, arr, low, high, el):
      if low > high:
          return -1
      mid = low + (high-low//2)
      if arr[mid] == el:
          return mid
      elif arr[mid] > el:
          return self.binarySearch(arr, low, mid-1, el)
      else:
          return self.binarySearch(arr, mid+1, high, el)
      
  def searchRange(self, arr, target):
    
      n = len(arr)
      ind = self.binarySearch(arr, 0, n-1, target)
      if ind == -1:
          return [ind, ind]
      else:
          # search for right index
          for j in range(ind, n):
              if arr[j] != target:
                  break
              rightIndex = j
          # search for left index
          for j in range(ind, -1, -1):
              if arr[j] != target:
                  break
              leftIndex = j
          return [leftIndex, rightIndex]
      
      
sol = Solution()
        
# Test 1
arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8] 
x = 2
print(sol.searchRange(arr, x))
# [1, 4]
          
# Test 2
arr = [5,7,7,8,8,10]
target = 8
print(sol.searchRange(arr, target))

# Test 3
arr = [5,7,7,8,8,10]
target = 6
print(sol.searchRange(arr, target))

# Test 4
arr = [1]
target = 1
print(sol.searchRange(arr, target))

# Test 4
arr = [2,2, 3]
target = 2
print(sol.searchRange(arr, target))


          
        
          
            
                  
      