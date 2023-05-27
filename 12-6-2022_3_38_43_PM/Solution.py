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
        q = deque([(root, 0)])
        arr = []
        while q:
            node, level = q.popleft()
            arr.append((node, level))
            if node.left:
                q.append((node.left, level+1))
            if node.right:
                q.append((node.right, level+1))
        res = [[] for _ in range(arr[-1][1]+1)]
        for node, level in arr:
            res[level].append(node.val)
        return res