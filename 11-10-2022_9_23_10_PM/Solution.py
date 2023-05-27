# https://leetcode.com/problems/reorder-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        q, curr = deque(), head
        while curr:
            q.append(curr)
            curr = curr.next
        b, prev = False, q.popleft()
        while q:
            prev.next = q.popleft() if b else q.pop()
            b, prev = not b, prev.next
        prev.next = None
        return head