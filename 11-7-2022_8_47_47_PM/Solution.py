# https://leetcode.com/problems/linked-list-cycle

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        slow, fast = head, head
        while slow and fast:
            if not slow.next or not fast.next or not fast.next.next:
                return False
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return Fast