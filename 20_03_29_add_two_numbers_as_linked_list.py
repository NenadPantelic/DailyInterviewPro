#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 17:56:16 2020

@author: nenad
"""
"""

You are given two linked-lists representing two non-negative integers. 
The digits are stored in reverse order and each of their nodes contain a single digit. 
Add the two numbers and return it as a linked list.

Example:
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""

# Definition for singly-linked list.
class ListNode(object):
  def __init__(self, x):
    self.val = x
    self.next = None

class Solution:
  def addTwoNumbers(self, l1, l2, c = 0):
    newHead = None
    n1 = l1
    n2 = l2
    carry = 0
    prevNode = None
    while n1 or n2:
        # accumulate sum of current nodes from both lists plus carried value from
        # previous summation
        # there is case when one list is longer than other one
        val1 = val2 = 0
        if n1:
            val1 = n1.val
            n1 = n1.next
        if n2:
            val2 = n2.val
            n2 = n2.next
        val = val1 + val2 + carry
        # value and carry
        carry = val // 10
        val %= 10
        # create new node
        node = ListNode(val)
        # connect new node
        if prevNode:
            prevNode.next = node
            prevNode = node
        else:
            prevNode = node
            newHead = prevNode
   
    if carry:
        prevNode.next = ListNode(carry)
    
    return newHead


def printList(node):
    while node:
        print (node.val)
        node = node.next

s = Solution()
# Test 1
l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)
result = s.addTwoNumbers(l1, l2)    
# 7 0 8
printList(result)  
print()

# Test 2
l3 = ListNode(2)
l3.next = ListNode(4)
l3.next.next = ListNode(3)
l3.next.next.next = ListNode(9)

l4 = ListNode(8)
l4.next = ListNode(6)
l4.next.next = ListNode(4)
l4.next.next.next = ListNode(4) 
result = s.addTwoNumbers(l3, l4)    
# 9342
# 4468
# 13810
printList(result)   
print()


l5 = ListNode(2)
l5.next = ListNode(4)
l5.next.next = ListNode(5)
l5.next.next.next = ListNode(7)

l6 = ListNode(8)
l6.next = ListNode(3)

result = s.addTwoNumbers(l5, l6)    
# 7542
# 0038
# 7580
printList(result)