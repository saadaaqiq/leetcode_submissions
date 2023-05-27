# https://leetcode.com/problems/sum-root-to-leaf-numbers

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(node, cur):
            nonlocal res
            x = cur * 10 + node.val
            if not node.left and not node.right:
                res += x
            else:
                if node.left:
                    dfs(node.left, x)
                if node.right:
                    dfs(node.right, x)

        dfs(root, 0)
        return res