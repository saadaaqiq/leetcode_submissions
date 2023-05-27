# https://leetcode.com/problems/path-sum

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
    
    def dfs(node, s):
      if not node:
        return False
      if not node.left and not node.right and s+node.val == targetSum:
        return True
      if node.left:
        if dfs(node.left, s+node.val):
          return True
      if node.right:
        if dfs(node.right, s+node.val):
          return True
      return False
    
    return dfs(root, 0)