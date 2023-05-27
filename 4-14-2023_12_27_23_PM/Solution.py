# https://leetcode.com/problems/degree-of-an-array

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        dic = {}
        for i, x in enumerate(nums):
            if x not in dic:
                dic[x] = [i, -1, 1]
            else:
                dic[x][1] = i
                dic[x][2] += 1
        max_freq = 1
        res = 1
        for k in dic:
            l, r, f = dic[k]
            if r!=-1 and (f > max_freq or (f == max_freq and r-l+1 < res)):
                max_freq = f
                res = r-l+1
        return res
