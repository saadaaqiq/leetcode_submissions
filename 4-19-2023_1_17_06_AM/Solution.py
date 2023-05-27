# https://leetcode.com/problems/remove-nth-node-from-end-of-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        arr = []
        cur = head
        while cur:
            arr.append(cur)
            cur = cur.next
        n = len(arr)
        if 0 == n - k:
            return head.next
        elif k == 1:
            arr[-2].next = None
            return head
        else:
            arr[n-k-1].next = arr[n-k+1]
            return head
            
