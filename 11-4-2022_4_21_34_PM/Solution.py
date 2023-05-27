# https://leetcode.com/problems/reverse-linked-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
  def reverseList(self, head):
    if not head:
      return None
    prev = None
    curr = head
    while curr:
      temp = curr.next
      curr.next = prev
      prev = curr
      curr = temp
    return prev
