# https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list

"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
  def treeToDoublyList(self, root):
    if not root: return None
    def dfs(node):
      hl, tl, hr, tr = node, node, node, node
      if node.left:
        hl,tl = dfs(node.left)
        tl.right = node
        node.left = tl
      if node.right:
        hr, tr = dfs(node.right)
        node.right = hr
        hr.left = node
      return (hl, tr)
    
    h, t = dfs(root)
    t.right = h
    h.left = t
    
    return h
      