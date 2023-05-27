# https://leetcode.com/problems/clone-binary-tree-with-random-pointer

# Definition for Node.
# class Node:
#     def __init__(self, val=0, left=None, right=None, random=None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.random = random

class NodeCopy:
  def __init__(self, val=0, left=None, right=None, random=None):
    self.val = val
    self.left = left
    self.right = right
    self.random = random

class Solution:
  def copyRandomBinaryTree(self, root):
    if not root:
      return None
    
    node_address_to_clone = {}    
    
    def cloneNode(node):
      clone = NodeCopy(node.val)
      node_address_to_clone[id(node)] = clone
      if node.left:
        clone.left = cloneNode(node.left)
      if node.right:
        clone.right = cloneNode(node.right)
      return clone
  
    clone_root = cloneNode(root)
    
    stack = [(root, clone_root)]
    
    while stack:
      node, clone = stack.pop()
      clone.random = None
      if node.random and id(node.random) in node_address_to_clone:
        clone.random = node_address_to_clone[id(node.random)]
      if node.left:
        stack.append((node.left, clone.left))
      if node.right:
        stack.append((node.right, clone.right))
    
    return clone_root  
      
