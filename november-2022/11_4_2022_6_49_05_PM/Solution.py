# https://leetcode.com/problems/middle-of-the-linked-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
  def middleNode(self, head):
    n = 1
    mid = head
    i = 0
    while head:
      while i < n//2:
        mid = mid.next
        i += 1
      head = head.next
      n += 1
    return mid