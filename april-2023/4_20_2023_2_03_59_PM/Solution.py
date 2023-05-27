# https://leetcode.com/problems/maximum-width-of-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        q = collections.deque([(root, 0, 0)])
        arr = []
        while q:
            node, l, p = q.popleft()
            if l >= len(arr):
                arr.append([inf, -inf])
            arr[-1][0] = min(arr[-1][0], p)
            arr[-1][1] = max(arr[-1][1], p)
            if node.left:
                q.append((node.left, l+1, 2*p))
            if node.right:
                q.append((node.right, l+1, 2*p+1))
        return max([r-l+1 for (l,r) in arr])


            