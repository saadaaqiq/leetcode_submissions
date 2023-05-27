# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
  def deleteDuplicates(self, node: Optional[ListNode]) -> Optional[ListNode]:
    if node and node.next and node.val != node.next.val:
      node.next = self.deleteDuplicates(node.next)
    elif node and node.next:
      while node.next and node.next.val == node.val:
        node = node.next
      node = self.deleteDuplicates(node.next)
    return node
