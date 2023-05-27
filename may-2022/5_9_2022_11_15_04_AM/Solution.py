# https://leetcode.com/problems/symmetric-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(direction):
            s = []
            s.append(root)
            res = []
            while s:
                n = s.pop()
                res.append(n.val if n else "null")
                if n:
                    s.append(n.left if direction else n.right)
                    s.append(n.right if direction else n.left)
            return res
        
        return dfs(True) == dfs(False)
            