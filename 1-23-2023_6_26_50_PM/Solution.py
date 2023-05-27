# https://leetcode.com/problems/partition-labels

class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        dic = { i: [-1, -1] for i in range(26) }

        for i, c in enumerate(s):
            x = ord(c)-97
            if dic[x][0] == -1:
                dic[x][0] = i
            dic[x][1] = i
        
        intervals = list(dic.values())
        intervals.sort()
        res = []
        for a, b in intervals:
            if a == -1:
                continue
            if not res or a > res[-1][1]:
                res.append([a,b])
            else:
                res[-1][0], res[-1][1] = min(res[-1][0], a), max(res[-1][1], b)
        return [I[1]-I[0]+1 for I in res]
                
                
            
