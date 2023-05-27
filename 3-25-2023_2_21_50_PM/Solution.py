# https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sortedListToBST(self, h):

        if not h:
            return None
        if not h.next:
            return TreeNode(h.val)
            
        prev = ListNode()
        prev.next = h
        slow, fast = h, h
        while fast and fast.next:
            prev = prev.next
            slow = slow.next
            fast = fast.next.next
        prev.next = None
        
        node = TreeNode(slow.val)
        node.left = self.sortedListToBST(h)
        node.right = self.sortedListToBST(slow.next)

        return node

