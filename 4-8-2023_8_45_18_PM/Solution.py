# https://leetcode.com/problems/clone-graph

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        clone = Node(node.val)
        q = collections.deque([(node, clone)])
        dic = {node: clone}
        while q:
            x, y = q.popleft()
            for xx in x.neighbors:
                if xx not in dic:
                    dic[xx] = Node(xx.val)
                    q.append((xx, dic[xx]))
                y.neighbors.append(dic[xx])
        return clone