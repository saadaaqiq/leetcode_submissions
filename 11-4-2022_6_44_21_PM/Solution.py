# https://leetcode.com/problems/middle-of-the-linked-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
  def middleNode(self, head):
    size = 0
    first = head
    while first:
      size += 1
      first = first.next
    first = head
    for i in range(size//2):
      first = first.next
    return first