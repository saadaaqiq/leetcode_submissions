# https://leetcode.com/problems/binary-tree-vertical-order-traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    if not root: return []
    dic = {}
    q = deque()
    q.append((root,0))
    while q:
      node, col = q.popleft()
      if col not in dic:
        dic[col] = []
      dic[col].append(node.val)
      if node.left:
        q.append((node.left, col-1))
      if node.right:
        q.append((node.right, col+1))
    res = []
    for k in sorted(dic.keys()):
      res.append(dic[k])
    return res