# https://leetcode.com/problems/balanced-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def isBalanced(self, root: Optional[TreeNode]) -> bool:
    
    def compare(node):
      if not node:
        return 0
      lsub, rsub = 1 + compare(node.left), 1 + compare(node.right)
      if lsub == 0 or rsub == 0 or abs(lsub-rsub) > 1:
        return -1
      return max(lsub, rsub)
    
    return compare(root) >= 0
      