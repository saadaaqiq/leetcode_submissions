# https://leetcode.com/problems/clone-graph

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        existing = {}
        return self.subClone(node, existing)
        
    def subClone(self, node, existing):
        if not node:
            return None
        clone = Node(node.val, [])
        
        if node.val not in existing:
            existing[clone.val]=clone
        else:
            return existing[clone.val]
            
        if not node.neighbors:
            return clone
        for neighbor in node.neighbors:
            if neighbor.val in existing:
                clone.neighbors.append(existing[neighbor.val])
            else:
                clone.neighbors.append(self.subClone(neighbor, existing))
        return clone      
