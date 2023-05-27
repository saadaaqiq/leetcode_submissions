# https://leetcode.com/problems/merge-two-sorted-lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
  def mergeTwoLists(self, a, b):
    if not a: return b
    if not b: return a
    if a.val <= b.val:
      a.next = self.mergeTwoLists(a.next, b)
      return a
    else:
      b.next = self.mergeTwoLists(a, b.next)
      return b
