# https://leetcode.com/problems/keys-and-rooms

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        vis = set()
        stack = [0]
        while stack:
            r = stack.pop()
            vis.add(r)
            for k in rooms[r]:
                if k not in vis:
                    stack.append(k)
        return len(vis) == len(rooms)