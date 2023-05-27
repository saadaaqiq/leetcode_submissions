# https://leetcode.com/problems/merge-k-sorted-lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for i, head in enumerate(lists):
            j = 0
            node = head
            while node:
                heapq.heappush(heap, (node.val, i, j, node))
                j += 1
                node = node.next
        curr = ListNode()
        head = curr
        while heap:
            v, i, j, n = heapq.heappop(heap)
            curr.next = n
            curr = curr.next
        return head.next