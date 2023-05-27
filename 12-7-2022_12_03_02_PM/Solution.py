# https://leetcode.com/problems/kth-smallest-element-in-a-bst

class Solution:
    def kthSmallest(self, root, k):
        c = 0

        def dfs(node):
            nonlocal c
            if node.left: 
                l = dfs(node.left)
                if l >= 0:
                    return l
            c += 1
            if c == k:
                return node.val
            if node.right: 
                r = dfs(node.right)
                if r >= 0:
                    return r
            return -1

        return dfs(root)

            
            
            
            

