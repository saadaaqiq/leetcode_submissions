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
            prev, curr = 0, node.val
            pvl, vl, pvr, vr = 0, 0, 0, 0
            if node.left: 
                pvl, vl = dfs(node.left)
            if node.right: 
                pvr, vr = dfs(node.right)
            curr = max(node.val + pvl + pvr, vl + vr)
            prev = vl + vr
            return [prev, curr]
        
        return dfs(root)[1]
        
            
            
