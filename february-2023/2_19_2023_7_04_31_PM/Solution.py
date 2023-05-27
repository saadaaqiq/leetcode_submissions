# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal

class Solution:
    def zigzagLevelOrder(self, root):
        if not root:
            return []
        arr = []
        q = collections.deque([(root, 0)])
        while len(q) > 0:
            node, depth = q.popleft()
            if depth >= len(arr):
                if arr and len(arr) % 2 == 0:
                    arr[-1].reverse()
                arr.append([])
            arr[-1].append(node.val)
            if node.left:
                q.append((node.left, depth+1))
            if node.right:
                q.append((node.right, depth+1))
        if arr and len(arr) % 2 == 0:
            arr[-1].reverse()
        return arr
                