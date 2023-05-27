# https://leetcode.com/problems/rotate-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
  def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
    if not head: 
      return None
    size = 0
    p = head
    while p:
      p = p.next
      size += 1
    rotations = k % size
    if rotations == 0:
      return head
    p = head
    for i in range(size-rotations-1):
      p = p.next
    q = p.next
    newhead = q
    p.next = None
    while q and q.next:
      q = q.next
    if q:
      q.next = head
    return newhead