# https://leetcode.com/problems/kth-smallest-element-in-a-bst

class Solution:
    def kthSmallest(self, root, k):
        arr = []

        def dfs(node):
            if node.left: dfs(node.left)
            arr.append(node.val)
            if node.right: dfs(node.right)

        dfs(root)
        return arr[k-1]
            
            
            
            

