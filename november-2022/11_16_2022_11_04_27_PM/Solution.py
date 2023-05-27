# https://leetcode.com/problems/partition-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
  def partition(self, head, x):
    first = ListNode(-101)
    first.next = head
    pos = first
    while pos and pos.next and pos.next.val < x:
      pos = pos.next
    prev = pos
    curr = pos.next
    while curr:
      if curr.val < x:
        prev.next = curr.next
        curr.next = pos.next
        pos.next = curr
        pos = pos.next
        curr = prev.next
      else:
        prev = prev.next
        curr = curr.next
    return first.next
      