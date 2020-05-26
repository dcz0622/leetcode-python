"""
PROBLEM DESCRIPTION

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order
and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Definition for singly-linked list:
  
  class ListNode:
    def __init__(self, val=0, next=None):
      self.val = val
      self.next = next


EXAMPLE

- Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
- Output: 7 -> 0 -> 8
- Explanation: 342 + 465 = 807
"""


class Solution:
  
  def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    l1Iter = l1
    l2Iter = l2
    carry = 0
    
    l3 = ListNode(None) # 1st element is dummy.
    l3Iter = l3
    
    while l1Iter is not None or l2Iter is not None:
      x = l1Iter.val if l1Iter is not None else 0
      y = l2Iter.val if l2Iter is not None else 0
      sum = x + y + carry # Carry from previous loop iteration
      carry = sum // 10 # Update carry for next loop iteration.
      
      l3Iter.next = ListNode(sum % 10)
      l3Iter = l3Iter.next
      
      # Update variables to prepare for next loop iteration.
      l1Iter = l1Iter.next if l1Iter is not None else None
      l2Iter = l2Iter.next if l2Iter is not None else None
    
    if carry != 0:
      l3Iter.next = ListNode(carry)
    
    return l3.next
