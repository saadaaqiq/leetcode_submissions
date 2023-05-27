# https://leetcode.com/problems/subtree-of-another-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    
    def check(p, q):
      if not p and not q: 
        return True
      if p and not q:
        return False
      if q and not p:
        return False
      if p.val != q.val:
        return False
      if not check(p.left, q.left):
        return False
      if not check(p.right, q.right):
        return False
      return True
    
    def dfs(p, q):
      if check(p,q) or (p and dfs(p.left, q)) or (p and dfs(p.right, q)):
        return True
      return False
    
    return dfs(root, subRoot)