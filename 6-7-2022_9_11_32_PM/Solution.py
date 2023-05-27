# https://leetcode.com/problems/number-of-good-leaf-nodes-pairs

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def countPairs(self, root: TreeNode, distance: int) -> int:
    c = [0]
    def echo(node):
      leftDistances = []
      rightDistances = []
      if not node.left and not node.right:
        return [1]
      if node.left:
        leftDistances += echo(node.left)
      if node.right:
        rightDistances += echo(node.right)
      for l in leftDistances:
        for r in rightDistances:
          if l + r <= distance:
            c[0] += 1
      return [ x+1 for x in (leftDistances + rightDistances) ]
    echo(root)
    return c[0]
          