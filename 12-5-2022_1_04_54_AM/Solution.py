# https://leetcode.com/problems/middle-of-the-linked-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
  def middleNode(self, head):
    n = 0
    curr = head
    while curr:
      n += 1
      curr = curr.next
    c = n//2 if n%2!=0 else (n+1)//2
    k = 0
    curr = head
    while k < c:
      curr = curr.next
      k += 1
    return curr
