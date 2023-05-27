# https://leetcode.com/problems/palindrome-linked-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
  def isPalindrome(self, head: Optional[ListNode]) -> bool:
    size = 0
    curr = head
    while curr:
      curr = curr.next
      size += 1
    if size == 1:
      return True
    i = 0
    curr = head
    nxt = head.next
    while i < size//2-1:
      t1 = curr
      t2 = nxt
      curr = nxt
      nxt = nxt.next
      t2.next = t1
      i += 1
    if size%2 == 1:
      nxt = nxt.next
    while curr and nxt:
      if curr.val != nxt.val:
        return False
      curr = curr.next
      nxt = nxt.next
    return True