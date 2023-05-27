# https://leetcode.com/problems/merge-two-sorted-lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
  def mergeTwoLists(self, l1, l2):
    head = ListNode(0)
    first = head
    while l1 and l2:
      if l1.val <= l2.val:
        first.next = l1
        first = first.next
        l1 = l1.next
      else:
        first.next = l2
        first = first.next
        l2 = l2.next
    if l1:
      first.next = l1
    if l2:
      first.next = l2
    return head.next