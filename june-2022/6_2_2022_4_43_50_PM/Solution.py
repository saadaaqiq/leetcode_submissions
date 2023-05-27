# https://leetcode.com/problems/add-two-numbers

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
  def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    carry = 0
    f1 = l1
    f2 = l2
    old = l1
    first = True
    while l1 or l2:
      v1 = l1.val if l1 else 0
      v2 = l2.val if l2 else 0
      newVal = v1 + v2 + carry
      if newVal <= 9: 
        if l1: 
          l1.val = newVal
        if l2:
          l2.val = newVal
        carry = 0
      else:
        if l1:
          l1.val = newVal % 10
        if l2:
          l2.val = newVal % 10
        carry = newVal // 10
      if l1:
        if l2 and l2.next and not l1.next:
          first = False
        if first:
          old = l1
        l1 = l1.next
      if l2:
        if not first:
          old = l2
        l2 = l2.next
      
    if carry > 0:
      old.next = ListNode(carry)
      
    if first:
      return f1
    else:
      return f2
    
    return f1
