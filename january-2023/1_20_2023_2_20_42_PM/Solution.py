# https://leetcode.com/problems/diameter-of-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        def dfs(node):
            nonlocal res
            l, r = 0, 0
            if node.left:
                l += dfs(node.left) + 1
            if node.right:
                r += dfs(node.right) + 1
            res = max(res, l+r)
            return max(l, r)
        dfs(root)
        return res