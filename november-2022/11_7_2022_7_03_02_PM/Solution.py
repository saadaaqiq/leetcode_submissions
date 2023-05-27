# https://leetcode.com/problems/binary-tree-level-order-traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = [[] for i in range(2000)]
        def dfs(node, level):
            res[level].append(node.val)
            if node.left:
                dfs(node.left, level+1)
            if node.right:
                dfs(node.right, level+1)
        dfs(root, 0)
        while not res[-1]:
            res.pop()
        return res