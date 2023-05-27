# https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        
        dic = {}
        for c1, c2, d in roads:
          if c1 not in dic:
            dic[c1] = []
          if c2 not in dic:
            dic[c2] = []
          dic[c1].append((c2, d))
          dic[c2].append((c1, d))
        
        res = float("infinity")
        
        def dfs(city, score):
          nonlocal res
          res = min(res, score)
          if city in dic:
            while dic[city]:
              c,d = dic[city].pop()
              dfs(c, min(score,d))        

        dfs(1, float("infinity"))
        return res          
        
