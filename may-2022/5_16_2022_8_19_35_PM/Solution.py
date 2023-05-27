# https://leetcode.com/problems/subtree-of-another-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    
    def areEqual(p,q):
      if not p and not q:
        return True
      if (p and not q) or \
          (q and not p) or \
          (p.val != q.val) or \
          (not areEqual(p.left, q.left)) or \
          (not areEqual(p.right, q.right)):
        return False
      return True
    
    def dfs(node, sub):
      if (node.val==sub.val and areEqual(node,sub)) or (node.left and dfs(node.left,sub)) or (node.right and dfs(node.right,sub)):
        return True
      return False
    
    return dfs(root, subRoot)