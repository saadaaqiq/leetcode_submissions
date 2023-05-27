# https://leetcode.com/problems/remove-nth-node-from-end-of-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
  def removeNthFromEnd(self, first: Optional[ListNode], n: int) -> Optional[ListNode]:
    arr = []
    head = first
    while head:
      arr.append(head)
      head = head.next
    if len(arr) == n:
      return first.next
    elif n == 1:
      arr[len(arr)-2].next = None
    else:
      arr[len(arr)-n-1].next = arr[len(arr)-n+1]
    
    return first