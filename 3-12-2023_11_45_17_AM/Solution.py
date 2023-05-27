# https://leetcode.com/problems/linked-list-cycle-ii

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next or not head.next.next:
            return None
        slow, fast = head.next, head.next.next
        while slow and fast and fast.next and slow != fast:
            slow, fast = slow.next, fast.next.next        
        if not fast or not fast.next:
            return None
        cur = head
        k = 0
        while cur != slow:
            k += 1
            cur = cur.next
            slow = slow.next
        return cur