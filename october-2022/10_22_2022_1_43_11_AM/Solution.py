# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
  def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
    
    def meth(node):
      if not node or not node.next:
        return node
      if node.val != node.next.val:
        node.next = meth(node.next)
        return node
      while node.next and node.next.val == node.val:
        node = node.next
      node = node.next
      return meth(node)
    
    return meth(head)