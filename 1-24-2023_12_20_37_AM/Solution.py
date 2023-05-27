# https://leetcode.com/problems/merge-two-sorted-lists

class Solution:
  def mergeTwoLists(self, a, b):
    if not a:
      return b
    if not b:
      return a
    h = ListNode(0)
    curr = h 
    while a and b:
      if a.val <= b.val:
        curr.next = a
        a = a.next
      else:
        curr.next = b
        b = b.next
      curr = curr.next
    if b:
      curr.next = b
    if a:
      curr.next = a
    return h.next