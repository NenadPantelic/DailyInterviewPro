#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 20:08:10 2020

@author: nenad
"""


"""
Given a string, find the length of the longest substring without repeating characters.

"""
class Solution:
  def lengthOfLongestSubstring(self, s):
      # length of longest substring
      maxLen = 0
      i = 0
      n = len(s)
      # start index of stream
      startIndex = 0
      # positions positions in string
      positions = {}
      while i < n:
          # check if char is already seen
          position = positions.get(s[i], None)
          # if not present - just go further
          if position is not None:
              # occurence of the current character is from this window
              if position >= startIndex:
                  # stream length is difference between current position(i) and starting position of that stream (window)
                  maxLen = max(maxLen, i - startIndex)
                  # start from the position+1 where we previously find this char
                  startIndex = position+1
    
          # update char position - insert new one, or update the existing one
          positions[s[i]] = i
          i += 1
      # if string ending makes non-repeating stream
      maxLen = max(maxLen, i - startIndex)   
      return maxLen

sol = Solution()           
print(sol.lengthOfLongestSubstring('abrkaabcdefghijjxxx'))
print(sol.lengthOfLongestSubstring('xxxabc'))
print(sol.lengthOfLongestSubstring("abcabcbb"))
print(sol.lengthOfLongestSubstring("dvdf"))

# 10