# https://leetcode.com/problems/swap-nodes-in-pairs

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, node: Optional[ListNode]) -> Optional[ListNode]:
        if not node or not node.next:
            return node
        temp = node.next
        node.next = self.swapPairs(temp.next)
        temp.next = node
        return temp
    