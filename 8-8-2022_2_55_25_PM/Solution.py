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
    arr = deque([[] for i in range(201)])
    q = deque()
    q.append((root,0))
    while q:
      node, col = q.popleft()
      arr[100+col].append(node.val)
      if node.left:
        q.append((node.left, col-1))
      if node.right:
        q.append((node.right, col+1))
    while not arr[0]:
      arr.popleft()
    while not arr[-1]:
      arr.pop()
    return list(arr)