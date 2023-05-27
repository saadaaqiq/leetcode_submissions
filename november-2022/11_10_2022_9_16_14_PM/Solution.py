# https://leetcode.com/problems/reorder-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        arr = []
        curr = head
        while curr:
            arr.append(curr)
            curr = curr.next
        l, r = 0, len(arr)-1
        last = ListNode()
        while l < r:
            last.next = arr[l]
            arr[l].next = arr[r]
            last = arr[r]
            l += 1
            r -= 1
        if l == r:
            last.next = arr[l]
            last = last.next
        last.next = None
