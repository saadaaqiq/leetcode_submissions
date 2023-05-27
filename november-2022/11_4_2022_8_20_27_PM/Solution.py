# https://leetcode.com/problems/linked-list-cycle-ii

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
  def detectCycle(self, head):
    slow, fast, node = head, head, None
    while fast and fast.next: 
      slow, fast = slow.next, fast.next.next
      if slow == fast:
        node = slow
        break
    if not node: return None
    slow = head
    while True:
      if slow == fast: return slow
      slow, fast = slow.next, fast.next
        
    
    