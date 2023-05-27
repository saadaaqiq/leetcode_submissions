# https://leetcode.com/problems/sum-of-left-leaves

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        somme = 0
        
        q = deque()
        q.append(root)
        while q:
            n = q.popleft()
            if n.left:
                if not n.left.left and not n.left.right:
                    somme += n.left.val
                else:
                    q.append(n.left)
            if n.right:
                q.append(n.right)
        
        return somme