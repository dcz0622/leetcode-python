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
    l1Iterator = l1
    l2Iterator = l2
    carry = 0
    
    l3 = ListNode(None) # 1st element is dummy.
    l3Iterator = l3
    
    while l1Iterator is not None or l2Iterator is not None:
      x = l1Iterator.val if l1Iterator is not None else 0
      y = l2Iterator.val if l2Iterator is not None else 0
      sum = x + y + carry # Carry from previous loop iteration
      carry = sum // 10 # Update carry for next loop iteration.
      
      l3Iterator.next = ListNode(sum % 10)
      l3Iterator = l3Iterator.next
      
      # Update variables to prepare for next loop iteration.
      l1Iterator = l1Iterator.next if l1Iterator is not None else None
      l2Iterator = l2Iterator.next if l2Iterator is not None else None
    
    if carry != 0:
      l3Iterator.next = ListNode(carry)
    
    return l3.next
