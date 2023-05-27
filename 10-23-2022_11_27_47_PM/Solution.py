# https://leetcode.com/problems/intersection-of-two-linked-lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
  def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
    l1, l2, p, q = 0, 0, headA, headB
    while p: p, l1 = p.next, l1+1
    while q: q, l2 = q.next, l2+1
    p, q = headA, headB
    while l1 > l2: p, l1 = p.next, l1-1
    while l2 > l1: q, l2 = q.next, l2-1
    while p and q:
      if p == q: return p
      p, q = p.next, q.next
    return None