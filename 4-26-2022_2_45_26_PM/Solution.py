# https://leetcode.com/problems/merge-intervals

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        l = len(intervals) - 1
        if l <= 0: 
            return intervals
        its = sorted(intervals, key=lambda x: x[0])
        
        i = 0
        j = 1
        while j <= l:
            if its[i][1]>=its[j][0]:
                its[j][0] = its[i][0]
                if its[i][1]>its[j][1]:
                    its[j][1] = its[i][1]
                del its[i]
                l = len(its)-1
            else:
                i+=1
                j+=1
                
        return its