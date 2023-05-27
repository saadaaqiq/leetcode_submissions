# https://leetcode.com/problems/odd-even-linked-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
  def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    if not head or not head.next or not head.next.next: return head
    lastodd, lasteven, curr = head, head.next, head.next.next
    while curr:
      # lastodd = 1, lasteven = 2, curr = 3
      # temp = 2
      temp = lastodd.next
      # 1 -> 3
      lastodd.next = curr
      # curr = 4
      curr = curr.next
      # lastodd = 3
      lastodd = lastodd.next
      # 3 -> 2
      lastodd.next = temp
      # 2 -> 4
      lasteven.next = curr
      # we stop if we can't advance
      if not curr or not curr.next:
        return head
      # curr = 5
      curr = curr.next
      # lasteven = 4
      lasteven = lasteven.next
    return head
      
    

