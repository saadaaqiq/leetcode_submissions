# https://leetcode.com/problems/validate-binary-search-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        q = deque([(root, -float("infinity"), float("infinity"))])
        while q:
            node, mini, maxi = q.popleft()
            if node.val <= mini or node.val >= maxi:
                return False
            if node.left:
                q.append((node.left, mini, min(maxi, node.val)))
            if node.right:
                q.append((node.right, max(node.val, mini), maxi))
        return True
            