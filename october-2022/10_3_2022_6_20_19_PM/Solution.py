# https://leetcode.com/problems/remove-nth-node-from-end-of-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
  def removeNthFromEnd(self, head, n):
    p = head
    i = 0
    while p and i <= n:
      i += 1
      p = p.next
    if n+1 > i:
      return head.next
    else:
      q = head
      while p:
        p = p.next
        q = q.next
      if q.next:
        q.next = q.next.next if q.next.next else None
    return head