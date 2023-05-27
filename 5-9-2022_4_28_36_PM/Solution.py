# https://leetcode.com/problems/invert-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def bfs(node):
            q = deque()
            q.append(node)
            while q:
                n = q.popleft()
                if n:
                    tempL = n.left
                    tempR = n.right
                    n.left = tempR
                    n.right = tempL
                    if n.left:
                        q.append(n.left)
                    if n.right:
                        q.append(n.right)
        
        bfs(root)
        return root
                
                    
                    