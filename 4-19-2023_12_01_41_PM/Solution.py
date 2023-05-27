# https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:

        def dfs(node):
            if not node: 
                return 0, 0, 0
            lx, ly, lm = dfs(node.left)
            rx, ry, rm = dfs(node.right)
            return 1 + ly, 1 + rx, max(lx, ry, lm, rm)

        return max(dfs(root)) - 1
            





                
            