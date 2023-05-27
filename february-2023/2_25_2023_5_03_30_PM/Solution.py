# https://leetcode.com/problems/binary-tree-preorder-traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        res = []

        def preorder(root):
            cur = root
            stack = []
            while stack or cur:
                if cur:
                    res.append(cur.val)
                    stack.append(cur.right)
                    cur = cur.left
                else:
                    cur = stack.pop()
        
        preorder(root)
        return res
