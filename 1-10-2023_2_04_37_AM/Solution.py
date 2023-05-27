# https://leetcode.com/problems/same-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack = [(p,q)]
        while stack:
            a, b = stack.pop()
            if (a and not b) or (b and not a) or (a and b and a.val!=b.val):
                return False
            if a and b:
                stack.append((a.left, b.left))
                stack.append((a.right, b.right))
        return True