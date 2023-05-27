# https://leetcode.com/problems/dota2-senate

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        dire, radiant = [], []
        for i, t in enumerate(senate):
            if t == "R":
                heapq.heappush(radiant, i)
            else:
                heapq.heappush(dire, i)    
        while dire and radiant:
            if dire[0] < radiant[0]:
                cur = heapq.heappop(dire)
                heapq.heappush(dire, cur + 10001)
                heapq.heappop(radiant)
            else:
                cur = heapq.heappop(radiant)
                heapq.heappush(radiant, cur + 10001)
                heapq.heappop(dire)
        return "Dire" if dire else "Radiant"