# https://leetcode.com/problems/reorder-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
  def reorderList(self, head: Optional[ListNode]) -> None:
    q = deque()
    q.append(head)
    node = head
    node = node.next
    while node:
      q.append(node)
      node = node.next
    
    node = q.popleft()
    i = 0
    while q:
      if i % 2 != 0:
        node.next = q.popleft()
      else:
        node.next = q.pop()
      node = node.next
      if not q:
        node.next = None
      i += 1
    
    