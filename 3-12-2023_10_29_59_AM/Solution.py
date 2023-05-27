# https://leetcode.com/problems/merge-k-sorted-lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        c = 0
        for head in lists:
            if head:
                heapq.heappush(heap, (head.val, c, head))
                c += 1
        first = ListNode()
        cur = first
        while heap:
            v, ind, node = heapq.heappop(heap)
            cur.next = node
            cur = cur.next
            if node.next:
                heapq.heappush(heap, (node.next.val, ind, node.next))
        return first.next
