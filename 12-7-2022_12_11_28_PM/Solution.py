# https://leetcode.com/problems/kth-smallest-element-in-a-bst

class Solution:
    def kthSmallest(self, root, k):
        
        stack = []
        
        while True:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if not k:
                return root.val
            root = root.right

            
            
            
            

