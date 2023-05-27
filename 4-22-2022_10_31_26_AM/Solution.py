# https://leetcode.com/problems/merge-two-sorted-lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, head1: Optional[ListNode], head2: Optional[ListNode]) -> Optional[ListNode]:
        if not head1 or not head2:
            return head1 or head2
        if head1.val < head2.val:
            head1.next = self.mergeTwoLists(head1.next, head2)
            return head1
        else:
            head2.next = self.mergeTwoLists(head1, head2.next)
            return head2
            
        