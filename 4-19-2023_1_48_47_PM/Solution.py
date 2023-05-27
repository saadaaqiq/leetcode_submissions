# https://leetcode.com/problems/odd-even-linked-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        xi, yi = head, head.next
        x0, y0 = head, head.next
        xf, yf = head, head.next
        while True:
            if xi:
                xf = xi
            if yi:
                yf = yi
            if xi:
                xi.next = xi.next.next if xi.next else None
                xi = xi.next
            if yi:
                yi.next = yi.next.next if yi.next else None
                yi = yi.next
            if not xi:
                break
        xf.next = y0
        return x0
        



