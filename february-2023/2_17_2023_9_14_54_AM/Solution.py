# https://leetcode.com/problems/minimum-distance-between-bst-nodes

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        res = float("inf")
        def dfs(node):
            nonlocal res
            mini, maxi = node.val, node.val
            if node.left:
                min_left, max_left = dfs(node.left)
                if max_left < node.val:
                    res = min(res, node.val - max_left)
                mini = min(mini, min_left)
            if node.right:
                min_right, max_right = dfs(node.right)
                if min_right > node.val:
                    res = min(res, min_right - node.val)
                maxi = max(maxi, max_right)
            return (mini, maxi)
        dfs(root)
        return res

