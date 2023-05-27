# https://leetcode.com/problems/symmetric-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        q = collections.deque([(root, root)])
        while q:
            node1, node2 = q.popleft()
            if not node1 and not node2:
                continue
            if (node1 and not node2) or (node2 and not node1) or node1.val != node2.val:
                return False
            q.append((node1.left, node2.right))
            q.append((node1.right, node2.left))
        return True
