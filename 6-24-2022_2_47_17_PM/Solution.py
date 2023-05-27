# https://leetcode.com/problems/reverse-linked-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
  def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    if not head:
      return head
    
    node = head
    prev = None
    temp = None
    
    while node.next:
      temp = node.next
      node.next = prev
      prev = node
      node = temp
    
    node.next = prev
    
    return node