# https://leetcode.com/problems/clone-graph

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        clone = Node(node.val)
        q = collections.deque([(node, clone)])
        dic = {}
        while q:
            cur, cur_clone = q.popleft()
            dic[cur] = cur_clone
            for neighbor in cur.neighbors:
                if neighbor not in dic:
                    neighbor_clone = Node(neighbor.val)
                    cur_clone.neighbors.append(neighbor_clone)
                    dic[neighbor] = neighbor_clone
                    q.append((neighbor, neighbor_clone))
                else:
                    cur_clone.neighbors.append(dic[neighbor])
                
        return clone







