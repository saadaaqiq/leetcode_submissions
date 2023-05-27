# https://leetcode.com/problems/palindrome-linked-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
  def isPalindrome(self, head: Optional[ListNode]) -> bool:
    stack = []
    curr = head
    size = 0
    while curr:
      curr = curr.next
      size += 1
    curr = head
    i = 0
    while i < size//2:
      stack.append(curr)
      curr = curr.next
      i += 1
    if size%2 == 1:
      curr = curr.next
    while curr:
      if curr.val != stack.pop().val:
        return False
      curr = curr.next
    return True