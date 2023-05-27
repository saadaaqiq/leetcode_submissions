# https://leetcode.com/problems/partition-labels

class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        dic = {}

        for i, c in enumerate(s):
            x = ord(c)-97
            if x not in dic:
                dic[x] = [i, i]
            else:
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
                
                
            
