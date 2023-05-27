# https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
  def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
    if not head:
      return None
    first = head
    size = 0
    while first:
      size += 1
      first = first.next
    first = head
    k = 0
    while k < size//2 - 1:
      first = first.next
      k += 1
    if first.next:
      first.next = first.next.next
    else:
      return None
    return head