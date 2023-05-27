# https://leetcode.com/problems/validate-binary-search-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(node, mini, maxi):
            if not node:
                return True
            if node.val >= maxi or node.val <= mini:
                return False
            return dfs(node.left, mini, min(node.val, maxi)) and dfs(node.right, max(node.val, mini), maxi)
        
        return dfs(root, -float("infinity"), float("infinity"))
