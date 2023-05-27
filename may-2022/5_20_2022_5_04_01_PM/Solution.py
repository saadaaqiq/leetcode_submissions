# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

  def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    
    p_ancestors = []
    q_ancestors = []
    
    def dfs(node, p, q, isP):
      if isP:
        if p.val > node.val:
          if node.right:
            p_ancestors.append(node)
            dfs(node.right, p, q, True)
        elif p.val < node.val:
          if node.left:
            p_ancestors.append(node)
            dfs(node.left, p, q, True)
        else:
          p_ancestors.append(node)
      if not isP:
        if q.val > node.val:
          if node.right:
            q_ancestors.append(node)
            dfs(node.right, p, q, False)
        elif q.val < node.val:
          if node.left:
            q_ancestors.append(node)
            dfs(node.left, p, q, False)
        else:
          q_ancestors.append(node)
          
    dfs(root, p, q, False)
    dfs(root, p, q, True)
    
    s = set( [ i.val for i in p_ancestors ] )
    k = len(q_ancestors) - 1
    while k>=0:
      if q_ancestors[k].val in s:
        return q_ancestors[k]
      k-=1
