# https://leetcode.com/problems/construct-binary-tree-from-string

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def str2tree(self, s: str) -> Optional[TreeNode]:
        
        if not s:
            return None
    
        stack = []
        for i in range(len(s)-1, -1, -1):
            stack.append(s[i])
        
        def get_num():
            tab = []
            while stack and (stack[-1].isnumeric() or stack[-1] == "-"):
                tab.append(stack.pop())
            return TreeNode(int(''.join(tab)))
        
        root = get_num()

        curr = root
        prevs = []

        while stack:
            if stack[-1] == '(':
                stack.pop()
                prevs.append(curr)
                if not curr.left:
                    curr.left = get_num()
                    curr = curr.left
                elif not curr.right:
                    curr.right = get_num()
                    curr = curr.right
                else:
                    prevs.pop()
            elif stack[-1] == ')':
                stack.pop()
                curr = prevs.pop()

        return root
                









