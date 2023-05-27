# https://leetcode.com/problems/middle-of-the-linked-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
  def middleNode(self, head):
    if not head or not head.next:
      return head
    slow, fast = head, head
    while fast and fast.next:
      slow = slow.next
      fast = fast.next.next
    return slow