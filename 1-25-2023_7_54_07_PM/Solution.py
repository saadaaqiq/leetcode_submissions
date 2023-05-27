# https://leetcode.com/problems/find-closest-node-to-given-two-nodes

class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:

        vis1 = set()
        vis2 = set()

        q = deque([(node1, node2)])

        while q:
            a, b = q.popleft()
            if a == b:
                return a
            if a in vis2 and b not in vis1:
                return a
            elif a not in vis2 and b in vis1:
                return b
            elif a in vis2 and b in vis1:
                return min(a,b)
            vis1.add(a)
            vis2.add(b)
            x = -1
            y = -1
            if edges[a] != -1 and edges[a] not in vis1:
                x = edges[a]
            if edges[b] != -1 and edges[b] not in vis2:
                y = edges[b]
            if x >= 0 and y >= 0:
                q.append((x, y))
            elif x >= 0 and y < 0:
                q.append((x, b))
            elif x < 0 and y >= 0:
                q.append((a, y))
            else:
                return -1
        return -1