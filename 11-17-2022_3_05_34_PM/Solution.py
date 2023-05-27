# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):

        anc_p, anc_q = [], []

        def dfs(node, path, goal):
            if node == goal:
                return path + [node]
            if node.left:
                arr1 = dfs(node.left, path + [node], goal)
                if arr1:
                    return arr1
            if node.right:
                arr2 = dfs(node.right, path + [node], goal)    
                if arr2:
                    return arr2
            return []

        anc_p = dfs(root, [], p)
        anc_q = dfs(root, [], q)

        print([node.val for node in anc_p])
        print([node.val for node in anc_q])

        i, j = 0, 0

        while i < len(anc_p)-1 and j < len(anc_q)-1 and anc_p[i] == anc_q[j] and anc_p[i+1]==anc_q[j+1]:
            i += 1
            j += 1
        
        return anc_p[i]
        
