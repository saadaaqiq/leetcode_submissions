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
      s, t = [p], [q]
      while s and t:
        n1, n2 = s.pop(), t.pop()
        if (n1 and not n2) or (n2 and not n1) or (n1 and n2 and n1.val != n2.val):
          return False
        if not n1 and not n2:
          continue
        s.append(n1.left)
        t.append(n2.left)
        s.append(n1.right)
        t.append(n2.right)
      return True
          
          
    def dfs(node, sub):
      if (node.val==sub.val and areEqual(node,sub)) or (node.left and dfs(node.left,sub)) or (node.right and dfs(node.right,sub)):
        return True
      return False
    
    return dfs(root, subRoot)