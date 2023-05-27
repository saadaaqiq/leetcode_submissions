# https://leetcode.com/problems/find-root-of-n-ary-tree

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
  def findRoot(self, tree: List['Node']) -> 'Node':
    dic = { node.val: node for node in tree }
    for node in tree:
      if node.children:
        for child in node.children:
          if child.val in dic:
            dic.pop(child.val)
    return dic.popitem()[1]