# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: 
            return []
        arr = []
        q = deque([(root,0)])
        maxlevel = 0
        while q:
            node, level = q.popleft()
            maxlevel = max(maxlevel, level)
            arr.append((node.val, level))
            if node.left: q.append((node.left, level+1))
            if node.right: q.append((node.right, level+1))
        res = [deque() for i in range(maxlevel+1)]
        for v, level in arr:
            if level%2==0:
                res[level].append(v)
            else:
                res[level].appendleft(v)
        for i in range(len(res)):
            res[i] = list(res[i])
        return res

                