# https://leetcode.com/problems/binary-search-tree-iterator

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = [root]
        self.vis = set()

    def next(self) -> int:
        print([node.val for node in self.stack])
        
        while self.stack[-1].val not in self.vis:
            x = self.stack.pop()
            l,r = x.left, x.right
            if r:
                self.stack.append(r)
            self.vis.add(x.val)
            self.stack.append(x)
            if l:
                self.stack.append(l)
        return self.stack.pop().val
        

    def hasNext(self) -> bool:
        return len(self.stack) > 0
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()