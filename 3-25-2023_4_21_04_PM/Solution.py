# https://leetcode.com/problems/check-completeness-of-a-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:

        q = collections.deque([root])
        empty = False

        while q:
            node = q.popleft()
            if not node:
                empty = True
                continue
            else:
                if empty:
                    return False
                q.append(node.left)
                q.append(node.right)

        return True                    