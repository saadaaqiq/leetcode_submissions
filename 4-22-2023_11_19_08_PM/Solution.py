# https://leetcode.com/problems/house-robber-iii

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:

        def dfs(node):
            if not node: return 0, 0
            r = node.val
            (lr, ls), (rr, rs) = dfs(node.left), dfs(node.right)
            return r + ls + rs, max(lr + rr, lr + rs, ls + rr, ls + rs)
        
        root_rob, root_skip = dfs(root)
        return max(root_rob, root_skip)
