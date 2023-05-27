# https://leetcode.com/problems/binary-tree-maximum-path-sum

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
  def maxPathSum(self, root: Optional[TreeNode]) -> int:
    
    res = root.val
    
    def dfs(node):
      if node.left and node.right:
        return node.val + max(0, dfs(node.left), dfs(node.right))
      elif node.right:
        return node.val + max(0, dfs(node.right))
      elif node.left:
        return node.val + max(0, dfs(node.left))
      else:
        return node.val
    
    stack = []
    stack.append(root)
    while stack:
      node = stack.pop()
      if node.left and node.right:
        l = dfs(node.left)
        r = dfs(node.right)
        v = node.val
        res = max(res, l+r+v, l+v, r+v, l, r)
        stack.append(node.left)
        stack.append(node.right)
      elif node.left and not node.right:
        l = dfs(node.left)
        v = node.val
        res = max(res, l+v, l)
        stack.append(node.left)
      elif node.right and not node.left:
        r = dfs(node.right)
        v = node.val
        res = max(res, r+v, r)
        stack.append(node.right)
        
    return res