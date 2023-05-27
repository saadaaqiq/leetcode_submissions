# https://leetcode.com/problems/partition-labels

class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        last = {c: i for (i,c) in enumerate(s)}

        res = []
        last_char = 0

        for i,c in enumerate(s):
            if res and i < last_char + res[-1]:
                res[-1] = max(res[-1], last[c]-last_char+1)
            else:
                res.append(last[c]-i+1)
                last_char = i
        
        return res
