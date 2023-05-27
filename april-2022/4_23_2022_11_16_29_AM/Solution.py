# https://leetcode.com/problems/clone-graph

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        existing = {}
        return self.subClone(node, existing)
    def subClone(self, node: 'Node', existing) -> 'Node': 
        if not node:
            return None
        clone = Node(node.val, [])
        if node.val not in existing:
            existing[node.val] = clone
        else:
            return clone
        if node.neighbors:
            for neighbor in node.neighbors:
                if neighbor.val not in existing:
                    clone.neighbors.append(self.subClone(neighbor, existing))
                else:
                    clone.neighbors.append(existing[neighbor.val])
        return clone