# https://leetcode.com/problems/clone-binary-tree-with-random-pointer

# Definition for Node.
# class Node:
#     def __init__(self, val=0, left=None, right=None, random=None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.random = random
class Solution:
  def copyRandomBinaryTree(self, root):
    if not root: return None
    dic = {}
    notYet = []
    def cloner(node):
      if node in dic:
        return dic[node]
      clone = NodeCopy(node.val)
      dic[node] = clone
      if node.left:
        clone.left = cloner(node.left)
      if node.right:
        clone.right = cloner(node.right)
      if node.random in dic:
        clone.random = dic[node.random]
      else:
        notYet.append((clone, node.random))
      return clone
    rClone = cloner(root)
    for (clone, random) in notYet:
      clone.random = dic[random] if random in dic else None
    return rClone
      
      