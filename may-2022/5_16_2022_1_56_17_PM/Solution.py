# https://leetcode.com/problems/binary-tree-level-order-traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
  
  def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    res = []
    
    if not root:
      return res 
        
    q = deque()
    q.append(root)
    
    ls = 1
    c = 0
    level = []
    while q:
      node = q.popleft()
      level.append(node.val)
      ls -= 1
      if node.left:
        c+=1
        q.append(node.left)
      if node.right:
        c+=1
        q.append(node.right)
      if ls == 0:
        res.append(level)
        level = []
        ls = c
        c = 0
        
    return res