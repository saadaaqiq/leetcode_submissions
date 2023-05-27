# https://leetcode.com/problems/binary-tree-pruning

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    
    top = TreeNode(1, None, root)

    def dfs(node):
      if not node:
        return False
      if node.val == 1:
        if node.right and not dfs(node.right):
          node.right = None
        if node.left and not dfs(node.left):
          node.left = None
        return True
      if node.val == 0:
        if not node.right and not node.left:
          return False
        l, r = not not node.left, not not node.right
        if r and not dfs(node.right):
          node.right = None
          r = False
        if l and not dfs(node.left):
          node.left = None
          l = False
        return l or r
      
    dfs(top)
    return top.right
    