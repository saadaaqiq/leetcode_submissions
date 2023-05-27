# https://leetcode.com/problems/merge-k-sorted-lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
  def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    newList = [(n.val, id(n), n) for n in lists if n]
    heapq.heapify(newList)
    res = ListNode()
    p = res
    while newList:
      v,iD,n = heapq.heappop(newList)
      p.next = n
      p = p.next
      if n.next:
        heapq.heappush(newList, (n.next.val, id(n.next), n.next))
    return res.next