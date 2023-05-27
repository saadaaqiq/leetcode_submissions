# https://leetcode.com/problems/clone-n-ary-tree

"""
class Node:
  def __init__(self, val=None, children=None):
    self.val = val
    self.children = children if children is not None else []
"""

class Solution:
  def cloneTree(self, node: 'Node') -> 'Node':
    if not node: return None
    nClone = Node(node.val)
    if node.children:
      nClone.children = []
      for child in node.children:
        nClone.children.append(self.cloneTree(child))
    return nClone
    
