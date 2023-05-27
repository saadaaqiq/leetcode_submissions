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
  def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
    if not root:
      return None
    
    arr = []
    
    def dfs(node):
      if node.left: dfs(node.left)
      arr.append(node)
      if node.right: dfs(node.right)
    
    dfs(root)
        
    for i in range(len(arr)):
      arr[i].left = arr[i-1]
      arr[i].right = arr[(i+1)%len(arr)]
      
    return arr[0]
      