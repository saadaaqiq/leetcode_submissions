# https://leetcode.com/problems/serialize-and-deserialize-binary-tree

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None



class Codec:

    def serialize(self, root):
        if not root:
            return ""
        dic = {}
        q = deque([(root, 0)])
        while q:
            node, level = q.popleft()
            if level not in dic:
                dic[level] = []
            dic[level].append(str(node.val) if node else ".")
            if node:
                q.append((node.left, level+1))
                q.append((node.right, level+1))
        s = ""
        i = 0
        while i+1 in dic:
            for j in range(len(dic[i])):
                s += dic[i][j] + ","
            i += 1
        return s + "x"
        

    def deserialize(self, data):
        if not data:
            return None
        level = data.split(",")
        level.pop()
        for i in range(len(level)):
            if level[i] == ".":
                level[i] = None
            else:
                level[i] = TreeNode(int(level[i]))
        root = level[0]
        i, l, r = 0, 1, 2
        while i < len(level):
            level[i].left = level[l] if l < len(level) else None
            l += 2
            level[i].right = level[r] if r < len(level) else None
            r += 2
            i += 1
            while i < len(level) and not level[i]:
                i += 1
        return root
        



        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))