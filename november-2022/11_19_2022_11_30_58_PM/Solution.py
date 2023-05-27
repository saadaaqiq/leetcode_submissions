# https://leetcode.com/problems/populating-next-right-pointers-in-each-node

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        q = deque([(root, None)])
        while q:
            node, target = q.popleft()
            node.next = target
            if node.right:
                q.append((node.right, target.left if target else None))
            if node.left:
                q.append((node.left, node.right))
        return root