# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        A, B = [], []
        def dfs(n,t,a):
            if n == t: 
                a.append(t)
                return True
            if n.left:
                a.append(n)
                if dfs(n.left, t, a): 
                    return True
                a.pop()
            if n.right:
                a.append(n)
                if dfs(n.right, t, a):
                    return True
                a.pop()
            return False
        dfs(root, p, A)
        dfs(root, q, B)
        A, B = list(reversed(A)), list(reversed(B))
        print([node.val for node in A])
        print([node.val for node in B])
        while A and B and A[-1] == B[-1]:
            anc = A.pop()
            B.pop()
            if not A or not B or A[-1]!=B[-1]:
                return anc
        
