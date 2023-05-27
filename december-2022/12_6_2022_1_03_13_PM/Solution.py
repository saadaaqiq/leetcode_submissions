# https://leetcode.com/problems/invert-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        q = deque()
        q.append(root)
        while q:
            node = q.popleft()
            if node.left and node.right:
                temp = node.left
                node.left = node.right
                node.right = temp
            elif node.left and not node.right:
                node.right = node.left
                node.left = None
            elif node.right and not node.left:
                node.left = node.right
                node.right = None
            
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return root