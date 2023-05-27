# https://leetcode.com/problems/path-sum

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
    
    def path(node, s):
      return node and ((not node.right and not node.left and s + node.val == targetSum) or path(node.right, s + node.val) or path(node.left, s + node.val))
      
    return path(root, 0)